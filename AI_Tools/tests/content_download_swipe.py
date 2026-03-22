#!/usr/bin/env python3
import os
import sys
import re
import pathlib
import subprocess
import argparse

# --- Constants ---
ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_FILE = ROOT / r"VLT_Content\__VLT_OBSVAULT\PDCT_JO_Consult\Social Swipe\Download Que.md"
DEFAULT_OUT = ROOT / r"VLT_Content\__VLT_OBSVAULT\PDCT_JO_Consult\Social Swipe\Social Media Format\Reels"

def download_reel(url, output_dir):
    """Download a single reel using yt-dlp."""
    # Clean URL: remove any markdown wrapping
    clean_url = url.split(')')[0].split(']')[0].split('"')[0].split("'")[0].split('>')[0].split('<')[0]
    if '(' in clean_url and clean_url.startswith('['): # markdown link [text](url)
        m = re.search(r'\((https?://[^)]+)\)', url)
        if m:
            clean_url = m.group(1)
            
    print(f"  Attempting: {clean_url}")
    cmd = ["py", "-3", "-m", "yt_dlp", clean_url, "-o", f"{output_dir}/%(id)s.%(ext)s", "--no-playlist", "--quiet"]
    try:
        subprocess.run(cmd, check=True)
        return True
    except Exception as e:
        print(f"  Error downloading {clean_url}: {e}")
        return False

def process_swipe_queue(file_path, output_dir):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    content = pathlib.Path(file_path).read_text(encoding='utf-8')
    lines = content.splitlines()
    new_lines = []
    
    download_count = 0
    
    for line in lines:
        # Check if it's a table row with content and not a header/separator
        if '|' in line and not line.strip().startswith('| ---'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 3: # | col1 | col2 | (split results in ['', col1, col2, ''])
                col1 = parts[1]
                col2 = parts[2]
                
                # Only process if col2 is not 'DONE'
                if col2.upper() != 'DONE' and col1:
                    # Find all URLs in col1 (could be multiple <br> separated)
                    urls = re.findall(r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*)', col1)
                    
                    if urls:
                        success_all = True
                        for url in urls:
                            if any(domain in url.lower() for domain in ['instagram.com/reel/', 'facebook.com', 'tiktok.com']):
                                if download_reel(url, output_dir):
                                    download_count += 1
                                else:
                                    success_all = False
                        
                        if success_all:
                            # Mark as DONE
                            parts[2] = 'DONE'
                            line = '| ' + ' | '.join(parts[1:-1]) + ' |'
                
        new_lines.append(line)
    
    # Write back updated content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
    
    print(f"\nFinished. Total reels downloaded/processed: {download_count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download social reels from Swipe Queue and mark as DONE")
    parser.add_argument("--input", default=str(DEFAULT_FILE), help="Path to Download Que.md")
    parser.add_argument("--output", default=str(DEFAULT_OUT), help="Output directory")
    
    args = parser.parse_args()
    process_swipe_queue(args.input, args.output)
