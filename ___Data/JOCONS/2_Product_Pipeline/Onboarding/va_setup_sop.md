---
tags:
  - consulting
---
# VA Setup SOP — Complete Toolstack & Setup Guide

> Panduan lengkap untuk VA: tools yang dibutuhkan, cara setup per client, dan checklist operasional harian.

---

## 1. Toolstack Overview

### Core Tools (Access Needed)

| Tool | Purpose | Access Type | Login |
|------|---------|-------------|-------|
| **Google Drive** | Client file storage + shared folders | Google account (team) | team@joconsult.com |
| **Google Calendar** | Booking & scheduling | Same Google account | — |
| **Google Sheets** | CRM, KPI tracking, Command Center | Same Google account | — |
| **Telegram** | Internal comms + progress channels | Personal account | — |
| **WhatsApp Business** | Client communication | Business number | — |
| **Instagram** | Content posting + DM monitoring | Client's IG (access via Meta Business) | — |
| **Meta Business Suite** | Keyword CTA automation + ads | Client grants Admin access | — |
| **TikTok Business** | Content posting | Client's login | — |
| **Wistia** | VSL video hosting | Team account | — |
| **Netlify** | Funnel deployment | Team account (deploy only) | — |
| **ElevenLabs** | Voice cloning + voiceover | Team account | — |
| **n8n** | Automation workflows | Team instance | — |
| **Canva** | Quick graphics | Team account | — |
| **CapCut** | Video editing (Editor uses, VA coordinates) | — | — |
| **Fathom** | Call recording | Team account | — |
| **Remotion** | Programmatic video rendering | VS Code (Jordan handles) | — |

### Per-Client Access Checklist

Ketika client baru sign, VA harus collect ini:

| Access | Dari Siapa | Format | Deadline |
|--------|-----------|--------|----------|
| Instagram login (or Meta Business invite) | Client | Admin role di Meta Business Suite | Day 0-1 |
| Meta Business Suite Admin access | Client | Invite via Business Settings | Day 0-1 |
| TikTok login | Client | Login credentials atau Business Center | Day 3 |
| Google Drive shared folder | VA creates | Share link ke client | Day 0 |
| Existing lead list (DMs, emails, WA) | Client | Spreadsheet / CSV | Day 10 |
| Voice recording (5-10 min) | Client | MP3/WAV uploaded to GDrive | Day 1-2 |
| Brand assets (logo, colors, fonts) | Client | Uploaded to GDrive | Day 1-2 |

---

## 2. Keyword CTA Automation Setup

### What It Does
Ketika seseorang comment keyword tertentu di IG post/reel, otomatis kirim DM dengan link/resource.

### Setup Steps

#### A. Get Meta Business Suite Access
1. Client buka: business.facebook.com → Settings → People
2. Client add VA email sebagai **Admin**
3. VA terima invite → accept
4. Verify: bisa lihat client's IG account di Meta Business Suite

#### B. Setup Keyword Automation di Meta Business Suite
1. Buka Meta Business Suite → Inbox → Automations
2. Klik "Create Automation"
3. Pilih "Keyword Reply"
4. Setup keyword pairs:

| Keyword | Auto-Reply Message | CTA |
|---------|-------------------|-----|
| `[KEYWORD 1 — e.g., "FREE"]` | "Hey [nama]! Ini dia [resource]... [link]" | Freebie delivery |
| `[KEYWORD 2 — e.g., "INFO"]` | "Thanks for reaching out! Ini detail program... [link]" | VSL / booking |
| `[KEYWORD 3 — e.g., "COACH"]` | "Mau ngobrol? Book free session di sini... [link]" | Calendar booking |

5. Test: comment keyword di client's post → verify DM terkirim
6. Document keyword pairs di client folder: `[client]/keyword_cta_pairs.md`

#### C. Copywriting Input Needed
Untuk setiap keyword CTA, VA butuh dari Jordan/Claude:
- **Keyword**: 1 kata, ALL CAPS, mudah diingat
- **Auto-reply message**: Max 2-3 kalimat, personal tone
- **CTA link**: Freebie URL / Calendar link / WhatsApp link
- **Follow-up sequence** (optional): 24h later auto-follow-up

#### D. TikTok Keyword CTA
TikTok tidak punya native keyword automation. Workaround:
1. Pin comment dengan CTA keyword di setiap video
2. Bio link → Linktree / direct booking page
3. Monitor DMs manually (or via n8n TikTok integration jika available)

---

## 3. Content Copywriting Setup

### What VA Needs to Setup Content Production

| Info | Source | Purpose |
|------|--------|---------|
| Client Brief | `content/clients/[name]/client_brief.md` | Brand voice, tone, avatar, offer |
| Footage Checklist | `content/clients/[name]/footage_checklist.md` | What footage exists |
| Swipe File Index | `content/swipe_file/_index.md` | Available viral structures |
| Hook Bank | `content/library/hook_bank.md` | Proven hooks |
| CTA Bank | `content/library/cta_bank.md` | CTA templates |
| Script Templates | `content/library/script_templates/` | Value-CTA, Authenticity, Breakdown |

### Content Production Flow (VA Role)

```
Jordan/Claude generates scripts
    ↓
VA organizes scripts ke folder → [client]/projects/[YYMMDD]_[slug]/
    ↓
VA coordinates with Editor → share Remotion MP4s + voiceovers + scripts
    ↓
VA tracks progress: drafted → editing → approved → posted
    ↓
VA shares approved batch ke client for review
    ↓
Client approves → VA schedules posting
```

### ElevenLabs Voice Clone Setup
1. Collect client's voice recording (5-10 min, clean audio)
2. Upload ke ElevenLabs → Voice Lab → Add Voice → Instant Voice Cloning
3. Name: `[client_name]_voice`
4. Test generate sample → verify quality
5. Share voice ID ke Jordan for Remotion integration

---

## 4. Meta Business Suite — Full Setup

### Initial Setup (Per Client)

| Step | Action | Notes |
|------|--------|-------|
| 1 | Get Admin access (see Section 2A) | — |
| 2 | Link IG account to Meta Business Suite | Client may need to do this first |
| 3 | Setup keyword CTA automations (see Section 2B) | — |
| 4 | Connect Facebook Pixel to VSL funnel | Jordan/n8n handles pixel install |
| 5 | Create Custom Audiences | Website visitors, IG engagers, video viewers |
| 6 | Build Lookalike Audiences | From Custom Audiences (top 1-3%) |
| 7 | Setup Ad Account (if running ads) | Client must own ad account, VA manages |

### Ads Setup Checklist

| Task | Status |
|------|--------|
| [ ] Pixel installed on VSL funnel | |
| [ ] Custom Audience: Website Visitors (30 days) | |
| [ ] Custom Audience: IG Engagers (90 days) | |
| [ ] Custom Audience: Video Viewers (50%+ watched) | |
| [ ] Lookalike from best Custom Audience | |
| [ ] Retargeting campaign structure approved | |
| [ ] Ad creatives (3-5 variations) approved by client | |
| [ ] Daily budget approved by client | |
| [ ] Campaign launched | |

---

## 5. GDrive Folder Structure (Per Client)

Saat client baru sign, create:

```
[Client Name] (Shared Folder — 10GB)/
├── 📁 onboarding/
│   ├── onboarding_form_responses.json
│   ├── client_info_life_story.mp4
│   ├── client_info_pmf.md
│   ├── client_info_positioning.md
│   └── client_info_product.md
├── 📁 brand_assets/
│   ├── logo/
│   ├── colors_fonts.md
│   └── reference_content/
├── 📁 testimonials/
│   ├── screenshots/
│   ├── before_after/
│   └── video_testimonials/
├── 📁 voice_clone/
│   └── training_samples/
├── 📁 raw_footage/
│   ├── talking_head/
│   ├── broll/
│   └── vsl_recording/
├── 📁 content/
│   ├── scripts/
│   ├── approved/
│   ├── posted/
│   └── content_calendar.xlsx
├── 📁 funnel/
│   ├── vsl_video/
│   └── landing_page_screenshots/
├── 📁 ads/
│   ├── creatives/
│   └── performance_reports/
├── 📁 lead_activation/
│   ├── lead_list.xlsx
│   └── reactivation_scripts/
└── 📁 deliverables/
    ├── offer_sheet.md
    ├── keyword_cta_pairs.md
    ├── sales_hq_dashboard.md
    └── weekly_reports/
```

---

## 6. Daily Checklist (VA)

### Morning (08:00-10:00)
- [ ] Check Telegram channels → flag overdue items
- [ ] Update CRM with yesterday's activities
- [ ] Coordinate with Editor → confirm today's batch
- [ ] Coordinate with Setter → review EOD report
- [ ] Follow up on pending client approvals

### Midday (12:00-14:00)
- [ ] Check content posting schedule → confirm posts went live
- [ ] Monitor keyword CTA performance (any triggers?)
- [ ] Organize incoming assets / feedback from client

### Afternoon (14:00-17:00)
- [ ] Prep tomorrow's tasks → brief Editor + Setter
- [ ] File any new materials to correct folders
- [ ] Update content tracking sheet (drafted/editing/approved/posted)
- [ ] Send EOD summary to Jordan via Telegram

### Weekly
| Day | Task |
|-----|------|
| Mon | Distribute weekly content batch to Editor |
| Wed | Mid-week check: content production + setter KPIs |
| Fri | Compile weekly report: content posted, leads, calls |
| Sun | Review next week's content calendar → flag gaps |

---

## 7. New Client Onboarding Checklist (VA)

Print and check off for every new client:

### Day 0 — Client Signs
- [ ] Create GDrive shared folder (structure from Section 5)
- [ ] Create Cook folders: `content/clients/[name]/` + `Fulfillment/_CLIENT_DELIVERABLES/[name]/`
- [ ] Send welcome email (template: `Fulfillment/_ONBOARDING/welcome_email_template.md`)
- [ ] Send Onboarding Form link
- [ ] Add to WhatsApp group + Telegram community
- [ ] Share video module access
- [ ] Setup Telegram progress channel (n8n)
- [ ] Update CRM → stage: "Closed"
- [ ] Copy client_brief template → fill with initial info
- [ ] Copy footage_checklist template → prepare for filming

### Day 1-3 — Follow Up
- [ ] Follow up: Onboarding Form lengkap?
- [ ] Follow up: Materials uploaded ke GDrive?
- [ ] Organize materials ke folder yang benar
- [ ] Notify Jordan: onboarding data complete → run offer agent

### Day 3-5 — Filming Coordination
- [ ] Schedule filming session (waktu + lokasi)
- [ ] Kirim filming prep brief ke client
- [ ] After filming: organize footage ke GDrive + Cook `a_roll/` & `footage/`
- [ ] Upload VSL ke Wistia → catat media ID
- [ ] Deploy funnel → test semua links

### Day 5-10 — Content
- [ ] Collect client's last 20 posts
- [ ] Share content calendar ke client
- [ ] Organize generated scripts
- [ ] Coordinate with Editor

### Day 8-10 — Automation
- [ ] Request Meta Business Suite access
- [ ] Setup keyword CTA (IG)
- [ ] Setup keyword CTA (TikTok — manual)
- [ ] Test CTA automation

### Day 10-14 — Activation & Launch
- [ ] Help client export lead list
- [ ] Organize leads (Hot/Warm/Cold)
- [ ] Prepare deliverables review doc
- [ ] Setup Chrome "Sales HQ" bookmarks
- [ ] Create Command Center sheet
- [ ] Schedule consultation + walkthrough calls

---

## 8. Troubleshooting

| Problem | Solution |
|---------|----------|
| Client gak isi Onboarding Form | WA reminder Day 1, 2, 3. Escalate ke Jordan Day 4. |
| Meta Business Suite access denied | Walk client through: business.facebook.com → Settings → People → Add |
| Keyword CTA gak trigger | Check: keyword exact match? Automation active? IG account linked? |
| Voice clone quality jelek | Ask client: rerecord in quiet room, speak naturally, min 5 min |
| Client gak respond approvals | WA → Telegram → Call. 48h max before escalation. |
| GDrive storage full | Archive old files. Max 10GB per client. |
| n8n automation error | Screenshot error → send to Jordan via Telegram |
