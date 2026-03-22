import requests
import re
import sys
import os
import json

url = "https://www.instagram.com/p/DG_X_9_v_9_/" # Official @instagram carousel
api_url = "https://igdownloader.app/api/ajaxSearch"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Referer": "https://igdownloader.app/",
    "X-Requested-With": "XMLHttpRequest"
})

try:
    print(f"Testing IGDownloader.app for: {url}")
    data = {
        "q": url,
        "t": "media",
        "lang": "en"
    }
    resp = session.post(api_url, data=data)
    resp.raise_for_status()
    print("Response received.")
    
    json_data = resp.json()
    html = json_data.get("data", "")
    
    # Write to a file for inspection
    with open("igdownloader_debug.html", "w", encoding="utf-8") as f:
        f.write(html)
        
    # Look for download links
    links = re.findall(r'href="(https?://[^"]+)"', html)
    print(f"Found {len(links)} links.")
    
    media_links = []
    for link in links:
        if "instagram" in link or "cdninstagram" in link:
            if link not in media_links:
                media_links.append(link)
                
    print(f"Found {len(media_links)} potential media links.")
    for l in media_links:
        print(f"  {l}")

except Exception as e:
    print(f"Error: {e}")
