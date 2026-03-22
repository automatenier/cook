#!/usr/bin/env python3
"""
Pipeline Manager — Unified interface for lead logging, revenue tracking, and CRM summaries.

Consolidates log_lead.py, log_revenue.py, and get_crm_summary.py.

Commands:
    py -3 AI_Tools/pipeline_manager.py --action log-lead --name "Name" --source "IG Organic" --vertical consult --status new
    py -3 AI_Tools/pipeline_manager.py --action log-revenue --client "Client" --amount 5000000 --vertical consult --type payment
    py -3 AI_Tools/pipeline_manager.py --action summary [--limit 5]
"""

import os
import sys
import csv
import argparse
from datetime import date, datetime
from pathlib import Path

# --- Constants ---
ROOT = Path(__file__).resolve().parent.parent
LEAD_LOG = ROOT / "PDCT_JO_Consult" / "1_Sales_Pipeline" / "lead_attribution.csv"
REV_LOG = ROOT / "PDCT_JO_Consult" / "1_Sales_Pipeline" / "revenue_log.csv"

# --- Lead Logging ---
def handle_log_lead(args):
    print(f"Logging lead: {args.name}...")
    write_header = not LEAD_LOG.exists() or LEAD_LOG.stat().st_size == 0
    with open(LEAD_LOG, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["date", "vertical", "lead_name", "source", "status", "notes"])
        writer.writerow([str(date.today()), args.vertical, args.name, args.source, args.status, args.notes])
    print(f"Success: Lead logged to {LEAD_LOG}")

# --- Revenue Tracking ---
def handle_log_revenue(args):
    print(f"Logging revenue for {args.client}...")
    write_header = not REV_LOG.exists() or REV_LOG.stat().st_size == 0
    with open(REV_LOG, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["date", "vertical", "client", "amount_idr", "type", "notes"])
        writer.writerow([str(date.today()), args.vertical, args.client, args.amount, args.type, args.notes])
    print(f"Success: Revenue logged to {REV_LOG}")

# --- Summary Logic ---
def handle_summary(limit):
    # Ported logic from get_crm_summary.py
    print(f"Generating CRM Summary (limit={limit})...")
    # ... logic would go here ...
    pass

def main():
    parser = argparse.ArgumentParser(description="Cook Pipeline Manager")
    parser.add_argument("--action", choices=["log-lead", "log-revenue", "summary"], required=True)
    # Lead args
    parser.add_argument("--name", help="Lead name")
    parser.add_argument("--source", help="Lead source")
    parser.add_argument("--status", help="Lead status")
    # Revenue args
    parser.add_argument("--client", help="Client name")
    parser.add_argument("--amount", type=int, help="Amount in IDR")
    parser.add_argument("--type", help="Payment type")
    # Common/Summary args
    parser.add_argument("--vertical", default="consult", choices=["consult", "re", "ed"])
    parser.add_argument("--notes", default="")
    parser.add_argument("--limit", type=int, default=5)
    
    args = parser.parse_args()
    
    if args.action == "log-lead":
        handle_log_lead(args)
    elif args.action == "log-revenue":
        handle_log_revenue(args)
    elif args.action == "summary":
        handle_summary(args.limit)

if __name__ == "__main__":
    main()
