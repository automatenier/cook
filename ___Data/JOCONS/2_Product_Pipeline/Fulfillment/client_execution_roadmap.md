---
tags:
  - consulting
---
# Client Execution Roadmap (AI-Powered)

> Chronological playbook from the moment a client signs. Every step shows what's automated by Claude vs what you do manually. Matches ALL deliverables from the JO Consult offer sheet.

---

## Overview

| Metric | Value |
|--------|-------|
| **Total Timeline** | 14-day sprint → 4-month engagement (or 12-month premium) |
| **Claude Tokens Per Client (Onboarding)** | ~250K input + ~255K output |
| **Claude Tokens Per Client (Monthly)** | ~270K input + ~240K output |
| **ElevenLabs** | Included in your 1-year plan (shared across clients) |
| **Your Manual Time** | ~12-15 hours across 14-day sprint |
| **Without AI** | ~30-40 hours |

### Deliverable Count (Per Offer Sheet)

| Deliverable | Quantity | AI-Generated | You Finish |
|-------------|----------|-------------|------------|
| Reels (Authentic) | 15/month | Script + Remotion draft | CapCut polish |
| Reels (Value & CTA) | 15/month | Script + Remotion draft | CapCut polish |
| TikTok mirror (from IG reels) | 30/month | Auto-reformat captions | Upload via CapCut TikTok export |
| Story templates | 30/month | Script + slide text | CapCut design |
| TikTok stories mirror | 30/month | Same assets | Upload to TikTok stories |
| YouTube scripts | 4/month | Full outline + script | Record + edit |
| Threads posts | 30/month (1/day) | Full post from outliers | Review & post |
| ElevenLabs voiceovers | 500 words/batch | Script text | API call + sync in CapCut |
| Lead magnet | 1 (free) | Content + design brief | Canva design |
| Wistia VSL video | 1 setup | — | Record + edit + upload |
| Wistia testimonial videos | 3-5 clips | — | Edit + upload |
| Netlify VSL funnel | 1 | Full HTML (Wistia embeds) | Deploy + test |
| Onsite filming session | 2 hrs JABODETABEK | Shot list + brief | Film + direct |
| AI asset photos (nanobabaabba pro) | As needed | — | Generate if client lacks assets |
| Meta Ads campaign | 1 setup + ongoing | Structure + copy | Launch in Ads Manager |
| Setter DM scripts | 6 documents | Full scripts per stage | Review & customize |
| Client Info docs | 4 documents | Process into content angles | Client fills out |
| IG keyword CTA | Setup once | Keyword pairs | Configure in Meta Biz Suite |
| TikTok keyword CTA | Setup once | Keyword pairs | Configure manually in TikTok |

---

### Core Principle: Client Swipe File

Every client gets a **swipe file** — a living knowledge base that Claude reads before every task.

```
Fulfillment/_CLIENT_DELIVERABLES/{client_name}/
├── swipe_file.md              ← Claude reads this FIRST for every task
├── onboarding.json            ← Raw onboarding data
├── offer_sheet.md             ← Generated offer
├── brand_voice_samples/       ← 5-10 of their best captions/scripts
├── testimonials/              ← Screenshots, quotes, video links
├── achievements/              ← Before/after photos, milestone screenshots
├── winning_content/           ← Their top-performing posts (data + captions)
├── graphics/                  ← Personal branded graphics (colors, overlays, lower thirds)
│   ├── color_palette.md       ← Brand colors, fonts, style guide
│   ├── lower_thirds/          ← Name/title overlays for reels
│   ├── cta_graphics/          ← CTA keyword graphics for reels
│   └── story_templates/       ← Branded story frame templates
├── voice_clone/               ← ElevenLabs voice profile
│   ├── voice_id.txt           ← ElevenLabs voice ID after cloning
│   ├── training_samples/      ← 5-10 min of clean audio for cloning
│   └── generated_audio/       ← Output voiceover files
├── lead_magnet/               ← Free lead magnet assets
├── content_calendar/          ← Weekly calendars
├── scripts/                   ← All generated reel/story/thread/YT scripts
├── remotion_props/            ← Generated Remotion JSON files
├── funnel/                    ← Netlify VSL files
├── gdrive_assets/             ← 10GB GDrive folder structure (link)
├── client_info/               ← Deep client context for engaging reels
│   ├── life_story.md          ← Origin, turning point, purpose, vision
│   ├── product_market_fit.md  ← Current/desired situation, USP, bridge
│   ├── offer_positioning.md   ← Avatar, positioning statement, mechanism
│   └── produk.md              ← Deliverables, coaching structure, bonuses, guarantees
├── dm_scripts/                ← Setter DM scripts per pipeline stage
│   ├── cold_scraping.md       ← Cold outreach scripts
│   ├── warm_scraping.md       ← Warm lead scripts
│   ├── sequence_notes.md      ← Follow-up sequence templates
│   └── disqualification.md    ← Disqualification scripts
└── analytics/                 ← Monthly performance snapshots
```

**The swipe file (`swipe_file.md`) contains:**
- Client avatar, niche, pain points, dream outcome
- Brand voice notes (formal/casual, emoji use, language mix)
- Their ICP description (who they're trying to attract)
- Top 5 performing content pieces + why they worked
- Offer summary (pricing, guarantee, bonuses)
- Content pillars & CTA keywords
- Platform-specific notes (IG aesthetic, Threads tone, YT style)
- **Personal graphics guide** (brand colors, lower third style, CTA graphic format)
- **Voice clone notes** (tone, pacing, which content types use AI voice)
- **Life story summary** (origin, turning point, purpose, vision — for authenticity reels)
- **Product-market fit** (current/desired situation, USP, bridge steps)
- **Offer positioning** (avatar profile, unique mechanism, positioning statement)
- Lessons learned (what bombed, what converted)

> Claude reads this file at the start of every prompt. Cost: ~1-2K extra input tokens per task. Tiny cost, massive quality improvement over time.

---

## Phase 0: Client Signs (Day 0)

### 0.1 — Payment Confirmed
- **Trigger:** Payment received (manual confirmation or n8n webhook)
- **Action:** Update CRM stage to "Closed"
- **Action:** Create client folder structure (see above)
- **Action:** Set up 10GB Google Drive shared folder for client assets

```bash
python tools/create_excel_crm.py  # if CRM doesn't exist yet
```

### 0.2 — Welcome Email + Google Calendar Booking Link
- **Who:** Claude generates → you review & send
- **Template:** `Fulfillment/_ONBOARDING/welcome_email_template.md`
- **What client gets:**
  - Confirmation they're in
  - What happens next (14-day roadmap overview)
  - **Google Calendar booking link** for Day 14 consultation session
  - **20+ Video Module access link** (Google Drive / course platform)
  - Community access links (WhatsApp group, Telegram)
  - Link to onboarding form
  - Request to **gather their swipe materials** (see 0.3)
  - Request to **record 5-10 min clean audio** for ElevenLabs voice clone

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Personalize welcome email from template | 2,000 | 1,500 |

**Claude shortcut:**
```
Prompt: "Read Fulfillment/_ONBOARDING/welcome_email_template.md and personalize
for [CLIENT NAME], a [AVATAR TYPE] who signed up for [PACKAGE].
Pain point: [X]. Include Google Calendar link: [GCAL_LINK].
Include request to gather: testimonial screenshots, before/after photos,
video demos, achievement screenshots, best-performing content links,
brand assets (logo, colors, fonts), and 5-10 min clean voice recording
for AI voiceover setup. Also include GDrive folder link: [GDRIVE_LINK].
Output ready-to-send email in Indonesian."
```

### 0.3 — Client Asset Collection Request
Ask the client to gather and share (via GDrive shared folder):
- **Testimonial images** — screenshots of client DMs, reviews, comments
- **Before/after photos** — their clients' transformation visuals
- **Video demos** — any existing video content, training clips
- **Achievement screenshots** — certifications, milestones, press mentions
- **Top 5 best-performing posts** — links + screenshots with engagement data
- **Brand assets** — logo, brand colors (hex), preferred fonts
- **Clean voice recording** (5-10 min) — for ElevenLabs voice clone
- **Personal photos/footage** — for personalized reel graphics
- **Life story video** — video of themselves speaking to camera covering origin, turning point, purpose, vision (see 1.5)
- **Product-market fit answers** — current/desired situation, USP, bridge steps
- **Offer positioning answers** — avatar profile, positioning statement, unique mechanism

### 0.4 — Community & Module Access
- **Manual:** Add to WhatsApp group + Telegram community
- **Manual:** Share 20+ video module access (GDrive / course platform)
- **N8n Telegram:** Create dedicated client progress channel
- **Time:** ~15 minutes

---

## Phase 1: Onboarding + Voice Clone (Days 1-3)

### 1.1 — Onboarding Form Collection
- **Who:** Client fills out (async) or you walk through on intake call
- **Template:** `Fulfillment/_ONBOARDING/onboarding_form_template.md`
- **Covers:** 6 phases (Niche, Vehicle, Assets, Roadmap, Value Stack, Pricing)
- **Output:** `Fulfillment/_CLIENT_DELIVERABLES/{client_name}/onboarding.json`

### 1.2 — Asset Handover & Video Modules
- **Manual:** Share relevant video modules based on their package
- **Assets to send:**
  - Training program PDF
  - Nutrition guide (based on their chosen approach)
  - Done-For-You assets (3 selected during onboarding)
  - 14-day & 120-day roadmap guides

### 1.3 — ElevenLabs Voice Clone Setup
- **Who:** You set up using client's audio samples → ElevenLabs API
- **Input:** 5-10 min of client's clean voice recording (from GDrive)
- **Process:**
  1. Upload audio samples to ElevenLabs (your 1-year plan account)
  2. Create voice clone → get Voice ID
  3. Save Voice ID to `voice_clone/voice_id.txt`
  4. Test with a sample script (30 seconds)
  5. Refine voice settings (stability, similarity, style)

```bash
# Clone voice via ElevenLabs API
curl -X POST "https://api.elevenlabs.io/v1/voices/add" \
  -H "xi-api-key: ${ELEVENLABS_API_KEY}" \
  -F "name={client_name}" \
  -F "files=@training_samples/sample1.mp3" \
  -F "files=@training_samples/sample2.mp3" \
  -F "description=Coach voice clone for content production"
```

**Usage per client:**
- 500 words/batch (as per offer sheet = ~3-4 min of audio)
- Used for: non-talking-head reels, story narration, ad voiceovers
- You have 1-year plan with ample tokens — shared across all clients

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| ElevenLabs voice clone setup | N/A (API call) | N/A (included in plan) |
| Generate 500 words of voiceover | N/A (API call) | N/A (included in plan) |
| Monthly voiceover (4 batches × 500 words) | N/A | N/A (included in plan) |

**Claude shortcut (generate voiceover scripts):**
```
Prompt: "Read swipe file for [CLIENT NAME]. Write a voiceover script
for a [VALUE-CTA / AUTHENTICITY] reel about [TOPIC].
500 words max. Natural speaking tone matching their brand voice.
Include: breath marks (||), emphasis markers (*word*),
pacing notes [slow], [normal], [fast].
This will be fed into ElevenLabs TTS."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Voiceover script (500 words) | ~2,000 | ~1,000 |
| Batch 4 voiceover scripts/month | ~6,000 | ~4,000 |

### 1.4 — Build Initial Swipe File + Graphics Guide
- **Who:** Claude compiles from onboarding data + collected assets → you review
- **Input:** Onboarding JSON + client's materials + brand assets
- **Output:** `swipe_file.md` + `graphics/color_palette.md`

**Claude shortcut:**
```
Prompt: "Create a swipe file for [CLIENT NAME] using their onboarding data
[PASTE JSON] and these brand voice samples [PASTE 5 CAPTIONS].
Also create a graphics/color_palette.md with:
- Primary, secondary, accent colors (hex)
- Font recommendations matching their brand
- Lower third style (name + title format)
- CTA graphic style (button shape, color, text style)
- Story frame style (border, background treatment)
Extract from their brand assets: [LOGO COLORS], [EXISTING POSTS STYLE].
Format both files."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Build swipe file + graphics guide | ~6,000 | ~4,000 |

### 1.5 — Client Info Deep Dive (For Engaging Reels)

> Not just the offer sheet — Claude needs their **life story, product-market fit, offer positioning, and produk details** to write reels that actually connect. This is what makes content personal, not generic.

**Client fills out (via Notion forms, GDrive doc, or intake call). Output saved to `client_info/`.**

#### A. Life Story (`client_info/life_story.md`)
- **Video Asset:** Client records video speaking directly to camera covering all points below
- **Asal-Usul (Origin):** Childhood, background, specific events that brought them here — humanizes them to their audience
- **Titik Balik (Turning Point):** How and why they entered coaching — was it a struggle they overcame? A mentor? The transition from "old life" to "new life"
- **Tujuan Utama (Purpose / "Why"):** What drives them beyond money — schooling siblings, changing industry standards, helping 1000 people. "What principle do you fight for?"
- **Visi (Vision):** Long-term goal for their business — helps their audience (and team) see where they're headed

#### B. Product-Market Fit (`client_info/product_market_fit.md`)
- **Current Situation — Surface Problems:** Specific visible problems (e.g., no leads, inconsistent income)
- **Current Situation — Deep Problems:** Root emotional issues (e.g., feeling incompetent, financial insecurity, imposter syndrome)
- **Desired Situation — Surface Wants:** Tangible goals (e.g., Rp 100jt/month, 20 clients)
- **Desired Situation — Deep Wants:** Emotional goals (e.g., freedom, respect from parents, proving doubters wrong)
- **USP — Why Trust You:** Their story/struggle that builds credibility
- **USP — Why Your Process:** What makes their method different from competitors (e.g., "organic, not ads")
- **The Bridge:** 15-30 specific steps from Current → Desired situation

#### C. Offer Positioning (`client_info/offer_positioning.md`)
- **The Avatar (e.g., "Steve"):**
  - Current Situation (1 sentence + detailed paragraph)
  - Desired Situation (1 sentence + detailed paragraph)
- **The Bridge:** Specific actions the avatar takes (onboard → fix offer → launch ads)
- **Positioning Statement:**
  - Identity: Who is the avatar? (aspiring entrepreneur, fitness influencer, etc.)
  - Unique Mechanism: How you help them in a way no competitor does
- **Logistics:** Timeframe, top 3 challenges, guarantees, proof

#### D. Produk Details (`client_info/produk.md`)
- **Deliverables:** 5-7 specific things they get (DFY CRM, weekly calls, funnel rebrand, etc.)
- **Coaching Structure:** How they receive support (1-on-1 onboarding, weekly group, daily Slack, video modules)
- **The Process / Roadmap:** Phase breakdown (Phase 1: Onboarding → Phase 2: Cash Injection → Phase 3: Content Systems)
- **Bonuses (Critical):** Items that save time/money — each with a value/price tag
- **Guarantees:** Conditional ("work free until X") and/or unconditional ("15-day money-back")

**Claude shortcut (process client info into swipe file):**
```
Prompt: "Read the following Client Info documents for [CLIENT NAME]:
- Life Story: [PASTE or reference client_info/life_story.md]
- Product-Market Fit: [PASTE or reference client_info/product_market_fit.md]
- Offer Positioning: [PASTE or reference client_info/offer_positioning.md]
- Produk: [PASTE or reference client_info/produk.md]

Extract key storytelling angles for reels:
1. 5 authenticity reel hooks from their life story (origin, struggle, turning point)
2. 5 value-CTA reel hooks from their PMF (surface problems → their solution)
3. Their unique mechanism (what makes them different) — 1-liner for CTAs
4. Their avatar's emotional journey (for story sequences)
5. Update swipe_file.md with all new context.
Output: updated swipe_file.md + content_angles.md"
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Process client info → swipe file + content angles | ~8,000 | ~5,000 |

---

## Phase 2: Offer Blueprint + Sales Toolkit (Days 2-4)

### 2.1 — Generate Custom Offer Sheet
- **Who:** Claude (via offer agent) → you review
- **Tool:** `tools/offer_agent.py`

```bash
python tools/offer_agent.py --from-file Fulfillment/_CLIENT_DELIVERABLES/{client_name}/onboarding.json
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Offer sheet generation (async mode) | ~6,000 | ~3,000 |

### 2.2 — Generate Sales Call Script
- **Who:** Claude generates from offer sheet → client uses on discovery calls
- **Per offer "Next Steps":** Download sales call script (pre-written)

**Claude shortcut:**
```
Prompt: "Read swipe file and offer sheet for [CLIENT NAME].
Generate a sales call script they can use on discovery calls.
Structure: rapport (2 min) → problem identification (5 min) →
solution presentation (5 min) → objection handling (3 min) →
close (2 min). Include exact phrases in Indonesian.
Reference their specific offer, guarantee, and pricing tiers."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Sales call script | ~5,000 | ~4,000 |

### 2.3 — Generate Email Sequence (7 Emails)
- **Who:** Claude generates → client sends via email tool
- **Per offer "Next Steps":** 7-email pre-written sequence

**Claude shortcut:**
```
Prompt: "Read swipe file and offer sheet for [CLIENT NAME].
Generate a 7-email nurture sequence for their leads:
Email 1: Welcome + story (Day 0)
Email 2: Pain point agitation (Day 1)
Email 3: Social proof / testimonial (Day 3)
Email 4: Behind the scenes / process (Day 5)
Email 5: Objection buster (Day 7)
Email 6: Scarcity / urgency (Day 10)
Email 7: Final CTA + guarantee (Day 14)
Each email: subject line, preview text, body (300-500 words),
CTA button text. Indonesian with English business terms."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| 7-email nurture sequence | ~5,000 | ~6,000 |

### 2.4 — Generate Ad Copy (3 Platforms)
- **Who:** Claude generates → you review → client launches
- **Per offer "Next Steps":** Ad copy for Facebook, Instagram, LinkedIn

**Claude shortcut:**
```
Prompt: "Read swipe file and offer sheet for [CLIENT NAME].
Generate ad copy for 3 platforms:
FACEBOOK: 3 variants (long-form, story-based, testimonial)
INSTAGRAM: 3 variants (hook-heavy, carousel caption, reel caption)
LINKEDIN: 2 variants (professional, thought-leader)
Each variant: headline, primary text, description, CTA.
Target their ICP. Landing page: [NETLIFY_URL]."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Ad copy 3 platforms (8 variants) | ~5,000 | ~5,000 |

### 2.5 — Export to PDF
- **Alternative:** Claude generates styled HTML → print to PDF

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Offer MD → styled HTML for PDF | ~3,000 | ~2,000 |

---

## Phase 3: Netlify VSL Funnel + Calendar System (Days 3-5)

### 3.1 — Wistia Video Setup (VSL + Testimonials)
- **Who:** You guide client on VSL recording → you edit in CapCut → upload to Wistia
- **Wistia account:** Set up project for client with organized folders

**Wistia deliverables:**
1. **VSL (Video Sales Letter)** — 5-15 min video of client presenting their offer
   - Script from offer sheet + client info (Claude generates)
   - Client records to camera (you direct or onsite film)
   - Edit in CapCut → upload to Wistia → get embed code + media ID
2. **Testimonial videos** (3-5 clips) — client's best client transformations
   - Short clips (30-90 sec each) of real results / client stories
   - Edit in CapCut → upload to Wistia → embed in funnel testimonial section
3. **Wistia settings:** Enable turnstile (email capture), set thumbnail, track engagement

**Claude shortcut (VSL script):**
```
Prompt: "Read swipe file + offer sheet + client_info/ for [CLIENT NAME].
Write a VSL script (5-15 min) structured as:
1. Hook — call out avatar's #1 pain (30 sec)
2. Story — client's turning point, from life_story.md (2 min)
3. Problem — why everything else failed, from PMF (2 min)
4. Solution — unique mechanism + bridge steps (3 min)
5. Proof — testimonial references + before/after (2 min)
6. Offer — deliverables, bonuses, guarantee (2 min)
7. CTA — book discovery call / WhatsApp (30 sec)
Indonesian. Natural speaking tone. Include teleprompter-ready format."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| VSL script generation | ~6,000 | ~4,000 |

### 3.2 — Deploy Netlify VSL Funnel
- **Who:** Claude generates customized HTML → you deploy to Netlify
- **Template:** Based on `Index.html` (1-page VSL with Wistia)
- **Components:**
  - **Wistia-hosted VSL** (main video, from 3.1)
  - **Wistia testimonial video embeds** (3-5 clips in testimonial section)
  - Client brand colors + fonts (from graphics guide)
  - Testimonial gallery (video embeds + screenshot images)
  - Transformation before/after grid
  - Offer cards (from offer sheet)
  - FAQ section (customized to niche)
  - WhatsApp CTA button
  - **Google Calendar booking link** for discovery calls

**Claude shortcut:**
```
Prompt: "Read Index.html as template. Read swipe file + offer sheet
for [CLIENT NAME]. Create customized 1-page VSL funnel.
Brand: [from graphics/color_palette.md]. Avatar: [ICP].
Offer: [from offer_sheet]. Testimonials: [LIST].
VSL Wistia media ID: [VSL_ID].
Testimonial Wistia IDs: [TESTIMONIAL_ID_1], [TESTIMONIAL_ID_2], [TESTIMONIAL_ID_3].
WhatsApp: [WA_LINK]. Calendar: [GCAL_LINK].
Embed testimonial videos in the social proof section.
Output complete HTML."
```

```bash
cd Fulfillment/_CLIENT_DELIVERABLES/{client_name}/funnel/
netlify deploy --prod --dir=.
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Generate customized VSL funnel HTML (with Wistia embeds) | ~10,000 | ~8,000 |

### 3.3 — Booking Calendar + Reminder Automation
- **Google Calendar** booking page for client's discovery calls
- **N8n automation:** WA & Email post-booking reminder system
  - 24h before: WhatsApp reminder + session prep tips
  - 1h before: Email reminder + Zoom link
  - No-show: Follow-up message (auto)

**Claude shortcut (generate reminder messages):**
```
Prompt: "Read swipe file for [CLIENT NAME]. Generate 3 reminder
messages for their booked discovery calls:
1. WhatsApp 24h before (warm, prep tips, what to expect)
2. Email 1h before (professional, Zoom link, agenda)
3. No-show follow-up (empathetic, reschedule link)
Indonesian. Match their brand voice."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| 3 booking reminder templates | ~2K input / ~1.5K output |

---

## Phase 4: Content Audit + Winning Template Matching (Days 5-7)

> Claude's job: take YOUR proven CapCut templates/viral structures and rewrite them for the client's ICP. Not inventing — adapting.

### 4.1 — Analyze Client's Existing Content
- **Input:** Client's last 20 posts + swipe file

**Claude shortcut:**
```
Prompt: "Read swipe file for [CLIENT NAME].
Analyze these 20 Instagram posts [PASTE CAPTIONS + METRICS].
Score each: hook (1-10), CTA clarity (1-10), pillar alignment.
Identify: top 3, gaps, frequency issues, voice consistency.
Output structured audit report."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Content audit (20 posts) | ~8,000 | ~4,000 |

### 4.2 — Match Winning Templates to Client ICP
- **Input:** Your winning CapCut templates + client swipe file
- **You provide:** Reel structures, story frameworks, Threads outliers, YT outlines

**Claude shortcut:**
```
Prompt: "Read swipe file for [CLIENT NAME]. Here are my winning templates:

REEL TEMPLATES (15 Authentic + 15 Value-CTA):
[PASTE YOUR TEMPLATE LIBRARY]

STORY TEMPLATES (30 stories, 14 sequential types):
- Testimonial stories, value-breaking, personal stories,
  wins, soft CTAs, lifestyle
[PASTE STORY FRAMEWORKS]

THREADS OUTLIERS:
[PASTE TOP PERFORMERS]

YOUTUBE OUTLINES:
[PASTE WINNING STRUCTURES]

For each, rewrite specifically for [CLIENT NAME]'s ICP.
Keep exact structure. Change examples/context to their niche."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Match all templates to client ICP | ~8,000 | ~6,000 |

### 4.3 — Generate 4-Week Content Calendar
- **Based on:** Audit + matched templates
- **Per offer:** 15 Authentic + 15 Value-CTA reels + 30 stories + 4 YT + 30 Threads (1/day)
- **TikTok:** Mirror all 30 reels + 30 stories (same content, reformatted captions)

**Claude shortcut:**
```
Prompt: "Create 4-week content calendar for [CLIENT NAME].
Per week:
- 4 Authentic reels (using matched templates) → mirror to TikTok
- 4 Value-CTA reels (using matched templates) → mirror to TikTok
- 7-8 story sequences (14 types rotated across month) → mirror to TikTok stories
- 7-8 Threads posts (1 per day, from outlier rewrites)
- 1 YouTube video (from winning outline)
Each: template used, topic, hook, CTA keyword, pillar, posting time.
Include TikTok caption variants (shorter, more hashtags, different CTA style).
All CTA keywords should direct to: free resource link OR YouTube video link.
Format as weekly table."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| 4-week calendar (30 reels + 30 stories + 30 Threads + 4 YT + TikTok mirror) | ~8,000 | ~8,000 |

---

## Phase 5: Content Production — AI Draft Pipeline (Days 7-14+)

> Flow: Claude rewrites templates → ElevenLabs voices non-talking-head segments → Remotion renders text/motion draft → you layer everything in CapCut → final export.

### 5.1 — Reel Script Generation (30 Reels/Month)
- **15 Authentic + 15 Value-CTA** — per offer sheet

**Claude shortcut (batch):**
```
Prompt: "Read swipe file for [CLIENT NAME]. Generate 30 reel scripts:
15 Authentic (using my authenticity templates) and
15 Value-CTA (using my value-CTA templates).
For each: Hook (0-3s), Value/Story (3-10s), CTA/Lesson (10-15s).
On-screen text per segment. CTA keywords from swipe file.
Mark which reels need ElevenLabs voiceover (non-talking-head)
vs which are talking-head only."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| 30 reel scripts (batch, 2 rounds of 15) | ~12,000 | ~18,000 |

### 5.2 — ElevenLabs Voiceover Generation
- **Who:** Claude writes VO scripts → ElevenLabs API generates audio → you sync in CapCut
- **For:** Non-talking-head reels (b-roll + voiceover), story narrations, ad voiceovers
- **Limit per offer:** 500 words/batch

```bash
# Generate voiceover via ElevenLabs API
curl -X POST "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}" \
  -H "xi-api-key: ${ELEVENLABS_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "[VOICEOVER SCRIPT]",
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
  }' --output voice_clone/generated_audio/reel_{n}.mp3
```

**Claude shortcut (voiceover scripts):**
```
Prompt: "Read swipe file for [CLIENT NAME]. From these reel scripts
marked for voiceover, write ElevenLabs-ready VO scripts.
Max 500 words total per batch. Natural speaking tone.
Include: breath marks (||), emphasis (*word*), pacing [slow/fast].
Indonesian. Match their speaking style from voice samples."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| VO scripts (500 words batch) | ~2,000 | ~1,000 |
| ElevenLabs TTS generation | N/A | N/A (included in plan) |

### 5.3 — Story Sequence Generation (30 Stories/Month)
- **Per offer:** 30 stories using 14 sequential types
- **Types rotate:** testimonial, value-breaking, personal story, win highlight, soft CTA, lifestyle, behind-the-scenes, poll, Q&A, tip, myth-bust, before/after, challenge, freebie promo

**Claude shortcut:**
```
Prompt: "Read swipe file for [CLIENT NAME]. Generate 30 story scripts
for this month using my 14 sequential story types:
[LIST TYPES]. Each story: 3-5 slides, text overlay,
engagement prompt (poll/quiz/question). Include which stories
should use ElevenLabs voice narration vs text-only.
Adapt all content to their ICP."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| 30 story sequences | ~8,000 | ~12,000 |

### 5.4 — Threads Posts — 30/Month (1 Per Day, From Winning Outliers)

**Claude shortcut:**
```
Prompt: "Read swipe file for [CLIENT NAME]. Generate 30 Threads posts (1/day).
Using my winning Threads outliers as templates:
[PASTE OUTLIER STRUCTURES]
Mix of: story threads, tip threads, hot-take threads, case study threads,
behind-the-scenes, myth-busting, listicles.
Each: hook line, body (150-300 words), closing CTA.
CTA should drive to: free resource (lead magnet) or YouTube video link.
Adapt all to their ICP + niche. Indonesian."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| 30 Threads posts from outliers (batch) | ~10,000 | ~15,000 |

### 5.5 — YouTube Video Scripts (From Winning Outlines)
- **Per offer:** 4 YouTube content ideas with research-backed thumbnail & titles

**Claude shortcut:**
```
Prompt: "Read swipe file for [CLIENT NAME]. Using my winning YT outline:
[STRUCTURE]. Generate 4 YouTube scripts for topics: [FROM CALENDAR].
Each: 3 title options, thumbnail text, description with timestamps,
tags, full script with chapter breakdown + key talking points.
Include retention bump moments and CTA placements."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| 4 YouTube scripts (from outlines) | ~12,000 | ~16,000 |

### 5.6 — Remotion Video Draft Generation
- **Flow:** Script → Remotion props → MP4 → import to CapCut → add b-roll + talking head + ElevenLabs audio + music → export

```bash
cd remotion
npm run render-value   # → out/value-reel.mp4
npm run render-auth    # → out/auth-reel.mp4
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| 30 script → Remotion props (batch) | ~10,000 | ~6,000 |

**Your CapCut workflow:**
1. Import Remotion MP4 (text/motion layer)
2. Add b-roll footage OR talking head video
3. If non-talking-head: sync ElevenLabs voiceover audio
4. Add transitions, music from your winning CapCut template
5. Apply personal graphics (lower thirds, CTA graphics from graphics/ folder)
6. Export → (~15 min per reel vs ~45 min from scratch)

### 5.7 — TikTok Mirroring (From IG Reels + Stories)
- **All 30 IG reels** → export from CapCut with TikTok-optimized captions (no IG watermark)
- **All 30 IG stories** → mirror to TikTok stories
- **Claude generates TikTok-specific caption variants** (shorter, more hashtags, TikTok trending sounds suggestions, different CTA phrasing)

**Claude shortcut:**
```
Prompt: "Read swipe file for [CLIENT NAME]. Take these 30 IG reel captions
and rewrite for TikTok:
[PASTE IG CAPTIONS]
For each: shorter hook, TikTok-style hashtags (mix niche + trending),
CTA directing to free resource or YouTube link via keyword comment.
Also suggest 2-3 trending TikTok sounds per content pillar.
Output: 30 TikTok captions + 30 story captions."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| 30 TikTok reel captions + 30 story captions | ~8,000 | ~10,000 |

**CapCut workflow for TikTok:**
1. Export same reel without IG watermark from CapCut
2. Swap caption (TikTok version from Claude)
3. Upload to TikTok → add TikTok sound if applicable
4. Mirror stories: same CapCut export → TikTok stories

### 5.8 — Onsite Filming Session (JABODETABEK)
- **Per offer:** 2 hours onsite filming at client's location
- **Purpose:** Produce raw footage for reels, stories, VSL, testimonials, and asset photos
- **When:** Schedule during Week 1-2 (before content production begins)

**Pre-filming brief (Claude generates):**
```
Prompt: "Read swipe file + content calendar for [CLIENT NAME].
Create an onsite filming shot list:
1. TALKING HEAD SETUPS (5-8 angles/backgrounds for reel variety)
2. B-ROLL SHOTS (15-20 clips: workspace, training, coaching, lifestyle)
3. STORY CONTENT (behind-the-scenes moments, equipment, daily routine)
4. VSL RECORDING (teleprompter setup, key segments from VSL script)
5. TESTIMONIAL INTERVIEWS (if client's clients available onsite)
6. ASSET PHOTOS (professional angles for feed, story, funnel graphics)
Include: lighting notes, audio setup, wardrobe suggestions.
Format as printable shot list for filming day."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Onsite filming shot list + brief | ~5,000 | ~4,000 |

**Onsite filming output:**
- 20-30 talking head clips (different angles, backgrounds, outfits)
- 15-20 b-roll clips (activities, workspace, lifestyle)
- VSL full recording (raw)
- 3-5 testimonial recordings (if available)
- 30-50 asset photos (multiple angles, lighting setups)
- Behind-the-scenes footage (for stories)

### 5.9 — AI Asset Photo Generation (nanobabaabba pro)
- **When:** Client resources are lacking — not enough photos, no professional shots, limited visual content
- **Tool:** nanobabaabba pro for generating professional-looking asset photos from different angles
- **Use cases:**
  - Product photos from multiple angles
  - Professional headshots/lifestyle variations
  - Background variations for story templates
  - Before/after visual mockups
  - Branded graphics with client's face/products

**Process:**
1. Upload client's existing photos/footage to nanobabaabba pro
2. Generate variations: different angles, backgrounds, lighting
3. Create asset library for reels, stories, funnel, and ads
4. Save to `graphics/ai_generated/` in client folder

### 5.10 — Multi-Platform Repurposing

```bash
python tools/repurpose_content.py --input "reel caption/transcript" --client "Client Name"
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Repurpose 30 reels → 150+ content pieces (IG + TikTok + Threads + YT) | ~45,000 | ~60,000 |

---

## Phase 6: Meta Keyword CTA + Ads Setup (Days 8-10)

### 6.1 — Instagram Keyword CTA Setup (Meta Business Suite)
- **Per offer:** "Instagram Keyword CTA Setup — automated keyword system for CTA efficiency"
- **How:** Meta Business Suite → Automated Responses → Keyword triggers
- **When someone comments a keyword** → auto-DM with **free resource link** or **YouTube video link**
- **All CTAs direct to free value** — lead magnets, YouTube videos, cheat sheets, mini trainings. No hard sell in DM automation.

**CTA destination strategy:**
- **Free resource keywords** (e.g., "GRATIS", "FREE", "GUIDE") → DM with lead magnet download link
- **Content keywords** (e.g., "TIPS", "VIDEO", "CARA") → DM with relevant YouTube video link
- **Info keywords** (e.g., "INFO", "PROGRAM") → DM with VSL funnel link (still free to watch)
- **The funnel:** Free resource → email capture → nurture sequence → booking → sale

**Setup steps (manual, one-time per client):**
1. Go to Meta Business Suite → Inbox → Automations
2. Create keyword triggers matching client's CTA keywords (from swipe file)
3. Set auto-reply: DM with link to free resource / YouTube video / lead magnet
4. Test with each keyword

**Claude shortcut (generate keyword + auto-reply pairs):**
```
Prompt: "Read swipe file for [CLIENT NAME]. Generate keyword CTA pairs
for Meta Business Suite automation:
- List 8-12 CTA keywords they should use in reels + stories (Indonesian + English)
- For each keyword: the auto-DM reply message (friendly, includes link)
- ALL links should direct to FREE resources:
  - Lead magnet keywords → lead magnet download link
  - Content keywords → specific YouTube video link
  - Tip keywords → cheat sheet / PDF link
  - Info keywords → VSL funnel link (free to watch)
- Include the exact CTA phrase to say in reel (e.g., 'Comment GRATIS untuk dapetin guide-nya')
Format as setup instructions for Meta Biz Suite."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| IG keyword CTA pairs + auto-reply messages | ~4,000 | ~3,000 |

### 6.2 — TikTok Keyword CTA Setup (Manual)
- **TikTok doesn't have Meta Biz Suite automation** — keyword CTA is manual via comment pinning + bio link
- **Strategy:** Same keyword system but manual reply workflow for setter

**TikTok CTA setup (manual, one-time per client):**
1. **Bio link:** Set up Linktree / link-in-bio with all free resources + YouTube links + booking
2. **Pinned comment:** On every reel, pin a comment with the CTA keyword instruction
3. **Auto-reply (manual/setter):** Setter monitors TikTok DMs → when keyword comment detected → send the free resource link via DM
4. **TikTok Creator Tools:** Enable auto-replies if available in client's region

**Claude shortcut (TikTok keyword pairs):**
```
Prompt: "Read swipe file for [CLIENT NAME]. Generate TikTok keyword CTA setup:
- Same 8-12 CTA keywords as Instagram (keep consistent across platforms)
- For each keyword: pinned comment text, DM reply template
- ALL links direct to FREE resources or YouTube videos
- Linktree structure: organize by content pillar
  - [Free Guide] → lead magnet
  - [Watch Full Video] → YouTube
  - [Free Training] → VSL funnel
  - [Book Call] → Google Calendar
- Setter instructions: how to monitor TikTok DMs for keyword comments
Format as TikTok-specific setup guide."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| TikTok keyword CTA setup + linktree structure | ~3,000 | ~3,000 |

### 6.3 — Meta Ads Retargeting Setup
- **Per offer:** "Tutorial & Support Teknis Meta Ads Retargeting — step-by-step, winning structures, 1-1 video call support"
- **Claude generates:** Full campaign structure, ad scripts, audience targeting

**Claude shortcut:**
```
Prompt: "Read swipe file and offer sheet for [CLIENT NAME].
Create complete Meta Ads setup:

1. PIXEL SETUP: Step-by-step for installing Meta Pixel on their
   Netlify VSL funnel (code snippet + placement instructions)

2. AUDIENCE SETUP:
   - Custom audience: website visitors (7/14/30 days)
   - Custom audience: IG engagers (90 days)
   - Custom audience: video viewers (25%/50%/75%)
   - Lookalike audiences: 1%, 3%, 5% from each custom

3. CAMPAIGN STRUCTURE:
   - Campaign 1: Cold traffic (interest-based + lookalike)
   - Campaign 2: Warm retargeting (IG engagers + web visitors)
   - Campaign 3: Hot retargeting (video viewers + form abandoners)

4. AD CREATIVES (2 per ad set):
   - Primary text, headline, description, CTA
   - Use their best-performing reel as creative
   - Landing page: [NETLIFY_URL]

5. BUDGET RECOMMENDATION:
   - Starting budget per campaign
   - Scaling rules (when to increase, when to kill)

Format as step-by-step tutorial they can follow."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Full Meta Ads setup tutorial + campaign structure | 6,000 | 6,000 |

---

## Phase 7: Lead Activation + Lead Magnet (Days 10-14)

### 7.1 — Create Free Lead Magnet
- **Per your content types:** Value & CTA reels drive keyword comments → auto-DM → lead magnet
- **Lead magnet = free value piece** that captures email/WA in exchange
- **Claude generates content** → you design in Canva (or Claude generates HTML)

**Lead magnet options (Claude suggests based on niche):**
- PDF guide (e.g., "7-Day Meal Plan for Busy CEOs")
- Video training (mini workshop, hosted on Wistia)
- Checklist/cheatsheet (1-page, high-value)
- Quiz/assessment (Google Forms → personalized result)

**Claude shortcut:**
```
Prompt: "Read swipe file for [CLIENT NAME]. Create a lead magnet that
converts their ICP. Based on their niche [NICHE] and pain point
[PAIN POINT], design:
1. Lead magnet title (3 options, curiosity-driven)
2. Full content (1500-2000 words for PDF, or outline for video)
3. Landing page copy (headline, bullets, CTA)
4. Thank-you page copy (delivers asset + upsell to discovery call)
5. Follow-up email sequence (3 emails after download)
The lead magnet should position their paid offer as the natural next step.
Format content ready for Canva PDF template."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Lead magnet content + landing page + 3 emails | 4,000 | 5,000 |

### 7.2 — Segment Existing Leads

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Lead segmentation analysis | 4,000 | 2,000 |

### 7.3 — Generate Reactivation Scripts (3 Channels × 3 Variants)

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Full reactivation script set | 4,000 | 4,000 |

### 7.4 — DM Closing & Post-Booking Playbook
- **Per offer:** "Instagram DM Closing & Post-Booking Playbook — broadcast strategy to warm up cold leads with CTAs"

**Claude shortcut:**
```
Prompt: "Read swipe file for [CLIENT NAME]. Create a DM closing playbook:
1. WARM-UP SEQUENCE: 5-day story engagement strategy before DM
2. OPENER SCRIPTS: 3 variants (casual, story-reply, value-drop)
3. QUALIFYING QUESTIONS: 3-5 questions to identify pain + budget
4. PITCH TRANSITION: How to move from DM to booking
5. OBJECTION HANDLERS: Top 5 objections + responses
6. POST-BOOKING: Confirmation message + what to expect
Match their brand voice. Indonesian."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| DM closing playbook | 4,000 | 4,000 |

---

## Phase 8: Consultation Session + Lead Magnet Launch (Day 14)

### 8.1 — Prep Session Brief

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Session prep brief | 6,000 | 3,000 |

### 8.2 — Consultation Agenda
During the Day 14 consultation, cover:
1. Review 14-day deliverables (offer sheet, content calendar, funnel, ads)
2. **Launch free lead magnet** — go live together on the call
3. Review Meta keyword CTA automation (test live)
4. Review first content batch → approve for posting
5. Set goals for Month 2-4
6. **Action:** Client creates their first CTA reel live on the call (you coach them)

### 8.3 — Post-Session: Swipe File Update + Action Items

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Action items + swipe file update | 3,000 | 2,000 |

---

## Phase 9: Team SOPs & Daily Reports (Days 14-21)

> Per offer: "Creative Director, Editor, Setter & Sales SOP & Daily Report"

### 9.1 — Generate Team SOPs
- **Who:** Claude generates SOPs → you customize → deliver to client's team

**Claude shortcut:**
```
Prompt: "Read swipe file for [CLIENT NAME]. Generate team SOPs:

1. CREATIVE DIRECTOR SOP:
   - Daily: Review content calendar, brief editor, approve scripts
   - Weekly: Content performance review, suggest pivots
   - Deliverables checklist + quality standards

2. VIDEO EDITOR SOP:
   - CapCut workflow: import Remotion draft → add b-roll → sync audio → export
   - Quality checklist (aspect ratio, text size, audio levels, CTA timing)
   - File naming convention + GDrive upload process

3. SETTER (DM SALES) SOP:
   DAILY WORKFLOW:
   1. Lihat inbox dan tanggapi pesan masuk
   2. Balas pesan dan aktif kirim 10-15 pesan baru (Max 100/hari)
   3. Pindahkan kontak personal ke (General)
   4. Label system (6 tipe di fitur Instagram):
      - No Tag = Lead
      - Flag = Follower
      - Lead = ICP
      - Shipped = ICP-LongForm
      - Ordered = ICP-Freebie
      - Paid = ICP-CTA
   5. Jika diskualifikasi → kirim Diskualifikasi Skrip
   6. Lanjutkan booking (link form n8n)
   7. Cek form submisi via Telegram
   8. Laporkan EOD (End of Day) via KPI form

   DM SCRIPTS PER STAGE:
   - Cold Scraping scripts (new ICP outreach)
   - Warm Scraping scripts (engaged followers)
   - Sequence Notes (follow-up cadence)
   - DM Skrip & Struktur (conversation flow)
   - Diskualifikasi Protokol (graceful exit)
   - ICP Criteria (qualification checklist)

   KPI DAILY REPORT:
   | Metric | Minimum |
   | Waktu Bekerja | 6-7 Jam |
   | Inbox Check | 100 |
   | New ICP | [target] |
   | Cold Scrape | [target] |
   | Warm Scrape | [target] |

   → Report via Google Form [FORM_LINK]

4. CLOSER/SALES SOP:
   - Pre-call prep checklist
   - Call script framework (from sales call script)
   - Post-call follow-up sequence
   - Close tracking in CRM

Each SOP: step-by-step instructions, KPIs, daily report template.
Format ready to share with team members."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| 4 team SOPs + daily report templates | 6,000 | 8,000 |

### 9.2 — Generate Setter DM Scripts (Per Pipeline Stage)
- **Who:** Claude generates from client info + swipe file → saved to `dm_scripts/`
- **Output:** Complete DM playbook the setter uses daily

**Claude shortcut:**
```
Prompt: "Read swipe file + client_info/ for [CLIENT NAME]. Generate setter DM scripts:

1. COLD SCRAPING (`dm_scripts/cold_scraping.md`):
   - 3 opener variants for cold ICP outreach (story reply, value-drop, direct)
   - Qualifier questions to confirm ICP fit
   - Transition to booking if qualified

2. WARM SCRAPING (`dm_scripts/warm_scraping.md`):
   - 3 opener variants for engaged followers (commented, liked, viewed stories)
   - Value-first approach before pitching
   - Transition to deeper conversation

3. SEQUENCE NOTES (`dm_scripts/sequence_notes.md`):
   - Day 1: Initial DM
   - Day 3: Follow-up if no reply (different angle)
   - Day 7: Value bomb (share relevant content/tip)
   - Day 14: Re-engage or archive
   - Cadence rules (when to pause, when to push)

4. DM SKRIP & STRUKTUR (`dm_scripts/dm_structure.md`):
   - Full conversation flow: opener → qualify → pain agitation → solution tease → booking
   - Objection handlers (busy, price, not sure, need to think)
   - Closing phrases that feel natural

5. DISKUALIFIKASI PROTOKOL (`dm_scripts/disqualification.md`):
   - Graceful exit scripts (not ICP, no budget, wrong timing)
   - Re-engage triggers (when to circle back later)
   - Label update instructions (move to correct IG label)

6. ICP CRITERIA (`dm_scripts/icp_criteria.md`):
   - Checklist: income level, pain point match, readiness signals
   - Red flags (tire kickers, serial course buyers, no urgency)
   - Green flags (asked about pricing, shared pain, engaged 3+ times)

All scripts in Indonesian. Match client's brand voice. Reference their offer/pricing."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Full setter DM script set (6 documents) | ~6,000 | ~8,000 |

### 9.3 — Set Up Team Daily/Weekly Calls
- **Manual:** Schedule recurring calls in Google Calendar
- **Per offer:** Daily & weekly training calls to review performance
- **N8n:** Auto-send agenda before each call (Claude generates)

---

## Phase 10: Scheduling, Distribution & Ongoing (Day 14+)

### 10.1 — Post Scheduling

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Weekly schedule generation | 3,000 | 2,000 |

### 10.2 — WA & Email Post-Booking Automation
- **Per offer:** Automated reminder system to prevent no-shows
- **N8n handles:** WhatsApp (Wassenger API) + Email reminders
- **Trigger:** When prospect books via Google Calendar

---

## Phase 11: N8n → Telegram Progress Tracking (Always On)

### Architecture

```
N8n Automation Hub
├── Trigger: Scheduled (daily 8AM Jakarta)
├── Trigger: Webhook (CRM update, content published, booking)
│
├── Channel: Client Private Group (You + Client)
│   ├── Daily check-in reminder (auto)
│   ├── Weekly progress summary (auto)
│   ├── Content published notifications
│   ├── Lead magnet download count updates
│   └── Milestone celebrations
│
├── Channel: Your Team Internal (You + Team)
│   ├── Daily task summary per client
│   ├── Content pipeline status (drafted/approved/published)
│   ├── Setter daily report summary
│   ├── Overdue action alerts
│   └── Weekly KPI dashboard
│
└── Channel: Your Personal Dashboard
    ├── All-client overview
    ├── Revenue/pipeline summary
    ├── Ad spend vs leads generated
    └── Upcoming deadlines
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Daily client check-in | 1,500 | 500 |
| Weekly progress summary | 2,000 | 1,000 |
| Team daily briefing | 3,000 | 2,000 |
| **Monthly Telegram total (1 client)** | **75,000** | **35,000** |

---

## Phase 12: Client Chrome Dashboard — "Your Sales HQ" (Day 14-15)

> Set up the client's Google Chrome with a bookmarked workspace so they can monitor everything themselves. This makes it feel like a full infrastructure handover — no gatekeeping, they own their system.

### 12.1 — Chrome Profile Setup
- **Manual:** Create a Chrome profile or bookmark folder called "Sales HQ" on client's browser
- **Contents:** Pinned tabs / bookmark bar with ALL their tools

### 12.2 — Dashboard Tabs (Bookmarked)

```
Chrome Bookmark Bar: "Sales HQ — [Client Name]"
│
├── 📊 Analytics & Monitoring
│   ├── Instagram Insights (native)
│   ├── TikTok Analytics (native)
│   ├── YouTube Studio Dashboard
│   ├── Meta Business Suite (keyword CTA + scheduling + inbox)
│   ├── Google Analytics (if connected to Netlify funnel)
│   └── Wistia Analytics (VSL watch rate, engagement)
│
├── 💰 Sales & Leads
│   ├── Excel CRM / Google Sheets CRM (live pipeline)
│   ├── Google Calendar Booking Page (discovery calls)
│   ├── Netlify VSL Funnel (live site)
│   ├── Lead Magnet Landing Page
│   └── Meta Ads Manager (campaign performance)
│
├── 📁 Content & Assets
│   ├── GDrive Asset Folder (10 GB shared)
│   ├── Content Calendar (Google Sheets or Notion)
│   ├── Canva (for lead magnet / story design)
│   └── Wistia Dashboard (video hosting)
│
├── 💬 Communication
│   ├── WhatsApp Web (client support + DM outreach)
│   ├── Telegram Web (progress tracking channels)
│   └── Email (nurture sequences)
│
└── 📋 Team & SOPs
    ├── Team SOPs (Google Docs — CD, Editor, Setter, Sales)
    ├── Daily Report Template (Google Sheets)
    └── Weekly KPI Dashboard (Google Sheets)
```

### 12.3 — Google Sheets "Command Center"
- **Who:** Claude generates → you set up in Google Sheets
- **What:** A single Google Sheet with tabs that the client checks daily

**Claude shortcut:**
```
Prompt: "Create a Google Sheets 'Command Center' template for [CLIENT NAME].
Tabs needed:
1. DAILY DASHBOARD — today's tasks, content to post, DMs to send
2. CONTENT TRACKER — all 30 reels + 30 stories + 30 Threads + 4 YT + TikTok mirrors
   (status: drafted/approved/posted, engagement metrics)
3. LEAD SCOREBOARD — hot/warm/cold counts, conversion funnel,
   weekly new leads, source breakdown (organic/CTA/ads/referral)
4. AD PERFORMANCE — spend, impressions, clicks, leads, cost per lead
5. WEEKLY KPI — setter metrics, content engagement, calls booked,
   show rate, close rate, revenue
6. TEAM DAILY REPORT — each team member's daily submission
Include conditional formatting (green/yellow/red) for KPIs.
Include formulas for automatic calculations.
Output as Google Sheets-ready format with headers + formulas."
```

| Task | Input Tokens | Output Tokens |
|------|-------------|---------------|
| Command Center Google Sheet template | 4,000 | 5,000 |

### 12.4 — Walkthrough Call
- **Manual:** 30-min screen share with client to walk through their Chrome dashboard
- **Show them:** How to check daily metrics, where to find content, how to read the CRM
- **Result:** Client feels full ownership — "this is YOUR sales infrastructure, not mine"

---

## Token Usage Summary: Full Client Lifecycle

> **Session rule:** One phase per session → `/clear` between phases. Run `/compact` before any large generation block. Switch to Haiku with `/model` before any mechanical task block.

### Onboarding Phase (Days 0-14) — One Time

| Task | Input | Output | Model |
|------|-------|--------|-------|
| Welcome email + booking link | 2,000 | 1,500 | Haiku |
| Swipe file + graphics guide | 6,000 | 4,000 | Sonnet |
| ElevenLabs voice clone setup | — | — | — |
| VSL script generation | 6,000 | 4,000 | Sonnet |
| Netlify VSL funnel HTML (with Wistia embeds) | 10,000 | 8,000 | Sonnet |
| Offer sheet generation | 6,000 | 3,000 | Sonnet |
| Sales call script | 5,000 | 4,000 | Sonnet |
| 7-email nurture sequence | 5,000 | 6,000 | Sonnet |
| Ad copy (3 platforms, 8 variants) | 5,000 | 5,000 | Sonnet |
| Offer → PDF HTML | 3,000 | 2,000 | Haiku |
| Booking reminder templates | 2,000 | 1,500 | Haiku |
| Content audit (20 posts) | 8,000 | 4,000 | Sonnet |
| Winning template → ICP matching | 8,000 | 6,000 | Sonnet |
| 4-week content calendar | 6,000 | 6,000 | Haiku |
| 30 reel scripts (Authentic + Value-CTA) | 12,000 | 18,000 | Sonnet |
| Voiceover scripts (first batch 500w) | 2,000 | 1,000 | Haiku |
| 30 story sequences | 8,000 | 12,000 | Haiku |
| 30 Threads posts (1/day, from outliers) | 10,000 | 15,000 | Haiku |
| 4 YouTube scripts (from outlines) | 12,000 | 16,000 | Sonnet |
| 30 Remotion props (batch) | 10,000 | 6,000 | Haiku |
| 30 TikTok reel + story captions (mirror) | 8,000 | 10,000 | Haiku |
| Onsite filming shot list + brief | 5,000 | 4,000 | Haiku |
| 30 repurposed content sets | ~~45,000~~ | ~~60,000~~ | **Tool** → `repurpose_content.py` |
| IG keyword CTA setup | 4,000 | 3,000 | Haiku |
| TikTok keyword CTA setup | 3,000 | 3,000 | Haiku |
| Meta Ads full setup tutorial | 6,000 | 6,000 | Sonnet |
| Lead magnet content + emails | 4,000 | 5,000 | Sonnet |
| Lead segmentation | 4,000 | 2,000 | Haiku |
| Reactivation scripts (3ch × 3var) | 4,000 | 4,000 | Sonnet |
| DM closing playbook | 4,000 | 4,000 | Sonnet |
| Client info → swipe file + content angles | 8,000 | 5,000 | Sonnet |
| Setter DM scripts (6 documents) | 6,000 | 8,000 | Sonnet |
| 4 team SOPs + daily reports | 6,000 | 8,000 | Sonnet |
| Command Center Google Sheet | 4,000 | 5,000 | Haiku |
| Consultation session prep | 6,000 | 3,000 | Sonnet |
| Post-session + swipe file update | 3,000 | 2,000 | Haiku |
| **ONBOARDING TOTAL (tool-routed)** | **~205,000** | **~195,000** | — |

> Repurpose task moved to Python tool saves ~105K tokens per onboarding.

### Monthly Ongoing — Per Client

| Task | Input | Output | Model |
|------|-------|--------|-------|
| 4 weekly content calendars | 20,000 | 20,000 | Haiku |
| 30 reel scripts (15 Authentic + 15 Value-CTA) | 12,000 | 18,000 | Sonnet |
| 30 story sequences (14 types rotated) | 8,000 | 12,000 | Haiku |
| 30 Threads posts (1/day, from outliers) | 10,000 | 15,000 | Haiku |
| 4 YouTube scripts (from outlines) | 12,000 | 16,000 | Sonnet |
| 4 voiceover scripts (500w batches) | 6,000 | 4,000 | Haiku |
| 30 Remotion props | 10,000 | 6,000 | Haiku |
| 30 TikTok reel + story captions (mirror) | 8,000 | 10,000 | Haiku |
| 30 repurposed content sets (→ 150+ pieces) | ~~45,000~~ | ~~60,000~~ | **Tool** → `repurpose_content.py` |
| 30 captions + hashtags (IG) | 18,000 | 12,000 | Haiku |
| 4 weekly schedules (IG + TikTok) | 10,000 | 8,000 | Haiku |
| 2 lead reactivation refreshes | 8,000 | 8,000 | Sonnet |
| Telegram automation (30 days) | 75,000 | 35,000 | **Haiku** (n8n-triggered) |
| 2 session prep briefs | 12,000 | 6,000 | Sonnet |
| 2 swipe file updates | 6,000 | 4,000 | Sonnet |
| 1 funnel update (new testimonials) | 4,000 | 3,000 | Haiku |
| 1 monthly performance analysis | 5,000 | 4,000 | Sonnet |
| ElevenLabs TTS (4 batches × 500w) | — | — | — |
| **MONTHLY TOTAL (tool-routed, model-split)** | **~225,000** | **~181,000** | — |

> Repurpose tool saves ~105K/month. Haiku for Telegram + mechanical tasks saves another ~40K.

### Token Projection Per Client Count

| Clients | Onboarding (optimized) | Monthly (optimized) | Month 1 Total |
|---------|------------------------|---------------------|---------------|
| 1 | 400K tokens | 406K tokens | ~806K tokens |
| 3 | 1.2M tokens | 1.22M tokens | ~2.42M tokens |
| 5 | 2.0M tokens | 2.03M tokens | ~4.03M tokens |
| 10 | 4.0M tokens | 4.06M tokens | ~8.06M tokens |

> **Model routing:** Sonnet for strategy/quality generation. Haiku for mechanical rewrites, templates, captions, props, scheduling, Telegram. Tool for repurposing. Run `/model` before each task block — don't let Sonnet handle Haiku work.

---

## Chronological Checklist

```
DAY 0  ☐ Payment confirmed → update CRM
       ☐ Create client folder structure + 10GB GDrive shared folder
       ☐ Generate & send welcome email with Google Calendar link (Claude)
       ☐ Send asset collection request (testimonials, photos, demos, voice recording)
       ☐ Send Client Info forms (Life Story, PMF, Offer Positioning, Produk)
       ☐ Send community invites (WhatsApp/Telegram)
       ☐ Share 20+ video module access
       ☐ Set up Telegram progress channels via n8n

DAY 1  ☐ Onboarding form sent / intake call scheduled
       ☐ Asset handover (training PDF, nutrition guide, DFY assets, roadmaps)
       ☐ Client starts gathering swipe materials + recording voice sample
       ☐ Client starts filling Client Info (Life Story video, PMF, Positioning, Produk)

DAY 2  ☐ Onboarding form completed → save as JSON
       ☐ Client Info collected → save to client_info/ (life_story, PMF, positioning, produk)
       ☐ Process Client Info → content angles + updated swipe file (Claude)
       ☐ Build swipe file + graphics guide from onboarding + assets (Claude)
       ☐ Run offer agent → generate offer sheet (Claude)
       ☐ Generate sales call script (Claude)

DAY 3  ☐ Generate 7-email nurture sequence (Claude)
       ☐ Generate ad copy for 3 platforms (Claude)
       ☐ Export offer sheet to PDF (Claude)
       ☐ Set up ElevenLabs voice clone from client audio
       ☐ Generate VSL script from client info + offer sheet (Claude)
       ☐ Start building Netlify VSL funnel HTML (Claude)

DAY 4  ☐ Onsite filming session (2 hrs JABODETABEK) — use shot list from Claude
       ☐ Client records VSL video (you direct using VSL script)
       ☐ Record testimonial videos (if client's clients available)
       ☐ Shoot asset photos from multiple angles
       ☐ If client lacks photo assets → generate via nanobabaabba pro
       ☐ Edit VSL in CapCut → upload to Wistia → get media ID
       ☐ Edit testimonial clips → upload to Wistia → get media IDs
       ☐ Deploy funnel to Netlify (with Wistia VSL + testimonial embeds)
       ☐ Set up booking calendar + WA/email reminder automation (n8n)
       ☐ Test: funnel, Wistia playback, WhatsApp CTA, calendar link, mobile

DAY 5  ☐ Collect client's last 20 posts
       ☐ Run content audit (Claude)
       ☐ Match winning templates to client ICP (Claude)
       ☐ Test ElevenLabs voice clone with sample script

DAY 7  ☐ Generate 4-week content calendar — IG + TikTok + Threads + YT (Claude)
       ☐ Batch generate 30 reel scripts — 15 Authentic + 15 Value-CTA (Claude)
       ☐ Generate 30 story sequences using 14 types (Claude)
       ☐ Generate 30 Threads posts — 1/day from outliers (Claude)
       ☐ Generate 4 YouTube scripts from winning outlines (Claude)
       ☐ Generate voiceover scripts for non-talking-head reels (Claude)
       ☐ Generate 30 TikTok mirror captions from IG reels (Claude)
       ☐ Client reviews & approves calendar

DAY 8  ☐ Convert scripts → Remotion props (Claude)
       ☐ Render Remotion video drafts
       ☐ Generate ElevenLabs voiceovers for marked reels
       ☐ Layer everything in CapCut (Remotion + b-roll + VO + personal graphics)
       ☐ Export CapCut reels for both IG and TikTok (no watermarks)
       ☐ Set up IG keyword CTA automation in Meta Biz Suite (Claude generates pairs)
       ☐ Set up TikTok keyword CTA manually (bio link, pinned comments, setter DM flow)
       ☐ All CTA keywords → free resources or YouTube video links

DAY 9  ☐ Repurpose 30 reels → 150+ content pieces across IG + TikTok + Threads (Claude)
       ☐ Generate all captions & hashtags — IG + TikTok versions (Claude)
       ☐ Upload TikTok mirrors (reels + stories)
       ☐ Set up Meta Ads retargeting (Claude generates full tutorial)

DAY 10 ☐ Segment client's existing leads (Claude + CRM)
       ☐ Generate reactivation scripts (Claude)
       ☐ Generate DM closing playbook (Claude)
       ☐ Create lead magnet content (Claude)

DAY 12 ☐ Send first batch of reactivation messages
       ☐ Track responses in CRM + Telegram
       ☐ Generate team SOPs + daily report templates (Claude)
       ☐ Generate setter DM scripts — 6 docs: cold, warm, sequence, structure, disqualification, ICP criteria (Claude)
       ☐ Share SOPs + DM scripts with client's team (CD, editor, setter)

DAY 13 ☐ Generate consultation session prep brief (Claude)
       ☐ Prepare lead magnet for launch

DAY 14 ☐ Consultation call (via Google Calendar)
       ☐ Launch lead magnet live on the call
       ☐ Test keyword CTA automation live
       ☐ Review first content batch together
       ☐ Set Month 2-4 goals
       ☐ Update swipe file with learnings (Claude)

DAY 15 ☐ Generate Command Center Google Sheet (Claude)
       ☐ Set up client Chrome profile / bookmark bar with "Sales HQ"
       ☐ Pin all dashboard tabs (analytics, CRM, funnel, ads, GDrive, team SOPs)
       ☐ 30-min walkthrough call — show client their full infrastructure
       ☐ Transition to ongoing monthly cycle
```

---

## Ongoing Monthly Cycle (Post Day 14)

| Day | AI Tasks | Manual Tasks |
|-----|----------|-------------|
| **Every Monday** | Generate weekly content calendar + 8 reel scripts + 8 story sequences + 7-8 Threads + VO scripts + TikTok captions (Claude) | Review & approve all scripts |
| **Every Tue-Thu** | Render Remotion drafts + ElevenLabs VO + generate YT scripts (Claude) | CapCut polish → dual export IG + TikTok |
| **Every Friday** | Generate posting schedule + captions + repurpose content (Claude) | Final review, schedule IG + TikTok + Threads posts |
| **Daily (auto)** | Telegram check-in to client (n8n + Claude) | Respond to client replies |
| **Sunday (auto)** | Weekly progress summary to client (n8n + Claude) | Review metrics |
| **Bi-weekly** | Lead reactivation refresh + swipe file update (Claude) | Send messages + track CRM |
| **Monthly** | Performance analysis + funnel update + ad refresh + lead magnet V2 (Claude) | Strategy call with client |
| **Weekly** | Team daily briefing (n8n + Claude) | Attend 4x group calls per offer |

---

## What You Still Do (The Human Touch)

1. **Record talking head videos** — your face, your energy
2. **CapCut final editing** — b-roll, transitions, music, personal graphics (from your winning templates)
3. **Export to both IG + TikTok** — same CapCut project, dual export (no watermark)
4. **Upload TikTok mirrors** — reels + stories mirrored from IG content
5. **Send DMs personally** — relationship-building stays human
6. **Strategy calls** — 4x weekly group calls + 1-1 sessions per offer
7. **Review & approve** — every AI output gets your final check
8. **Onsite filming JABODETABEK** (2 hours per offer) — talking heads, b-roll, VSL, testimonials, asset photos
9. **Direct VSL recording** — coach client through VSL script on camera
10. **Edit VSL + testimonial clips** → upload to Wistia
11. **Generate AI asset photos** (nanobabaabba pro) — when client lacks professional photos
12. **Meta Ads Manager** — launch + monitor campaigns (Claude drafts everything)
13. **Meta Biz Suite** — configure IG keyword CTA automation (Claude generates the pairs)
14. **TikTok keyword CTA** — manual setup (bio link, pinned comments, setter monitors DMs)

## What Claude Handles (The AI Engine)

1. **Swipe file management** — learns per client, improves over time
2. **Winning template → ICP rewriting** — your proven structures, their context
3. **30 reel scripts/month** — 15 Authentic + 15 Value-CTA from winning templates
4. **30 story sequences/month** — 14 rotating types adapted to ICP
5. **30 Threads posts/month** (1/day) — from your proven outlier formats
6. **4 YouTube scripts/month** — from your winning outlines
7. **ElevenLabs voiceover scripts** — natural VO for non-talking-head content
8. **Remotion video draft props** — text/motion layers for CapCut
9. **TikTok mirror captions** — 30 reel + 30 story captions reformatted for TikTok
10. **150+ repurposed content pieces/month** — 1 reel → IG + TikTok + Threads + YT
11. **VSL script** — full teleprompter-ready script from client info + offer sheet
12. **Netlify VSL funnel** — customized 1-page with Wistia VSL + testimonial video embeds
13. **Sales toolkit** — call script + 7 emails + ad copy (3 platforms)
14. **Lead magnet content** — free value piece + landing page + follow-up emails
15. **IG keyword CTA automation** — keyword/auto-reply pairs for Meta Biz Suite (all → free resources/YT links)
16. **TikTok keyword CTA pairs** — same keywords + DM templates + linktree structure (manual setup)
17. **Meta Ads structure** — full retargeting tutorial + campaign setup + creatives
18. **DM closing playbook** — scripts for each pipeline stage + objection handlers
19. **Setter DM script set** — 6 documents (cold, warm, sequence, structure, disqualification, ICP criteria)
20. **Client Info → content angles** — life story, PMF, positioning processed into reel hooks + storytelling angles
21. **Onsite filming shot list** — talking head setups, b-roll, asset photos, VSL recording brief
22. **Team SOPs** — Creative Director, Editor, Setter (with IG label system + KPI), Sales + daily report templates
23. **Lead segmentation & reactivation** — 3 channels × 3 variants
24. **Telegram progress tracking** — automated daily/weekly via n8n
25. **Session prep & swipe file updates** — briefings that get smarter
26. **Scheduling** — optimal posting times & weekly plans (IG + TikTok coordinated)

## What ElevenLabs Handles (The Voice Engine)

1. **Voice cloning** — one-time setup per client from 5-10 min audio
2. **Non-talking-head voiceovers** — b-roll reels with client's cloned voice
3. **Story narrations** — voice-over for text-heavy story slides
4. **Ad voiceovers** — cloned voice for Meta ad audio
5. **Cost:** Included in your 1-year plan — shared token quota across all clients
