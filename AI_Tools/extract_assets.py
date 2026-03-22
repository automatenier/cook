import os
import sys
import json
from pathlib import Path
from PIL import Image
from dotenv import load_dotenv

# Load .env for GEMINI_API_KEY
load_dotenv(Path(__file__).parent / ".env")

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("Error: google-genai not installed. Run: pip install google-genai")
    sys.exit(1)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY not set")
    sys.exit(1)

def get_bounding_boxes(image_path: str):
    client = genai.Client(api_key=api_key)
    img_file = Path(image_path)
    
    prompt = """
    Analyze this image and find the bounding boxes for these 5 distinct assets:
    1. Background Layer (Full-screen background image)
    2. Logo Layer (Circular profile picture/logo top left)
    3. Before & After (Middle/Right section showing progress photos)
    4. Screenshot (The client text message)
    5. Graph (The weight loss trend line graph)

    Return ONLY a JSON list of objects with 'name' and 'box_2d' [ymin, xmin, ymax, xmax] in normalized coordinates (0-1000).
    Example: [{"name": "background", "box_2d": [0, 0, 1000, 1000]}, ...]
    """
    
    # Need to read as bytes for direct upload if it's small, or use upload
    image_bytes = img_file.read_bytes()
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            types.Content(
                role="user",
                parts=[
                    types.Part.from_bytes(data=image_bytes, mime_type="image/png"),
                    types.Part.from_text(text=prompt),
                ],
            )
        ],
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
        )
    )
    
    return json.loads(response.text)

def crop_assets(image_path: str, output_dir: str):
    boxes = get_bounding_boxes(image_path)
    print(f"Found {len(boxes)} boxes.")
    
    img = Image.open(image_path)
    width, height = img.size
    
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    
    results = []
    for asset in boxes:
        name = asset['name'].replace(" ", "_")
        ymin, xmin, ymax, xmax = asset['box_2d']
        
        # Convert normalized to pixel coordinates
        left = xmin * width / 1000
        top = ymin * height / 1000
        right = xmax * width / 1000
        bottom = ymax * height / 1000
        
        cropped = img.crop((left, top, right, bottom))
        filename = f"Asset_{name}.png"
        cropped.save(out_path / filename)
        results.append((name, filename))
        print(f"Saved {filename}")
    
    return results

if __name__ == "__main__":
    img_path = "PDCT_JO_Consult/C Storyboarding/0. Asset/Product Photo/zz Image Swipe/ObsAttachment/Asset_Asset_636_Pasted_image_20251226001030_612.png"
    out_dir = "PDCT_JO_Consult/C Storyboarding/0. Asset/Product Photo/zz Image Swipe/ObsAttachment/Extracted_Assets"
    crop_assets(img_path, out_dir)
