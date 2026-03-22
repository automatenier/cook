import requests
import re
import os

url = "https://www.instagram.com/p/DWAdM4rCWo9/"
api_url = f"https://snapdownloader.com/tools/instagram-downloader/download?url={url}"
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
})

resp = session.get(api_url)
print(f"Status: {resp.status_code}")
matches = re.findall(r'(https?://[^\s"\']+\.(mp4|jpg|jpeg|png|webp)[^\s"\'\?]*\b)', resp.text, re.IGNORECASE)

unique_links = []
for m in matches:
    link = m[0].replace("&amp;", "&")
    if "snapdownloader.com" in link: continue # Skip UI assets
    if link not in unique_links:
        unique_links.append(link)

print(f"Found {len(unique_links)} links.")
for i, link in enumerate(unique_links):
    print(f"Link {i}: {link}")
