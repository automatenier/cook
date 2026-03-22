import modal
import os
import io
from pathlib import Path

# Define the Modal Image with FFmpeg installed
image = (
    modal.Image.debian_slim()
    .apt_install("ffmpeg")
    .pip_install("pathlib")
)

app = modal.App("video-guide-renderer")

@app.function(image=image, timeout=600)
def render_guide_video(frames_data: list, durations: list):
    """
    frames_data: List of bytes (image contents)
    durations: List of floats (seconds per frame)
    """
    import subprocess
    import tempfile
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        
        # Save frames to temp directory
        frame_files = []
        for i, frame_bytes in enumerate(frames_data):
            frame_path = tmp_path / f"frame_{i:03d}.jpg"
            frame_path.write_bytes(frame_bytes)
            frame_files.append(frame_path)
            
        # Create concat.txt for ffmpeg
        concat_path = tmp_path / "concat.txt"
        with open(concat_path, "w") as f:
            for i, (file, dur) in enumerate(zip(frame_files, durations)):
                f.write(f"file '{file.name}'\n")
                f.write(f"duration {dur}\n")
            # Repeat last file to ensure duration is respected
            f.write(f"file '{frame_files[-1].name}'\n")
            
        output_path = tmp_path / "guide_video.mp4"
        
        # Run FFmpeg to stitch frames
        # We use a vertical 9:16 resolution (720x1280)
        cmd = [
            "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_path),
            "-pix_fmt", "yuv420p", "-vf", "scale=720:1280,format=yuv420p",
            "-r", "30", str(output_path)
        ]
        
        subprocess.run(cmd, check=True, capture_output=True)
        
        return output_path.read_bytes()

if __name__ == "__main__":
    # This part runs locally to trigger the Modal function
    import sys
    
    # Configuration
    REF_VIDEO = r"C:\Users\natha\OneDrive - Bina Nusantara\Cook\PDCT_Real_Estate\A Reference\Video\_Trend\tiktok_inijoeng_7553571445754957067.mp4"
    ASSETS_DIR = r"C:\Users\natha\OneDrive - Bina Nusantara\Cook\PDCT_Real_Estate\Assets\inijoeng_frames"
    OUTPUT_FILE = r"C:\Users\natha\OneDrive - Bina Nusantara\Cook\PDCT_Real_Estate\Guide_Video_Reference_Modal.mp4"
    
    # 1. Get scene durations locally using ffprobe
    def get_scene_durations(video_path):
        import re
        cmd = f'ffmpeg -i "{video_path}" -filter:v "select=\'gt(scene,0.4)\',showinfo" -f null -'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        timestamps = [0.0]
        matches = re.findall(r"pts_time:([\d.]+)", result.stderr)
        for m in matches:
            timestamps.append(float(m))
        
        dur_cmd = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{video_path}"'
        total_dur = float(subprocess.run(dur_cmd, shell=True, capture_output=True, text=True).stdout.strip())
        timestamps.append(total_dur)
        
        return [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]

    import subprocess
    durs = get_scene_durations(REF_VIDEO)
    
    # 2. Collect frames
    assets_path = Path(ASSETS_DIR)
    # Get the 15 renamed files in order
    frame_files = sorted([f for f in assets_path.glob("*.jpg")])[:len(durs)]
    frames_data = [f.read_bytes() for f in frame_files]
    
    # 3. Trigger Modal
    print(f"--- Sending {len(frames_data)} frames to Modal for rendering ---")
    with app.run():
        video_bytes = render_guide_video.remote(frames_data, durs)
            
    # 4. Save result
    with open(OUTPUT_FILE, "wb") as f:
        f.write(video_bytes)
        
    print(f"Successfully rendered guide video via Modal: {OUTPUT_FILE}")
