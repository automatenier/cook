import os
import subprocess
import json
import uuid
import argparse
from pathlib import Path

def run_command(command):
    print(f"Executing: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.stdout

def create_breakdown(video_path, output_dir, notebook_id=None):
    video_path = Path(video_path).resolve()
    output_dir = Path(output_dir).resolve()
    assets_dir = output_dir / "Assets" / video_path.stem
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. Extract Frames with ffmpeg
    print("--- Extracting Frames ---")
    frame_pattern = assets_dir / "scene_%03d.jpg"
    ffmpeg_cmd = f'ffmpeg -i "{video_path}" -filter:v "select=\'gt(scene,0.4)\',showinfo" -fps_mode vfr -strict unofficial "{frame_pattern}"'
    run_command(ffmpeg_cmd)
    
    # 2. Generate Canvas
    print("--- Generating Canvas ---")
    files = sorted([f.name for f in assets_dir.glob("*.jpg")])
    nodes = []
    x, y = 0, 0
    width, height = 400, 711
    padding = 50
    cols = 5
    
    for i, file in enumerate(files):
        nodes.append({
            "id": str(uuid.uuid4())[:16],
            "type": "file",
            "file": f"Assets/{video_path.stem}/{file}",
            "x": x,
            "y": y,
            "width": width,
            "height": height
        })
        if (i + 1) % cols == 0:
            x = 0
            y += height + padding
        else:
            x += width + padding
            
    canvas_path = output_dir / f"{video_path.stem}_Storyboard.canvas"
    with open(canvas_path, 'w', encoding='utf-8') as f:
        json.dump({"nodes": nodes, "edges": []}, f, indent=2)
    
    # 3. Generate Markdown Template
    print("--- Generating Markdown Breakdown ---")
    md_path = output_dir / f"{video_path.stem}_Breakdown.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(f"# Video Breakdown: {video_path.stem}\n\n")
        f.write("## Storyboard\n\n")
        for i, file in enumerate(files):
            f.write(f"### Scene {i+1:02d}\n")
            f.write(f"![[Assets/{video_path.stem}/{file}]]\n")
            f.write("**Transcript:** [Insert from NotebookLM]\n\n")
            f.write("---\n\n")
            
    print(f"Breakdown complete!\nCanvas: {canvas_path}\nMarkdown: {md_path}\nAssets: {assets_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Break down a video into frames, canvas, and markdown.")
    parser.add_argument("video", help="Path to the video file")
    parser.add_argument("--output", help="Output directory (default: current)", default=".")
    
    args = parser.parse_args()
    create_breakdown(args.video, args.output)
