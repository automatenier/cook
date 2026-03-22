"""
query_footage.py — Footage Library Query Tool

Usage:
  python tools/query_footage.py                          # List all clips
  python tools/query_footage.py --category intro         # Filter by category
  python tools/query_footage.py --min-score 8            # Virality score >= 8
  python tools/query_footage.py --category hook --min-score 7
  python tools/query_footage.py --tag talking-head
  python tools/query_footage.py --top 5                  # Top 5 by virality score
  python tools/query_footage.py --log INT-001            # Log a use of a clip (+1 used, updates date)
"""

import csv
import argparse
import os
from datetime import date
from tabulate import tabulate

LIBRARY_PATH = os.path.join(os.path.dirname(__file__), "..", "content", "library", "footage_library.csv")


def load_library():
    with open(LIBRARY_PATH, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_library(rows):
    fieldnames = rows[0].keys()
    with open(LIBRARY_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def display(rows):
    if not rows:
        print("No clips found.")
        return
    headers = ["ID", "Title", "Category", "Duration", "Score", "Used", "Last Used", "Tags"]
    table = [
        [
            r["clip_id"],
            r["title"][:40],
            r["category"],
            f"{r['duration_sec']}s",
            r["virality_score"],
            r["times_used"],
            r["last_used"] or "—",
            r["tags"][:30],
        ]
        for r in rows
    ]
    print(tabulate(table, headers=headers, tablefmt="rounded_outline"))
    print(f"\n{len(rows)} clip(s)")


def main():
    parser = argparse.ArgumentParser(description="Query the footage library")
    parser.add_argument("--category", help="Filter by category (intro, hook, b-roll, cta, transition)")
    parser.add_argument("--min-score", type=int, help="Minimum virality score")
    parser.add_argument("--tag", help="Filter by tag (without #)")
    parser.add_argument("--top", type=int, help="Show top N clips by virality score")
    parser.add_argument("--log", metavar="CLIP_ID", help="Log a use of a clip (increments times_used)")
    args = parser.parse_args()

    rows = load_library()

    # Log a use
    if args.log:
        updated = False
        for row in rows:
            if row["clip_id"].lower() == args.log.lower():
                row["times_used"] = str(int(row["times_used"]) + 1)
                row["last_used"] = date.today().isoformat()
                updated = True
                break
        if updated:
            save_library(rows)
            print(f"Logged use for {args.log}. Total uses: {row['times_used']}, last used: {row['last_used']}")
        else:
            print(f"Clip ID '{args.log}' not found.")
        return

    # Filters
    if args.category:
        rows = [r for r in rows if r["category"].lower() == args.category.lower()]
    if args.min_score:
        rows = [r for r in rows if int(r["virality_score"]) >= args.min_score]
    if args.tag:
        rows = [r for r in rows if f"#{args.tag.lstrip('#')}" in r["tags"]]

    # Sort by virality score desc
    rows = sorted(rows, key=lambda r: int(r["virality_score"]), reverse=True)

    if args.top:
        rows = rows[: args.top]

    display(rows)


if __name__ == "__main__":
    main()
