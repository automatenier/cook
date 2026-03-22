import requests
import re
import sys
import os

url = "https://www.instagram.com/p/DG_X_9_v_9_/" # Official @instagram carousel
# Try SaveFrom.net
api_url = "https://savefrom.net/api/v1/save"
# This might not work.

# How about using a public proxy or another scraper?
# Let's try https://snapsave.app/api/ajaxSearch
api_url = "https://snapsave.app/api/ajaxSearch"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Referer": "https://snapsave.app/",
    "X-Requested-With": "XMLHttpRequest"
})

try:
    print(f"Testing SnapSave for: {url}")
    data = {
        "url": url
    }
    resp = session.post(api_url, data=data)
    resp.raise_for_status()
    print("Response received.")
    
    # SnapSave returns HTML in a JSON 'data' field
    html = resp.json().get("data", "")
    
    # Look for download links
    links = re.findall(r'href="(https?://[^"]+)"', html)
    print(f"Found {len(links)} links.")
    
    media_links = []
    for link in links:
        if "instagram" in link or "cdninstagram" in link or "snapsave" in link:
            if link not in media_links:
                media_links.append(link)
                
    print(f"Found {len(media_links)} potential media links.")
    for l in media_links:
        print(f"  {l}")

except Exception as e:
    print(f"Error: {e}")
