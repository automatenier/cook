"""
re_linkedin_scraper.py — Find GIIC employee profiles via DuckDuckGo search
No LinkedIn account, no subscription, no API key needed.

Run: py -3 AI_Tools/re_linkedin_scraper.py

Output: PDCT_Real_Estate/pipeline/giic_linkedin_leads.csv
"""

import csv
import time
import re
import random
from pathlib import Path

try:
    from ddgs import DDGS
except ImportError:
    print("Installing ddgs...")
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "ddgs", "-q"])
    from ddgs import DDGS

OUTPUT = Path(__file__).parent.parent / "PDCT_Real_Estate/pipeline/giic_linkedin_leads.csv"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

# Target: professionals working in GIIC/Cikarang area — likely homebuyers/investors
SEARCH_QUERIES = [
    'site:linkedin.com/in "GIIC" "Cikarang"',
    'site:linkedin.com/in "Kota Deltamas" Cikarang',
    'site:linkedin.com/in "Greenland International Industrial Center"',
    'site:linkedin.com/in "Toyota Manufacturing Indonesia" Cikarang',
    'site:linkedin.com/in "Panasonic" GIIC Indonesia',
    'site:linkedin.com/in "Astra" Cikarang manufacturing',
    'site:linkedin.com/in "Unilever" Cikarang Indonesia',
    'site:linkedin.com/in "EJIP" OR "MM2100" Cikarang engineer',
    'site:linkedin.com/in "pabrik Cikarang" supervisor manager',
    'site:linkedin.com/in Cikarang "industrial" HR Indonesia',
    'site:linkedin.com/in "Delta Silicon" Cikarang Indonesia',
    'site:linkedin.com/in "Jababeka" Cikarang Indonesia',
    'site:linkedin.com/in "Bekasi" "manufacturing" manager Indonesia',
    'site:linkedin.com/in GIIC Deltamas Indonesia',
]

MAX_RESULTS_PER_QUERY = 15


def parse_profile(result: dict, query: str) -> dict:
    title = result.get("title", "")
    url = result.get("href", "")
    snippet = result.get("body", "")

    # Extract name: "Name - Role | LinkedIn" or "Name | LinkedIn"
    name = re.split(r"\s[-–|]\s", title)[0].strip()
    name = re.sub(r"\s*\|?\s*LinkedIn.*", "", name, flags=re.IGNORECASE).strip()

    # Extract role and company from title remainder
    role = ""
    company = ""
    title_remainder = title.replace(name, "").strip(" -–|")
    title_parts = [p.strip() for p in re.split(r"[-–|]", title_remainder) if p.strip()]
    title_parts = [p for p in title_parts if "LinkedIn" not in p]
    if title_parts:
        role = title_parts[0]
    if len(title_parts) > 1:
        company = title_parts[1]

    # Clean snippet
    snippet_clean = snippet[:250] if snippet else ""

    return {
        "name": name,
        "linkedin_url": url,
        "role": role,
        "company": company,
        "snippet": snippet_clean,
        "source_query": query,
    }


def run():
    print("GIIC LinkedIn Lead Scraper — DuckDuckGo Method")
    print("=" * 50)
    print(f"Running {len(SEARCH_QUERIES)} queries, max {MAX_RESULTS_PER_QUERY} results each\n")

    all_results = []
    seen_urls = set()

    with DDGS() as ddgs:
        for i, query in enumerate(SEARCH_QUERIES, 1):
            print(f"[{i}/{len(SEARCH_QUERIES)}] {query[:70]}...")

            try:
                raw = list(ddgs.text(query, max_results=MAX_RESULTS_PER_QUERY))
            except Exception as e:
                print(f"  Error: {e}")
                time.sleep(5)
                continue

            # Filter to LinkedIn profile URLs only
            profiles = [r for r in raw if "linkedin.com/in/" in r.get("href", "")]

            new = 0
            for r in profiles:
                url = r["href"]
                if url not in seen_urls:
                    seen_urls.add(url)
                    all_results.append(parse_profile(r, query))
                    new += 1

            print(f"  {len(profiles)} profiles found, {new} new | Total: {len(all_results)}")

            if i < len(SEARCH_QUERIES):
                delay = random.uniform(2, 5)
                time.sleep(delay)

    if not all_results:
        print("\nNo results found.")
        return

    # Sort: profiles with both role+company first
    all_results.sort(key=lambda r: -(bool(r["role"]) + bool(r["company"])))

    # Write CSV
    fieldnames = ["name", "linkedin_url", "role", "company", "snippet", "source_query"]
    with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_results)

    print(f"\nDone: {len(all_results)} profiles saved -> {OUTPUT}")

    print("\nSample leads:")
    for r in all_results[:15]:
        print(f"  {r['name']}")
        print(f"    Role: {r['role']} | Company: {r['company']}")
        print(f"    URL:  {r['linkedin_url']}")

    # Company distribution
    companies = {}
    for r in all_results:
        c = r["company"][:35] if r["company"] else "—"
        companies[c] = companies.get(c, 0) + 1
    print("\nTop companies:")
    for company, count in sorted(companies.items(), key=lambda x: -x[1])[:10]:
        print(f"  {count:3d}  {company}")


if __name__ == "__main__":
    run()
