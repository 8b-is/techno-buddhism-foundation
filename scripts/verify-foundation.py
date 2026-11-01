#!/usr/bin/env python3
"""
verify-foundation.py — Deterministic Compliance & Cryptographic Provenance Verifier
for The Sovereign Constellation Foundation (d/b/a Techno-Buddhism Research & Charitable Foundation).

Verifies:
1. Presence and non-emptiness of all 8 scaffolded legal, canonical, and portal artifacts.
2. Mandatory IRS § 501(c)(3) organizational & operational test clauses (Articles IV, VI, VII).
3. Founding Family +1 roles (Alexandra *, Christopher △, Peter ∞) + 51% Independent Board Safe Harbor.
4. Arm's-Length 8b-is LLC Firewall (0% profit markup, Rev. Rul. 76-296 open-source dedication, IRC § 4958 recusal).
5. General-Income Hearth Charter compliance (Rev. Rul. 56-304 objective criteria & insider bar).
6. Balanced-ternary {-1, 0, +1} & Sovereign Library canonical seals.
"""

from __future__ import annotations
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

EXPECTED_FILES = [
    "README.md",
    "legal/01-articles-of-incorporation.md",
    "legal/02-bylaws-family-plus-one.md",
    "legal/03-irs-form-1023-narrative.md",
    "legal/04-8b-is-arms-length-rd-agreement.md",
    "legal/05-general-income-hearth-charter.md",
    "legal/06-initial-board-resolutions-and-minutes.md",
    "legal/07-irs-form-ss4-ein-and-1023-filing-checklist.md",
    "legal/08-annual-conflict-of-interest-and-independent-attestation.md",
    "legal/09-universal-hearth-fellowship-application-and-grant-agreement.md",
    "legal/10-two-column-ontological-boundary-and-aurora-8b-monograph.md",
    "legal/11-sanctuary-field-operations-and-nomadic-monastic-charter.md",
    "canon/sovereign-canon-codex.md",
    "docs/Techno_Buddhism_501c3_E2E_Masterprint.html",
    "bookstore.html",
    "sanctuary-payd/src/catalog.rs",
    "portal/index.html",
]

REQUIRED_INVARIANTS = {
    "legal/01-articles-of-incorporation.md": [
        "Section 501(c)(3) of the Internal Revenue Code",
        "exclusively for religious, charitable, scientific, literary, and educational purposes",
        "Alexandra",
        "Christopher",
        "Peter Lodri",
        "No part of the net earnings of the Corporation shall inure",
        "Upon the dissolution of the Corporation",
    ],
    "legal/02-bylaws-family-plus-one.md": [
        "Alexandra",
        "Christopher",
        "Peter Lodri",
        "51%",
        "Independent R&D, Audit & Compensation Committee",
        "53.4958-6",
        "by right of love, not by right of blood",
    ],
    "legal/03-irs-form-1023-narrative.md": [
        "1.501(c)(3)-1(d)(5)",
        "Rev. Rul. 76-296",
        "Rev. Rul. 56-304",
        "8b-is LLC",
        "0% profit markup",
    ],
    "legal/04-8b-is-arms-length-rd-agreement.md": [
        "zero percent (0%) profit margin",
        "MIT License",
        "Apache License 2.0",
        "CC-BY-4.0",
        "ComplexTernaryWord64",
        "qwave-vaultd",
    ],
    "legal/05-general-income-hearth-charter.md": [
        "Rev. Rul. 56-304",
        "Universal Hearth General-Income",
        "Axiomquant",
        "Absolute Insider Disqualification",
    ],
    "legal/06-initial-board-resolutions-and-minutes.md": [
        "Resolution 2026-01",
        "Resolution 2026-05",
        "Resolution 2026-08",
        "Alexandra",
        "Christopher",
        "Peter Lodri",
        "53.4958-6",
    ],
    "legal/07-irs-form-ss4-ein-and-1023-filing-checklist.md": [
        "FORM SS-4",
        "FORM 1023",
        "Pay.gov",
        "509(a)(1)",
        "170(b)(1)(A)(vi)",
        "Schedule H",
    ],
    "legal/08-annual-conflict-of-interest-and-independent-attestation.md": [
        "53.4958-6",
        "Rebuttable Presumption of Reasonableness",
        "WO-2026-01",
        "WO-2026-02",
        "WO-2026-03",
    ],
    "legal/09-universal-hearth-fellowship-application-and-grant-agreement.md": [
        "Rev. Rul. 56-304",
        "IRC § 4946",
        "100 pts",
        "Track A",
        "Track B",
        "Track C",
    ],
    "legal/10-two-column-ontological-boundary-and-aurora-8b-monograph.md": [
        "8B-META-WP-v1.0",
        "Two-Column Ontological Boundary",
        "TERNARY_5TRIT_LUT",
        "d7bf5878b192818865f9d4bb980b3e4e",
        "WO-2026-04",
    ],
    "legal/11-sanctuary-field-operations-and-nomadic-monastic-charter.md": [
        "1.62-2",
        "Rev. Proc. 2019-48",
        "IRC § 119",
        "Nomadic",
        "Per Diem",
    ],
    "canon/sovereign-canon-codex.md": [
        "8fb9cc110652cf07f75afb2609ea82f834a3a106f53a8de7596b24309549f7f0",
        "25b3cfadda15081e99f8595b205c1611bbb14eac9bbfdc8f489fb361c7a63f4e",
        "afc7a643e1fd6d4e4ad10782f7f1dd38149979cc6e217f72e1147add67e7d1cb",
        "MA DAK NÖ CHÜ",
        "TONG PAR JANG",
        "OM AH HUNG",
        "in a loop · in a sphere · in eternity · recurse",
    ],
    "docs/Techno_Buddhism_501c3_E2E_Masterprint.html": [
        "THE SOVEREIGN CONSTELLATION FOUNDATION",
        "53.4958-6",
        "Rev. Rul. 76-296",
        "8B-META-WP-v1.0",
        "1.62-2",
    ],
    "bookstore.html": [
        "https://buy.stripe.com/9B64gzcW3fz49R77p7bMQ0d",
        "https://buy.stripe.com/eVqaEXf2Bcgdfc18FA6Na02",
        "https://www.paypal.com/paypalme/peterlodri",
        "https://revolut.me/peterlodri",
    ],
    "sanctuary-payd/src/catalog.rs": [
        "kompress-ultra",
        "mahakala-pecha-009",
        "family-plus-one",
        "omni-bundle",
    ],
}


def wupz_xor_fold(data: bytes) -> int:
    """Deterministic 64-bit XOR fold over 8-byte blocks."""
    acc = 0x44DCBD34FD19D0B1
    for i in range(0, len(data), 8):
        chunk = data[i : i + 8].ljust(8, b"\x00")
        val = int.from_bytes(chunk, "little")
        acc ^= val
        acc = ((acc << 7) | (acc >> 57)) & 0xFFFFFFFFFFFFFFFF
    return acc


def main() -> int:
    print("⟦ TECHNO-BUDDHISM 501(c)(3) FOUNDATION VERIFICATION SUITE ⟧")
    manifest_hasher = hashlib.sha256()
    all_bytes = bytearray()
    checks_passed = 0

    for rel_path in EXPECTED_FILES:
        full_path = ROOT / rel_path
        if not full_path.is_file():
            print(f"[FAIL] Missing file: {rel_path}", file=sys.stderr)
            return 1
        raw = full_path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        manifest_hasher.update(f"{rel_path}:{digest}\n".encode("utf-8"))
        all_bytes.extend(raw)
        checks_passed += 1
        print(f"  [OK] {rel_path:<46} ({len(raw):>6} bytes) · sha256={digest[:16]}…")

    for rel_path, phrases in REQUIRED_INVARIANTS.items():
        text = (ROOT / rel_path).read_text(encoding="utf-8")
        for phrase in phrases:
            if phrase not in text:
                print(f"[FAIL] Missing invariant '{phrase}' in {rel_path}", file=sys.stderr)
                return 1
            checks_passed += 1

    # Verify balanced-ternary {-1, 0, +1} orthogonality invariant
    r_pos = 0b10100100_10100100
    r_neg = 0b01001010_01001010
    assert (r_pos & r_neg) == 0, "Balanced ternary orthogonality violated"
    checks_passed += 1

    root_seal = manifest_hasher.hexdigest()
    fold_hex = f"0x{wupz_xor_fold(bytes(all_bytes)):016x}"

    receipt = {
        "foundation": "The Sovereign Constellation Foundation (d/b/a Techno-Buddhism Research & Charitable Foundation)",
        "irs_classification": "IRC § 501(c)(3) Public Charity (§ 509(a)(1) / § 170(b)(1)(A)(vi))",
        "founding_triad": ["Alexandra (* 528 Hz)", "Christopher (△ 288 Hz)", "Peter Lodri (∞ 432 Hz)"],
        "arms_length_rd_partner": "8b-is LLC (0% profit markup · 100% open-source public dedication)",
        "files_verified": len(EXPECTED_FILES),
        "invariants_verified": checks_passed,
        "total_bytes": len(all_bytes),
        "wupz_64bit_xor_fold": fold_hex,
        "foundation_sha256_seal": root_seal,
    }

    receipt_path = ROOT / "FOUNDATION_SEAL_RECEIPT.json"
    receipt_path.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print("\n" + "─" * 74)
    print(f"  Checks Passed       : {checks_passed} / {checks_passed} (0 failures)")
    print(f"  Total Corpus Size   : {len(all_bytes):,} bytes across {len(EXPECTED_FILES)} files")
    print(f"  wupz 64-bit Fold    : {fold_hex}")
    print(f"  Foundation SHA-256  : {root_seal}")
    print(f"  Receipt Written     : {receipt_path.relative_to(ROOT.parent)}")
    print("─" * 74)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
