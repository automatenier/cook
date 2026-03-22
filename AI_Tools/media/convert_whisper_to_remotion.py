import json
import math
from pathlib import Path

def convert_whisper_to_remotion(whisper_json_path, output_json_path, fps=30):
    with open(whisper_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    layers = []
    
    # Progress Bar (Runs for entire duration)
    total_duration = data.get('segments', [])[-1]['end'] if data.get('segments') else 0
    layers.append({
        "type": "progress-bar",
        "content": "top-bar",
        "startFrame": 0,
        "endFrame": math.ceil(total_duration * fps),
        "props": {
            "color": "#FFFFFF",
            "position": "top",
            "animation": "fade-in"
        }
    })

    # Group words into 1-3 word phrases
    all_words = []
    for segment in data.get('segments', []):
        for word_info in segment.get('words', []):
            all_words.append(word_info)

    i = 0
    while i < len(all_words):
        # Group 2-3 words depending on length and timing
        group_size = 2
        if i + 2 < len(all_words):
            # If next word is very short or part of a small phrase, maybe 3
            if len(all_words[i]['word']) + len(all_words[i+1]['word']) + len(all_words[i+2]['word']) < 15:
                group_size = 3
        
        group = all_words[i:i+group_size]
        text = " ".join([w['word'].strip() for w in group])
        start_time = group[0]['start']
        end_time = group[-1]['end']
        
        # Ensure there's a gap or overlapping? Usually captions are back-to-back
        # But we want them to show exactly when spoken
        
        layers.append({
            "type": "text",
            "content": text,
            "startFrame": math.floor(start_time * fps),
            "endFrame": math.ceil(end_time * fps),
            "props": {
                "color": "#FFFFFF",
                "position": "bottom",
                "animation": "slide-up"
            }
        })
        
        i += group_size

    # Add a hook notification if needed (first 3 seconds)
    layers.append({
        "type": "notification",
        "content": "Most fitness coaches waste 3 hours on content", # Placeholder or inferred?
        "startFrame": 0,
        "endFrame": 60, # 2 seconds
        "props": {
            "position": "center",
            "animation": "pop",
            "color": "#000000"
        }
    })

    remotion_props = {
        "slug": "reproduction-video",
        "durationInSeconds": total_duration,
        "layers": layers
    }
    
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(remotion_props, f, indent=2)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python convert_whisper_to_remotion.py input.json output.json")
    else:
        convert_whisper_to_remotion(sys.argv[1], sys.argv[2])
