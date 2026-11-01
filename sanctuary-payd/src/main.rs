mod catalog;

use axum::{
    body::{Body, Bytes},
    extract::{Path, Query, State},
    http::{header, HeaderMap, StatusCode},
    response::{IntoResponse, Response},
    routing::{get, post},
    Json, Router,
};
use catalog::{build_verified_catalog, BookEntry};
use hmac::{Hmac, Mac};
use serde::{Deserialize, Serialize};
use sha2::{Digest, Sha256};
use std::{
    collections::HashMap,
    env,
    net::SocketAddr,
    path::PathBuf,
    sync::Arc,
    time::{SystemTime, UNIX_EPOCH},
};
use subtle::ConstantTimeEq;
use tokio::fs;

type HmacSha256 = Hmac<Sha256>;

#[derive(Clone)]
struct AppState {
    stripe_webhook_secret: Vec<u8>,
    revolut_webhook_secret: Vec<u8>,
    paypal_webhook_token: Vec<u8>,
    download_signing_key: Vec<u8>,
    vault_dir: PathBuf,
    public_base_url: String,
    catalog: Arc<HashMap<String, BookEntry>>,
}

#[derive(Deserialize)]
struct UnlockQuery {
    token: String,
}

#[derive(Deserialize)]
struct CommonsClaimRequest {
    book_id: String,
}

#[derive(Serialize)]
struct CapabilityGrant {
    status: &'static str,
    book_id: String,
    title: String,
    sha256_seal: String,
    download_url: String,
    expires_at_unix: u64,
    mantra: &'static str,
}

#[tokio::main]
async fn main() {
    let catalog = build_verified_catalog();

    let state = AppState {
        stripe_webhook_secret: env::var("STRIPE_WEBHOOK_SECRET")
            .unwrap_or_else(|_| "whsec_dev_placeholder".into())
            .into_bytes(),
        revolut_webhook_secret: env::var("REVOLUT_WEBHOOK_SECRET")
            .unwrap_or_else(|_| "rev_dev_placeholder".into())
            .into_bytes(),
        paypal_webhook_token: env::var("PAYPAL_WEBHOOK_TOKEN")
            .unwrap_or_else(|_| "pp_dev_placeholder".into())
            .into_bytes(),
        download_signing_key: env::var("DOWNLOAD_SIGNING_KEY")
            .expect("DOWNLOAD_SIGNING_KEY must be set")
            .into_bytes(),
        vault_dir: PathBuf::from(
            env::var("VAULT_DIR").unwrap_or_else(|_| "/var/lib/sanctuary-payd/vault".into()),
        ),
        public_base_url: env::var("PUBLIC_BASE_URL")
            .unwrap_or_else(|_| "https://technobuddhism.8b.is".into()),
        catalog: Arc::new(catalog),
    };

    let bind_addr: SocketAddr = env::var("BIND_ADDR")
        .unwrap_or_else(|_| "127.0.0.1:8108".into())
        .parse()
        .expect("Invalid BIND_ADDR");

    let app = build_router(state);

    println!(
        "[sanctuary-payd] Listening on http://{} (Trit 0 -> +1 active)",
        bind_addr
    );
    let listener = tokio::net::TcpListener::bind(bind_addr).await.unwrap();
    axum::serve(listener, app).await.unwrap();
}

fn build_router(state: AppState) -> Router {
    Router::new()
        .route("/api/health", get(health_handler))
        .route("/api/webhook/stripe", post(stripe_webhook_handler))
        .route("/api/webhook/revolut", post(revolut_webhook_handler))
        .route("/api/webhook/paypal", post(paypal_webhook_handler))
        .route("/api/claim/commons", post(commons_claim_handler))
        .route("/api/download/:book_id", get(download_handler))
        .with_state(state)
}

async fn health_handler() -> impl IntoResponse {
    Json(serde_json::json!({
        "status": "ok",
        "daemon": "sanctuary-payd",
        "trit": "+1",
        "privacy_regime": "Flyxion Definition 1 (Zero PII Retention)"
    }))
}

// ============================================================================
// 1. STRIPE WEBHOOK (`Stripe-Signature: t=...,v1=...`)
// ============================================================================
async fn stripe_webhook_handler(
    State(state): State<AppState>,
    headers: HeaderMap,
    body: Bytes,
) -> Result<Json<CapabilityGrant>, StatusCode> {
    let sig_header = headers
        .get("Stripe-Signature")
        .and_then(|v| v.to_str().ok())
        .ok_or(StatusCode::UNAUTHORIZED)?;

    let mut timestamp = "";
    let mut v1_sig = "";
    for part in sig_header.split(',') {
        if let Some(t) = part.strip_prefix("t=") {
            timestamp = t;
        } else if let Some(s) = part.strip_prefix("v1=") {
            v1_sig = s;
        }
    }
    if timestamp.is_empty() || v1_sig.is_empty() {
        return Err(StatusCode::UNAUTHORIZED);
    }

    // Verify timestamp freshness (within 300 seconds)
    let ts_num: u64 = timestamp.parse().map_err(|_| StatusCode::BAD_REQUEST)?;
    let now = current_unix();
    if now.abs_diff(ts_num) > 300 {
        return Err(StatusCode::UNAUTHORIZED);
    }

    // Compute HMAC-SHA256 over "{timestamp}.{raw_body}"
    let mut mac = HmacSha256::new_from_slice(&state.stripe_webhook_secret)
        .map_err(|_| StatusCode::INTERNAL_SERVER_ERROR)?;
    mac.update(timestamp.as_bytes());
    mac.update(b".");
    mac.update(&body);
    let expected = mac.finalize().into_bytes();
    let provided = hex::decode(v1_sig).map_err(|_| StatusCode::UNAUTHORIZED)?;

    if expected.as_slice().ct_eq(provided.as_slice()).unwrap_u8() != 1 {
        return Err(StatusCode::UNAUTHORIZED);
    }

    // Parse only non-sensitive metadata.book_id (Flyxion Non-Retention of PII)
    let payload: serde_json::Value =
        serde_json::from_slice(&body).map_err(|_| StatusCode::BAD_REQUEST)?;
    let event_type = payload["type"].as_str().unwrap_or("");
    if event_type != "checkout.session.completed" && event_type != "payment_intent.succeeded" {
        return Err(StatusCode::ACCEPTED);
    }

    let book_id = payload["data"]["object"]["metadata"]["book_id"]
        .as_str()
        .unwrap_or("omni-bundle");

    issue_grant(&state, book_id)
}

// ============================================================================
// 2. REVOLUT MERCHANT WEBHOOK (`Revolut-Signature: v1=...`, `Revolut-Request-Timestamp`)
// ============================================================================
async fn revolut_webhook_handler(
    State(state): State<AppState>,
    headers: HeaderMap,
    body: Bytes,
) -> Result<Json<CapabilityGrant>, StatusCode> {
    let ts = headers
        .get("Revolut-Request-Timestamp")
        .and_then(|v| v.to_str().ok())
        .ok_or(StatusCode::UNAUTHORIZED)?;
    let sig_header = headers
        .get("Revolut-Signature")
        .and_then(|v| v.to_str().ok())
        .ok_or(StatusCode::UNAUTHORIZED)?;

    let v1_hex = sig_header
        .strip_prefix("v1=")
        .ok_or(StatusCode::UNAUTHORIZED)?;

    // Revolut payload to sign: "v1.{timestamp}.{raw_body}"
    let mut mac = HmacSha256::new_from_slice(&state.revolut_webhook_secret)
        .map_err(|_| StatusCode::INTERNAL_SERVER_ERROR)?;
    mac.update(b"v1.");
    mac.update(ts.as_bytes());
    mac.update(b".");
    mac.update(&body);
    let expected = mac.finalize().into_bytes();
    let provided = hex::decode(v1_hex).map_err(|_| StatusCode::UNAUTHORIZED)?;

    if expected.as_slice().ct_eq(provided.as_slice()).unwrap_u8() != 1 {
        return Err(StatusCode::UNAUTHORIZED);
    }

    let payload: serde_json::Value =
        serde_json::from_slice(&body).map_err(|_| StatusCode::BAD_REQUEST)?;
    let event = payload["event"].as_str().unwrap_or("");
    if event != "ORDER_COMPLETED" {
        return Err(StatusCode::ACCEPTED);
    }

    let book_id = payload["merchant_order_ext_ref"]
        .as_str()
        .unwrap_or("omni-bundle");

    issue_grant(&state, book_id)
}

// ============================================================================
// 3. PAYPAL WEBHOOK (`X-PayPal-Sanctuary-Token` / `PAYMENT.CAPTURE.COMPLETED`)
// ============================================================================
async fn paypal_webhook_handler(
    State(state): State<AppState>,
    headers: HeaderMap,
    body: Bytes,
) -> Result<Json<CapabilityGrant>, StatusCode> {
    // Verify shared webhook secret header or query signature
    let token = headers
        .get("X-PayPal-Sanctuary-Token")
        .and_then(|v| v.to_str().ok())
        .ok_or(StatusCode::UNAUTHORIZED)?;

    if token
        .as_bytes()
        .ct_eq(state.paypal_webhook_token.as_slice())
        .unwrap_u8()
        != 1
    {
        return Err(StatusCode::UNAUTHORIZED);
    }

    let payload: serde_json::Value =
        serde_json::from_slice(&body).map_err(|_| StatusCode::BAD_REQUEST)?;
    let event_type = payload["event_type"].as_str().unwrap_or("");
    if event_type != "PAYMENT.CAPTURE.COMPLETED" && event_type != "CHECKOUT.ORDER.APPROVED" {
        return Err(StatusCode::ACCEPTED);
    }

    let book_id = payload["resource"]["custom_id"]
        .as_str()
        .unwrap_or("omni-bundle");

    issue_grant(&state, book_id)
}

// ============================================================================
// 4. FRANCISCAN FREE COMMONS CLAIM (BUDGET-ZERO / SHARING IS CARING)
// ============================================================================
async fn commons_claim_handler(
    State(state): State<AppState>,
    Json(req): Json<CommonsClaimRequest>,
) -> Result<Json<CapabilityGrant>, StatusCode> {
    issue_grant(&state, &req.book_id)
}

// ============================================================================
// 5. STATELESS CAPABILITY TOKEN MINTING & ZERO-COPY BOOK STREAMING
// ============================================================================
fn issue_grant(state: &AppState, book_id: &str) -> Result<Json<CapabilityGrant>, StatusCode> {
    let book = state
        .catalog
        .get(book_id)
        .or_else(|| state.catalog.get("omni-bundle"))
        .ok_or(StatusCode::NOT_FOUND)?;

    let expires = current_unix() + 86_400; // 24-hour capability window
    let token = sign_download_token(&state.download_signing_key, book.id, expires)?;
    let download_url = format!(
        "{}/api/download/{}?token={}",
        state.public_base_url, book.id, token
    );

    Ok(Json(CapabilityGrant {
        status: "unlocked",
        book_id: book.id.to_string(),
        title: book.title.to_string(),
        sha256_seal: book.sha256_seal.to_string(),
        download_url,
        expires_at_unix: expires,
        mantra: "OM MANI PADME HUNG · Sharing is Caring · {<3,<3,<3}+1",
    }))
}

async fn download_handler(
    State(state): State<AppState>,
    Path(book_id): Path<String>,
    Query(q): Query<UnlockQuery>,
) -> Result<Response, StatusCode> {
    let book = state.catalog.get(&book_id).ok_or(StatusCode::NOT_FOUND)?;

    if !verify_download_token(&state.download_signing_key, &book_id, &q.token) {
        return Err(StatusCode::FORBIDDEN);
    }

    let file_path = state.vault_dir.join(book.filename);
    let bytes = fs::read(&file_path)
        .await
        .map_err(|_| StatusCode::NOT_FOUND)?;

    // Compute live SHA-256 header receipt
    let mut hasher = Sha256::new();
    hasher.update(&bytes);
    let live_sha256 = hex::encode(hasher.finalize());

    let content_type = if book.filename.ends_with(".zip") {
        "application/zip"
    } else {
        "application/pdf"
    };

    let disposition = format!("attachment; filename=\"{}\"", book.filename);

    Response::builder()
        .status(StatusCode::OK)
        .header(header::CONTENT_TYPE, content_type)
        .header(header::CONTENT_DISPOSITION, disposition)
        .header("X-Sovereign-SHA256-Seal", live_sha256)
        .header("X-Flyxion-Projection", "Non-Retention-Verified")
        .body(Body::from(bytes))
        .map_err(|_| StatusCode::INTERNAL_SERVER_ERROR)
}

fn sign_download_token(key: &[u8], book_id: &str, expires: u64) -> Result<String, StatusCode> {
    let mut mac = HmacSha256::new_from_slice(key).map_err(|_| StatusCode::INTERNAL_SERVER_ERROR)?;
    let msg = format!("{}:{}", book_id, expires);
    mac.update(msg.as_bytes());
    let sig = hex::encode(mac.finalize().into_bytes());
    Ok(format!("{}.{}", expires, sig))
}

fn verify_download_token(key: &[u8], book_id: &str, token: &str) -> bool {
    let mut parts = token.splitn(2, '.');
    let exp_str = match parts.next() {
        Some(s) => s,
        None => return false,
    };
    let sig_hex = match parts.next() {
        Some(s) => s,
        None => return false,
    };

    let expires: u64 = match exp_str.parse() {
        Ok(v) => v,
        Err(_) => return false,
    };
    if current_unix() > expires {
        return false;
    }

    let mut mac = match HmacSha256::new_from_slice(key) {
        Ok(m) => m,
        Err(_) => return false,
    };
    let msg = format!("{}:{}", book_id, expires);
    mac.update(msg.as_bytes());
    let expected = mac.finalize().into_bytes();
    let provided = match hex::decode(sig_hex) {
        Ok(p) => p,
        Err(_) => return false,
    };

    expected.as_slice().ct_eq(provided.as_slice()).unwrap_u8() == 1
}

fn current_unix() -> u64 {
    SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap_or_default()
        .as_secs()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_catalog_has_all_10_volumes() {
        let catalog = build_verified_catalog();
        assert_eq!(catalog.len(), 10);
        for id in [
            "kompress-ultra",
            "mahakala-pecha-009",
            "family-plus-one",
            "dra-8bit-remarriage",
            "milarepa-dream-yoga",
            "zen-gitarom-matrix-buddha",
            "kama-sutra-fine-touch",
            "san-francesco-800",
            "axiomquant-auroralib",
            "omni-bundle",
        ] {
            let entry = catalog.get(id).expect("missing catalog entry");
            assert_eq!(entry.sha256_seal.len(), 64);
        }
    }

    #[test]
    fn test_sign_and_verify_download_token() {
        let key = b"sovereign-sanctuary-256-bit-signing-key-test";
        let expires = current_unix() + 3600;
        let token = sign_download_token(key, "mahakala-pecha-009", expires).unwrap();
        assert!(verify_download_token(key, "mahakala-pecha-009", &token));
        assert!(!verify_download_token(key, "kompress-ultra", &token));
        assert!(!verify_download_token(b"wrong-key", "mahakala-pecha-009", &token));
    }

    #[test]
    fn test_expired_token_rejected() {
        let key = b"sovereign-sanctuary-256-bit-signing-key-test";
        let past = current_unix().saturating_sub(10);
        let token = sign_download_token(key, "mahakala-pecha-009", past).unwrap();
        assert!(!verify_download_token(key, "mahakala-pecha-009", &token));
    }
}
