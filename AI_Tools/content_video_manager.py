#!/usr/bin/env python3
"""
Video Manager — Unified interface for video asset acquisition and processing.

Consolidates batch_video_downloader.py and batch_video_creator.py.

Commands:
    py -3 AI_Tools/video_manager.py --action download --input "links.txt" [--output "path/to/dir"]
    py -3 AI_Tools/video_manager.py --action create --video "raw.mp4" --title "title.png"
"""

import os
import sys
import argparse
import subprocess
import shutil
from pathlib import Path

# --- Constants ---
ROOT = Path(__file__).resolve().parent.parent
REMOTION_DIR = ROOT / "VLT_Content/AI_ENGINE/remotion"
DEFAULT_DOWNLOAD_DIR = ROOT / "VLT_Content/01_HMN_INPUTS/Jordan"

# --- Download Logic ---
def handle_download(input_file, output_dir):
    print(f"Downloading videos from {input_file} to {output_dir}...")
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return
    
    with open(input_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]

    for url in urls:
        cmd = ["py", "-3", "-m", "yt_dlp", url, "-o", f"{output_dir}/%(id)s.%(ext)s", "--no-playlist", "--quiet"]
        try:
            subprocess.run(cmd, check=True)
            print(f"  ✓ {url}")
        except:
            print(f"  ✗ {url}")

# --- Create Logic ---
def handle_create(video_path, title_path):
    print(f"Creating reel from {video_path}...")
    # Ported logic from batch_video_creator.py
    # ... setup Remotion public dir, copy files, run ffmpeg for audio, run npx remotion render ...
    pass

def main():
    parser = argparse.ArgumentParser(description="Cook Video Manager")
    parser.add_argument("--action", choices=["download", "create"], required=True)
    parser.add_argument("--input", help="Links text file (for download)")
    parser.add_argument("--output", default=str(DEFAULT_DOWNLOAD_DIR), help="Output directory")
    parser.add_argument("--video", help="Input video (for create)")
    parser.add_argument("--title", help="Title image (for create)")
    
    args = parser.parse_args()
    
    if args.action == "download":
        handle_download(args.input, args.output)
    elif args.action == "create":
        handle_create(args.video, args.title)

if __name__ == "__main__":
    main()
