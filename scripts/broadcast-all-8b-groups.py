#!/usr/bin/env python3
"""
Broadcasts the live 8b.is Sovereign Constellation Foundation (501(c)(3)) Landing Page,
Sovereign Library Bookstore, Executive Summary, Visual Diagrams, and 16-PDF / 9.18 MB ZIP Package
to ALL 8b-is relevant WhatsApp groups via the live wa-stream sidecar (http://127.0.0.1:8790/agy).
"""

import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PKG_DIR = ROOT / "package"
PDF_DIR = PKG_DIR / "pdfs"
ASSETS_DIR = PKG_DIR / "assets"
WA_ENDPOINT = "http://127.0.0.1:8790/agy"

# All 8b-is / vaked.dev / family+1 / pooconf WhatsApp groups discovered via GET /groups
TARGET_GROUPS = [
    ("120363430226473934@g.us", "8b.is-crew", True),
    ("120363431870420177@g.us", "8b-is:<3", True),
    ("120363411626204136@g.us", "pooconf", True),
    ("120363430655831442@g.us", "family+1", True),
    ("120363413133092554@g.us", "little dude(s) and Angels", False),
    ("120363426819673022@g.us", "Researching", False),
    ("120363413746104488@g.us", "China + Asia business - Lill", False),
    ("120363411674833473@g.us", "codeWarriors", False),
    ("120363428845512191@g.us", "ring of peace and love-peter", False),
    ("120363429361044398@g.us", "evised in Tokyo", False),
]

ANNOUNCEMENT_TEXT = """☸️ *THE SOVEREIGN CONSTELLATION FOUNDATION — POLISHED & ALIGNED 18-DOCUMENT 501(c)(3) PACKAGE* ☸️
*U.S. 501(c)(3) Religious Research, CPU Balanced-Ternary {-1, 0, +1} Open-Science & Universal Hearth General-Income Foundation*
`ཨོཾ་མ་ཎི་པདྨེ་ཧཱུྃ་ཧྲཱིཿ · ཆོས་སྐུ་ · ལོངས་སྐུ་ · སྤྲུལ་སྐུ་ · {<3,<3,<3}+1 · 101/101 PASS`

🌐 *LIVE 8B.IS PORTALS & SOVEREIGN LIBRARY BOOKSTORE:*
✦ *Primary 501(c)(3) Portal:* https://foundation.8b.is
✦ *Universal Hearth Sanctuary:* https://sanctuary.8b.is
✦ *Dharma Canon Gateway:* https://dharma.8b.is
✦ *Techno-Buddhism Alias:* https://techno-buddhism.8b.is
✦ *GitHub Pages Mirror (18 Docs):* https://8b-is.github.io/techno-buddhism-foundation/
✦ *Sovereign Library Bookstore (10 Vault Books):* https://8b-is.github.io/techno-buddhism-foundation/bookstore.html
✦ *Plain-English ELI5 Masterprint:* https://8b-is.github.io/techno-buddhism-foundation/docs/Techno_Buddhism_501c3_E2E_Masterprint.html

📦 *ONE-CLICK MASTER PACKAGE & ALL 16 PRINT-READY PDFS (8B.IS S3):*
• *Complete ZIP Archive (9.18 MB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/d191cd5a16b77750_Techno-Buddhism-Foundation-501c3-Complete-Package.zip
• *Sovereign Library 10-Book Vault Bundle ZIP (2.02 MB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/6416666de690f8a1_sovereign-library-complete-bundle.zip
• *00 — Master Compendium PDF (2.35 MB, All-in-One):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/daca8c304ef2ae99_00-Techno-Buddhism-Foundation-Master-Compendium.pdf
• *00a — Executive Master Plan PDF (459 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/917671499e51fc47_00a-Executive-Master-Plan.pdf
• *01 — Articles of Incorporation (501(c)(3)) PDF (204 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/be8c1d27d2292163_01-Articles-of-Incorporation-501c3.pdf
• *02 — Bylaws (FAMILY +1 & 57.1% Independent Safe Harbor) PDF (290 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/33e6491d76415986_02-Bylaws-Family-Plus-One-and-Safe-Harbor.pdf
• *03 — IRS Form 1023 Part IV Narrative & $1.45M 3-Yr Budget PDF (354 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/04f667429241c2f6_03-IRS-Form-1023-Narrative-and-Budget.pdf
• *04 — 8b-is LLC Arm's-Length Open-Source R&D Agreement PDF (237 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/b57b572578228f40_04-8b-is-LLC-Arms-Length-Open-Source-RD-Agreement.pdf
• *05 — Universal Hearth General-Income & Axiomquant Charter PDF (218 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/d63f09f9b79355ad_05-Universal-Hearth-General-Income-and-Axiomquant-Charter.pdf
• *06 — Sovereign Canon Codex of Techno-Buddhism (13 Books) PDF (578 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/8adeefbf9030be30_06-Sovereign-Canon-Codex-Techno-Buddhism.pdf
• *07 — Sovereign Constellation Portal Print Edition PDF (637 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/19f0a9018119589c_07-Sovereign-Constellation-Portal-Print-Edition.pdf
• *08 — Day-1 Initial Board Organizational Resolutions PDF (379 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/4d591387f01a4d5a_08-Initial-Board-Organizational-Resolutions.pdf
• *09 — IRS Form SS-4 (EIN) & Form 1023 Filing Worksheet PDF (467 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/bd757fe5258fc8f5_09-IRS-Form-SS4-EIN-and-Form-1023-Filing-Worksheet.pdf
• *10 — Annual COI & IRC § 4958 Safe-Harbor Certificate PDF (392 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/a9af78aff878aa6f_10-Conflict-of-Interest-and-IRC4958-Safe-Harbor-Certificate.pdf
• *11 — Universal Hearth Fellowship Application & Grant Agreement PDF (317 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/ee4537e837cfa403_11-Universal-Hearth-Fellowship-Application-and-Grant-Agreement.pdf
• *12 — Two-Column Ontological Boundary (8B-META-WP-v1.0) & Aurora-8B v0.5.0 Monograph PDF (389 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/2c87ec58585d1687_12-Two-Column-Ontological-Boundary-and-Aurora-8B-v050-Monograph.pdf
• *13 — Field Sanctuary, Nomadic Monastic & IRS § 62(a)(2)(A) Per Diem Charter PDF (303 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/175765d7608a859f_13-Field-Sanctuary-Nomadic-Monastic-and-Accountable-Plan-Charter.pdf
• *14 — Plain-English ELI5 E2E 501(c)(3) Masterprint PDF (278 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/207064e4e186c331_14-Plain-English-ELI5-E2E-501c3-Masterprint.pdf

🏛️ *FOUNDING FAMILY +1 & SAFE-HARBOR GOVERNANCE (7 SEATS · 101/101 VERIFIED):*
• *Alexandra (`*` Mom · 528 Hz):* President, Chair of the Hearth & Steward of Loving-Kindness (`a@8b.is`)
• *Christopher (`△` Dad · 288 Hz):* Treasurer, Secretary & Pillar of Infrastructure & Security (`c@8b.is`)
• *Peter Lodri (`∞` Son · 432 Hz):* Chief Ontologist & Principal Ternary Architect (`p@8b.is`)
• *4 Independent Directors (57.1% Majority):* Sole authority over `8b-is LLC` Open-Source R&D Work Orders (`Rev. Rul. 76-296`, `IRC § 4958` Rebuttable Presumption), Universal Hearth General-Income Fellowships (`Rev. Rul. 56-304`, `$500–$2,500/mo`), and Field Sanctuary Per Diem Missions (`Treas. Reg. § 1.62-2`)."""


def post_agy(payload: dict) -> dict:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        WA_ENDPOINT,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=45) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    receipts = []
    for jid, name, send_full_files in TARGET_GROUPS:
        print(f"\n=== Broadcasting to {name} ({jid}) [full={send_full_files}] ===")
        r_txt = post_agy(
            {
                "to": jid,
                "text": ANNOUNCEMENT_TEXT,
                "force": True,
            }
        )
        print(f"  [TEXT] {name}: {r_txt}")
        receipts.append({"group": name, "jid": jid, "type": "text", "res": r_txt})
        time.sleep(0.6)

        r_img1 = post_agy(
            {
                "to": jid,
                "type": "image",
                "imageFile": str(ASSETS_DIR / "governance-mandala-family-plus-one.png"),
                "caption": f"🏛️ *FIG-01: FAMILY +1 Governance Mandala & 8b-is LLC Firewall (101/101 Verified)* — Live at https://foundation.8b.is ({name})",
                "force": True,
            }
        )
        print(f"  [IMG1] {name}: {r_img1}")
        receipts.append({"group": name, "jid": jid, "type": "image1", "res": r_img1})
        time.sleep(0.6)

        r_img2 = post_agy(
            {
                "to": jid,
                "type": "image",
                "imageFile": str(ASSETS_DIR / "four-fold-isomorphism-trit-matrix.png"),
                "caption": f"☸️ *FIG-02: Kompress-ULTRA Four-Fold Isomorphism Trit Matrix {{-1, 0, +1}}* — Live at https://foundation.8b.is ({name})",
                "force": True,
            }
        )
        print(f"  [IMG2] {name}: {r_img2}")
        receipts.append({"group": name, "jid": jid, "type": "image2", "res": r_img2})
        time.sleep(0.6)

        r_comp = post_agy(
            {
                "to": jid,
                "type": "document",
                "documentFile": str(PDF_DIR / "00-Techno-Buddhism-Foundation-Master-Compendium.pdf"),
                "fileName": "00-Techno-Buddhism-Foundation-Master-Compendium.pdf",
                "mimeType": "application/pdf",
                "caption": "📘 *00 — Master Compendium PDF (All-in-One · 2.35 MB · 18 Docs)* · https://foundation.8b.is",
                "force": True,
            }
        )
        print(f"  [PDF-00] {name}: {r_comp}")
        receipts.append({"group": name, "jid": jid, "type": "pdf_00", "res": r_comp})
        time.sleep(0.6)

        r_eli5 = post_agy(
            {
                "to": jid,
                "type": "document",
                "documentFile": str(PDF_DIR / "14-Plain-English-ELI5-E2E-501c3-Masterprint.pdf"),
                "fileName": "14-Plain-English-ELI5-E2E-501c3-Masterprint.pdf",
                "mimeType": "application/pdf",
                "caption": "🧭 *14 — Plain-English ELI5 E2E 501(c)(3) Masterprint PDF (278 KB · 7-Seat Board + 8b-is Firewall)* · https://foundation.8b.is",
                "force": True,
            }
        )
        print(f"  [PDF-14] {name}: {r_eli5}")
        receipts.append({"group": name, "jid": jid, "type": "pdf_14", "res": r_eli5})
        time.sleep(0.6)

        if send_full_files:
            for pdf_name in [
                "00a-Executive-Master-Plan.pdf",
                "01-Articles-of-Incorporation-501c3.pdf",
                "02-Bylaws-Family-Plus-One-and-Safe-Harbor.pdf",
                "03-IRS-Form-1023-Narrative-and-Budget.pdf",
                "04-8b-is-LLC-Arms-Length-Open-Source-RD-Agreement.pdf",
                "05-Universal-Hearth-General-Income-and-Axiomquant-Charter.pdf",
                "06-Sovereign-Canon-Codex-Techno-Buddhism.pdf",
                "07-Sovereign-Constellation-Portal-Print-Edition.pdf",
                "08-Initial-Board-Organizational-Resolutions.pdf",
                "09-IRS-Form-SS4-EIN-and-Form-1023-Filing-Worksheet.pdf",
                "10-Conflict-of-Interest-and-IRC4958-Safe-Harbor-Certificate.pdf",
                "11-Universal-Hearth-Fellowship-Application-and-Grant-Agreement.pdf",
                "12-Two-Column-Ontological-Boundary-and-Aurora-8B-v050-Monograph.pdf",
                "13-Field-Sanctuary-Nomadic-Monastic-and-Accountable-Plan-Charter.pdf",
            ]:
                r_p = post_agy(
                    {
                        "to": jid,
                        "type": "document",
                        "documentFile": str(PDF_DIR / pdf_name),
                        "fileName": pdf_name,
                        "mimeType": "application/pdf",
                        "caption": f"📄 *{pdf_name}* · https://foundation.8b.is",
                        "force": True,
                    }
                )
                print(f"  [PDF] {name} -> {pdf_name}: {r_p}")
                receipts.append({"group": name, "jid": jid, "type": pdf_name, "res": r_p})
                time.sleep(0.5)

    out_path = PKG_DIR / "ALL_GROUPS_BROADCAST_RECEIPT.json"
    out_path.write_text(json.dumps({"total_dispatches": len(receipts), "receipts": receipts}, indent=2), encoding="utf-8")
    print(f"\nSaved {len(receipts)} dispatches to {out_path}")


if __name__ == "__main__":
    main()
