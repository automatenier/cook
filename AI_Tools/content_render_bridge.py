import json
import os
import pandas as pd
import argparse

# Paths
FOOTAGE_LIB = "VLT_Content/AI_BRAIN/Shared Assets/footage_library.csv" # Adjusted based on typical structure
RENDER_PROPS = "VLT_Content/AI_ENGINE/render_props.json"

def verify_assets(storyboard_df, footage_root):
    """Checks if all files in the 'Video Content' column exist."""
    missing = []
    for asset in storyboard_df['Video Content'].dropna():
        asset_path = os.path.join(footage_root, asset)
        if not os.path.exists(asset_path):
            missing.append(asset)
    return missing

def generate_props(csv_path, footage_root, output_path):
    df = pd.read_csv(csv_path)
    
    # 1. Verify Assets
    missing = verify_assets(df, footage_root)
    if missing:
        print(f"❌ ERROR: Missing assets found: {missing}")
        return False

    # 2. Build Props
    props = {
        "project": os.path.basename(csv_path),
        "timeline": []
    }
    
    for _, row in df.iterrows():
        item = {
            "order": row['Order'],
            "video": row['Video Content'],
            "audio": row['Background Audio'] if pd.notna(row['Background Audio']) else None,
            "sfx": row['Sound Effect'] if pd.notna(row['Sound Effect']) else None,
            "notes": row['Notes'] if pd.notna(row['Notes']) else ""
        }
        props["timeline"].append(item)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(props, f, indent=2)
    
    print(f"✅ SUCCESS: Props generated at {output_path}")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    parser.add_argument("--root", required=True)
    args = parser.parse_args()
    
    generate_props(args.csv, args.root, RENDER_PROPS)
