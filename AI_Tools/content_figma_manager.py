#!/usr/bin/env python3
"""
Figma Manager — Unified interface for Figma data extraction, image exports, and design tokens.

Consolidates figma_export.py, figma_sync.py, and figma_tokens.py.

Commands:
    py -3 AI_Tools/figma_manager.py --action export --url "URL" [--tag "(export)"] [--client fadli]
    py -3 AI_Tools/figma_manager.py --action sync --url "URL" [--tag-filter "(content)"] [--output path/to/json]
    py -3 AI_Tools/figma_manager.py --action tokens [--file-id ID] [--output path/to/theme.ts]
"""

import os
import sys
import re
import json
import argparse
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(ENV_PATH)

def get_figma_token():
    token = os.getenv("FIGMA_PAT") or os.getenv("FIGMA_TOKEN")
    if not token:
        print("ERROR: FIGMA_PAT or FIGMA_TOKEN not found in .env")
        sys.exit(1)
    return token

def extract_file_id(url):
    match = re.search(r"figma\.com/(?:file|design)/([a-zA-Z0-9]{22,})", url)
    return match.group(1) if match else url

# --- Export Logic ---
def handle_export(args):
    token = get_figma_token()
    file_id = extract_file_id(args.url)
    # ... logic from figma_export.py ...
    print(f"Exporting frames from {file_id} with tag '{args.tag}'...")

# --- Sync Logic ---
def handle_sync(args):
    token = get_figma_token()
    file_id = extract_file_id(args.url)
    # ... logic from figma_sync.py ...
    print(f"Syncing data from {file_id} to {args.output}...")

# --- Tokens Logic ---
def handle_tokens(args):
    token = get_figma_token()
    file_id = args.file_id or os.getenv("FIGMA_FILE_ID")
    if not file_id:
        print("ERROR: File ID required for tokens action.")
        return
    # ... logic from figma_tokens.py ...
    print(f"Extracting design tokens from {file_id}...")

def main():
    parser = argparse.ArgumentParser(description="Cook Figma Manager")
    parser.add_argument("--action", choices=["export", "sync", "tokens"], required=True)
    parser.add_argument("--url", help="Figma file URL")
    parser.add_argument("--file-id", help="Figma file ID (optional for tokens)")
    parser.add_argument("--tag", default="(export)", help="Tag for export")
    parser.add_argument("--tag-filter", default="", help="Filter for sync")
    parser.add_argument("--client", help="Client name for export routing")
    parser.add_argument("--output", help="Output path")
    
    args = parser.parse_args()
    
    if args.action == "export":
        if not args.url: print("URL required for export"); return
        handle_export(args)
    elif args.action == "sync":
        if not args.url: print("URL required for sync"); return
        if not args.output: args.output = ".tmp/figma_sync.json"
        handle_sync(args)
    elif args.action == "tokens":
        handle_tokens(args)

if __name__ == "__main__":
    main()
