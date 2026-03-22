---
description: Scrapes YouTube channels, calculates Outlier Score (views / channel avg × recency × hook modifiers), fetches transcripts, summarises with Claude Haiku, and outputs to Google Sheets or .tmp/outlier_results.json.
tags:
  - workflow
  - youtube
  - research
  - content-strategy
---

# Workflow: Cross-Niche Outlier Finder

**Tool:** `VLT_VLT_Content/AI_ENGINE/yt_tools/yt_outlier_finder.py`
**Trigger:** `/yt-outlier-finder`

---

## Inputs Required

| Input | Flag | Default |
|-------|------|---------|
| Channel handles | `--channels` | required |
| Your niche | `--niche` | `"business and productivity"` |
| Lookback window | `--days` | `30` |
| Number of top results | `--top` | `10` |
| Min outlier score | `--min-score` | `1.5` |
| Google Sheet ID | `--sheets-id` | optional |

---

## Outlier Score Formula

```
Score = (video_views / channel_avg_views) × recency_boost × hook_modifier

recency_boost: 1.5 (published today) → 1.0 (at edge of window)
hook_modifier: ×1.30 if title contains money keywords
               ×1.20 if title contains time keywords
               (stack both if applicable → ×1.56 max)

Example: 500K views on a 100K-avg channel, published 5 days ago, money hook
  = (500K / 100K) × 1.42 × 1.30 = 9.2× outlier score
```

---

## API Modes

| Condition | Behaviour |
|-----------|-----------|
| `YOUTUBE_API_KEY` set in `.env` | Uses YouTube Data API v3 (exact view counts, precise dates) |
| No `YOUTUBE_API_KEY` | Uses `scrapetube` for listing + parses view text ("1.2M views") — no API key needed |
| `ANTHROPIC_API_KEY` set | Claude Haiku generates 2-sentence summary + 3 adapted titles per outlier |
| `GOOGLE_SERVICE_ACCOUNT_JSON` set | Writes results to Google Sheet |
| Always | Saves full results to `.tmp/outlier_results.json` |

---

## Prerequisites

```bash
pip install -r VLT_VLT_Content/AI_ENGINE/yt_tools/requirements_yt.txt
```

For Google Sheets output, set in `.env`:
```
GOOGLE_SERVICE_ACCOUNT_JSON=/path/to/service-account.json
```

---

## Example Invocations

**Quick scan (no API keys needed):**
```bash
py -3 VLT_VLT_Content/AI_ENGINE/yt_tools/yt_outlier_finder.py \
  --channels "@mkbhd,@aliabdaal,@grahamstephan" \
  --niche "AI tools for business" \
  --days 30 \
  --top 10 \
  --min-score 2.0
```

**Full pipeline with Sheets output:**
```bash
py -3 VLT_VLT_Content/AI_ENGINE/yt_tools/yt_outlier_finder.py \
  --channels "@thefutur,@garyvee,@patrickbetdavid" \
  --niche "social media marketing for coaches" \
  --days 30 \
  --top 15 \
  --sheets-id "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgVE2upms"
```

**Skip AI titles (faster scan):**
```bash
py -3 VLT_VLT_Content/AI_ENGINE/yt_tools/yt_outlier_finder.py \
  --channels "@hubermanlab,@lexfridman" \
  --niche "health and performance" \
  --no-ai
```

---

## Outputs

| Output | Location |
|--------|----------|
| Full results JSON | `.tmp/outlier_results.json` |
| Google Sheet rows | Sheet specified by `--sheets-id` |
| Terminal summary | Printed — score + original title + first AI title |

Google Sheet columns:
`Channel | Title | Video ID | Views | Outlier Score | Thumbnail URL | Summary | AI Title 1 | AI Title 2 | AI Title 3`

---

## Choosing Target Channels

For cross-niche research, pick channels that:
- Cover adjacent topics (your audience overlaps, but they're not direct competitors)
- Have consistent posting (weekly or more)
- Have 50K–5M subscribers (mass-market formats without hyper-niche audiences)

Example niches to scan for a fitness coaching channel:
- Business / entrepreneur: `@garyvee,@alexhormozi,@grahamstephan`
- Productivity / self-dev: `@aliabdaal,@thomasfrank`
- Health adjacent: `@hubermanlab,@peterattiamd`

---

## Common Errors

| Error | Fix |
|-------|-----|
| `scrapetube error` | The channel handle may be wrong — try with or without `@` |
| `No outliers found` | Lower `--min-score` or increase `--days` |
| `Claude error: json decode` | Retry — Haiku occasionally returns malformed JSON |
| Sheets write fails | Check `GOOGLE_SERVICE_ACCOUNT_JSON` is set and the sheet is shared with the service account |

---

## Notes

- Run from the **Cook/ root directory**.
- Transcript availability varies by channel — some disable transcripts. `(transcript unavailable)` is expected for ~20% of videos.
- The scrapetube "recency" fallback uses relative time text ("3 weeks ago") which is approximate ±2 days.
- For highest accuracy, get a free YouTube Data API v3 key from Google Cloud Console and add `YOUTUBE_API_KEY` to `.env`.
