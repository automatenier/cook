---
tags:
  - consulting
---
# 02 — Workout & Nutrition Tracker Dashboard

> Trainee logs workouts and meals via Telegram bot. Data feeds into a Google Sheets dashboard that coach can review anytime.

---

## Trigger
- **Type:** Telegram bot commands from trainee

## Bot Commands

| Command | Action |
|---|---|
| `/workout` | Pull today's workout → show exercises → trainee marks complete |
| `/meal` | Show today's meal plan → trainee uploads food photos |
| `/progress` | Show weekly stats (workouts completed, meals logged, streak) |
| `/weight` | Log today's weight |

## Flow — Workout Logging

```
Trainee sends: /workout
  → Google Sheets: Pull today's program (from 01-AI-Program-Generation)
  → Telegram: Send workout card
      "💪 Hari ini: Upper Body Push
       1. Bench Press — 3×8-10 (rest 90s)
       2. OHP — 3×8-10 (rest 90s)
       3. ...

       Klik ✅ kalau udah selesai per exercise"
  → Trainee clicks ✅ per exercise (inline keyboard callbacks)
  → Google Sheets: Log completion (timestamp, exercises done, notes)
  → When all done:
      → Telegram: "🎉 Workout selesai! Total: {duration}. Notes?"
      → Trainee sends optional notes (difficulty, pain, etc.)
      → Google Sheets: Update row with notes
      → Telegram (Coach channel): "{trainee} finished workout. Notes: {notes}"
```

## Flow — Meal Logging

```
Trainee sends: /meal
  → Telegram:
      "🍽 Meals hari ini:
       ☐ Breakfast (target: {calories}cal)
       ☐ Lunch (target: {calories}cal)
       ☐ Dinner (target: {calories}cal)
       ☐ Snacks

       Upload foto + keterangan per meal"
  → Trainee sends photo + text
  → Telegram: Get file → Google Drive: Upload photo
  → Google Sheets: Log meal (timestamp, meal_type, photo_link, description)
  → After all meals logged:
      → Telegram (Coach channel): "{trainee} logged all meals today ✅"
```

## Dashboard (Google Sheets)

### Tab 1: Daily Log
| Date | Trainee | Workout Done | Exercises Completed | Duration | Notes | Breakfast | Lunch | Dinner | Weight |
|---|---|---|---|---|---|---|---|---|---|

### Tab 2: Weekly Summary (auto-calculated)
| Week | Trainee | Workouts (done/target) | Meals Logged | Avg Weight | Streak | Compliance % |
|---|---|---|---|---|---|---|

### Tab 3: Coach View (all trainees)
| Trainee | This Week % | Last Weigh-In | Trend | Needs Attention? |
|---|---|---|---|---|

## Conditional Formatting
- 🟢 80%+ compliance
- 🟡 50-80% compliance
- 🔴 <50% compliance

## Integrations
- Telegram Bot (existing TRAINEE-BOT)
- Google Sheets (dashboard)
- Google Drive (meal photos)
