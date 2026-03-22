
import os
import json
import subprocess
import shutil
from pathlib import Path

VIDEO_DIR = Path(r"C:\Users\natha\OneDrive - Bina Nusantara\Cook\VLT_Content\__VLT_OBSVAULT\PDCT_Real_Estate\__VIDEO")
REMOTION_PUBLIC = Path(r"C:\Users\natha\OneDrive - Bina Nusantara\Cook\VLT_Content\AI_ENGINE\remotion\public")
TARGET_DIR = REMOTION_PUBLIC / "PDCT_Real_Estate" / "__VIDEO"
PROPS_FILE = Path(r"C:\Users\natha\OneDrive - Bina Nusantara\Cook\VLT_Content\AI_ENGINE\remotion\src\video_to_audio_props.json")

def get_video_info(video_path):
    cmd = [
        "ffprobe",
        "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=duration,r_frame_rate",
        "-of", "json",
        str(video_path)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    data = json.loads(result.stdout)
    stream = data["streams"][0]
    duration = float(stream["duration"])
    fps_num, fps_den = map(int, stream["r_frame_rate"].split('/'))
    fps = fps_num / fps_den
    return {
        "filename": video_path.name,
        "durationInSeconds": duration,
        "fps": fps,
        "durationInFrames": int(duration * 30) # Normalize to 30fps for Remotion
    }

def main():
    if not TARGET_DIR.exists():
        TARGET_DIR.mkdir(parents=True)

    video_files = sorted([f for f in VIDEO_DIR.glob("*.mp4")])
    props = []

    for vf in video_files:
        print(f"Processing {vf.name}...")
        info = get_video_info(vf)
        props.append(info)
        
        # Copy to public folder
        target_path = TARGET_DIR / vf.name
        if not target_path.exists():
            shutil.copy2(vf, target_path)

    with open(PROPS_FILE, "w") as f:
        json.dump({"videos": props}, f, indent=2)

    total_frames = sum(v["durationInFrames"] for v in props)
    print(f"Total videos: {len(props)}")
    print(f"Total frames: {total_frames}")
    print(f"Total duration: {total_frames / 30:.2f}s")
    print(f"Props saved to {PROPS_FILE}")

if __name__ == "__main__":
    main()
