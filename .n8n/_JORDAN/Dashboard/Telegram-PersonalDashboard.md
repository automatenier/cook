---
tags:
  - automation
---
# Telegram-PersonalDashboard

> Weekly executive summary sent to your personal Telegram. All-client overview: revenue pipeline, content output, ad performance, upcoming deadlines.

---

## Trigger
- **Type:** Cron / Schedule
- **Time:** 07:00 WIB every Monday

## Flow

```
Schedule (Monday 07:00 WIB)
  → Google Sheets: Pull all active clients + stages
  → Google Sheets: Pull CRM pipeline data (revenue, stages, close dates)
  → Google Sheets: Pull content output totals (all clients, last 7 days)
  → Google Sheets: Pull ad spend + lead data (if Meta Ads connected)
  → Anthropic (Claude Haiku): Generate executive summary
  → Telegram: Send to your personal chat
```

## Nodes Detail

### 1. Data Sources (Google Sheets)

**Client Master:**
- Total active clients
- Each client's current phase (onboarding / sprint / ongoing)
- Upcoming milestones (Day 14 consultation, monthly call, etc.)

**CRM Pipeline:**
- Leads in pipeline by stage (Discovery → Interested → Booked → Closed)
- Revenue closed this month
- Revenue projected (booked calls × close rate)

**Content Output:**
- Total content pieces posted across all clients (last 7 days)
- Per-client breakdown

**Ad Performance (if available):**
- Total ad spend
- Total leads from ads
- Cost per lead

### 2. Anthropic (Claude Haiku) — Generate Summary
- **Model:** claude-haiku-4-5-20251001
- **System prompt:**
```
Kamu adalah business intelligence assistant untuk agency owner.
Generate concise executive dashboard. English OK for metrics, Indonesian for commentary.
Focus on: what needs attention, what's working, what's at risk.
Format for Telegram markdown.
```
- **User prompt:**
```
Date: {monday_date}
Week: {week_number}

CLIENTS:
{client_list_with_phases}

PIPELINE:
- Discovery: {discovery_count}
- Conversation: {conversation_count}
- Interested: {interested_count}
- Booked: {booked_count}
- This month closed: {closed_count} (Rp {revenue})
- Projected: Rp {projected}

CONTENT (last 7 days):
- Total pieces posted: {total_content}
{per_client_breakdown}

ADS (if available):
- Spend: Rp {ad_spend}
- Leads: {ad_leads}
- CPL: Rp {cpl}

UPCOMING:
{deadlines_and_milestones}

Generate executive dashboard:
1. 🟢🟡🔴 Overall health status
2. Revenue snapshot (closed + pipeline)
3. Content velocity (on pace or behind?)
4. Top priority this week (1 thing to focus on)
5. Risk flags (clients at risk, overdue items)
6. Quick wins available
```

### 3. Telegram — Send to Personal Chat
- **Chat ID:** Your personal Telegram ID
- **Parse mode:** Markdown

## Example Output

```
🏢 WEEKLY DASHBOARD — 17 Feb 2026 (Week 8)

STATUS: 🟢 On Track

━━━ 💰 REVENUE ━━━
Closed this month: Rp 15,000,000 (1 client)
Pipeline: 3 booked calls → projected Rp 22,500,000
Target: Rp 30,000,000 → 75% tracked

━━━ 👥 CLIENTS (3 Active) ━━━
• Coach Aldi — Day 10 (sprint) 🟢
• Coach Budi — Day 4 (onboarding) 🟢
• Coach Citra — Month 2 (ongoing) 🟢

━━━ 📱 CONTENT (Last 7 Days) ━━━
Total: 24 pieces posted
• Aldi: 8 reels + 7 stories + 7 Threads ✅
• Budi: onboarding (no content yet)
• Citra: 8 reels + 7 stories + 7 Threads ✅

━━━ 🎯 THIS WEEK'S PRIORITY ━━━
Close 2 of 3 booked calls → hit Rp 30M target

━━━ ⚠️ RISK FLAGS ━━━
• Coach Budi: onboarding form incomplete (Day 4)
  → Follow up today or sprint timeline slips

━━━ ⚡ QUICK WINS ━━━
• Coach Citra's reel "3 Kesalahan Diet" went viral (2.4K views)
  → Repurpose into Threads + YouTube short this week
```

## Token Budget
- ~4,000 input / ~2,000 output per week
- 4 weeks = ~16K input / ~8K output per month (minimal cost)

## Error Handling
- If CRM data missing → show "CRM data unavailable" with link to manually check
- Connect to `Notif-Error`
