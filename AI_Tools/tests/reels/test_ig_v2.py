import requests
import re
import sys
import os

url = "https://www.instagram.com/p/DG_X_9_v_9_/" # Official @instagram carousel
api_url = "https://snapinsta.app/api/ajaxSearch"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "https://snapinsta.app/",
    "X-Requested-With": "XMLHttpRequest"
})

try:
    print(f"Testing SnapInsta for: {url}")
    data = {
        "q": url,
        "t": "media",
        "lang": "en"
    }
    resp = session.post(api_url, data=data)
    resp.raise_for_status()
    print("Response received.")
    
    # The response is usually HTML inside a JSON or just HTML
    html = resp.text
    if '"data"' in html:
        try:
            html = resp.json().get("data", "")
        except:
            pass
            
    # Look for download links
    # SnapInsta uses <a href="...">Download</a>
    links = re.findall(r'href="(https?://[^"]+)"', html)
    print(f"Found {len(links)} links.")
    
    unique_links = []
    for link in links:
        if "instagram" in link or "cdninstagram" in link or "snapinsta" in link:
            if link not in unique_links:
                unique_links.append(link)
                
    print(f"Filtered {len(unique_links)} potential media links.")
    for l in unique_links:
        print(f"  {l}")

except Exception as e:
    print(f"Error: {e}")
