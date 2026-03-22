
import argparse
import json
import os
import sys
import shutil
from pathlib import Path
from dotenv import load_dotenv

def get_gemini_client():
    try:
        from google import genai
    except ImportError:
        print("Error: google-genai not installed. Run: pip install google-genai")
        sys.exit(1)
    
    # Try to find .env in root
    env_path = Path(__file__).parent.parent / ".env"
    load_dotenv(env_path)
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not set in .env")
        sys.exit(1)
        
    return genai.Client(api_key=api_key)

def approve_all(client_name):
    """Move all scripts from scripts/ to approved/ for a specific client."""
    workspace = Path("VLT_Content/02_HMN_HUMANFLOW")
    client_paths = list(workspace.glob(f"**/{client_name}/projects/*/scripts"))
    
    if not client_paths:
        print(f"Error: No project folders found for client '{client_name}'")
        return

    count = 0
    for script_dir in client_paths:
        approved_dir = script_dir.parent / "approved"
        approved_dir.mkdir(exist_ok=True)
        
        for script in script_dir.glob("*.md"):
            dest = approved_dir / script.name
            shutil.move(str(script), str(dest))
            print(f"  Approved: {script.name} -> {approved_dir.name}/")
            count += 1
            
    print(f"\nSuccessfully approved {count} scripts for {client_name}.")

def review_script(script_path: Path, checklist_path: Path):
    client = get_gemini_client()
    
    script_content = script_path.read_text(encoding="utf-8")
    checklist_content = checklist_path.read_text(encoding="utf-8")

    prompt = f"""
You are an expert Short-Form Content Strategist. Your task is to review a video script based on a specific Viral Checklist.

### VIRAL CHECKLIST ###
{checklist_content}

### SCRIPT TO REVIEW ###
{script_content}

### INSTRUCTIONS ###
1. Review the script strictly against the 3 gates in the checklist.
2. Provide a score from 0-10 for each gate.
3. Provide an overall "Viral Score" (0-10).
4. Give specific, actionable suggestions for improvement.
5. Identify if the script is ready for production (Score > 8).

Return the response as a valid JSON object with the following structure:
{{
  "gate_1_hook": {{"score": 0, "feedback": ""}},
  "gate_2_body": {{"score": 0, "feedback": ""}},
  "gate_3_cta": {{"score": 0, "feedback": ""}},
  "overall_viral_score": 0,
  "is_production_ready": false,
  "suggestions": [],
  "shareability_check": ""
}}
Return ONLY the JSON.
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt],
    )

    raw = response.text.strip()
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1]
        if "```" in raw:
            raw = raw.rsplit("```", 1)[0]

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        print(f"Error decoding JSON from Gemini: {raw}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Review or Approve content scripts")
    parser.add_argument("script", nargs="?", help="Path to the .md script file")
    parser.add_argument("--approve-all", help="Approve all scripts for this client", metavar="CLIENT_NAME")
    parser.add_argument("--checklist", help="Path to the checklist file", default="VLT_Content/AI_BRAIN/HMN_Guide/viral_checklist.md")
    parser.add_argument("--output", "-o", help="Output JSON path")
    args = parser.parse_args()

    if args.approve_all:
        approve_all(args.approve_all)
        return

    if not args.script:
        parser.print_help()
        sys.exit(1)

    script_path = Path(args.script)
    checklist_path = Path(args.checklist)

    if not script_path.exists():
        print(f"Error: Script file not found: {args.script}")
        sys.exit(1)
    if not checklist_path.exists():
        print(f"Error: Checklist file not found: {args.checklist}")
        sys.exit(1)

    print(f"Reviewing script: {script_path.name}...")
    review = review_script(script_path, checklist_path)

    # Save output
    if args.output:
        out_path = Path(args.output)
    else:
        # Default to VLT_Content/03_HMN_REVIEW/scripts_reviewed/[script_name]_review.json        
        out_path = Path("VLT_Content/03_HMN_REVIEW/scripts_reviewed") / f"{script_path.stem}_review.json"

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(review, indent=2), encoding="utf-8")
    
    print(f"\n--- REVIEW SUMMARY: {script_path.name} ---")
    print(f"Overall Viral Score: {review['overall_viral_score']}/10")
    print(f"Production Ready: {'YES' if review['is_production_ready'] else 'NO'}")       
    print(f"\nGate 1 (Hook): {review['gate_1_hook']['score']}/10")
    print(f"  {review['gate_1_hook']['feedback']}")
    print(f"\nGate 2 (Body): {review['gate_2_body']['score']}/10")
    print(f"  {review['gate_2_body']['feedback']}")
    print(f"\nGate 3 (CTA): {review['gate_3_cta']['score']}/10")
    print(f"  {review['gate_3_cta']['feedback']}")

    print("\nSuggestions:")
    for s in review['suggestions']:
        print(f"- {s}")

    print(f"\nFull review saved to: {out_path}")

if __name__ == "__main__":
    main()
