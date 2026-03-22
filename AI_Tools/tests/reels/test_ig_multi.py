import requests
import re
import sys
import os

url = "https://www.instagram.com/p/DG_X_9_v_9_/" # Official @instagram carousel
# Try fastdl.app
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
})

try:
    print(f"Fetching FastDL for: {url}")
    # Step 1: Get the page to get the CSRF token if any
    resp = session.get("https://fastdl.app/")
    resp.raise_for_status()
    
    # Step 2: Hit the process endpoint
    api_url = "https://fastdl.app/api/v1/process"
    payload = {"url": url}
    resp = session.post(api_url, json=payload)
    
    if resp.status_code == 200:
        print("Success!")
        data = resp.json()
        print(f"Data: {json.dumps(data, indent=2)[:500]}")
    else:
        print(f"Failed: {resp.status_code}")
        # Try another approach: snapinsta.app
        print("Trying SnapInsta...")
        api_url = "https://snapinsta.app/api/ajaxSearch"
        data = {"q": url, "t": "media", "lang": "en"}
        resp = session.post(api_url, data=data)
        if resp.status_code == 200:
            print("SnapInsta success!")
            # SnapInsta returns HTML in a JSON 'data' field
            html = resp.json().get("data", "")
            links = re.findall(r'href="(https?://[^"]+)"', html)
            print(f"Found {len(links)} links.")
        else:
            print(f"SnapInsta failed: {resp.status_code}")

except Exception as e:
    print(f"Error: {e}")
