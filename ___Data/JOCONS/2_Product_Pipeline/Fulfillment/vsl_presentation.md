---
tags:
  - consulting
---
# VSL Presentation Workflow

## Objective
Take client's completed VSL Presentation Form, generate a copywriting draft (1 main point per slide = many slides), then design eye-catching visuals after client approves the copy.

## Required Inputs
- Completed VSL Presentation Form (`Fulfillment/_OFFER_BLUEPRINT/vsl_presentation_form.md`)
- Client swipe file (if available)
- Client's brand colors + font preference

## The 3-Step Process

### Step 1: Generate Copywriting Draft

**Claude prompt:**
```
Read the completed VSL Presentation Form for {CLIENT_NAME}: [PASTE FORM ANSWERS]
Also read their swipe file: [REFERENCE]

Generate a VSL presentation script with these rules:
- EACH SLIDE has exactly 1 main point
- A single sentence can be its own slide
- Short, punchy, scroll-stopping text
- Viewer should feel momentum — each slide pulls them to the next
- Mix text sizes: some slides are 1 big word, some are 1 short sentence
- Total: 40-80 slides (more is better — fast pacing keeps attention)

Slide structure:
1. HOOK (slides 1-5): Pattern interrupt, call out avatar's pain
2. AGITATE (slides 6-12): Make the pain vivid, show failed alternatives
3. STORY (slides 13-22): Client's origin story, turning point
4. MECHANISM (slides 23-32): Unique method, 3-5 steps
5. PROOF (slides 33-42): Testimonials, numbers, transformations
6. OFFER (slides 43-55): Deliverables, bonuses, guarantee
7. CTA (slides 56-60+): What to do next, urgency

For each slide output:
- Slide number
- Text (1 main point only)
- Visual direction (what the background should convey)
- Text size: BIG / MEDIUM / SMALL

Output in Indonesian (match client's tone from form).
```

**Output:** Save to `Fulfillment/_CLIENT_DELIVERABLES/{client_name}/vsl_presentation_draft.md`

| Task | Input Tokens | Output Tokens |
|---|---|---|
| VSL presentation draft (40-80 slides) | ~8,000 | ~10,000 |

### Step 2: Client Review & Approval

- Share draft with client
- Client marks: approve / edit / remove per slide
- Iterate if needed (usually 1-2 rounds)

### Step 3: Design Visuals

**After copy is approved, design in Canva / PowerPoint:**

**Design principles:**
- 1 main point per slide — NO information overload
- Large text, high contrast
- Brand colors from `graphics/color_palette.md`
- Alternate between:
  - Text-only slides (bold statement on solid color)
  - Text + background image (client photo / b-roll)
  - Data slides (single number, big font)
  - Testimonial slides (screenshot + highlight)
- Pacing: viewer should spend 2-4 seconds per slide max
- Transitions: simple cuts or subtle slides (no fancy animations)

**Visual hierarchy per slide type:**

| Slide Type | Background | Text Treatment |
|---|---|---|
| Hook | Dark, dramatic | BIG white text, centered |
| Pain point | Muted, desaturated | Medium text, left-aligned |
| Story | Personal photo of client | Text overlay with semi-transparent bar |
| Mechanism step | Clean, light background | Step number (BIG) + description (SMALL) |
| Testimonial | Screenshot of DM/review | Highlight key phrase in brand color |
| Offer item | Brand color background | Icon + deliverable name |
| Bonus | Gold/accent color | "BONUS" tag + item |
| Guarantee | Green background | Shield icon + guarantee text |
| CTA | Brand primary color | BIG CTA text + arrow |

**Output:** Export as:
1. PDF (for Wistia / screen recording)
2. Individual PNGs (for Remotion / video assembly)
3. Canva share link (for client access)

Save to: `Fulfillment/_CLIENT_DELIVERABLES/{client_name}/vsl_presentation/`

## Edge Cases
- **Client gives short answers:** Ask follow-up questions before generating. Weak input = weak slides.
- **Too many slides:** Better to have 80 fast slides than 30 slow ones. Pacing > length.
- **Client wants to record themselves presenting:** Generate teleprompter version alongside slides.
- **Client has no photos:** Use AI asset photos (nanobabaabba pro) or stock with brand color overlay.

## Example Slide Sequence (first 15 slides)

```
Slide 1:  [BIG] "Lo tau gak..."
Slide 2:  [BIG] "90% coach gagal scale"
Slide 3:  [MEDIUM] "Bukan karena gak jago"
Slide 4:  [BIG] "Tapi karena gak punya SISTEM"
Slide 5:  [SMALL] "Dan lo mungkin salah satunya"
Slide 6:  [MEDIUM] "Lo udah coba posting tiap hari"
Slide 7:  [MEDIUM] "Udah beli course mahal"
Slide 8:  [MEDIUM] "Udah hire freelancer"
Slide 9:  [BIG] "Tapi hasilnya?"
Slide 10: [BIG] "Masih stuck di 5 klien"
Slide 11: [SMALL] "Gue tau karena gue pernah di situ"
Slide 12: [BIG] "Nama gue {CLIENT_NAME}"
Slide 13: [MEDIUM] "Dan 2 tahun lalu gue hampir quit"
Slide 14: [MEDIUM] "{TURNING_POINT_STORY}"
Slide 15: [BIG] "Sampai gue nemuin 1 hal..."
```
