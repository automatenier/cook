import json
import os
import argparse
import sys

# Constants
FPS = 30
RENDER_PROPS = "VLT_Content/AI_ENGINE/render_props.json"

def parse_canvas(canvas_path):
    """Parses Obsidian .canvas JSON and translates to a Remotion-ready timeline."""
    if not os.path.exists(canvas_path):
        print(f"❌ Error: File not found {canvas_path}")
        return None

    with open(canvas_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    nodes = data.get('nodes', [])
    timeline = []

    # Filter for 'file' type nodes (actual media) or 'text' nodes
    # Sort by X position to determine order
    sorted_nodes = sorted(nodes, key=lambda n: n.get('x', 0))

    current_frame = 0
    for node in sorted_nodes:
        node_type = node.get('type')
        x = node.get('x', 0)
        y = node.get('y', 0)
        width = node.get('width', 400)
        
        # Calculate duration based on width (e.g., 100px = 1 second)
        # We can normalize this: 400px = 4 seconds (120 frames at 30fps)
        duration_frames = int((width / 100) * FPS)
        
        # Determine start frame based on X position relative to previous node
        # In a spatial timeline, x position can be absolute
        start_frame = int((x / 100) * FPS)
        if start_frame < 0: start_frame = 0

        item = {
            "id": node.get('id'),
            "type": node_type,
            "startFrame": start_frame,
            "durationFrames": duration_frames,
            "layer": int(y / 100), # Simple layer mapping based on vertical position
            "props": {}
        }

        if node_type == 'file':
            item["file"] = node.get('file')
        elif node_type == 'text':
            item["text"] = node.get('text')

        timeline.append(item)

    return {
        "project": os.path.basename(canvas_path),
        "timeline": timeline,
        "fps": FPS
    }

def main():
    parser = argparse.ArgumentParser(description="Convert Obsidian Canvas to Remotion Render Props")
    parser.add_argument("--file", required=True, help="Path to the .canvas file")
    parser.add_argument("--output", default=RENDER_PROPS, help="Output JSON path")
    args = parser.parse_args()

    props = parse_canvas(args.file)
    if props:
        os.makedirs(os.path.dirname(args.output), exist_ok=True)
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(props, f, indent=2)
        print(f"✅ SUCCESS: Generated render props from {args.file}")
        print(f"📍 Location: {args.output}")

if __name__ == "__main__":
    main()
