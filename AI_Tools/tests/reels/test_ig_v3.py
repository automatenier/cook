import requests
import re
import sys
import os

url = "https://www.instagram.com/p/DG_X_9_v_9_/" # Official @instagram carousel
# Try snapdownloader's instagram-downloader
api_url = f"https://snapdownloader.com/tools/instagram-downloader/download?url={url}"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
})

try:
    print(f"Fetching: {api_url}")
    resp = session.get(api_url)
    resp.raise_for_status()
    print("Response received.")
    
    # Look for ANY media-looking URL that is NOT snapdownloader.com
    # Snapdownloader usually returns links from their CDN or direct IG links.
    # Let's look for common media patterns.
    
    # Look for anything that looks like a CDN link or has an extension
    all_links = re.findall(r'href="(https?://[^"]+)"', resp.text)
    print(f"Found {len(all_links)} total links.")
    
    media_links = []
    for link in all_links:
        if "snapdownloader.com" in link:
            continue
        # Look for links that contain "cdn" or "fbcdn" or "igcdn" or have media extensions
        if any(x in link for x in ["cdn", "fbcdn", "igcdn", ".mp4", ".jpg", ".png", "dl.snapcdn.app"]):
            if link not in media_links:
                media_links.append(link)
                
    print(f"Found {len(media_links)} potential media links.")
    for l in media_links:
        print(f"  {l}")

except Exception as e:
    print(f"Error: {e}")
