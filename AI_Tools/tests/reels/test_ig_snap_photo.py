import requests
import re
import sys
import os

url = "https://www.instagram.com/p/DG_X_9_v_9_/" # Official @instagram carousel
# Try snapdownloader's photo-downloader
api_url = f"https://snapdownloader.com/tools/instagram-photo-downloader/download?url={url}"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
})

try:
    print(f"Fetching SnapDownloader Photo: {api_url}")
    resp = session.get(api_url)
    resp.raise_for_status()
    print("Response received.")
    
    # Write to a file for inspection
    with open("snapdownloader_photo_debug.html", "w", encoding="utf-8") as f:
        f.write(resp.text)
        
    # SnapDownloader uses a script 'odownloader.js' which likely does the heavy lifting.
    # Let's see if there's any JSON in the script tags.
    script_data = re.findall(r'<script>.*?(?:var|const|let)\s+data\s*=\s*(\{.*?\});.*?</script>', resp.text, re.DOTALL)
    if script_data:
        print(f"Found {len(script_data)} script data blocks.")
        # print(script_data[0][:500])
    
    # Try looking for dl.snapcdn.app links in the HTML
    matches = re.findall(r'https://dl\.snapcdn\.app/download\?token=[^"]+', resp.text)
    print(f"Found {len(matches)} direct download links.")
    for m in matches:
        print(f"  {m}")

except Exception as e:
    print(f"Error: {e}")
