---
tags:
  - memory
---
# 14-Day Sprint — Delivery Architecture

> Reference this when executing any client sprint phase. Do not re-read the full worksheet unless you need the exact block.
> Full worksheet: `PDCT_JO_Consult/deliverables/Z Products/Client Worksheet/Client_X_Worksheet.md`

---

## Gating Rules (Do Not Skip)

Each day requires the prior day's COLLECT items before proceeding.

| Gate | Required before proceeding |
|------|---------------------------|
| Day 0 → Day 1 | Contracts signed + GDrive folder shared + community access granted + Telegram channel live |
| Day 1 → Day 2 | `onboarding.json` saved + all 4 client_info docs in GDrive + voice sample uploaded + brand assets uploaded |
| Day 2 → Day 3 | Offer sheet approved + swipe file approved |
| Day 3 → Day 4 | VSL script approved + ElevenLabs Voice ID collected |
| Day 4 → Day 5 | Funnel live at Netlify URL + Wistia IDs confirmed + calendar link working |
| Day 5 → Day 7 | Content audit complete + template matches done |
| Day 7 → Day 8 | Content calendar approved by client |
| Day 8 → Day 9 | Remotion props batch saved + IG/TikTok keyword CTA pairs approved |
| Day 9 → Day 10 | TikTok mirrors uploaded confirmed |
| Day 10 → Day 12 | Lead list received + DFY asset inputs collected (food prefs, cooking time, family situation, top 5 restaurants, travel frequency) |
| Day 12 → Day 13 | Reactivation batch sent + first results logged |

---

## What Agents Generate Per Phase

| Day | Output | Method |
|-----|--------|--------|
| 0 | Welcome email, asset collection message, folder structure | Inline — templates in `_ONBOARDING/` |
| 2 | Offer sheet, swipe file, content angles, sales call script, 7-email nurture, ad copy (3 platforms), 5 bonuses, transformation roadmap | `offer_agent.py` + inline |
| 3 | VSL script (teleprompter format), Netlify funnel HTML (placeholder Wistia IDs) | Inline |
| 4 | Filming shot list, finalized funnel HTML (real Wistia IDs), test checklist | Inline |
| 5 | Content audit report (20 posts scored), template matches to client ICP | Inline |
| 7 | 4-week content calendar, 30 reel scripts (15 Authentic + 15 Value-CTA), 30 story sequences, 30 Threads posts, 4 YouTube scripts, VO scripts (ElevenLabs format), 30 TikTok mirror captions | Inline |
| 8 | Remotion JSON props (batch 30), IG keyword CTA pairs (8–12), TikTok CTA setup | Inline |
| 9 | 150+ repurposed pieces, IG captions + hashtags (30), Meta Ads setup + creatives | `repurpose_content.py` + inline |
| 10 | Lead segments (Hot/Warm/Cold), reactivation scripts (3 channels × 3 variants), DM closing playbook, lead magnet content (title + full content + landing copy + 3 follow-up emails), 4 DFY assets (shopping list, 7-day meal plan, restaurant guide, travel protocol), Notion workspace home | Inline |
| 12 | 4 team SOPs (Creative Director, Editor, Setter, Closer), 6 setter DM script docs | Inline |
| 13 | Day 14 consultation prep brief, pre-call verification checklist | Inline |
| 15 | Command center Google Sheet template (6 tabs with formulas) | Inline |

---

## Output File Paths (Per Client)

All outputs save to `PDCT_JO_Consult/deliverables/Z Products/Fulfillment/_CLIENT_DELIVERABLES/[CLIENT]/`:

```
[CLIENT]/
├── client_info/           ← life_story, PMF, offer_positioning, produk (client fills)
├── swipe_file.md          ← Day 2
├── content_angles.md      ← Day 2
├── offer_sheet.md + .json ← Day 2
├── sales_call_script.md   ← Day 2
├── email_sequence.md      ← Day 2
├── ad_copy.md             ← Day 2
├── bonuses/               ← Day 2 (bonus_1.md → bonus_5.md + summary)
├── roadmap.md             ← Day 2
├── vsl_script.md          ← Day 3
├── funnel/index.html      ← Day 3 draft → Day 4 final
├── filming_brief.md       ← Day 4
├── voice_clone/           ← ElevenLabs samples + generated audio
├── content_calendar/      ← Day 7
├── scripts/               ← All script batches
├── remotion_props/        ← Day 8 JSON props
├── dm_scripts/            ← CTAs, reactivation, setter scripts, DM playbook
├── lead_magnet/           ← Lead magnet content + DFY assets + Notion workspace
├── analytics/             ← Meta Ads setup, command center template
└── day14_prep_brief.md    ← Day 13
```

---

## Monthly Cadence (Post Day 14)

```
MONDAY      Generate: 8 reel scripts + 8 story sequences + 7-8 Threads posts + VO scripts + TikTok captions
            Jordan: review + approve

TUESDAY     Render Remotion → ElevenLabs VO → CapCut polish → dual export (IG + TikTok)
WEDNESDAY   CapCut continued → final review → schedule IG + TikTok
THURSDAY    YT script → CapCut YT edit → Threads scheduled
FRIDAY      Posting schedule + IG captions + repurpose batch (via tool)

DAILY       n8n: auto Telegram check-in to client
SUNDAY      n8n: weekly progress summary to client

BI-WEEKLY   Lead reactivation refresh + swipe file update
MONTHLY     Performance analysis + funnel update + ad refresh + strategy call
```

---

## Client Health Check (Run Before Every Weekly Call)

- Posting consistently (3–4 reels/week)?
- Setter hitting DM KPIs (1+ booking/day)?
- Leads converting to calls?
- Content quality improving week-over-week?
- Client responsive and engaged?
- Funnel converting (VSL watch rate, calendar bookings)?
- Renewal / upsell conversation needed?
