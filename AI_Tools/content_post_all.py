#!/usr/bin/env python3
"""
content_post_all.py — Orchestrate posting to YouTube, Instagram, and Facebook.

Usage:
  py -3 AI_Tools/content_post_all.py --file "video.mp4" --title "My Title" --description "My Description"
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path

# Add vault auto-unlock
try:
    from cook_vault_manager import decrypt_all
    decrypt_all()
except ImportError:
    pass

def run_command(cmd):
    print(f"Executing: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing {' '.join(cmd)}")
        print(result.stderr)
    else:
        print(result.stdout)
    return result.returncode

def main():
    parser = argparse.ArgumentParser(description="Post video to YouTube, Instagram, and Facebook.")
    parser.add_argument("--file", required=True, help="Path to the video file.")
    parser.add_argument("--title", required=True, help="Title for the post.")
    parser.add_argument("--description", required=True, help="Description/Caption for the post.")
    parser.add_argument("--keywords", help="Keywords/Tags for YouTube.")
    parser.add_argument("--brand", help="Brand key from brands.json (e.g., hts, realestate)")
    
    args = parser.parse_args()
    
    video_path = Path(args.file).resolve()
    if not video_path.exists():
        print(f"Error: Video file not found at {video_path}")
        sys.exit(1)

    # 1. YouTube Upload
    print("--- Posting to YouTube ---")
    yt_cmd = [
        "py", "-3", "AI_Tools/content_youtube_upload.py",
        "--file", str(video_path),
        "--title", args.title,
        "--description", args.description
    ]
    if args.keywords:
        yt_cmd.extend(["--keywords", args.keywords])
    
    yt_status = run_command(yt_cmd)

    # 2. Instagram & Facebook Posting
    print("\n--- Posting to Instagram & Facebook ---")
    fb_ig_cmd = [
        "py", "-3", "AI_Tools/content_fb_ig_post.py",
        "--file", str(video_path),
        "--caption", f"{args.title}\n\n{args.description}",
        "--platform", "both"
    ]
    if args.brand:
        fb_ig_cmd.extend(["--brand", args.brand])
    
    fb_ig_status = run_command(fb_ig_cmd)

    # 3. Threads Posting
    print("\n--- Posting to Threads ---")
    threads_cmd = [
        "py", "-3", "AI_Tools/content_threads_post.py",
        "--text", f"{args.title}\n\n{args.description}"
    ]
    if video_path:
        threads_cmd.extend(["--file", str(video_path)])
    if args.brand:
        threads_cmd.extend(["--brand", args.brand])
    
    threads_status = run_command(threads_cmd)

    print("\n--- Summary ---")
    print(f"YouTube: {'Success' if yt_status == 0 else 'Failed'}")
    print(f"Meta (IG/FB): {'Success' if fb_ig_status == 0 else 'Failed'}")
    print(f"Threads: {'Success' if threads_status == 0 else 'Failed'}")
    print("\nNote: TikTok still requires manual posting or separate automation.")

if __name__ == "__main__":
    main()
