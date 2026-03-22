#!/usr/bin/env python3
"""
content_fb_ig_post.py — Post media to Facebook Page and/or Instagram Business Account

Usage:
  Single file:   py -3 AI_Tools/content_fb_ig_post.py --file "path.jpg" --caption "text" --platform ig
  Folder:        py -3 AI_Tools/content_fb_ig_post.py --folder "path/" --platform both
  Manifest CSV:  py -3 AI_Tools/content_fb_ig_post.py --manifest "path/manifest.csv"

Required .env keys:
  META_PAGE_ACCESS_TOKEN  — Long-lived Page Access Token (60-day)
  META_IG_USER_ID         — Instagram Business Account ID
  META_FB_PAGE_ID         — Facebook Page ID
  IMGBB_API_KEY           — (Optional) imgbb.com free API key for image hosting
                            Get one free at: https://api.imgbb.com/
                            If not set, falls back to 0x0.st temp hosting (testing only)

Notes:
  - IG requires media to be at a public URL. This script auto-uploads to imgbb or 0x0.st.
  - FB images/videos are uploaded directly (no hosting needed).
  - IG Reels: MP4, H.264, 3-90 seconds, max 1GB
  - IG Carousels: not yet supported (use manifest with multiple images manually)
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

# Global defaults from .env
PAGE_ACCESS_TOKEN = os.getenv("META_PAGE_ACCESS_TOKEN")
IG_USER_ID = os.getenv("META_IG_USER_ID")
FB_PAGE_ID = os.getenv("META_FB_PAGE_ID")
IMGBB_API_KEY = os.getenv("IMGBB_API_KEY", "")

GRAPH_URL = "https://graph.facebook.com/v19.0"
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
VIDEO_EXTS = {".mp4", ".mov", ".avi"}

def load_brand_config(brand_key: str):
    """Load brand configuration from brands.json."""
    brand_file = Path(__file__).parent / "brands.json"
    if not brand_file.exists():
        print(f"[warn] brands.json not found at {brand_file}")
        return None
    
    with open(brand_file, "r") as f:
        config = json.load(f)
    
    return config.get(brand_key)


# ── Media Hosting (required for IG) ──────────────────────────────────────────

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
    """Upload file to temp host (catbox.moe or 0x0.st) — for testing only."""
    print("  [warn] Using temp host — set IMGBB_API_KEY for permanent hosting")
    
    # Try Catbox.moe first (good for larger files)
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

    # Fallback to 0x0.st
    with open(file_path, "rb") as f:
        resp = requests.post(
            "https://0x0.st",
            files={"file": f},
            timeout=120,
            verify=False
        )
    resp.raise_for_status()
    url = resp.text.strip()
    if not url.startswith("http"):
        raise RuntimeError(f"0x0.st returned unexpected response: {url}")
    return url


def get_public_url(file_path: str) -> str:
    """Get a public URL for the file (for IG upload)."""
    if IMGBB_API_KEY:
        return upload_to_imgbb(file_path)
    return upload_to_temp_host(file_path)


# ── Facebook Publishing ───────────────────────────────────────────────────────

def post_fb_image(file_path: str, caption: str) -> dict:
    """Post image directly to Facebook Page (multipart upload)."""
    with open(file_path, "rb") as f:
        resp = requests.post(
            f"{GRAPH_URL}/{FB_PAGE_ID}/photos",
            data={"message": caption, "access_token": PAGE_ACCESS_TOKEN},
            files={"source": f},
            timeout=60,
        )
    resp.raise_for_status()
    result = resp.json()
    return {"platform": "fb", "type": "image", "post_id": result.get("id"), "success": True}


def post_fb_video(file_path: str, caption: str) -> dict:
    """Post video directly to Facebook Page (multipart upload)."""
    with open(file_path, "rb") as f:
        resp = requests.post(
            f"{GRAPH_URL}/{FB_PAGE_ID}/videos",
            data={"description": caption, "access_token": PAGE_ACCESS_TOKEN},
            files={"source": f},
            timeout=180,
        )
    resp.raise_for_status()
    result = resp.json()
    return {"platform": "fb", "type": "video", "post_id": result.get("id"), "success": True}


# ── Instagram Publishing ──────────────────────────────────────────────────────

def post_ig_image(file_path: str, caption: str) -> dict:
    """Post single image to Instagram Business Account."""
    print("  Uploading image to public host...")
    public_url = get_public_url(file_path)
    print(f"  Hosted at: {public_url}")

    # Step 1: Create media container
    resp = requests.post(
        f"{GRAPH_URL}/{IG_USER_ID}/media",
        data={
            "image_url": public_url,
            "caption": caption,
            "access_token": PAGE_ACCESS_TOKEN,
        },
        timeout=30,
    )
    resp.raise_for_status()
    creation_id = resp.json()["id"]

    # Step 2: Publish
    time.sleep(3)
    resp = requests.post(
        f"{GRAPH_URL}/{IG_USER_ID}/media_publish",
        data={"creation_id": creation_id, "access_token": PAGE_ACCESS_TOKEN},
        timeout=30,
    )
    resp.raise_for_status()
    return {"platform": "ig", "type": "image", "media_id": resp.json().get("id"), "success": True}


def post_ig_reel(file_path: str, caption: str) -> dict:
    """Post video as Reel to Instagram Business Account."""
    print("  Uploading video to public host...")
    public_url = get_public_url(file_path)
    print(f"  Hosted at: {public_url}")

    # Step 1: Create media container
    resp = requests.post(
        f"{GRAPH_URL}/{IG_USER_ID}/media",
        data={
            "media_type": "REELS",
            "video_url": public_url,
            "caption": caption,
            "share_to_feed": "true",
            "access_token": PAGE_ACCESS_TOKEN,
        },
        timeout=30,
    )
    resp.raise_for_status()
    creation_id = resp.json()["id"]

    # Step 2: Poll for processing (max ~100 seconds)
    print("  Waiting for video processing", end="", flush=True)
    for _ in range(20):
        time.sleep(5)
        print(".", end="", flush=True)
        check = requests.get(
            f"{GRAPH_URL}/{creation_id}",
            params={"fields": "status_code", "access_token": PAGE_ACCESS_TOKEN},
            timeout=15,
        )
        check.raise_for_status()
        status = check.json().get("status_code")
        if status == "FINISHED":
            print(" done")
            break
        if status == "ERROR":
            print()
            raise RuntimeError(f"IG video processing error: {check.json()}")
    else:
        print()
        raise TimeoutError("IG video processing timed out after 100s")

    # Step 3: Publish
    resp = requests.post(
        f"{GRAPH_URL}/{IG_USER_ID}/media_publish",
        data={"creation_id": creation_id, "access_token": PAGE_ACCESS_TOKEN},
        timeout=30,
    )
    resp.raise_for_status()
    return {"platform": "ig", "type": "reel", "media_id": resp.json().get("id"), "success": True}


# ── Core Post Dispatcher ──────────────────────────────────────────────────────

def post_file(file_path: str, caption: str, platform: str) -> list[dict]:
    """Post a single file to the specified platform(s). Returns list of results."""
    ext = Path(file_path).suffix.lower()
    is_image = ext in IMAGE_EXTS
    is_video = ext in VIDEO_EXTS

    if not (is_image or is_video):
        print(f"  Skipping — unsupported format ({ext})")
        return []

    platforms = ["ig", "fb"] if platform == "both" else [platform]
    results = []

    for p in platforms:
        print(f"  → Posting to {p.upper()}...")
        try:
            if p == "fb":
                result = post_fb_image(file_path, caption) if is_image else post_fb_video(file_path, caption)
            else:
                result = post_ig_image(file_path, caption) if is_image else post_ig_reel(file_path, caption)
            pid = result.get("post_id") or result.get("media_id")
            print(f"  ✓ {p.upper()} posted — ID: {pid}")
            results.append(result)
        except requests.HTTPError as e:
            body = e.response.text if e.response else str(e)
            print(f"  ✗ {p.upper()} HTTP error: {body}")
            results.append({"platform": p, "success": False, "error": body})
        except Exception as e:
            print(f"  ✗ {p.upper()} failed: {e}")
            results.append({"platform": p, "success": False, "error": str(e)})

    return results


# ── Input Modes ───────────────────────────────────────────────────────────────

def post_from_folder(folder: str, platform: str, caption: str = "") -> None:
    """Post all media files from a folder. Prompts for caption per file if not provided."""
    folder_path = Path(folder)
    files = sorted(
        f for f in folder_path.iterdir()
        if f.is_file() and f.suffix.lower() in IMAGE_EXTS | VIDEO_EXTS
    )

    if not files:
        print(f"No media files found in {folder}")
        return

    print(f"Found {len(files)} file(s)\n")
    for f in files:
        file_caption = caption or input(f"Caption for '{f.name}' (Enter to skip): ").strip()
        print(f"\nPosting: {f.name}")
        post_file(str(f), file_caption, platform)


def post_from_manifest(manifest_path: str) -> None:
    """
    Post from CSV manifest.
    Required columns: file_path, caption, platform
    Optional:         post_type (reel|image|video — auto-detected if omitted)
    """
    import csv

    with open(manifest_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [r for r in reader if r.get("file_path", "").strip()]

    if not rows:
        print("Manifest is empty or has no file_path column.")
        return

    print(f"Manifest: {len(rows)} row(s)\n")
    for row in rows:
        file_path = row["file_path"].strip()
        caption = row.get("caption", "").strip()
        platform = row.get("platform", "ig").strip().lower()
        name = Path(file_path).name

        if not Path(file_path).exists():
            print(f"  ✗ File not found: {file_path}")
            continue

        print(f"Posting: {name} → {platform.upper()}")
        results = post_file(file_path, caption, platform)
        print(json.dumps(results, indent=2))


# ── Entry Point ───────────────────────────────────────────────────────────────

def main():
    global PAGE_ACCESS_TOKEN, IG_USER_ID, FB_PAGE_ID
    
    parser = argparse.ArgumentParser(
        description="Post media to Facebook Page and/or Instagram via Meta Graph API"
    )
    parser.add_argument("--file", help="Path to a single media file")
    parser.add_argument("--folder", help="Folder containing media files")
    parser.add_argument("--manifest", help="Path to CSV manifest (columns: file_path, caption, platform)")
    parser.add_argument("--caption", default="", help="Caption text (used with --file or --folder)")
    parser.add_argument(
        "--platform", default="ig", choices=["ig", "fb", "both"],
        help="Target platform (default: ig)"
    )
    parser.add_argument("--brand", help="Brand key from brands.json (e.g., hts, realestate)")
    args = parser.parse_args()

    # Apply brand config if provided
    if args.brand:
        config = load_brand_config(args.brand)
        if config:
            print(f"Using config for brand: {config.get('name', args.brand)}")
            if config.get("page_id"):
                FB_PAGE_ID = config["page_id"]
            if config.get("ig_id"):
                IG_USER_ID = config["ig_id"]
            if config.get("access_token"):
                PAGE_ACCESS_TOKEN = config["access_token"]
        else:
            print(f"[error] Brand '{args.brand}' not found in brands.json")
            sys.exit(1)

    # Validate credentials
    missing = []
    if not PAGE_ACCESS_TOKEN:
        missing.append("META_PAGE_ACCESS_TOKEN")
    if not IG_USER_ID and args.platform in ("ig", "both"):
        missing.append("META_IG_USER_ID")
    if not FB_PAGE_ID and args.platform in ("fb", "both"):
        missing.append("META_FB_PAGE_ID")
    if missing:
        print(f"\n[error] Missing .env keys: {', '.join(missing)}")
        print("Add these to your .env file and retry.\n")
        sys.exit(1)

    if args.file:
        if not Path(args.file).exists():
            print(f"[error] File not found: {args.file}")
            sys.exit(1)
        caption = args.caption or input("Caption: ").strip()
        print(f"\nPosting: {Path(args.file).name}")
        results = post_file(args.file, caption, args.platform)
        print(json.dumps(results, indent=2))

    elif args.folder:
        if not Path(args.folder).exists():
            print(f"[error] Folder not found: {args.folder}")
            sys.exit(1)
        post_from_folder(args.folder, args.platform, args.caption)

    elif args.manifest:
        if not Path(args.manifest).exists():
            print(f"[error] Manifest not found: {args.manifest}")
            sys.exit(1)
        post_from_manifest(args.manifest)

    else:
        print("Specify --file, --folder, or --manifest")
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
