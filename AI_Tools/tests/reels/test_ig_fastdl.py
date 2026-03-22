import requests
import re
import sys
import os
import json

url = "https://www.instagram.com/p/DG_X_9_v_9_/" # Official @instagram carousel
api_url = "https://fastdl.app/api/v1/process"

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Referer": "https://fastdl.app/",
    "Content-Type": "application/json",
    "Origin": "https://fastdl.app"
})

try:
    print(f"Testing FastDL for: {url}")
    payload = {
        "url": url
    }
    resp = session.post(api_url, json=payload)
    resp.raise_for_status()
    print("Response received.")
    
    data = resp.json()
    # FastDL usually returns a list of media in a 'media' or similar field
    # Let's inspect the JSON keys
    print(f"Keys: {list(data.keys())}")
    
    if 'data' in data:
        data = data['data']
        print(f"Sub-keys: {list(data.keys())}")
        
    media = data.get('medias', []) or data.get('media', [])
    print(f"Found {len(media)} media items.")
    
    for i, item in enumerate(media):
        print(f"Item {i+1}: {item.get('url')}")

except Exception as e:
    print(f"Error: {e}")
    if 'resp' in locals():
        print(f"Status Code: {resp.status_code}")
        print(f"Response: {resp.text[:500]}")
