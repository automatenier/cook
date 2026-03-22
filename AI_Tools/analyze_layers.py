
import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv

# Load .env to get GEMINI_API_KEY
load_dotenv(Path(__file__).parent / ".env")

try:
    from google import genai
except ImportError:
    print("Error: google-genai not installed. Run: pip install google-genai")
    sys.exit(1)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY not set in .env")
    sys.exit(1)

def analyze_video_layers(video_path: str):
    video_file = Path(video_path)
    print(f"Uploading {video_file.name} to Gemini...")
    client = genai.Client(api_key=api_key)
    uploaded = client.files.upload(file=video_file)

    # Wait for file to become ACTIVE
    print("Waiting for file to be ready...")
    while uploaded.state.name != "ACTIVE":
        time.sleep(3)
        uploaded = client.files.get(name=uploaded.name)
        print(f"  File state: {uploaded.state.name}")

    print(f"Processing with Gemini...")

    prompt = """
    Analyze this video and identify the 3 layers for production purposes.
    The user mentioned there are 3 layers. 
    Please describe:
    1. Layer 1 (e.g. Background/A-roll)
    2. Layer 2 (e.g. Middle/Speaker/Overlay)
    3. Layer 3 (e.g. Foreground/Captions/Graphics)
    
    Provide a detailed description of what each layer contains visually and how they are used.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[uploaded, prompt],
    )

    print("\n--- Layer Analysis ---")
    print(response.text)

if __name__ == "__main__":
    video_path = "C:\\Users\\natha\\OneDrive - Bina Nusantara\\Cook\\Reel2.mov"
    analyze_video_layers(video_path)
