import sys
import json
import uuid
import math

def create_element(etype, x, y, width, height, text=""):
    id = str(uuid.uuid4())
    element = {
        "id": id,
        "type": etype,
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "angle": 0,
        "strokeColor": "#1e1e1e",
        "backgroundColor": "transparent",
        "fillStyle": "hachure",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "roundness": {"type": 3} if etype == "rectangle" else None,
        "seed": 12345,
        "version": 1,
        "versionNonce": 0,
        "isDeleted": False,
        "boundElements": None,
        "updated": 1,
        "link": None,
        "locked": False
    }
    
    if text:
        text_id = str(uuid.uuid4())
        element["boundElements"] = [{"type": "text", "id": text_id}]
        text_element = {
            "id": text_id,
            "type": "text",
            "x": x + 10,
            "y": y + 10,
            "width": width - 20,
            "height": height - 20,
            "angle": 0,
            "strokeColor": "#1e1e1e",
            "backgroundColor": "transparent",
            "fillStyle": "hachure",
            "strokeWidth": 1,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "roundness": None,
            "seed": 54321,
            "version": 1,
            "versionNonce": 0,
            "isDeleted": False,
            "boundElements": None,
            "updated": 1,
            "link": None,
            "locked": False,
            "text": text,
            "fontSize": 20,
            "fontFamily": 1,
            "textAlign": "center",
            "verticalAlign": "middle",
            "containerId": id,
            "originalText": text
        }
        return [element, text_element]
    return [element]

def generate_excalidraw(data, output_path):
    elements = []
    center_x, center_y = 500, 500
    
    # Root Node
    root_w, root_h = 200, 80
    elements.extend(create_element("rectangle", center_x - root_w/2, center_y - root_h/2, root_w, root_h, data.get("root", "Topic")))
    
    # Branch Nodes
    nodes = data.get("nodes", [])
    radius = 300
    for i, node_text in enumerate(nodes):
        angle = (2 * math.pi * i) / len(nodes)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        
        node_w, node_h = 150, 60
        elements.extend(create_element("rectangle", x - node_w/2, y - node_h/2, node_w, node_h, node_text))
        
        # Simple line connector
        elements.append({
            "type": "arrow",
            "x": center_x,
            "y": center_y,
            "points": [[0, 0], [x - center_x, y - center_y]],
            "strokeColor": "#1e1e1e",
            "backgroundColor": "transparent",
            "strokeWidth": 1,
            "roughness": 1,
            "opacity": 100,
            "startArrowhead": None,
            "endArrowhead": None
        })

    excalidraw_data = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": elements,
        "appState": {"viewBackgroundColor": "#ffffff", "gridSize": None},
        "files": {}
    }
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(excalidraw_data, f, indent=2)
    print(f"✅ Excalidraw mindmap saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: py -3 excalidraw_gen.py <input_json_path> <output_excalidraw_path>")
        sys.exit(1)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        data = json.load(f)
    # Extract map_data if it's nested
    map_data = data.get("map_data", data)
    generate_excalidraw(map_data, sys.argv[2])
