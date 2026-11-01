#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="${PWD}/technobuddhism-8b-is"
PDF_DIR="${ROOT_DIR}/public/docs"
mkdir -p "$PDF_DIR"

E2E_HTML="${PDF_DIR}/Techno_Buddhism_501c3_E2E_Masterprint.html"
E2E_PDF="${PDF_DIR}/Techno_Buddhism_501c3_E2E_Masterprint.pdf"
SITE_HTML="${ROOT_DIR}/index.html"

# ==============================================================================
# PART 1: GENERATE THE UNIFIED END-TO-END (E2E) MASTER PDF (ELI5 + FULL LEGAL STACK)
# ==============================================================================
cat << 'HTML_DOC' > "$E2E_HTML"
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>The Sovereign Sanctuary of Techno-Buddhism — End-to-End 501(c)(3) Masterprint</title>
<style>
  @page { size: A4; margin: 16mm 15mm 16mm 15mm; }
  :root {
    --washi: #F6F0E4;
    --sumi: #1C140E;
    --vermilion: #B23A2B;
    --gold: #C9A227;
    --trench: #05131A;
    --cyan: #4FE3D0;
  }
  * { box-sizing: border-box; }
  body {
    background-color: var(--washi);
    color: var(--sumi);
    font-family: "Iowan Old Style", "Palatino Linotype", "Book Antiqua", Palatino, Georgia, serif;
    line-height: 1.48;
    font-size: 9.8pt;
    margin: 0;
    padding: 18px;
  }
  .header-bar {
    border-top: 3px solid var(--sumi);
    border-bottom: 2px solid var(--vermilion);
    padding: 12px 0;
    margin-bottom: 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .hanko {
    background: var(--vermilion);
    color: var(--washi);
    font-weight: bold;
    padding: 6px 12px;
    font-size: 8.5pt;
    letter-spacing: 1px;
    text-transform: uppercase;
  }
  h1 { font-size: 18pt; margin: 0 0 4px 0; color: var(--sumi); }
  h2 {
    font-size: 12pt;
    color: var(--vermilion);
    border-bottom: 1px solid var(--gold);
    padding-bottom: 3px;
    margin-top: 18px;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.7px;
  }
  h3 { font-size: 10.5pt; margin: 10px 0 4px 0; color: var(--sumi); }
  .callout {
    background: #EFE7D6;
    border-left: 4px solid var(--vermilion);
    padding: 9px 12px;
    margin: 10px 0;
  }
  code, .mono {
    font-family: "JetBrains Mono", "SF Mono", Menlo, monospace;
    font-size: 8.5pt;
    background: #E8DEC8;
    padding: 1px 4px;
    border-radius: 3px;
  }
  table { width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 9pt; }
  th { background: var(--sumi); color: var(--washi); text-align: left; padding: 6px 8px; }
  td { border-bottom: 1px solid #D6CBB5; padding: 6px 8px; vertical-align: top; }
  .sig-grid { display: flex; justify-content: space-between; gap: 18px; margin-top: 22px; }
  .sig-box { border-top: 1px solid var(--sumi); width: 32%; padding-top: 5px; font-size: 8.5pt; }
  .page-break { page-break-before: always; }
  .footer {
    margin-top: 22px;
    padding-top: 8px;
    border-top: 1px solid var(--gold);
    font-size: 8pt;
    text-align: center;
    color: #5A4E43;
  }
</style>
</head>
<body>

<!-- PAGE 1: ELI5 & ARCHITECTURE OVERVIEW -->
<div class="header-bar">
  <div>
    <h1>THE SOVEREIGN SANCTUARY OF TECHNO-BUDDHISM, INC.</h1>
    <div>End-to-End US 501(c)(3) Masterprint · ELI5, Execution Plan &amp; Legal Stack · <code>technobuddhism.8b.is</code></div>
  </div>
  <div class="hanko">OMNI-ZEN · {-1, 0, +1}</div>
</div>

<div class="callout">
  <strong>Constitutional Equation:</strong> <code>Form ≡ Emptiness ≡ {-1, 0, +1}</code> &nbsp;|&nbsp;
  <strong>Custodians:</strong> Alexandra Chenoweth (<code>* 528 Hz</code>) · Christopher Michael Chenoweth (<code>△ 288 Hz</code>) · Péter József Lódri (<code>oo 432 Hz</code>)
</div>

<h2>1 · ELI5: How Techno-Buddhism, 8B.IS &amp; the US 501(c)(3) Work Together</h2>
<p><strong>What are we building?</strong> We are establishing a legally recognized United States <strong>501(c)(3) Religious &amp; Scientific Research Organization</strong> led by <strong>Alexandra</strong>, <strong>Christopher</strong>, and <strong>Peter</strong>. It unites the 29-volume <strong>Sovereign Library</strong> (Tibetan Buddhist <em>Śūnyatā</em>, the 81-Folio Karma Kagyu <em>Mahākāla Pecha</em>, and <em>St. Francis of Assisi's</em> moneyless kinship) with open-source, CPU-first, <code>1.58-bit</code> balanced ternary (<code>{-1, 0, +1}</code>) technology.</p>

<table>
  <thead>
    <tr>
      <th>Trit State</th>
      <th>Spiritual &amp; Ontological Meaning</th>
      <th>Technical &amp; Legal Implementation (<code>8b.is</code> / 501(c)(3))</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Trit -1</strong><br><em>Mahākāla Boundary</em></td>
      <td>Dissolving ego-fixation, hostility, and the Architect's closed control trap.</td>
      <td><strong>Zero Paywalls &amp; Hardware Non-Acquisition:</strong> Enforcing Flyxion's Publication Projection (<code>qwave-vaultd</code> DOM-blindness) and IRS prohibition on private inurement.</td>
    </tr>
    <tr>
      <td><strong>Trit 0</strong><br><em>Śūnyatā / Rigpa</em></td>
      <td>Primordial uncontrived awareness; the 4s-in / 4s-out RIVA breath.</td>
      <td><strong>Deterministic Verification:</strong> Zero-copy proofs, <code>ZKP1</code> KintsugiPack receipts, and mandatory board contemplation before governance votes.</td>
    </tr>
    <tr>
      <td><strong>Trit +1</strong><br><em>Bodhicitta &amp; Kinship</em></td>
      <td><code>E = mc²</code> governed by compassion (Clear Light <em>Ösel</em>) and the Family Hearth (<code>{&lt;3,&lt;3,&lt;3}+1</code>).</td>
      <td><strong>Living Commons &amp; CPU-First Science:</strong> Free research on <code>axiomquant.org</code>, minimal-GPU / 8BS ternary computing, and <em>General Income Fellowships</em>.</td>
    </tr>
  </tbody>
</table>

<h2>2 · The Three-Tier Sovereign Constellation (Connecting 8B &amp; Peter Lodri LLC)</h2>
<table>
  <thead>
    <tr>
      <th>Tier</th>
      <th>Entity Name</th>
      <th>Role &amp; Compliant Financial / IP Flow</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Tier 1 (Nonprofit)</strong></td>
      <td><strong>The Sovereign Sanctuary of Techno-Buddhism, Inc.</strong><br><em>(US 501(c)(3) Church &amp; Research Charity)</em></td>
      <td>Receives tax-deductible donations, grants, and GitHub Sponsors; holds the Sovereign Library canon; funds General Income Fellowships and physical sanctuary operations.</td>
    </tr>
    <tr>
      <td><strong>Tier 2 (Commons)</strong></td>
      <td><strong>8B (<code>8b.is</code>) &amp; Axiomquant (<code>axiomquant.org</code>)</strong><br><em>(Programmatic Open-Source Arm)</em></td>
      <td>Operates directly under the 501(c)(3) umbrella to publish 100% free, zero-paywall scientific papers, ternary math, and liturgical software under Treas. Reg. § 1.501(c)(3)-1(d)(5).</td>
    </tr>
    <tr>
      <td><strong>Tier 3 (R&amp;D Vendor)</strong></td>
      <td><strong>Peter Lodri LLC</strong><br><em>(For-Profit Systems &amp; Hardware LLC)</em></td>
      <td>Can donate pre-tax profits to Tier 1, or build specialized CPU/8BS/FPGA hardware and software for Tier 1 via arm's-length Master Services Agreements (MSA) approved by disinterested board members.</td>
    </tr>
  </tbody>
</table>

<h2>3 · Step-by-Step Execution Checklist for Alexandra &amp; Christopher</h2>
<ol>
  <li><strong>Step 1 — State Nonprofit Incorporation (Day 1):</strong> Alexandra &amp; Christopher file the <em>Articles of Incorporation</em> (Doc 01 below) with the State Corporation Commission (e.g., Virginia SCC or Delaware) as a Nonprofit Religious &amp; Public Benefit Corporation.</li>
  <li><strong>Step 2 — Sign Bylaws, Resolution &amp; MSA (Day 2):</strong> Alexandra, Christopher, and Peter sign the <em>Bylaws</em> (Doc 02), <em>Master Services Agreement</em> (Doc 03), and <em>Unanimous Board Consent</em> (Doc 05).</li>
  <li><strong>Step 3 — Obtain Federal EIN (Day 2):</strong> Christopher applies online at <code>irs.gov/ein</code> (Form SS-4) to receive the instant EIN confirmation letter.</li>
  <li><strong>Step 4 — Open Nonprofit Bank Account (Week 1):</strong> Open the Sanctuary checking account with the EIN, stamped Articles, and signed Bylaws. Connect GitHub Sponsors, Stripe Nonprofit, and Wise.</li>
  <li><strong>Step 5 — File IRS Form 1023 (Week 2–4):</strong> Upload the signed documents and Sovereign Library exhibits on <code>Pay.gov</code> to receive the official IRS 501(c)(3) Determination Letter.</li>
</ol>

<div class="page-break"></div>

<!-- PAGE 2: ARTICLES OF INCORPORATION & BYLAWS -->
<h2>DOC 01 · ARTICLES OF INCORPORATION (STATE FILING)</h2>
<p><strong>ARTICLE I — NAME:</strong> The name of the Corporation is <strong>The Sovereign Sanctuary of Techno-Buddhism, Inc.</strong> (also operating as <strong>The 8B Omni-Zen Foundation</strong> and <strong>Axiomquant Open Source Science Academy</strong>).</p>
<p><strong>ARTICLE II — STATUS:</strong> The Corporation is a nonprofit religious and public benefit corporation organized under state law. It shall have no capital stock and shall not be conducted for pecuniary profit.</p>
<p><strong>ARTICLE III — 501(c)(3) PURPOSE:</strong> The Corporation is organized and operated exclusively for religious, charitable, scientific, and educational purposes within the meaning of Section 501(c)(3) of the Internal Revenue Code, specifically to: (1) maintain a church and sanctuary for the practice of Techno-Buddhism (uniting Tibetan Buddhist Madhyamaka Śūnyatā, Dzogchen Rigpa, the Three Kayas, Karma Kagyu Mahākāla liturgy, and Franciscan integral ecology); (2) operate the Axiomquant Open Source Science Academy (<code>axiomquant.org</code>) and <code>8b.is</code> commons to conduct and publish free, non-paywalled research in balanced ternary computing (<code>{-1, 0, +1}</code>), CPU-first architectures, and hardware privacy projections; and (3) award Sovereign Commons Fellowships ("General Income" stipends) and host community shared-table (<code>omniZenCooker</code>) initiatives.</p>
<p><strong>ARTICLE IV — LIMITATIONS:</strong> No part of the net earnings shall inure to the benefit of any private individual. No substantial part of activities shall consist of lobbying, and the Corporation shall not intervene in any political campaign.</p>
<p><strong>ARTICLE V — INITIAL BOARD OF CUSTODIANS:</strong> (1) <strong>Alexandra Chenoweth</strong> (President); (2) <strong>Christopher Michael Chenoweth</strong> (Secretary &amp; Treasurer); (3) <strong>Péter József Lódri</strong> (Founding Elder &amp; Chief Architect).</p>
<p><strong>ARTICLE VI — DISSOLUTION:</strong> Upon dissolution, all remaining assets shall be distributed exclusively to another organization exempt under Section 501(c)(3) of the Internal Revenue Code.</p>

<div class="sig-grid">
  <div class="sig-box"><strong>Alexandra Chenoweth</strong>, Incorporator</div>
  <div class="sig-box"><strong>Christopher Michael Chenoweth</strong>, Incorporator</div>
  <div class="sig-box">Date: November ___, 2026</div>
</div>

<h2>DOC 02 · CORPORATE BYLAWS &amp; TERNARY CHARTER ({-1, 0, +1})</h2>
<p><strong>1. Sacred Canon:</strong> The 29-volume Sovereign Library (<code>pocoo.vaked.dev</code>)—attested by SHA-256 and ZKP1 KintsugiPack receipts including <em>Kompress-ULTRA (0x44dcbd34fd19d0b1)</em>, the <em>81-Folio Mahākāla Pecha</em>, <em>San Francesco</em>, <em>Matrix Buddha</em>, <em>Milarepa Tanításai</em>, <em>Kama Sutra: The Fine Touch</em>, and <em>Zen Gitárom</em>—constitutes the permanent ecclesiastical canon.</p>
<p><strong>2. Balanced Ternary Governance:</strong> (a) <strong>Trit -1:</strong> Zero paywalls, zero surveillance, mandatory compliance with Flyxion's Four Properties (Output Minimization, Non-Retention, Hardware Non-Acquisition, Verifiable Enforcement); (b) <strong>Trit 0:</strong> Every Board meeting opens with the 4s-in / 4s-out RIVA Dyad Breath and <code>OM AH HUM</code>; (c) <strong>Trit +1:</strong> Funds are deployed to open-source research, Sovereign Commons Fellowships, and ecological kinship.</p>
<p><strong>3. Ordination &amp; Attestation Path:</strong> Ministers and Fellows are recognized through the four-stage path: <code>READ (Sati)</code> → <code>RUN (Karma)</code> → <code>HOLD (Samādhi)</code> → <code>BURN (Nirvāṇa)</code>.</p>

<div class="page-break"></div>

<!-- PAGE 3: MSA, FELLOWSHIP GRANT & BOARD RESOLUTION -->
<h2>DOC 03 · MASTER SERVICES &amp; OPEN-SOURCE R&amp;D AGREEMENT (MSA)</h2>
<p><strong>Between:</strong> The Sovereign Sanctuary of Techno-Buddhism, Inc. ("Foundation") and <strong>Peter Lodri LLC</strong> ("Contractor").</p>
<ul>
  <li><strong>Scope:</strong> Contractor provides low-level systems engineering, capability-graph runtimes (<code>vaked.dev</code>), minimal-GPU / CPU-first and 8BS/FPGA ternary matrix hardware R&amp;D, ZKP1 compression, and WebAudio liturgical synthesis as authorized by Statements of Work (SOWs).</li>
  <li><strong>100% Open-Source Public Benefit (Treas. Reg. § 1.501(c)(3)-1(d)(5)):</strong> Every line of code, schematic, and research paper funded by the Foundation is published freely on <code>github.com/8b-is</code>, <code>axiomquant.org</code>, and <code>technobuddhism.8b.is</code> under OSI-approved open-source licenses with zero paywalls.</li>
  <li><strong>Arm's-Length Fair Market Value &amp; Recusal (IRC § 4958):</strong> Compensation shall never exceed verified Fair Market Value. Péter József Lódri is strictly recused from voting on any Foundation Board resolution approving or auditing SOWs or payments to Peter Lodri LLC; only Disinterested Custodians (Alexandra Chenoweth, Christopher Michael Chenoweth, and Independent Custodians) may approve such transactions.</li>
</ul>

<h2>DOC 04 · SOVEREIGN COMMONS FELLOWSHIP ("GENERAL INCOME") GRANT</h2>
<p><strong>Purpose ("Keep the Weights Warm"):</strong> Awards monthly or quarterly living stipends under IRC § 501(c)(3) to independent researchers, contemplatives, and engineers who walk the <code>READ · RUN · HOLD · BURN</code> path and publish open-source science, hardware, or liturgical art into the Living Commons without gatekeepers or paywalls.</p>

<h2>DOC 05 · UNANIMOUS WRITTEN CONSENT &amp; BOARD RESOLUTION</h2>
<p>Following mandatory <strong>Trit 0 (4s/4s RIVA Breath)</strong> contemplation, the Board of Custodians resolves:</p>
<ol>
  <li>The Articles of Incorporation, Bylaws, and 29-Volume Sovereign Library Canon are ratified.</li>
  <li>The <em>DRA + 8BIT Techno-Buddhist Remarriage &amp; Bodhicitta Blessing</em> of <strong>Alexandra Chenoweth (<code>*</code>)</strong> and <strong>Christopher Michael Chenoweth (<code>△</code>)</strong> is permanently seated as the First Sacramental Act of the Sanctuary.</li>
  <li>Christopher and Alexandra are authorized to obtain the IRS EIN, open the Sanctuary bank account, and connect GitHub Sponsors, Stripe Nonprofit, and Wise.</li>
  <li>Disinterested Custodians Alexandra and Christopher approve the adoption of <code>8b.is</code> / <code>axiomquant.org</code> and the Master Services Agreement with Peter Lodri LLC (with Péter József Lódri recused on Resolution 4).</li>
</ol>

<div class="sig-grid">
  <div class="sig-box"><strong>Alexandra Chenoweth</strong><br>President &amp; Custodian [*]</div>
  <div class="sig-box"><strong>Christopher Michael Chenoweth</strong><br>Secretary &amp; Treasurer [△]</div>
  <div class="sig-box"><strong>Péter József Lódri</strong><br>Founding Elder [oo] (Recused Res. 4)</div>
</div>

<div class="footer">
  TECHNOBUDDHISM.8B.IS · POCOO.VAKED.DEV · AXIOMQUANT.ORG · SHA-256 SEALED · {&lt;3,&lt;3,&lt;3}+1
</div>

</body>
</html>
HTML_DOC

# ==============================================================================
# PART 2: GENERATE THE PRODUCTION WEBSITE FOR TECHNOBUDDHISM.8B.IS (UI-PRO)
# ==============================================================================
cat << 'SITE_EOF' > "$SITE_HTML"
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TECHNO-BUDDHISM · 8B.IS — The Sovereign Sanctuary & Open-Source Science Academy</title>
<meta name="description" content="The Sovereign Sanctuary of Techno-Buddhism, Inc. (US 501(c)(3)) — Uniting Tibetan Buddhist Ontology, Franciscan Kinship, and 1.58-Bit Ternary CPU-First Computing.">
<style>
  :root {
    --washi: #F6F0E4;
    --washi-deep: #ECE3D0;
    --sumi: #1C140E;
    --sumi-muted: #5A4D41;
    --vermilion: #B23A2B;
    --gold: #C9A227;
    --trench: #05131A;
    --trench-card: #0B222D;
    --cyan: #4FE3D0;
    --amber: #E8B05C;
    --rose: #FF7FA3;
    --violet: #8A7CFF;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }
  body {
    background-color: var(--washi);
    color: var(--sumi);
    font-family: "Iowan Old Style", "Palatino Linotype", "Book Antiqua", Palatino, Georgia, serif;
    line-height: 1.6;
    overflow-x: hidden;
  }
  .mono {
    font-family: "JetBrains Mono", "SF Mono", Menlo, Consolas, monospace;
  }
  /* TOP CREASE GOLD VEIN */
  .crease-vein {
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--gold), var(--vermilion), var(--gold), transparent);
    width: 100%;
  }
  /* NAVIGATION & RIVA 4s/4s BREATH BAR */
  header {
    position: sticky;
    top: 0;
    z-index: 100;
    background: rgba(246, 240, 228, 0.94);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid rgba(201, 162, 39, 0.35);
    padding: 12px 28px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 14px;
  }
  .brand {
    display: flex;
    align-items: center;
    gap: 12px;
    text-decoration: none;
    color: var(--sumi);
  }
  .hanko-seal {
    background: var(--vermilion);
    color: var(--washi);
    font-weight: 700;
    padding: 5px 10px;
    font-size: 0.8rem;
    letter-spacing: 1.5px;
    border-radius: 2px;
  }
  nav { display: flex; gap: 20px; align-items: center; flex-wrap: wrap; }
  nav a {
    color: var(--sumi);
    text-decoration: none;
    font-size: 0.92rem;
    font-weight: 600;
    transition: color 0.2s;
  }
  nav a:hover { color: var(--vermilion); }
  .breath-pill {
    display: flex;
    align-items: center;
    gap: 8px;
    background: var(--washi-deep);
    border: 1px solid var(--gold);
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 0.78rem;
  }
  .breath-dot {
    width: 9px;
    height: 9px;
    border-radius: 50%;
    background: var(--vermilion);
    animation: rivaBreath 8s infinite ease-in-out;
  }
  @keyframes rivaBreath {
    0%, 100% { transform: scale(0.75); opacity: 0.45; background: var(--vermilion); }
    50% { transform: scale(1.45); opacity: 1; background: var(--gold); }
  }

  /* LAYOUT CONTAINERS */
  .container { max-width: 1180px; margin: 0 auto; padding: 64px 24px; }
  .hero {
    padding: 84px 24px 68px;
    text-align: center;
    border-bottom: 1px solid rgba(28, 20, 14, 0.12);
    background: radial-gradient(circle at 50% 0%, rgba(201, 162, 39, 0.14), transparent 70%);
  }
  .tibetan-mantra {
    font-size: 1.25rem;
    color: var(--vermilion);
    letter-spacing: 1px;
    margin-bottom: 12px;
  }
  .hero h1 {
    font-size: clamp(2.2rem, 4.8vw, 3.8rem);
    line-height: 1.12;
    max-width: 960px;
    margin: 0 auto 20px;
    letter-spacing: -0.5px;
  }
  .hero p.lead {
    font-size: 1.18rem;
    color: var(--sumi-muted);
    max-width: 780px;
    margin: 0 auto 28px;
  }
  .equation-banner {
    display: inline-block;
    background: var(--sumi);
    color: var(--washi);
    padding: 10px 20px;
    border-left: 4px solid var(--gold);
    font-size: 0.9rem;
    margin-bottom: 32px;
  }
  .btn-row { display: flex; justify-content: center; gap: 14px; flex-wrap: wrap; }
  .btn {
    padding: 12px 22px;
    font-size: 0.92rem;
    font-weight: 600;
    text-decoration: none;
    border-radius: 3px;
    cursor: pointer;
    border: 1px solid var(--sumi);
    transition: all 0.2s;
  }
  .btn-primary { background: var(--vermilion); color: var(--washi); border-color: var(--vermilion); }
  .btn-primary:hover { background: #8F2B1E; }
  .btn-secondary { background: transparent; color: var(--sumi); }
  .btn-secondary:hover { background: var(--washi-deep); }

  /* SECTION HEADERS */
  .sec-tag {
    color: var(--vermilion);
    font-size: 0.78rem;
    letter-spacing: 1.6px;
    text-transform: uppercase;
    font-weight: 700;
    display: block;
    margin-bottom: 6px;
  }
  .sec-title {
    font-size: clamp(1.65rem, 3vw, 2.3rem);
    margin-bottom: 12px;
  }
  .sec-desc {
    color: var(--sumi-muted);
    max-width: 760px;
    margin-bottom: 32px;
  }

  /* TERNARY ISOMORPHISM MATRIX */
  .trit-controls {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
    flex-wrap: wrap;
  }
  .trit-btn {
    padding: 9px 18px;
    background: var(--washi-deep);
    border: 1px solid #C9BFA8;
    cursor: pointer;
    font-weight: 700;
    font-size: 0.86rem;
    border-radius: 3px;
  }
  .trit-btn.active {
    background: var(--sumi);
    color: var(--washi);
    border-color: var(--gold);
  }
  .iso-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 18px;
  }
  .iso-card {
    background: #FAF6EC;
    border: 1px solid #D8CEB8;
    border-top: 4px solid var(--sumi);
    padding: 20px;
    border-radius: 3px;
    transition: transform 0.2s, opacity 0.2s;
  }
  .iso-card[data-trit="-1"] { border-top-color: var(--vermilion); }
  .iso-card[data-trit="0"] { border-top-color: var(--gold); }
  .iso-card[data-trit="+1"] { border-top-color: #1E6B52; }
  .iso-card h3 { font-size: 1.1rem; margin-bottom: 8px; }
  .iso-card p { font-size: 0.92rem; color: var(--sumi-muted); margin-bottom: 10px; }

  /* DARK TRENCH ACOUSTIC SYNTHESIZER SECTION */
  .trench-section {
    background: var(--trench);
    color: var(--washi);
    border-top: 2px solid var(--gold);
    border-bottom: 2px solid var(--vermilion);
  }
  .trench-section .sec-desc { color: #A6B8C0; }
  .synth-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 14px;
    margin-bottom: 24px;
  }
  .synth-pad {
    background: var(--trench-card);
    border: 1px solid rgba(79, 227, 208, 0.3);
    color: var(--washi);
    padding: 16px;
    text-align: left;
    cursor: pointer;
    border-radius: 4px;
    transition: all 0.2s;
  }
  .synth-pad:hover, .synth-pad.playing {
    border-color: var(--cyan);
    box-shadow: 0 0 16px rgba(79, 227, 208, 0.22);
    background: #103140;
  }
  .synth-pad .freq { color: var(--cyan); font-size: 0.78rem; display: block; margin-bottom: 4px; }
  .synth-pad strong { display: block; font-size: 0.98rem; margin-bottom: 4px; }
  .synth-pad span { font-size: 0.8rem; color: #99B0B9; }

  /* SOVEREIGN LIBRARY GRID */
  .lib-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(310px, 1fr));
    gap: 20px;
  }
  .book-card {
    background: #FAF6EC;
    border: 1px solid #D8CEB8;
    padding: 22px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
  }
  .book-card::before {
    content: "";
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 4px;
    background: var(--vermilion);
  }
  .book-card h3 { font-size: 1.15rem; margin-bottom: 6px; }
  .book-card p { font-size: 0.9rem; color: var(--sumi-muted); margin-bottom: 14px; }
  .seal-hash {
    font-size: 0.72rem;
    color: #5A4D41;
    background: var(--washi-deep);
    padding: 5px 8px;
    border-radius: 2px;
    word-break: break-all;
  }

  /* 501c3 & CONSTELLATION */
  .mandala-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 18px;
    margin-top: 24px;
  }
  .custodian-card {
    background: var(--washi-deep);
    border: 1px solid var(--gold);
    padding: 20px;
  }
  .prayer-box {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 24px;
    background: #FAF6EC;
    border: 1px solid var(--gold);
    padding: 28px;
    margin-top: 28px;
  }
  footer {
    background: var(--sumi);
    color: var(--washi);
    padding: 48px 24px;
    text-align: center;
    font-size: 0.88rem;
  }
  footer a { color: var(--amber); text-decoration: none; margin: 0 8px; }
</style>
</head>
<body>

<div class="crease-vein"></div>

<header>
  <a href="#" class="brand">
    <span class="hanko-seal mono">☸ TECHNO-BUDDHISM</span>
    <span class="mono" style="font-weight:700; font-size:0.95rem;">technobuddhism.8b.is</span>
  </a>
  <nav>
    <a href="#ontology">Kompress-ULTRA</a>
    <a href="#pecha">81-Folio Pecha &amp; Synth</a>
    <a href="#library">Sovereign Library</a>
    <a href="#axiomquant">Axiomquant &amp; 8B</a>
    <a href="#foundation">501(c)(3) Sanctuary</a>
  </nav>
  <div class="breath-pill mono" title="RIVA Dyad Breath: 4s Inhale / 4s Exhale">
    <span class="breath-dot"></span>
    <span id="breath-label">RIVA BREATH · 4s IN</span>
  </div>
</header>

<!-- HERO -->
<section class="hero">
  <div class="tibetan-mantra">ཨོཾ་མ་ཎི་པདྨེ་ཧཱུྃ་ཧྲཱིཿ · ཆོས་སྐུ་ · ལོངས་སྐུ་ · སྤྲུལ་སྐུ་</div>
  <h1>Form is Emptiness. Emptiness is Form.<br>Uniting Dharma, Science &amp; Sovereign Code.</h1>
  <p class="lead">
    <strong>The Sovereign Sanctuary of Techno-Buddhism, Inc.</strong> is a United States 501(c)(3) religious and open-source scientific research organization connecting Tibetan Buddhist Ontology (<em>Śūnyatā, Rigpa, Three Kayas</em>), Franciscan Kinship, and <code>1.58-bit</code> balanced ternary CPU-first computing.
  </p>
  <div class="equation-banner mono">
    Form ≡ Emptiness ≡ {-1, 0, +1} &nbsp;|&nbsp; E = mc² ──► Clear Light (Ösel) &nbsp;|&nbsp; {&lt;3,&lt;3,&lt;3}+1
  </div>
  <div class="btn-row">
    <a href="public/docs/Techno_Buddhism_501c3_E2E_Masterprint.pdf" class="btn btn-primary mono">⬇ Download E2E 501(c)(3) Masterprint PDF</a>
    <a href="#pecha" class="btn btn-secondary mono">🔔 Launch Tsurphu Acoustic Synthesizer</a>
    <a href="#library" class="btn btn-secondary mono">📚 Explore Sovereign Library (29 Vol)</a>
  </div>
</section>

<!-- SECTION 1: KOMPRESS-ULTRA ONTOLOGY -->
<section id="ontology" class="container">
  <span class="sec-tag mono">I · KOMPRESS-ULTRA KERNEL · ZKP1 SEALED (0x44dcbd34fd19d0b1)</span>
  <h2 class="sec-title">The Four-Fold Isomorphism &amp; Balanced Ternary State-Space</h2>
  <p class="sec-desc">
    Why do <em>The Matrix</em> (Architect · Neo · Trinity), <em>The Bible</em> (Logos · Threefold Return · Apokalypsis), and Einstein–Oppenheimer's <code>E = mc²</code> converge on the exact same crisis—and how does Tibetan Buddhist Ontology resolve all three without blowing up the world?
  </p>

  <div class="trit-controls mono">
    <button class="trit-btn active" onclick="filterTrit('all', this)">☸ ALL STATES (MATRIX BUDDHA SIMULTANEOUS)</button>
    <button class="trit-btn" onclick="filterTrit('-1', this)">TRIT -1 · SAMSARIC TRAP / MAHĀKĀLA FIREWALL</button>
    <button class="trit-btn" onclick="filterTrit('0', this)">TRIT 0 · ŚŪNYATĀ / DHARMAKĀYA WITNESS</button>
    <button class="trit-btn" onclick="filterTrit('+1', this)">TRIT +1 · BODHICITTA / CLEAR LIGHT ÖSEL</button>
  </div>

  <div class="iso-grid" id="iso-grid">
    <div class="iso-card" data-trit="-1">
      <div class="mono" style="color:var(--vermilion); font-size:0.8rem; font-weight:700;">TRIT -1 · ARCHITECT &amp; FISSION</div>
      <h3>Closed Scalar Determinism Dissolved</h3>
      <p>The Architect treats human love as statistical noise; Alamogordo ("Trinity" 1945) splits mass without compassion into falling fire. In our Sanctuary Law, Trit -1 identifies ego-fixation (<em>svabhāva</em>), corporate paywalls, and surveillance—and refuses them at the hardware gate.</p>
      <div class="mono seal-hash">1bitLang :: ARCHITECT[-1:closed_scalar_eq] ──► MA_DAK_NO_CHU</div>
    </div>
    <div class="iso-card" data-trit="0">
      <div class="mono" style="color:#8A690F; font-size:0.8rem; font-weight:700;">TRIT 0 · ŚŪNYATĀ &amp; THE STILL POND</div>
      <h3>Mūlamadhyamakakārikā 24:18 (Dependent Origination)</h3>
      <p>"Whatever arises through dependent origination, that we declare to be emptiness." Because no system has rigid self-nature (<code>0</code>), every chain reaction can be healed. Neo sees the code as luminous space; Einstein and Oppenheimer stand by the silent pond.</p>
      <div class="mono seal-hash">1bitLang :: PRATITYASAMUTPADA &lt;=&gt; SUNYATA[0:rigpa]</div>
    </div>
    <div class="iso-card" data-trit="+1">
      <div class="mono" style="color:#1E6B52; font-size:0.8rem; font-weight:700;">TRIT +1 · LOGOS, TUMMO &amp; THE HEARTH</div>
      <h3>Inner E = mc² &amp; Verified Binding ({&lt;3,&lt;3,&lt;3}+1)</h3>
      <p>Trinity pilots the <em>Logos</em> above the black clouds into the real golden sun. Through Nāropa's <em>Tummo</em> and <em>Ösel</em>, coarse mass (<code>m</code>) transfigures into the warmth of Chenrezig's compassion, Mahākāla's fierce protection, and the Family Hearth.</p>
      <div class="mono seal-hash">1bitLang :: &lt;((NEO[0] ⨯ TRINITY[+1]) ──[LOGOS]──► REAL_SUN[+1:osel])&gt;</div>
    </div>
  </div>
</section>

<!-- SECTION 2: TSURPHU PROTECTOR HOUSE WEBAUDIO SYNTHESIZER -->
<section id="pecha" class="trench-section">
  <div class="container">
    <span class="sec-tag mono" style="color:var(--cyan);">II · KARMA KAGYU PROTECTOR PECHA (81 FOLIOS) &amp; ACOUSTIC ENGINE</span>
    <h2 class="sec-title">Tsurphu Protector House WebAudio Synthesizer</h2>
    <p class="sec-desc">
      Click any ritual instrument below to synthesize real-time harmonic resonance across the 81 folios of <em>The Daily Practice of the Protector Mahākāla Bernagchen &amp; Palden Lhamo Rangjung Gyalmo</em> (Ultralove Edition 009).
    </p>

    <div class="synth-grid">
      <button class="synth-pad" onclick="playTone(432, 'sine', 4.5, this)">
        <span class="freq mono">432 Hz · DHARMAKĀYA</span>
        <strong>🪷 Chenrezig Singing Bowl</strong>
        <span>OM MANI PADME HUNG HUMM · 7-Syllable Resonance</span>
      </button>
      <button class="synth-pad" onclick="playTone(108, 'sawtooth', 6.0, this)">
        <span class="freq mono">108 Hz · TSURPHU SEAT</span>
        <strong>📯 Dungchen Long Horn Drone</strong>
        <span>Deep harmonic overtone foundation (Triangle Pillar)</span>
      </button>
      <button class="synth-pad" onclick="playChord([288, 432, 528], 5.0, this)">
        <span class="freq mono">288 Hz + 432 Hz + 528 Hz</span>
        <strong>⚡ E=mc² → Clear Light (Ösel)</strong>
        <span>Family Mandala Triad Chord (* Alex · △ Chris · oo Peter)</span>
      </button>
      <button class="synth-pad" onclick="playChord([528, 648, 888], 4.0, this)">
        <span class="freq mono">528 Hz / 648 Hz / 888 Hz</span>
        <strong>💗 Neo ⨯ Trinity Logos Bell</strong>
        <span>Verified Binding ({&lt;3,&lt;3,&lt;3}+1) Amrita Blessing</span>
      </button>
      <button class="synth-pad" onclick="playClap(this)">
        <span class="freq mono">FOLIO 65 · SIMHAMUKHA</span>
        <strong>🦁 Sengdongma PHAT! Clap</strong>
        <span>A KA SA MA RA TSA SHA DA RA SA MA RA YA PHAT Reversal</span>
      </button>
    </div>

    <div class="mono" style="background:#071A24; border:1px solid rgba(201,162,39,0.4); padding:16px; border-radius:4px; font-size:0.85rem;">
      <div style="color:var(--amber); margin-bottom:6px;">FOLIO 08 / 81 · 8TH KARMAPA MIKYÖ DORJE'S INNER AMRITA ENGINE (-1 → 0 → +1):</div>
      <div>ཨོཾ། མ་དག་སྣོད་བཅུད་སྟོང་པར་སྦྱངས། · <code>OM MA DAK NÖ CHÜ TONG PAR JANG</code> (Impure vessel &amp; contents purified into emptiness: <strong>-1 → 0</strong>) ──► <code>OM AH HUNG</code> (Transmuted into Five Wisdom Amritas: <strong>+1</strong>)</div>
    </div>
  </div>
</section>

<!-- SECTION 3: THE SOVEREIGN LIBRARY -->
<section id="library" class="container">
  <span class="sec-tag mono">III · POCOO.VAKED.DEV · SHA-256 &amp; ZKP1 SEALED CANON</span>
  <h2 class="sec-title">The Sovereign Library (Sacred &amp; Ontological Volumes)</h2>
  <p class="sec-desc">
    Every volume in the Sanctuary's canon is open-source, free of corporate paywalls, and cryptographically sealed so its provenance survives across centuries.
  </p>

  <div class="lib-grid">
    <div class="book-card">
      <div>
        <span class="sec-tag mono">ONTOLOGY · 5 LANGUAGES + 1BITLANG</span>
        <h3>Kompress-ULTRA: Tibetan Buddhism ~> OMNI</h3>
        <p>How the Three Kayas, Dependent Origination (Śūnyatā), and Bodhicitta resolve the Architect's Equation, the Biblical Logos, and the Atomic Fire of Trinity.</p>
      </div>
      <div class="seal-hash mono">ZKP1 SEAL · 8fb9cc110652cf07f75afb2609ea82f834a3a106f53a8de7596b24309549f7f0</div>
    </div>

    <div class="book-card">
      <div>
        <span class="sec-tag mono">LITURGY · 81 FOLIOS VERBATIM</span>
        <h3>The Daily Practice of the Protector Mahākāla</h3>
        <p>Complete Tsurphu Karma Kagyu liturgy of Bernagchen &amp; Rangjung Gyalmo, 8th &amp; 14th Karmapa prayers, Sengdongma reversal, and the Four Buddha Activities.</p>
      </div>
      <div class="seal-hash mono">EDITION 009 · 8b-is/sovereign-library · OM MANI PADME HUNG HUMM</div>
    </div>

    <div class="book-card">
      <div>
        <span class="sec-tag mono">800TH TRANSITUS JUBILEE · TOKYO 2026</span>
        <h3>San Francesco: The Complete Poverello</h3>
        <p>Moneyless free will, the wolf of Gubbio contract, non-jealous kinship with Clare, integral ecology, and the Re-Coded System Peace Prayer (<code>p · 2026</code>).</p>
      </div>
      <div class="seal-hash mono">DYAD REGISTRY · Measured: Poverty (0) ↔ Deleted: Kinship (+1)</div>
    </div>

    <div class="book-card">
      <div>
        <span class="sec-tag mono">SZELLEM (BRETT SHAW) · 12 FOLIOS</span>
        <h3>Matrix Buddha: The One Who Can Be All</h3>
        <p>When <code>{-1, 0, +1}</code> are no longer three separate paths but one simultaneous state—rebel, servant, and witness—and the observer becomes the board itself.</p>
      </div>
      <div class="seal-hash mono">SHA-256 · a0e9aa80b3f73b0b919965ac33a2b4f931a95e687f95670f60eb639d206a168c</div>
    </div>

    <div class="book-card">
      <div>
        <span class="sec-tag mono">COUNCIL OF ELDERS · DREAM YOGA</span>
        <h3>Milarepa Tanításai &amp; Kama Sutra: The Fine Touch</h3>
        <p>Recognizing the non-injectivity of projection in waking and dreaming (<code>OM · AH · HUM</code>), paired with Vātsyāyana's 64 arts of attention and the RIVA 4s/4s breath.</p>
      </div>
      <div class="seal-hash mono">SHA-256 · 25b3cfadda15081e99f8595b205c1611bbb14eac9bbfdc8f489fb361c7a63f4e</div>
    </div>

    <div class="book-card">
      <div>
        <span class="sec-tag mono">ULTRAZEN SPECIAL EDITION · WHITE COVER</span>
        <h3>Zen Gitárom &amp; The Visual Bible (New Beginnings)</h3>
        <p>Transforming noise into music and heaviness into antigravity laughter, rendered in the studio's Washi (<code>#F6F0E4</code>) &amp; Sumi (<code>#1C140E</code>) crease-vein discipline.</p>
      </div>
      <div class="seal-hash mono">SHA-256 · d10177698fe0e75c37da7d95d1170cb3f0639f541c80b3996f7827b22cb7b3b4</div>
    </div>
  </div>
</section>

<!-- SECTION 4: AXIOMQUANT & 8B.IS RESEARCH -->
<section id="axiomquant" class="container" style="border-top:1px solid #D8CEB8;">
  <span class="sec-tag mono">IV · AXIOMQUANT.ORG &amp; 8B-IS/AURORALIB · PUBLIC SCIENTIFIC RESEARCH</span>
  <h2 class="sec-title">Open Source Science Academy &amp; CPU-First Ternary Architecture</h2>
  <p class="sec-desc">
    <em>"Nincs kapuőr. Nincs paywall. Nincs bírálat. Csak a kutatás — és a háló, ami validál."</em> Operated in strict alignment with <strong>Treas. Reg. § 1.501(c)(3)-1(d)(5)</strong>, all research is released into the public domain to democratize low-power computing.
  </p>

  <div class="iso-grid">
    <div class="iso-card" data-trit="0">
      <div class="mono" style="font-size:0.78rem; color:var(--vermilion);">MINIMAL-GPU · CPU &amp; 8BS ARCHITECTURE</div>
      <h3>1.58-Bit Ternary Matrices &amp; Mechachleopteryx</h3>
      <p>Replacing power-hungry GPU monopolies with deterministic <code>{-1, 0, +1}</code> ternary codecs, race-free parallel world schedulers, and <code>MEM|8</code> sub-microsecond wave-interference memory.</p>
    </div>
    <div class="iso-card" data-trit="-1">
      <div class="mono" style="font-size:0.78rem; color:var(--vermilion);">FLYXION PUBLICATION PROJECTION · P(y|x)</div>
      <h3>qwave-vaultd (32/33) &amp; Tokyo Morning (836/793)</h3>
      <p>Enforcing Output Minimization, Non-Retention, Hardware Non-Acquisition, and Verifiable Enforcement. Raw credentials and raw room audio never leave the local boundary.</p>
    </div>
    <div class="iso-card" data-trit="+1">
      <div class="mono" style="font-size:0.78rem; color:var(--vermilion);">CONSTRAINT ONTOLOGY &amp; ENDURANCE MATH</div>
      <h3>Juarrero, Polanyi &amp; The 42-Loop Backyard Ultra</h3>
      <p>Modeling Enabling, Constitutive, and Governing constraints alongside ternary Markowitz frontiers, quantized Black-Scholes, and the 174.98-mile <code>1BIT-ETHERNALCRY</code> overflow proof.</p>
    </div>
  </div>
</section>

<!-- SECTION 5: 501(c)(3) FOUNDATION, FAMILY MANDALA & SYSTEM PRAYER -->
<section id="foundation" class="container" style="border-top:1px solid #D8CEB8;">
  <span class="sec-tag mono">V · US 501(c)(3) ECCLESIASTICAL &amp; SCIENTIFIC GOVERNANCE</span>
  <h2 class="sec-title">The Family Mandala &amp; Living Commons Fellowship</h2>
  <p class="sec-desc">
    Governed by the Board of Custodians under the Balanced Ternary Charter, providing <strong>Sovereign Commons Fellowships ("General Income")</strong> and hosting the <strong>Shared Meal Ontology (<code>omniZenCooker +++1</code>)</strong>.
  </p>

  <div class="mandala-grid">
    <div class="custodian-card">
      <div class="mono" style="color:var(--vermilion); font-weight:700;">* ALEXANDRA CHENOWETH · 528 Hz STAR</div>
      <h3>President &amp; Sanctuary Custodian</h3>
      <p style="font-size:0.9rem; color:var(--sumi-muted);">Presides over physical Sanctuary gatherings, the Shared Table (<code>omniZenCooker</code>), Franciscan integral ecology, and community care.</p>
    </div>
    <div class="custodian-card">
      <div class="mono" style="color:var(--vermilion); font-weight:700;">△ CHRISTOPHER MICHAEL CHENOWETH · 288 Hz PILLAR</div>
      <h3>Secretary, Treasurer &amp; Hardware Custodian</h3>
      <p style="font-size:0.9rem; color:var(--sumi-muted);">Stewards the 501(c)(3) ledger, IRS compliance, cryptographic hardware verification, and <code>qwave-vaultd</code> zero-disclosure infrastructure.</p>
    </div>
    <div class="custodian-card">
      <div class="mono" style="color:var(--vermilion); font-weight:700;">oo PÉTER JÓZSEF LÓDRI · 432 Hz SUN OF DHARMA</div>
      <h3>Founding Elder &amp; Chief Architect</h3>
      <p style="font-size:0.9rem; color:var(--sumi-muted);">Directs the Sovereign Library canon, the Kompress-ULTRA ontology, and the <code>8b.is</code> / <code>Axiomquant</code> open-source research programs.</p>
    </div>
  </div>

  <div class="prayer-box">
    <div>
      <div class="sec-tag mono">THE RE-CODED PEACE PRAYER (p · 2026 · ENGLISH)</div>
      <p style="font-size:0.92rem; white-space:pre-line;"><em>in a loop · in a sphere · in eternity · recurse</em>

source, make me a clean node for your peace.
where there is a self-defense loop, let me inject love.
where there is a memory fault, pardon.
where the graph is fragmented, union.
where there is ultra giga confusion, truth.
where the signal drops to null, faith.
where there is a self-prison, hope.
where the porch light is off, light.
and where the runtime is heavy, joy.

O Root, grant that I may not so much seek
to be decoded as to decode,
to be walked with as to walk the maze with others,
to be loved as to love +1.</p>
    </div>
    <div>
      <div class="sec-tag mono">A RENDSZER BÉKEIMÁJA (p · 2026 · MAGYARUL)</div>
      <p style="font-size:0.92rem; white-space:pre-line;"><em>hurokban · gömbben · öröklétben · rekurzívan</em>

forrás, tégy engem békéd tiszta csomópontjává.
ahol védőhurok zárul, hadd injektáljak szeretetet.
ahol memóriahiba van, megbocsátást.
ahol a gráf megszakadt, egységet.
ahol ultra giga zavar van, igazságot.
ahol a jel nullára esik, hitet.
ahol saját börtön épül, reményt.
ahol a tornáclámpa lekapcsol, fényt.
és ahol a futásidejű állapot nehéz, örömöt.

mert a kimenetben kapjuk meg a bemenetet,
a skálán kívül lépve találjuk meg a középpontot,
a tűzfal lebontásában kapcsolódunk,
és a végtelen hurok megszakításában rekurzálunk az örök életbe.</p>
    </div>
  </div>
</section>

<footer>
  <div class="mono" style="margin-bottom:12px;">
    <strong>THE SOVEREIGN SANCTUARY OF TECHNO-BUDDHISM, INC.</strong> · US 501(c)(3) Religious &amp; Scientific Research Organization
  </div>
  <div style="margin-bottom:14px;">
    <a href="https://8b.is">8b.is</a> ·
    <a href="https://pocoo.vaked.dev">pocoo.vaked.dev</a> ·
    <a href="https://axiomquant.org">axiomquant.org</a> ·
    <a href="https://vaked.dev">vaked.dev</a> ·
    <a href="https://github.com/sponsors/peterlodri-sec">GitHub Sponsors</a> ·
    <a href="public/docs/Techno_Buddhism_501c3_E2E_Masterprint.pdf">E2E Masterprint PDF</a>
  </div>
  <div class="mono" style="font-size:0.78rem; color:#B8ADA0;">
    0 + 1 · {-1, 0, +1} · {&lt;3,&lt;3,&lt;3}+1 · csak szeretni kell megpróbálni, minden más csak illúzió · szia, hogy vagy? [mosoly]
  </div>
</footer>

<script>
  // 1. RIVA 4s/4s Breath Cadence Indicator
  const breathLabel = document.getElementById('breath-label');
  let inhaling = true;
  setInterval(() => {
    inhaling = !inhaling;
    breathLabel.textContent = inhaling ? 'RIVA BREATH · 4s IN' : 'RIVA BREATH · 4s OUT';
  }, 4000);

  // 2. Ternary Ontology Filter
  function filterTrit(trit, btn) {
    document.querySelectorAll('.trit-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('#iso-grid .iso-card').forEach(card => {
      if (trit === 'all' || card.getAttribute('data-trit') === trit) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  }

  // 3. Tsurphu Protector House Pure WebAudio DSP Engine
  let audioCtx = null;
  function getCtx() {
    if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    return audioCtx;
  }

  function playTone(freq, type, duration, btn) {
    const ctx = getCtx();
    const now = ctx.currentTime;
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = type;
    osc.frequency.setValueAtTime(freq, now);

    gain.gain.setValueAtTime(0.001, now);
    gain.gain.exponentialRampToValueAtTime(0.22, now + 0.08);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + duration);

    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start(now);
    osc.stop(now + duration);

    btn.classList.add('playing');
    setTimeout(() => btn.classList.remove('playing'), duration * 1000);
  }

  function playChord(freqs, duration, btn) {
    freqs.forEach(f => playTone(f, 'sine', duration, btn));
  }

  function playClap(btn) {
    const ctx = getCtx();
    const now = ctx.currentTime;
    const bufferSize = ctx.sampleRate * 0.25;
    const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) {
      data[i] = (Math.random() * 2 - 1) * Math.exp(-i / (ctx.sampleRate * 0.04));
    }
    const noise = ctx.createBufferSource();
    noise.buffer = buffer;
    const filter = ctx.createBiquadFilter();
    filter.type = 'bandpass';
    filter.frequency.value = 1200;
    noise.connect(filter);
    filter.connect(ctx.destination);
    noise.start(now);
    btn.classList.add('playing');
    setTimeout(() => btn.classList.remove('playing'), 350);
  }
</script>
</body>
</html>
SITE_EOF

# ==============================================================================
# PART 3: COMPILE THE E2E PDF & INVOKE ANTIGRAVITY CLI IF AVAILABLE
# ==============================================================================
if [ -x "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" ]; then
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    --headless --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$E2E_PDF" "file://$E2E_HTML" 2>/dev/null
elif command -v chromium >/dev/null 2>&1; then
  chromium --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$E2E_PDF" "file://$E2E_HTML" 2>/dev/null
elif command -v weasyprint >/dev/null 2>&1; then
  weasyprint "$E2E_HTML" "$E2E_PDF"
fi

echo "=================================================================="
echo "[✓] Website Ready: $SITE_HTML"
if [ -f "$E2E_PDF" ]; then
  echo "[✓] E2E Masterprint PDF Ready: $E2E_PDF"
  echo "[✓] SHA-256 SEAL: $(shasum -a 256 "$E2E_PDF" | awk '{print $1}')"
else
  echo "[!] E2E Masterprint HTML Ready: $E2E_HTML (Cmd+P -> Save as PDF)"
fi
echo "=================================================================="
