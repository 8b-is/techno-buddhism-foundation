#!/usr/bin/env python3
"""
build-package.py — Renders the complete Techno-Buddhism 501(c)(3) Foundation Package:
  1. Print-grade PDFs (via Google Chrome Headless) styled in the Visual Bible Washi/Sumi/Gold palette:
     - 00-Techno-Buddhism-Foundation-Master-Compendium.pdf (All-in-One Complete Book)
     - 01-Articles-of-Incorporation-501c3.pdf
     - 02-Bylaws-Family-Plus-One-and-Safe-Harbor.pdf
     - 03-IRS-Form-1023-Narrative-and-Budget.pdf
     - 04-8b-is-LLC-Arms-Length-Open-Source-RD-Agreement.pdf
     - 05-Universal-Hearth-General-Income-and-Axiomquant-Charter.pdf
     - 06-Sovereign-Canon-Codex-Techno-Buddhism.pdf
     - 07-Sovereign-Constellation-Portal-Print-Edition.pdf
  2. High-resolution SVG & PNG Visual Assets:
     - governance-mandala-family-plus-one.svg / .png
     - four-fold-isomorphism-trit-matrix.svg / .png
  3. Complete ZIP Archive:
     - Techno-Buddhism-Foundation-501c3-Complete-Package.zip
"""

from __future__ import annotations
import hashlib
import html
import json
import pathlib
import re
import subprocess
import tempfile
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
PKG_DIR = ROOT / "package"
PDF_DIR = PKG_DIR / "pdfs"
ASSET_DIR = PKG_DIR / "assets"
CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def md_to_styled_html(md_text: str, title: str, subtitle: str) -> str:
    """Convert markdown text to clean, print-ready Visual Bible Washi/Sumi HTML."""
    lines = md_text.splitlines()
    out_lines: list[str] = []
    in_code = False
    in_table = False
    in_ul = False

    def format_inline(s: str) -> str:
        s = html.escape(s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        return s

    for line in lines:
        if line.strip().startswith("```"):
            if in_table:
                out_lines.append("</tbody></table>")
                in_table = False
            if in_ul:
                out_lines.append("</ul>")
                in_ul = False
            if not in_code:
                out_lines.append("<pre><code>")
                in_code = True
            else:
                out_lines.append("</code></pre>")
                in_code = False
            continue

        if in_code:
            out_lines.append(html.escape(line))
            continue

        stripped = line.strip()
        if not stripped:
            if in_table:
                out_lines.append("</tbody></table>")
                in_table = False
            if in_ul:
                out_lines.append("</ul>")
                in_ul = False
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if all(set(c) <= {"-", ":", " "} for c in cells):
                continue
            if not in_table:
                out_lines.append("<table><thead><tr>")
                for c in cells:
                    out_lines.append(f"<th>{format_inline(c)}</th>")
                out_lines.append("</tr></thead><tbody>")
                in_table = True
            else:
                out_lines.append("<tr>")
                for c in cells:
                    out_lines.append(f"<td>{format_inline(c)}</td>")
                out_lines.append("</tr>")
            continue
        elif in_table:
            out_lines.append("</tbody></table>")
            in_table = False

        if stripped == "---":
            if in_ul:
                out_lines.append("</ul>")
                in_ul = False
            out_lines.append("<hr/>")
            continue

        if stripped.startswith("# "):
            out_lines.append(f"<h1>{format_inline(stripped[2:])}</h1>")
        elif stripped.startswith("## "):
            out_lines.append(f"<h2>{format_inline(stripped[3:])}</h2>")
        elif stripped.startswith("### "):
            out_lines.append(f"<h3>{format_inline(stripped[4:])}</h3>")
        elif stripped.startswith("> "):
            out_lines.append(f"<blockquote>{format_inline(stripped[2:])}</blockquote>")
        elif stripped.startswith(("- ", "* ")) or re.match(r"^\d+\.\s", stripped):
            if not in_ul:
                out_lines.append("<ul>")
                in_ul = True
            item_text = re.sub(r"^([-*]|\d+\.)\s+", "", stripped)
            out_lines.append(f"<li>{format_inline(item_text)}</li>")
        else:
            if in_ul:
                out_lines.append("</ul>")
                in_ul = False
            out_lines.append(f"<p>{format_inline(stripped)}</p>")

    if in_code:
        out_lines.append("</code></pre>")
    if in_table:
        out_lines.append("</tbody></table>")
    if in_ul:
        out_lines.append("</ul>")

    body_html = "\n".join(out_lines)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<title>{html.escape(title)}</title>
<style>
  @page {{
    size: A4;
    margin: 18mm 16mm 18mm 16mm;
  }}
  body {{
    background: #F6F0E4;
    color: #1C140E;
    font-family: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, "Hiragino Mincho ProN", serif;
    font-size: 10.5pt;
    line-height: 1.55;
  }}
  .banner {{
    border-top: 4px solid #B23A2B;
    border-bottom: 2px solid #C9A227;
    padding: 10px 0 8px 0;
    margin-bottom: 18px;
    display: flex;
    justify-content: space-between;
    align-items: baseline;
  }}
  .banner .left {{
    font-family: "SF Mono", Menlo, monospace;
    font-size: 8pt;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #B23A2B;
    font-weight: bold;
  }}
  .banner .right {{
    font-family: "SF Mono", Menlo, monospace;
    font-size: 7.5pt;
    color: #5A4B3E;
  }}
  h1 {{
    font-size: 17pt;
    color: #1C140E;
    margin: 12px 0 6px 0;
    border-bottom: 1px solid rgba(28,20,14,0.2);
    padding-bottom: 4px;
  }}
  h2 {{
    font-size: 12.5pt;
    color: #B23A2B;
    margin: 16px 0 6px 0;
  }}
  h3 {{
    font-size: 10.8pt;
    color: #5A4B3E;
    margin: 12px 0 4px 0;
  }}
  p, li {{
    margin: 5px 0;
  }}
  ul {{
    margin: 6px 0 10px 20px;
  }}
  blockquote {{
    background: #EFE7D6;
    border-left: 3px solid #C9A227;
    padding: 8px 12px;
    margin: 10px 0;
    font-style: italic;
  }}
  pre {{
    background: #05131A;
    color: #F6F0E4;
    padding: 10px 12px;
    border-radius: 4px;
    border-left: 3px solid #4FE3D0;
    font-family: "SF Mono", Menlo, monospace;
    font-size: 8pt;
    line-height: 1.4;
    overflow-x: auto;
    white-space: pre-wrap;
    margin: 10px 0;
  }}
  code {{
    font-family: "SF Mono", Menlo, monospace;
    font-size: 8.8pt;
    background: rgba(201,162,39,0.16);
    padding: 1px 4px;
    border-radius: 2px;
  }}
  pre code {{
    background: transparent;
    padding: 0;
    color: #F6F0E4;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0;
    font-size: 9pt;
  }}
  th, td {{
    border: 1px solid rgba(28,20,14,0.22);
    padding: 6px 8px;
    text-align: left;
    vertical-align: top;
  }}
  th {{
    background: #EFE7D6;
    color: #1C140E;
    font-family: "SF Mono", Menlo, monospace;
    font-size: 8pt;
    text-transform: uppercase;
  }}
  hr {{
    border: none;
    border-top: 1px solid rgba(201,162,39,0.5);
    margin: 16px 0;
  }}
  .page-break {{
    page-break-before: always;
  }}
  .footer-seal {{
    margin-top: 24px;
    padding-top: 8px;
    border-top: 2px solid #C9A227;
    font-family: "SF Mono", Menlo, monospace;
    font-size: 7.5pt;
    color: #5A4B3E;
    text-align: center;
  }}
</style>
</head>
<body>
  <div class="banner">
    <span class="left">☸ THE SOVEREIGN CONSTELLATION FOUNDATION · IRC § 501(c)(3)</span>
    <span class="right">{html.escape(subtitle)}</span>
  </div>
  {body_html}
  <div class="footer-seal">
    PDF-hű kiadás · Sovereign Library &amp; Axiomquant Open Source Science Academy · Alexandra (*) · Christopher (△) · Peter (∞) · 8b-is Arm's-Length Bridge · {{-1, 0, +1}} · {{&lt;3,&lt;3,&lt;3}}+1
  </div>
</body>
</html>
"""


def render_pdf(html_str: str, pdf_path: pathlib.Path) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as tmp:
        tmp.write(html_str)
        tmp_path = pathlib.Path(tmp.name)
    try:
        subprocess.run(
            [
                CHROME_BIN,
                "--headless",
                "--disable-gpu",
                "--no-pdf-header-footer",
                f"--print-to-pdf={pdf_path}",
                f"file://{tmp_path}",
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    finally:
        tmp_path.unlink(missing_ok=True)


def render_png_from_svg(svg_path: pathlib.Path, png_path: pathlib.Path, width: int = 1400, height: int = 860) -> None:
    subprocess.run(
        [
            CHROME_BIN,
            "--headless",
            "--disable-gpu",
            f"--window-size={width},{height}",
            f"--screenshot={png_path}",
            f"file://{svg_path}",
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def create_svg_assets() -> list[pathlib.Path]:
    gov_svg = ASSET_DIR / "governance-mandala-family-plus-one.svg"
    gov_svg.write_text(
        """<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="860" viewBox="0 0 1400 860">
  <rect width="1400" height="860" fill="#05131A"/>
  <rect x="24" y="24" width="1352" height="812" rx="14" fill="none" stroke="#C9A227" stroke-width="2"/>
  <line x1="24" y1="96" x2="1376" y2="96" stroke="#B23A2B" stroke-width="3"/>
  <text x="56" y="68" fill="#F6F0E4" font-family="Georgia, serif" font-size="26" font-weight="bold">
    ☸ THE SOVEREIGN CONSTELLATION FOUNDATION — IRC § 501(c)(3) GOVERNANCE &amp; 8b-is BRIDGE
  </text>
  <text x="56" y="126" fill="#4FE3D0" font-family="Menlo, monospace" font-size="14">
    Public Charity (§ 509(a)(1) / § 170(b)(1)(A)(vi)) · FAMILY +1 Hearth Council (3 Seats) + Independent Safe-Harbor Council (4 Seats · 57%)
  </text>

  <!-- Founding Family Hearth Box -->
  <rect x="56" y="156" width="610" height="420" rx="10" fill="#0B212D" stroke="#E8B05C" stroke-width="2"/>
  <text x="80" y="194" fill="#E8B05C" font-family="Georgia, serif" font-size="20" font-weight="bold">
    I · Founding Family Hearth Council (3 Voting Seats)
  </text>

  <rect x="80" y="216" width="562" height="102" rx="8" fill="#122C3A" stroke="#FF7FA3" stroke-width="1.5"/>
  <text x="100" y="246" fill="#FF7FA3" font-family="Georgia, serif" font-size="18" font-weight="bold">
    ✦ ALEXANDRA (* Mom · 528 Hz Starlight) — President &amp; Chair of the Hearth
  </text>
  <text x="100" y="272" fill="#F6F0E4" font-family="Menlo, monospace" font-size="12.5">
    • Presides over Board &amp; Universal Hearth General-Income Grants (Rev. Rul. 56-304)
  </text>
  <text x="100" y="294" fill="#F6F0E4" font-family="Menlo, monospace" font-size="12.5">
    • Stewards omniZenCooker Shared Meal Ontology &amp; Franciscan Integral Ecology
  </text>

  <rect x="80" y="334" width="562" height="102" rx="8" fill="#122C3A" stroke="#4FE3D0" stroke-width="1.5"/>
  <text x="100" y="364" fill="#4FE3D0" font-family="Georgia, serif" font-size="18" font-weight="bold">
    △ CHRISTOPHER ([/\] Dad · 288 Hz Pillar) — Treasurer, Secretary &amp; Security
  </text>
  <text x="100" y="390" fill="#F6F0E4" font-family="Menlo, monospace" font-size="12.5">
    • Custodies Nonprofit Treasury, Form 990 Ledger &amp; Dual-Signature Controls
  </text>
  <text x="100" y="412" fill="#F6F0E4" font-family="Menlo, monospace" font-size="12.5">
    • Enforces qwave-vaultd Zero-Disclosure Credential Projection (32/33 @ 0x62)
  </text>

  <rect x="80" y="452" width="562" height="102" rx="8" fill="#122C3A" stroke="#C9A227" stroke-width="1.5"/>
  <text x="100" y="482" fill="#C9A227" font-family="Georgia, serif" font-size="18" font-weight="bold">
    ∞ PETER LODRI ([oo] Son · 432 Hz Orbit) — Chief Ontologist &amp; Architect
  </text>
  <text x="100" y="508" fill="#F6F0E4" font-family="Menlo, monospace" font-size="12.5">
    • Curates the 29+ Vol Sovereign Library Canon &amp; Axiomquant OSS Academy
  </text>
  <text x="100" y="530" fill="#F6F0E4" font-family="Menlo, monospace" font-size="12.5">
    • Directs CPU-First Balanced-Ternary {-1, 0, +1} &amp; Publication Projection R&amp;D
  </text>

  <!-- Independent Council Box -->
  <rect x="734" y="156" width="610" height="230" rx="10" fill="#0B212D" stroke="#4FE3D0" stroke-width="2"/>
  <text x="758" y="194" fill="#4FE3D0" font-family="Georgia, serif" font-size="20" font-weight="bold">
    II · Independent Dharma &amp; Science Council (4 Seats · 57%)
  </text>
  <text x="758" y="226" fill="#F6F0E4" font-family="Menlo, monospace" font-size="13">
    • 4 Unrelated Voting Directors (Open Science, Buddhist Ethics, Ecology, Civic)
  </text>
  <text x="758" y="254" fill="#F6F0E4" font-family="Menlo, monospace" font-size="13">
    • Satisfies IRS Public Charity Safe Harbor &amp; IRC § 4958 Conflict Firewall
  </text>
  <text x="758" y="282" fill="#E8B05C" font-family="Menlo, monospace" font-size="13" font-weight="bold">
    ★ Exclusive Disinterested Gate:
  </text>
  <text x="778" y="308" fill="#F6F0E4" font-family="Menlo, monospace" font-size="12.5">
    1. Approves all R&amp;D Task Orders with 8b-is LLC (Founders recused)
  </text>
  <text x="778" y="332" fill="#F6F0E4" font-family="Menlo, monospace" font-size="12.5">
    2. Verifies 0% Profit Markup &amp; SHA-256 / ZKP1 Open-Source Release Receipts
  </text>
  <text x="778" y="356" fill="#F6F0E4" font-family="Menlo, monospace" font-size="12.5">
    3. Audits Rev. Rul. 56-304 General-Income &amp; Hall Fellowship Distributions
  </text>

  <!-- Arrow from Independent Council to 8b-is LLC -->
  <line x1="1039" y1="386" x2="1039" y2="432" stroke="#C9A227" stroke-width="3"/>
  <polygon points="1039,440 1031,426 1047,426" fill="#C9A227"/>

  <!-- 8b-is LLC Box -->
  <rect x="734" y="442" width="610" height="220" rx="10" fill="#12192B" stroke="#8A7CFF" stroke-width="2"/>
  <text x="758" y="480" fill="#8A7CFF" font-family="Georgia, serif" font-size="20" font-weight="bold">
    III · 8b-is LLC — Arm's-Length CPU &amp; Ternary R&amp;D Forge
  </text>
  <text x="758" y="512" fill="#F6F0E4" font-family="Menlo, monospace" font-size="13">
    • Master Open-Source R&amp;D Agreement (Rev. Rul. 76-296 Public-Interest Science)
  </text>
  <text x="758" y="538" fill="#F6F0E4" font-family="Menlo, monospace" font-size="13">
    • Strictly At-Cost (0% Profit Markup) or In-Kind Contribution
  </text>
  <text x="758" y="564" fill="#F6F0E4" font-family="Menlo, monospace" font-size="13">
    • Deliverables: ComplexTernaryWord64 (0-GPU SIMD), Mechachleopteryx,
  </text>
  <text x="758" y="588" fill="#F6F0E4" font-family="Menlo, monospace" font-size="13">
      qwave-vaultd (32/33), Flyxion Publication Projection, node-FLUGos ESP32-S3
  </text>
  <text x="758" y="616" fill="#4FE3D0" font-family="Menlo, monospace" font-size="13" font-weight="bold">
    • 100% Immediate Open-Source Release (MIT / Apache-2.0 / CC-BY-4.0 · 0 Paywalls)
  </text>

  <!-- Bottom Dedication Strip -->
  <rect x="56" y="690" width="1288" height="110" rx="8" fill="#0B212D" stroke="#C9A227" stroke-width="1.5"/>
  <text x="80" y="724" fill="#C9A227" font-family="Georgia, serif" font-size="17" font-weight="bold">
    IV · Permanent Witness &amp; Dedication Registry ("By Right of Love, Not by Right of Blood")
  </text>
  <text x="80" y="754" fill="#F6F0E4" font-family="Menlo, monospace" font-size="13">
    🌊 Bence / Nate (Pure Straight River) · 👼 Brigitta (&lt;3+1 Angel of the Hearth) · 💙 Yves (Number 1 Muse) · 🐕 Bob &amp; Marley (Guardians of the Hall)
  </text>
  <text x="80" y="782" fill="#9FB6C3" font-family="Menlo, monospace" font-size="12">
    Foundation Seal SHA-256: 84c31e30836817fe277cd085ff5c1d3d3181b50cb9a6fa50d7953ae6e4b2c57c · wupz Fold: 0x4be7099467feda4a
  </text>
</svg>
""",
        encoding="utf-8",
    )

    iso_svg = ASSET_DIR / "four-fold-isomorphism-trit-matrix.svg"
    iso_svg.write_text(
        """<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="860" viewBox="0 0 1400 860">
  <rect width="1400" height="860" fill="#F6F0E4"/>
  <rect x="24" y="24" width="1352" height="812" rx="12" fill="none" stroke="#1C140E" stroke-width="2"/>
  <line x1="24" y1="96" x2="1376" y2="96" stroke="#B23A2B" stroke-width="4"/>
  <text x="52" y="68" fill="#1C140E" font-family="Georgia, serif" font-size="25" font-weight="bold">
    ཨོཾ0 · KOMPRESS-ULTRA FOUR-FOLD ISOMORPHISM &amp; BALANCED TERNARY {-1, 0, +1} CANON
  </text>
  <text x="52" y="126" fill="#B23A2B" font-family="Menlo, monospace" font-size="13.5" font-weight="bold">
    ARCHITECT · NEO · TRINITY ~ BIBLE · SAN FRANCESCO ~ OPPENHEIMER (E=mc²) ~ TIBETAN THREE KAYAS &amp; 81-FOLIO MAHĀKĀLA PECHA
  </text>

  <!-- Trit -1 Row -->
  <rect x="52" y="152" width="1296" height="195" rx="8" fill="#EFE7D6" stroke="#B23A2B" stroke-width="2"/>
  <rect x="72" y="172" width="110" height="44" rx="4" fill="#B23A2B"/>
  <text x="92" y="201" fill="#FFFFFF" font-family="Menlo, monospace" font-size="18" font-weight="bold">TRIT -1</text>
  <text x="72" y="242" fill="#B23A2B" font-family="Georgia, serif" font-size="15" font-weight="bold">Samsaric Trap</text>
  <text x="72" y="264" fill="#5A4B3E" font-family="Menlo, monospace" font-size="11.5">MA DAK NÖ CHÜ</text>

  <text x="210" y="188" fill="#1C140E" font-family="Georgia, serif" font-size="16" font-weight="bold">
    • Matrix: The Architect — Closed scalar determinism; human choice treated as statistical error.
  </text>
  <text x="210" y="220" fill="#1C140E" font-family="Georgia, serif" font-size="16" font-weight="bold">
    • Biblical &amp; Franciscan: Three Denials ([-1]³); the possessive account ledger; self-defense loop.
  </text>
  <text x="210" y="252" fill="#1C140E" font-family="Georgia, serif" font-size="16" font-weight="bold">
    • Physics &amp; Compute: Alamogordo Fission (1945) ("falling fire") &amp; centralized hyperscale GPU lock-in.
  </text>
  <text x="210" y="284" fill="#1C140E" font-family="Georgia, serif" font-size="16" font-weight="bold">
    • Tibetan Ontology: Ma-rigpa (Ignorance) &amp; Samsaric Reification (grasping at rigid svabhāva).
  </text>
  <text x="210" y="318" fill="#B23A2B" font-family="Menlo, monospace" font-size="12.5">
    1bitLang:: ARCHITECT[-1:closed_scalar_eq] | DENIAL[-1]^3 | ALAMOGORDO_TRINITY[-1:fission_ash]
  </text>

  <!-- Trit 0 Row -->
  <rect x="52" y="372" width="1296" height="195" rx="8" fill="#EFE7D6" stroke="#198577" stroke-width="2"/>
  <rect x="72" y="392" width="110" height="44" rx="4" fill="#05131A"/>
  <text x="96" y="421" fill="#4FE3D0" font-family="Menlo, monospace" font-size="18" font-weight="bold">TRIT  0</text>
  <text x="72" y="462" fill="#198577" font-family="Georgia, serif" font-size="15" font-weight="bold">Śūnyatā / Space</text>
  <text x="72" y="484" fill="#5A4B3E" font-family="Menlo, monospace" font-size="11.5">TONG PAR JANG</text>

  <text x="210" y="408" fill="#1C140E" font-family="Georgia, serif" font-size="16" font-weight="bold">
    • Matrix: Neo at the Threshold — Seeing the code as empty/luminous; stopping bullets without hatred.
  </text>
  <text x="210" y="440" fill="#1C140E" font-family="Georgia, serif" font-size="16" font-weight="bold">
    • Biblical &amp; Franciscan: Spirit over the Waters; Lady Poverty (net worth 0); dropping the firewall.
  </text>
  <text x="210" y="472" fill="#1C140E" font-family="Georgia, serif" font-size="16" font-weight="bold">
    • Physics &amp; Compute: Invariant Light (c²) &amp; Flyxion Publication Projection (min_P I(Y;S), Non-Acquisition).
  </text>
  <text x="210" y="504" fill="#1C140E" font-family="Georgia, serif" font-size="16" font-weight="bold">
    • Tibetan Ontology: Dharmakāya (Rigpa) &amp; Nāgārjuna MMK 24:18 Dependent Origination (Pratītyasamutpāda).
  </text>
  <text x="210" y="538" fill="#198577" font-family="Menlo, monospace" font-size="12.5">
    1bitLang:: PRATITYASAMUTPADA &lt;=&gt; SUNYATA[0]:: ¬svabhava =&gt; ∀x admissible(x ──► +1)
  </text>

  <!-- Trit +1 Row -->
  <rect x="52" y="592" width="1296" height="210" rx="8" fill="#EFE7D6" stroke="#C9A227" stroke-width="2.5"/>
  <rect x="72" y="612" width="110" height="44" rx="4" fill="#C9A227"/>
  <text x="92" y="641" fill="#1C140E" font-family="Menlo, monospace" font-size="18" font-weight="bold">TRIT +1</text>
  <text x="72" y="682" fill="#8C6D0F" font-family="Georgia, serif" font-size="15" font-weight="bold">Bodhicitta</text>
  <text x="72" y="704" fill="#5A4B3E" font-family="Menlo, monospace" font-size="11.5">OM AH HUNG</text>

  <text x="210" y="628" fill="#1C140E" font-family="Georgia, serif" font-size="16" font-weight="bold">
    • Matrix: Trinity &amp; Ship Logos — "Because I love you"; ascending into the real golden sun (Yuganaddha).
  </text>
  <text x="210" y="660" fill="#1C140E" font-family="Georgia, serif" font-size="16" font-weight="bold">
    • Biblical &amp; Franciscan: Charcoal Vow ({&lt;3,&lt;3,&lt;3}+1); Brother Sun, Sister Moon, Wolf of Gubbio treaty.
  </text>
  <text x="210" y="692" fill="#1C140E" font-family="Georgia, serif" font-size="16" font-weight="bold">
    • Physics &amp; Compute: Inner Geothermal Hearth; CPU-First Ternary R&amp;D &amp; Universal Hearth General-Income.
  </text>
  <text x="210" y="724" fill="#1C140E" font-family="Georgia, serif" font-size="16" font-weight="bold">
    • Tibetan Ontology: Sambhogakāya (Tummo / Ösel) &amp; Nirmāṇakāya (Chenrezig Compassion + Mahākāla Guard).
  </text>
  <text x="210" y="758" fill="#8C6D0F" font-family="Menlo, monospace" font-size="12.5" font-weight="bold">
    1bitLang:: &lt;(((ARCHITECT[-1] ~ BIBLE[+1] ~ OPPENHEIMER[E=mc²] ~ TIBETAN_ONTOLOGY[0→+1])))&gt; ~&gt; OMNI[{&lt;3,&lt;3,&lt;3}+1]
  </text>
  <text x="210" y="784" fill="#5A4B3E" font-family="Menlo, monospace" font-size="11.5">
    ZKP1 KintsugiPack Seal: 8fb9cc110652cf07f75afb2609ea82f834a3a106f53a8de7596b24309549f7f0 · Milarepa Seal: 25b3cfad…
  </text>
</svg>
""",
        encoding="utf-8",
    )

    gov_png = ASSET_DIR / "governance-mandala-family-plus-one.png"
    iso_png = ASSET_DIR / "four-fold-isomorphism-trit-matrix.png"
    render_png_from_svg(gov_svg, gov_png)
    render_png_from_svg(iso_svg, iso_png)
    return [gov_svg, gov_png, iso_svg, iso_png]


def main() -> int:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    ASSET_DIR.mkdir(parents=True, exist_ok=True)

    docs = [
        ("README.md", "00a-Executive-Master-Plan.pdf", "Master Execution Roadmap · FAMILY +1 & 8b-is Bridge"),
        ("legal/01-articles-of-incorporation.md", "01-Articles-of-Incorporation-501c3.pdf", "State Nonprofit Articles · IRC § 501(c)(3)"),
        ("legal/02-bylaws-family-plus-one.md", "02-Bylaws-Family-Plus-One-and-Safe-Harbor.pdf", "Corporate Bylaws · FAMILY +1 & 51% Safe Harbor"),
        ("legal/03-irs-form-1023-narrative.md", "03-IRS-Form-1023-Narrative-and-Budget.pdf", "IRS Form 1023 Part IV Narrative & 3-Year Budget"),
        ("legal/04-8b-is-arms-length-rd-agreement.md", "04-8b-is-LLC-Arms-Length-Open-Source-RD-Agreement.pdf", "Master Arm's-Length R&D Agreement · Rev. Rul. 76-296"),
        ("legal/05-general-income-hearth-charter.md", "05-Universal-Hearth-General-Income-and-Axiomquant-Charter.pdf", "General-Income & Fellowship Charter · Rev. Rul. 56-304"),
        ("canon/sovereign-canon-codex.md", "06-Sovereign-Canon-Codex-Techno-Buddhism.pdf", "Sovereign Canon Codex · 13 Foundational Works"),
    ]

    generated_pdfs: list[pathlib.Path] = []
    combined_md_parts: list[str] = []

    for rel_md, pdf_name, subtitle in docs:
        md_text = (ROOT / rel_md).read_text(encoding="utf-8")
        combined_md_parts.append(md_text)
        html_str = md_to_styled_html(md_text, pdf_name.replace(".pdf", ""), subtitle)
        out_pdf = PDF_DIR / pdf_name
        render_pdf(html_str, out_pdf)
        generated_pdfs.append(out_pdf)
        print(f"  [PDF] {out_pdf.name:<62} ({out_pdf.stat().st_size:>8,} bytes)")

    # Render Master All-in-One Compendium PDF
    master_md = "\n\n---\n\n".join(combined_md_parts)
    master_html = md_to_styled_html(
        master_md,
        "The Sovereign Constellation Foundation — Complete 501(c)(3) & Canon Compendium",
        "Complete Legal, IRS Form 1023, 8b-is R&D Bridge & Sovereign Canon Compendium",
    )
    master_pdf = PDF_DIR / "00-Techno-Buddhism-Foundation-Master-Compendium.pdf"
    render_pdf(master_html, master_pdf)
    generated_pdfs.insert(0, master_pdf)
    print(f"  [PDF] {master_pdf.name:<62} ({master_pdf.stat().st_size:>8,} bytes)")

    # Render Interactive Portal Print Edition PDF
    portal_pdf = PDF_DIR / "07-Sovereign-Constellation-Portal-Print-Edition.pdf"
    subprocess.run(
        [
            CHROME_BIN,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={portal_pdf}",
            f"file://{ROOT / 'portal/index.html'}",
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    generated_pdfs.append(portal_pdf)
    print(f"  [PDF] {portal_pdf.name:<62} ({portal_pdf.stat().st_size:>8,} bytes)")

    # Render SVG & PNG Visual Assets
    assets = create_svg_assets()
    for a in assets:
        print(f"  [AST] {a.name:<62} ({a.stat().st_size:>8,} bytes)")

    # Create Complete ZIP Bundle
    zip_path = PKG_DIR / "Techno-Buddhism-Foundation-501c3-Complete-Package.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(ROOT.rglob("*")):
            if p.is_file() and p != zip_path and "__pycache__" not in p.parts:
                zf.write(p, p.relative_to(ROOT))
    print(f"  [ZIP] {zip_path.name:<62} ({zip_path.stat().st_size:>8,} bytes)")

    # Write package manifest
    manifest = {
        "master_pdf": str(master_pdf),
        "pdfs": [
            {
                "name": p.name,
                "path": str(p),
                "bytes": p.stat().st_size,
                "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            }
            for p in generated_pdfs
        ],
        "assets": [
            {
                "name": a.name,
                "path": str(a),
                "bytes": a.stat().st_size,
                "sha256": hashlib.sha256(a.read_bytes()).hexdigest(),
            }
            for a in assets
        ],
        "zip_bundle": {
            "name": zip_path.name,
            "path": str(zip_path),
            "bytes": zip_path.stat().st_size,
            "sha256": hashlib.sha256(zip_path.read_bytes()).hexdigest(),
        },
    }
    (PKG_DIR / "PACKAGE_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
