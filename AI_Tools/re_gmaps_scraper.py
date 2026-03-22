"""
re_gmaps_scraper.py — Google Maps scraper for GIIC Deltamas companies
Uses Google Places API (free tier: ~28k requests/month free credit)

Setup:
  1. Go to console.cloud.google.com → Enable "Places API"
  2. Create API key → add as GOOGLE_MAPS_API_KEY in .env
  3. Run: py -3 AI_Tools/re_gmaps_scraper.py

Output: PDCT_Real_Estate/pipeline/giic_gmaps_leads.csv
"""

import os
import csv
import time
import json
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
OUTPUT = Path(__file__).parent.parent / "PDCT_Real_Estate/pipeline/giic_gmaps_leads.csv"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

# GIIC Deltamas center coordinates
GIIC_LAT = -6.3485
GIIC_LNG = 107.1607
RADIUS_M = 3000  # 3km radius covers the GIIC complex

SEARCH_QUERIES = [
    "manufacturing company GIIC Cikarang",
    "pabrik Greenland International Industrial Center",
    "factory Deltamas Cikarang",
    "perusahaan Jepang GIIC Bekasi",
    "industrial company Kota Deltamas",
]

FIELDS = "name,formatted_address,formatted_phone_number,website,rating,user_ratings_total,business_status,types"


def nearby_search(query: str, page_token: str = None) -> dict:
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": query,
        "location": f"{GIIC_LAT},{GIIC_LNG}",
        "radius": RADIUS_M,
        "key": API_KEY,
    }
    if page_token:
        params["pagetoken"] = page_token
    r = requests.get(url, params=params, timeout=15)
    r.raise_for_status()
    return r.json()


def get_place_details(place_id: str) -> dict:
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {"place_id": place_id, "fields": FIELDS, "key": API_KEY}
    r = requests.get(url, params=params, timeout=15)
    r.raise_for_status()
    return r.json().get("result", {})


def run():
    if not API_KEY:
        print("ERROR: GOOGLE_MAPS_API_KEY not set in .env")
        print("  Get one free at: console.cloud.google.com → Enable Places API → Create key")
        return

    seen_ids = set()
    rows = []

    for query in SEARCH_QUERIES:
        print(f"\nSearching: {query}")
        page_token = None

        for page in range(3):  # max 3 pages = ~60 results per query
            try:
                data = nearby_search(query, page_token)
            except Exception as e:
                print(f"  Error: {e}")
                break

            results = data.get("results", [])
            print(f"  Page {page+1}: {len(results)} results")

            for place in results:
                pid = place.get("place_id")
                if pid in seen_ids:
                    continue
                seen_ids.add(pid)

                # Get full details (phone, website)
                try:
                    details = get_place_details(pid)
                    time.sleep(0.1)  # avoid rate limit
                except Exception as e:
                    details = {}
                    print(f"    Details error for {place.get('name')}: {e}")

                row = {
                    "name": place.get("name", ""),
                    "address": place.get("formatted_address", ""),
                    "phone": details.get("formatted_phone_number", ""),
                    "website": details.get("website", ""),
                    "rating": place.get("rating", ""),
                    "reviews": place.get("user_ratings_total", ""),
                    "status": details.get("business_status", ""),
                    "types": ", ".join(place.get("types", [])),
                    "place_id": pid,
                    "maps_url": f"https://maps.google.com/?cid={pid}",
                    "source_query": query,
                }
                rows.append(row)
                print(f"    + {row['name']} | {row['phone']} | {row['website']}")

            page_token = data.get("next_page_token")
            if not page_token:
                break
            time.sleep(2)  # Google requires delay before using next_page_token

    if not rows:
        print("\nNo results found.")
        return

    # Write CSV
    fieldnames = ["name", "address", "phone", "website", "rating", "reviews",
                  "status", "types", "place_id", "maps_url", "source_query"]
    with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n✓ {len(rows)} companies saved → {OUTPUT}")
    print("\nTop leads (with phone or website):")
    qualified = [r for r in rows if r["phone"] or r["website"]]
    for r in qualified[:10]:
        print(f"  {r['name']} | {r['phone']} | {r['website']}")
    print(f"\nTotal qualified (have contact): {len(qualified)}/{len(rows)}")


if __name__ == "__main__":
    run()
