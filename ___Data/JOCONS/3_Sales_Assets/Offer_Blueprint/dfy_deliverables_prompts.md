---
tags:
  - consulting
---
# DFY Deliverables — Prompt Library

> **When to run:** After `offer_agent.py` has generated the client's offer sheet.
> **Before every prompt:** Claude reads `swipe_file.md` + `offer_sheet.md` + `client_info/` for that client.
> **Output target:** Notion-paste-ready markdown. Each deliverable becomes a Notion page inside the client's workspace.

---

## How This Fits in the 14-Day Sprint

```
Day 2  → Offer agent runs → offer_sheet.md generated
Day 3  → Run PROMPT 1 (Bonuses) + PROMPT 2 (Roadmap)
Day 4  → Run PROMPT 3 (DFY Assets) after filming + client info collected
Day 7  → Drop all Notion pages into client workspace
Day 14 → Walk client through their Notion deliverables on consultation call
```

---

## PROMPT 1 — Bonus Stack Generator

> Generates 3-5 fully written bonuses. Each bonus includes its name, perceived value, sales description, AND the actual deliverable content ready to paste into Notion.

```
Read the following files for [CLIENT NAME]:
- swipe_file.md
- offer_sheet.md
- client_info/product_market_fit.md
- client_info/offer_positioning.md

You are building the BONUS STACK for this fitness coach's high-ticket offer.

The bonuses must:
1. Each solve ONE specific, named frustration from the avatar's daily life
2. Be high-perceived-value but low-effort for the coach to fulfill
3. Feel like they could be sold separately (standalone value)
4. Each have a dollar value assigned ($200–$1,000+)
5. Use the "name the mechanism" principle — no generic titles

Generate EXACTLY 5 bonuses. For each bonus, output:

---

## 🎁 BONUS #[N]: [Catchy Named Title] (Valued at $[X])

### Tagline
[One sentence — what it does and who it's for]

### Why This Exists (Sales Copy)
[2-3 sentences explaining the specific problem this solves.
Written as client benefit, not feature description.
Sound like the offer sheet — specific, emotional, results-focused.]

### What's Inside
[Bullet list of 5-8 specific items inside this bonus.
Be specific — "37 recipes" not "many recipes", "6-minute routine" not "short routine"]

### Notion Page Content
[Write the FULL CONTENT of this bonus — everything the client's client would actually read/use.
Structured for Notion with H2 headings, bullet points, callout blocks.
This is the actual deliverable, not a description of it.
Minimum 400 words of real content per bonus.]

---

After all 5 bonuses, add:

## Bonus Stack Summary (for Offer Sheet / Sales Page)

List all 5 bonuses in this format:
- **BONUS #1:** [Title] — $[Value] — [One sentence description]
- **BONUS #2:** ...
- **Total Bonus Value:** $[Sum]
- **Main Offer Price:** [from offer sheet]
- **Total Value:** $[Offer + All Bonuses]

Output in Indonesian. Match the coach's brand voice from swipe_file.md.
```

---

## PROMPT 2 — Roadmap Generator

> Creates the phase-by-phase transformation journey. Visual-ready for Notion. Used in the VSL, offer sheet sales calls, and delivered as a client onboarding resource.

```
Read the following files for [CLIENT NAME]:
- swipe_file.md
- offer_sheet.md
- client_info/product_market_fit.md
- client_info/life_story.md
- client_info/produk.md

You are creating the TRANSFORMATION ROADMAP — the visual journey that shows the client's client exactly how they get from their Current Situation to their Desired Outcome.

This roadmap is:
1. Used in the VSL and on sales calls (visual storytelling)
2. Delivered as a Notion page to paying clients (their guide)
3. Referenced throughout the coaching program

The roadmap must have 4 phases. Each phase must:
- Have a named mechanism (not "Phase 1: Basics" — name the process itself)
- Cover a specific number of weeks
- Address ONE root cause or transformation lever per phase
- Include what the coach does AND what the client does in that phase
- End with a clear milestone the client achieves before moving to Phase 2

Output in this EXACT Notion-ready format:

---

# [CLIENT NAME]'s Signature System: [Give the full system a proprietary name]

## Perjalananmu: [Current State] → [Desired State]

> 💬 [One sentence that captures the emotional transformation — from pain to identity shift]

---

## 🗺️ Gambaran Umum

| Fase | Nama | Minggu | Fokus Utama | Milestone |
|------|------|--------|-------------|-----------|
| 1 | [Name] | 1-[X] | [Core focus] | [Result client has] |
| 2 | [Name] | [X]-[X] | [Core focus] | [Result client has] |
| 3 | [Name] | [X]-[X] | [Core focus] | [Result client has] |
| 4 | [Name] | [X]-[X] | [Core focus] | [Result client has] |

---

## Fase 1: [Proprietary Phase Name] (Minggu 1–[X])

### 🎯 Fokus Fase Ini
[2-3 sentences explaining the ROOT CAUSE this phase addresses.
Why do we start here? What breaks down if we skip this phase?]

### Apa Yang Terjadi
**Yang coach lakukan:**
- [Specific action 1]
- [Specific action 2]
- [Specific action 3]

**Yang kamu lakukan:**
- [Specific client action 1]
- [Specific client action 2]
- [Specific client action 3]

### Tools & Resources di Fase Ini
- [Bonus/DFY asset that supports this phase]
- [Module or resource]

### ✅ Milestone: Apa yang kamu capai sebelum pindah ke Fase 2
> [Specific, measurable result. Not vague — "turun 3kg" or "tidur 7 jam tanpa gangguan" not "merasa lebih baik"]

---

[Repeat same structure for Fase 2, 3, 4]

---

## 🏁 Kehidupan Setelah Program

[Short paragraph — what life looks like AFTER all 4 phases complete.
Paint the specific "after" scenario using their avatar's dream life from PMF doc.
This is the emotional payoff — make it real and vivid.]

---

## ❓ FAQ Roadmap

**Q: Berapa lama program ini?**
A: [From offer sheet — total weeks]

**Q: Bagaimana kalau saya ketinggalan satu minggu?**
A: [Reassuring answer specific to their program structure]

**Q: Apa yang terjadi setelah program selesai?**
A: [Alumni program, maintenance, continuing support from offer sheet]

---

Output in Indonesian. Use the coach's exact niche language from swipe_file.md (e.g., if they say "ibu sibuk" use that, don't switch to "wanita karir").
```

---

## PROMPT 3 — DFY Asset Pack Generator

> Generates all Done-For-You assets. Run this AFTER filming day when you know the client's preferences (food, restaurants, travel habits). Each asset becomes its own Notion page.

### 3A — Shopping List (Instacart/Alfamart Style)

```
Read the following files for [CLIENT NAME]:
- swipe_file.md
- offer_sheet.md
- client_info/product_market_fit.md

The avatar is: [PASTE AVATAR DESCRIPTION FROM SWIPE FILE]
Their dietary approach: [e.g., "no strict dieting, real food", "low carb", "Mediterranean"]
Local context: Indonesia (Alfamart, Indomaret, Sayurbox, HappyFresh)

Create a DONE-FOR-YOU SHOPPING LIST they can use every week. This list must:
1. Be organized by store section (not by meal)
2. Include specific brand names available in Indonesia
3. Include approximate prices where helpful
4. Have a "grab and go" format — the client should be able to open Notion on their phone in the store and just check items off

Output in Notion-ready format:

---

# 🛒 Daftar Belanja Mingguan — [CLIENT NAME]'s System

> ✅ List ini sudah dipilihkan khusus untukmu. Tinggal buka di HP, masuk supermarket, centang satu per satu. Tidak perlu berpikir.

## Cara Pakai
1. Screenshot halaman ini atau buka Notion di HP
2. Pergi ke [Alfamart/Indomaret/Sayurbox]
3. Centang tiap item saat kamu ambil
4. Selesai dalam [X] menit — belanja tanpa berpikir

---

## 🥩 Protein (Sumber Energi + Pembentuk Otot)
- [ ] [Specific item + brand + quantity] — Rp [range]
- [ ] [Item]
...

## 🥦 Sayuran & Buah
- [ ] [Items]
...

## 🥑 Lemak Sehat
- [ ] [Items]
...

## 🌾 Karbohidrat Cerdas
- [ ] [Items]
...

## 🧀 Snack yang Aman
- [ ] [Items — things that fit their dietary approach, no willpower needed]
...

## 🧴 Dapur & Bumbu
- [ ] [Oils, seasonings, sauces that align with their method]
...

## 💊 Suplemen (Opsional)
- [ ] [Based on their protocol — only if the coach recommends]
...

---

## 🚀 Versi Express (10 Menit Belanja)
> Kalau lagi buru-buru banget, beli HANYA ini:
- [ ] [5-7 most essential items that keep them on track]

---

## ❌ Hindari Ini
[Short list of items that look healthy but sabotage their specific goals]

---

Output in Indonesian. Be specific to their avatar's lifestyle (e.g., if they're busy moms, items should be quick-to-cook. If corporate professionals, ready-to-eat options matter).
```

---

### 3B — 7-Day Meal Plan (No-Think Plan)

```
Read the following files for [CLIENT NAME]:
- swipe_file.md
- offer_sheet.md
- client_info/product_market_fit.md

Avatar food preferences: [FILL FROM ONBOARDING — what do they like, hate, allergies]
Cooking time available: [e.g., "15 min max on weekdays", "can cook Sunday prep"]
Family situation: [e.g., "kids at home", "solo", "partner not dieting"]
Calorie/macro target: [From offer sheet or leave flexible]

Create a 7-DAY MEAL PLAN that requires ZERO decision-making. Rules:
- Repeat breakfasts (2 options rotation max — decision fatigue killer)
- Prep-friendly (Sunday batch cook where possible)
- Real food they actually want to eat (not sad diet food)
- Includes exact portions where it matters
- Each meal has a 5-minute "shortcut version" for chaos days

Output in Notion-ready format:

---

# 📅 Rencana Makan 7 Hari — [CLIENT NAME]'s System

> 🧠 Plan ini dirancang agar kamu tidak perlu berpikir "makan apa ya?" satu kali pun minggu ini.

## Persiapan Minggu (Sunday Prep — 45 menit)
[Specific batch cook instructions — what to prep in advance]
- [ ] [Task 1]
- [ ] [Task 2]

---

## SENIN

### 🌅 Sarapan
**[Meal name]**
- [Ingredient + amount]
- [Total: ~X kalori / X protein]
- ⚡ Shortcut: [2-minute alternative if no time]

### ☀️ Makan Siang
...

### 🌙 Makan Malam
...

### 🍎 Camilan (jika lapar)
...

---

[Repeat for SELASA through MINGGU]

---

## 📊 Ringkasan Nutrisi Mingguan
| Hari | Kalori | Protein | Lemak | Karbo |
|------|--------|---------|-------|-------|
| Senin | ~[X] | [X]g | [X]g | [X]g |
...

---

## 🔄 Aturan Swap
> Tidak suka salah satu menu? Swap dengan ini:
- Sarapan alternatif: [Options]
- Makan siang alternatif: [Options]
- Makan malam alternatif: [Options]

---

Output in Indonesian. Real food. No diet bro language. Match the avatar's actual lifestyle.
```

---

### 3C — Restaurant Survival Guide

```
Read the following files for [CLIENT NAME]:
- swipe_file.md
- client_info/product_market_fit.md

The avatar's most common dining situations:
[FILL FROM ONBOARDING — where do they eat? Business lunch? Family dinner? Social events?]

Specific restaurants/warung to cover:
[FILL FROM ONBOARDING — ask client their top 5 most-visited places]

Create a RESTAURANT SURVIVAL GUIDE that tells them EXACTLY what to order at each place — no guessing, no willpower required.

Output in Notion-ready format:

---

# 🍽️ Panduan Makan di Luar — [CLIENT NAME]'s System

> 📌 Simpan halaman ini. Sebelum pergi ke restoran mana pun, buka ini dan kamu sudah tahu mau pesan apa.

## Prinsip Utama (Berlaku di Mana Saja)
1. [Simple rule 1 — e.g., "protein dulu, karbohidrat belakangan"]
2. [Simple rule 2]
3. [Simple rule 3]
> 🧠 Dengan 3 aturan ini, kamu bisa makan di restoran mana pun dan tetap on track.

---

## 🏪 [Restaurant Name #1]

**Situasi:** [When they'd typically go here]

### ✅ Pesan Ini
| Menu | Kenapa Bagus | Modifikasi |
|------|-------------|------------|
| [Specific menu item] | [Why it works] | [Ask for X without Y] |
| [Menu item] | | |

### ❌ Hindari Ini
- [Item + why — keep it short, not preachy]
- [Item]

### 💬 Cara Bilang ke Waiter
> "[Exact phrase to say when ordering — e.g., 'Bisa saosnya dipisah? Dan nasinya setengah porsi?']"

---

[Repeat for Restaurant #2 through #5]

---

## 🎉 Skenario Khusus

### Makan Siang Meeting / Business Lunch
[What to do when eating with clients/bosses and can't choose the restaurant]

### Arisan / Makan Keluarga
[Strategy for family gatherings, lots of food on the table]

### Acara Ulang Tahun / Pesta
[Permission + strategy for celebrations without derailing progress]

### Makan di Mal (Foodcourt)
[Go-to choices at common Indonesian mall food courts]

---

Output in Indonesian. Be specific — actual menu names, not general advice.
```

---

### 3D — Travel Protocol

```
Read the following files for [CLIENT NAME]:
- swipe_file.md
- client_info/product_market_fit.md

Travel patterns: [FILL FROM ONBOARDING — how often do they travel? Business or leisure? Domestic or international? Hotel or family home?]

Create a TRAVEL PROTOCOL that covers exactly what to do before, during, and after travel to maintain results. This is their "never falls off while traveling" playbook.

Output in Notion-ready format:

---

# ✈️ Protokol Perjalanan — [CLIENT NAME]'s System

> 🎯 Perjalanan tidak harus menghancurkan progressmu. Ini adalah protokol yang kami buat khusus untukmu.

## 🗓️ 48 Jam Sebelum Berangkat

**Persiapan tubuh:**
- [ ] [Specific action — e.g., "Makan lebih tinggi protein 2 hari sebelum"]
- [ ] [Action]

**Persiapan logistik:**
- [ ] [Pack these snacks — list specific items]
- [ ] [Download/prepare these apps: e.g., Grab Food, HappyFresh for destination]
- [ ] [Research: hotel gym, nearby grocery, halal restaurants at destination]

---

## 🏨 Di Hotel / Tempat Menginap

### Workout Tanpa Gym (15 Menit)
> Ini cukup untuk mempertahankan progress. Tidak perlu sempurna.

[Specific bodyweight routine — exercise name, reps, sets]
- [Exercise 1] — [X] reps × [X] sets
- [Exercise 2] — [X] reps × [X] sets
...
Total waktu: ~15 menit | Tidak perlu peralatan

### Sarapan Hotel Strategy
[What to pick from hotel breakfast buffet — common items found in most Indonesian hotels]

### Room Service Safe Choices
[What to order if eating in the room]

---

## 🍽️ Makan di Kota Tujuan

### Cara Riset Restoran Cepat
1. Google: "[City] + "restaurant + high protein"
2. GoFood/GrabFood: filter [X]
3. Minta rekomendasi hotel concierge: "[Exact phrase to say]"

### Snack Darurat (Beli di Minimarket Lokal)
- [Item 1 — found at Indomaret/Alfamart nationally]
- [Item 2]
- [Item 3]
> ✅ Dengan ini kamu tidak akan pernah kelaparan dan terpaksa makan sembarangan.

---

## 🔄 Kembali ke Rumah

### Re-entry Protocol (Hari Pertama Pulang)
- [ ] [What to eat day 1 back]
- [ ] [Movement/workout to get back on track]
- [ ] [Mindset reset — don't punish yourself if you slipped]

### Kalau Kamu "Lepas Kendali" Selama Perjalanan
> [Short, compassionate note — what to do if they ate poorly the whole trip. No guilt, just a clear next step.]

---

## 📍 Destinasi Spesifik

[If client travels to specific cities regularly, add a section per city]

### Jakarta → [City Name]
[Specific restaurant picks, grocery options, hotel gym quality]

---

Output in Indonesian. Practical, not preachy. This should feel like advice from a friend who travels a lot and has figured it out — not a nutrition textbook.
```

---

## PROMPT 4 — Full Notion Workspace Packager

> Run this LAST. It generates the master Notion page structure that links all deliverables together into one client-facing workspace.

```
Read the following files for [CLIENT NAME]:
- swipe_file.md
- offer_sheet.md

You have already generated these deliverables for this client:
- offer_sheet.md (their main program)
- 5 bonuses (Bonus #1 through #5)
- Transformation roadmap (4 phases)
- DFY shopping list
- 7-day meal plan
- Restaurant survival guide
- Travel protocol

Create the MASTER NOTION WORKSPACE HOME PAGE that:
1. Welcomes the client with their name and program name
2. Gives them a clear orientation ("start here" path)
3. Links to every deliverable with a one-line description
4. Sets expectations for how to use each resource
5. Includes a quick-reference "Daily Habits" section

Output in Notion-ready format:

---

# 🎉 Selamat Datang, [CLIENT'S CLIENT NAME]!

## Kamu sekarang resmi menjadi bagian dari [PROGRAM NAME].

> 💬 [Personalized welcome message from the coach — 2-3 sentences. Warm, specific, references their goal from the avatar. Use coach's brand voice from swipe_file.md.]

---

## 🚀 Mulai Di Sini (Urutan Penting)

Ikuti urutan ini di minggu pertama:

1. **Baca Roadmap-mu** → Pahami 4 fase perjalananmu
2. **Simpan Daftar Belanja** → Screenshot atau bookmark untuk belanja mingguan
3. **Print/Save Rencana Makan** → Pakai mulai Senin depan
4. **Baca Panduan Restoran** → Simpan di HP untuk dibuka saat makan di luar
5. **Buka Bonus #1** → Mulai hari ini, tidak perlu menunggu

---

## 📁 Semua Resource-mu

### 🗺️ Program Utama
| Resource | Apa Isinya | Kapan Pakai |
|----------|------------|-------------|
| [Roadmap link] | 4 fase transformasimu dari [Current] → [Desired] | Baca sekali, revisit setiap bulan |
| [Offer Sheet / Program Overview] | Semua yang termasuk dalam programmu | Referensi kapan pun |

### 🎁 Bonus-mu
| Bonus | Isi Singkat | Kapan Pakai |
|-------|-------------|-------------|
| Bonus #1: [Title] | [One line] | [When to use — e.g., "Setiap pagi"] |
| Bonus #2: [Title] | [One line] | |
| Bonus #3: [Title] | [One line] | |
| Bonus #4: [Title] | [One line] | |
| Bonus #5: [Title] | [One line] | |

### 🍽️ Done-For-You Assets
| Asset | Apa Isinya | Kapan Pakai |
|-------|------------|-------------|
| Daftar Belanja Mingguan | [X] item siap centang | Setiap belanja minggu |
| Rencana Makan 7 Hari | Sarapan, makan siang, makan malam sudah ditentukan | Setiap hari |
| Panduan Restoran | [X] restoran dengan pilihan menu spesifik | Sebelum makan di luar |
| Protokol Perjalanan | Routine + strategi makan saat traveling | Sebelum trip |

---

## 📋 Kebiasaan Harian (Copy ke Kalender / Reminderm-u)

> Ini adalah minimum yang perlu kamu lakukan setiap hari. Sesederhana ini.

**Pagi:**
- [ ] [Habit 1 from their program — specific, takes <5 min]
- [ ] [Habit 2]

**Siang:**
- [ ] [Habit]

**Malam:**
- [ ] [Habit 1]
- [ ] [Habit 2]

> 💡 Jangan coba lakukan semua sekaligus. Mulai dengan satu kebiasaan sampai terasa otomatis, baru tambah yang berikutnya.

---

## 📞 Cara Menghubungi [COACH NAME]

| Butuh Apa | Hubungi Via | Waktu Respons |
|-----------|------------|---------------|
| Pertanyaan cepat | WhatsApp: [number] | <4 jam (jam kerja) |
| Review progress | Telegram group | Harian |
| Jadwal konsultasi | [Calendar link] | [Booking window] |
| Darurat | WA voice note | Sesegera mungkin |

---

## 🏆 Komunitas

[Link to WhatsApp group / Telegram community]
> Bergabung dengan [X] coach lain yang sedang dalam perjalanan yang sama. Share progress, tanya jawab, dan dapatkan dukungan.

---

Output in Indonesian. The homepage should feel premium, organized, and warm. Not overwhelming — clear hierarchy, everything one click away.
```

---

## Notion Setup Guide (How to Build the Workspace)

> Run this after you have all the content generated. Takes ~30 minutes to set up per client.

### Step 1 — Create the Notion Workspace

1. Go to Notion → New page → "Client Name — Program Name"
2. Set as a **private page** initially
3. Change cover photo to something matching their brand aesthetic (Unsplash)
4. Add the coach's logo as the page icon (emoji or upload)

### Step 2 — Paste Content

Paste each prompt output into Notion. Notion accepts markdown, so:
- `#` becomes H1
- `##` becomes H2
- `- [ ]` becomes a checkbox
- `| table |` becomes a Notion table
- `>` text becomes a quote block

**After pasting, manually convert these to Notion native blocks:**
- Convert `> 💬 text` blocks → **Callout blocks** (choose matching emoji + background color)
- Convert phase headers → **Toggle headers** (so client can collapse/expand each phase)
- Convert the "Kebiasaan Harian" section → a **Template button** (so they can create a fresh daily checklist each day)
- Convert the weekly meal plan days → **Synced blocks** (so if you update Monday, it updates everywhere)

### Step 3 — Link All Pages

In the Master Home Page:
- Replace each `[link]` placeholder with actual Notion page links
- Use `@` to mention pages inline
- Add a **linked database view** if you want to show content calendar here too

### Step 4 — Set Sharing

1. Click "Share" → "Share to web" → **OFF** (keep private by default)
2. Click "Invite" → enter client's email → **Can view** access (not edit)
3. Optional: Give **Can comment** access if you want them to leave feedback on content
4. Copy the private link → send to client in onboarding welcome message

### Step 5 — Walk Through on Day 14 Call

Screen share the Notion workspace. Walk through in this order:
1. Show the Home Page → explain the "start here" path
2. Open Roadmap → walk through all 4 phases (5 minutes)
3. Open one Bonus → read through it together, answer questions
4. Open Shopping List → show how to use on phone
5. Open Restaurant Guide → find a restaurant they actually go to
6. Explain how to reach you (the contact table at the bottom)

> Client should end the call feeling like they have everything they need AND they know how to use it.

---

## Notion Template Naming Convention

```
[CLIENT NAME] — Program Workspace/
├── 🏠 Home (Master Page)
├── 🗺️ Roadmap — [Program Name]
├── 🎁 Bonuses/
│   ├── Bonus 1 — [Title]
│   ├── Bonus 2 — [Title]
│   ├── Bonus 3 — [Title]
│   ├── Bonus 4 — [Title]
│   └── Bonus 5 — [Title]
├── 🍽️ DFY Assets/
│   ├── Daftar Belanja Mingguan
│   ├── Rencana Makan 7 Hari
│   ├── Panduan Restoran
│   └── Protokol Perjalanan
└── 📋 Daily Tracker (optional — template button)
```

---

## Quick Reference — Which Prompt to Run When

| Deliverable | Prompt | Inputs Needed | Notion Page |
|-------------|--------|---------------|-------------|
| Bonus Stack (all 5) | PROMPT 1 | swipe_file + offer_sheet + PMF + positioning | `Bonuses/` folder |
| Roadmap (4 phases) | PROMPT 2 | swipe_file + offer_sheet + PMF + life_story + produk | `Roadmap` page |
| Shopping List | PROMPT 3A | swipe_file + PMF + dietary preferences | `DFY Assets/` |
| 7-Day Meal Plan | PROMPT 3B | swipe_file + PMF + food preferences + cooking time | `DFY Assets/` |
| Restaurant Guide | PROMPT 3C | swipe_file + PMF + client's top 5 restaurants | `DFY Assets/` |
| Travel Protocol | PROMPT 3D | swipe_file + PMF + travel patterns | `DFY Assets/` |
| Home Page | PROMPT 4 | All above already generated | Master home page |
