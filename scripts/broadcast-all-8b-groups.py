#!/usr/bin/env python3
"""
Broadcasts the live 8b.is Sovereign Constellation Foundation (501(c)(3)) Landing Page,
Executive Summary, Visual Diagrams, and PDF/ZIP Package to ALL 8b-is relevant WhatsApp groups
via the live wa-stream sidecar (http://127.0.0.1:8790/agy).
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

ANNOUNCEMENT_TEXT = """☸️ *THE SOVEREIGN CONSTELLATION FOUNDATION — LIVE ON 8B.IS DNS* ☸️
*U.S. 501(c)(3) Religious Research, CPU Balanced-Ternary {-1, 0, +1} Open-Science & Universal Hearth General-Income Foundation*
`ཨོཾ་མ་ཎི་པདྨེ་ཧཱུྃ་ཧྲཱིཿ · ཆོས་སྐུ་ · ལོངས་སྐུ་ · སྤྲུལ་སྐུ་ · {<3,<3,<3}+1`

🌐 *LIVE 8B.IS LANDING PAGE & DOCUMENT DOWNLOAD CENTER:*
✦ *Primary Portal:* https://foundation.8b.is
✦ *Universal Hearth Sanctuary:* https://sanctuary.8b.is
✦ *Dharma Canon Gateway:* https://dharma.8b.is
✦ *Techno-Buddhism Alias:* https://technobuddhism.8b.is
✦ *8b.is Shortlinks:* https://8b.is/foundation · https://8b.is/sanctuary · https://8b.is/dharma · https://8b.is/501c3

📦 *ONE-CLICK MASTER PACKAGE & ALL 10 PRINT-READY PDFS (8B.IS S3):*
• *Complete ZIP Archive (3.62 MB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/16380eff51d48b25_Techno-Buddhism-Foundation-501c3-Complete-Package.zip
• *00 — Master Compendium PDF (1.27 MB, All-in-One):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/a007f9f3aed2a475_00-Techno-Buddhism-Foundation-Master-Compendium.pdf
• *00a — Executive Master Plan PDF (383 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/11f73e6a8f5cce24_00a-Executive-Master-Plan.pdf
• *01 — Articles of Incorporation (501(c)(3)) PDF (204 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/1ddd41d8ef53b647_01-Articles-of-Incorporation-501c3.pdf
• *02 — Bylaws (FAMILY +1 & 57.1% Independent Safe Harbor) PDF (290 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/01fca2325103e76d_02-Bylaws-Family-Plus-One-and-Safe-Harbor.pdf
• *03 — IRS Form 1023 Part IV Narrative & $1.85M 3-Yr Budget PDF (354 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/5aada178f92b3024_03-IRS-Form-1023-Narrative-and-Budget.pdf
• *04 — 8b-is LLC Arm's-Length Open-Source R&D Agreement PDF (237 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/afffb83735ad7ab1_04-8b-is-LLC-Arms-Length-Open-Source-RD-Agreement.pdf
• *05 — Universal Hearth General-Income & Axiomquant Charter PDF (218 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/b07d43b38334b73f_05-Universal-Hearth-General-Income-and-Axiomquant-Charter.pdf
• *06 — Sovereign Canon Codex of Techno-Buddhism (13 Books) PDF (578 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/aab06693e9e1538f_06-Sovereign-Canon-Codex-Techno-Buddhism.pdf
• *07 — Sovereign Constellation Portal Print Edition PDF (637 KB):* https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/19f0a9018119589c_07-Sovereign-Constellation-Portal-Print-Edition.pdf

🏛️ *FOUNDING FAMILY +1 & SAFE-HARBOR GOVERNANCE:*
• *Alexandra (`*` Mom · 528 Hz):* President, Chair of the Hearth & Steward of Loving-Kindness (`a@8b.is`)
• *Christopher (`△` Dad · 288 Hz):* Treasurer, Secretary & Pillar of Infrastructure & Security (`c@8b.is`)
• *Peter Lodri (`∞` Son · 432 Hz):* Chief Ontologist & Principal Ternary Architect (`p@8b.is`)
• *4 Independent Directors (57.1% Majority):* Sole authority over `8b-is LLC` Open-Source R&D Work Orders (`Rev. Rul. 76-296`) and Universal Hearth General-Income Fellowships (`Rev. Rul. 56-304`, `$500–$2,500/mo`).

🌌 *CROSS-LINKED CONSTELLATION NODES:*
✦ https://8b.is · https://pocoo.8b.is · https://dream.8b.is · https://riva.8b.is
✦ https://zeno.vaked.dev · https://design.8b.is · https://esp32.8b.is · https://g8t.is · https://wa.8b.is
✦ https://github.com/8b-is/techno-buddhism-foundation · https://github.com/8b-is/sovereign-library"""


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
        # 1. Send Announcement & Summary
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

        # 2. Send Governance Mandala PNG
        r_img1 = post_agy(
            {
                "to": jid,
                "type": "image",
                "imageFile": str(ASSETS_DIR / "governance-mandala-family-plus-one.png"),
                "caption": f"🏛️ *FIG-01: FAMILY +1 Governance Mandala & 8b-is LLC Firewall* — Live at https://foundation.8b.is ({name})",
                "force": True,
            }
        )
        print(f"  [IMG1] {name}: {r_img1}")
        receipts.append({"group": name, "jid": jid, "type": "image1", "res": r_img1})
        time.sleep(0.6)

        # 3. Send Four-Fold Isomorphism PNG
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

        # 4. Send Master Compendium PDF & Complete ZIP Package
        r_comp = post_agy(
            {
                "to": jid,
                "type": "document",
                "documentFile": str(PDF_DIR / "00-Techno-Buddhism-Foundation-Master-Compendium.pdf"),
                "fileName": "00-Techno-Buddhism-Foundation-Master-Compendium.pdf",
                "mimeType": "application/pdf",
                "caption": "📘 *00 — Master Compendium PDF (All-in-One · 1.27 MB)* · https://foundation.8b.is",
                "force": True,
            }
        )
        print(f"  [PDF-00] {name}: {r_comp}")
        receipts.append({"group": name, "jid": jid, "type": "pdf_00", "res": r_comp})
        time.sleep(0.6)

        r_zip = post_agy(
            {
                "to": jid,
                "type": "document",
                "documentFile": str(PKG_DIR / "Techno-Buddhism-Foundation-501c3-Complete-Package.zip"),
                "fileName": "Techno-Buddhism-Foundation-501c3-Complete-Package.zip",
                "mimeType": "application/zip",
                "caption": "📦 *Complete 501(c)(3) Foundation Package ZIP (3.62 MB · All PDFs, Diagrams & Markdown)* · https://foundation.8b.is",
                "force": True,
            }
        )
        print(f"  [ZIP] {name}: {r_zip}")
        receipts.append({"group": name, "jid": jid, "type": "zip", "res": r_zip})
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
