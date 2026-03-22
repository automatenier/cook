import os
import sys
import subprocess
import json
import math
from pathlib import Path

def run_command(cmd, cwd=None):
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True, cwd=cwd)

def main():
    if len(sys.argv) < 2:
        print("Usage: py -3 AI_Tools/create_captions.py <audio_file>")
        sys.exit(1)

    audio_path = Path(sys.argv[1]).resolve()
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
    
    # 3. Update props.json with audio source
    # We copy audio to public first
    public_audio = remotion_dir / "public" / "task-audio.mp3"
    run_command(["cmd", "/c", "copy", str(audio_path), str(public_audio)])
    
    with open(output_props, 'r', encoding='utf-8') as f:
        props = json.load(f)
    
    props["videoSrc"] = "task-audio.mp3"
    props["backgroundVideos"] = []   # Clear footage for "captions only"
    # TRANSPARENCY REQUIREMENT 1/3: component must receive transparent=True
    # so ReproductionReel renders backgroundColor='transparent' not '#111'.
    # Without this prop the background stays black regardless of codec flags.
    props["transparent"] = True

    with open(output_props, 'w', encoding='utf-8') as f:
        json.dump(props, f, indent=2)

    # 4. Render — WebM with real alpha channel
    # TRANSPARENCY REQUIREMENTS 2+3/3:
    #   --codec vp8          → VP8/VP9 are the only codecs with alpha support (h265 does NOT work)
    #   --image-format png   → PNG frames preserve alpha; jpeg would destroy it
    #   --pixel-format yuva420p → adds the actual alpha plane to the output
    # Output must be .webm — MP4 container does not support alpha.
    print("--- Phase 3: Rendering (Transparent WebM) ---")
    output_webm = remotion_dir / "out" / f"{audio_path.stem}_captions.webm"
    render_cmd = [
        "npx.cmd", "remotion", "render",
        "src/index.ts", "reproduction-video",
        "--output", str(output_webm),
        "--codec", "vp8",
        "--image-format", "png",
        "--pixel-format", "yuva420p",
    ]
    run_command(render_cmd, cwd=str(remotion_dir))

    print(f"\nDONE! Transparent captions exported to: {output_webm}")

if __name__ == "__main__":
    main()
