---
tags:
  - consulting
---
# Client Onboarding Form Template

Use this template to collect answers from new clients after payment. These answers feed directly into the Offer Agent tool (`tools/offer_agent.py --from-file`).

Save completed forms as JSON: `Fulfillment/_ONBOARDING/{client_name}_onboarding.json`

---

## Phase 1: Niche Deep-Dive

### 1.1 Avatar (Target Client)
**Question:** "Siapa target klien utama kamu?"
- Options: CEO/Exec (Pria 40+), Post-Partum Mom, Software Engineer, Custom
- **Field:** `avatar_type`, `avatar_description`

### 1.2 Pain Point
**Question:** "Apa masalah utama yang mereka hadapi?"
- For CEO: Penampilan, Energi, Kesehatan
- For Post-Partum: Body confidence, Energy, Time
- For Software Engineer: Posture, Weight, Energy
- **Field:** `pain_point`

### 1.3 Dream Outcome
**Question:** "Apa hasil akhir yang mereka inginkan dalam 90 hari?"
- Example: "Perut rata & rahang tajam, terlihat 10 tahun lebih muda"
- **Field:** `dream_outcome`

### 1.4 Roadblock
**Question:** "Apa hambatan terbesar yang mencegah mereka mencapai hasil ini?"
- Options: Jadwal padat, Client dinners, Waktu prep, Custom
- **Field:** `roadblock`

---

## Phase 2: The Vehicle (Program Structure)

### 2.1 Program Name
**Question:** "Apa nama program transformasi kamu?"
- Smart default: "The High-Performance Physique System"
- **Field:** `program_name`

### 2.2 Training Style
**Question:** "Metode training apa yang akan digunakan?"
- Options: Biometric-Based (Oura/Apple Watch), Hybrid (Gym + Home), Bodyweight Only, Custom
- **Field:** `training_style`

### 2.3 Nutrition Approach
**Question:** "Pendekatan nutrisi apa?"
- Options: Protein-First IF, Macro Tracking, Meal Plans, Intuitive Eating
- **Field:** `nutrition_approach`

### 2.4 Accountability Method
**Question:** "Bagaimana cara maintain mereka on-track?"
- Options: Daily Check-in (WhatsApp), Weekly Audit (Zoom), VIP Concierge (24/7 WhatsApp)
- **Field:** `accountability`

---

## Phase 3: Done-For-You Assets

### 3.1 DFY Asset Selection (Multi-select)
**Question:** "Pilih 3 aset siap pakai yang akan disertakan:"
- [ ] Grocery/Restaurant Solution (Go-Food Cheat Sheet + Shopping List)
- [ ] Travel/Hotel Protocol (Airport Guide + Hotel Workout)
- [ ] Nutrition Templates (Power Shake Menu + Plate Method)
- [ ] Sleep & Recovery Protocol (Oura/Apple Watch optimization)
- [ ] Recovery Gear (Massage Gun mini)
- **Field:** `dfy_assets` (array)

---

## Phase 4: 12-Week Roadmap

### 4.1 Roadmap Approval
**Question:** "Apakah kamu setuju dengan roadmap standar 4-fase, atau mau customize?"
- Phase 1: Bio-Audit (Week 1-3) — Baseline + Quick Wins
- Phase 2: Metabolic Ignite (Week 4-6) — Visible Fat Loss
- Phase 3: Peak Performance (Week 7-9) — Muscle Definition
- Phase 4: Autopilot Mastery (Week 10-12) — Sustainability
- **Field:** `roadmap_approved` (boolean), `roadmap_custom` (optional object)

---

## Phase 5: Value Stack (Bonuses)

### 5.1 Bonus Selection (Multi-select)
**Question:** "Pilih 2-3 bonus untuk membuat penawaran irresistible:"
- [ ] Sleep & Recovery Protocol ($500 value)
- [ ] Executive Wardrobe Guide ($300 value)
- [ ] Recovery Gear — Massage Gun Mini ($200 value)
- [ ] Monthly Maintenance Blueprint ($400 value)
- [ ] Crisis Toolkit ($300 value)
- **Field:** `bonuses` (array)

---

## Phase 6: Risk Reversal & Pricing

### 6.1 Guarantee
**Question:** "Guarantee apa yang paling confident kamu berikan?"
- Options: "Work Until You Win", "30-Day Boardroom Confidence Refund", "Data-Driven Guarantee"
- **Field:** `guarantee_type`, `guarantee_details`

### 6.2 Pricing
**Question:** "Struktur harga apa yang cocok?"
- Plan A: Pay-in-Full VIP — Rp 35.000.000
- Plan B: Installment 3x — Rp 13.500.000/bulan
- Plan C: Ultra-Premium — Rp 75.000.000
- Custom pricing also accepted
- **Field:** `pricing` (array of objects with tier, price_idr, details)

---

## Additional Info

### Client Details
- **Field:** `client_name` (required)
- **Field:** `client_instagram` (optional)
- **Field:** `client_email` (optional)
- **Field:** `client_phone` (optional)
- **Field:** `notes` (free text, anything extra)
