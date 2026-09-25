#!/usr/bin/env python3
"""Generate a public index (README.md, index.html, actors.json) of the
public Apify Store Actors published by one Apify user.

Uses ONLY the unauthenticated public Apify Store API:
    GET https://api.apify.com/v2/store?username=<user>&limit=100&offset=N
No token, no secrets. Only public listing fields are emitted (whitelist).
Standard library only (runs on a bare GitHub Actions runner).

Usage:
    python generate.py                       # fetch live, write next to this script
    python generate.py --out DIR             # write elsewhere
    python generate.py --input store.json    # offline, from a saved API response
    python generate.py --base-url https://<user>.github.io/<repo>/   # also emit sitemap.xml/robots.txt
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

USERNAME = "plym-actor-factory"
STORE_API = "https://api.apify.com/v2/store"
PROFILE_URL = f"https://apify.com/{USERNAME}"
PAGE_TITLE = "Official-register change monitors on Apify | plym-actor-factory"
META_DESC = (
    "Pay-per-event Apify Actors that watch your portfolio of company, licence and "
    "permit identifiers in official public registers (UK, EU, US, Canada, Australia, "
    "Brazil) and emit typed change events. Pay only for delivered events."
)

# Display order of groups.
GROUPS = [
    "United Kingdom",
    "European Union & wider Europe",
    "Cross-border KYB & finance",
    "United States – federal",
    "United States – state",
    "Canada",
    "Australia",
    "Latin America",
    "Global / security",
    "Other",
]

# Explicit mapping for known Actors (name -> group). New Actors fall back to heuristics.
OVERRIDES = {
    "gleif-lei-portfolio-watch": "Cross-border KYB & finance",
    "dach-supplier-kyb-packet": "Cross-border KYB & finance",
    "poland-supplier-kyb-packet": "Cross-border KYB & finance",
    "us-contractor-license-risk-monitor": "United States – state",
    "us-il-idfpr-license-portfolio-monitor": "United States – state",
    "fmcsa-safer-risk-event-monitor": "United States – federal",
    "h1b-lca-employer-filing-watchlist": "United States – federal",
    "lookalike-ct-brand-abuse-monitor": "Global / security",
    "brazil-cnpj-situacao-change-monitor": "Latin America",
}

US_STATE_HINTS = re.compile(
    r"\b(California|Illinois|Texas|Florida|New York|Ohio|Pennsylvania|Washington State|"
    r"Georgia|Michigan|New Jersey|Virginia|Massachusetts|Colorado|Arizona)\b"
)
EUROPE_PREFIXES = (
    "eu-", "czech-", "finland-", "france-", "netherlands-", "norway-", "spain-",
    "switzerland-", "germany-", "austria-", "italy-", "belgium-", "denmark-",
    "sweden-", "ireland-", "portugal-", "estonia-", "latvia-", "lithuania-",
)


def classify(item: dict) -> str:
    name = item["name"]
    if name in OVERRIDES:
        return OVERRIDES[name]
    text = f"{item.get('title', '')} {item.get('description', '')}"
    if "kyb" in name:
        return "Cross-border KYB & finance"
    if name.startswith("uk-"):
        return "United Kingdom"
    if name.startswith(EUROPE_PREFIXES):
        return "European Union & wider Europe"
    if name.startswith(("ca-", "canada-")):
        return "Canada"
    if name.startswith(("au-", "australia-")):
        return "Australia"
    if name.startswith(("brazil-", "mexico-", "chile-", "argentina-", "colombia-")):
        return "Latin America"
    if name.startswith("us-"):
        return "United States – state" if US_STATE_HINTS.search(text) else "United States – federal"
    return "Other"


def fetch_store(username: str) -> list[dict]:
    items, offset, limit = [], 0, 100
    while True:
        qs = urllib.parse.urlencode({"username": username, "limit": limit, "offset": offset})
        req = urllib.request.Request(
            f"{STORE_API}?{qs}",
            headers={"User-Agent": "actor-index-generator/1.0", "Accept": "application/json"},
        )
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, timeout=30) as r:
                    data = json.load(r)["data"]
                break
            except Exception:  # noqa: BLE001 - retry transient errors / 429
                if attempt == 3:
                    raise
                time.sleep(2 ** (attempt + 1))
        page = data.get("items", [])
        items.extend(page)
        offset += len(page)
        if not page or offset >= int(data.get("total", 0)):
            return items


def first_sentence(text: str, max_len: int = 200) -> str:
    text = re.sub(r"\s+", " ", (text or "").strip())
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    s = m.group(1) if m else text
    if len(s) > max_len:
        s = s[: max_len - 1].rsplit(" ", 1)[0] + "…"
    return s


def fmt_usd(v: float) -> str:
    s = f"{v:.5f}".rstrip("0")
    if s.endswith("."):
        s += "00"
    elif len(s.split(".")[1]) < 2:
        s += "0"
    return "$" + s


def pricing(item: dict) -> dict:
    """Public pricing only: model, primary event(s) and Actor start price."""
    info = item.get("currentPricingInfo") or {}
    model = info.get("pricingModel") or "FREE"
    out = {"model": model, "events": [], "startUsd": None}
    events = ((info.get("pricingPerEvent") or {}).get("actorChargeEvents")) or {}
    for key, ev in events.items():
        price = ev.get("eventPriceUsd")
        if key == "apify-actor-start":
            out["startUsd"] = price
            continue
        out["events"].append(
            {"event": key, "title": ev.get("eventTitle") or key, "priceUsd": price,
             "primary": bool(ev.get("isPrimaryEvent"))}
        )
    out["events"].sort(key=lambda e: (not e["primary"], e["event"]))
    return out


def price_label(p: dict) -> str:
    if p["model"] == "PAY_PER_EVENT" and p["events"]:
        e = p["events"][0]
        s = f"{fmt_usd(e['priceUsd'])} per event"
        if len(p["events"]) > 1:
            s += f" (+{len(p['events']) - 1} other event types)"
        return s
    if p["model"] == "FREE":
        return "Free (platform usage only)"
    return p["model"].replace("_", " ").title()


def event_title(a: dict) -> str:
    ev = a["pricing"]["events"]
    return f"Charged per: {ev[0]['title']}" if ev else ""


def normalise(raw: list[dict], username: str) -> list[dict]:
    actors = []
    for it in raw:
        if it.get("username") != username or not it.get("name"):
            continue  # guard: only this user's public Store listings
        p = pricing(it)
        actors.append({
            # --- whitelist of public listing fields only ---
            "name": it["name"],
            "title": it.get("title") or it["name"],
            "url": f"https://apify.com/{username}/{it['name']}",
            "description": re.sub(r"\s+", " ", it.get("description") or "").strip(),
            "useCase": first_sentence(it.get("description") or ""),
            "categories": sorted(it.get("categories") or []),
            "group": classify(it),
            "pricing": p,
            "priceLabel": price_label(p),
        })
    actors.sort(key=lambda a: (GROUPS.index(a["group"]), a["title"].lower()))
    return actors


def grouped(actors):
    for g in GROUPS:
        rows = [a for a in actors if a["group"] == g]
        if rows:
            yield g, rows


def cat_label(c: str) -> str:
    return {"AI": "AI", "DEVELOPER_TOOLS": "Developer tools", "LEAD_GENERATION": "Lead generation",
            "REAL_ESTATE": "Real estate"}.get(c, c.replace("_", " ").capitalize())


def md_escape(s: str) -> str:
    return s.replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")


INTRO = (
    "Pay-per-event [Apify](https://apify.com) Actors that **watch a portfolio of identifiers** "
    "(company numbers, LEIs, licence and permit numbers, facility IDs …) in **official public "
    "registers and open-data feeds**, and emit **typed change events** (status changes, "
    "insolvency notices, licence revocations, new filings, …) instead of raw data dumps. "
    "You pay a small fee only for events actually delivered."
)
AUDIENCE = (
    "Built for compliance, KYB/KYC, supplier-risk, credit, procurement, legal and "
    "data teams who need to know *when something changes* for the entities they "
    "care about – run on a schedule, pipe results to webhooks, Slack, sheets or your "
    "own systems via the Apify API, or call them from AI agents (MCP)."
)


def render_readme(actors) -> str:
    out = [
        "# Official-register change monitors on Apify",
        "",
        INTRO,
        "",
        AUDIENCE,
        "",
        f"**{len(actors)} public Actors** · Browse all on the Apify Store: "
        f"[apify.com/{USERNAME}]({PROFILE_URL})",
        "",
        "Prices are per delivered event in USD, plus a tiny Apify *Actor start* fee "
        "(typically $0.00005 per GB of memory). Always check the Store page for current pricing.",
        "",
        "## Contents",
        "",
    ]
    for g, rows in grouped(actors):
        anchor = re.sub(r"[^a-z0-9 -]", "", g.lower()).replace(" ", "-")
        out.append(f"- [{g}](#{anchor}) ({len(rows)})")
    for g, rows in grouped(actors):
        out += ["", f"## {g}", "", "| Actor | Use case | Price |", "|---|---|---|"]
        for a in rows:
            out.append(
                f"| [{md_escape(a['title'])}]({a['url']}) | {md_escape(a['useCase'])} "
                f"| {md_escape(a['priceLabel'])} |"
            )
    out += [
        "",
        "---",
        "",
        f"All Actors: [{PROFILE_URL}]({PROFILE_URL}). This page is generated automatically "
        "from the public Apify Store listing. Data sources are the official public registers "
        "named in each Actor's description; this project is not affiliated with those registers.",
        "",
    ]
    return "\n".join(out)


CSS = """
:root{--fg:#1d1d1f;--muted:#5f6368;--bg:#fff;--card:#f7f8fa;--line:#e3e5e8;--accent:#0b57d0}
@media (prefers-color-scheme:dark){:root{--fg:#e8eaed;--muted:#9aa0a6;--bg:#131416;--card:#1d1f22;--line:#2e3134;--accent:#8ab4f8}}
*{box-sizing:border-box}
body{margin:0;font:15px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--fg);background:var(--bg)}
main{max-width:1100px;margin:0 auto;padding:32px 20px 64px}
h1{font-size:28px;margin:0 0 12px}
h2{font-size:19px;margin:36px 0 10px;padding-bottom:6px;border-bottom:1px solid var(--line)}
p{margin:0 0 12px;max-width:820px}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
.lead{font-size:16px}.muted{color:var(--muted);font-size:13px}
.bar{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin:22px 0 4px;position:sticky;top:0;background:var(--bg);padding:10px 0;z-index:1}
#q{flex:1;min-width:240px;padding:10px 12px;font-size:15px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--fg)}
.btn{display:inline-block;padding:9px 14px;border-radius:8px;background:var(--accent);color:#fff!important;font-weight:600}
@media (prefers-color-scheme:dark){.btn{color:#131416!important}}
table{width:100%;border-collapse:collapse;font-size:14px}
th,td{text-align:left;vertical-align:top;padding:9px 10px;border-bottom:1px solid var(--line)}
th{font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);font-weight:600}
td.t{width:30%;font-weight:600}td.p{width:17%;white-space:nowrap}
.tag{display:inline-block;font-size:11px;padding:1px 6px;margin:4px 4px 0 0;border-radius:999px;background:var(--card);border:1px solid var(--line);color:var(--muted);font-weight:500}
footer{margin-top:40px;color:var(--muted);font-size:13px}
#none{display:none;padding:20px 0;color:var(--muted)}
"""

JS = """
(function(){var q=document.getElementById('q'),c=document.getElementById('count'),n=document.getElementById('none');
function run(){var t=q.value.trim().toLowerCase().split(/\\s+/).filter(Boolean),shown=0;
document.querySelectorAll('section.g').forEach(function(s){var v=0;s.querySelectorAll('tbody tr').forEach(function(r){
var h=r.getAttribute('data-s'),ok=t.every(function(w){return h.indexOf(w)>-1});r.style.display=ok?'':'none';if(ok)v++});
s.style.display=v?'':'none';shown+=v});c.textContent=shown;n.style.display=shown?'none':'block';}
q.addEventListener('input',run);if(location.hash.indexOf('#q=')===0){q.value=decodeURIComponent(location.hash.slice(3));}run();})();
"""


def render_html(actors, base_url: str | None) -> str:
    e = html.escape
    canon = f'<link rel="canonical" href="{e(base_url)}">\n' if base_url else ""
    ld = {
        "@context": "https://schema.org", "@type": "ItemList", "name": PAGE_TITLE,
        "numberOfItems": len(actors),
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": a["url"], "name": a["title"]}
            for i, a in enumerate(actors)
        ],
    }
    parts = [f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(PAGE_TITLE)}</title>
<meta name="description" content="{e(META_DESC)}">
<meta name="robots" content="index,follow">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(PAGE_TITLE)}">
<meta property="og:description" content="{e(META_DESC)}">
{canon}<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; img-src 'self' data:; base-uri 'none'; form-action 'none'">
<meta name="referrer" content="strict-origin-when-cross-origin">
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False).replace("</", "<\\/")}</script>
</head>
<body>
<main>
<h1>Official-register change monitors on Apify</h1>
<p class="lead">Pay-per-event <a href="https://apify.com">Apify</a> Actors that <strong>watch a portfolio of identifiers</strong> (company numbers, LEIs, licence and permit numbers, facility IDs …) in <strong>official public registers and open-data feeds</strong>, and emit <strong>typed change events</strong> instead of raw data dumps. You pay only for events actually delivered.</p>
<p>Built for compliance, KYB/KYC, supplier-risk, credit, procurement, legal and data teams who need to know <em>when something changes</em> for the entities they care about – run on a schedule, pipe results to webhooks, Slack, sheets or your own systems via the Apify API, or call them from AI agents (MCP).</p>
<div class="bar">
<input id="q" type="search" placeholder="Filter by country, register, identifier or keyword (e.g. UK, insolvency, LEI, licence)…" aria-label="Filter Actors" autocomplete="off">
<span class="muted"><span id="count">{len(actors)}</span> of {len(actors)} Actors</span>
<a class="btn" href="{PROFILE_URL}">All Actors on Apify →</a>
</div>
<p class="muted">Prices are per delivered event in USD, plus a tiny Apify <em>Actor start</em> fee (typically $0.00005 per GB of memory). Check each Store page for current pricing.</p>
"""]
    for g, rows in grouped(actors):
        parts.append(f'<section class="g"><h2>{e(g)} <span class="muted">({len(rows)})</span></h2>\n'
                     '<table><thead><tr><th>Actor</th><th>Use case</th><th>Price</th></tr></thead><tbody>\n')
        for a in rows:
            search = " ".join([a["title"], a["name"], a["description"], g, " ".join(a["categories"])]).lower()
            tags = "".join(f'<span class="tag">{e(cat_label(c))}</span>' for c in a["categories"])
            parts.append(
                f'<tr data-s="{e(search)}"><td class="t"><a href="{e(a["url"])}">{e(a["title"])}</a><br>{tags}</td>'
                f'<td title="{e(a["description"])}">{e(a["useCase"])}</td><td class="p" title="{e(event_title(a))}">{e(a["priceLabel"])}</td></tr>\n'
            )
        parts.append("</tbody></table></section>\n")
    parts.append(f"""<p id="none">No Actors match that filter. <a href="{PROFILE_URL}">Browse all Actors on Apify</a>.</p>
<footer>All Actors: <a href="{PROFILE_URL}">{PROFILE_URL}</a> · Generated automatically from the public Apify Store listing · Data sources are the official public registers named in each Actor's description; not affiliated with those registers. <a href="actors.json">actors.json</a></footer>
</main>
<script>{JS}</script>
</body>
</html>
""")
    return "".join(parts)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument("--input", help="saved Store API JSON response (offline mode)")
    ap.add_argument("--username", default=USERNAME)
    ap.add_argument("--base-url", help="public site URL; enables canonical + sitemap.xml/robots.txt")
    args = ap.parse_args()

    if args.input:
        with open(args.input, encoding="utf-8") as f:
            d = json.load(f)
        raw = d["data"]["items"] if "data" in d else d
    else:
        raw = fetch_store(args.username)
    actors = normalise(raw, args.username)
    if not actors:
        print("No public Actors returned; refusing to overwrite output.", file=sys.stderr)
        return 1

    os.makedirs(args.out, exist_ok=True)
    def write(name, content):
        with open(os.path.join(args.out, name), "w", encoding="utf-8", newline="\n") as f:
            f.write(content)

    write("README.md", render_readme(actors))
    write("index.html", render_html(actors, args.base_url))
    public = [{k: a[k] for k in ("name", "title", "url", "description", "categories", "group", "pricing")}
              for a in actors]
    write("actors.json", json.dumps({"username": args.username, "profile": PROFILE_URL,
                                     "count": len(public), "actors": public},
                                    indent=2, ensure_ascii=False) + "\n")
    if args.base_url:
        base = args.base_url.rstrip("/") + "/"
        write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
              f"  <url><loc>{html.escape(base)}</loc></url>\n</urlset>\n")
        write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {base}sitemap.xml\n")
    print(f"Wrote {len(actors)} Actors to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
