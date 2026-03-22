import requests
import os

urls = [
    "https://instagram.fyka1-1.fna.fbcdn.net/v/t51.82787-15/654568361_18078397514562439_7661399082845513194_n.jpg",
    "https://instagram.fyka1-1.fna.fbcdn.net/v/t51.82787-15/653870982_18078397523562439_3711512115871945013_n.jpg",
    "https://instagram.fyka1-1.fna.fbcdn.net/v/t51.82787-15/652767453_18078397532562439_8230033406405480432_n.jpg"
]

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Referer": "https://www.instagram.com/"
})

out_dir = r"VLT_Content\__VLT_OBSVAULT\01_HMN_INPUTS\Reels"
os.makedirs(out_dir, exist_ok=True)

for i, url in enumerate(urls):
    filename = f"slide{i+1}.jpg"
    filepath = os.path.join(out_dir, filename)
    print(f"Downloading {filename}...")
    resp = session.get(url)
    if resp.status_code == 200:
        with open(filepath, 'wb') as f:
            f.write(resp.content)
        print(f"Saved to {filepath} ({len(resp.content)} bytes)")
    else:
        print(f"Failed to download {filename}: {resp.status_code}")
