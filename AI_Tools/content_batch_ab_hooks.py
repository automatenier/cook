import os
import sys
import subprocess
import argparse
import re
import textwrap
import asyncio
import json
from pathlib import Path

# Constants
OUTPUT_BASE = Path("VLT_Content/04_HMN_OUTPUTS/AB_Tests/1_mov")
# On Windows, ffmpeg drawtext filter requires escaping colons in paths
FONT_PATH = "C\\:/Windows/Fonts/arialbd.ttf"  # Bold Arial for hooks

def run_command(cmd):
    print(f"Executing: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

def parse_hooks_md(md_path):
    hooks = []
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Updated table parser for: | ID | Video Path | Hook | Slug |
    pattern = r"\| (\d+) \| (.*?) \| (.*?) \| (.*?) \|"
    matches = re.findall(pattern, content)
    for m in matches:
        hooks.append({
            "id": m[0],
            "video": m[1].strip(),
            "text": m[2].strip(),
            "slug": m[3].strip()
        })
    return hooks

def wrap_text(text, width=25):
    """Wraps text to ensure it stays within the vertical video width."""
    # Remove <br> tags and replace with newlines
    text = text.replace("<br>", "\n").replace("<br/>", "\n")
    # Also handle markdown bold **
    text = text.replace("**", "")
    lines = []
    for line in text.split("\n"):
        lines.extend(textwrap.wrap(line, width=width))
    return "\n".join(lines)

def render_hook_local(video_path, hook, output_dir):
    # 1. Wrap text to prevent cutting off at the edges
    wrapped_text = wrap_text(hook['text'], width=22)
    
    # 2. Escape for ffmpeg:
    # Colons and single quotes need specific escaping for the drawtext filter
    safe_text = wrapped_text.replace("'", "'\\''").replace(":", "\\:")
    
    output_path = output_dir / f"hook_{hook['id']}_{hook['slug']}.mp4"
    
    # FFmpeg command calibrated to "CBD Deltamas" benchmark:
    #   - fontsize: 55 (safe for 1080px width with wrapping)
    #   - y: h*0.15 (upper safe zone, matching top-tier hook placement)
    #   - line_spacing: 10 (readability)
    #   - borderw: 4 (high contrast outline)
    
    cmd = [
        "ffmpeg", "-y",
        "-i", str(video_path),
        "-vf", f"drawtext=fontfile='{FONT_PATH}':text='{safe_text}':fontsize=55:fontcolor=white:borderw=4:bordercolor=black:line_spacing=10:x=(w-text_w)/2:y=h*0.15:enable='between(t,0,3)'",
        "-c:v", "libx264", "-crf", "23", "-preset", "veryfast",
        "-c:a", "copy",
        str(output_path)
    ]
    
    run_command(cmd)

async def render_hook_modal(video_path, hook, output_dir):
    try:
        import modal
    except ImportError:
        print("Error: 'modal' package not installed. Run 'pip install modal'.")
        return False

    # Note: Modal rendering usually requires the video to be in the 'public' folder
    # of the remotion project or accessible via URL. 
    # For this demo, we'll assume the 'render_remotion' function can handle props.
    # However, 'ReproductionReel' or similar is needed.
    
    print(f"  [Modal] Rendering {hook['id']} via cloud...")
    
    # Define props for Remotion
    props = {
        "hookText": wrap_text(hook['text'], width=22),
        "videoSrc": video_path.name, # Modal would need the file uploaded or in mount
        "transparent": False
    }
    
    try:
        render_fn = modal.Function.from_name("cook-tools", "render_remotion")
        # Assuming there is a 'HookTestReel' or we use 'ValueCTAReel'
        # For now, let's use 'ValueCTAReel' logic or similar if it exists
        composition = "ValueCTAReel" 
        
        mp4_data = await render_fn.remote.aio(composition, props)
        
        output_path = output_dir / f"hook_{hook['id']}_{hook['slug']}.mp4"
        output_path.write_bytes(mp4_data)
        return True
    except Exception as e:
        print(f"  [Modal] Error: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Batch render A/B hook captions onto a video.")
    parser.add_argument("--video", help="Optional default input video (if missing from MD)")
    parser.add_argument("--hooks", required=True, help="Path to Markdown file with hooks table")
    parser.add_argument("--modal", action="store_true", help="Use Modal cloud rendering")
    
    args = parser.parse_args()
    
    hooks_md = Path(args.hooks).resolve()
    if not hooks_md.exists():
        print(f"Error: Hooks file not found at {hooks_md}")
        sys.exit(1)
        
    hooks = parse_hooks_md(hooks_md)
    if not hooks:
        print("Error: No hooks found in Markdown file.")
        sys.exit(1)
        
    # Ensure output dir exists
    OUTPUT_BASE.mkdir(parents=True, exist_ok=True)
    
    print(f"Found {len(hooks)} hooks. Starting {'Modal' if args.modal else 'Local'} batch render...")
    
    if args.modal:
        async def run_batch():
            tasks = []
            for hook in hooks:
                v_path = Path(hook['video'] if hook['video'] else args.video).resolve()
                tasks.append(render_hook_modal(v_path, hook, OUTPUT_BASE))
            await asyncio.gather(*tasks)
        asyncio.run(run_batch())
    else:
        for hook in hooks:
            v_path = Path(hook['video'] if hook['video'] else args.video).resolve()
            if not v_path.exists():
                print(f"Error: Video not found at {v_path}. Skipping Hook {hook['id']}.")
                continue
                
            print(f"\n--- Rendering Hook {hook['id']} on {v_path.name}: {hook['text']} ---")
            try:
                render_hook_local(v_path, hook, OUTPUT_BASE)
            except Exception as e:
                print(f"Failed to render hook {hook['id']}: {e}")

    print(f"\nBatch render complete! Files saved to: {OUTPUT_BASE}")

if __name__ == "__main__":
    main()

