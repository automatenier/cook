---
tags:
  - consulting
---
# 05 — Gamifikasi Workout Progress & Group Leaderboards

> Turns workout compliance into a game with XP points, streak badges, level-ups, and group leaderboards. Drives trainee motivation through friendly competition and visible progress.

---

## Core Mechanics

| Mechanic | How It Works |
|---|---|
| **XP Points** | Earn XP for every completed action (workout, meal log, check-in) |
| **Streaks** | Consecutive days of compliance → streak counter + multiplier |
| **Badges** | Milestone achievements (first workout, 7-day streak, 30-day warrior, etc.) |
| **Levels** | Accumulate XP to level up (Beginner → Warrior → Beast → Legend) |
| **Leaderboard** | Weekly ranking among all trainees in the same coach's program |

## XP Point System

```
Action                          | Base XP | Streak Multiplier
-------------------------------|---------|------------------
Complete workout (logged)       | 100     | x1.5 after 7 days
Log all meals for the day      | 50      | x1.5 after 7 days
Log weight/progress photo      | 75      | —
Reply to coach check-in        | 25      | —
Complete all daily tasks       | 50      | Bonus (on top of individual)
Weekend workout (Sat/Sun)      | 150     | Extra motivation for weekends
Personal Record (PR)           | 200     | One-time per exercise
```

### Streak Multiplier Rules
- Days 1-6: x1.0 (normal)
- Days 7-13: x1.5
- Days 14-29: x2.0
- Days 30+: x2.5 (Legend multiplier)
- Streak breaks → reset to x1.0 (but total XP is never lost)

## Level System

```
Level       | XP Required | Badge Emoji
------------|-------------|------------
Newbie      | 0           | 🥚
Starter     | 500         | 🌱
Warrior     | 2,000       | ⚔️
Fighter     | 5,000       | 🔥
Beast       | 10,000      | 🦁
Legend      | 25,000      | 👑
Immortal    | 50,000      | 💎
```

## Badge Collection

| Badge | Condition | Emoji |
|---|---|---|
| First Blood | Complete first workout | 🩸 |
| Consistency King | 7-day streak | 👑 |
| Iron Will | 14-day streak | 🔩 |
| 30-Day Warrior | 30-day streak | ⚔️ |
| Meal Prepper | Log meals for 7 consecutive days | 🍱 |
| Weekend Warrior | Workout on both Sat & Sun | 🏋️ |
| PR Crusher | Hit a personal record | 💪 |
| Photo Day | Submit progress photo | 📸 |
| Perfect Week | 100% compliance for 7 days | ⭐ |
| Coach's Pick | Manually awarded by coach | 🏆 |

## Flow — XP Calculation (On Workout Log)

```
Webhook: Triggered when /workout is logged (from 02-Dashboard)
  → Google Sheets: Get trainee's current XP, streak, level
  → Code Node: Calculate XP earned
      base_xp = 100
      IF streak >= 30: multiplier = 2.5
      ELIF streak >= 14: multiplier = 2.0
      ELIF streak >= 7: multiplier = 1.5
      ELSE: multiplier = 1.0
      earned = base_xp * multiplier
      new_total = current_xp + earned
      new_level = calculate_level(new_total)
  → Google Sheets: Update XP, streak, level
  → IF: Level changed?
      → Anthropic (Claude Haiku): Generate level-up celebration message
      → Telegram (Trainee): "🎉 LEVEL UP! {name} naik ke level {new_level}! {emoji}"
      → Telegram (Group — optional): Announce level-up to group
  → IF: New badge earned?
      → Telegram (Trainee): "🏅 Badge baru: {badge_name} {badge_emoji}!"
```

## Flow — Daily Leaderboard (20:00 WIB)

```
Cron (20:00 WIB daily)
  → Google Sheets: Pull all trainees under same coach
  → Code Node: Sort by weekly XP (Mon-Sun), take top 10
  → Code Node: Format leaderboard message
  → Telegram (Group Chat):
      "🏆 LEADERBOARD HARI INI

       1. {name} — {xp} XP {streak_emoji}
       2. {name} — {xp} XP
       3. {name} — {xp} XP
       ...

       🔥 Top performer: {top_name} dengan {top_xp} XP!
       💪 Keep pushing, semua progress itu dihitung!"
```

## Flow — Weekly Leaderboard Reset & Recap (Sunday 21:00)

```
Cron (Sunday 21:00 WIB)
  → Google Sheets: Pull full week XP data
  → Code Node: Calculate weekly rankings + awards
  → Anthropic (Claude Haiku): Generate weekly recap with highlights
  → Telegram (Group Chat):
      "📊 WEEKLY RECAP — Week {week_number}

       🥇 Champion: {1st_name} — {xp} XP
       🥈 Runner-up: {2nd_name} — {xp} XP
       🥉 3rd Place: {3rd_name} — {xp} XP

       📈 Most Improved: {improved_name} (+{delta} XP vs last week)
       🔥 Longest Streak: {streak_name} ({streak_days} hari)
       ⭐ Perfect Week: {perfect_names}

       Minggu depan, siapa yang bisa geser posisi? 💪"
  → Google Sheets: Archive weekly data, reset weekly XP counter
```

## Flow — Streak Milestone Celebration

```
Webhook: Triggered on streak update
  → IF: streak == 7 OR streak == 14 OR streak == 30 OR streak == 60 OR streak == 90
      → Anthropic (Claude Haiku): Generate milestone message
      → ElevenLabs (optional): Voice note celebration with coach's voice
      → Telegram (Trainee): Personal celebration message
      → Telegram (Group): "{name} just hit a {streak}-day streak! 🔥"
      → Google Sheets: Award badge
```

## Flow — Coach Awards Badge

```
Telegram (Coach-BOT): Coach sends /award {trainee} {badge}
  → Code Node: Parse command
  → Google Sheets: Add badge to trainee's collection
  → Telegram (Trainee): "🏆 Coach baru aja kasih kamu badge: {badge_name}!"
  → Telegram (Group — optional): Announce coach award
```

## Google Sheets Structure — Gamification Tab

| Column | Description |
|---|---|
| trainee_id | Unique ID |
| name | Trainee name |
| total_xp | Lifetime XP |
| weekly_xp | Current week XP (resets Sunday) |
| level | Current level name |
| streak_current | Current streak count |
| streak_longest | All-time longest streak |
| badges | Comma-separated badge list |
| last_activity | Timestamp of last logged action |
| multiplier | Current streak multiplier |

## /stats Command (Trainee-BOT)

```
Trainee sends: /stats
  → Google Sheets: Pull trainee gamification data
  → Telegram:
      "📊 Stats kamu, {name}:

       Level: {level} {emoji}
       Total XP: {total_xp}
       Minggu ini: {weekly_xp} XP
       Streak: {streak} hari 🔥
       Multiplier: x{multiplier}
       Badges: {badge_emojis}

       Ranking minggu ini: #{rank} dari {total} trainees"
```

## Integrations
- Telegram Bot (TRAINEE-BOT for /stats, Coach-BOT for /award, Group Chat for leaderboards)
- Google Sheets (XP tracking, leaderboard data, badge collection)
- Anthropic Claude Haiku (celebration messages, weekly recaps)
- ElevenLabs (optional voice celebrations for streak milestones)
