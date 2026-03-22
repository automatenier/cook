#!/usr/bin/env python3
import os
import sys
import re
import json
import requests
import argparse
import pathlib
import subprocess

# --- Constants ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_OUT = ROOT / r"VLT_Content\__VLT_OBSVAULT\01_HMN_INPUTS\Reels"

class ReelDownloader:
    def __init__(self, output_dir=None):
        self.output_dir = output_dir or DEFAULT_OUT
        os.makedirs(self.output_dir, exist_ok=True)
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        })

    def download_file(self, url, filename, headers=None):
        """Download file from URL."""
        try:
            print(f"  Downloading: {url}")
            current_headers = self.session.headers.copy()
            if headers:
                current_headers.update(headers)
            if "instagram.com" in url or "cdninstagram.com" in url:
                current_headers["Referer"] = "https://www.instagram.com/"

            resp = self.session.get(url, headers=current_headers, stream=True, timeout=30)
            resp.raise_for_status()
            
            filepath = os.path.join(self.output_dir, filename)
            with open(filepath, 'wb') as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"  Saved to: {filepath}")
            return True
        except Exception as e:
            print(f"  Error downloading file: {e}")
            return False

    def handle_tiktok(self, url):
        """TikTok download using yt-dlp as primary, scraper as fallback."""
        print(f"Processing TikTok: {url}")
        
        # Try yt-dlp first
        print("  Trying yt-dlp...")
        output_tmpl = os.path.join(self.output_dir, "tiktok_%(uploader)s_%(id)s.%(ext)s")
        cmd = ["py", "-3", "-m", "yt_dlp", url, "-o", output_tmpl, "--no-playlist", "--quiet"]
        try:
            subprocess.run(cmd, check=True)
            print("  ✓ Downloaded via yt-dlp")
            return True
        except:
            print("  ✗ yt-dlp failed (likely IP block)")

        # Fallback to scraper (original logic)
        try:
            resp = self.session.get(url)
            resp.raise_for_status()
            html = resp.text
            regex = r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">([\s\S]*?)</script>'
            match = re.search(regex, html)
            if match:
                data = json.loads(match.group(1))
                scope = data.get("__DEFAULT_SCOPE__", {})
                video_detail = scope.get("webapp.video-detail", {})
                item_info = video_detail.get("itemInfo", {})
                item_struct = item_info.get("itemStruct", {})
                
                video_url = item_struct.get("video", {}).get("playAddr") or item_struct.get("video", {}).get("downloadAddr")
                if video_url:
                    author = item_struct.get("author", {}).get("uniqueId", "unknown")
                    video_id = item_struct.get("id", "tiktok_video")
                    filename = f"tiktok_{author}_{video_id}.mp4"
                    cookies = "; ".join([f"{k}={v}" for k, v in self.session.cookies.get_dict().items()])
                    headers = {"Referer": "https://www.tiktok.com/", "Cookie": cookies}
                    return self.download_file(video_url, filename, headers=headers)
            
            print("  Error: TikTok scraper failed.")
            return False
        except Exception as e:
            print(f"  TikTok Error: {e}")
            return False

    def handle_facebook(self, url):
        """Facebook download logic."""
        print(f"Processing Facebook: {url}")
        # Try yt-dlp first
        print("  Trying yt-dlp...")
        output_tmpl = os.path.join(self.output_dir, "facebook_%(id)s.%(ext)s")
        cmd = ["py", "-3", "-m", "yt_dlp", url, "-o", output_tmpl, "--no-playlist", "--quiet"]
        try:
            subprocess.run(cmd, check=True)
            print("  ✓ Downloaded via yt-dlp")
            return True
        except:
            print("  ✗ yt-dlp failed")

        try:
            api_url = "https://fbdownloader.to/api/ajaxSearch"
            data = {"q": url}
            resp = self.session.post(api_url, data=data)
            resp.raise_for_status()
            match = re.search(r'https://dl\.snapcdn\.app/download\?token=[^"]+', resp.text)
            if match:
                download_url = match.group(0)
                filename = f"facebook_video_{int(os.path.getmtime(self.output_dir))}.mp4"
                return self.download_file(download_url, filename)
            print("  Error: Facebook download link not found.")
            return False
        except Exception as e:
            print(f"  Facebook Error: {e}")
            return False

    def handle_instagram(self, url):
        """Instagram download logic supporting Carousels."""
        print(f"Processing Instagram: {url}")
        
        # Try yt-dlp first
        print("  Trying yt-dlp...")
        output_tmpl = os.path.join(self.output_dir, "instagram_%(uploader)s_%(id)s_%(playlist_index)s.%(ext)s")
        cmd = ["py", "-3", "-m", "yt_dlp", url, "-o", output_tmpl, "--quiet"]
        try:
            subprocess.run(cmd, check=True)
            print("  ✓ Downloaded via yt-dlp (supports carousels)")
            return True
        except:
            print("  ✗ yt-dlp failed (likely needs cookies)")

        # Fallback to snapdownloader (current logic)
        try:
            api_url = f"https://snapdownloader.com/tools/instagram-downloader/download?url={url}"
            resp = self.session.get(api_url)
            resp.raise_for_status()
            
            # Find all MP4 and JPG links (SnapDownloader returns them in the response)
            # Carousels often have multiple media items
            matches = re.findall(r'(https?://[^\s"\']+\.(mp4|jpg|jpeg|png|webp)[^\s"\'\?]*\b)', resp.text, re.IGNORECASE)
            
            if not matches:
                print("  Error: No media links found for Instagram.")
                return False
            
            success = False
            unique_links = []
            for m in matches:
                link = m[0].replace("&amp;", "&")
                if "snapdownloader.com" in link: continue # Skip UI assets
                if link not in unique_links:
                    unique_links.append(link)
            
            print(f"  Found {len(unique_links)} media items in carousel/post.")
            for i, link in enumerate(unique_links):
                ext = "mp4" if ".mp4" in link.lower() else "jpg"
                filename = f"instagram_media_{int(os.path.getmtime(self.output_dir))}_{i}.{ext}"
                if self.download_file(link, filename):
                    success = True
            
            return success
        except Exception as e:
            print(f"  Instagram Error: {e}")
            return False

    def process(self, url):
        if "tiktok.com" in url:
            return self.handle_tiktok(url)
        elif "facebook.com" in url or "fb.watch" in url:
            return self.handle_facebook(url)
        elif "instagram.com" in url:
            return self.handle_instagram(url)
        else:
            print(f"Unsupported URL: {url}")
            return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download Reels/Carousels (v2.1)")
    parser.add_argument("url", help="Social media URL to download")
    parser.add_argument("--output", help="Output directory")
    
    args = parser.parse_args()
    
    downloader = ReelDownloader(args.output)
    success = downloader.process(args.url)
    sys.exit(0 if success else 1)
