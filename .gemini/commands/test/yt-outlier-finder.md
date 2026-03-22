> **Model: Haiku / Tool** -- tool runner; Haiku generates summaries inside the tool

# Workflow: Cross-Niche Outlier Finder

**Tool:** `VLT_Content/AI_ENGINE/yt_tools/yt_outlier_finder.py`
**Trigger:** `/yt-outlier-finder`

## Inputs

| Input | Flag | Default |
|-------|------|---------|
| Channel handles | `--channels` | required |
| Your niche | `--niche` | "business and productivity" |
| Lookback | `--days` | 30 |
| Results | `--top` | 10 |
| Min score | `--min-score` | 1.5 |
| Sheet ID | `--sheets-id` | optional |

## Outlier Score Formula
```
Score = (video_views / channel_avg_views) x recency_boost x hook_modifier
recency_boost: 1.5 (today) -> 1.0 (edge of window)
hook_modifier: x1.30 money keywords | x1.20 time keywords
```

## Example Invocations

```bash
py -3 VLT_Content/AI_ENGINE/yt_tools/yt_outlier_finder.py   --channels "@mkbhd,@aliabdaal" --niche "AI tools for business" --days 30 --top 10

py -3 VLT_Content/AI_ENGINE/yt_tools/yt_outlier_finder.py   --channels "@thefutur,@garyvee" --niche "social media for coaches"   --days 30 --sheets-id "YOUR_SHEET_ID"

# Skip AI titles (faster):
py -3 VLT_Content/AI_ENGINE/yt_tools/yt_outlier_finder.py   --channels "@hubermanlab" --niche "health" --no-ai
```

## Outputs
- Full results: `.tmp/outlier_results.json`
- Google Sheet (if `--sheets-id` set)
- Terminal: score + original title + AI title

## Common Errors
| scrapetube error | try handle with/without @ |
| No outliers found | lower --min-score or increase --days |

Run from **Cook/ root directory**.
