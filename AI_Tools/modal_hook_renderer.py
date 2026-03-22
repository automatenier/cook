import modal
import os
import textwrap
import subprocess
import re
from pathlib import Path

# 1. Define the Modal App
app = modal.App("hook-ab-renderer")

# 2. Container image with FFmpeg
image = (
    modal.Image.debian_slim()
    .apt_install("ffmpeg")
    .pip_install("pathlib")
)

# 3. Font path in container
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def clean_hook_text(text):
    """Applies user rules: no asterisks, no <br> symbols, no dashes, pure text."""
    # Remove asterisks
    text = text.replace("**", "").replace("*", "")
    # Remove dashes/long dashes
    text = text.replace("--", "").replace("—", "")
    # Convert <br> to newlines
    text = text.replace("<br>", "\n").replace("<br/>", "\n")
    
    # Split by newlines provided by user and wrap each part if it's too long
    lines = text.split("\n")
    processed_lines = []
    for line in lines:
        if line.strip():
            # Safety wrap at 22 chars to prevent cutting, but preserve user breaks
            processed_lines.extend(textwrap.wrap(line.strip(), width=22))
            
    return "\n".join(processed_lines)

@app.function(image=image, timeout=600)
def render_on_modal(video_bytes: bytes, hook_text: str, filename: str) -> bytes:
    """Renders a single hook on a video using FFmpeg in the Modal cloud."""
    input_path = Path("/tmp/input.mp4")
    input_path.write_bytes(video_bytes)
    
    output_path = Path(f"/tmp/{filename}")
    
    # Apply the new cleaning rules
    safe_text = clean_hook_text(hook_text)
    
    # Escape for ffmpeg drawtext
    ffmpeg_text = safe_text.replace("'", "'\\''").replace(":", "\\:")
    
    # FFmpeg command: Centered (x), Upper Third (y), Bold White, Black Border
    # text_align=center ensures multiline blocks are centered line-by-line
    cmd = [
        "ffmpeg", "-y",
        "-i", str(input_path),
        "-vf", f"drawtext=fontfile='{FONT_PATH}':text='{ffmpeg_text}':fontsize=55:fontcolor=white:borderw=4:bordercolor=black:line_spacing=10:x=(w-text_w)/2:y=h*0.15:text_align=center:enable='between(t,0,3)'",
        "-c:v", "libx264", "-crf", "23", "-preset", "veryfast",
        "-c:a", "copy",
        str(output_path)
    ]
    
    print(f"Rendering: {safe_text.replace('\n', ' ')[:30]}...")
    subprocess.run(cmd, check=True)
    
    return output_path.read_bytes()

@app.local_entrypoint()
def main(hooks_file: str):
    hooks_path = Path(hooks_file).resolve()
    if not hooks_path.exists():
        print(f"Error: Hooks file not found: {hooks_path}")
        return

    with open(hooks_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    matches = []
    for line in lines:
        if "|" in line and "ID" not in line and "---" not in line:
            # Split and clean columns
            cols = [c.strip() for c in line.split("|")]
            # Format: | (empty) | ID | Path | Hook | Slug | Status | (empty) |
            if len(cols) >= 5:
                hid = cols[1]
                v_path = cols[2]
                text = cols[3]
                slug = cols[4]
                if v_path and text:
                    matches.append((hid, v_path, text, slug))
    
    if not matches:
        print("No hooks found in Markdown table.")
        return

    output_dir = Path("VLT_Content/04_HMN_OUTPUTS/AB_Tests/Modal_Renders")
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Found {len(matches)} hooks. Processing on Modal Cloud...")
    
    video_cache = {}

    for i, m in enumerate(matches):
        hid, v_path_str, text, slug = m
        hid = hid.strip() if hid else f"{i+1:02}"
        slug = slug.strip() if slug else f"hook-{hid}"
        v_path = Path(v_path_str.strip()).resolve()
        
        if not v_path.exists():
            continue
            
        if v_path not in video_cache:
            video_cache[v_path] = v_path.read_bytes()
            
        out_filename = f"hook_{hid}_{slug}.mp4"
        print(f"  [Cloud] Queueing Hook {hid}...")
        
        rendered_bytes = render_on_modal.remote(video_cache[v_path], text, out_filename)
        
        out_path = output_dir / out_filename
        out_path.write_bytes(rendered_bytes)
        print(f"  [Done] Saved {out_filename}")

    print(f"\nRender Complete! Files in: {output_dir}")
