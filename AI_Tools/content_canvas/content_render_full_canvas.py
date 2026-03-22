import modal
import json
import os
import argparse
import subprocess
from pathlib import Path

# 1. Define the Modal App
app = modal.App("canvas-full-renderer")

# 2. Container image with FFmpeg
image = (
    modal.Image.debian_slim()
    .apt_install("ffmpeg")
    .pip_install("pathlib")
)

# 3. Font path in container
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def get_latest_hook(hooks_file):
    """Parses Markdown table and returns the latest hook text."""
    if not os.path.exists(hooks_file):
        return "New Property Concept"
    
    with open(hooks_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Simple parser for the Markdown table
    matches = []
    for line in lines:
        if "|" in line and "ID" not in line and "---" not in line:
            cols = [c.strip() for c in line.split("|")]
            if len(cols) >= 4:
                # cols[1] is ID, cols[2] is Path, cols[3] is Hook text
                matches.append(cols[3])
    
    return matches[-1] if matches else "Real Estate Content"

def clean_hook_text(text):
    """Applies Production Batch rules: no asterisks, no <br> symbols, no dashes."""
    text = text.replace("**", "").replace("*", "")
    text = text.replace("--", "").replace("—", "")
    text = text.replace("<br>", "\n").replace("<br/>", "\n")
    return text

@app.function(image=image, timeout=1200)
def render_canvas_on_modal(canvas_data: dict, file_bytes_map: dict, hook_text: str) -> bytes:
    """Stitches videos, adds audio, and applies hook/captions on Modal."""
    
    # 1. Save all files to /tmp in container
    tmp_dir = Path("/tmp/assets")
    tmp_dir.mkdir(parents=True, exist_ok=True)
    
    local_paths = {}
    for filename, content in file_bytes_map.items():
        p = tmp_dir / os.path.basename(filename)
        p.write_bytes(content)
        local_paths[filename] = str(p)

    output_path = Path("/tmp/final_render.mp4")
    
    # 2. Build FFmpeg Filter Graph
    # Sort nodes by startFrame
    timeline = sorted(canvas_data['timeline'], key=lambda x: x['startFrame'])
    
    # Separate video and audio nodes
    video_nodes = [n for n in timeline if n['type'] == 'file' and (n['file'].lower().endswith(('.mp4', '.mov', '.m4v')))]
    audio_nodes = [n for n in timeline if n['type'] == 'file' and (n['file'].lower().endswith(('.mp3', '.wav', '.m4a')))]

    # Input flags for FFmpeg
    inputs = []
    for node in video_nodes:
        inputs.extend(["-i", local_paths[node['file']]])
    for node in audio_nodes:
        inputs.extend(["-i", local_paths[node['file']]])

    # Simple concatenation filter (as a starting point)
    # [0:v][0:a][1:v][1:a] concat=n=2:v=1:a=1 [v][a]
    filter_complex = ""
    for i in range(len(video_nodes)):
        filter_complex += f"[{i}:v][{i}:a]"
    filter_complex += f"concat=n={len(video_nodes)}:v=1:a=1[v_concat][a_concat];"
    
    # Add background audio if present
    if audio_nodes:
        audio_idx = len(video_nodes)
        filter_complex += f"[{audio_idx}:a]volume=0.3[bg_audio];"
        filter_complex += f"[a_concat][bg_audio]amix=inputs=2:duration=first[a_final];"
    else:
        filter_complex += f"[a_concat]anull[a_final];"

    # Add Hook Text (Production Batch Style: Upper Third, Centered)
    safe_text = clean_hook_text(hook_text).replace("'", "'\\''").replace(":", "\\:")
    filter_complex += f"[v_concat]drawtext=fontfile='{FONT_PATH}':text='{safe_text}':fontsize=55:fontcolor=white:borderw=4:bordercolor=black:line_spacing=10:x=(w-text_w)/2:y=h*0.15:text_align=center:enable='between(t,0,4)'[v_final]"

    cmd = [
        "ffmpeg", "-y"
    ] + inputs + [
        "-filter_complex", filter_complex,
        "-map", "[v_final]", "-map", "[a_final]",
        "-c:v", "libx264", "-crf", "23", "-preset", "veryfast",
        str(output_path)
    ]

    print(f"Executing: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)
    
    return output_path.read_bytes()

@app.local_entrypoint()
def main(canvas_file: str, hooks_file: str = "Z Brainstorm/Production_Batch.md"):
    canvas_path = Path(canvas_file).resolve()
    hooks_path = Path(hooks_file).resolve()
    
    # 1. Parse Canvas
    from content_render_canvas import parse_canvas
    props = parse_canvas(str(canvas_path))
    
    # 2. Get Hook
    hook_text = get_latest_hook(str(hooks_path))
    print(f"Using Hook: {hook_text}")

    # 3. Collect Bytes for Modal
    file_bytes_map = {}
    vault_root = Path(os.getcwd())
    
    for item in props['timeline']:
        if item['type'] == 'file':
            # Handle relative paths from vault root
            file_path = vault_root / item['file']
            if not file_path.exists():
                # Try finding it in the same folder as canvas
                file_path = canvas_path.parent / item['file']
                
            if file_path.exists():
                file_bytes_map[item['file']] = file_path.read_bytes()
            else:
                print(f"⚠️ Warning: File not found {item['file']}")

    # 4. Trigger Modal Render
    print("🚀 Uploading to Modal Cloud for rendering...")
    final_bytes = render_canvas_on_modal.remote(props, file_bytes_map, hook_text)
    
    output_dir = Path("VLT_Content/04_HMN_OUTPUTS/Canvas_Renders")
    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / f"canvas_render_{canvas_path.stem}.mp4"
    out_path.write_bytes(final_bytes)
    
    print(f"✅ DONE! Video saved to: {out_path}")

if __name__ == "__main__":
    import sys
    # For local testing if needed without modal entrypoint
    pass
