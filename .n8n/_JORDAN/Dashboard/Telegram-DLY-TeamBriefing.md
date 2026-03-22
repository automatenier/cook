---
tags:
  - automation
---
# Telegram-DLY-TeamBriefing

> Auto-sends daily task briefing to internal team Telegram channel. Each team member (VA, Editor, Setter) sees their tasks for the day across ALL clients.

---

## Trigger
- **Type:** Cron / Schedule
- **Time:** 08:30 WIB daily (Monday-Saturday)

## Flow

```
Schedule (08:30 WIB)
  → Google Sheets: Pull active client list
  → Loop Each Client:
      → Google Sheets: Pull today's content calendar
      → Google Sheets: Pull today's setter targets
      → Google Sheets: Pull pending approvals / blockers
  → Merge: Combine all clients into one briefing
  → Anthropic (Claude Haiku): Format team briefing by role
  → Telegram: Send to internal team channel
```

## Nodes Detail

### 1. Schedule Trigger
```json
{
  "type": "n8n-nodes-base.scheduleTrigger",
  "parameters": {
    "rule": {
      "interval": [{ "field": "cronExpression", "expression": "0 8 * * 1-6" }]
    }
  }
}
```

### 2. Google Sheets — Pull All Client Tasks
Per client, pull:
- Today's content to edit/post (for Editor)
- Today's assets to organize/follow-up (for VA)
- Today's DM targets and pipeline status (for Setter)
- Any pending client approvals or blockers

### 3. Anthropic (Claude Haiku) — Format Briefing
- **Model:** claude-haiku-4-5-20251001
- **System prompt:**
```
Kamu adalah operations manager.
Format daily team briefing yang clear dan actionable.
Group tasks by ROLE (VA, Editor, Setter), then by CLIENT.
Bahasa: Indonesian. Keep it scannable — bullet points, no fluff.
```
- **User prompt:**
```
Date: {today}
Active clients: {client_list}

PER CLIENT DATA:
{client_1_name}:
  Content today: {content_tasks}
  Setter pipeline: {setter_data}
  Pending approvals: {pending}
  Blockers: {blockers}

{client_2_name}:
  ...

Format as team briefing:
1. VA TASKS — organized by client (asset follow-ups, GDrive, scheduling, client comms)
2. EDITOR TASKS — organized by client (which reels/stories to edit today, deadlines)
3. SETTER TASKS — organized by client (DM targets, follow-ups due, pipeline status)
4. BLOCKERS — anything that needs Jordan's attention

End with "Reply thread ini kalau ada update atau blocker baru"
```

### 4. Telegram — Send to Team Channel
- **Chat ID:** `{internal_team_chat_id}`
- **Parse mode:** Markdown

## Example Output

```
📋 DAILY BRIEFING — Senin, 17 Feb 2026

━━━ 👤 VA TASKS ━━━

Coach Aldi:
• Follow up onboarding form (belum lengkap — Section 4)
• Organize raw footage dari filming session kemarin → GDrive
• Share approved content calendar ke client

Coach Budi:
• Upload edited VSL ke Wistia → catat media ID
• Schedule 30-min walkthrough call

━━━ 🎬 EDITOR TASKS ━━━

Coach Aldi:
• Edit 4 reels (W3: authentic_01-02, value_01-02)
• Remotion + VO files sudah di GDrive/scripts/
• Deadline: Rabu jam 17:00

Coach Budi:
• Edit VSL raw footage → CapCut → Wistia
• Edit 2 testimonial clips (30-90 detik each)

━━━ 💬 SETTER TASKS ━━━

Coach Aldi:
• Pipeline: 12 active convos, 3 at Problem Aware stage
• Follow-up due: 2 warm leads (Day 3 follow-up)
• Target hari ini: 4 new ICPs, 10 DMs

Coach Budi:
• Pipeline: 8 active convos, 1 ready to book
• Reactivation batch: Send 10 warm messages (scripts in dm_scripts/)

━━━ ⚠️ BLOCKERS ━━━

• Coach Aldi belum kirim voice recording untuk ElevenLabs
  → VA: follow up today

Reply thread ini kalau ada update 👇
```

## Token Budget
- ~3,000 input / ~2,000 output per day (all clients combined)
- 26 days/month = ~78K input / ~52K output per month

## Error Handling
- If no tasks found for a role → "No tasks today" under that section
- If Sheets fails → send static "Check Sheets manually, automation error" + trigger `Notif-Error`
