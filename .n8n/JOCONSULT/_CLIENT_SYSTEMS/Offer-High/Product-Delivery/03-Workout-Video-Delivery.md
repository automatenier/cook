---
tags:
  - consulting
---
# 03 — Workout Video Delivery

> Trainee types exercise name in Telegram → bot finds matching video from library → sends directly in chat. No need to open another app.

---

## Trigger
- **Type:** Telegram bot command `/video`

## Flow

```
Trainee sends: /video bench press
  → Edit Fields: Extract keyword ("bench press")
  → Google Sheets: Search "Video Library" sheet for matching keyword
  → IF: Match found
      → Google Drive: Get video file by ID
      → Telegram: Send video with caption
          "🎬 Bench Press
           Form tips: {tips}
           Sets: {today_sets} × {today_reps}"
  → IF: No match
      → Telegram: "Video gak ketemu buat '{keyword}'. Coba kata kunci lain:
         bench press, squat, deadlift, pull up, ohp, dll"
```

## Auto-Delivery (Daily Workout)

```
Cron: Setiap pagi sesuai workout schedule
  → Google Sheets: Pull today's exercises for trainee
  → Loop Each Exercise:
      → Google Sheets: Find video by exercise keyword
      → Queue videos
  → Telegram: Send as media group
      "📋 Workout Hari Ini: {focus}

       Video 1/4: Bench Press
       Video 2/4: Incline DB Press
       Video 3/4: Cable Fly
       Video 4/4: Tricep Pushdown

       Klik /workout kalau mau mulai tracking!"
```

## Video Library (Google Sheets)

| exercise_keyword | exercise_name | video_gdrive_id | tips | category | difficulty |
|---|---|---|---|---|---|
| bench press | Barbell Bench Press | 1a2b3c4d... | Keep shoulder blades retracted, arch slightly | Push | Intermediate |
| squat | Barbell Back Squat | 5e6f7g8h... | Break at hips first, knees track toes | Legs | Intermediate |
| pull up | Pull Up | 9i0j1k2l... | Full dead hang, chin over bar | Pull | Advanced |

## Video Sources
- Coach records demo videos → uploads to GDrive
- Organized by category: Push, Pull, Legs, Core, Cardio
- Each video: 15-30 seconds, clear form demo
- File naming: `{exercise_keyword}_{difficulty}.mp4`

## ElevenLabs Integration (Optional)
Before sending video, attach voice-over with coach's cloned voice:
```
"Oke {trainee}, ini bench press. Inget ya: retract shoulder blades,
slight arch. 3 set, 8-10 reps. Rest 90 detik. Let's go!"
```

## Integrations
- Telegram Bot (existing TRAINEE-BOT)
- Google Sheets (video library index)
- Google Drive (video file storage)
- ElevenLabs (optional coach voice-over)
