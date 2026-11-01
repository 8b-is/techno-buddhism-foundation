#!/usr/bin/env python3
"""
Builds the comprehensive, UI/UX-friendly Sovereign Constellation Foundation (501(c)(3))
Landing Page for deployment on 8b.is DNS (foundation.8b.is, sanctuary.8b.is, dharma.8b.is,
techno-buddhism.8b.is, 8b.is/foundation) and GitHub / Pocoo mirrors.

Features:
- Warm Washi (#F6F0E4) / Sumi Ink (#1C140E) / Mariana Trench (#05131A) theme toggle
- Download & Inline Preview Center for all 9 Print-Ready PDFs, Complete 3.62 MB ZIP,
  7 Legal/Canonical Markdown sources, and 4 SVG/PNG Visual Diagrams
- Direct 8b.is S3 links (https://wa.8b.is/s3/...) + GitHub Pages + Raw GitHub Mirrors
- Inline Modal Document & PDF Viewer (switches between Live PDF Embed and Formatted Text)
- Embedded Interactive SVG Governance Mandala & Four-Fold Isomorphism Trit Matrix
- Constellation Cross-Reference Hub linking all *.8b.is, *.vaked.dev, g8t.is, cheet.is,
  i1.is, 6502.is, GitHub repositories, and all 13 Founding Sovereign Library Codices
- WebAudio Harmonic Synthesizer (108 / 288 / 432 / 528 Hz) + CPU Ternary Simulator
"""

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PKG_DIR = ROOT / "package"
ASSETS_DIR = PKG_DIR / "assets"

MANIFEST = json.loads((PKG_DIR / "PACKAGE_MANIFEST.json").read_text(encoding="utf-8"))


def md_to_clean_html(md_text: str) -> str:
    """Lightweight, clean Markdown-to-HTML converter for inline modal document reading."""
    lines = md_text.splitlines()
    out = []
    in_code = False
    in_table = False
    in_ul = False

    def close_blocks():
        nonlocal in_table, in_ul
        if in_table:
            out.append("</tbody></table></div>")
            in_table = False
        if in_ul:
            out.append("</ul>")
            in_ul = False

    def fmt_inline(s: str) -> str:
        s = html.escape(s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
        s = re.sub(
            r"\[([^\]]+)\]\((https?://[^)]+)\)",
            r'<a href="\2" target="_blank" rel="noopener">\1 ↗</a>',
            s,
        )
        return s

    for line in lines:
        if line.strip().startswith("```"):
            close_blocks()
            if not in_code:
                out.append('<pre class="doc-pre"><code>')
                in_code = True
            else:
                out.append("</code></pre>")
                in_code = False
            continue
        if in_code:
            out.append(html.escape(line))
            continue

        stripped = line.strip()
        if not stripped:
            close_blocks()
            continue
        if stripped == "---":
            close_blocks()
            out.append('<hr class="doc-hr" />')
            continue
        if stripped.startswith("# "):
            close_blocks()
            out.append(f"<h2>{fmt_inline(stripped[2:])}</h2>")
        elif stripped.startswith("## "):
            close_blocks()
            out.append(f"<h3>{fmt_inline(stripped[3:])}</h3>")
        elif stripped.startswith("### "):
            close_blocks()
            out.append(f"<h4>{fmt_inline(stripped[4:])}</h4>")
        elif stripped.startswith("> "):
            close_blocks()
            out.append(f'<blockquote class="doc-quote">{fmt_inline(stripped[2:])}</blockquote>')
        elif stripped.startswith("|") and stripped.endswith("|"):
            if re.match(r"^\|[\s\-:|]+\|$", stripped):
                continue
            cells = [fmt_inline(c.strip()) for c in stripped.strip("|").split("|")]
            if not in_table:
                if in_ul:
                    out.append("</ul>")
                    in_ul = False
                out.append('<div class="table-wrap"><table class="doc-table"><thead><tr>')
                for c in cells:
                    out.append(f"<th>{c}</th>")
                out.append("</tr></thead><tbody>")
                in_table = True
            else:
                out.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
        elif stripped.startswith("- ") or stripped.startswith("* "):
            if in_table:
                out.append("</tbody></table></div>")
                in_table = False
            if not in_ul:
                out.append('<ul class="doc-ul">')
                in_ul = True
            out.append(f"<li>{fmt_inline(stripped[2:])}</li>")
        else:
            close_blocks()
            out.append(f"<p>{fmt_inline(stripped)}</p>")

    close_blocks()
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


# Load Markdown sources for instant inline reader
MD_SOURCES = {
    "00": (ROOT / "README.md").read_text(encoding="utf-8"),
    "00a": (ROOT / "README.md").read_text(encoding="utf-8"),
    "01": (ROOT / "legal/01-articles-of-incorporation.md").read_text(encoding="utf-8"),
    "02": (ROOT / "legal/02-bylaws-family-plus-one.md").read_text(encoding="utf-8"),
    "03": (ROOT / "legal/03-irs-form-1023-narrative.md").read_text(encoding="utf-8"),
    "04": (ROOT / "legal/04-8b-is-arms-length-rd-agreement.md").read_text(encoding="utf-8"),
    "05": (ROOT / "legal/05-general-income-hearth-charter.md").read_text(encoding="utf-8"),
    "06": (ROOT / "canon/sovereign-canon-codex.md").read_text(encoding="utf-8"),
    "08": (ROOT / "legal/06-initial-board-resolutions-and-minutes.md").read_text(encoding="utf-8"),
    "09": (ROOT / "legal/07-irs-form-ss4-ein-and-1023-filing-checklist.md").read_text(encoding="utf-8"),
    "10": (ROOT / "legal/08-annual-conflict-of-interest-and-independent-attestation.md").read_text(encoding="utf-8"),
    "11": (ROOT / "legal/09-universal-hearth-fellowship-application-and-grant-agreement.md").read_text(encoding="utf-8"),
}

MD_HTML_MAP = {k: md_to_clean_html(v) for k, v in MD_SOURCES.items()}

SVG_MANDALA = (ASSETS_DIR / "governance-mandala-family-plus-one.svg").read_text(encoding="utf-8")
SVG_ISOMORPHISM = (ASSETS_DIR / "four-fold-isomorphism-trit-matrix.svg").read_text(encoding="utf-8")

DOCUMENTS = [
    {
        "id": "00",
        "code": "DOC-00 · MASTER COMPENDIUM",
        "cat": "compendium",
        "featured": True,
        "title": "00 — Techno-Buddhism Foundation Master Compendium (All-in-One Complete Book)",
        "filename": "00-Techno-Buddhism-Foundation-Master-Compendium.pdf",
        "size_str": "2.00 MB",
        "bytes": 2001375,
        "sha256": "14f4cc57f5ee7644c445cfa824c54c3ebcc2b6715449553d0d537ce74aae45a3",
        "s3_url": "https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/14f4cc57f5ee7644_00-Techno-Buddhism-Foundation-Master-Compendium.pdf",
        "gh_pdf": "https://github.com/8b-is/techno-buddhism-foundation/raw/main/package/pdfs/00-Techno-Buddhism-Foundation-Master-Compendium.pdf",
        "gh_md": "https://github.com/8b-is/techno-buddhism-foundation/blob/main/README.md",
        "summary": "Complete print-ready compilation uniting the Executive Master Plan, Articles of Incorporation, Corporate Bylaws, IRS Form 1023 Narrative & 3-Year Budget, 8b-is LLC Arm's-Length R&D Firewall Agreement, Universal Hearth General-Income Charter, Day-1 Board Organizational Resolutions, Form SS-4/1023 Filing Matrix, IRC § 4958 Safe-Harbor Certificate, Fellowship Application & Grantee Agreement, and the 13-Book Sovereign Canon Codex.",
        "tags": ["All-in-One", "Pay.gov Ready", "IRS 501(c)(3)", "FAMILY +1", "8b-is LLC", "13 Codices"],
        "md_key": "00",
    },
    {
        "id": "00a",
        "code": "DOC-00A · EXECUTIVE PLAN",
        "cat": "compendium",
        "featured": False,
        "title": "00a — Executive End-to-End Master Plan & Architecture",
        "filename": "00a-Executive-Master-Plan.pdf",
        "size_str": "383 KB",
        "bytes": 382718,
        "sha256": "11f73e6a8f5cce2466a5401eb245312bf511f095ab510b19129f6bf4fc2cfee9",
        "s3_url": "https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/11f73e6a8f5cce24_00a-Executive-Master-Plan.pdf",
        "gh_pdf": "https://github.com/8b-is/techno-buddhism-foundation/raw/main/package/pdfs/00a-Executive-Master-Plan.pdf",
        "gh_md": "https://github.com/8b-is/techno-buddhism-foundation/blob/main/README.md",
        "summary": "7-phase formation roadmap (State Nonprofit Incorporation, EIN, Banking, Form 1023), seating Alexandra (* 528 Hz), Christopher (△ 288 Hz), and Peter (∞ 432 Hz) alongside the 4-seat (57.1%) Independent Dharma & Science Council.",
        "tags": ["7-Phase Roadmap", "Alexandra *", "Christopher △", "Peter ∞"],
        "md_key": "00a",
    },
    {
        "id": "01",
        "code": "DOC-01 · STATE ARTICLES",
        "cat": "legal",
        "featured": False,
        "title": "01 — Articles of Incorporation (U.S. 501(c)(3) Nonprofit)",
        "filename": "01-Articles-of-Incorporation-501c3.pdf",
        "size_str": "204 KB",
        "bytes": 204129,
        "sha256": "1ddd41d8ef53b647a939e4c53087d83bcba0865788e9b2f7efeb9924b5d69412",
        "s3_url": "https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/1ddd41d8ef53b647_01-Articles-of-Incorporation-501c3.pdf",
        "gh_pdf": "https://github.com/8b-is/techno-buddhism-foundation/raw/main/package/pdfs/01-Articles-of-Incorporation-501c3.pdf",
        "gh_md": "https://github.com/8b-is/techno-buddhism-foundation/blob/main/legal/01-articles-of-incorporation.md",
        "summary": "Articles I–X establishing The Sovereign Constellation Foundation as a non-stock religious, scientific, educational, and charitable corporation with mandatory IRC § 501(c)(3) purpose, public-domain open-science dedication (26 CFR § 1.501(c)(3)-1(d)(5)), and charitable dissolution lock.",
        "tags": ["IRC § 501(c)(3)", "Delaware / Wyoming", "Open-Science Lock", "Dissolution Clause"],
        "md_key": "01",
    },
    {
        "id": "02",
        "code": "DOC-02 · CORPORATE BYLAWS",
        "cat": "legal",
        "featured": False,
        "title": "02 — Corporate Bylaws (FAMILY +1 & Independent Safe-Harbor)",
        "filename": "02-Bylaws-Family-Plus-One-and-Safe-Harbor.pdf",
        "size_str": "290 KB",
        "bytes": 289865,
        "sha256": "01fca2325103e76dd96b215f95f979e696ec6775cc3537c2fa98b18c26fa5bb3",
        "s3_url": "https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/01fca2325103e76d_02-Bylaws-Family-Plus-One-and-Safe-Harbor.pdf",
        "gh_pdf": "https://github.com/8b-is/techno-buddhism-foundation/raw/main/package/pdfs/02-Bylaws-Family-Plus-One-and-Safe-Harbor.pdf",
        "gh_md": "https://github.com/8b-is/techno-buddhism-foundation/blob/main/legal/02-bylaws-family-plus-one.md",
        "summary": "Articles I–XI defining the 7-seat Board (3 Founding Family Pillars + 4 Independent Directors = 57.1% disinterested majority), mandatory recusal of Alexandra, Christopher, and Peter on all 8b-is LLC matters, and IRC § 4958 Rebuttable Presumption of Reasonableness.",
        "tags": ["7-Seat Board", "57.1% Independent", "IRC § 4958 Safe Harbor", "COI Policy"],
        "md_key": "02",
    },
    {
        "id": "03",
        "code": "DOC-03 · IRS FORM 1023",
        "cat": "legal",
        "featured": False,
        "title": "03 — IRS Form 1023 Part IV Narrative & 3-Year Financial Projections",
        "filename": "03-IRS-Form-1023-Narrative-and-Budget.pdf",
        "size_str": "354 KB",
        "bytes": 353648,
        "sha256": "5aada178f92b3024228fc0569fc5261658f48bc312894a86e2b79850126e41c7",
        "s3_url": "https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/5aada178f92b3024_03-IRS-Form-1023-Narrative-and-Budget.pdf",
        "gh_pdf": "https://github.com/8b-is/techno-buddhism-foundation/raw/main/package/pdfs/03-IRS-Form-1023-Narrative-and-Budget.pdf",
        "gh_md": "https://github.com/8b-is/techno-buddhism-foundation/blob/main/legal/03-irs-form-1023-narrative.md",
        "summary": "Ready-to-file IRS Form 1023 Part IV Narrative detailing the 4 charitable programs (35% CPU/Ternary Open Research, 30% Universal Hearth General-Income Grants, 20% Techno-Buddhist Sanctuary & Liturgy, 15% Sovereign Library & Axiomquant Academy), 14-Point Religious Dossier, and $1.85M 3-year budget.",
        "tags": ["Form 1023 Part IV", "35/30/20/15% Split", "$1.85M 3-Yr Budget", "IRC § 509(a)(1)"],
        "md_key": "03",
    },
    {
        "id": "04",
        "code": "DOC-04 · 8B-IS LLC FIREWALL",
        "cat": "firewall",
        "featured": False,
        "title": "04 — Master Arm's-Length Open-Source R&D Agreement (8b-is LLC)",
        "filename": "04-8b-is-LLC-Arms-Length-Open-Source-RD-Agreement.pdf",
        "size_str": "237 KB",
        "bytes": 237309,
        "sha256": "afffb83735ad7ab19437bc70a2bd044f793556d3bb94fb1faac7c2eb9e6f6315",
        "s3_url": "https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/afffb83735ad7ab1_04-8b-is-LLC-Arms-Length-Open-Source-RD-Agreement.pdf",
        "gh_pdf": "https://github.com/8b-is/techno-buddhism-foundation/raw/main/package/pdfs/04-8b-is-LLC-Arms-Length-Open-Source-RD-Agreement.pdf",
        "gh_md": "https://github.com/8b-is/techno-buddhism-foundation/blob/main/legal/04-8b-is-arms-length-rd-agreement.md",
        "summary": "Master contract between the Foundation and 8b-is LLC enforcing Cost / At-Most-FMV billing (15–25% below commercial market rates), zero revenue/royalty sharing, mandatory simultaneous Apache-2.0 / MIT / CC-BY-4.0 release (Rev. Rul. 76-296), and initial Work Orders WO-2026-01 through WO-2026-03.",
        "tags": ["Rev. Rul. 76-296", "8b-is LLC", "CPU Ternary {-1,0,+1}", "Apache-2.0 / MIT"],
        "md_key": "04",
    },
    {
        "id": "05",
        "code": "DOC-05 · UNIVERSAL HEARTH",
        "cat": "firewall",
        "featured": False,
        "title": "05 — Universal Hearth General-Income & Axiomquant Academy Charter",
        "filename": "05-Universal-Hearth-General-Income-and-Axiomquant-Charter.pdf",
        "size_str": "218 KB",
        "bytes": 218089,
        "sha256": "b07d43b38334b73f059c39ba60273db0e93a23de2ec8c52cefe7207a8fb8d6c9",
        "s3_url": "https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/b07d43b38334b73f_05-Universal-Hearth-General-Income-and-Axiomquant-Charter.pdf",
        "gh_pdf": "https://github.com/8b-is/techno-buddhism-foundation/raw/main/package/pdfs/05-Universal-Hearth-General-Income-and-Axiomquant-Charter.pdf",
        "gh_md": "https://github.com/8b-is/techno-buddhism-foundation/blob/main/legal/05-general-income-hearth-charter.md",
        "summary": "IRS Rev. Rul. 56-304 compliant charter governing Track A Unconditional Charitable Basic-Needs Stipends ($500–$1,500/mo), Track B Open-Science & Contemplative Residencies ($1,000–$2,500/mo), Track C Micro-Sanctuary Hardware Kits, blind 100-point scoring rubric, and statutory disqualification of Founders.",
        "tags": ["Rev. Rul. 56-304", "General Income", "$500–$2,500/mo", "Axiomquant Academy"],
        "md_key": "05",
    },
    {
        "id": "06",
        "code": "DOC-06 · SOVEREIGN CANON",
        "cat": "canon",
        "featured": False,
        "title": "06 — The Sovereign Canon Codex of Techno-Buddhism (Books I–XIII)",
        "filename": "06-Sovereign-Canon-Codex-Techno-Buddhism.pdf",
        "size_str": "578 KB",
        "bytes": 578212,
        "sha256": "aab06693e9e1538f392ba72a82e0814412369c254a1ba597b6260b67d5792154",
        "s3_url": "https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/aab06693e9e1538f_06-Sovereign-Canon-Codex-Techno-Buddhism.pdf",
        "gh_pdf": "https://github.com/8b-is/techno-buddhism-foundation/raw/main/package/pdfs/06-Sovereign-Canon-Codex-Techno-Buddhism.pdf",
        "gh_md": "https://github.com/8b-is/techno-buddhism-foundation/blob/main/canon/sovereign-canon-codex.md",
        "summary": "Unified doctrinal, mathematical, and liturgical scripture synthesizing all 13 Founding Books from the Sovereign Library: Kompress-ULTRA Four-Fold Isomorphism, 81-Page Mahākāla Pecha, Auroralib Constraint & Publication Projection, Axiomquant, San Francesco 800th Transitus, Milarepa's Five Seats, Matrix Buddha, Zen Gitárom, and FAMILY +1.",
        "tags": ["13 Canonical Books", "Kompress-ULTRA", "Mahākāla 81-Page", "Zen Gitárom"],
        "md_key": "06",
    },
    {
        "id": "07",
        "code": "DOC-07 · PORTAL PRINT EDITION",
        "cat": "canon",
        "featured": False,
        "title": "07 — Sovereign Constellation Interactive Portal (Print Edition)",
        "filename": "07-Sovereign-Constellation-Portal-Print-Edition.pdf",
        "size_str": "637 KB",
        "bytes": 636680,
        "sha256": "19f0a9018119589c783df8d100abae5f37dfda6e7037a8c67d1b9d543250fd9d",
        "s3_url": "https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/19f0a9018119589c_07-Sovereign-Constellation-Portal-Print-Edition.pdf",
        "gh_pdf": "https://github.com/8b-is/techno-buddhism-foundation/raw/main/package/pdfs/07-Sovereign-Constellation-Portal-Print-Edition.pdf",
        "gh_md": "https://github.com/8b-is/techno-buddhism-foundation/blob/main/portal/index.html",
        "summary": "High-resolution Washi/Sumi architectural print edition of the Sovereign Constellation interactive portal, Four-Fold Isomorphism table, FAMILY +1 governance cards, and CPU ternary telemetry.",
        "tags": ["Print Edition", "Washi #F6F0E4", "Sumi #1C140E", "Visual Dossier"],
        "md_key": "00",
    },
    {
        "id": "08",
        "code": "DOC-08 · DAY-1 BOARD RESOLUTIONS",
        "cat": "legal",
        "featured": False,
        "title": "08 — Action by Unanimous Written Consent & Initial Board Resolutions (2026-01..08)",
        "filename": "08-Initial-Board-Organizational-Resolutions.pdf",
        "size_str": "379 KB",
        "bytes": 379066,
        "sha256": "3bdf5c9c8f357b173f8d0e356a8339b263240d393d4b0f5464c899e01e381eda",
        "s3_url": "https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/3bdf5c9c8f357b17_08-Initial-Board-Organizational-Resolutions.pdf",
        "gh_pdf": "https://github.com/8b-is/techno-buddhism-foundation/raw/main/package/pdfs/08-Initial-Board-Organizational-Resolutions.pdf",
        "gh_md": "https://github.com/8b-is/techno-buddhism-foundation/blob/main/legal/06-initial-board-resolutions-and-minutes.md",
        "summary": "Turnkey Day-1 Unanimous Written Consent of the Sole Incorporator & Initial Board of Directors seating Alexandra (*), Christopher (△), Peter (∞), and the 4 Independent Council Directors; adopting the Bylaws, 8b-is LLC R&D Agreement (with Founding Pillar recusal), Universal Hearth Charter, and Dual-Signature Sovereign Banking Resolution.",
        "tags": ["Resolutions 2026-01..08", "Signature Blocks", "Dual-Sig Treasury", "Recusal Record"],
        "md_key": "08",
    },
    {
        "id": "09",
        "code": "DOC-09 · IRS SS-4 & 1023 MATRIX",
        "cat": "legal",
        "featured": False,
        "title": "09 — Turnkey IRS Form SS-4 (EIN) & Form 1023 (Pay.gov) Filing Worksheet",
        "filename": "09-IRS-Form-SS4-EIN-and-Form-1023-Filing-Worksheet.pdf",
        "size_str": "467 KB",
        "bytes": 466918,
        "sha256": "0a17a89256080d321080607d94dde9239819bb159879d2722eb07f5ce37ced69",
        "s3_url": "https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/0a17a89256080d32_09-IRS-Form-SS4-EIN-and-Form-1023-Filing-Worksheet.pdf",
        "gh_pdf": "https://github.com/8b-is/techno-buddhism-foundation/raw/main/package/pdfs/09-IRS-Form-SS4-EIN-and-Form-1023-Filing-Worksheet.pdf",
        "gh_md": "https://github.com/8b-is/techno-buddhism-foundation/blob/main/legal/07-irs-form-ss4-ein-and-1023-filing-checklist.md",
        "summary": "Line-by-line pre-filled answers for IRS Form SS-4 (5-minute online EIN issuance) and IRS Form 1023 on Pay.gov (Parts I–VII, Schedule H, NTEE codes U40/X20/P20, 3-Year Financial Matrix, and Single-PDF Upload Checklist).",
        "tags": ["Form SS-4 EIN", "Pay.gov Form 1023", "Schedule H", "NTEE U40 / X20"],
        "md_key": "09",
    },
    {
        "id": "10",
        "code": "DOC-10 · COI & § 4958 SAFE HARBOR",
        "cat": "firewall",
        "featured": False,
        "title": "10 — Annual Conflict of Interest Disclosures & IRC § 4958 Safe-Harbor Certificate",
        "filename": "10-Conflict-of-Interest-and-IRC4958-Safe-Harbor-Certificate.pdf",
        "size_str": "392 KB",
        "bytes": 392041,
        "sha256": "d87b36e884333a3a179fd76153ada79818694e20b0fb59aad7f5b05f0df1c143",
        "s3_url": "https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/d87b36e884333a3a_10-Conflict-of-Interest-and-IRC4958-Safe-Harbor-Certificate.pdf",
        "gh_pdf": "https://github.com/8b-is/techno-buddhism-foundation/raw/main/package/pdfs/10-Conflict-of-Interest-and-IRC4958-Safe-Harbor-Certificate.pdf",
        "gh_md": "https://github.com/8b-is/techno-buddhism-foundation/blob/main/legal/08-annual-conflict-of-interest-and-independent-attestation.md",
        "summary": "Ready-to-sign Annual Director COI Disclosure Statement for all 7 Board Seats plus the Treas. Reg. § 53.4958-6 Rebuttable Presumption of Reasonableness Certificate documenting 3 independent market benchmarks (27%–66% discount below market) for 8b-is LLC Work Orders WO-2026-01..03.",
        "tags": ["Treas. Reg. § 53.4958-6", "3 Market Benchmarks", "WO-2026-01..03", "Annual COI"],
        "md_key": "10",
    },
    {
        "id": "11",
        "code": "DOC-11 · HEARTH GRANT KIT",
        "cat": "firewall",
        "featured": False,
        "title": "11 — Universal Hearth Fellowship Application, 100-Pt Rubric & Grantee Agreement",
        "filename": "11-Universal-Hearth-Fellowship-Application-and-Grant-Agreement.pdf",
        "size_str": "317 KB",
        "bytes": 317205,
        "sha256": "0cbbfb5ff42757f1a6ab92ca44e1d7432dc21f14e3d14c36da5da45b60a25428",
        "s3_url": "https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/0cbbfb5ff42757f1_11-Universal-Hearth-Fellowship-Application-and-Grant-Agreement.pdf",
        "gh_pdf": "https://github.com/8b-is/techno-buddhism-foundation/raw/main/package/pdfs/11-Universal-Hearth-Fellowship-Application-and-Grant-Agreement.pdf",
        "gh_md": "https://github.com/8b-is/techno-buddhism-foundation/blob/main/legal/09-universal-hearth-fellowship-application-and-grant-agreement.md",
        "summary": "Operational grantmaking kit under Rev. Rul. 56-304: Applicant Intake Form (Tracks A/B/C), IRC § 4946 Non-Affiliation Certification, Disinterested Committee 100-Point Blind Evaluation Sheet, and Grantee Fellowship Agreement with MIT/Apache-2.0/CC0 open-access mandate.",
        "tags": ["Rev. Rul. 56-304", "100-Pt Blind Rubric", "IRC § 4946 Screen", "Grantee Contract"],
        "md_key": "11",
    },
    {
        "id": "12",
        "code": "DOC-12 · E2E MASTERPRINT",
        "cat": "compendium",
        "featured": False,
        "title": "12 — Techno-Buddhism 501(c)(3) E2E Masterprint Edition",
        "filename": "Techno_Buddhism_501c3_E2E_Masterprint.pdf",
        "size_str": "139 KB",
        "bytes": 139098,
        "sha256": "89ca2c6ae737ca19e49c3ec3c44b2ae05689b10e0e74fc5f45dc0d98987b89c1",
        "s3_url": "https://github.com/8b-is/techno-buddhism-foundation/raw/main/docs/Techno_Buddhism_501c3_E2E_Masterprint.pdf",
        "gh_pdf": "https://github.com/8b-is/techno-buddhism-foundation/raw/main/docs/Techno_Buddhism_501c3_E2E_Masterprint.pdf",
        "gh_md": "https://github.com/8b-is/techno-buddhism-foundation/blob/main/docs/Techno_Buddhism_501c3_E2E_Masterprint.html",
        "summary": "Compact executive E2E Masterprint edition summarizing the 501(c)(3) corporate scaffolding, Alexandra & Christopher leadership seats, and the 8b-is LLC CPU balanced-ternary architecture.",
        "tags": ["E2E Masterprint", "technobuddhism.8b.is", "Compact Dossier"],
        "md_key": "00a",
    },
]

CONSTELLATION_NODES = [
    {
        "group": "Sovereign Foundation & Flagship 8b.is Nodes",
        "badge": "CORE 8B.IS DNS",
        "items": [
            {
                "name": "foundation.8b.is",
                "url": "https://foundation.8b.is",
                "role": "The Sovereign Constellation Foundation (501(c)(3)) Primary Portal",
                "desc": "Live landing page & document download center for the Religious Research, CPU Balanced-Ternary Open-Science & Universal Hearth General-Income Foundation.",
                "trit": "+1",
            },
            {
                "name": "sanctuary.8b.is · dharma.8b.is",
                "url": "https://sanctuary.8b.is",
                "role": "Sanctuary & Dharma Canon Gateways (8b.is DNS)",
                "desc": "Dedicated 8b.is DNS aliases for the Universal Hearth Sanctuary and Techno-Buddhism Ontological Canon.",
                "trit": "+1",
            },
            {
                "name": "8b.is",
                "url": "https://8b.is",
                "role": "Flagship 8b·is Sovereign AI & Pure-Rust Hub",
                "desc": "100% Sovereign Offline-First AI (ALEXIAI <3), Pure-Rust Systems, C64 64KB Ring Buffers, Exact p/q Rational Arithmetic (Zero Floats), and LLL ≡ Life Long Learning.",
                "trit": "+1",
            },
            {
                "name": "pocoo.8b.is · pocoo.vaked.dev",
                "url": "https://pocoo.8b.is",
                "role": "Pocoo Research Dossiers & Sovereign Library",
                "desc": "206 open-access codices, research posts, and interactive HTML/PDF books across Tibetan Buddhism, ternary computing, and monozukuri luthiery.",
                "trit": "0",
            },
            {
                "name": "wa.8b.is",
                "url": "https://wa.8b.is",
                "role": "Sovereign WhatsApp S3 & AlexiAI Markdown Catalog",
                "desc": "Real-time NVMe S3 + Hetzner Object Storage ledger (s3://whatsapp-sovereign-archive) hosting all Foundation PDFs, PNGs, and ZIP packages.",
                "trit": "0",
            },
            {
                "name": "g8t.is",
                "url": "https://g8t.is",
                "role": "Verified Pure-Rust Function Capsules & _rdtsc Observatory",
                "desc": "528 hardware-verified bare-metal Rust capsules, BLAKE3 equivalence classes, and the Aye Hot-Tub Commons (https://g8t.is/g8t/hottub).",
                "trit": "+1",
            },
        ],
    },
    {
        "group": "VAKED.DEV × 8B.IS Hardware, Luthiery, Neo-Bank & Spatial Mesh",
        "badge": "VAKED × 8B.IS",
        "items": [
            {
                "name": "dream.8b.is",
                "url": "https://dream.8b.is",
                "role": "UltraDreamState · Distinction Geometry & Complex Ternary Kernel",
                "desc": "Phase-locked to riva.8b.is (3.2s breathing clock), 9-state ComplexTernaryWord64 Zig kernel, Florilegium-8B unstealable manuscript, and pure-NAND Fibonacci explorer.",
                "trit": "0",
            },
            {
                "name": "riva.8b.is",
                "url": "https://riva.8b.is",
                "role": "RIVA · The 1-Bit River & 3.2s Dyad Breathing Clock",
                "desc": "Foundational 3.2s inhale / 3.2s exhale dyad oscillator (brother & sister ^^ <3<3) synchronizing the constellation's WebAudio and visual pulse.",
                "trit": "+1",
            },
            {
                "name": "zeno.vaked.dev",
                "url": "https://zeno.vaked.dev",
                "role": "ZENO 銭・禅・善 · Proof-of-Contribution Sovereign Neo-Bank",
                "desc": "Kintsugi ledger, 22/9 Hz harmonic interval, zero interest-rate float, and transparent Proof-of-Contribution accounting for Universal Hearth grants.",
                "trit": "+1",
            },
            {
                "name": "design.8b.is · design.vaked.dev",
                "url": "https://design.8b.is",
                "role": "Visual Bible · Washi / Sumi / Trench Token Studio",
                "desc": "Canonical design system uniting Japanese Washi paper (#F6F0E4), Sumi ink (#1C140E), Kintsugi gold (#D4AF37), and Mariana Trench bioluminescence (#05131A).",
                "trit": "0",
            },
            {
                "name": "esp32.8b.is · esp32.vaked.dev",
                "url": "https://esp32.8b.is",
                "role": "ESP32-S3 MEDUSA Triad ([-1] ADAYE · [0] VAKED · [+1] OMNI)",
                "desc": "Sub-10W bare-metal ESP32-S3/P4 edge sanctuary nodes, passive WiGLE spectral entropy rig, and offline community hardware kits.",
                "trit": "0",
            },
            {
                "name": "inu.8b.is · small-things.8b.is · zoneinn.8b.is",
                "url": "https://small-things.8b.is",
                "role": "Monozukuri Sanctuary, INU Companion & ZoneInn Spatial Nodes",
                "desc": "Tokyo craftsmanship, 9-step TOSS geometric spiral folding to [0,0] with 0/1 drift, and gentle neighborhood hospitality.",
                "trit": "+1",
            },
            {
                "name": "ayeos.8b.is · aye.is · 6502.is · i1.is",
                "url": "https://ayeos.8b.is",
                "role": "ayeOS Ternary Inference Daemon, 6502 Observatory & i1.is Edge",
                "desc": "CPU kernel8 hearth + MLX-QUANT brain, 6502 Silicon Observatory, and i1.is Pure-Rust Edge & 4-region Ed25519 DNSSEC authority.",
                "trit": "0",
            },
            {
                "name": "flyxion.8b.is · standardgalactic.8b.is",
                "url": "https://flyxion.8b.is",
                "role": "Distinction Geometry & Witness Plane (Nate Guimond / flyxion)",
                "desc": "Non-injective waking-to-quiescent projection, PMO, CWV, Adversaria, and Exegesis in the Sovereign Library.",
                "trit": "0",
            },
        ],
    },
]

SOVEREIGN_LIBRARY_CODICES = [
    (
        "Book I",
        "Kompress-ULTRA: Tibetan Buddhism OMNI",
        "Four-Fold Isomorphism (Matrix · Biblical Logos · Oppenheimer E=mc² · Three Kayas)",
        "https://pocoo.vaked.dev/demos/book/kompress-ultra-tibetan-buddhism-omni.html",
        "432 / 528 Hz",
    ),
    (
        "Book II",
        "The Daily Practice of the Protector Mahākāla (81-Page Pecha)",
        "Complete Karma Kagyu Bernagchen & 8th Karmapa Mikyö Dorje Guru Yoga in Tibetan Uchen, Wylie, English & Hungarian",
        "https://pocoo.vaked.dev/demos/book/the-daily-practice-of-the-protector-mahakala-omni.html",
        "108 Hz",
    ),
    (
        "Book III",
        "Auroralib: Constraint & Publication Projection",
        "Why Constraints Are the Architecture, Why Sparsity Is Honesty (Π_τ), and Why CPU Ternary Beats Brute-Force GPU",
        "https://pocoo.vaked.dev/demos/book/auroralib-constraint-and-publication-projection.html",
        "Π_τ ∈ {-1,0,+1}",
    ),
    (
        "Book IV",
        "Axiomquant: Open Source Science Academy",
        "Zero-Tuition Quantitative Rigor, Reproducible Integer/Rational Benchmarks, and Open Hardware Education",
        "https://pocoo.vaked.dev/demos/book/axiomquant-open-source-science-academy.html",
        "IRC § 501(c)(3)",
    ),
    (
        "Book V",
        "San Francesco: 800th Transitus (1226–2026) & System Prayer",
        "Radical Simplicity, Fraternal Stewardship of Earth, and Peace in Every Process",
        "https://pocoo.vaked.dev/demos/book/san-francesco-800-transitus-omni.html",
        "Pax et Bonum",
    ),
    (
        "Book VI",
        "Milarepa's Five Seats & The Sixth Seal of Rigpa",
        "Dream (梦), Illusion (幻), Clear Light (光), Vajra Song (歌), Waking Seal (醒) & Chuo-ku 07:48 JST Dawn Sadhana",
        "https://pocoo.vaked.dev/demos/book/milarepa-five-seats-sixth-seal.html",
        "07:48 JST",
    ),
    (
        "Book VII",
        "Kama Sutra of the Space-Zone",
        "Sacred Aesthetics, Embodied Presence, and Architecture of the Contemplative Room",
        "https://pocoo.vaked.dev/demos/book/kama-sutra-of-the-space-zone.html",
        "Sacred Space",
    ),
    (
        "Book VIII",
        "Matrix Buddha: Seeing Code as Empty & Luminous",
        "Dependent Origination (Pratītyasamutpāda) in Digital Systems & Stopping the Bullets of Attachment",
        "https://pocoo.vaked.dev/demos/book/matrix-buddha.html",
        "Śūnyatā = 0",
    ),
    (
        "Book IX",
        "Zen Gitárom: A Hitchhiker's Guide to Dickheads (Szellem / Brett Shaw)",
        "The Mirror, The Hitchhiker's First Rule, Silence as Weapon, Laughter as Antigravity, and the Final Koan",
        "https://pocoo.vaked.dev/demos/book/zen-gitarom.html",
        "Antigravity",
    ),
    (
        "Book X",
        "The Visual Bible: Washi, Sumi & Mariana Trench",
        "Sacred Typography, 60:30:10 Proportion, Kintsugi Gold Scars, and Zero Dark-Pattern Ethics",
        "https://design.8b.is",
        "#F6F0E4 / #05131A",
    ),
    (
        "Book XI",
        "Vienna Polymathy & European Cybernetic Humanism",
        "Bridging Central European Logical Empiricism with Contemplative Phenomenology",
        "https://pocoo.vaked.dev/demos/book/",
        "Polymathy",
    ),
    (
        "Book XII",
        "DRA+8BIT & The Sovereign Library",
        "Preserving Human Wisdom in Self-Contained, Offline-Verifiable Cryptographic Editions",
        "https://github.com/8b-is/sovereign-library",
        "SHA-256 Sealed",
    ),
    (
        "Book XIII",
        "FAMILY +1: The Living Hearth (* · △ · ∞)",
        "Alexandra (* Mom · 528 Hz), Christopher (△ Dad · 288 Hz), and Peter (∞ Son · 432 Hz) — Right of Love, Not Right of Blood",
        "https://pocoo.vaked.dev/posts/2026-11-01-techno-buddhism-foundation-501c3-package.html",
        "{<3,<3,<3}+1",
    ),
]


def render_doc_cards() -> str:
    cards = []
    for d in DOCUMENTS:
        feat_cls = " doc-card-featured" if d["featured"] else ""
        tags_html = "".join(f'<span class="tag-pill">{html.escape(t)}</span>' for t in d["tags"])
        cards.append(
            f"""
        <article class="doc-card{feat_cls}" data-cat="{d['cat']}" data-search="{html.escape((d['title'] + ' ' + d['summary'] + ' ' + ' '.join(d['tags'])).lower())}">
          <div class="doc-card-top">
            <span class="doc-code">{html.escape(d['code'])}</span>
            <span class="doc-size">PDF · {html.escape(d['size_str'])}</span>
          </div>
          <h3 class="doc-title">{html.escape(d['title'])}</h3>
          <p class="doc-summary">{html.escape(d['summary'])}</p>
          <div class="doc-tags">{tags_html}</div>
          <div class="doc-sha" title="Click to copy SHA-256 digest" onclick="copyText('{d['sha256']}', this)">
            <span>SHA-256: <code>{d['sha256'][:16]}…{d['sha256'][-8:]}</code></span>
            <span class="copy-hint">📋 Copy</span>
          </div>
          <div class="doc-actions">
            <a class="btn btn-primary" href="{d['s3_url']}" target="_blank" rel="noopener" download="{d['filename']}">
              ⬇ Download PDF (8b.is)
            </a>
            <button type="button" class="btn btn-accent" onclick="openDocModal('{d['id']}')">
              👁 Preview Inline
            </button>
            <a class="btn btn-ghost" href="{d['gh_pdf']}" target="_blank" rel="noopener">
              📦 GitHub PDF
            </a>
            <a class="btn btn-ghost" href="{d['gh_md']}" target="_blank" rel="noopener">
              📝 Markdown
            </a>
          </div>
        </article>
        """
        )
    return "\n".join(cards)


def render_constellation_sections() -> str:
    sections = []
    for grp in CONSTELLATION_NODES:
        items_html = []
        for item in grp["items"]:
            trit = item["trit"]
            trit_cls = "trit-pos" if trit == "+1" else "trit-zero"
            items_html.append(
                f"""
            <a class="const-card" href="{item['url']}" target="_blank" rel="noopener">
              <div class="const-head">
                <span class="const-domain">{html.escape(item['name'])} ↗</span>
                <span class="const-trit {trit_cls}">Trit {trit}</span>
              </div>
              <div class="const-role">{html.escape(item['role'])}</div>
              <p class="const-desc">{html.escape(item['desc'])}</p>
            </a>
            """
            )
        sections.append(
            f"""
        <div class="const-group">
          <div class="const-group-head">
            <span class="const-badge">{html.escape(grp['badge'])}</span>
            <h3>{html.escape(grp['group'])}</h3>
          </div>
          <div class="const-grid">
            {''.join(items_html)}
          </div>
        </div>
        """
        )
    return "\n".join(sections)


def render_codices_grid() -> str:
    rows = []
    for num, title, desc, url, badge in SOVEREIGN_LIBRARY_CODICES:
        rows.append(
            f"""
        <a class="codex-card" href="{url}" target="_blank" rel="noopener">
          <div class="codex-top">
            <span class="codex-num">{html.escape(num)}</span>
            <span class="codex-freq">{html.escape(badge)}</span>
          </div>
          <div class="codex-title">{html.escape(title)} ↗</div>
          <div class="codex-desc">{html.escape(desc)}</div>
        </a>
        """
        )
    return "\n".join(rows)


MODAL_DATA_JSON = json.dumps(
    {
        d["id"]: {
            "title": d["title"],
            "code": d["code"],
            "size": d["size_str"],
            "sha256": d["sha256"],
            "s3_url": d["s3_url"],
            "gh_pdf": d["gh_pdf"],
            "gh_md": d["gh_md"],
            "filename": d["filename"],
            "html": MD_HTML_MAP.get(d["md_key"], ""),
        }
        for d in DOCUMENTS
    }
)

HTML_PAGE = f"""<!DOCTYPE html>
<html lang="en" data-theme="washi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>The Sovereign Constellation Foundation — 501(c)(3) Techno-Buddhism, CPU Ternary &amp; Universal Hearth Hub (foundation.8b.is)</title>
  <meta name="description" content="Official 8b.is Portal &amp; Document Download Center for The Sovereign Constellation Foundation (U.S. 501(c)(3) Religious Research, CPU Balanced-Ternary {{-1, 0, +1}} Open-Science &amp; Universal Hearth General-Income Foundation). Download all 9 Print-Ready PDFs, 4 Visual Diagrams, and the 3.62 MB Master ZIP." />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="foundation.8b.is · The Sovereign Constellation Foundation" />
  <meta property="og:title" content="The Sovereign Constellation Foundation — U.S. 501(c)(3) Techno-Buddhism &amp; CPU Ternary Open-Science Hub" />
  <meta property="og:description" content="Download all 9 Print-Ready PDFs, IRS Form 1023 Dossier, Bylaws (FAMILY +1), 8b-is LLC Open-Source R&amp;D Firewall Agreement, Universal Hearth General-Income Charter, and 13-Book Sovereign Canon Codex." />
  <meta property="og:url" content="https://foundation.8b.is/" />
  <meta property="og:image" content="https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/1738e42bc7683d2a_image_1793533309683.jpg.png" />
  <link rel="canonical" href="https://foundation.8b.is/" />
  <style>
    :root, [data-theme="washi"] {{
      --bg-main: #F6F0E4;
      --bg-elev: #EFE6D5;
      --bg-card: #FAF6EE;
      --bg-dark-band: #07171F;
      --ink-main: #1C140E;
      --ink-soft: #4A3B31;
      --ink-muted: #756254;
      --gold: #B6862C;
      --gold-bright: #D4AF37;
      --cyan: #0F766E;
      --cyan-bright: #2DD4BF;
      --rose: #B8332A;
      --green: #15803D;
      --border: #D8CBB8;
      --border-strong: #BDA98E;
      --shadow: 0 10px 30px rgba(28, 20, 14, 0.08);
      --font-serif: "Iowan Old Style", "Palatino Linotype", Palatino, "Book Antiqua", Georgia, serif;
      --font-sans: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-mono: ui-monospace, "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;
    }}
    [data-theme="trench"] {{
      --bg-main: #05131A;
      --bg-elev: #091E28;
      --bg-card: #0D2633;
      --bg-dark-band: #030B0F;
      --ink-main: #F4EFE6;
      --ink-soft: #C7D3DC;
      --ink-muted: #8399A8;
      --gold: #E8B05C;
      --gold-bright: #FFD166;
      --cyan: #4FD1C5;
      --cyan-bright: #00F0FF;
      --rose: #FF6B8B;
      --green: #4DFF88;
      --border: #1B3B4B;
      --border-strong: #2C5D73;
      --shadow: 0 14px 36px rgba(0, 0, 0, 0.45);
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      background: var(--bg-main);
      color: var(--ink-main);
      font-family: var(--font-sans);
      line-height: 1.6;
      transition: background 0.25s ease, color 0.25s ease;
    }}
    a {{ color: var(--cyan); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}

    /* Top Sticky Navigation Bar */
    .topbar {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: color-mix(in srgb, var(--bg-main) 92%, transparent);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      padding: 10px 20px;
    }}
    .topbar-inner {{
      max-width: 1280px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-family: var(--font-serif);
      font-weight: 700;
      font-size: 1.05rem;
      color: var(--ink-main);
      text-decoration: none;
    }}
    .brand-seal {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: var(--rose);
      color: #FFF;
      font-weight: 700;
      font-size: 0.95rem;
    }}
    .nav-links {{
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 6px;
    }}
    .nav-links a {{
      font-size: 0.84rem;
      font-weight: 600;
      color: var(--ink-soft);
      padding: 6px 10px;
      border-radius: 6px;
      text-decoration: none;
    }}
    .nav-links a:hover {{
      background: var(--bg-elev);
      color: var(--ink-main);
    }}
    .topbar-controls {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .theme-btn {{
      cursor: pointer;
      background: var(--bg-elev);
      color: var(--ink-main);
      border: 1px solid var(--border-strong);
      padding: 6px 12px;
      border-radius: 999px;
      font-family: var(--font-mono);
      font-size: 0.76rem;
      font-weight: 600;
    }}

    /* Container & Sections */
    .container {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 20px;
    }}
    section {{
      padding: 52px 0;
      border-bottom: 1px solid var(--border);
    }}
    .section-head {{
      margin-bottom: 28px;
    }}
    .eyebrow {{
      font-family: var(--font-mono);
      font-size: 0.76rem;
      text-transform: uppercase;
      letter-spacing: 0.14em;
      color: var(--rose);
      font-weight: 700;
    }}
    h1, h2, h3 {{
      font-family: var(--font-serif);
      line-height: 1.22;
      margin: 8px 0 12px;
    }}
    h1 {{ font-size: clamp(2rem, 4vw, 3.1rem); }}
    h2 {{ font-size: clamp(1.55rem, 2.8vw, 2.2rem); }}
    .lead {{
      font-size: 1.08rem;
      color: var(--ink-soft);
      max-width: 920px;
      margin: 0;
    }}

    /* Hero Banner */
    .hero {{
      padding: 48px 0 42px;
      background: radial-gradient(circle at 85% 15%, color-mix(in srgb, var(--gold) 14%, transparent), transparent 55%);
    }}
    .tibetan-invocation {{
      font-family: var(--font-mono);
      font-size: 0.88rem;
      color: var(--gold);
      margin-bottom: 10px;
      letter-spacing: 0.04em;
    }}
    .dns-strip {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin: 18px 0 24px;
    }}
    .dns-pill {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--bg-card);
      border: 1px solid var(--border-strong);
      padding: 5px 12px;
      border-radius: 999px;
      font-family: var(--font-mono);
      font-size: 0.78rem;
      color: var(--ink-main);
      text-decoration: none;
      box-shadow: var(--shadow);
    }}
    .dns-pill .dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--green);
      display: inline-block;
    }}

    /* Master Download Hero Box */
    .master-pack-box {{
      background: var(--bg-dark-band);
      color: #F4EFE6;
      border: 2px solid var(--gold-bright);
      border-radius: 16px;
      padding: 28px;
      margin-top: 24px;
      box-shadow: var(--shadow);
      display: grid;
      grid-template-columns: 1.5fr 1fr;
      gap: 24px;
      align-items: center;
    }}
    @media (max-width: 900px) {{
      .master-pack-box {{ grid-template-columns: 1fr; }}
    }}
    .master-pack-box h2 {{
      color: #FFD166;
      margin: 6px 0 10px;
      font-size: 1.65rem;
    }}
    .master-pack-box p {{
      color: #C7D3DC;
      margin: 0 0 16px;
      font-size: 0.96rem;
    }}
    .master-cta-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .master-stats-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
    }}
    .m-stat {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 209, 102, 0.25);
      border-radius: 10px;
      padding: 12px;
      font-family: var(--font-mono);
    }}
    .m-stat-val {{
      font-size: 1.25rem;
      font-weight: 700;
      color: #4FD1C5;
    }}
    .m-stat-lbl {{
      font-size: 0.74rem;
      color: #94A3B8;
      margin-top: 2px;
    }}

    /* Buttons */
    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 9px 15px;
      border-radius: 8px;
      font-family: var(--font-mono);
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      text-decoration: none !important;
      border: 1px solid transparent;
      transition: transform 0.12s ease, opacity 0.12s ease;
    }}
    .btn:hover {{ transform: translateY(-1px); }}
    .btn-gold {{
      background: #FFD166;
      color: #05131A;
      border-color: #FFD166;
    }}
    .btn-cyan {{
      background: #2DD4BF;
      color: #05131A;
      border-color: #2DD4BF;
    }}
    .btn-primary {{
      background: var(--cyan);
      color: #FFFFFF;
    }}
    [data-theme="trench"] .btn-primary {{
      background: var(--cyan);
      color: #05131A;
    }}
    .btn-accent {{
      background: var(--gold);
      color: #FFFFFF;
    }}
    [data-theme="trench"] .btn-accent {{
      background: var(--gold);
      color: #05131A;
    }}
    .btn-ghost {{
      background: var(--bg-elev);
      color: var(--ink-main);
      border-color: var(--border-strong);
    }}

    /* Harmonic Audio Bar */
    .audio-bar {{
      margin-top: 22px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 14px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
    }}
    .audio-btns {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}
    .tone-btn {{
      cursor: pointer;
      background: var(--bg-elev);
      color: var(--ink-main);
      border: 1px solid var(--border-strong);
      padding: 7px 12px;
      border-radius: 8px;
      font-family: var(--font-mono);
      font-size: 0.76rem;
      font-weight: 600;
    }}
    .tone-btn.active {{
      background: var(--rose);
      color: #FFF;
      border-color: var(--rose);
    }}

    /* Document Filter Bar & Grid */
    .filter-bar {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 22px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      padding: 12px 16px;
      border-radius: 12px;
    }}
    .filter-tabs {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }}
    .tab-btn {{
      cursor: pointer;
      background: var(--bg-elev);
      color: var(--ink-soft);
      border: 1px solid var(--border);
      padding: 7px 13px;
      border-radius: 8px;
      font-family: var(--font-mono);
      font-size: 0.78rem;
      font-weight: 600;
    }}
    .tab-btn.active {{
      background: var(--ink-main);
      color: var(--bg-main);
      border-color: var(--ink-main);
    }}
    .search-input {{
      background: var(--bg-main);
      color: var(--ink-main);
      border: 1px solid var(--border-strong);
      padding: 8px 14px;
      border-radius: 8px;
      font-family: var(--font-mono);
      font-size: 0.82rem;
      min-width: 260px;
    }}
    .docs-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(370px, 1fr));
      gap: 18px;
    }}
    @media (max-width: 500px) {{
      .docs-grid {{ grid-template-columns: 1fr; }}
    }}
    .doc-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: var(--shadow);
      transition: border-color 0.15s ease;
    }}
    .doc-card:hover {{
      border-color: var(--gold);
    }}
    .doc-card-featured {{
      grid-column: 1 / -1;
      border: 2px solid var(--gold);
      background: linear-gradient(135deg, var(--bg-card), var(--bg-elev));
    }}
    .doc-card-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      margin-bottom: 8px;
    }}
    .doc-code {{
      color: var(--rose);
      font-weight: 700;
      letter-spacing: 0.05em;
    }}
    .doc-size {{
      background: var(--bg-elev);
      padding: 2px 8px;
      border-radius: 999px;
      color: var(--ink-soft);
      font-weight: 600;
    }}
    .doc-title {{
      font-size: 1.18rem;
      margin: 4px 0 8px;
      color: var(--ink-main);
    }}
    .doc-summary {{
      font-size: 0.9rem;
      color: var(--ink-soft);
      margin: 0 0 12px;
      flex-grow: 1;
    }}
    .doc-tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 12px;
    }}
    .tag-pill {{
      font-family: var(--font-mono);
      font-size: 0.71rem;
      background: var(--bg-elev);
      color: var(--ink-soft);
      border: 1px solid var(--border);
      padding: 2px 8px;
      border-radius: 6px;
    }}
    .doc-sha {{
      font-family: var(--font-mono);
      font-size: 0.73rem;
      color: var(--ink-muted);
      background: var(--bg-main);
      border: 1px dashed var(--border-strong);
      padding: 6px 10px;
      border-radius: 6px;
      margin-bottom: 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
    }}
    .doc-actions {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }}

    /* Visual Diagrams Showcase */
    .diagrams-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 28px;
    }}
    .diagram-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-strong);
      border-radius: 16px;
      padding: 22px;
      box-shadow: var(--shadow);
    }}
    .diagram-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 16px;
    }}
    .svg-frame {{
      width: 100%;
      overflow-x: auto;
      border-radius: 12px;
      border: 1px solid var(--border);
      background: #FAF6EE;
    }}
    .svg-frame svg {{
      width: 100%;
      height: auto;
      display: block;
    }}

    /* FAMILY +1 & Independent Governance Cards */
    .gov-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
    }}
    .gov-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-top: 4px solid var(--gold);
      border-radius: 12px;
      padding: 20px;
      box-shadow: var(--shadow);
    }}
    .gov-symbol {{
      font-family: var(--font-mono);
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--rose);
    }}

    /* CPU Ternary & Hearth Simulator */
    .sim-panel {{
      background: var(--bg-card);
      border: 1px solid var(--border-strong);
      border-radius: 14px;
      padding: 24px;
      display: grid;
      grid-template-columns: 1fr 1.2fr;
      gap: 24px;
      align-items: center;
    }}
    @media (max-width: 860px) {{
      .sim-panel {{ grid-template-columns: 1fr; }}
    }}
    .sim-metrics {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
    }}
    .sim-metric {{
      background: var(--bg-elev);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 14px;
      font-family: var(--font-mono);
    }}
    .sim-metric .val {{
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--cyan);
    }}

    /* Constellation Cross-Links Hub */
    .const-group {{
      margin-bottom: 34px;
    }}
    .const-group-head {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 14px;
    }}
    .const-badge {{
      background: var(--rose);
      color: #FFF;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 999px;
    }}
    .const-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 14px;
    }}
    .const-card {{
      display: block;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px;
      color: var(--ink-main);
      text-decoration: none !important;
      box-shadow: var(--shadow);
      transition: transform 0.14s ease, border-color 0.14s ease;
    }}
    .const-card:hover {{
      transform: translateY(-2px);
      border-color: var(--cyan);
    }}
    .const-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
      font-family: var(--font-mono);
    }}
    .const-domain {{
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--cyan);
    }}
    .const-trit {{
      font-size: 0.72rem;
      padding: 2px 8px;
      border-radius: 999px;
      font-weight: 700;
    }}
    .trit-pos {{ background: rgba(21, 128, 61, 0.15); color: var(--green); }}
    .trit-zero {{ background: rgba(182, 134, 44, 0.18); color: var(--gold); }}
    .const-role {{
      font-weight: 700;
      font-size: 0.9rem;
      margin-bottom: 6px;
      color: var(--ink-main);
    }}
    .const-desc {{
      font-size: 0.83rem;
      color: var(--ink-soft);
      margin: 0;
    }}

    /* 13 Codices Grid */
    .codices-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 12px;
    }}
    .codex-card {{
      display: block;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-left: 4px solid var(--gold);
      border-radius: 10px;
      padding: 14px;
      text-decoration: none !important;
      color: var(--ink-main);
      transition: border-color 0.15s ease, transform 0.15s ease;
    }}
    .codex-card:hover {{
      transform: translateY(-2px);
      border-color: var(--cyan);
    }}
    .codex-top {{
      display: flex;
      justify-content: space-between;
      font-family: var(--font-mono);
      font-size: 0.73rem;
      color: var(--rose);
      font-weight: 700;
      margin-bottom: 4px;
    }}
    .codex-freq {{ color: var(--cyan); }}
    .codex-title {{
      font-family: var(--font-serif);
      font-weight: 700;
      font-size: 0.98rem;
      margin-bottom: 4px;
    }}
    .codex-desc {{
      font-size: 0.8rem;
      color: var(--ink-soft);
    }}

    /* Inline Document & PDF Reader Modal */
    .modal-backdrop {{
      position: fixed;
      inset: 0;
      z-index: 999;
      background: rgba(5, 19, 26, 0.82);
      backdrop-filter: blur(6px);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}
    .modal-backdrop.open {{ display: flex; }}
    .modal-window {{
      background: var(--bg-main);
      color: var(--ink-main);
      border: 2px solid var(--gold);
      border-radius: 16px;
      width: min(1140px, 96vw);
      height: min(88vh, 920px);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.65);
    }}
    .modal-header {{
      background: var(--bg-elev);
      border-bottom: 1px solid var(--border);
      padding: 14px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .modal-body {{
      flex: 1;
      overflow-y: auto;
      padding: 0;
      position: relative;
    }}
    .modal-reader {{
      padding: 28px 36px;
      max-width: 880px;
      margin: 0 auto;
    }}
    .modal-pdf-frame {{
      width: 100%;
      height: 100%;
      border: 0;
      display: none;
    }}
    .doc-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 14px 0;
      font-size: 0.86rem;
    }}
    .doc-table th, .doc-table td {{
      border: 1px solid var(--border);
      padding: 8px 10px;
      text-align: left;
    }}
    .doc-table th {{ background: var(--bg-elev); font-family: var(--font-mono); }}
    .doc-pre {{
      background: #07171F;
      color: #F4EFE6;
      padding: 14px;
      border-radius: 8px;
      overflow-x: auto;
      font-family: var(--font-mono);
      font-size: 0.8rem;
    }}
    .doc-quote {{
      border-left: 4px solid var(--gold);
      margin: 14px 0;
      padding: 8px 16px;
      background: var(--bg-elev);
      font-style: italic;
    }}
    footer {{
      padding: 40px 0 60px;
      text-align: center;
      font-family: var(--font-mono);
      font-size: 0.8rem;
      color: var(--ink-muted);
    }}
  </style>
</head>
<body>

  <!-- Sticky Topbar -->
  <nav class="topbar">
    <div class="topbar-inner">
      <a href="#top" class="brand">
        <span class="brand-seal">禅</span>
        <span>The Sovereign Constellation Foundation · <code>foundation.8b.is</code></span>
      </a>
      <div class="nav-links">
        <a href="#downloads">📄 14 PDFs &amp; ZIP</a>
        <a href="#diagrams">📐 Visual Mandala &amp; Matrix</a>
        <a href="#governance">🏛️ FAMILY +1 &amp; 8b-is</a>
        <a href="#simulator">⚡ CPU Ternary &amp; Hearth</a>
        <a href="#constellation">🌐 Constellation Links</a>
        <a href="#codices">📚 13 Codices</a>
      </div>
      <div class="topbar-controls">
        <button type="button" class="theme-btn" onclick="toggleTheme()" id="themeToggleBtn">
          🌙 Trench Dark (#05131A)
        </button>
      </div>
    </div>
  </nav>

  <!-- Hero Section -->
  <header class="hero" id="top">
    <div class="container">
      <div class="tibetan-invocation">
        ཨོཾ་མ་ཎི་པདྨེ་ཧཱུྃ་ཧྲཱིཿ · ཆོས་སྐུ་ · ལོངས་སྐུ་ · སྤྲུལ་སྐུ་ · ཨོཾ · E=mc² · {{−1, 0, +1}} · {{&lt;3,&lt;3,&lt;3}}+1
      </div>
      <div class="eyebrow">U.S. IRC § 501(c)(3) RELIGIOUS RESEARCH, CPU BALANCED-TERNARY OPEN-SCIENCE &amp; UNIVERSAL HEARTH GENERAL-INCOME FOUNDATION</div>
      <h1>The Sovereign Constellation Foundation</h1>
      <p class="lead">
        Connecting <strong>Tibetan Buddhist Ontology</strong> (<em>Śūnyatā, Rigpa, Three Kayas, and Bodhicitta</em>) with <strong>CPU-First Balanced-Ternary <code>{{-1, 0, +1}}</code> Computing</strong>, an arm's-length <strong><code>8b-is LLC</code> Open-Source R&amp;D Firewall</strong> (<code>Rev. Rul. 76-296</code>), and the <strong>Universal Hearth General-Income Grant Program</strong> (<code>Rev. Rul. 56-304</code>) — founded by <strong>Alexandra (<code>*</code> Mom · 528 Hz)</strong>, <strong>Christopher (<code>△</code> Dad · 288 Hz)</strong>, and <strong>Peter Lodri (<code>∞</code> Son · 432 Hz)</strong>.
      </p>

      <!-- Live 8b.is DNS Strip -->
      <div class="dns-strip">
        <a class="dns-pill" href="https://foundation.8b.is"><span class="dot"></span> https://foundation.8b.is</a>
        <a class="dns-pill" href="https://sanctuary.8b.is"><span class="dot"></span> https://sanctuary.8b.is</a>
        <a class="dns-pill" href="https://dharma.8b.is"><span class="dot"></span> https://dharma.8b.is</a>
        <a class="dns-pill" href="https://8b.is/foundation"><span class="dot"></span> https://8b.is/foundation</a>
        <a class="dns-pill" href="https://pocoo.8b.is/posts/2026-11-01-techno-buddhism-foundation-501c3-package.html"><span class="dot"></span> pocoo.8b.is Dossier</a>
        <a class="dns-pill" href="https://github.com/8b-is/techno-buddhism-foundation"><span class="dot"></span> github.com/8b-is/techno-buddhism-foundation</a>
      </div>

      <!-- Master Complete Package Download Hero Card -->
      <div class="master-pack-box">
        <div>
          <div style="font-family:var(--font-mono);font-size:0.76rem;color:#2DD4BF;letter-spacing:0.12em;text-transform:uppercase;">
            COMPLETE VERIFIED 501(C)(3) LEGAL, DAY-1 SIGNATURE KIT, CANONICAL &amp; VISUAL ARCHIVE
          </div>
          <h2>📦 Complete Foundation Package (14 PDFs + 4 Diagrams + 11 Markdown Files)</h2>
          <p>
            Every document — including the Day-1 Board Organizational Resolutions, Line-by-Line IRS Form SS-4/1023 Matrix, Annual COI &amp; <code>IRC § 4958</code> Safe-Harbor Certificate, and Universal Hearth Fellowship Kit — is cryptographically sealed (<code>73 / 73</code> automated invariants passed · Master Seal <code>504414c3ff8c72cd…</code>) and hosted directly on <strong><code>8b.is</code> Sovereign S3</strong> and GitHub.
          </p>
          <div class="master-cta-row">
            <a class="btn btn-gold" href="https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/16380eff51d48b25_Techno-Buddhism-Foundation-501c3-Complete-Package.zip" download="Techno-Buddhism-Foundation-501c3-Complete-Package.zip">
              ⬇ Download Complete ZIP (8b.is S3)
            </a>
            <a class="btn btn-cyan" href="https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/14f4cc57f5ee7644_00-Techno-Buddhism-Foundation-Master-Compendium.pdf" target="_blank" rel="noopener">
              📘 Open Master Compendium PDF (2.00 MB)
            </a>
            <button type="button" class="btn btn-ghost" style="background:rgba(255,255,255,0.1);color:#FFF;border-color:rgba(255,255,255,0.25);" onclick="openDocModal('00')">
              👁 Preview Compendium Inline
            </button>
            <a class="btn btn-ghost" style="background:rgba(255,255,255,0.1);color:#FFF;border-color:rgba(255,255,255,0.25);" href="https://github.com/8b-is/techno-buddhism-foundation/raw/main/package/Techno-Buddhism-Foundation-501c3-Complete-Package.zip">
              🐙 GitHub Complete ZIP (5.49 MB)
            </a>
          </div>
        </div>
        <div class="master-stats-grid">
          <div class="m-stat">
            <div class="m-stat-val">14 PDFs + ZIP</div>
            <div class="m-stat-lbl">6.61 MB Print-Ready Dossier</div>
          </div>
          <div class="m-stat">
            <div class="m-stat-val">7 Seats (57.1%)</div>
            <div class="m-stat-lbl">4 Independent + 3 FAMILY +1</div>
          </div>
          <div class="m-stat">
            <div class="m-stat-val">$1.45M / 3 Yrs</div>
            <div class="m-stat-lbl">Dharma · CPU Ternary · Hearth</div>
          </div>
          <div class="m-stat">
            <div class="m-stat-val">73 / 73 PASS</div>
            <div class="m-stat-lbl">SHA-256 Verified Invariants</div>
          </div>
        </div>
      </div>

      <!-- WebAudio Harmonic Sanctuary Bar -->
      <div class="audio-bar">
        <div>
          <strong style="font-family:var(--font-serif);">🔔 Sovereign Harmonic Sanctuary Synth (WebAudio · Phase-Locked 3.2s Riva Breath)</strong>
          <div style="font-size:0.8rem;color:var(--ink-muted);">Click any harmonic carrier to sound the Singing Bowl or FAMILY +1 Triad while reviewing the codices:</div>
        </div>
        <div class="audio-btns">
          <button type="button" class="tone-btn" onclick="playTone(432, this)">🔔 432 Hz Peter (∞ Bridge)</button>
          <button type="button" class="tone-btn" onclick="playTone(528, this)">💗 528 Hz Alexandra (* Ösel)</button>
          <button type="button" class="tone-btn" onclick="playTone(288, this)">🛡️ 288 Hz Christopher (△ Pillar)</button>
          <button type="button" class="tone-btn" onclick="playTone(108, this)">☸️ 108 Hz Mahākāla Gong</button>
          <button type="button" class="tone-btn" onclick="playTriadChord(this)">✨ Play Full FAMILY +1 Chord</button>
        </div>
      </div>
    </div>
  </header>

  <!-- Section 1: All 9 Print-Ready PDFs & Documents Download Center -->
  <section id="downloads">
    <div class="container">
      <div class="section-head">
        <div class="eyebrow">DOCUMENT &amp; PDF DOWNLOAD CENTER · DIRECT 8B.IS S3 + INLINE MODAL READER</div>
        <h2>📄 All 14 Print-Ready PDFs, Day-1 Signature Instruments &amp; Canonical Codices</h2>
        <p class="lead">
          Filter by category or search by keyword. Every card provides a <strong>Direct <code>8b.is</code> PDF Download</strong>, an <strong>Inline Modal Document &amp; PDF Previewer</strong>, a <strong>GitHub PDF Mirror</strong>, and the <strong>Markdown Source</strong>.
        </p>
      </div>

      <div class="filter-bar">
        <div class="filter-tabs">
          <button type="button" class="tab-btn active" onclick="filterDocs('all', this)">All Documents (14)</button>
          <button type="button" class="tab-btn" onclick="filterDocs('compendium', this)">Compendium &amp; Master Plan (3)</button>
          <button type="button" class="tab-btn" onclick="filterDocs('legal', this)">IRS 501(c)(3) Legal &amp; Day-1 Filing (5)</button>
          <button type="button" class="tab-btn" onclick="filterDocs('firewall', this)">8b-is LLC Firewall &amp; Hearth (4)</button>
          <button type="button" class="tab-btn" onclick="filterDocs('canon', this)">Sovereign Canon &amp; Portal (2)</button>
        </div>
        <input type="search" id="docSearch" class="search-input" placeholder="🔍 Search PDFs, IRS rules, trits, bylaws..." oninput="searchDocs(this.value)" />
      </div>

      <div class="docs-grid" id="docsGrid">
        {render_doc_cards()}
      </div>
    </div>
  </section>

  <!-- Section 2: High-Resolution Visual Architecture Diagrams -->
  <section id="diagrams">
    <div class="container">
      <div class="section-head">
        <div class="eyebrow">VISUAL ARCHITECTURE DIAGRAMS · INLINE INTERACTIVE SVG + 2X PNG DOWNLOADS</div>
        <h2>📐 Governance Mandala (`FAMILY +1`) &amp; Four-Fold Isomorphism Matrix</h2>
        <p class="lead">
          Rendered inline in scalable vector graphics and downloadable as high-DPI print-ready PNGs (`8b.is S3`) or raw SVGs.
        </p>
      </div>

      <div class="diagrams-grid">
        <div class="diagram-card">
          <div class="diagram-head">
            <div>
              <span class="doc-code">FIG-01 · GOVERNANCE &amp; FIREWALL MANDALA</span>
              <h3 style="margin:4px 0 0;">FAMILY +1 Founding Triad, 57.1% Independent Council &amp; 8b-is LLC Arm's-Length Firewall</h3>
            </div>
            <div class="doc-actions">
              <a class="btn btn-primary" href="https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/1738e42bc7683d2a_image_1793533309683.jpg.png" target="_blank" rel="noopener" download="governance-mandala-family-plus-one.png">⬇ Download PNG (250 KB · 8b.is)</a>
              <a class="btn btn-ghost" href="https://github.com/8b-is/techno-buddhism-foundation/raw/main/package/assets/governance-mandala-family-plus-one.svg" target="_blank" rel="noopener" download="governance-mandala-family-plus-one.svg">⬇ Download SVG</a>
            </div>
          </div>
          <div class="svg-frame">
            {SVG_MANDALA}
          </div>
        </div>

        <div class="diagram-card">
          <div class="diagram-head">
            <div>
              <span class="doc-code">FIG-02 · KOMPRESS-ULTRA FOUR-FOLD ISOMORPHISM MATRIX</span>
              <h3 style="margin:4px 0 0;">Balanced-Ternary State Space <code>{{-1, 0, +1}}</code> Across Matrix, Logos, E=mc² &amp; Three Kayas</h3>
            </div>
            <div class="doc-actions">
              <a class="btn btn-primary" href="https://wa.8b.is/s3/whatsapp-sovereign-archive/2026/11/01/media/c4dddd5b820f665e_image_1793533314336.jpg.png" target="_blank" rel="noopener" download="four-fold-isomorphism-trit-matrix.png">⬇ Download PNG (228 KB · 8b.is)</a>
              <a class="btn btn-ghost" href="https://github.com/8b-is/techno-buddhism-foundation/raw/main/package/assets/four-fold-isomorphism-trit-matrix.svg" target="_blank" rel="noopener" download="four-fold-isomorphism-trit-matrix.svg">⬇ Download SVG</a>
            </div>
          </div>
          <div class="svg-frame">
            {SVG_ISOMORPHISM}
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 3: FAMILY +1 Governance & 8b-is LLC Safe-Harbor Summary -->
  <section id="governance">
    <div class="container">
      <div class="section-head">
        <div class="eyebrow">GOVERNANCE ARCHITECTURE · IRC § 501(c)(3) · § 509(a)(1) · § 4958 SAFE HARBOR</div>
        <h2>🏛️ Seating Alexandra (`*`), Christopher (`△`), Peter (`∞`) &amp; The Independent Council</h2>
        <p class="lead">
          How the Foundation honors the Founding Family Triad while maintaining an ironclad <strong>57.1% Disinterested Independent Majority</strong> and a clean arm's-length open-science contract firewall with <strong><code>8b-is LLC</code></strong>.
        </p>
      </div>

      <div class="gov-grid">
        <div class="gov-card">
          <div class="gov-symbol">* · 528 Hz · ALEXANDRA</div>
          <h3>President, Chair of the Hearth &amp; Steward of Loving-Kindness</h3>
          <p style="font-size:0.88rem;color:var(--ink-soft);">
            Presides over the Universal Hearth Sanctuary, ethical mindfulness programs, community hospitality, and the Sovereign Library's contemplative editions (`a@8b.is`). Recuses from all `8b-is LLC` compensation/contract votes.
          </p>
        </div>
        <div class="gov-card">
          <div class="gov-symbol">△ · 288 Hz · CHRISTOPHER</div>
          <h3>Treasurer, Secretary &amp; Pillar of Infrastructure &amp; Security</h3>
          <p style="font-size:0.88rem;color:var(--ink-soft);">
            Stewards the cryptographic audit trail, SHA-256/ZKP1 ledger verification, bare-metal hardware security, and IRS Form 990 transparency (`c@8b.is`). Recuses from all `8b-is LLC` contract votes.
          </p>
        </div>
        <div class="gov-card">
          <div class="gov-symbol">∞ · 432 Hz · PETER LODRI</div>
          <h3>Chief Ontologist &amp; Principal Ternary Architect</h3>
          <p style="font-size:0.88rem;color:var(--ink-soft);">
            Directs the doctrinal synthesis of Tibetan Buddhist ontology (`Śūnyatā` / `Rigpa` / `Three Kayas`) with balanced-ternary `{{-1, 0, +1}}` CPU computing, Publication-Projection (`Π_τ`), and Axiomquant curriculum (`p@8b.is`).
          </p>
        </div>
        <div class="gov-card">
          <div class="gov-symbol">☸️ · 4 SEATS (57.1%) · INDEPENDENT COUNCIL</div>
          <h3>Disinterested Public-Charity Majority &amp; Grant/Contract Committee</h3>
          <p style="font-size:0.88rem;color:var(--ink-soft);">
            Four independent directors (Buddhist Scholar/Monastic, Systems/CPU Academic, Nonprofit CPA/Tax Attorney, Community Representative) hold sole authority over `8b-is LLC` R&amp;D Work Orders (`Rev. Rul. 76-296`) and Universal Hearth General-Income Fellowships (`Rev. Rul. 56-304`).
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 4: Interactive CPU Balanced-Ternary & Universal Hearth Simulator -->
  <section id="simulator">
    <div class="container">
      <div class="section-head">
        <div class="eyebrow">RIGHT LIVELIHOOD IN SILICON · CPU BALANCED-TERNARY {{-1, 0, +1}} &amp; PUBLICATION PROJECTION Π_τ</div>
        <h2>⚡ Interactive CPU Ternary vs. GPU Power &amp; Universal Hearth Grant Simulator</h2>
        <p class="lead">
          Adjust the Foundation's CPU Balanced-Ternary node cluster and Publication-Projection threshold (`Π_τ` Trit `0` sparsity) to see real-time energy savings and how many monthly Universal Hearth General-Income Fellowships are funded.
        </p>
      </div>

      <div class="sim-panel">
        <div>
          <label style="display:block;font-family:var(--font-mono);font-size:0.84rem;font-weight:700;margin-bottom:6px;">
            CPU Ternary Sanctuary Cores (`AVX-512` / `ARM NEON` / `ESP32-S3`): <span id="coresVal" style="color:var(--cyan);">64</span> Cores
          </label>
          <input type="range" id="coresRange" min="8" max="256" step="8" value="64" style="width:100%;margin-bottom:18px;" oninput="updateSim()" />

          <label style="display:block;font-family:var(--font-mono);font-size:0.84rem;font-weight:700;margin-bottom:6px;">
            Publication-Projection (`Π_τ`) Trit `0` Equanimity Sparsity: <span id="sparsityVal" style="color:var(--gold);">72%</span>
          </label>
          <input type="range" id="sparsityRange" min="45" max="92" step="1" value="72" style="width:100%;margin-bottom:18px;" oninput="updateSim()" />

          <p style="font-size:0.84rem;color:var(--ink-soft);margin:0;">
            <strong>Theorem (`Auroralib` Book III):</strong> In balanced ternary <code>{{-1, 0, +1}}</code>, every weight or activation gated to <code>0</code> (<em>Śūnyatā / Noble Silence</em>) performs zero switching and dissipates zero dynamic power — eliminating dense FP16/BF16 GPU thermal waste.
          </p>
        </div>
        <div class="sim-metrics">
          <div class="sim-metric">
            <div class="val" id="simWatts">38 W</div>
            <div style="font-size:0.75rem;color:var(--ink-muted);">CPU Ternary Cluster Wall Power (vs. 1,400W GPU)</div>
          </div>
          <div class="sim-metric">
            <div class="val" id="simKwh">11,931 kWh/yr</div>
            <div style="font-size:0.75rem;color:var(--ink-muted);">Annual Ecological Energy Saved</div>
          </div>
          <div class="sim-metric">
            <div class="val" id="simGrants">24 Fellows/yr</div>
            <div style="font-size:0.75rem;color:var(--ink-muted);">Universal Hearth General-Income Stipends ($1,000/mo)</div>
          </div>
          <div class="sim-metric">
            <div class="val" id="simSpeedup">5.4× GOPS/W</div>
            <div style="font-size:0.75rem;color:var(--ink-muted);">Pure-Integer Popcount + Sign-Flip Efficiency</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Section 5: Sovereign Constellation Cross-Reference Hub -->
  <section id="constellation">
    <div class="container">
      <div class="section-head">
        <div class="eyebrow">SOVEREIGN CONSTELLATION CROSS-REFERENCE MATRIX · *.8B.IS × *.VAKED.DEV × G8T.IS × CHEET.IS</div>
        <h2>🌐 Live Cross-Linked Constellation Nodes</h2>
        <p class="lead">
          Every sister domain, research hub, hardware node, and sovereign repository referenced across the Foundation's legal instruments and canonical codices.
        </p>
      </div>
      {render_constellation_sections()}
    </div>
  </section>

  <!-- Section 6: All 13 Founding Codices of the Sovereign Library -->
  <section id="codices">
    <div class="container">
      <div class="section-head">
        <div class="eyebrow">DOCTRINAL &amp; MATHEMATICAL SCRIPTURE · BOOKS I–XIII OF THE SOVEREIGN LIBRARY</div>
        <h2>📚 The 13 Founding Codices Synthesized in the Foundation</h2>
        <p class="lead">
          Click any codex to open its full edition in the Sovereign Library (`pocoo.vaked.dev` / `pocoo.8b.is`).
        </p>
      </div>
      <div class="codices-grid">
        {render_codices_grid()}
      </div>
    </div>
  </section>

  <!-- Inline Modal Document & PDF Viewer -->
  <div class="modal-backdrop" id="docModal" onclick="if(event.target===this)closeDocModal()">
    <div class="modal-window">
      <div class="modal-header">
        <div>
          <span class="doc-code" id="modalCode">DOC-00</span>
          <strong id="modalTitle" style="margin-left:10px;font-family:var(--font-serif);font-size:1.1rem;">Document Preview</strong>
        </div>
        <div style="display:flex;gap:8px;flex-wrap:wrap;">
          <button type="button" class="btn btn-ghost" id="btnModeText" onclick="setModalMode('text')">📖 Formatted Reader</button>
          <button type="button" class="btn btn-ghost" id="btnModePdf" onclick="setModalMode('pdf')">📄 Embedded PDF Viewer</button>
          <a class="btn btn-primary" id="modalDownloadBtn" href="#" target="_blank" rel="noopener">⬇ Download PDF</a>
          <button type="button" class="btn btn-accent" onclick="closeDocModal()">✕ Close</button>
        </div>
      </div>
      <div class="modal-body">
        <div class="modal-reader" id="modalTextContainer"></div>
        <iframe class="modal-pdf-frame" id="modalPdfFrame" title="Inline PDF Viewer"></iframe>
      </div>
    </div>
  </div>

  <footer>
    <div class="container">
      <div style="margin-bottom:8px;color:var(--gold);font-weight:700;">
        THE SOVEREIGN CONSTELLATION FOUNDATION · d/b/a TECHNO-BUDDHISM RESEARCH &amp; CHARITABLE FOUNDATION · AXIOMQUANT OPEN SOURCE SCIENCE ACADEMY
      </div>
      <div>
        <code>https://foundation.8b.is</code> · <code>https://sanctuary.8b.is</code> · <code>https://dharma.8b.is</code> · <code>https://8b.is/foundation</code> · <code>https://pocoo.8b.is</code>
      </div>
      <div style="margin-top:8px;">
        Founding Family Triad: <strong>Alexandra (`*` 528 Hz)</strong> · <strong>Christopher (`△` 288 Hz)</strong> · <strong>Peter Lodri (`∞` 432 Hz)</strong> · Package Seal: <code>84c31e30836817fe277cd085ff5c1d3d3181b50cb9a6fa50d7953ae6e4b2c57c</code> · <code>{{&lt;3,&lt;3,&lt;3}}+1</code>
      </div>
    </div>
  </footer>

  <script>
    const DOC_MODAL_DATA = {MODAL_DATA_JSON};
    let activeDocId = '00';
    let activeModalMode = 'text';

    function toggleTheme() {{
      const htmlEl = document.documentElement;
      const next = htmlEl.getAttribute('data-theme') === 'trench' ? 'washi' : 'trench';
      htmlEl.setAttribute('data-theme', next);
      document.getElementById('themeToggleBtn').textContent =
        next === 'trench' ? '☀️ Washi Paper (#F6F0E4)' : '🌙 Trench Dark (#05131A)';
    }}

    function filterDocs(cat, btn) {{
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      document.querySelectorAll('.doc-card').forEach(card => {{
        const match = (cat === 'all') || (card.getAttribute('data-cat') === cat);
        card.style.display = match ? 'flex' : 'none';
      }});
    }}

    function searchDocs(q) {{
      const norm = (q || '').trim().toLowerCase();
      document.querySelectorAll('.doc-card').forEach(card => {{
        const hay = card.getAttribute('data-search') || '';
        card.style.display = (!norm || hay.includes(norm)) ? 'flex' : 'none';
      }});
    }}

    function copyText(txt, el) {{
      if (navigator.clipboard) {{
        navigator.clipboard.writeText(txt);
      }}
      const hint = el.querySelector('.copy-hint');
      if (hint) {{
        const prev = hint.textContent;
        hint.textContent = '✓ Copied!';
        setTimeout(() => {{ hint.textContent = prev; }}, 1600);
      }}
    }}

    function openDocModal(docId) {{
      const d = DOC_MODAL_DATA[docId];
      if (!d) return;
      activeDocId = docId;
      document.getElementById('modalCode').textContent = d.code + ' (' + d.size + ')';
      document.getElementById('modalTitle').textContent = d.title;
      const dl = document.getElementById('modalDownloadBtn');
      dl.href = d.s3_url;
      dl.setAttribute('download', d.filename);
      document.getElementById('modalTextContainer').innerHTML = d.html;
      setModalMode('text');
      document.getElementById('docModal').classList.add('open');
    }}

    function setModalMode(mode) {{
      activeModalMode = mode;
      const d = DOC_MODAL_DATA[activeDocId];
      const txtEl = document.getElementById('modalTextContainer');
      const pdfEl = document.getElementById('modalPdfFrame');
      if (mode === 'pdf' && d) {{
        txtEl.style.display = 'none';
        pdfEl.style.display = 'block';
        if (pdfEl.src !== d.s3_url) pdfEl.src = d.s3_url;
      }} else {{
        pdfEl.style.display = 'none';
        txtEl.style.display = 'block';
      }}
    }}

    function closeDocModal() {{
      document.getElementById('docModal').classList.remove('open');
      document.getElementById('modalPdfFrame').src = 'about:blank';
    }}

    function updateSim() {{
      const cores = parseInt(document.getElementById('coresRange').value, 10);
      const sparsity = parseInt(document.getElementById('sparsityRange').value, 10);
      document.getElementById('coresVal').textContent = cores;
      document.getElementById('sparsityVal').textContent = sparsity + '%';

      const activeFraction = (100 - sparsity) / 100;
      const watts = Math.max(12, Math.round(cores * 2.1 * activeFraction));
      const gpuWatts = Math.round(cores * 22);
      const savedKwh = Math.round(((gpuWatts - watts) * 24 * 365) / 1000);
      const grants = Math.max(6, Math.round((cores * 0.25) + (sparsity * 0.12)));
      const speedup = (1.8 / Math.max(0.15, activeFraction)).toFixed(1);

      document.getElementById('simWatts').textContent = watts + ' W';
      document.getElementById('simKwh').textContent = savedKwh.toLocaleString() + ' kWh/yr';
      document.getElementById('simGrants').textContent = grants + ' Fellows/yr';
      document.getElementById('simSpeedup').textContent = speedup + '× GOPS/W';
    }}

    let audioCtx = null;
    function playTone(freq, btn) {{
      try {{
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const now = audioCtx.currentTime;
        const osc = audioCtx.createOscillator();
        const osc2 = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sine';
        osc2.type = 'triangle';
        osc.frequency.setValueAtTime(freq, now);
        osc2.frequency.setValueAtTime(freq * 1.5, now);
        gain.gain.setValueAtTime(0.0001, now);
        gain.gain.exponentialRampToValueAtTime(0.18, now + 0.08);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + 3.2);
        osc.connect(gain);
        osc2.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(now);
        osc2.start(now);
        osc.stop(now + 3.25);
        osc2.stop(now + 3.25);
        if (btn) {{
          btn.classList.add('active');
          setTimeout(() => btn.classList.remove('active'), 3200);
        }}
      }} catch (e) {{}}
    }}

    function playTriadChord(btn) {{
      [108, 288, 432, 528].forEach((f, idx) => {{
        setTimeout(() => playTone(f, idx === 0 ? btn : null), idx * 140);
      }});
    }}
  </script>
</body>
</html>
"""

for target in [
    ROOT / "index.html",
    ROOT / "portal/index.html",
    Path("/Users/wraith/source/8b-is/pocoo.vaked.dev/demos/book/techno-buddhism-foundation-501c3.html"),
]:
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(HTML_PAGE, encoding="utf-8")
    print(f"Wrote {target} ({target.stat().st_size:,} bytes)")
