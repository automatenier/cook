---
tags:
  - consulting
---
# 04 — Personalized Reminders & Check-ins

> Auto-sends personalized reminders based on trainee's schedule, missed workouts, and coach preferences. Uses ElevenLabs for voice reminders with coach's cloned voice.

---

## Triggers (Multiple)

| Trigger | Time | Condition |
|---|---|---|
| Morning workout reminder | 06:00 WIB | If trainee has workout scheduled today |
| Workout time reminder | 30 min before scheduled time | Based on trainee's preferred workout time |
| Missed workout nudge | 21:00 WIB | If no workout logged by evening |
| Meal reminder | 07:00 / 12:00 / 18:00 | If meal not yet logged |
| Weekly check-in | Sunday 10:00 | All trainees |
| Streak celebration | On completion | When trainee hits streak milestone |

## Flow — Morning Reminder

```
Cron (06:00 WIB daily)
  → Google Sheets: Pull today's schedule per trainee
  → IF: Has workout today
      → Anthropic (Claude Haiku): Generate personalized morning message
      → ElevenLabs: Generate voice note with coach's voice (optional)
      → Telegram: Send text + voice note
  → IF: Rest day
      → Telegram: "Rest day hari ini! Recovery itu bagian dari progress 💤"
```

## Claude Prompt for Personalized Messages

```
You are a fitness coach sending a morning reminder via Telegram.

Trainee: {name}
Today's workout: {focus} ({exercises_count} exercises, ~{duration} min)
Current streak: {streak} days
Last workout feedback: "{last_notes}"
Weekly compliance: {compliance}%

Generate a SHORT motivational reminder (2-3 sentences max).
- Reference their streak if > 3 days
- Reference yesterday's feedback if relevant
- If compliance < 70%, add gentle accountability
- Bahasa Indonesia, casual, supportive
- No emoji overload (max 2)
```

## Flow — Missed Workout Nudge (21:00)

```
Cron (21:00 WIB daily)
  → Google Sheets: Check if today's workout is logged
  → IF: NOT logged AND has workout scheduled
      → Anthropic: Generate gentle nudge
      → Telegram:
          "Hey {name}, gue notice workout hari ini belum ke-log.

           Masih sempet? Atau mau reschedule ke besok?

           Reply:
           ✅ Udah workout, lupa log → /workout
           📅 Reschedule besok
           ❌ Skip hari ini"
      → Handle inline keyboard response
      → Google Sheets: Update accordingly
  → IF: Logged
      → Skip (already handled in workout completion flow)
```

## Flow — Coach Brief Before Notification

Based on your SOP notes: "sblm notif-workout, send brief ke coach dulu, biar dia bisa kasi personal touch"

```
Cron (05:30 WIB — 30 min before trainee reminder)
  → Google Sheets: Pull trainee's today workout + recent data
  → Telegram (Coach Channel):
      "📋 {trainee} punya workout hari ini: {focus}

       Streak: {streak} | Compliance: {compliance}%
       Last feedback: '{notes}'

       Mau tambah personal message? Reply dalam 15 menit.
       Kalau gak reply, reminder default akan dikirim."
  → Wait: 15 minutes
  → IF: Coach replied
      → Append coach's message to trainee reminder
  → ELSE
      → Send default AI-generated reminder
```

## ElevenLabs Voice Reminders

For high-tier clients, send voice notes with coach's cloned voice:

```
ElevenLabs TTS:
  Text: "{personalized_message}"
  Voice ID: {coach_voice_id}
  Model: eleven_multilingual_v2
  Output: MP3 → send via Telegram voice message
```

## Integrations
- Telegram Bot (TRAINEE-BOT for trainees, Coach-BOT for coach)
- Google Sheets (schedule, compliance tracking)
- Anthropic Claude Haiku (personalized messages)
- ElevenLabs (voice reminders — optional)
