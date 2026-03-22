---
tags:
  - consulting
---
# 06 — Laporan Progress Harian & Mingguan

> Auto-generates daily summaries for trainees and comprehensive weekly progress reports for both trainees and coaches. Pulls data from workout logs, meal tracking, gamification, and compliance metrics.

---

## Report Types

| Report | For | When | Channel |
|---|---|---|---|
| Daily Recap (Trainee) | Trainee | 21:30 WIB daily | Telegram (TRAINEE-BOT) |
| Daily Coach Summary | Coach | 22:00 WIB daily | Telegram (Coach-BOT) |
| Weekly Progress Report (Trainee) | Trainee | Sunday 20:00 WIB | Telegram (TRAINEE-BOT) |
| Weekly Coach Report | Coach | Sunday 20:30 WIB | Telegram (Coach-BOT) |
| Monthly Overview | Coach + Trainee | 1st of month 09:00 | Telegram (both) |

---

## Flow — Daily Trainee Recap (21:30 WIB)

```
Cron (21:30 WIB daily)
  → Google Sheets: Pull today's data per trainee
      - Workout: completed? exercises done, duration, notes
      - Meals: logged? calories, protein, compliance
      - Weight: logged today?
      - XP earned today, current streak
  → Anthropic (Claude Haiku): Generate personalized daily recap
  → Telegram (TRAINEE-BOT):
      "📋 Recap hari ini, {name}:

       🏋️ Workout: {status_emoji} {workout_summary}
       🍽️ Meals: {meals_logged}/3 logged ({calories} kcal, {protein}g protein)
       ⚖️ Weight: {weight_status}
       🔥 Streak: {streak} hari
       ⭐ XP hari ini: +{daily_xp} (Total: {total_xp})

       {personalized_note}

       Besok: {tomorrow_preview}"
```

### Claude Prompt for Daily Recap Note

```
You are a fitness coach assistant generating a short personalized note for a trainee's daily recap.

Data:
- Workout completed: {yes/no}
- Meal compliance: {meals_logged}/3
- Current streak: {streak} days
- Weekly compliance so far: {compliance}%
- Today's mood/notes: "{trainee_notes}"

Generate 1-2 sentences. Bahasa Indonesia, casual, supportive.
- If everything done: celebrate briefly
- If workout missed: no guilt, gentle encouragement
- If meals missed: remind importance of nutrition tracking
- If streak is high: acknowledge the consistency
- Keep it real, not overly cheerful
```

## Flow — Daily Coach Summary (22:00 WIB)

```
Cron (22:00 WIB daily)
  → Google Sheets: Pull ALL trainees' data for today
  → Code Node: Aggregate per trainee
      - compliance_rate per trainee
      - flag trainees with 0 activity
      - flag trainees who broke streak
  → Code Node: Format summary
  → Telegram (Coach-BOT):
      "📊 Daily Summary — {date}

       ✅ Completed workout: {count}/{total} trainees
       🍽️ All meals logged: {count}/{total}
       ⚠️ Zero activity today: {inactive_names}

       Per trainee:
       {name}: Workout ✅ | Meals 3/3 | Streak 12 🔥
       {name}: Workout ❌ | Meals 1/3 | Streak 0 ⚠️
       {name}: Workout ✅ | Meals 2/3 | Streak 5

       🚨 Needs attention:
       - {name}: 3 hari tanpa workout
       - {name}: Streak baru putus hari ini

       Reply /note {name} {message} untuk kirim personal message."
```

## Flow — Weekly Progress Report — Trainee (Sunday 20:00)

```
Cron (Sunday 20:00 WIB)
  → Google Sheets: Pull full week data per trainee (Mon-Sun)
  → Code Node: Calculate weekly metrics
      - workouts_completed / workouts_scheduled
      - avg_calories, avg_protein
      - weight_change (if logged)
      - total_xp_earned
      - streak status
      - compliance_percentage
  → Anthropic (Claude Haiku): Generate weekly analysis
  → Telegram (TRAINEE-BOT):
      "📈 WEEKLY PROGRESS — {name}
       Week {week_number} ({date_range})

       ━━━ WORKOUT ━━━
       Completed: {done}/{scheduled} ({compliance}%)
       {progress_bar}
       Fav exercise: {most_logged_exercise}

       ━━━ NUTRITION ━━━
       Avg calories: {avg_cal} kcal/day
       Avg protein: {avg_protein}g/day
       Meal logging: {meal_compliance}%

       ━━━ BODY ━━━
       Weight: {weight_start} → {weight_end} ({delta})
       Trend: {trend_emoji} {trend_text}

       ━━━ GAMIFIKASI ━━━
       XP minggu ini: +{weekly_xp}
       Level: {level} {emoji}
       Streak: {streak} hari
       Badges earned: {new_badges}
       Ranking: #{rank}/{total}

       ━━━ COACH NOTES ━━━
       {ai_generated_weekly_insight}

       Semangat minggu depan! 💪"
```

### Claude Prompt for Weekly Insight

```
You are a fitness coach assistant generating a weekly insight for a trainee.

Weekly data:
- Workout compliance: {compliance}%
- Nutrition compliance: {meal_compliance}%
- Weight change: {delta} kg
- Streak: {streak} days
- Compared to last week: compliance {up/down} by {diff}%
- Coach's notes this week: "{coach_notes}"

Generate 2-3 sentences of insight. Bahasa Indonesia, casual.
- Highlight what went well
- One area to focus on next week
- If declining: gentle course-correction
- If improving: momentum acknowledgment
- Be specific, reference actual numbers
```

## Flow — Weekly Coach Report (Sunday 20:30)

```
Cron (Sunday 20:30 WIB)
  → Google Sheets: Pull ALL trainees' weekly data
  → Code Node: Calculate aggregate metrics + per-trainee breakdown
  → Anthropic (Claude Haiku): Generate coach summary with recommendations
  → Telegram (Coach-BOT):
      "📊 WEEKLY COACH REPORT — Week {week_number}

       ━━━ OVERVIEW ━━━
       Active trainees: {count}
       Avg workout compliance: {avg_compliance}%
       Avg meal logging: {avg_meal}%
       Total workouts completed: {total_workouts}

       ━━━ TOP PERFORMERS ━━━
       🥇 {name} — {compliance}% compliance, {xp} XP
       🥈 {name} — {compliance}% compliance, {xp} XP
       🥉 {name} — {compliance}% compliance, {xp} XP

       ━━━ NEEDS ATTENTION ━━━
       🔴 {name}: {compliance}% compliance (turun dari {prev}%)
           → Suggestion: {ai_suggestion}
       🟡 {name}: Streak putus di hari ke-{day}
           → Suggestion: {ai_suggestion}

       ━━━ PER TRAINEE ━━━
       {name}: W {w_compliance}% | M {m_compliance}% | {delta_weight} | Streak {streak}
       {name}: W {w_compliance}% | M {m_compliance}% | {delta_weight} | Streak {streak}
       ...

       ━━━ RECOMMENDATIONS ━━━
       {ai_generated_coach_recommendations}

       Reply /adjust {name} {note} untuk update program."
```

## Flow — Monthly Overview (1st of Month, 09:00)

```
Cron (1st of month 09:00 WIB)
  → Google Sheets: Pull full month data
  → Code Node: Calculate monthly aggregates
      - Total workouts, avg compliance per week
      - Weight progression (start → end)
      - Best week vs worst week
      - Total XP earned, level progression
      - Badge collection for the month
  → Anthropic (Claude Sonnet — higher quality for monthly): Generate monthly report
  → Telegram (TRAINEE-BOT): Detailed monthly progress
  → Telegram (Coach-BOT): Per-trainee monthly summary
  → Google Sheets: Archive monthly data to "Monthly Archive" tab
```

### Monthly Trainee Message Format

```
"📅 MONTHLY PROGRESS — {name}
 {month} {year}

 ━━━ HIGHLIGHTS ━━━
 🏋️ Total workouts: {total}/{scheduled} ({compliance}%)
 🍽️ Avg daily calories: {avg_cal} | Protein: {avg_protein}g
 ⚖️ Weight: {start_weight} → {end_weight} ({total_delta} kg)
 🔥 Longest streak: {longest_streak} hari
 ⭐ Total XP: +{monthly_xp} ({start_level} → {end_level})
 🏅 New badges: {badges}

 ━━━ WEEK BY WEEK ━━━
 Week 1: {compliance}% {bar}
 Week 2: {compliance}% {bar}
 Week 3: {compliance}% {bar}
 Week 4: {compliance}% {bar}

 ━━━ COACH'S MONTHLY REVIEW ━━━
 {ai_monthly_insight}

 Bulan depan target kita: {next_month_focus}"
```

## Google Sheets Structure — Reports Tab

| Column | Description |
|---|---|
| trainee_id | Unique ID |
| date | Report date |
| report_type | daily / weekly / monthly |
| workouts_done | Count completed |
| workouts_scheduled | Count scheduled |
| compliance_pct | Workout compliance % |
| meals_logged | Total meals logged |
| avg_calories | Average daily calories |
| avg_protein | Average daily protein (g) |
| weight_start | Weight at period start |
| weight_end | Weight at period end |
| xp_earned | XP earned in period |
| streak_at_report | Streak count at report time |
| coach_notes | Any coach notes for the period |
| ai_insight | AI-generated insight text |

## Progress Bar Generator (Code Node)

```javascript
function progressBar(percentage) {
  const filled = Math.round(percentage / 10);
  const empty = 10 - filled;
  return '█'.repeat(filled) + '░'.repeat(empty) + ` ${percentage}%`;
}
// Example: progressBar(70) → "███████░░░ 70%"
```

## Integrations
- Telegram Bot (TRAINEE-BOT for trainee reports, Coach-BOT for coach summaries)
- Google Sheets (all tracking data + reports archive)
- Anthropic Claude Haiku (daily/weekly personalized insights)
- Anthropic Claude Sonnet (monthly deep analysis — higher quality)
