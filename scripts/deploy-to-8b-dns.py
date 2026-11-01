#!/usr/bin/env python3
"""
Deploys the Sovereign Constellation Foundation (501(c)(3)) Landing Page to 8b.is DNS:
- https://foundation.8b.is
- https://sanctuary.8b.is
- https://dharma.8b.is
- https://techno-buddhism.8b.is
And registers shortlinks on 8b.is:
- https://8b.is/foundation -> https://foundation.8b.is
- https://8b.is/sanctuary  -> https://sanctuary.8b.is
- https://8b.is/dharma     -> https://dharma.8b.is
- https://8b.is/501c3      -> https://foundation.8b.is
"""

import json
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML_CONTENT = (ROOT / "index.html").read_text(encoding="utf-8")
BOOKSTORE_CONTENT = (ROOT / "bookstore.html").read_text(encoding="utf-8")
ORCH_KEY = "8b-peter-sovereign"

DOMAINS = [
    ("foundation.8b.is", "The Sovereign Constellation Foundation — 501(c)(3) Techno-Buddhism & CPU Ternary Hub", HTML_CONTENT),
    ("sanctuary.8b.is", "Universal Hearth Sanctuary & General-Income Fellowship Portal (501(c)(3))", HTML_CONTENT),
    ("dharma.8b.is", "The Sovereign Canon Codex of Techno-Buddhism — 13 Books & Liturgy", HTML_CONTENT),
    ("techno-buddhism.8b.is", "Techno-Buddhism · 8b.is Sovereign Library Bookstore & 501(c)(3) Sanctuary", BOOKSTORE_CONTENT),
    ("technobuddhism.8b.is", "Techno-Buddhism · 8b.is Sovereign Library Bookstore & 501(c)(3) Sanctuary", BOOKSTORE_CONTENT),
    ("bookstore.8b.is", "Sovereign Library Bookstore · 10 Vault Editions & 501(c)(3) Foundation", BOOKSTORE_CONTENT),
]

SHORTLINKS = [
    ("foundation", "https://foundation.8b.is"),
    ("sanctuary", "https://sanctuary.8b.is"),
    ("dharma", "https://dharma.8b.is"),
    ("501c3", "https://foundation.8b.is"),
    ("hearth", "https://sanctuary.8b.is"),
    ("bookstore", "https://techno-buddhism.8b.is"),
    ("techno-buddhism", "https://techno-buddhism.8b.is"),
]


def post_json(url: str, payload: dict, headers: dict = None) -> dict:
    data = json.dumps(payload).encode("utf-8")
    hdrs = {"Content-Type": "application/json", "User-Agent": "8b-is-sovereign-deployer/1.0"}
    if headers:
        hdrs.update(headers)
    req = urllib.request.Request(url, data=data, headers=hdrs, method="POST")
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    print("⟦ DEPLOYING TO 8B.IS SOVEREIGN DNS ORCHESTRATOR ⟧")
    for domain, title, content in DOMAINS:
        payload = {
            "domain": domain,
            "title": title,
            "owner": "p@8b.is",
            "mode": "inline_html",
            "tls_ca": "letsencrypt",
            "git_url": "https://github.com/8b-is/techno-buddhism-foundation.git",
            "git_branch": "main",
            "inline_html": content,
            "key": ORCH_KEY,
        }
        res = post_json(
            f"https://8b.is/api/orchestrator/sites?key={ORCH_KEY}",
            payload,
            {"x-sovereign-key": ORCH_KEY},
        )
        print(f"  [SITE] {domain:26s} -> ok={res.get('ok')} ({res.get('message', '')})")

        dep = post_json(
            f"https://8b.is/api/orchestrator/sites/deploy?key={ORCH_KEY}",
            {"domain": domain},
            {"x-sovereign-key": ORCH_KEY},
        )
        print(f"  [SYNC] {domain:26s} -> {dep.get('deploy_result')}")

    print("\n⟦ REGISTERING 8B.IS SHORTLINKS IN DATABOMB MVCC ⟧")
    for slug, target in SHORTLINKS:
        for host in ("https://i1.is/api/short",):
            try:
                res = post_json(
                    host,
                    {
                        "domain": "8b.is",
                        "slug": slug,
                        "target_url": target,
                        "owner_email": "p@8b.is",
                    },
                )
                print(f"  [SHORT] https://8b.is/{slug:14s} -> {res.get('short_url')} ({res.get('status')})")
            except Exception as e:
                print(f"  [SHORT] {slug}: {e}")


if __name__ == "__main__":
    main()
