---
tags:
  - consulting
---
# SOP — Weekly Coach Video (60-90 detik)

> Setiap minggu, coach rekam 1 video pendek buat tiap trainee. Celebrate wins + adjustment minggu depan. Dikirim via Telegram setiap Minggu malam.

---

## Kenapa Ini Penting

- Trainee merasa **dilihat** dan **diperhatikan** → retention naik
- Personal touch yang AI gak bisa replace
- 60 detik effort dari coach = trainee tetap motivated 1 minggu penuh

---

## Jadwal

| Hari | Waktu | Apa |
|---|---|---|
| **Minggu 18:00** | Coach terima brief dari bot | Data trainee minggu ini (auto dari n8n) |
| **Minggu 18:00-20:00** | Coach rekam video | 1 video per trainee, 60-90 detik |
| **Minggu 20:00** | Kirim ke trainee | Via Telegram / WhatsApp |

---

## Coach Brief (Auto dari N8N — Minggu 18:00)

Coach terima message di Telegram (Coach-BOT):

```
📋 WEEKLY VIDEO BRIEF — {trainee_name}

WINS MINGGU INI:
✅ Workout compliance: {compliance}% ({done}/{scheduled})
✅ Streak: {streak} hari
✅ Best moment: {highlight}
✅ Weight: {start} → {end} ({delta} kg)

PERLU DIBAHAS:
⚠️ {adjustment_1} (misal: "Meal logging cuma 60% — remind soal nutrition")
⚠️ {adjustment_2} (misal: "Leg day di-skip 2x — cek apakah ada issue")

PROGRAM MINGGU DEPAN:
📅 Focus: {next_week_focus}
📅 Target: {next_week_target}

Rekam video 60-90 detik, cover:
1. Celebrate 1 win spesifik
2. 1 adjustment buat minggu depan
3. Semangatin buat minggu depan
```

---

## Script Template (Coach Tinggal Ikutin)

```
"Hey {name}! Minggu ini gue mau bilang... [CELEBRATE WIN].

{contoh: "Lo udah workout 5 dari 5 hari, streak lo udah 12 hari — that's insane bro."}

Satu hal yang gue mau lo improve minggu depan: [ADJUSTMENT].

{contoh: "Meal logging lo masih 60%, gue mau lo push ke 80% — cukup foto aja, gak perlu detail banget."}

Minggu depan kita fokus ke [NEXT WEEK FOCUS].

{contoh: "Upper body strength — gue udah adjust program lo, cek di bot ya."}

Keep going, proud of you. See you next week! 💪"
```

**Total: 60-90 detik. Gak perlu editing. Raw selfie video = lebih authentic.**

---

## Recording Rules

| Rule | Detail |
|---|---|
| **Durasi** | 60-90 detik. MAX 2 menit. Lebih singkat lebih baik. |
| **Format** | Selfie video, portrait mode (9:16) |
| **Setting** | Dimana aja — gym, rumah, kantor. Gak perlu studio. |
| **Editing** | ZERO. Raw video = authentic. Jangan pake filter. |
| **Tone** | Casual, supportive, kayak ngobrol sama temen |
| **Mention by name** | WAJIB sebut nama trainee di awal |
| **Specific wins** | WAJIB sebut angka/achievement spesifik, bukan generic "good job" |
| **1 adjustment only** | Jangan kasih 5 hal buat di-improve. Cukup 1 yang paling penting. |

---

## Delivery

| Method | How |
|---|---|
| **Telegram** | Coach reply video ke Coach-BOT → n8n forward ke TRAINEE-BOT |
| **WhatsApp** | Kirim langsung ke trainee (kalau gak pake Telegram) |
| **Deadline** | Minggu 20:00 WIB — sebelum weekly report dikirim (20:30) |

---

## N8N Flow

```
Cron (Minggu 18:00 WIB)
  → Google Sheets: Pull weekly data per trainee
  → Anthropic (Claude Haiku): Generate coach brief dari data
  → Telegram (Coach-BOT): Kirim brief per trainee ke coach

Coach replies with video:
  → Telegram (Coach-BOT): Receive video
  → n8n: Match video ke trainee (dari reply thread)
  → Telegram (TRAINEE-BOT): Forward video ke trainee
      "🎥 Video dari Coach buat kamu minggu ini! 👇"
  → Google Sheets: Mark "weekly_video_sent = TRUE"

Cron (Minggu 21:00 — Reminder kalau belum kirim)
  → Google Sheets: Check trainee yang belum dapet video
  → IF: Ada yang missing
      → Telegram (Coach-BOT): "⚠️ Video untuk {names} belum dikirim. Deadline 30 menit lagi!"
```

---

## Kalau Coach Gak Sempat Rekam

Backup plan (urutan prioritas):

1. **Voice note 30 detik** — sama strukturnya (win + adjustment + semangat)
2. **Text message personal** — bukan template, harus specific ke data trainee
3. **AI-generated voice** (ElevenLabs) — last resort, pake coach's cloned voice + brief dari Claude

---

## KPI

| Metric | Target |
|---|---|
| Video sent rate | 100% setiap minggu |
| Avg video duration | 60-90 detik |
| Trainee reply rate | > 70% reply setelah terima video |
| Retention impact | Track: trainee yang terima video vs yang gak → compare churn rate |
