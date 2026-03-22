---
tags:
  - consulting
---
# Content Creation Workflow

## Objective
Create content for JO Consult or clients using pre-analyzed viral structures, client-specific footage/assets, and agent-powered scripting + repurposing.

## Who Does What

| Role | Responsibility |
|------|---------------|
| **You** | Find viral refs, shoot footage, edit in CapCut, publish |
| **Gemini** | Analyze viral reel structures → JSON |
| **Agent (Claude)** | Write scripts using swipe file + client brief, repurpose content |
| **Remotion** | Render video drafts from footage + assets using brief filenames |

## Key Directories

| Directory | Purpose |
|-----------|---------|
| `content/swipe_file/` | Winning viral structures (Gemini-analyzed JSON) |
| `content/clients/[name]/` | Per-client: brief, footage checklist, a-roll, footage, assets, projects |
| `content/library/` | Hook bank, CTA bank, script templates |
| `content/strategy/` | Viral checklist, idea generation, bio setup |
| `content/assets_shared/` | Cross-client logos, fonts, LUTs, NanoBanana library |
| `remotion/src/` | Remotion video templates |

## Tools Used
- `tools/analyze_viral_reel.py` — Manual markdown analysis → JSON (optional: `--gemini` flag)
- `tools/repurpose_content.py` — Claude content repurposing
- Remotion (`remotion/` — ValueCTAReel + AuthenticityReel templates)
- CapCut (manual — your creative editing)
- NanoBanana (AI image generation for assets)

---

## Steps

### Step 1: Find Viral Reference

1. Find a reel/video that performs well in your niche
2. Download via Telegram → n8n → OneDrive pipeline
3. Save reference as: `content/swipe_file/[slug]_ref_01.mp4` (or in client project folder)

### Step 2: Analyze with Gemini

**Option A — Gemini (primary):**
- Run reel through Gemini for structural analysis
- Save output: `content/swipe_file/[slug]_[structure-type].json`
- Update the index: `content/swipe_file/_index.md`

**Option B — Manual:**
1. Print template: `python tools/analyze_viral_reel.py --template`
2. Watch reel, fill in `.md` template
3. Convert to JSON: `python tools/analyze_viral_reel.py notes.md`
4. Save to `content/swipe_file/`

### Step 3: Agent Writes the Brief

Tell Claude: "Create a reel for @[client] using swipe structure #[number]"

Agent reads:
- `content/swipe_file/[slug].json` — the viral structure
- `content/clients/[name]/client_brief.md` — brand, tone, offer, avatar
- `content/clients/[name]/footage_checklist.md` — what footage exists
- `content/library/hook_bank.md` — hook options
- `content/library/cta_bank.md` — CTA options
- `content/library/script_templates/[type].md` — structure template

Agent outputs:
- `content/clients/[name]/projects/[YYMMDD]_[slug]/brief.md`
- Brief includes **exact filenames** for each segment (which A-roll, which b-roll, which nano image)

### Step 4: Prepare Assets

Based on the brief:
1. **A-Roll** — already shot (one-time) → in `content/clients/[name]/a_roll/`
2. **Footage** — shoot new b-roll or screen recordings if needed → `content/clients/[name]/footage/`
3. **Graphics** — generate NanoBanana images, create overlays → `content/clients/[name]/assets/`
4. Project-specific assets → `content/clients/[name]/projects/[YYMMDD]_[slug]/`

### Step 5: Assemble in Remotion or CapCut

**Remotion route:**
1. `cd remotion && npm start`
2. Feed brief filenames as props to `ValueCTAReel` / `AuthenticityReel`
3. Preview and render

**CapCut route (your personal workflow in Obsidian):**
1. Open CapCut with the brief as your shot list
2. Import footage/assets using the exact filenames from the brief
3. Add: music, transitions, color grading, captions
4. Export to: `content/clients/[name]/projects/[YYMMDD]_[slug]/export/`

### Step 6: Repurpose with Agent

Tell Claude: "Repurpose the brief at content/clients/[name]/projects/[slug]/brief.md"

Or run:
```
python tools/repurpose_content.py content/clients/[name]/projects/[slug]/brief.md --type reel-value
```

Output: `content/clients/[name]/projects/[YYMMDD]_[slug]/repurposed.json`
- Threads post
- Newsletter email
- YouTube script outline
- TikTok caption
- 3-5 story slide scripts

### Step 7: Publish

- Instagram Reel → post with caption from repurposed.json
- TikTok → post with TikTok variant
- Threads → lead magnet version
- Stories → 3-5 slide sequence
- Newsletter → schedule via n8n
- YouTube → save outline for long-form day

---

## Filename Convention

```
[CLIENT]_[ASSET-TYPE]_[DESCRIPTOR]_[SEQ].[ext]
```

| Type | Category | Example |
|------|----------|---------|
| `aroll` | A-Roll (talking head) | `missmochi_aroll_cta-dm_01.mp4` |
| `broll` | B-roll video | `missmochi_broll_gym-training_01.mp4` |
| `screen` | Screen recording | `missmochi_screen_dashboard_01.mp4` |
| `testimonial` | Client testimonial | `missmochi_testimonial_sarah_01.mp4` |
| `nano` | NanoBanana AI image | `missmochi_nano_hook-busy-mom_01.png` |
| `overlay` | Graphic overlay | `missmochi_overlay_cta-free_01.png` |
| `thumb` | Thumbnail | `missmochi_thumb_steal-competitors_01.png` |
| `ref` | Reference reel | `missmochi_ref_steal-competitors_01.mp4` |
| `lut` | Color LUT | `warm-sunset_lut_01.cube` |

Full convention documented in: `content/README.md`

---

## Onboarding a New Client for Content

1. Copy `content/clients/_template/` → `content/clients/[client_name]/`
2. Fill out `client_brief.md` (brand, tone, offer, avatar)
3. Go through `footage_checklist.md` — schedule the one-time A-roll shoot
4. After shoot: drop clips into `a_roll/` with proper filenames
5. Start creating: "Create a reel for @[client] using swipe structure #[X]"

---

## Edge Cases
- If A-roll doesn't exist yet: agent notes it in the brief as `[NEEDS SHOOT]` and the brief becomes a shot list
- If Gemini analysis fails: check file format (MP4 works best), file size (<100MB), or do manual analysis
- If no swipe structure fits: agent writes from scratch using `content/library/script_templates/`
- If Claude repurposing feels off-voice: update `client_brief.md` with more voice examples and words they use
- If client changes appearance significantly: reshoot A-roll — note in footage_checklist.md

## Expected Output (per content piece)
- 1 brief with exact filenames per segment
- 1 finished reel (IG + TikTok)
- 1 Threads post
- 1 newsletter email
- 1 YouTube script outline
- 3-5 story slides
- All from ONE piece of content
