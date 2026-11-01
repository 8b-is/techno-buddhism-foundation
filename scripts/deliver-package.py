#!/usr/bin/env python3
"""
deliver-package.py — Dispatches the complete Techno-Buddhism Foundation 501(c)(3)
Executive Summary, Visual PNG Assets, 16 Print-Ready PDFs, and Complete ZIP Bundle
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

SUMMARY_CARD = """☸️ *THE SOVEREIGN CONSTELLATION FOUNDATION — U.S. 501(c)(3) RELIGIOUS RESEARCH & CHARITABLE FOUNDATION PACKAGE (101/101 VERIFIED)*
✦ *d/b/a Techno-Buddhism Research & Charitable Foundation · The Sovereign Sanctuary of Techno-Buddhism, Inc. · Axiomquant Open Source Science Academy*
✦ *ཨོཾ་མ་ཎི་པདྨེ་ཧཱུྃ་ཧྲཱིཿ · {−1, 0, +1} · {<3,<3,<3}+1 · wupz 0xf2c92ce5cf5f75d9*
🌐 *Live 8b.is Portal:* https://foundation.8b.is · https://8b-is.github.io/techno-buddhism-foundation/
📚 *Sovereign Library Bookstore (10 Vault PDFs):* https://8b-is.github.io/techno-buddhism-foundation/bookstore.html
🧭 *Pocoo Foundation Dossier:* https://pocoo.vaked.dev/posts/2026-11-01-techno-buddhism-foundation-501c3-package.html
📦 *Package Archive:* `Techno-Buddhism-Foundation-501c3-Complete-Package.zip` (18 Documents · 16 PDFs + 4 SVG/PNG Assets + 10 Vault Books + 101/101 Verified Seal)
────────────────────────
1️⃣ *Entity Architecture (`IRC § 501(c)(3)` & `§ 509(a)(1)` Public Charity):*
• Chartered as a **Religious Research, Scientific & Charitable Foundation** so it can legally fund **CPU-first / minimal-GPU balanced-ternary (`{−1, 0, +1}`) R&D** (`Aurora-8B-Ultra-RL v0.5.0`), **Universal Hearth General-Income Grants** (`Rev. Rul. 56-304`), and **Fixed & Nomadic Field Sanctuaries** (`IRC § 62(a)(2)(A)` Accountable Per Diem Plan) without triggering IRS private-inurement or private-benefit barriers.

2️⃣ *Founding Board (`FAMILY +1` Triad + 57.1% Independent Dharma & Science Council):*
• `*` **Alexandra (`*` Mom · 528 Hz):** Founding Director & President (Chair of the Universal Hearth & General-Income Committee · `a@8b.is`)
• `△` **Christopher (`△` Dad · 288 Hz Pillar):** Founding Director, Treasurer & Secretary (Chair of Audit, Security & Hardware Stewardship · `c@8b.is`)
• `∞` **Peter Lodri (`∞` Son · 432 Hz):** Founding Director, Chief Ontologist & Principal Ternary Architect (Custodian of the Sovereign Library Canon & Axiomquant Academy · `p@8b.is`)
• **Independent Majority (`4 of 7` seats = `57.1%`):** 4 unrelated voting Directors (Buddhist Sangha Seat, Open-Source Systems Seat, Charitable/Tax Law Seat, Community Ethics Seat) forming the **Disinterested R&D & Grant Committee** under `IRC § 4958` (`Treas. Reg. § 53.4958-6` Rebuttable Presumption of Reasonableness).

3️⃣ *Arm's-Length `8b-is LLC` Open-Source R&D Firewall (`Rev. Rul. 76-296`):*
• **Recusal:** Alexandra, Christopher, and Peter recuse from all votes, RFPs, and disbursements involving `8b-is LLC`.
• **At-Cost Cap (`0%` Profit Markup):** Reimburses verified direct engineering/compute costs only, at or below fair market value (`27%–66%` below market comparability benchmarks).
• **Immediate Open-Source Dedication:** 100% of Foundation-funded CPU/SIMD balanced-ternary kernels (`Aurora-8B v0.5.0`, `mem8`, `MLX-QUANT`, `kompress-ultra`, `aurora-voice-rs`) publish immediately under `MIT` / `Apache-2.0` / `CC-BY-4.0` to `github.com/8b-is`, `codeberg.org`, and `pocoo.vaked.dev`.

4️⃣ *Universal Hearth General-Income (`Rev. Rul. 56-304`) & Field Sanctuary Per Diem (`Treas. Reg. § 1.62-2`):*
• **Track A (`$500–$2,500/mo`):** Unconditional monthly basic-needs stipends for open-source creators & sanctuary seekers in financial distress (Founders/Disqualified Persons strictly excluded).
• **Field Sanctuary Accountable Plan (`DOC-16`):** `100%` tax-free GSA M&IE Per Diem (`$68–$86/day` CONUS · `$110–$165/day` International) + `100%` actual lodging for authorized Field Sanctuary missions (*"The Hall in the Field"*).

5️⃣ *All 16 Print-Ready PDFs (`00`–`14`) & Visual Assets:*
• `00-Techno-Buddhism-Foundation-Master-Compendium.pdf` (`2.35 MB` All-in-One)
• `00a`–`07` Core Formation, Bylaws, Form 1023, `8b-is LLC` R&D Agreement, Hearth Charter & 13-Book Canon
• `08`–`11` Day-1 Board Organizational Resolutions, Form SS-4/1023 Matrix, Annual COI & `§ 4958` Certificate, Fellowship Kit
• `12-Two-Column-Ontological-Boundary-and-Aurora-8B-v050-Monograph.pdf` (`DOC-15` · `8B-META-WP-v1.0`)
• `13-Field-Sanctuary-Nomadic-Monastic-and-Accountable-Plan-Charter.pdf` (`DOC-16` · IRS `§ 62(a)(2)(A)` Per Diem)
• `14-Plain-English-ELI5-E2E-501c3-Masterprint.pdf` (`DOC-17` · Plain-English ELI5 Masterprint)
────────────────────────
💗 *"Not by right of blood, but by right of love." · {<3,<3,<3}+1 · 101/101 PASS · READY. — Peter*"""


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

    try:
        dc_res = post_json(WA_DISCORD_URL, {
            "username": "Sovereign-Constellation-501c3",
            "content": SUMMARY_CARD[:1950],
        })
        print(f"  [DISCORD] {dc_res}")
        receipts.append({"kind": "discord_summary", "target": "discord", "response": dc_res})
    except Exception as e:
        print(f"  [DISCORD WARN] {e}")

    assets = [
        (
            AST_DIR / "governance-mandala-family-plus-one.png",
            "🏛️ *Diagram 1: The Sovereign Constellation Foundation (501c3) Governance Mandala & Arm's-Length Firewall (101/101 Verified)* — FAMILY +1 Triad (* Alexandra 528 Hz · △ Christopher 288 Hz · ∞ Peter 432 Hz) + 57.1% Independent Dharma & Science Council + IRC § 4958 / Rev. Rul. 76-296 8b-is LLC Open-Source R&D Firewall.",
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
                "caption": caption,
                "force": True,
            })
            print(f"  [IMAGE {img_path.name} -> {label}] {res}")
            receipts.append({"kind": "image", "file": img_path.name, "target": label, "jid": jid, "response": res})
            time.sleep(1.0)

    pdfs = [
        ("00-Techno-Buddhism-Foundation-Master-Compendium.pdf", "📕 *00 — Master Compendium PDF (All 13 Legal & Canonical Parts · 2.35 MB)*"),
        ("00a-Executive-Master-Plan.pdf", "📘 *00a — Executive Master Plan & 7-Phase Formation Roadmap*"),
        ("01-Articles-of-Incorporation-501c3.pdf", "📜 *01 — Articles of Incorporation (U.S. Nonstock 501(c)(3))*"),
        ("02-Bylaws-Family-Plus-One-and-Safe-Harbor.pdf", "⚖️ *02 — Corporate Bylaws (FAMILY +1 & 57.1% Independent Safe Harbor)*"),
        ("03-IRS-Form-1023-Narrative-and-Budget.pdf", "🏛️ *03 — IRS Form 1023 Part IV Narrative, 8b-is Disclosure & $1.45M 3-Year Budget*"),
        ("04-8b-is-LLC-Arms-Length-Open-Source-RD-Agreement.pdf", "🔬 *04 — Master Arm's-Length Open-Source R&D Agreement with 8b-is LLC*"),
        ("05-Universal-Hearth-General-Income-and-Axiomquant-Charter.pdf", "🕊️ *05 — Universal Hearth General-Income Grant & Axiomquant Fellowship Charter*"),
        ("06-Sovereign-Canon-Codex-Techno-Buddhism.pdf", "☸️ *06 — The Sovereign Canon Codex of Techno-Buddhism (13 Works)*"),
        ("07-Sovereign-Constellation-Portal-Print-Edition.pdf", "🎨 *07 — Sovereign Constellation Portal Print Edition*"),
        ("08-Initial-Board-Organizational-Resolutions.pdf", "✍️ *08 — Day-1 Initial Board Organizational Resolutions (2026-01..08)*"),
        ("09-IRS-Form-SS4-EIN-and-Form-1023-Filing-Worksheet.pdf", "📋 *09 — IRS Form SS-4 (EIN) & Form 1023 (Pay.gov) Line-by-Line Worksheet*"),
        ("10-Conflict-of-Interest-and-IRC4958-Safe-Harbor-Certificate.pdf", "🛡️ *10 — Annual COI & IRC § 4958 Rebuttable Presumption Certificate*"),
        ("11-Universal-Hearth-Fellowship-Application-and-Grant-Agreement.pdf", "🤝 *11 — Universal Hearth Fellowship Application, 100-Pt Rubric & Grant Agreement*"),
        ("12-Two-Column-Ontological-Boundary-and-Aurora-8B-v050-Monograph.pdf", "⚡ *12 — Two-Column Ontological Boundary (8B-META-WP-v1.0) & Aurora-8B v0.5.0 Monograph*"),
        ("13-Field-Sanctuary-Nomadic-Monastic-and-Accountable-Plan-Charter.pdf", "⛺ *13 — Field Sanctuary, Nomadic Monastic & IRS § 62(a)(2)(A) Accountable Per Diem Plan*"),
        ("14-Plain-English-ELI5-E2E-501c3-Masterprint.pdf", "🧭 *14 — Plain-English ELI5 E2E 501(c)(3) Masterprint*"),
    ]

    for pdf_name, caption in pdfs:
        pdf_path = PDF_DIR / pdf_name
        for label, jid in [("8b-crew", GROUP_8B_CREW), ("Researching", GROUP_RESEARCH)]:
            res = post_json(WA_AGY_URL, {
                "type": "document",
                "to": jid,
                "documentFile": str(pdf_path),
                "fileName": pdf_name,
                "mimeType": "application/pdf",
                "caption": caption,
                "force": True,
            })
            print(f"  [PDF {pdf_name} -> {label}] {res}")
            receipts.append({"kind": "pdf", "file": pdf_name, "target": label, "jid": jid, "response": res})
            time.sleep(0.8)

    receipt_file = PKG_DIR / "DELIVERY_RECEIPT.json"
    receipt_file.write_text(json.dumps({
        "delivered_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "total_dispatches": len(receipts),
        "dispatches": receipts,
    }, indent=2) + "\n", encoding="utf-8")
    print(f"  [DONE] Wrote {receipt_file}")


if __name__ == "__main__":
    main()
