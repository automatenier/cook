import os
import sys
import subprocess
import json
import math
import argparse
from pathlib import Path

def run_command(cmd, cwd=None):
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True, cwd=cwd)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("audio_file", help="Path to the audio/video file")
    parser.add_argument("--hook", help="Static hook text to display at the top", default=None)
    parser.add_argument("--hook-color", help="Color of the hook text (hex)", default="#FFFFFF")
    args = parser.parse_args()

    audio_path = Path(args.audio_file).resolve()
    root_dir = Path(__file__).resolve().parent.parent
    remotion_dir = root_dir / "VLT_Content" / "AI_ENGINE" / "remotion"
    tmp_dir = root_dir / ".tmp"
    output_props = remotion_dir / "src" / "props.json"
    
    # 1. Transcribe with Whisper
    print("--- Phase 1: Transcribing ---")
    whisper_cmd = [
        "py", "-3", "-m", "whisper",
        str(audio_path),
        "--model", "base",
        "--output_format", "json",
        "--word_timestamps", "True",
        "--output_dir", str(tmp_dir)
    ]
    run_command(whisper_cmd)
    
    # Find the json file
    whisper_json = tmp_dir / f"{audio_path.stem}.json"
    
    # 2. Convert to Remotion Props
    print("--- Phase 2: Converting to Props ---")
    convert_script = root_dir / "AI_Tools" / "convert_whisper_to_remotion.py"
    run_command(["py", "-3", str(convert_script), str(whisper_json), str(output_props)])
    
    # 3. Update props.json with audio source and transparency
    # We copy audio to public first
    public_audio = remotion_dir / "public" / "task-audio.mp3"
    run_command(["cmd", "/c", "copy", str(audio_path), str(public_audio)])
    
    with open(output_props, 'r', encoding='utf-8') as f:
        props = json.load(f)
    
    props["videoSrc"] = "task-audio.mp3"
    props["backgroundVideos"] = []  # Clear footage
    props["transparent"] = True
    
    if args.hook:
        props["hookText"] = args.hook
        props["hookColor"] = args.hook_color

    with open(output_props, 'w', encoding='utf-8') as f:
        json.dump(props, f, indent=2)

    # 4. Render — MP4 (Note: MP4/H.264 does not support native alpha, but we keep transparent=True for blend modes)
    print("--- Phase 3: Rendering (MP4) ---")
    output_mp4 = remotion_dir / "out" / f"{audio_path.stem}_transparent.mp4"
    render_cmd = [
        "npx.cmd", "remotion", "render",
        "src/index.ts", "reproduction-video",
        "--output", str(output_mp4),
        "--codec", "h264",
    ]
    run_command(render_cmd, cwd=str(remotion_dir))

    print(f"\nDONE! Transparent captions exported to: {output_mp4}")

if __name__ == "__main__":
    main()
