import requests
import re
import sys
import os

url = "https://www.instagram.com/p/DG_X_9_v_9_/" # Official @instagram carousel
api_url = "https://saveig.app/api/ajaxSearch"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Referer": "https://saveig.app/",
    "X-Requested-With": "XMLHttpRequest"
})

try:
    print(f"Testing SaveIG for: {url}")
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
    with open("saveig_debug.html", "w", encoding="utf-8") as f:
        f.write(html)
        
    # Look for download links
    # SaveIG uses <div class="download-items"> ... <a href="...">Download</a>
    links = re.findall(r'href="(https?://[^"]+)"', html)
    print(f"Found {len(links)} links.")
    
    unique_links = []
    for link in links:
        if "instagram" in link or "cdninstagram" in link or "saveig" in link:
            if link not in unique_links:
                unique_links.append(link)
                
    print(f"Filtered {len(unique_links)} potential media links.")
    for l in unique_links:
        print(f"  {l}")

except Exception as e:
    print(f"Error: {e}")
