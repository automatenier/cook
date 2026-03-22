import json
import argparse
import re
import os

def parse_markdown_to_props(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    props = {
        "videoSrc": "user-video.mp4",
        "popAudioSrc": "pop.mp3",
        "items": []
    }

    # Extract Global Assets
    video_source_match = re.search(r'- Video_Source: "([^"]+)"', content)
    if video_source_match:
        props["videoSrc"] = video_source_match.group(1)
        
    audio_pop_match = re.search(r'- Audio_Pop: "([^"]+)"', content)
    if audio_pop_match:
        props["popAudioSrc"] = audio_pop_match.group(1)

    # Extract Items Table
    table_pattern = r'\| ID \| Label \| Image \| Row \| Slot \| Appear \(Frame\) \| Move \(Frame\) \|.*?
\|---\|---\|---\|---\|---\|---\|---\|.*?
(.*?)(?:

|
---|$)'
    table_match = re.search(table_pattern, content, re.DOTALL)
    
    if table_match:
        rows = table_match.group(1).strip().split('
')
        for row in rows:
            cols = [c.strip() for c in row.strip('|').split('|')]
            if len(cols) >= 7:
                item = {
                    "id": cols[0],
                    "label": cols[1],
                    "image": cols[2].strip('"'),
                    "targetRow": cols[3],
                    "targetCol": int(cols[4]),
                    "entryFrame": int(cols[5]),
                    "moveFrame": int(cols[6])
                }
                props["items"].append(item)

    return props

def main():
    parser = argparse.ArgumentParser(description='Convert Video Data Markdown to Remotion Props JSON')
    parser.add_argument('--input', required=True, help='Path to the input Markdown file')
    parser.add_argument('--output', default='VLT_Content/AI_ENGINE/remotion/src/props.json', help='Path to save the output JSON')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"Error: {args.input} not found.")
        return

    props = parse_markdown_to_props(args.input)
    
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(props, f, indent=2)
    
    print(f"Successfully converted {args.input} to {args.output}")

if __name__ == "__main__":
    main()
