import requests
import re
import sys
import os

url = "https://www.instagram.com/p/DG_X_9_v_9_/" # Official @instagram carousel
# Try snapdownloader's instagram-downloader
api_url = f"https://snapdownloader.com/tools/instagram-downloader/download?url={url}"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
})

try:
    print(f"Fetching: {api_url}")
    resp = session.get(api_url)
    resp.raise_for_status()
    print("Response received.")
    
    # Write to a file for inspection
    with open("response_debug.html", "w", encoding="utf-8") as f:
        f.write(resp.text)
    
    # The odownloader.js might be fetching data via another API call.
    # Let's look for any JSON or suspicious URLs in the HTML.
    
    # Try a broader regex for any media-looking URL
    # Snapdownloader usually returns links like https://dl.snapcdn.app/...
    matches = re.findall(r'https?://[^\s"\']+\.(mp4|jpg|jpeg|png|webp)[^\s"\'\?]*', resp.text, re.IGNORECASE)
    print(f"Found {len(matches)} potential media extensions.")
    
    full_matches = re.findall(r'(https?://[^\s"\']+\.(?:mp4|jpg|jpeg|png|webp)[^\s"\'\?]*\b)', resp.text, re.IGNORECASE)
    print(f"Found {len(full_matches)} full matches.")
    for m in full_matches:
        if "snapdownloader.com" not in m:
            print(f"  {m}")

except Exception as e:
    print(f"Error: {e}")
