import json
import argparse
import os
from pathlib import Path

def parse_canvas(canvas_path):
    with open(canvas_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    nodes = data.get('nodes', [])
    # Sort nodes by Y coordinate (top to bottom)
    nodes.sort(key=lambda n: n.get('y', 0))
    
    script_beats = []
    current_beat = {"visual": "", "audio": "", "overlay": ""}
    
    for node in nodes:
        node_type = node.get('type')
        
        if node_type == 'file':
            # It's an asset
            file_path = node.get('file', '')
            # If we had a beat with a visual already, save it and start a new one
            if current_beat["visual"]:
                script_beats.append(current_beat)
                current_beat = {"visual": "", "audio": "", "overlay": ""}
            current_beat["visual"] = f"![[{file_path}]]"
            
        elif node_type == 'text':
            text = node.get('text', '').strip()
            if not text: continue
            
            # Check if it's bold (Overlay Text convention)
            if text.startswith('**') and text.endswith('**'):
                current_beat["overlay"] = text.replace('**', '')
            else:
                current_beat["audio"] = text
                
    # Append the last beat
    if current_beat["visual"] or current_beat["audio"]:
        script_beats.append(current_beat)
        
    return script_beats

def generate_markdown(beats, title="Canvas Storyboard"):
    md = f"# MASTER SCRIPT: {title}\n"
    md += "| Time | Visual | Audio (Script) | Overlay Text |\n"
    md += "|------|--------|----------------|--------------|\n"
    
    for i, beat in enumerate(beats):
        time = f"{i*5}-{(i+1)*5}s" # Placeholder timing
        md += f"| {time} | {beat['visual']} | {beat['audio']} | {beat['overlay']} |\n"
        
    return md

def main():
    parser = argparse.ArgumentParser(description='Convert Obsidian Canvas to Video Brief')
    parser.add_argument('--input', required=True, help='Path to the .canvas file')
    parser.add_argument('--output', help='Path to save the output Markdown')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"Error: {args.input} not found.")
        return

    title = Path(args.input).stem
    beats = parse_canvas(args.input)
    md_content = generate_markdown(beats, title)
    
    output_path = args.output or f"VLT_Content/__VLT_OBSVAULT/02_HMN_AIREVIEW/brief_{title.lower().replace(' ', '_')}.md"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print(f"Successfully converted Canvas to Brief: {output_path}")

if __name__ == "__main__":
    main()
