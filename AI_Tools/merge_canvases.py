import os
import json
import uuid
from pathlib import Path

def merge_canvases(source_dir, target_canvas_path):
    source_dir = Path(source_dir).resolve()
    target_canvas_path = Path(target_canvas_path).resolve()
    
    all_nodes = []
    current_y = 0
    padding_y = 200
    
    canvas_files = list(source_dir.glob("*.canvas"))
    for canvas_file in canvas_files:
        with open(canvas_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            nodes = data.get("nodes", [])
            
            # Find the min/max height of this block to shift y for next
            max_y_in_block = 0
            for node in nodes:
                # Update path to be relative to the target canvas
                # Original path was "Assets/..."
                # New path should be "C Storyboarding/Assets/..."
                node["file"] = f"C Storyboarding/{node['file']}"
                
                # Shift node to current_y
                node["y"] += current_y
                
                # Check max height for next offset
                node_bottom = node["y"] + node["height"]
                if node_bottom > max_y_in_block:
                    max_y_in_block = node_bottom
            
            all_nodes.extend(nodes)
            current_y = max_y_in_block + padding_y

    with open(target_canvas_path, 'w', encoding='utf-8') as f:
        json.dump({"nodes": all_nodes, "edges": []}, f, indent=2)
    
    print(f"Merged {len(canvas_files)} canvases into {target_canvas_path}")

if __name__ == "__main__":
    # Source is now the Storyboarding folder in Consult
    # Target is still Here.canvas in Consult
    merge_canvases("PDCT_JO_Consult/C Storyboarding", "PDCT_JO_Consult/Here.canvas")
