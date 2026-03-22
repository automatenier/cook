"""
batch_proof_images.py
---------------------
Reads Authority_Proof_Planner.csv and generates story images for every row
that has a Photo_Path filled in.

Usage:
    py -3 AI_Tools/batch_proof_images.py

Outputs to:
    VLT_Content/04_HMN_OUTPUTS/jocons/authority_proof/
    e.g.  01_Candid_Balcony_Street.jpg

Fill in the Photo_Path column in the CSV (absolute or relative path to your photo)
then re-run. Rows with an empty Photo_Path are skipped and listed at the end.
"""

import csv
import os
import re
import sys
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────
ROOT    = Path(__file__).parent.parent
CSV     = ROOT / "01 HMN__Command/00_CONTENT/Authority_Proof_Planner.csv"
OUT_DIR = ROOT / "VLT_Content/04_HMN_OUTPUTS/jocons/authority_proof"

# ── Import the existing tool ────────────────────────────────────────────────
sys.path.insert(0, str(ROOT / "AI_Tools"))
from content_template_proof_image import create_proof_image


def slugify(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", text).strip("_")


def main():
    if not CSV.exists():
        print(f"CSV not found: {CSV}")
        sys.exit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with open(CSV, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    done, skipped = [], []

    for row in rows:
        photo = row.get("Photo_Path", "").strip()
        row_id = row.get("ID", "?").strip()
        visual = row.get("Visual_Type", "").strip()

        if not photo:
            skipped.append(f"  Row {row_id} ({visual}) — no photo path")
            continue

        photo_path = Path(photo) if Path(photo).is_absolute() else ROOT / photo
        if not photo_path.exists():
            skipped.append(f"  Row {row_id} ({visual}) — file not found: {photo_path}")
            continue

        out_name = f"{int(row_id):02d}_{slugify(visual)}.jpg"
        out_path = OUT_DIR / out_name

        create_proof_image(
            input_path  = str(photo_path),
            output_path = str(out_path),
            hook        = row["Hook"],
            mechanism   = row["Mechanism"],
            proof       = row["Proof"],
        )
        done.append(f"  {out_name}")

    print(f"\nGenerated: {len(done)}/{len(rows)}")
    for d in done:
        print(d)

    if skipped:
        print(f"\nSkipped ({len(skipped)}) — fill Photo_Path in the CSV to include:")
        for s in skipped:
            print(s)

    print(f"\nOutput folder: {OUT_DIR}")


if __name__ == "__main__":
    main()
