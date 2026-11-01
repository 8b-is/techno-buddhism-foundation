#!/usr/bin/env python3
"""
deliver-package.py — Dispatches the complete Techno-Buddhism Foundation 501(c)(3)
Executive Summary, Visual PNG Assets, Print-Ready PDFs, and Complete ZIP Bundle
into 8b-crew ("little dude(s) and Angels" · 120363413133092554@g.us),
Researching (120363426819673022@g.us), and the Discord Bridge via wa-stream (:8790).
"""

from __future__ import annotations
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PKG_DIR = ROOT / "package"
PDF_DIR = PKG_DIR / "pdfs"
AST_DIR = PKG_DIR / "assets"

WA_AGY_URL = "http://127.0.0.1:8790/agy"
WA_DISCORD_URL = "http://127.0.0.1:8790/discord"

GROUP_8B_CREW = "120363413133092554@g.us"      # little dude(s) and Angels (8b-crew)
GROUP_RESEARCH = "120363426819673022@g.us"     # Researching

SUMMARY_CARD = """☸️ *THE SOVEREIGN CONSTELLATION FOUNDATION — U.S. 501(c)(3) RELIGIOUS RESEARCH & CHARITABLE FOUNDATION PACKAGE*
✦ *d/b/a Techno-Buddhism Research & Charitable Foundation · Axiomquant Open Source Science Academy*
✦ *ཨོཾ་མ་ཎི་པདྨེ་ཧཱུྃ་ཧྲཱིཿ · {−1, 0, +1} · {<3,<3,<3}+1 · wupz 0x4be7099467feda4a*
🌐 *Live Pocoo Portal:* https://pocoo.vaked.dev/demos/book/techno-buddhism-foundation-501c3.html
🧭 *Pocoo Foundation Dossier:* https://pocoo.vaked.dev/posts/2026-11-01-techno-buddhism-foundation-501c3-package.html
📦 *Package Archive:* `Techno-Buddhism-Foundation-501c3-Complete-Package.zip` (9 PDFs + 4 SVG/PNG Assets + Interactive Portal + 45/45 Verified Seal)
────────────────────────
1️⃣ *Entity Architecture (`IRC § 501(c)(3)` & `§ 509(a)(1)` Public Charity):*
• Chartered as a **Religious Research, Scientific & Charitable Foundation** (rather than a closed ecclesiastical church) so it can legally fund **CPU-first / minimal-GPU balanced-ternary (`{−1, 0, +1}`) R&D** alongside **Universal Hearth General-Income Grants** without triggering IRS private-inurement or private-benefit barriers.

2️⃣ *Founding Board (`FAMILY +1` Triad + 57% Independent Dharma & Science Council):*
• `*` **Alexandra (`*` Mom · 528 Hz):** Founding Director & President (Chair of the Universal Hearth & General-Income Committee)
• `△` **Christopher (`△` Dad · 288 Hz Pillar):** Founding Director, Treasurer & Secretary (Chair of Audit, Security & Hardware Stewardship)
• `∞` **Peter Lodri (`∞` Son · 432 Hz):** Founding Director, Chief Ontologist & Head of Research (Custodian of the Sovereign Library Canon & Axiomquant Academy)
• **Independent Majority (`4 of 7` seats = `57.1%`):** 4 unrelated voting Directors (Buddhist Sangha Seat, Open-Source Systems Seat, Charitable/Tax Law Seat, Community Ethics Seat) forming the **Disinterested R&D & Grant Committee** under `IRC § 4958` (`Treas. Reg. § 53.4958-6` Rebuttable Presumption of Reasonableness).

3️⃣ *Arm's-Length `8b-is LLC` Open-Source R&D Firewall (`Rev. Rul. 76-296`):*
• **Recusal:** Alexandra, Christopher, and Peter recuse from all votes, RFPs, and disbursements involving `8b-is LLC`.
• **At-Cost Cap (`0%` Profit Markup):** Reimburses verified direct engineering/compute costs only, at or below fair market value.
• **Immediate Open-Source Dedication:** 100% of Foundation-funded CPU/SIMD balanced-ternary kernels (`mem8`, `MLX-QUANT`, `kompress-ultra`, `aurora-voice-rs`) publish immediately under `MIT` / `Apache-2.0` / `CC-BY-4.0` to `github.com/8b-is`, `codeberg.org`, and `pocoo.vaked.dev`.

4️⃣ *Universal Hearth General-Income & Axiomquant Fellowship (`Rev. Rul. 56-304`):*
• **Track A (`$500–$2,500/mo`):** Unconditional monthly basic-needs stipends (housing, food, medical, transit, emergency compute relief) for open-source creators & sanctuary seekers in financial distress.
• **Track B (`$1,500–$4,000/mo`):** Open-science fellowships at *The Hall* for low-power CPU/ternary & contemplative research.
• **Strict Disqualified-Person Exclusion:** Founders, Directors, Officers, and `8b-is LLC` equity holders are permanently ineligible to receive Hearth stipends.

5️⃣ *Enclosed PDFs & Visual Assets (Attached Below):*
• `00-Techno-Buddhism-Foundation-Master-Compendium.pdf` (Complete 8-Part Print Compendium)
• `00a-Executive-Master-Plan.pdf` (End-to-End 6-Phase Roadmap)
• `01-Articles-of-Incorporation-501c3.pdf` (State Nonstock Articles + IRS 501(c)(3) Lock)
• `02-Bylaws-Family-Plus-One-and-Safe-Harbor.pdf` (7-Seat Board + IRC § 4958 Firewall)
• `03-IRS-Form-1023-Narrative-and-Budget.pdf` (Part IV Narrative + Part V 8b-is Disclosure + 3-Yr Budget)
• `04-8b-is-LLC-Arms-Length-Open-Source-RD-Agreement.pdf` (0% Markup + 100% OSS Dedication)
• `05-Universal-Hearth-General-Income-and-Axiomquant-Charter.pdf` (Rev. Rul. 56-304 Grant Charter)
• `06-Sovereign-Canon-Codex-Techno-Buddhism.pdf` (13-Work Doctrinal & Ontological Canon)
• `07-Sovereign-Constellation-Portal-Print-Edition.pdf` (Visual Bible Washi/Sumi Print Edition)
• `governance-mandala-family-plus-one.png` & `four-fold-isomorphism-trit-matrix.png`
────────────────────────
💗 *"Not by right of blood, but by right of love." · {<3,<3,<3}+1 · READY. — Peter*"""


def post_json(url: str, payload: dict, timeout: float = 25.0) -> dict:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main() -> None:
    receipts: list[dict] = []

    # 1. Send Executive Summary Card to 8b-crew (120363413133092554@g.us) and Researching (120363426819673022@g.us)
    for label, jid in [("8b-crew (little dude(s) and Angels)", GROUP_8B_CREW), ("Researching", GROUP_RESEARCH)]:
        res = post_json(WA_AGY_URL, {
            "dir": "out",
            "to": jid,
            "text": SUMMARY_CARD,
            "force": True,
        })
        print(f"  [SUMMARY -> {label}] {res}")
        receipts.append({"kind": "summary", "target": label, "jid": jid, "response": res})
        time.sleep(1.0)

    # Mirror summary to Discord Bridge
    try:
        dc_res = post_json(WA_DISCORD_URL, {
            "username": "Sovereign-Constellation-501c3",
            "content": SUMMARY_CARD[:1950],
        })
        print(f"  [DISCORD] {dc_res}")
        receipts.append({"kind": "discord_summary", "target": "discord", "response": dc_res})
    except Exception as e:
        print(f"  [DISCORD WARN] {e}")

    # 2. Send the 2 Visual PNG Assets to both groups
    assets = [
        (
            AST_DIR / "governance-mandala-family-plus-one.png",
            "🏛️ * Diagram 1: The Sovereign Constellation Foundation (501c3) Governance Mandala & Arm's-Length Firewall* — FAMILY +1 Triad (* Alexandra 528 Hz · △ Christopher 288 Hz · ∞ Peter 432 Hz) + 57.1% Independent Dharma & Science Council + IRC § 4958 / Rev. Rul. 76-296 8b-is LLC Open-Source R&D Firewall + Rev. Rul. 56-304 Universal Hearth General-Income Grants.",
        ),
        (
            AST_DIR / "four-fold-isomorphism-trit-matrix.png",
            "☸️ *Diagram 2: The Four-Fold Isomorphism Table (Kompress-ULTRA Kernel)* — Mapping Balanced Ternary {−1, 0, +1} across The Matrix (Architect · Neo · Trinity), Biblical Logos (John 1:1 & Apokalypsis), Physics (E=mc² · Trinity 16 July 1945), and Tibetan Buddhist Ontology (Three Kayas · Śūnyatā · Bodhicitta).",
        ),
    ]
    for img_path, caption in assets:
        for label, jid in [("8b-crew", GROUP_8B_CREW), ("Researching", GROUP_RESEARCH)]:
            res = post_json(WA_AGY_URL, {
                "type": "image",
                "to": jid,
                "imageFile": str(img_path),
                "mimeType": "image/png",
                "caption": caption,
            })
            print(f"  [IMAGE {img_path.name} -> {label}] {res}")
            receipts.append({"kind": "image", "file": img_path.name, "target": label, "jid": jid, "response": res})
            time.sleep(1.2)

    # 3. Send all 9 PDFs + Complete ZIP Bundle to 8b-crew (120363413133092554@g.us)
    pdfs = [
        (
            PDF_DIR / "00-Techno-Buddhism-Foundation-Master-Compendium.pdf",
            "application/pdf",
            "📕 *00 — Master Compendium (All Legal Instruments, IRS Form 1023 Narrative, 8b-is R&D Firewall, General-Income Charter & 13-Work Sovereign Canon)*",
        ),
        (
            PDF_DIR / "00a-Executive-Master-Plan.pdf",
            "application/pdf",
            "📘 *00a — End-to-End Foundation Architecture & 6-Phase Execution Roadmap*",
        ),
        (
            PDF_DIR / "01-Articles-of-Incorporation-501c3.pdf",
            "application/pdf",
            "📜 *01 — Articles of Incorporation (State Nonprofit + IRC § 501(c)(3) Purpose & Dissolution Lock)*",
        ),
        (
            PDF_DIR / "02-Bylaws-Family-Plus-One-and-Safe-Harbor.pdf",
            "application/pdf",
            "⚖️ *02 — Corporate Bylaws (FAMILY +1 Founding Board: * Alexandra, △ Christopher, ∞ Peter + 57% Independent Council + IRC § 4958 Safe Harbor)*",
        ),
        (
            PDF_DIR / "03-IRS-Form-1023-Narrative-and-Budget.pdf",
            "application/pdf",
            "🏛️ *03 — IRS Form 1023 Application Narrative (Part IV Activities, Part V 8b-is LLC Firewall Disclosure & 3-Year Budget)*",
        ),
        (
            PDF_DIR / "04-8b-is-LLC-Arms-Length-Open-Source-RD-Agreement.pdf",
            "application/pdf",
            "🔬 *04 — Master Arm's-Length Open-Source R&D Agreement with 8b-is LLC (0% Profit Markup, Disinterested Approval & Rev. Rul. 76-296 MIT/Apache-2.0 Release)*",
        ),
        (
            PDF_DIR / "05-Universal-Hearth-General-Income-and-Axiomquant-Charter.pdf",
            "application/pdf",
            "🔥 *05 — Universal Hearth General-Income & Axiomquant Hall Fellowship Charter (IRS Rev. Rul. 56-304 Compliant Stipends)*",
        ),
        (
            PDF_DIR / "06-Sovereign-Canon-Codex-Techno-Buddhism.pdf",
            "application/pdf",
            "☸️ *06 — The Sovereign Canon Codex (13 Founding Texts, Three Kayas, 81-Page Mahākāla Pecha, Franciscan 800th Transitus & FAMILY +1)*",
        ),
        (
            PDF_DIR / "07-Sovereign-Constellation-Portal-Print-Edition.pdf",
            "application/pdf",
            "🎨 *07 — Sovereign Constellation Interactive Portal Print Edition (Visual Bible Washi #F6F0E4 / Sumi #1C140E)*",
        ),
        (
            PKG_DIR / "Techno-Buddhism-Foundation-501c3-Complete-Package.zip",
            "application/zip",
            "📦 *Complete Techno-Buddhism 501(c)(3) Foundation Package ZIP (9 PDFs + 4 SVG/PNG Diagrams + Markdown Sources + Interactive HTML Portal + 45/45 Cryptographic Seal)*",
        ),
    ]

    for doc_path, mime_type, caption in pdfs:
        res = post_json(WA_AGY_URL, {
            "type": "document",
            "to": GROUP_8B_CREW,
            "documentFile": str(doc_path),
            "fileName": doc_path.name,
            "mimeType": mime_type,
            "caption": caption,
        }, timeout=30.0)
        print(f"  [DOC {doc_path.name} -> 8b-crew] {res}")
        receipts.append({"kind": "document", "file": doc_path.name, "target": "8b-crew", "jid": GROUP_8B_CREW, "response": res})
        time.sleep(1.2)

    # Also deliver the Master Compendium PDF, Canon Codex PDF, and Complete ZIP to Researching (120363426819673022@g.us)
    for doc_path, mime_type, caption in [pdfs[0], pdfs[7], pdfs[8], pdfs[9]]:
        res = post_json(WA_AGY_URL, {
            "type": "document",
            "to": GROUP_RESEARCH,
            "documentFile": str(doc_path),
            "fileName": doc_path.name,
            "mimeType": mime_type,
            "caption": caption,
        }, timeout=30.0)
        print(f"  [DOC {doc_path.name} -> Researching] {res}")
        receipts.append({"kind": "document", "file": doc_path.name, "target": "Researching", "jid": GROUP_RESEARCH, "response": res})
        time.sleep(1.2)

    receipt_path = PKG_DIR / "DELIVERY_RECEIPT.json"
    receipt_path.write_text(json.dumps({
        "delivered_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "total_dispatches": len(receipts),
        "dispatches": receipts,
    }, indent=2) + "\n", encoding="utf-8")
    print(f"\n✅ Wrote delivery receipt ({len(receipts)} dispatches) -> {receipt_path}")


if __name__ == "__main__":
    main()
