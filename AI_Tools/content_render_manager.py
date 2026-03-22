#!/usr/bin/env python3
"""
Render Manager — Unified interface for Remotion video rendering.

Handles batch rendering (Modal cloud or Local), individual script rendering, 
and progress tracking.

Commands:
    py -3 AI_Tools/render_manager.py --client fadli --modal
    py -3 AI_Tools/render_manager.py --client fadli --local
    py -3 AI_Tools/render_manager.py --client fadli --status
    py -3 AI_Tools/render_manager.py --all --modal
"""

import os
import sys
import json
import argparse
import asyncio
import re
import subprocess
from pathlib import Path

# --- Configuration ---
ROOT = Path(__file__).parent.parent
OUTPUTS_DIR = ROOT / "Content" / "04_OUTPUTS"
REMOTION_DIR = ROOT / "Content" / "40_ENGINE" / "remotion"

CLIENTS = {
    "fadli": {
        "workspace": ROOT / "VLT_Content/02_HMN_HUMANFLOW/jocons/fadli",
        "output_dir": "fadli",
        "color": "#FF6B6B",
    },
    "mathew_jordan": {
        "workspace": ROOT / "VLT_Content/02_HMN_HUMANFLOW/jocons/Mathew_Jordan",      
        "output_dir": "Mathew_Jordan", 
        "color": "#FFB347",
    },
    "ruth": {
        "workspace": ROOT / "VLT_Content/02_HMN_HUMANFLOW/jocons/ruth",
        "output_dir": "ruth",
        "color": "#74B9FF",
    },
    "real_estate": {
        "workspace": ROOT / "VLT_Content/02_HMN_HUMANFLOW/real_estate",
        "output_dir": "real_estate",   
        "color": "#2ECC71",
    },
}

COMPOSITION_MAP = {
    "story": "AuthenticityReel",       
    "bts": "AuthenticityReel",
}

# --- Parsing & Logic ---

def get_composition(script_type: str) -> str:
    t = script_type.lower()
    for kw, comp in COMPOSITION_MAP.items():
        if kw in t: return comp
    return "ValueCTAReel"

def parse_script(path: Path):
    text = path.read_text(encoding='utf-8')
    fm, sections, in_fm, current = {}, {}, False, None
    for i, line in enumerate(text.split('\n')):
        if i == 0 and line.strip() == '---':
            in_fm = True
            continue
        if in_fm:
            if line.strip() == '---': in_fm = False; continue
            if ':' in line:
                k, v = line.split(':', 1)
                fm[k.strip()] = v.strip()
            continue
        if line.startswith('#### '):
            current = line[5:].strip().lower()
            sections[current] = []
        elif current and line.strip():
            sections[current].append(line.strip())
    return fm, {k: '\n'.join(v) for k, v in sections.items()}

def build_props(fm, sections, composition, brand_color):
    hook = re.sub(r'\[[\w\s]+\]', '', sections.get('hook', '')).strip()
    if composition == 'ValueCTAReel':
        value = re.sub(r'\[[\w\s]+\]', '', sections.get('value', sections.get('body', ''))).strip()
        cta_raw = sections.get('cta', '')
        cta_clean = re.sub(r'\[[\w\s]+\]', '', cta_raw).strip()
        m = re.search(r'\*\*([A-Z]+)\*\*', cta_raw)
        return {
            'hookText': hook[:150], 'valueText': value[:300], 
            'ctaText': cta_clean[:200], 'ctaKeyword': m.group(1) if m else "DM",
            'brandColor': brand_color
        }
    else:
        story = re.sub(r'\[[\w\s]+\]', '', sections.get('value', sections.get('story', sections.get('body', '')))).strip()
        lines = [l for l in story.split('\n') if l.strip()]
        return {
            'hookText': hook[:150], 'storyText': story[:300], 
            'lessonText': lines[-1] if lines else story[:100],
            'brandColor': brand_color
        }

# --- Actions ---

def show_status(client_key):
    if client_key not in CLIENTS:
        print(f"Unknown client: {client_key}")
        return
    cfg = CLIENTS[client_key]
    out_dir = OUTPUTS_DIR / cfg['output_dir']
    approved = list(cfg['workspace'].glob("projects/*/approved/*.md"))
    rendered = list(out_dir.glob("*.mp4")) if out_dir.exists() else []
    
    print(f"--- Render Status: {client_key.upper()} ---")
    print(f"Approved: {len(approved)} | Rendered: {len(rendered)}")
    if approved:
        pct = (len(rendered)/len(approved))*100
        bar = '█' * int(pct//5) + '-' * (20 - int(pct//5))
        print(f"Progress: |{bar}| {pct:.1f}%")

async def render_modal(jobs):
    try:
        import modal
    except ImportError:
        print("modal not installed.")
        return
    render_fn = modal.Function.lookup("cook-tools", "render_remotion")
    async def one(job):
        fm, sections = parse_script(job['script'])
        comp = get_composition(fm.get('type', 'value'))
        props = build_props(fm, sections, comp, job['color'])
        job['out_path'].parent.mkdir(parents=True, exist_ok=True)
        try:
            mp4 = await render_fn.remote.aio(comp, props)
            job['out_path'].write_bytes(mp4)
            print(f"  ✓ {job['script'].name}")
            return True
        except Exception as e:
            print(f"  ✗ FAIL {job['script'].name}: {e}")
            return False
    await asyncio.gather(*[one(j) for j in jobs])

def render_local(jobs):
    npx = "npx.cmd" if os.name == "nt" else "npx"
    for job in jobs:
        fm, sections = parse_script(job['script'])
        comp = get_composition(fm.get('type', 'value'))
        props = build_props(fm, sections, comp, job['color'])
        job['out_path'].parent.mkdir(parents=True, exist_ok=True)
        print(f"Rendering {job['script'].name} locally...")
        cmd = [npx, "remotion", "render", "src/index.ts", comp, "--props", json.dumps(props), "--output", str(job['out_path']), "--overwrite"]
        subprocess.run(cmd, cwd=str(REMOTION_DIR), check=True, shell=(os.name=="nt"))

def main():
    parser = argparse.ArgumentParser(description="Cook Render Manager")
    parser.add_argument('--client', help='Client key')
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--modal', action='store_true', help='Render via Modal Cloud')
    parser.add_argument('--local', action='store_true', help='Render locally')
    parser.add_argument('--status', action='store_true', help='Show progress')
    parser.add_argument('--force', action='store_true', help='Overwrite existing')
    
    args = parser.parse_args()
    keys = list(CLIENTS.keys()) if args.all else ([args.client] if args.client else [])
    
    if args.status:
        for k in keys: show_status(k)
        return

    jobs = []
    for k in keys:
        if k not in CLIENTS: continue
        cfg = CLIENTS[k]
        scripts = list(cfg['workspace'].glob("projects/*/approved/*.md"))
        for s in scripts:
            out_path = OUTPUTS_DIR / cfg['output_dir'] / (s.stem + ".mp4")
            if out_path.exists() and not args.force: continue
            jobs.append({'script': s, 'out_path': out_path, 'color': cfg['color']})

    if not jobs:
        print("No scripts to render.")
        return

    if args.modal:
        asyncio.run(render_modal(jobs))
    elif args.local:
        render_local(jobs)

if __name__ == "__main__":
    main()
