"""
Sprint Status Checker — shows today's agenda for all active clients

Reads: AI_MEMORY/JOConsults.md  (active client list + start dates)
       PDCT_JO_Consult/deliverables/Z Products/Client Worksheet/Client_X_Worksheet.md

Usage:
  py -3 AI_Tools/client_status.py
  py -3 AI_Tools/client_status.py --client Fadli
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

BASE      = Path(__file__).parent.parent
MEMORY    = BASE / "AI_MEMORY" / "JOConsults.md"
WORKSHEET_DIR = BASE / "PDCT_JO_Consult" / "deliverables" / "Z Products" / "Client Worksheet"

# 14-day sprint milestone map
SPRINT = {
    0:  "Onboarding call + contracts signed",
    1:  "Brand questionnaire submitted by client",
    2:  "Offer sheet drafted (run offer_agent.py)",
    3:  "Content audit done (run analyze_viral_reel.py)",
    4:  "ONSITE filming session (JABODETABEK)",
    5:  "Viral formats identified + reel strategy",
    6:  "VSL script drafted",
    7:  "First reel posted",
    8:  "Lead magnet ready",
    9:  "Repurpose batch (run repurpose_content.py)",
    10: "Setter activated — DM scripts live",
    11: "n8n automation deployed",
    12: "Lead activation — CTA live",
    13: "Performance review + metrics pull",
    14: "Retainer pitch + Day-14 handover call",
}

def parse_active_clients(memory_path: Path) -> list[dict]:
    """Parse active clients table from JOConsults.md"""
    clients = []
    if not memory_path.exists():
        return clients

    text = memory_path.read_text(encoding="utf-8")
    # Find the Active Clients table
    table_match = re.search(
        r"##\s+Active Clients.*?\n(\|.+\n)+", text, re.DOTALL
    )
    if not table_match:
        return clients

    for line in table_match.group(0).splitlines():
        if not line.startswith("|") or "---" in line or "Client" in line:
            continue
        parts = [p.strip() for p in line.split("|") if p.strip()]
        if len(parts) >= 5:
            try:
                start_str = parts[4].strip("`")
                start = date.fromisoformat(start_str)
                clients.append({
                    "name":      parts[0],
                    "tier":      parts[1],
                    "phase":     parts[2],
                    "start":     start,
                    "day":       (date.today() - start).days,
                    "worksheet": parts[5] if len(parts) > 5 else "",
                })
            except (ValueError, IndexError):
                continue
    return clients


def get_worksheet_state(client_name: str) -> dict:
    """Find and read current state from worksheet"""
    # Try to find worksheet by client name
    for ws_file in WORKSHEET_DIR.glob("*.md"):
        text = ws_file.read_text(encoding="utf-8", errors="ignore")
        if client_name.lower() in text.lower():
            # Extract CURRENT STATE table
            state = {"file": ws_file.name, "day": "?", "phase": "?", "paused": ""}
            m = re.search(r"\*\*Day\*\*\s*\|\s*(\d+)", text)
            if m: state["day"] = m.group(1)
            m = re.search(r"\*\*Phase\*\*\s*\|\s*(.+)", text)
            if m: state["phase"] = m.group(1).strip()
            m = re.search(r"\*\*Paused.*?\*\*\s*\|\s*(.+)", text)
            if m: state["paused"] = m.group(1).strip()
            return state
    return {}


def print_client_status(client: dict, show_worksheet: bool = True):
    day = client["day"]
    today_task = SPRINT.get(day, SPRINT.get(14, "Retainer / post-sprint"))
    prev_task  = SPRINT.get(day - 1, "—") if day > 0 else "—"
    next_task  = SPRINT.get(day + 1, "Retainer phase") if day < 14 else "Post-sprint"

    bar_done  = min(day, 14)
    bar_total = 14
    bar       = "█" * bar_done + "░" * (bar_total - bar_done)

    print(f"\n{'='*60}")
    print(f"  CLIENT  : {client['name']}  |  {client['tier']}")
    print(f"  STARTED : {client['start'].strftime('%d %b %Y')}  |  DAY {day} / 14")
    print(f"  PROGRESS: [{bar}] {int(bar_done/bar_total*100)}%")
    print(f"{'─'*60}")
    print(f"  YESTERDAY : {prev_task}")
    print(f"  TODAY     : {today_task}")
    print(f"  TOMORROW  : {next_task}")

    if day > 14:
        print(f"\n  *** Sprint complete — pitch retainer if not yet done ***")

    if show_worksheet:
        ws = get_worksheet_state(client["name"])
        if ws:
            print(f"\n  WORKSHEET : {ws['file']}")
            print(f"  WS STATE  : Day {ws['day']} | {ws['phase']}")
            if ws["paused"] and ws["paused"] not in ("-", "Nothing", ""):
                print(f"  BLOCKED   : {ws['paused']}")
        else:
            print(f"\n  WORKSHEET : Not found in {WORKSHEET_DIR.name}/")

    print()


def main():
    ap = argparse.ArgumentParser(description="Sprint status for active clients")
    ap.add_argument("--client", help="Filter by client name (optional)")
    args = ap.parse_args()

    print(f"\n  COOK — CLIENT SPRINT STATUS  |  {date.today().strftime('%A, %d %B %Y')}")

    clients = parse_active_clients(MEMORY)

    if not clients:
        # Fallback: hardcoded known clients
        print("\n  (MEMORY not parseable — using known data)")
        clients = [
            {"name": "Fadli", "tier": "Bedah Digital",
             "start": date(2026, 2, 21), "day": (date.today() - date(2026, 2, 21)).days,
             "phase": "Onboarding", "worksheet": "Client_2_Worksheet.md"},
        ]

    if args.client:
        clients = [c for c in clients if args.client.lower() in c["name"].lower()]
        if not clients:
            print(f"\n  No active client matching '{args.client}'")
            sys.exit(1)

    for client in clients:
        print_client_status(client)

    if not clients:
        print("\n  No active clients found in JOConsults.md")


if __name__ == "__main__":
    main()
