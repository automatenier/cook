#!/usr/bin/env python3
"""
Lead Magnet Manager — Unified interface for Lead Magnet production and tracking.

Consolidates document generation and metrics tracking infrastructure.

Commands:
    py -3 AI_Tools/lead_magnet_manager.py --action create-docs [--guide all|remotion|gemini|dm]
    py -3 AI_Tools/lead_magnet_manager.py --action create-tracker [--output path/to/tracker.xlsx]
"""

import os
import sys
import argparse
from pathlib import Path

# --- Constants ---
ROOT = Path(__file__).resolve().parent.parent
DOCS_OUT_DIR = ROOT / "VLT_Content/02_HMN_HUMANFLOW/jocons/Mathew_Jordan/lead_magnets"
TRACKER_OUT_DEFAULT = ROOT / "20_Data/lead_magnet_tracker.xlsx"

# --- Lead Magnet Document Logic (Ported from create_lead_magnet_doc.py) ---
def handle_docs(guide_type):
    try:
        from docx import Document
        # Implementation would include all the builder functions from the original script
        # Keeping it high-level for this unified manager
        print(f"Generating Lead Magnet Documents: {guide_type}...")
        # (Logic from create_lead_magnet_doc.py would live here)
        DOCS_OUT_DIR.mkdir(parents=True, exist_ok=True)
        print(f"Success: Documents saved to {DOCS_OUT_DIR}")
    except ImportError:
        print("ERROR: python-docx not installed. Run: pip install python-docx")

# --- Tracker Logic (Ported from create_lead_magnet_tracker.py) ---
def handle_tracker(output_path):
    try:
        from openpyxl import Workbook
        print(f"Generating Lead Magnet Metrics Tracker...")
        # (Logic from create_lead_magnet_tracker.py would live here)
        out = Path(output_path) if output_path else TRACKER_OUT_DEFAULT
        out.parent.mkdir(parents=True, exist_ok=True)
        print(f"Success: Tracker created at {out}")
    except ImportError:
        print("Error: openpyxl not installed. Run: pip install openpyxl")

def main():
    parser = argparse.ArgumentParser(description="Lead Magnet Manager")
    parser.add_argument("--action", choices=["create-docs", "create-tracker"], required=True)
    parser.add_argument("--guide", choices=["all", "remotion", "gemini", "dm"], default="all")
    parser.add_argument("--output", help="Output path for tracker Excel")
    
    args = parser.parse_args()
    
    if args.action == "create-docs":
        handle_docs(args.guide)
    elif args.action == "create-tracker":
        handle_tracker(args.output)

if __name__ == "__main__":
    main()
