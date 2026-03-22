---
tags:
  - consulting
---
# 01 — AI Program Generation (Iterate Later)

> Claude generates a 12-week training + nutrition program from client onboarding data. Coach reviews, adjusts, then system delivers week-by-week via Telegram.

---

## Trigger
- **Type:** Manual (coach triggers after onboarding) OR Webhook (after onboarding form submitted)

## Flow

```
Trigger (coach request or form webhook)
  → Google Sheets: Pull trainee profile (age, weight, goals, injuries, experience level)
  → Anthropic (Claude Haiku/Sonnet): Generate 12-week program
      - Phase 1 (Week 1-4): Foundation
      - Phase 2 (Week 5-8): Progressive Overload
      - Phase 3 (Week 9-12): Peak / Specialization
  → Google Sheets: Store full program (1 row per day, 84 rows)
  → Telegram: Notify coach "Program generated for {trainee}. Review before activation."
  → Coach approves (Telegram button callback)
  → Google Sheets: Mark program as "Active"
  → Triggers: Weekly delivery starts (see 03-Workout-Video-Delivery)
```

## Claude Prompt for Program Generation

```
You are a certified fitness program designer.

Trainee profile:
- Name: {name}
- Age: {age}, Gender: {gender}
- Weight: {weight}kg, Height: {height}cm
- Goal: {goal} (fat loss / muscle gain / strength / general fitness)
- Experience: {level} (beginner / intermediate / advanced)
- Injuries/limitations: {injuries}
- Available equipment: {equipment}
- Days per week: {days}
- Session duration: {duration} minutes

Generate a 12-week progressive program:
- Each day: exercise name, sets, reps, rest time, tempo, RPE
- Include warm-up and cool-down
- Progressive overload built in (increase weight/reps/sets each phase)
- Nutrition guidelines: daily calories, protein/carb/fat split, meal timing
- Deload week every 4th week

Output as structured JSON:
{
  "week_1": {
    "day_1": {
      "focus": "Upper Body Push",
      "exercises": [
        {"name": "Bench Press", "sets": 3, "reps": "8-10", "rest": "90s", "video_keyword": "bench press"}
      ],
      "warmup": "...",
      "cooldown": "..."
    }
  },
  "nutrition": {
    "daily_calories": 2200,
    "protein_g": 180,
    "carbs_g": 220,
    "fat_g": 65
  }
}
```

## Iteration Flow (Coach Adjusts)

```
Coach sends: "/adjust {trainee} week 3 — replace squats with leg press (knee issue)"
  → Anthropic: Regenerate affected weeks with adjustment
  → Google Sheets: Update program
  → Telegram: Confirm changes to coach
```

## Data Storage
- **Google Sheets:** `Programs` sheet — 1 row per training day per trainee
- **Columns:** trainee_id, week, day, focus, exercises (JSON), nutrition, status

## Token Budget
- Initial generation: ~4,000 input / ~8,000 output
- Iteration/adjustment: ~2,000 input / ~3,000 output
