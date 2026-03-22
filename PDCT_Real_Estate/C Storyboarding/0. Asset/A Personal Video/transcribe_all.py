import os
import subprocess
from pathlib import Path

def main():
    video_dir = Path(r"VLT_Content\__VLT_OBSVAULT\PDCT_Real_Estate\__VIDEO")
    output_file = Path("transcriptions.md")
    
    videos = list(video_dir.glob("*.mp4"))
    videos.sort()
    
    with open(output_file, "w", encoding="utf-8") as f:
        for i, video in enumerate(videos):
            print(f"Transcribing {i+1}/{len(videos)}: {video.name}")
            
            # Run whisper
            # We use --model base for speed, --output_format txt
            # We'll capture the output and write it to our md file
            try:
                result = subprocess.run(
                    ["py", "-3", "-m", "whisper", str(video), "--model", "base", "--output_format", "txt", "--output_dir", ".tmp"],
                    capture_output=True,
                    text=True,
                    check=True
                )
                
                txt_file = Path(".tmp") / f"{video.stem}.txt"
                if txt_file.exists():
                    transcript = txt_file.read_text(encoding="utf-8").strip()
                    f.write(f"## {video.name}\n\n")
                    f.write(transcript + "\n\n")
                    if i < len(videos) - 1:
                        f.write("---\n\n")
                else:
                    print(f"Warning: Transcript file not found for {video.name}")
                    
            except subprocess.CalledProcessError as e:
                print(f"Error transcribing {video.name}: {e}")
                f.write(f"## {video.name}\n\nError transcribing file.\n\n")
                if i < len(videos) - 1:
                    f.write("---\n\n")

    print(f"Finished! Transcriptions saved to {output_file}")

if __name__ == "__main__":
    main()
