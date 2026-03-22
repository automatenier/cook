
import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv

# Load .env to get GEMINI_API_KEY
load_dotenv(Path(__file__).parent / ".env")

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("Error: google-genai not installed. Run: pip install google-genai")
    sys.exit(1)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY not set in .env")
    sys.exit(1)

def analyze_frames(frame_paths: list):
    client = genai.Client(api_key=api_key)
    
    uploaded_files = []
    for path in frame_paths:
        p = Path(path)
        if not p.exists():
            print(f"Warning: {path} not found.")
            continue
        print(f"Uploading {p.name}...")
        uploaded = client.files.upload(file=p)
        
        # Wait for file to become ACTIVE
        while uploaded.state.name != "ACTIVE":
            time.sleep(2)
            uploaded = client.files.get(name=uploaded.name)
        
        uploaded_files.append(uploaded)

    if not uploaded_files:
        print("No files uploaded.")
        return

    print(f"Processing frames with Gemini...")

    prompt = """
    Analyze these 3 frames from a video and identify the 3 layers for production purposes.
    The user mentioned there are 3 layers in the original video.
    Please describe:
    1. Layer 1 (Background/A-roll)
    2. Layer 2 (Middle ground/Speaker/Overlays)
    3. Layer 3 (Foreground/Captions/Graphics)
    
    Identify what is consistently in each layer across the frames.
    """

    # Combine frames and prompt
    contents = uploaded_files + [prompt]

    response = client.models.generate_content(
        model="gemini-2.0-flash", # Use 2.0 flash for speed
        contents=contents,
    )

    print("\n--- Layer Analysis ---")
    print(response.text)

if __name__ == "__main__":
    frames = [
        "___Data/frame_start.jpg",
        "___Data/frame_middle.tmp", # I renamed it earlier
        "___Data/frame_end.jpg"
    ]
    # Make sure all are .jpg or valid image extensions for the API
    # I'll rename frame_middle.tmp back to .jpg first
    Path("___Data/frame_middle.tmp").rename("___Data/frame_middle.jpg")
    
    analyze_frames(["___Data/frame_start.jpg", "___Data/frame_middle.jpg", "___Data/frame_end.jpg"])
