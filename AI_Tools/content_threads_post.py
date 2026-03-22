#!/usr/bin/env python3
"""
content_threads_post.py — Post media or text to Threads via Threads API

Usage:
  Text only:     py -3 AI_Tools/content_threads_post.py --text "Hello Threads!"
  Image:         py -3 AI_Tools/content_threads_post.py --file "path.jpg" --text "Caption"
  Video/Reel:    py -3 AI_Tools/content_threads_post.py --file "video.mp4" --text "Caption"

Required .env keys:
  THREADS_ACCESS_TOKEN  — User Access Token with threads_content_publish permission
  THREADS_USER_ID       — Threads User ID
  IMGBB_API_KEY         — (Optional) for image hosting
"""

import os
import sys
import time
import argparse
import requests
import json
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

THREADS_ACCESS_TOKEN = os.getenv("THREADS_ACCESS_TOKEN")
THREADS_USER_ID = os.getenv("THREADS_USER_ID")
IMGBB_API_KEY = os.getenv("IMGBB_API_KEY", "")

THREADS_API_URL = "https://graph.threads.net/v1.0"
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
VIDEO_EXTS = {".mp4", ".mov", ".avi"}

# ── Media Hosting (required for Threads) ─────────────────────────────────────

def upload_to_imgbb(file_path: str) -> str:
    """Upload image to imgbb.com and return permanent public URL."""
    with open(file_path, "rb") as f:
        resp = requests.post(
            "https://api.imgbb.com/1/upload",
            params={"key": IMGBB_API_KEY},
            files={"image": f},
            timeout=30,
        )
    resp.raise_for_status()
    return resp.json()["data"]["url"]

def upload_to_temp_host(file_path: str) -> str:
    """Upload file to temp host (catbox.moe or 0x0.st)."""
    try:
        with open(file_path, "rb") as f:
            resp = requests.post(
                "https://catbox.moe/user/api.php",
                data={"reqtype": "fileupload"},
                files={"fileToUpload": f},
                timeout=180
            )
        resp.raise_for_status()
        url = resp.text.strip()
        if url.startswith("http"):
            return url
    except Exception as e:
        print(f"  [warn] Catbox failed: {e}")

    with open(file_path, "rb") as f:
        resp = requests.post(
            "https://0x0.st",
            files={"file": f},
            timeout=120,
            verify=False
        )
    resp.raise_for_status()
    url = resp.text.strip()
    return url

def get_public_url(file_path: str) -> str:
    """Get a public URL for the file."""
    if IMGBB_API_KEY and Path(file_path).suffix.lower() in IMAGE_EXTS:
        return upload_to_imgbb(file_path)
    return upload_to_temp_host(file_path)

def load_brand_config(brand_key: str):
    """Load brand configuration from brands.json."""
    brand_file = Path(__file__).parent / "brands.json"
    if not brand_file.exists():
        print(f"[warn] brands.json not found at {brand_file}")
        return None
    
    with open(brand_file, "r") as f:
        config = json.load(f)
    
    return config.get(brand_key)

# ── Threads Publishing ────────────────────────────────────────────────────────

def post_to_threads(text: str, file_path: str = None) -> dict:
    """Post text and optional media to Threads."""
    global THREADS_ACCESS_TOKEN, THREADS_USER_ID
    
    payload = {
        "text": text,
        "access_token": THREADS_ACCESS_TOKEN
    }

    if file_path:
        ext = Path(file_path).suffix.lower()
        public_url = get_public_url(file_path)
        print(f"  Media hosted at: {public_url}")
        
        if ext in IMAGE_EXTS:
            payload["media_type"] = "IMAGE"
            payload["image_url"] = public_url
        elif ext in VIDEO_EXTS:
            payload["media_type"] = "VIDEO"
            payload["video_url"] = public_url
        else:
            print(f"  Unsupported format {ext}, posting as text-only.")
    else:
        payload["media_type"] = "TEXT"

    # Step 1: Create media container
    print(f"  Creating Threads container ({payload['media_type']})...")
    resp = requests.post(
        f"{THREADS_API_URL}/{THREADS_USER_ID}/threads",
        data=payload,
        timeout=30,
    )
    if resp.status_code != 200:
        print(f"  Error creating container: {resp.text}")
        resp.raise_for_status()
    
    creation_id = resp.json()["id"]

    # Step 2: Wait if it's a video
    if payload.get("media_type") == "VIDEO":
        print("  Waiting for video processing", end="", flush=True)
        for _ in range(20):
            time.sleep(5)
            print(".", end="", flush=True)
            check = requests.get(
                f"{THREADS_API_URL}/{creation_id}",
                params={"fields": "status_code", "access_token": THREADS_ACCESS_TOKEN},
                timeout=15,
            )
            status = check.json().get("status_code")
            if status == "FINISHED":
                print(" done")
                break
            if status == "ERROR":
                print()
                raise RuntimeError(f"Threads video processing error: {check.json()}")
        else:
            print()
            raise TimeoutError("Threads video processing timed out")
    else:
        time.sleep(2) # Short buffer for images/text

    # Step 3: Publish
    print("  Publishing to Threads...")
    resp = requests.post(
        f"{THREADS_API_URL}/{THREADS_USER_ID}/threads_publish",
        data={"creation_id": creation_id, "access_token": THREADS_ACCESS_TOKEN},
        timeout=30,
    )
    if resp.status_code != 200:
        print(f"  Error publishing: {resp.text}")
        resp.raise_for_status()
        
    post_id = resp.json().get("id")
    return {"platform": "threads", "post_id": post_id, "success": True}

def main():
    global THREADS_ACCESS_TOKEN, THREADS_USER_ID
    
    parser = argparse.ArgumentParser(description="Post to Threads")
    parser.add_argument("--text", required=True, help="Caption or text content")
    parser.add_argument("--file", help="Path to image or video file")
    parser.add_argument("--brand", help="Brand key from brands.json (e.g., hts, realestate)")
    args = parser.parse_args()

    # Apply brand config if provided
    if args.brand:
        config = load_brand_config(args.brand)
        if config:
            print(f"Using config for brand: {config.get('name', args.brand)}")
            if config.get("threads_id"):
                THREADS_USER_ID = config["threads_id"]
            if config.get("threads_access_token"):
                THREADS_ACCESS_TOKEN = config["threads_access_token"]
        else:
            print(f"[error] Brand '{args.brand}' not found in brands.json")
            sys.exit(1)

    if not THREADS_ACCESS_TOKEN or not THREADS_USER_ID:
        print("[error] Missing THREADS_ACCESS_TOKEN or THREADS_USER_ID in .env")
        sys.exit(1)

    try:
        result = post_to_threads(args.text, args.file)
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"[error] Failed to post to Threads: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
