---
tags:
  - consulting
---
# Client 1 — [CLIENT NAME] | Execution Worksheet

> **To run:** Say `"Execute [Client Name] workflow"` — I read this file, find the current state, and drive from here. You only step in when I explicitly pause and ask.

---

## 📍 CURRENT STATE

| | |
|---|---|
| **Client Name** | Mathew Jordan |
| **Day** | 0 |
| **Phase** | Day 0 — In Progress |
| **Last Completed** | Welcome email finalized (links inserted) |
| **⏸️ Paused — Waiting For** | Jordan: Community + Module Access · Telegram channel (n8n trigger) |

---

## 🗂️ CLIENT PROFILE

> Fill this before first execution. Everything else flows from here.

| Field | Value |
|---|---|
| **Full Name** | Mathew Jordan |
| **IG Handle** | @jordan_engo |
| **Email** | jengolodoe@gmail.com |
| **WhatsApp** | 087881647878 |
| **Niche** | Fitness for busy moms |
| **Avatar (1 sentence)** | Busy Indonesian mom who wants to get fit but has no time between kids, work, and household |
| **Package** | AI & Scale (Best Deal) |
| **Payment Date** | 2026-02-18 |
| **Day 14 Call Date** | 2026-03-04 |
| **GDrive Folder** | https://drive.google.com/drive/folders/DEMO_MathewJordan_Assets_1A2B3C4D |
| **Telegram Channel** | *(set up Day 0 — pending Jordan)* |
| **Netlify URL** | *(collected Day 4)* |
| **Google Calendar Link** | https://calendar.google.com/calendar/appointments/schedules/DEMO_MathewJordan_Day14 |
| **Wistia Project** | *(collected Day 4)* |
| **ElevenLabs Voice ID** | *(collected Day 3)* |
| **Lead Magnet Link** | *(collected Day 10)* |

---

## 📋 SESSION LOG

| # | Date | What Was Done | Paused At | Next Session Starts At |
|---|------|--------------|-----------|------------------------|
| 1 | 2026-02-18 | Profile seeded · Folders created (22 subfolders) · welcome_email.md · asset_collection_message.md | Google Calendar link + GDrive link | Day 0 COLLECT: paste both links → I finalize email + send |
| 2 | 2026-02-18 | Dummy links inserted (demo) · welcome_email.md finalized · asset_collection_message.md updated · Worksheet updated | Community + Module Access · Telegram channel (n8n trigger) | Jordan completes PLATFORM steps → confirm "Community done" + paste TELEGRAM_CHANNEL |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

---
---

# 14-DAY SPRINT EXECUTION

> **Tags:**
> `🤖 AUTO` — I execute this immediately, no input needed
> `📥 COLLECT` — I pause here. Exact instructions below each block.
> `🎬 ONSITE` — Physical action required
> `⚙️ PLATFORM` — UI action in a specific tool

---

## 📅 DAY 0 — CLIENT SIGNED

**Status:** ⬜ Not Started | 🟡 In Progress | ✅ Done

---

### 🤖 AUTO: Create Folder Structure

```bash
# Run this when Day 0 executes — substitute [CLIENT_NAME] with actual name (no spaces, use underscores)

CLIENT="[CLIENT_NAME]"
BASE="c:/Users/natha/OneDrive - Bina Nusantara/Cook"

mkdir -p "$BASE/Fulfillment/_CLIENT_DELIVERABLES/$CLIENT"/{client_info,swipe_file,offer_sheet,brand_voice_samples,testimonials,achievements,winning_content,graphics/{lower_thirds,cta_graphics,story_templates},voice_clone/{training_samples,generated_audio},lead_magnet,content_calendar,scripts,remotion_props,funnel,dm_scripts,analytics}

mkdir -p "$BASE/content/clients/$CLIENT"/{a_roll,footage,assets,projects}
```

**Output:** All subfolders created. I'll confirm when done.

---

### 🤖 AUTO: Generate Welcome Email

> I generate this using `Fulfillment/_ONBOARDING/welcome_email_template.md` + client profile above.
> Output: Full ready-to-send email in Indonesian.
> Saves to: `Fulfillment/_CLIENT_DELIVERABLES/[CLIENT]/welcome_email.md`

**I need from profile before generating:**
- Client name ✓
- Package ✓
- Google Calendar link for Day 14 → see COLLECT below
- Module GDrive link → **FIXED** (hardcoded, no input needed): `https://drive.google.com/drive/folders/DEMO_JOConsult_Modules_AI_Scale`

---

### 🤖 AUTO: Attach & Send Contracts

> Attach these 3 documents to the welcome email before sending:
> 1. `Perjanjian Legal.pdf` — Main legal agreement
> 2. `Garansi Bersyarat.pdf` — Conditional revenue guarantee
> 3. `Kebijakan Privasi.pdf` — Privacy policy
>
> Source files: `Fulfillment/_ONBOARDING/contracts/`
> Client is instructed to sign + return to jordanmathew811@gmail.com **before** Onboarding Call.

---

### 📥 COLLECT: Signed Contracts

**Wait for client to return all 3 signed documents before scheduling Onboarding Call.**

**Confirm here when received:**
```
CONTRACTS_SIGNED: received ✓ | Date: [DATE]
```

*→ Claude saves to `Fulfillment/_CLIENT_DELIVERABLES/[CLIENT]/client_info/signed_contracts/`*
*→ This gates the Onboarding Call. Do not proceed to Phase 2 without this.*

---

### 🤖 AUTO: Generate Asset Collection Message

> I generate the exact WhatsApp/Telegram message to send the client listing all assets they need to gather.
> Includes: testimonials, before/after photos, voice recording, brand assets, logo, Client Info forms.
> Output: Ready-to-copy message.

---

### 📥 COLLECT: Google Calendar Booking Link

**What to do:**
1. Go to [Google Calendar](https://calendar.google.com) → Settings → Appointment schedules → Create
2. Name it: `[CLIENT NAME] — Day 14 Consultation`
3. Set duration: 60 minutes | Set availability: around Day 14 date
4. Copy the booking link

**Paste here:**
```
GOOGLE_CALENDAR_LINK:
```

*→ Claude adds this to profile and inserts into welcome email.*

---

### 📥 COLLECT: GDrive Shared Folder Link

**What to do:**
1. Go to [drive.google.com](https://drive.google.com)
2. Create a new folder: `[CLIENT NAME] — Assets`
3. Inside, create subfolders: `Testimonials`, `Before-After`, `Voice Sample`, `Brand Assets`, `Top Posts`
4. Click Share → Add [client email] → Can edit
5. Click "Copy link"

**Paste here:**
```
GDRIVE_LINK:
```

*→ Claude adds this to profile and inserts into welcome email.*

---

### ⚙️ PLATFORM: Community + Module Access

**Jordan does:**
- [ ] Add client to WhatsApp group
- [ ] Add client to Telegram community
- [ ] Share 20+ video module access link

**Report back:** "Community done" → I continue.

---

### ⚙️ PLATFORM: Telegram Progress Channel (n8n)

**Jordan does:**
- [ ] Trigger n8n workflow to create dedicated Telegram progress channel for this client

**Paste channel link here:**
```
TELEGRAM_CHANNEL:
```

*→ Claude adds to profile.*

---

**DAY 0 COMPLETE WHEN:** Welcome email sent + GDrive shared + community access granted + Telegram channel live.

---

## 📅 DAY 1 — ONBOARDING KICKOFF

**Status:** ⬜ Not Started | 🟡 In Progress | ✅ Done

---

### 🤖 AUTO: Generate Onboarding Instructions for Client

> I generate the exact message/guide to send the client explaining:
> - How to fill the onboarding form
> - What Client Info docs to complete (Life Story, PMF, Offer Positioning, Produk)
> - Where to upload voice recording (GDrive folder)
> - Where to upload brand assets

**Output:** Ready-to-send message + link to all forms.

---

### 📥 COLLECT: Onboarding Form Answers

**What to do:**
1. Send client the onboarding form (from `Fulfillment/_ONBOARDING/onboarding_form_template.md`)
2. When client fills it → export/paste answers
3. Save the completed file as: `Fulfillment/_CLIENT_DELIVERABLES/[CLIENT]/onboarding.json`

**Confirm here when JSON is saved:**
```
ONBOARDING_JSON: saved ✓
```

*→ This is the trigger to run Day 2. Claude cannot proceed without this.*

---

### 📥 COLLECT: Client Info Docs

**What to do:** Client fills all 4 documents and uploads to GDrive:
- `life_story.md` — Origin, turning point, purpose, vision
- `product_market_fit.md` — Current/desired situation, USP, bridge
- `offer_positioning.md` — Avatar, positioning statement, mechanism
- `produk.md` — Deliverables, coaching structure, bonuses, guarantees

**Confirm here when all 4 are in GDrive:**
```
CLIENT_INFO: ready ✓
```

---

### 📥 COLLECT: Voice Sample

**What to do:** Client records 5-10 min of clean audio (no background music, no reverb) and uploads to GDrive `Voice Sample` subfolder.

**Confirm here when uploaded:**
```
VOICE_SAMPLE: uploaded ✓
```

---

### 📥 COLLECT: Brand Assets

**What to do:** Client uploads to GDrive `Brand Assets` subfolder:
- Logo (PNG transparent + white versions)
- Brand colors (hex codes or screenshot)
- Preferred fonts (if any)
- Top 5 best-performing posts (links + screenshots with engagement data)
- Testimonial screenshots

**Confirm here when received:**
```
BRAND_ASSETS: received ✓
```

---

**DAY 1 COMPLETE WHEN:** Onboarding JSON saved + all 4 Client Info docs in + voice sample in + brand assets in.

---

## 📅 DAY 2 — FULL BUILD (Biggest Auto-Run Day)

**Status:** ⬜ Not Started | 🟡 In Progress | ✅ Done

> **Requires:** `ONBOARDING_JSON: saved ✓` + `CLIENT_INFO: ready ✓` from Day 1
> When you say "execute" and these are confirmed, I run all 8 tasks below in sequence.

---

### 🤖 AUTO: Process Client Info → Content Angles + Swipe File

> Reads all 4 `client_info/` docs → extracts:
> - 5 authenticity reel hooks from life story
> - 5 value-CTA hooks from PMF
> - Their unique mechanism (1-liner)
> - Avatar emotional journey
> Saves to: `swipe_file.md` + `content_angles.md`

---

### 🤖 AUTO: Build Swipe File + Graphics Guide

> Reads onboarding JSON + brand assets + Client Info
> Saves: `swipe_file.md` (full) + `graphics/color_palette.md`

---

### 🤖 AUTO: Run Offer Agent → Generate Offer Sheet

```bash
python tools/offer_agent.py --from-file "Fulfillment/_CLIENT_DELIVERABLES/[CLIENT]/onboarding.json"
```

> Saves: `offer_sheet.md` + `offer_sheet.json`

---

### 🤖 AUTO: Generate Sales Call Script

> Reads `swipe_file.md` + `offer_sheet.md`
> Saves: `sales_call_script.md`

---

### 🤖 AUTO: Generate 7-Email Nurture Sequence

> Reads swipe file + offer sheet → 7 emails (Day 0, 1, 3, 5, 7, 10, 14)
> Saves: `email_sequence.md`

---

### 🤖 AUTO: Generate Ad Copy (3 Platforms)

> Facebook (3 variants) + Instagram (3 variants) + LinkedIn (2 variants)
> Saves: `ad_copy.md`

---

### 🤖 AUTO: Generate DFY Bonus Stack (5 Bonuses — Full Content)

> Uses `Fulfillment/_OFFER_BLUEPRINT/dfy_deliverables_prompts.md` → PROMPT 1
> Reads swipe file + offer sheet + PMF + offer positioning
> Saves: `bonuses/bonus_1.md` through `bonus_5.md` + `bonus_stack_summary.md`

---

### 🤖 AUTO: Generate Transformation Roadmap (4 Phases)

> Uses PROMPT 2 from dfy_deliverables_prompts.md
> Reads swipe file + offer sheet + PMF + life story + produk
> Saves: `roadmap.md`

---

**Jordan reviews at end of Day 2:**

```
OFFER_SHEET_APPROVED: ✓ / needs changes: [notes]
SWIPE_FILE_APPROVED: ✓ / needs changes: [notes]
```

*→ If changes needed, describe them here and I revise.*

---

**DAY 2 COMPLETE WHEN:** All 8 outputs saved and approved.

---

## 📅 DAY 3 — SALES TOOLKIT + VOICE SETUP

**Status:** ⬜ Not Started | 🟡 In Progress | ✅ Done

---

### 🤖 AUTO: Export Offer Sheet → PDF-Ready HTML

> Reads `offer_sheet.md` → generates styled HTML for PDF print
> Saves: `funnel/offer_sheet.html`

---

### 🤖 AUTO: Generate VSL Script

> Reads swipe file + offer sheet + all client_info docs
> Structure: Hook → Story → Problem → Solution → Proof → Offer → CTA
> Saves: `vsl_script.md` (teleprompter format)

---

### 🤖 AUTO: Start Building Netlify VSL Funnel HTML

> Reads `vsl_script.md` + offer sheet + color palette
> Generates full 1-page VSL funnel HTML (Wistia embed slots, brand colors, booking link)
> Saves: `funnel/index.html` (with placeholder Wistia IDs — to be replaced Day 4)

---

### ⚙️ PLATFORM: ElevenLabs Voice Clone Setup

**Jordan does:**
1. Go to [elevenlabs.io](https://elevenlabs.io) → Voices → Add a new voice → Instant Voice Cloning
2. Upload the 5-10 min voice sample from GDrive
3. Name the voice: `[CLIENT NAME]`
4. Test with: "Halo, ini adalah saya. Terima kasih sudah bergabung."
5. Copy the Voice ID from the URL or API section

**Paste here:**
```
ELEVENLABS_VOICE_ID:
```

*→ Claude saves this to profile + uses it for all voiceover generation.*

---

**DAY 3 COMPLETE WHEN:** VSL script approved + funnel HTML drafted + Voice ID collected.

---

## 📅 DAY 4 — FILMING + FUNNEL LIVE

**Status:** ⬜ Not Started | 🟡 In Progress | ✅ Done

---

### 🤖 AUTO: Generate Onsite Filming Shot List

> Reads swipe file + content calendar (if started) + offer sheet
> Generates printable shot list: talking head setups, b-roll, VSL recording, testimonials, asset photos
> Saves: `filming_brief.md`

---

### 🎬 ONSITE: Filming Session (2 Hours)

**Jordan does:**
- [ ] Film talking head clips (5-8 angles/backgrounds)
- [ ] Film b-roll (15-20 clips)
- [ ] Direct VSL recording (use teleprompter from `vsl_script.md`)
- [ ] Film testimonial clips (if client's clients available)
- [ ] Shoot asset photos
- [ ] Upload all raw footage to GDrive

---

### 🎬 ONSITE: Edit + Upload to Wistia

**Jordan does:**
- [ ] Edit VSL in CapCut → upload to Wistia → copy media ID
- [ ] Edit testimonial clips → upload to Wistia → copy each media ID

**Paste here:**
```
WISTIA_VSL_ID:
WISTIA_TESTIMONIAL_ID_1:
WISTIA_TESTIMONIAL_ID_2:
WISTIA_TESTIMONIAL_ID_3:
```

---

### 🤖 AUTO: Finalize Netlify Funnel (Real Wistia IDs)

> Takes `funnel/index.html` → replaces placeholder Wistia IDs with real ones above
> Inserts Google Calendar link, WhatsApp link, brand colors
> Saves: `funnel/index.html` (final)

---

### ⚙️ PLATFORM: Deploy to Netlify

```bash
# Jordan runs this or I run it:
cd "c:/Users/natha/OneDrive - Bina Nusantara/Cook/Fulfillment/_CLIENT_DELIVERABLES/[CLIENT]/funnel"
netlify deploy --prod --dir=.
```

**Paste Netlify URL:**
```
NETLIFY_URL:
```

---

### ⚙️ PLATFORM: Booking Calendar + n8n Reminders

**Jordan does:**
- [ ] Connect n8n automation: new booking → WA reminder 24h + 1h before

**Confirm:**
```
BOOKING_REMINDERS: live ✓
```

---

### 🤖 AUTO: Test Checklist Generation

> I generate a test checklist for Jordan to run through the live funnel

---

**DAY 4 COMPLETE WHEN:** Funnel live + Wistia plays + WhatsApp CTA works + calendar link works + mobile tested.

---

## 📅 DAY 5 — CONTENT AUDIT

**Status:** ⬜ Not Started | 🟡 In Progress | ✅ Done

---

### 📥 COLLECT: Last 20 Posts Data

**What to do:** Pull client's last 20 Instagram posts. For each, collect:
- Caption text
- Views / reach / saves / comments
- Post date

**Paste or upload here:**
```
POSTS_DATA: [paste or confirm file uploaded to GDrive]
```

---

### 🤖 AUTO: Run Content Audit

> Reads 20 posts + swipe file → scores each: hook (1-10), CTA clarity (1-10), pillar alignment
> Identifies top 3 content gaps
> Saves: `Fulfillment/_CONTENT_AUDIT/client_audits/[CLIENT]/audit_report.md`

---

### 🤖 AUTO: Match Winning Templates to Client ICP

> Reads swipe file + content audit → rewrites your proven CapCut templates for this client's niche
> Saves: `Fulfillment/_CONTENT_AUDIT/client_audits/[CLIENT]/template_matches.md`

---

**DAY 5 COMPLETE WHEN:** Audit done + templates matched + top 3 gaps identified.

---

## 📅 DAY 7 — FULL CONTENT BATCH

**Status:** ⬜ Not Started | 🟡 In Progress | ✅ Done

> Biggest AUTO day after Day 2. All 7 tasks run in sequence.

---

### 🤖 AUTO: Generate 4-Week Content Calendar (All Platforms)

> IG + TikTok + Threads + YouTube
> Saves: `content_calendar/month_1_calendar.md`

---

### 🤖 AUTO: Batch Generate 30 Reel Scripts

> 15 Authentic + 15 Value-CTA, from matched templates
> Saves: `scripts/reels_batch_1.md`

---

### 🤖 AUTO: Generate 30 Story Sequences

> 14 rotating types (testimonial, value, personal story, win, soft CTA, lifestyle, etc.)
> Saves: `scripts/stories_batch_1.md`

---

### 🤖 AUTO: Generate 30 Threads Posts

> 1/day, from winning outlier formats
> Saves: `scripts/threads_batch_1.md`

---

### 🤖 AUTO: Generate 4 YouTube Scripts

> From winning outline structures
> Saves: `scripts/youtube_batch_1.md`

---

### 🤖 AUTO: Generate Voiceover Scripts (Non-Talking-Head Reels)

> 500-word batch, ElevenLabs-ready format (breath marks, pacing)
> Saves: `voice_clone/generated_audio/vo_scripts_batch_1.md`

---

### 🤖 AUTO: Generate 30 TikTok Mirror Captions

> Rewrites all IG captions for TikTok (shorter, hashtags, CTA style)
> Saves: `scripts/tiktok_captions_batch_1.md`

---

### 📥 COLLECT: Client Calendar Approval

**What to do:** Share `content_calendar/month_1_calendar.md` with client → get approval or revision notes.

**Paste feedback here:**
```
CALENDAR_APPROVED: ✓ / Changes: [notes]
```

*→ If changes: describe here → I revise specific scripts.*

---

**DAY 7 COMPLETE WHEN:** All scripts generated + calendar approved.

---

## 📅 DAY 8 — PRODUCTION + KEYWORD CTAs

**Status:** ⬜ Not Started | 🟡 In Progress | ✅ Done

---

### 🤖 AUTO: Convert Scripts → Remotion Props (Batch)

> Reads approved scripts → generates Remotion JSON files for all 30 reels
> Saves: `remotion_props/batch_1/`

---

### 🤖 AUTO: Generate IG Keyword CTA Pairs

> Reads swipe file → generates 8-12 keyword + auto-DM reply pairs for Meta Business Suite
> All keywords → free resources or YouTube links only
> Saves: `dm_scripts/ig_keyword_cta.md`

---

### 🤖 AUTO: Generate TikTok Keyword CTA Setup

> Same keywords → pinned comment text + DM reply templates + linktree structure
> Saves: `dm_scripts/tiktok_cta.md`

---

### 🎬 ONSITE: CapCut Production

**Jordan does:**
- [ ] Render Remotion drafts → import to CapCut
- [ ] Add b-roll / talking head footage
- [ ] Sync ElevenLabs VO (run API call for marked reels)
- [ ] Apply personal graphics (lower thirds, CTA overlays)
- [ ] Dual export: IG version + TikTok version (no watermark)

---

### ⚙️ PLATFORM: Meta Business Suite — Keyword CTA

**Jordan does:**
1. Open Meta Business Suite → Inbox → Automations
2. Set up each keyword pair from `dm_scripts/ig_keyword_cta.md`
3. Test each one

**Confirm:**
```
IG_KEYWORD_CTA: live ✓
```

---

### ⚙️ PLATFORM: TikTok Keyword CTA

**Jordan does:**
- [ ] Set up Linktree with all resources
- [ ] Pin keyword comment on each reel as it goes up
- [ ] Brief setter on monitoring TikTok DMs

**Confirm:**
```
TIKTOK_CTA: live ✓
```

---

## 📅 DAY 9 — REPURPOSE + ADS

**Status:** ⬜ Not Started | 🟡 In Progress | ✅ Done

---

### 🤖 AUTO: Repurpose 30 Reels → 150+ Content Pieces

```bash
python tools/repurpose_content.py --batch "Fulfillment/_CLIENT_DELIVERABLES/[CLIENT]/scripts/reels_batch_1.md" --client "[CLIENT]"
```

> Saves: `scripts/repurposed_batch_1.md`

---

### 🤖 AUTO: Generate All IG Captions + Hashtags

> Saves: `scripts/ig_captions_batch_1.md`

---

### 🤖 AUTO: Generate Full Meta Ads Setup Tutorial + Creatives

> Pixel setup → audience setup → 3 campaign structure → ad creatives (2 per ad set)
> Saves: `analytics/meta_ads_setup.md`

---

### ⚙️ PLATFORM: Upload TikTok Mirrors

**Jordan does:**
- [ ] Upload all 30 IG reels (no watermark) to TikTok with TikTok captions
- [ ] Mirror 30 stories to TikTok stories

**Confirm:**
```
TIKTOK_MIRRORS: uploaded ✓
```

---

## 📅 DAY 10 — LEAD ACTIVATION + DFY ASSETS

**Status:** ⬜ Not Started | 🟡 In Progress | ✅ Done

---

### 📥 COLLECT: Client's Lead List

**What to do:** Client exports existing leads (DM history, email list, old inquiries) → shares via GDrive.

**Confirm here:**
```
LEAD_LIST: received ✓ | Count: [X] leads
```

---

### 🤖 AUTO: Segment Leads (Hot / Warm / Cold)

> Reads lead list → segments by engagement recency
> Saves: `dm_scripts/lead_segments.md`

---

### 🤖 AUTO: Generate Reactivation Scripts (3 Channels × 3 Variants)

> DM + Email + WhatsApp, each with Hot / Warm / Cold variants
> Saves: `dm_scripts/reactivation_scripts.md`

---

### 🤖 AUTO: Generate DM Closing Playbook

> Warm-up → opener → qualify → pitch → objection handlers → post-booking
> Saves: `dm_scripts/dm_closing_playbook.md`

---

### 🤖 AUTO: Generate Lead Magnet Content

> Uses PROMPT from `dfy_deliverables_prompts.md` → title options + full content + landing page copy + 3 follow-up emails
> Saves: `lead_magnet/lead_magnet_content.md`

---

### 🤖 AUTO: Generate DFY Asset Pack (Notion-Ready)

> Uses PROMPTS 3A–3D from `dfy_deliverables_prompts.md`

**But first — I need these inputs:**

```
FOOD_PREFERENCES: [What does the avatar eat/avoid? Any allergies?]
COOKING_TIME: [e.g., "15 min max weekdays, can do Sunday prep"]
FAMILY_SITUATION: [e.g., "husband + 2 kids", "solo professional"]
TOP_5_RESTAURANTS: [Client's most-visited restaurants]
TRAVEL_FREQUENCY: [How often do they travel? Business/leisure?]
```

> Once above filled → I generate:
> - Shopping list (Notion checkbox format)
> - 7-day meal plan with shortcuts
> - Restaurant guide with exact menu items
> - Travel protocol
> Saves: `lead_magnet/dfy_[type].md` × 4

---

### 🤖 AUTO: Build Full Notion Workspace (Client Deliverable)

> Uses PROMPT 4 from `dfy_deliverables_prompts.md`
> Links all: roadmap + bonuses + DFY assets + daily habits + contact table
> Saves: `lead_magnet/notion_workspace_home.md`
> **Jordan then pastes each file into Notion and sets sharing.**

---

## 📅 DAY 12 — REACTIVATION + TEAM SOPS

**Status:** ⬜ Not Started | 🟡 In Progress | ✅ Done

---

### 🤖 AUTO: Generate Team SOPs (4 Roles)

> Creative Director + Editor + Setter (with IG label system + KPI) + Closer
> Each SOP includes: daily workflow, KPIs, daily report template
> Saves: `dm_scripts/team_sops.md`

---

### 🤖 AUTO: Generate Setter DM Scripts (6 Documents)

> Cold scraping + warm scraping + sequence notes + DM structure + disqualification + ICP criteria
> All in client's niche language and brand voice
> Saves: `dm_scripts/setter_scripts_[type].md` × 6

---

### 🎬 ONSITE: First Reactivation Batch

**Jordan coaches client through:**
- [ ] Send first 10 reactivation messages (using reactivation scripts)
- [ ] Track responses in CRM

**Paste early results here:**
```
REACTIVATION_RESULTS: [X replies / X interested / notes]
```

---

## 📅 DAY 13 — DAY 14 PREP

**Status:** ⬜ Not Started | 🟡 In Progress | ✅ Done

---

### 🤖 AUTO: Generate Day 14 Consultation Prep Brief

> Reads everything generated so far → produces:
> - Full summary of deliverables ready to demo
> - Agenda for the call
> - Client's goals and what to set for months 2-4
> Saves: `day14_prep_brief.md`

---

### 🤖 AUTO: Check Funnel + Systems Before Call

> I generate a pre-call verification checklist covering everything that needs to be live by Day 14.

---

## 📅 DAY 14 — CONSULTATION + LAUNCH

**Status:** ⬜ Not Started | 🟡 In Progress | ✅ Done

---

### 🎬 ONSITE: Consultation Call

**Agenda (use `day14_prep_brief.md`):**
- [ ] Review all deliverables together
- [ ] Launch lead magnet live on the call
- [ ] Test keyword CTA live (comment keyword, watch auto-DM trigger)
- [ ] Walk through content batch → approve first posts
- [ ] Set Month 2, 3, 4 goals
- [ ] Client records first CTA reel live (you coach)

**Call recording (Fathom link):**
```
FATHOM_CALL:
```

---

### 🤖 AUTO: Post-Session Swipe File Update

> After call: paste key learnings/notes below → I update `swipe_file.md` with new context.

```
POST_SESSION_NOTES: [paste anything learned on the call]
```

---

## 📅 DAY 15 — CHROME DASHBOARD + NOTION HANDOVER

**Status:** ⬜ Not Started | 🟡 In Progress | ✅ Done

---

### 🤖 AUTO: Generate Command Center Google Sheet Template

> Full Google Sheets setup with:
> - Daily Dashboard, Content Tracker, Lead Scoreboard, Ad Performance, Weekly KPI, Team Daily Report
> - Formulas + conditional formatting included
> Saves: `analytics/command_center_template.md`

---

### ⚙️ PLATFORM: Notion Workspace Setup

**Jordan does (using all the Notion-ready files already generated):**
1. Create Notion workspace → paste `notion_workspace_home.md` as Home page
2. Create subpages: Roadmap + each Bonus + each DFY Asset
3. Set sharing: invite [client email] → Can view
4. Copy workspace link

**Paste Notion link:**
```
NOTION_WORKSPACE:
```

---

### 🎬 ONSITE: Chrome Dashboard Walkthrough (30 min)

- [ ] Screen share Notion workspace → walk through "start here" path
- [ ] Set up Chrome "Sales HQ" bookmark bar
- [ ] Show client their Command Center Google Sheet

---

**SPRINT COMPLETE** ✅

Update `## 📍 CURRENT STATE` → Day: 15, Phase: Ongoing, Last Completed: Day 15 Handover

---
---

# AFTER DAY 14 — ONGOING DELIVERY

---

## Weekly Cadence

```
MONDAY      🤖 Claude generates: weekly calendar + 8 reel scripts + 8 story sequences +
               7-8 Threads + VO scripts + TikTok captions
            📥 Jordan: review + approve

TUESDAY     🎬 Render Remotion → ElevenLabs VO → CapCut polish → dual export
WEDNESDAY   🎬 CapCut continued → final review → schedule IG + TikTok
THURSDAY    🎬 YT script → CapCut YT edit → Threads scheduled
FRIDAY      🤖 Claude: posting schedule + captions + repurpose batch

DAILY       ⚙️ n8n: auto check-in to client (Claude writes messages)
SUNDAY      ⚙️ n8n: weekly progress summary to client (Claude writes)

BI-WEEKLY   🤖 Lead reactivation refresh + swipe file update
MONTHLY     🤖 Performance analysis + funnel update + ad refresh + strategy call
```

---

## Monthly Review Log

| Month | Revenue | Leads | Best Content | Pivot Made | Renewal? |
|-------|---------|-------|--------------|------------|----------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

---

## Weekly Call Log (Every [DAY] at [TIME])

| Week | Date | Wins | Issues | Action Items |
|------|------|------|--------|--------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

---

## Client Health Check (Run Before Every Weekly Call)

- [ ] Posting consistently (3-4 reels/week)?
- [ ] Setter hitting DM KPIs (1+ booking/day)?
- [ ] Leads converting to calls?
- [ ] Content quality improving?
- [ ] Client responsive and engaged?
- [ ] Funnel converting (VSL watch rate, calendar bookings)?
- [ ] Renewal / upsell conversation needed?

> **Last check date:**
> **Notes:**

---

*Last updated by Claude:*
