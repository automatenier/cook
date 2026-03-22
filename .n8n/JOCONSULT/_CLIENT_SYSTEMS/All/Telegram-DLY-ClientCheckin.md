---
tags:
  - consulting
---
# Telegram-DLY-ClientCheckin

> Auto-sends daily morning check-in to each client's Telegram channel with today's tasks and a motivational nudge.

---

## Trigger
- **Type:** Cron / Schedule
- **Time:** 08:00 WIB daily (Monday-Saturday). Skip Sunday.

## Flow

```
Schedule (08:00 WIB)
  → Google Sheets: Pull today's content calendar row (filter by date)
  → Google Sheets: Pull client list (active clients only)
  → Loop Each Client:
      → IF today has scheduled content:
          → Anthropic (Claude Haiku): Format check-in message
          → Telegram: Send to client's private channel
      → ELSE (no content today):
          → Telegram: Send light check-in (no task list)
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

### 2. Google Sheets — Pull Active Clients
- **Sheet:** "Client Master" (or CRM sheet)
- **Filter:** `status = "Active"`
- **Fields needed:** `client_name`, `telegram_chat_id`, `content_calendar_sheet_id`

### 3. Google Sheets — Pull Today's Tasks
- **Sheet:** Per-client content calendar
- **Filter:** `date = TODAY()`
- **Fields needed:** `platform`, `content_type`, `topic`, `status`, `post_time`

### 4. Anthropic (Claude Haiku) — Format Message
- **Model:** claude-haiku-4-5-20251001
- **System prompt:**
```
Kamu adalah asisten check-in harian untuk client coaching.
Tugas: format pesan pagi yang friendly dan actionable.
Bahasa: Indonesian casual (lo/gue OK, tapi professional).
Keep it short — max 10 lines.
Include emoji sparingly.
```
- **User prompt:**
```
Client: {client_name}
Today's date: {date}
Scheduled content:
{content_list}

Format as a Telegram morning check-in. Include:
1. Greeting (vary daily — don't repeat "Selamat pagi" every day)
2. Today's content tasks (what's posting, what needs approval)
3. One motivational line or reminder
4. End with "Reply kalau ada yang perlu di-adjust"
```

### 5. Telegram — Send Message
- **Chat ID:** `{client_telegram_chat_id}`
- **Parse mode:** Markdown
- **Message:** Claude output

## Message Templates (Claude will vary these)

### With tasks:
```
Pagi {CLIENT}! ☀️

Hari ini lineup-nya:
📱 IG Reel — "{TOPIC}" (posting jam {TIME})
📱 Threads — "{TOPIC}" (jam {TIME})
📖 Story — {TYPE} (2 slides, jam {TIME})

Status: ✅ Semua sudah ready di folder

Ada yang mau di-adjust sebelum posting? Reply aja di sini 👇
```

### No tasks today:
```
Hey {CLIENT}! Hari ini gak ada posting scheduled.

Good time untuk:
- Review metrics minggu ini
- Rekam 1-2 talking head clips buat stock
- Cek inbox — ada leads baru yang perlu di-follow up?

Enjoy the day! 💪
```

## Data Requirements
- Google Sheets: Client Master with `telegram_chat_id` column
- Google Sheets: Per-client content calendar with `date` column
- Telegram Bot token (existing)
- Anthropic API key (existing)

## Token Budget
- ~1,500 input / ~500 output per client per day
- 5 clients × 30 days = ~225K input / ~75K output per month

## Error Handling
- Connect to existing `Notif-Error` workflow
- If Google Sheets fails → send fallback generic message (no task list)
- If Claude fails → send static template message
