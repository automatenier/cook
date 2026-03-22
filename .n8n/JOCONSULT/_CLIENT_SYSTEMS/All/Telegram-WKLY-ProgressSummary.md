---
tags:
  - consulting
---
# Telegram-WKLY-ProgressSummary

> Auto-generates weekly scorecard for each client every Sunday night — content posted, engagement, leads, calls booked. Sent to client's Telegram channel.

---

## Trigger
- **Type:** Cron / Schedule
- **Time:** 20:00 WIB every Sunday

## Flow

```
Schedule (Sunday 20:00 WIB)
  → Google Sheets: Pull active client list
  → Loop Each Client:
      → Google Sheets: Pull this week's content tracker (posted/engagement)
      → Google Sheets: Pull this week's lead data (new leads, replies, bookings)
      → Google Sheets: Pull setter KPIs (DMs sent, convos, calls booked)
      → Anthropic (Claude Haiku): Generate weekly scorecard
      → Telegram: Send to client's private channel
```

## Nodes Detail

### 1. Schedule Trigger
```json
{
  "type": "n8n-nodes-base.scheduleTrigger",
  "parameters": {
    "rule": {
      "interval": [{ "field": "cronExpression", "expression": "0 20 * * 0" }]
    }
  }
}
```

### 2. Google Sheets — Pull Weekly Metrics
Pull from 3 sources per client:

**Content Tracker:**
- Posts published this week (count per platform)
- Total engagement (likes, comments, saves, shares)
- Best performing post (highest engagement)

**Lead Tracker:**
- New leads this week
- Reply rate on reactivation messages
- Calls booked

**Setter KPIs:**
- DMs sent
- New ICPs discovered
- Conversations advanced
- Show rate

### 3. Anthropic (Claude Haiku) — Generate Scorecard
- **Model:** claude-haiku-4-5-20251001
- **System prompt:**
```
Kamu adalah performance analyst untuk coaching business.
Buat weekly scorecard yang jelas dan motivating.
Bahasa: Indonesian professional tapi friendly.
Gunakan emoji untuk status indicators: 🟢 on track, 🟡 needs attention, 🔴 behind.
Format: clean Telegram markdown.
```
- **User prompt:**
```
Client: {client_name}
Week: {week_start} — {week_end}

CONTENT:
- Posts published: {count} / {target}
- Total engagement: {engagement}
- Best post: "{best_post_topic}" — {best_post_engagement}
- Platforms: IG {ig_count}, TikTok {tt_count}, Threads {threads_count}, YT {yt_count}

LEADS:
- New leads: {new_leads}
- Reactivation replies: {reactivation_replies} / {reactivation_sent}
- Calls booked: {calls_booked}
- Show rate: {show_rate}%

SETTER:
- DMs sent: {dms_sent}
- New ICPs: {new_icps}
- Conversations active: {active_convos}

Generate a weekly scorecard with:
1. Performance summary (3 bullet points)
2. Metric table with 🟢🟡🔴 indicators
3. Top win of the week
4. 1 focus area for next week
5. Motivational close
```

### 4. Telegram — Send Scorecard
- **Chat ID:** `{client_telegram_chat_id}`
- **Parse mode:** Markdown

## Example Output

```
📊 Weekly Report — {CLIENT NAME}
📅 10 Feb — 16 Feb 2026

HIGHLIGHTS:
• 8 reels posted across IG + TikTok 🟢
• 3 new leads from keyword CTA 🟢
• 1 call booked (target: 2) 🟡

━━━━━━━━━━━━━━━━━━━━━

| Metric           | Actual | Target | Status |
|------------------|--------|--------|--------|
| Content posted   |     8  |     8  |   🟢   |
| Engagement rate  |  3.2%  |    3%  |   🟢   |
| New leads        |     3  |     4  |   🟡   |
| Calls booked     |     1  |     2  |   🟡   |
| Show rate        |  100%  |   80%  |   🟢   |
| DMs sent         |    45  |    50  |   🟡   |

━━━━━━━━━━━━━━━━━━━━━

🏆 Win of the week:
Reel "3 Kesalahan Diet" dapet 2.4K views — highest ever!

🎯 Focus minggu depan:
Boost DM outreach — target 10-15 new DMs/day biar leads naik.

Keep pushing! Konsistensi lo udah keliatan hasilnya 🔥
```

## Token Budget
- ~2,000 input / ~1,000 output per client per week
- 5 clients × 4 weeks = ~40K input / ~20K output per month

## Error Handling
- If metrics sheet is empty → send "No data available this week, will update Monday"
- Connect to `Notif-Error` workflow
