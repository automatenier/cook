---
tags:
  - consulting
---
# Client Deliverable Map — Complete Package

> Everything a client receives when they sign. Every system, template, dashboard, automation, and asset — mapped out.
> Stack: Excel (hub) + n8n (automation) + Telegram (client interface) + Remotion→CapCut (production)

---

## Master Deliverable Index

| # | Deliverable | Type | Setup/Ongoing | Client Touches It? |
|---|------------|------|---------------|-------------------|
| 1 | Content Calendar Sheet | Excel | Setup + monthly | Yes — reviews, approves |
| 2 | CEO Dashboard Sheet | Excel | Setup + auto-updates | Yes — checks weekly |
| 3 | Swipe File Library Sheet | Excel | Setup + grows monthly | Yes — browses for ideas |
| 4 | Hook & CTA Bank Sheet | Excel | Setup + grows | Yes — picks favorites |
| 5 | Prompt Library Doc | Google Docs | Setup + grows | Yes — self-serve scripting |
| 6 | 14 DFY Reels/Month | Video files | Monthly | Yes — approves via Telegram |
| 7 | 70+ Repurposed Pieces/Month | Text content | Monthly | Yes — copy-paste to post |
| 8 | Telegram Approval Bot | n8n + Telegram | Setup + always-on | Yes — daily interaction |
| 9 | Keyword CTA Automation | Meta Business Suite | Setup + maintained | Yes — tests it |
| 10 | VSL Funnel | Netlify + Wistia | Setup (one-time) | Yes — shares link |
| 11 | Setter Scripts (Customized) | Google Docs | Setup (one-time) | Yes — setter uses daily |
| 12 | ElevenLabs Voice Clone | ElevenLabs | Setup (one-time) | No — backend |
| 13 | Offer Sheet | Google Docs/PDF | Setup (one-time) | Yes — uses on calls |
| 14 | AI Solopreneur Module | Video course | Setup + access | Yes — watches + learns |
| 15 | Weekly Mastermind | Live call | Weekly | Yes — attends |
| 16 | Monthly 1-on-1 Consultation | Live call | Monthly | Yes — attends |
| 17 | Private Community | Telegram group | Always-on | Yes — daily |
| 18 | Chrome Sales HQ Bookmarks | Chrome profile | Setup (one-time) | Yes — daily workspace |

---

## Deliverable #1: Content Calendar Sheet

**What:** Excel workbook — the single source of truth for all content.
**n8n reads this** → triggers Telegram notifications → schedules posts.

### Tabs

#### Tab 1: `Calendar` (Main View)

| Column | Description | Who Fills |
|--------|------------|-----------|
| `Week` | Week number (1-4) | Auto |
| `Date` | Posting date | Team |
| `Day` | Mon-Sun | Auto |
| `Reel #` | 1-14 | Auto |
| `Topic` | Reel topic | Team |
| `Swipe Structure` | Which viral structure (linked to Swipe File) | Team |
| `Hook` | The hook line | Team |
| `Script Status` | Draft → Review → Approved | Team → Client |
| `Script Link` | Link to Google Doc with full script | Team |
| `Edit Status` | Remotion → CapCut → Done | Team |
| `Preview Link` | GDrive link to preview MP4 | Team |
| `Client Approval` | Pending → Approved → Revisi | Client (via Telegram or Sheet) |
| `Client Notes` | Feedback / masukan from client | Client |
| `Telegram Sent` | Yes/No (H-12 notification) | Auto (n8n) |
| `Posted` | Yes/No | Auto (n8n) |
| `Platform` | IG / TikTok / Both | Team |
| `CTA Keyword` | The keyword for auto-DM | Team |
| `Caption` | Full caption text | Team |
| `Threads Post` | Repurposed Threads text | Team |
| `Story Slides` | Link to story slide scripts | Team |
| `TikTok Caption` | TikTok-specific caption | Team |

#### Tab 2: `Repurposed Content`

| Column | Description |
|--------|------------|
| `Reel #` | Linked to Calendar tab |
| `Threads Post` | Full text — client copy-pastes |
| `Story Slide 1-5` | Text per slide |
| `Newsletter Snippet` | Email-ready paragraph |
| `YouTube Outline` | Long-form script outline |
| `TikTok Caption` | TikTok-specific version |
| `LinkedIn Post` | If applicable |

#### Tab 3: `Footage Inventory`

| Column | Description |
|--------|------------|
| `Filename` | e.g., `busyfit_aroll_cta-dm_01.mp4` |
| `Type` | A-Roll / B-Roll / Screen / Testimonial |
| `Description` | What's in the clip |
| `Duration` | Seconds |
| `Shot Date` | When it was recorded |
| `Status` | Available / Needs Reshoot / Planned |
| `Used In` | Which reel #s have used this clip |

#### Tab 4: `Performance Tracker`

| Column | Description | Source |
|--------|------------|--------|
| `Reel #` | Linked | — |
| `Date Posted` | — | n8n |
| `Views (24h)` | — | Manual / API |
| `Views (7d)` | — | Manual / API |
| `Likes` | — | Manual / API |
| `Comments` | — | Manual / API |
| `Shares` | — | Manual / API |
| `Saves` | — | Manual / API |
| `DM Keyword Triggers` | How many auto-DMs sent | n8n |
| `Engagement Rate` | Auto-calculated | Formula |
| `Hook Used` | From Calendar | Linked |
| `Structure Used` | From Calendar | Linked |
| `Score` | Outlier score vs avg | Formula |

### n8n Triggers from This Sheet

| Trigger | When | Action |
|---------|------|--------|
| New row with date = tomorrow | Daily check | Send Telegram preview H-12 |
| `Client Approval` changes to "Approved" | On edit | Queue for posting |
| `Client Approval` changes to "Revisi" | On edit | Alert team in Telegram |
| `Posted` = Yes | After posting | Log to Performance Tracker |
| End of week | Sunday 20:00 | Compile weekly report → Telegram |

---

## Deliverable #2: CEO Dashboard Sheet

**What:** Excel — full business overview. Auto-updates from n8n + manual inputs.
**Client checks this weekly** to see the big picture.

### Tabs

#### Tab 1: `Dashboard` (Overview — The One Page)

| Section | Metrics | Source |
|---------|---------|--------|
| **Revenue** | Monthly revenue, MRR, cash collected, outstanding | Manual / n8n invoice tracking |
| **Pipeline** | Total leads, qualified, booked, showed, closed, close rate | CRM / Setter reports |
| **Content** | Reels posted this month, avg views, avg engagement, best performer | Content Calendar Sheet |
| **Growth** | Follower count (IG, TikTok), follower growth %, new followers/week | Manual / API |
| **Ads** | Ad spend, CPL (cost per lead), ROAS, active campaigns | Meta Ads / manual |
| **Setter** | DMs sent, convos opened, calls booked, show rate | Setter EOD reports |
| **Automation** | Keyword triggers this month, auto-DMs sent, Telegram approvals | n8n logs |

#### Tab 2: `Monthly Trends`

| Column | Description |
|--------|------------|
| `Month` | Jan, Feb, Mar... |
| `Revenue` | Total |
| `New Clients` | Count |
| `Leads Generated` | Count |
| `Close Rate` | % |
| `Reels Posted` | Count |
| `Avg Views` | Number |
| `Avg Engagement` | % |
| `Follower Growth` | Net new |
| `Ad Spend` | Rp |
| `ROAS` | Ratio |

Charts auto-generated from this data (Excel native charts).

#### Tab 3: `Setter Report`

| Column | Description | Filled By |
|--------|------------|-----------|
| `Date` | — | Auto |
| `Inbox Checked` | Count | Setter (via n8n form) |
| `New Convos` | Count | Setter |
| `Follow-ups Sent` | Count | Setter |
| `Calls Proposed` | Count | Setter |
| `Calls Booked` | Count | Setter |
| `Qualified` | Count | Setter |
| `Calls Showed` | Count | Setter |
| `Closed` | Count | Setter |
| `Common Objections` | Text | Setter |
| `Notes` | Text | Setter |

#### Tab 4: `Lead Pipeline`

| Column | Description |
|--------|------------|
| `Lead Name` | — |
| `Source` | IG DM / TikTok / Ads / Referral |
| `Stage` | Discovery → Engaged → Conversation → Problem Aware → Solution Aware → Interested → Booked → Showed → Closed |
| `Pain Point` | What they said |
| `Last Contact` | Date |
| `Next Action` | What setter does next |
| `Notes` | — |

### n8n Auto-Updates

| Data Point | How It Updates |
|-----------|---------------|
| Setter daily metrics | Telegram bot collects EOD → writes to Sheet |
| Content performance | Weekly scrape or manual entry |
| Keyword CTA triggers | n8n logs each trigger → writes to Sheet |
| Revenue | Manual entry after payment confirmed |

---

## Deliverable #3: Swipe File Library Sheet

**What:** Excel — all analyzed viral structures in one browsable database.
**Client uses this** to pick structures for their own scripts (using Prompt Library).

| Column | Description |
|--------|------------|
| `#` | Structure number |
| `Name` | e.g., "Steal Competitors Hook" |
| `Structure Type` | Value-CTA / Authenticity / Breakdown / Controversy / Tutorial |
| `Hook Type` | Result-Provocative / Authority-Personal / Pain-Callout / etc. |
| `Niche` | Fitness / Business / General |
| `Hook Example` | The actual hook line |
| `Structure Breakdown` | Segment-by-segment (Hook → Interest → Value 1-3 → CTA) |
| `Timing` | e.g., "0:00-0:03 Hook, 0:03-0:05 Interest, ..." |
| `Reference Link` | Original reel URL |
| `Performance` | Views / engagement of original |
| `Times Used` | How many times we've used this structure |
| `Best Result` | Best performing reel using this structure |
| `JSON Link` | Link to full Gemini analysis JSON |

**Grows monthly** — team adds 5-10 new structures per month from viral research.

---

## Deliverable #4: Hook & CTA Bank Sheet

**What:** Excel — proven hooks and CTAs, categorized and scored.

### Tab 1: `Hook Bank`

| Column | Description |
|--------|------------|
| `Hook` | The actual hook text |
| `Category` | Result+Provocative / Authority / Controversial / Pain / Curiosity |
| `Formula` | The template it follows |
| `Language` | Indo / English / Both |
| `Times Used` | Count |
| `Avg Performance` | Avg views when used |
| `Best Reel` | Link to best-performing reel using this hook |

### Tab 2: `CTA Bank`

| Column | Description |
|--------|------------|
| `CTA Text` | e.g., "Comment FREE buat dapetin checklist" |
| `Type` | DM Keyword / Save+Follow / Link in Bio / WhatsApp / Calendar |
| `Keyword` | The trigger word (ALL CAPS) |
| `Auto-DM Message` | What gets sent |
| `Conversion Rate` | % of comments that DM |
| `Times Used` | Count |

---

## Deliverable #5: Prompt Library Doc

**What:** Google Doc — tested Claude prompts client can use to self-serve between monthly batches.
**This is what makes it premium** — client can generate their own scripts anytime.

### Prompts Included

| # | Prompt Name | What It Does | Output |
|---|------------|-------------|--------|
| 1 | **Reel Script Writer** | "Write a reel script for [topic] using swipe structure #[X] for [client name]" | Full script with hook, segments, CTA, filenames |
| 2 | **Hook Generator** | "Generate 10 hook variations for [topic] targeting [avatar]" | 10 hooks categorized by type |
| 3 | **Caption Writer** | "Write IG caption for a reel about [topic] with CTA keyword [KEYWORD]" | Ready-to-post caption |
| 4 | **Threads Repurposer** | "Repurpose this reel script into a Threads post: [script]" | Threads-ready text |
| 5 | **Story Sequence Writer** | "Create 3-5 story slides from this reel brief: [brief]" | Slide-by-slide story scripts |
| 6 | **Newsletter Repurposer** | "Turn this reel script into a newsletter email: [script]" | Email-ready content |
| 7 | **YouTube Outline** | "Expand this reel into a 10-min YouTube script outline: [script]" | YouTube script with sections |
| 8 | **TikTok Caption** | "Rewrite this IG caption for TikTok audience: [caption]" | TikTok-native caption |
| 9 | **Objection Destroyer** | "Write a reel script that addresses this objection: [objection]" | Reel targeting specific objection |
| 10 | **Content Idea Generator** | "Generate 20 reel ideas for [niche] targeting [avatar] based on these pain points: [list]" | 20 ideas with hook + structure suggestion |
| 11 | **DM Script Writer** | "Write a DM script for [scenario: cold/warm/follow-up] targeting [avatar]" | Conversation script |
| 12 | **Offer Pitch Refiner** | "Rewrite this offer pitch to be more compelling: [current pitch]" | Refined pitch |

### Each Prompt Includes:
- The exact prompt text (copy-paste ready)
- What to fill in (marked with `[brackets]`)
- Example input
- Example output
- Tips for best results

---

## Deliverable #6: 14 DFY Reels/Month

**What:** 14 fully produced reels — scripted, edited, captioned, scheduled.

### Production Pipeline Per Reel

```
Step 1: SCRIPT (Claude)
  Input:  Swipe structure + client brief + footage inventory
  Output: Brief with exact filenames per segment
  Time:   ~5 min per script
    │
Step 2: REMOTION BASELINE
  Input:  Brief filenames + a-roll clips + assets
  Process:
    → Auto-assemble segments per timing
    → Generate captions (Whisper → styled SRT)
    → Remove silences from talking head clips
    → Add intro animation (template)
    → Add CTA overlay (from CTA bank)
    → Add text overlays per segment
  Output: Baseline MP4
  Time:   ~5 min render
    │
Step 3: CAPCUT POLISH
  Input:  Remotion baseline MP4
  Process:
    → Music selection + timing
    → Transitions between segments
    → Color grading (LUT from client profile)
    → Caption style refinement
    → Pacing adjustments
    → Creative touches (zooms, effects)
  Output: Final MP4
  Time:   ~20-30 min per reel
    │
Step 4: UPLOAD + NOTIFY
  Input:  Final MP4
  Process:
    → Upload to GDrive (preview link)
    → Update Content Calendar Sheet
    → n8n triggers Telegram notification H-12
  Output: Client sees preview in Telegram
    │
Step 5: APPROVAL
  Client taps: ✅ Approve / 🔄 Revisi / 💬 Masukan
    │
Step 6: SCHEDULE + POST
  n8n queues to IG + TikTok at scheduled time
  Auto-posts caption + hashtags
  Keyword CTA ready
```

### What Client Receives Per Reel

| Asset | Format | Where |
|-------|--------|-------|
| Reel video (IG) | MP4, 9:16, 15-60s | GDrive + posted to IG |
| Reel video (TikTok) | MP4, 9:16, no watermark | GDrive + posted to TikTok |
| IG Caption | Text | Content Calendar Sheet |
| TikTok Caption | Text | Content Calendar Sheet |
| Threads Post | Text | Repurposed Content tab |
| Story Slides (3-5) | Text scripts | Repurposed Content tab |
| Newsletter Snippet | Text | Repurposed Content tab |
| YouTube Outline | Text | Repurposed Content tab |

**14 reels × 7 repurposed pieces = 98+ content pieces/month**

---

## Deliverable #7: Telegram Approval Bot

**What:** n8n-powered Telegram bot — client's daily interface with the system.

### Messages Client Receives

| Message Type | Trigger | Frequency |
|-------------|---------|-----------|
| Content preview (H-12) | Scheduled time - 12 hours | Daily (when content scheduled) |
| Draft review request | New script ready | 3-4x/week |
| Weekly performance report | Every Monday 08:00 | Weekly |
| Lead alert | New qualified lead | As it happens |
| Shoot reminder | 48h before filming | As scheduled |
| Monthly report | 1st of month | Monthly |
| Mastermind reminder | 24h before call | Weekly |
| Consultation reminder | 24h before call | Monthly |

### Bot Commands (Client Can Send)

| Command | Action |
|---------|--------|
| `/status` | Shows this week's content status |
| `/next` | Shows next scheduled reel details |
| `/approve [reel#]` | Approves a specific reel |
| `/revisi [reel#] [notes]` | Sends revision request with feedback |
| `/report` | Pulls latest performance summary |
| `/help` | Lists available commands |

---

## Deliverable #8: Keyword CTA Automation

**What:** Meta Business Suite automation — auto-DM when someone comments a keyword.

### Per Client Setup

| Keyword | Reel Type | Auto-DM Content | CTA Link |
|---------|-----------|-----------------|----------|
| `FREE` | Value-CTA | "Hey! Ini dia [freebie]..." | Freebie link |
| `INFO` | Value-CTA | "Thanks! Ini detail program..." | VSL link |
| `COACH` | Authenticity | "Mau ngobrol? Book free session..." | Calendar link |
| `[CUSTOM]` | Per reel | Per reel | Per reel |

**n8n tracks:** Every trigger logged → CEO Dashboard updated.

---

## Deliverable #9: VSL Funnel

**What:** One-page landing site — Netlify hosted, Wistia video.

### Components

| Element | Detail |
|---------|--------|
| Hero section | VSL video (Wistia) + headline |
| CTA button | WhatsApp / Calendar booking |
| Social proof | Testimonial cards |
| Offer breakdown | Deliverables list |
| FAQ | Accordion |
| Mobile optimized | Yes |
| Domain | Custom subdomain or client's domain |
| Analytics | Wistia play rate + Google Analytics |

---

## Deliverable #10: Setter Scripts (Customized)

**What:** Google Doc — all 8 scripts tailored to client's brand, offer, and avatar.

### Scripts Included

| # | Script | Customized With |
|---|--------|----------------|
| 1 | Inbound | Client's offer name, CTA links, brand voice |
| 2 | Outbound | Client's niche, ICP criteria, competitor handles |
| 3 | Post-Booking | Client's calendar link, offer details |
| 4 | Freebie | Client's lead magnet name + link |
| 5 | Inbound Ads | Client's ad topics, offer summary |
| 6 | Show-Up | Client's name, call details |
| 7 | Follow-Up | Client's case studies, content links |
| 8 | Upsell | Client's add-on services, referral reward |

Source template: `Fulfillment/_ONBOARDING/setter_scripts_master.md`

---

## Deliverable #11: ElevenLabs Voice Clone

**What:** AI voice clone of client — for non-talking-head voiceovers.

| Detail | Spec |
|--------|------|
| Input | 5-10 min clean voice recording |
| Output | ElevenLabs voice profile |
| Used for | Voiceover on b-roll segments, story narration |
| Quality | Instant Voice Cloning (or Professional if budget allows) |
| Client access | No (backend tool) |

---

## Deliverable #12: Offer Sheet

**What:** Professional offer document — client uses on sales calls and in DMs.

### Contains
- Power statement
- Avatar description
- Signature system (3 pillars)
- Deliverables + value stack
- Bonuses
- Guarantee
- Pricing
- Objection handling quick reference

### Format
- Google Doc (editable)
- PDF export (shareable)
- Generated by `tools/offer_agent.py`

---

## Deliverable #13: AI Solopreneur Module

**What:** Private video course — teaches solopreneurs to sell on social media with AI.
**Format:** Video modules (GDrive/course platform) + supporting docs.

### Curriculum

#### Module 1: Foundation — Selling on Social Media in 2026
- Why social media is the #1 sales channel for solopreneurs
- The content-to-cash pipeline: views → trust → DMs → calls → revenue
- Your daily workflow: 2 hours/day content + engagement system
- Metrics that matter (vanity vs revenue metrics)
- **Homework:** Define your ICP + power statement

#### Module 2: Offer Architecture
- Why "what you sell" matters more than "how you sell"
- The high-ticket offer formula (niche + result + timeframe)
- Signature system: how to name your method
- Value stacking: deliverables, bonuses, guarantees
- Pricing psychology for Indonesian market
- **Homework:** Complete Offer Sheet template

#### Module 3: Content Strategy — The AI-Powered Approach
- The 3 content types: Value-CTA, Authenticity, Breakdown
- Hook psychology: why first 3 seconds decide everything
- Using swipe file structures (how to find + analyze winning reels)
- Content calendar planning (14 reels/month structure)
- The repurposing multiplier: 1 reel → 7 pieces
- **Homework:** Pick 5 swipe structures, write 5 hooks

#### Module 4: AI Scriptwriting with Prompts
- Introduction to AI prompting (Claude / ChatGPT)
- How to use the Prompt Library effectively
- Writing reel scripts with AI: input → output → refine
- Generating hooks, captions, Threads posts, stories
- Quality control: how to spot and fix AI-sounding content
- Adding your voice: the 80/20 rule (AI writes 80%, you add 20% personality)
- **Homework:** Generate 3 reel scripts using Prompt Library

#### Module 5: Video Production Basics
- Filming setup: phone, ring light, mic (budget friendly)
- A-roll recording: how to talk to camera naturally
- B-roll ideas for every niche
- CapCut basics: cuts, transitions, music, captions
- Remotion overview: what automated editing looks like
- How your reels get produced (the Remotion → CapCut pipeline)
- **Homework:** Record 3 A-roll clips

#### Module 6: Instagram Growth Engine
- Profile optimization (bio, highlights, link)
- Keyword CTA system: how it works, why it converts
- Hashtag strategy 2026
- Stories strategy: the 3-5 slide sequence
- Reels algorithm: what IG rewards
- The DM funnel: content → keyword → auto-DM → conversation → call
- **Homework:** Optimize profile, setup first keyword CTA

#### Module 7: DM Sales — The Conversation Framework
- Why DM selling beats cold calling
- The 9-stage journey: Discovery → Closed
- Reading buying signals
- Objection handling in DMs (when to text, when to call)
- Setter workflow: how to hire and train a setter
- **Homework:** Open 5 genuine DM conversations

#### Module 8: Automation & Systems
- What n8n is and why it matters
- Your automation stack: Telegram bot, auto-scheduling, keyword CTA
- Reading your CEO Dashboard
- Using the Content Calendar Sheet
- The weekly rhythm: what to check, when
- **Homework:** Review your dashboard, identify 1 bottleneck

#### Module 9: Scaling — From 1 Client to 20
- When to hire (setter, editor, VA)
- KPI tracking for your team
- The feedback loop: objections → content → fewer objections
- Pricing increases: when and how
- Adding revenue streams: group coaching, courses, mastermind
- **Homework:** Create your 90-day scaling plan

#### Module 10: Advanced — AI Deep Dive
- Advanced prompting techniques
- Using AI for offer refinement
- AI-assisted sales call prep
- Trend detection with AI
- Building your own prompt library
- What's coming: AI video editing, AI outreach, AI analytics
- **Homework:** Build 3 custom prompts for your niche

### Mastermind Calls — Weekly Material

| Week | Topic | Format |
|------|-------|--------|
| 1 | Hot Seats (3 members share challenges) | Live coaching + group brainstorm |
| 2 | Module Deep-Dive (expand on one module) | Teaching + Q&A |
| 3 | Guest Expert / Case Study | Interview or presentation + Q&A |
| 4 | Open Q&A + Wins | Ask anything + celebrate wins |

**Rotating monthly — so every 4 weeks clients get all formats.**

### Mastermind Extras
- Recordings available in GDrive (private folder)
- Summary notes posted in community after each call
- Action items tracked per member
- Accountability partners assigned (pairs rotate monthly)

---

## Deliverable #14: Chrome Sales HQ

**What:** Chrome bookmark folder — client's entire business in one browser window.

### Bookmarks

| Folder | Links |
|--------|-------|
| **Analytics** | IG Insights, TikTok Analytics, YouTube Studio, Wistia Stats |
| **Sales** | CEO Dashboard Sheet, Content Calendar Sheet, Calendar Booking, VSL Funnel |
| **Content** | GDrive Content Folder, Swipe File Sheet, Hook Bank Sheet, Prompt Library |
| **Communication** | WhatsApp Web, Telegram Bot, Community Group |
| **Ads** | Meta Ads Manager, Ad Creatives Folder |
| **Learning** | AI Module (course), Mastermind Recordings |

---

## Deliverable #15: Monthly 1-on-1 Consultation

| Detail | Spec |
|--------|------|
| Frequency | Monthly |
| Duration | 60 minutes |
| Platform | Google Meet |
| Recording | Fathom (auto-transcript) |
| Agenda shared | 24h before via Telegram |

### Standard Agenda
1. Review last month's CEO Dashboard numbers (10 min)
2. Content performance: what worked, what didn't (10 min)
3. Pipeline review: leads, close rate, bottlenecks (10 min)
4. Strategy for next month: content direction, offer tweaks (15 min)
5. Open Q&A (15 min)

### Deliverables From Call
- Updated content direction for next month
- Any offer/pricing adjustments documented
- Action items sent via Telegram within 24h

---

## Deliverable #16: Private Community

| Detail | Spec |
|--------|------|
| Platform | Telegram Group (or Discord) |
| Members | All active retainer clients |
| Moderated by | Jordan + VA |

### Channels (if Telegram Supergroup or Discord)

| Channel | Purpose |
|---------|---------|
| `#announcements` | Updates, new features, schedule changes |
| `#wins` | Client wins (screenshots, milestones) |
| `#questions` | Ask anything, peer support |
| `#content-ideas` | Share content inspo, swipe files |
| `#resources` | New modules, templates, tools |
| `#mastermind-notes` | Post-call summaries + recordings |

---

## Complete Delivery Timeline

### Setup Phase (One-Time, Days 0-14)

| Day | Deliverables Created |
|-----|---------------------|
| 0 | Content Calendar Sheet, CEO Dashboard Sheet (empty structure) |
| 0 | Client folders (Cook + GDrive) |
| 0 | Community access, module access |
| 1-3 | Offer Sheet (from onboarding data) |
| 1-3 | Swipe File Library Sheet (seeded with 10 structures for their niche) |
| 1-3 | Hook & CTA Bank Sheet (seeded from master library) |
| 1-3 | ElevenLabs voice clone |
| 3-5 | VSL Funnel (deployed) |
| 3-5 | Filming session (A-roll + VSL) |
| 5-7 | Prompt Library Doc (customized to their niche/avatar) |
| 8-10 | Keyword CTA Automation (live) |
| 8-10 | Telegram Approval Bot (connected) |
| 10-12 | Setter Scripts (customized) |
| 10-12 | Chrome Sales HQ (setup) |
| 13-14 | Everything tested end-to-end |
| 14 | First consultation + system walkthrough |

### Monthly Recurring

| Deliverable | Cadence |
|------------|---------|
| 14 DFY reels | Monthly (rolling, ~3-4/week) |
| 70+ repurposed pieces | Monthly (auto from reels) |
| Swipe library additions | 5-10 new structures/month |
| CEO Dashboard updates | Auto (daily/weekly) |
| Telegram notifications | Auto (daily) |
| Weekly mastermind | Every week |
| Monthly consultation | Every month |
| System maintenance | Ongoing (n8n, sheets, automations) |

---

## What Client Pays For (Summary)

```
ONE MONTHLY RETAINER = Everything above.

Setup fee (one-time):
├── Notion-free system deployment (Sheets + Telegram + n8n)
├── VSL funnel build + filming session
├── Voice clone + offer sheet + setter scripts
├── Content system seeded (swipe file, hooks, CTAs, prompts)
└── Full 14-day onboarding sprint

Monthly retainer:
├── 14 DFY reels (script → edit → post)
├── 70+ repurposed content pieces
├── AI token usage (Claude scripting + repurposing)
├── n8n infrastructure (10+ automations running)
├── Telegram approval bot
├── System maintenance + improvements
├── CEO Dashboard auto-updates
├── Swipe library growth
├── Monthly 1-on-1 consultation (60 min)
├── Weekly mastermind access
├── AI Solopreneur Module access
├── Private community access
└── Unlimited async Telegram support

Add-ons (extra revenue):
├── Extra reels beyond 14 → Creative Director + Editor fee
├── Ads management → % of spend or flat
├── Setter placement → monthly fee
├── Funnel updates → per project
└── Event/launch support → per event
```

---

## Files To Build

| # | Deliverable | Format | Where It Lives | Status |
|---|------------|--------|---------------|--------|
| 1 | Content Calendar Sheet | Excel | Client's GDrive | Template needed |
| 2 | CEO Dashboard Sheet | Excel | Client's GDrive | Template needed |
| 3 | Swipe File Library Sheet | Excel | Client's GDrive | Template needed |
| 4 | Hook & CTA Bank Sheet | Excel | Client's GDrive | Template needed |
| 5 | Prompt Library Doc | Google Docs | Client's GDrive | Template needed |
| 6 | Remotion templates | Code | Cook/remotion/ | Exists (ValueCTAReel, AuthenticityReel) |
| 7 | n8n workflows | JSON | n8n instance | Need to build per-client |
| 8 | Telegram bot config | n8n | n8n instance | Need to build |
| 9 | VSL funnel template | HTML | Fulfillment/_OFFER_BLUEPRINT/ | Exists (vsl_template_client.html) |
| 10 | Setter scripts | Markdown → Google Docs | Fulfillment/_ONBOARDING/ | Exists (setter_scripts_master.md) |
| 11 | AI Module curriculum | Video scripts | Need to produce | Outlined above |
| 12 | Chrome Sales HQ | Bookmark export | Per client | Template needed |
| 13 | Offer sheet generator | Python | tools/offer_agent.py | Exists |
