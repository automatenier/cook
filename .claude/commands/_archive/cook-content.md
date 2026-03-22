---
tags:
  - claude-config
---
Run full content production for a client. Arguments: $ARGUMENTS
Parse as: first word = client name, second word = month (e.g. month_01, month_02).

Do not ask for confirmation between steps.

---

**STEP 1 — Load client context**

Read `VLT_Content/clients/[nama]/client_brief.md` — niche, ICP, offer, tone, brand voice.
Check `VLT_Content/library/` for hook bank and CTA templates if they exist.
Check `VLT_Content/Z Swipe Files/` for relevant swipe structures.

**STEP 2 — Generate 30 Reel scripts**

- 15 Authentic/story-based
- 15 Value/CTA-based
Save each to `VLT_Content/clients/[nama]/projects/[month]/scripts/reel_[01-30].md`
Format per script: Hook | Body (3 points max) | CTA

**STEP 3 — Generate 30 Story sequences**

Each = 3–5 slides: Hook slide → Body → Poll/Question → CTA
Save to `VLT_Content/clients/[nama]/projects/[month]/scripts/stories_[01-30].md`

**STEP 4 — Generate 30 Threads posts**

Mix: thread opener, single insight, hot take, poll
Save to `VLT_Content/clients/[nama]/projects/[month]/scripts/threads_[01-30].md`

**STEP 5 — Generate 4 YouTube scripts**

Long-form (8–12 min). Format: Hook → Context → 3–5 Main Points → Outro + CTA
Save to `VLT_Content/clients/[nama]/projects/[month]/scripts/youtube_[01-04].md`

**STEP 6 — Run repurpose tool**

Execute `tools/repurpose_content.py` for the 30 reels.
Each reel → Instagram caption, TikTok caption, Threads thread, LinkedIn post.
Output to `VLT_Content/clients/[nama]/projects/[month]/repurposed/`

**STEP 7 — Content audit (if client has existing content)**

If client brief includes an IG handle, score existing content:
- Hook strength (1–10), CTA clarity (1–10), ICP alignment (1–10), Engagement bait (1–10)
Output to `Z Products/Fulfillment/_CONTENT_AUDIT/client_audits/[nama]/[month]_audit.md`

**STEP 8 — Generate Jordan's review file**

Write `VLT_Content/clients/[nama]/projects/[month]/REVIEW_[month].md` with:
- Top 5 reels to review (best hooks — list reel numbers)
- 2 scripts that need Jordan's personal tone adjusted
- Any brand voice flags
- Approval instructions (one-line)

**STEP 9 — Update checklist**

In `A Human Workflow/A Manager/_clients/[nama]_checklist.md`, mark `[x]`:
- 30 Reel scripts di-generate
- Story/Threads/YT scripts di-generate
- Repurpose complete
- Content audit done (if applicable)

**STEP 10 — Tell Jordan**

Output: "Content batch for [NAMA] [MONTH] ready. Open `VLT_Content/clients/[nama]/projects/[month]/REVIEW_[month].md` — 10 minutes to review. Reply 'Batch approved for [NAMA]' or give feedback by reel number."
