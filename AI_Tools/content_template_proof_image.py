import argparse
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

def create_proof_image(input_path, output_path, hook, mechanism, proof):
    if not os.path.exists(input_path):
        print(f"Error: Input file {input_path} does not exist.")
        return

    try:
        img = Image.open(input_path).convert("RGBA")
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    # Resize to 1080x1920 (Instagram Story size) while maintaining aspect ratio, cropping the center
    target_width, target_height = 1080, 1920
    img_ratio = img.width / img.height
    target_ratio = target_width / target_height

    if img_ratio > target_ratio:
        # Image is wider than target, scale by height
        new_height = target_height
        new_width = int(new_height * img_ratio)
    else:
        # Image is taller than target, scale by width
        new_width = target_width
        new_height = int(new_width / img_ratio)

    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Crop center
    left = (new_width - target_width) / 2
    top = (new_height - target_height) / 2
    right = (new_width + target_width) / 2
    bottom = (new_height + target_height) / 2
    img = img.crop((left, top, right, bottom))

    # Prepare text drawing
    draw = ImageDraw.Draw(img, "RGBA")
    
    # Try to load Arial font (default on Windows), fallback to Pillow default if not found
    try:
        font_hook = ImageFont.truetype("arialbd.ttf", 45) # Bold for hook
        font_body = ImageFont.truetype("arial.ttf", 38)   # Regular for mechanism
        font_proof = ImageFont.truetype("arialbd.ttf", 42) # Bold for proof
    except IOError:
        print("Arial font not found, falling back to default font. Text might look small.")
        font_hook = ImageFont.load_default()
        font_body = ImageFont.load_default()
        font_proof = ImageFont.load_default()

    # Wrap text to fit inside the 1080px width
    max_chars_hook = 40
    max_chars_body = 48
    
    hook_lines = textwrap.wrap(hook, width=max_chars_hook)
    mech_lines = textwrap.wrap(mechanism, width=max_chars_body)
    proof_lines = textwrap.wrap(proof, width=max_chars_hook)

    # Layout configuration
    line_height_hook = 55
    line_height_body = 45
    padding = 40
    margin = 50 # Distance from screen edge
    
    total_height_hook = len(hook_lines) * line_height_hook
    total_height_mech = len(mech_lines) * line_height_body
    total_height_proof = len(proof_lines) * line_height_hook
    
    section_spacing = 30
    
    box_height = (total_height_hook + section_spacing + 
                  total_height_mech + section_spacing + 
                  total_height_proof + (padding * 2))
                  
    box_width = target_width - (margin * 2)

    # Draw semi-transparent background box
    # Position: Lower middle (300px from the bottom)
    box_y_end = target_height - 300
    box_y_start = box_y_end - box_height
    box_x_start = margin
    box_x_end = target_width - margin

    draw.rectangle(
        [(box_x_start, box_y_start), (box_x_end, box_y_end)],
        fill=(0, 0, 0, 160) # Black with ~60% opacity for legibility but keeping photo visible
    )

    # Draw Text Layers
    y_text = box_y_start + padding
    x_text = box_x_start + padding

    # Layer 1: Hook
    for line in hook_lines:
        draw.text((x_text, y_text), line, font=font_hook, fill=(255, 255, 255, 255)) # Pure white
        y_text += line_height_hook
    
    y_text += section_spacing

    # Layer 2: Mechanism
    for line in mech_lines:
        draw.text((x_text, y_text), line, font=font_body, fill=(210, 210, 210, 255)) # Slightly grey for contrast
        y_text += line_height_body
        
    y_text += section_spacing

    # Layer 3: Proof
    for line in proof_lines:
        draw.text((x_text, y_text), line, font=font_proof, fill=(255, 255, 255, 255)) # Pure white
        y_text += line_height_hook

    # Save output
    final_img = img.convert("RGB") # Remove alpha channel for saving as JPEG
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    
    final_img.save(output_path, quality=95)
    print(f"✅ Success! Authority Proof Image saved to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Authority Proof Image")
    parser.add_argument("--input", required=True, help="Path to raw image")
    parser.add_argument("--output", required=True, help="Path to save final image")
    parser.add_argument("--hook", required=True, help="The Observation / Hook")
    parser.add_argument("--mechanism", required=True, help="The Mechanism / How")
    parser.add_argument("--proof", required=True, help="The Result / Proof")
    
    args = parser.parse_args()
    create_proof_image(args.input, args.output, args.hook, args.mechanism, args.proof)