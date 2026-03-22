import requests
import re
import sys
import os

url = "https://www.instagram.com/p/DG_X_9_v_9_/" # Official @instagram carousel
api_url = "https://igdown.org/api/v1/process"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Referer": "https://igdown.org/",
    "X-Requested-With": "XMLHttpRequest"
})

try:
    print(f"Testing IGDown for: {url}")
    data = {
        "url": url
    }
    resp = session.post(api_url, data=data)
    resp.raise_for_status()
    print("Response received.")
    
    json_data = resp.json()
    # IGDown usually returns JSON with media list
    media = json_data.get("media", [])
    print(f"Found {len(media)} media items.")
    
    for item in media:
        print(f"  {item.get('url')}")

except Exception as e:
    print(f"Error: {e}")
