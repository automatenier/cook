---
tags:
  - consulting
---
# Internal Infrastructure Map — JO Consult Team

> How the TEAM operates. Every role, their tools, their data flows, and how the Founder monitors everything from Obsidian.

---

## Team Roles

```
┌─────────────────────────────────────────────────────────────────────┐
│                    FOUNDER (Jordan)                                 │
│                                                                     │
│  Obsidian Vault = Command Center                                   │
│  Monitors: Agent (Claude), n8n, all team outputs                   │
│  Decisions: Strategy, offers, creative direction, scaling           │
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────┐   │
│  │  Closer  │  │ Creative │  │  Setter  │  │       VA         │   │
│  │          │  │ Director │  │          │  │                  │   │
│  │ Sales    │  │ Content  │  │ DM Lead  │  │ Operations       │   │
│  │ calls    │  │ quality  │  │ qualify  │  │ coordination     │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Role #1: Founder (Jordan)

### Primary Tools

| Tool                | Purpose                                                     | How Used                               |
| ------------------- | ----------------------------------------------------------- | -------------------------------------- |
| **Obsidian**        | Command center, strategy, brainstorming, content flow state | Daily — creative work + monitoring     |
| **VS Code (Cook/)** | Agent orchestration, system building                        | Daily — Claude commands + tool runs    |
| **n8n Dashboard**   | Monitor all automations                                     | Daily — check for errors, review flows |
| **Excel**           | CEO dashboards across clients                               | Weekly — review numbers                |
| **Google Meet**     | Consultations, mastermind calls                             | Weekly/monthly                         |
| **Telegram**        | Team comms, client bots, alerts                             | Always-on                              |
| **CapCut**          | Creative video editing                                      | When in content flow state             |
| **Fathom**          | Call recordings + transcripts                               | After every sales/consultation call    |

### Obsidian Vault — Founder's Command Center

```
SecondBrainObsidian/
│
├── Operations/                          ← MONITORING HUB
│   ├── 📊 Dashboard.md                 ← Daily overview (linked to everything)
│   │   ├── Active Clients (count + status)
│   │   ├── Pipeline Summary (leads → closed)
│   │   ├── Revenue This Month
│   │   ├── Content Production Status
│   │   ├── Team KPIs (setter, VA, editor)
│   │   └── n8n Health (errors, uptime)
│   │
│   ├── 📋 Project Tracker.md            ← Per-client status
│   │   ├── [Client A] — Day 8/14, content sprint
│   │   ├── [Client B] — Month 3, steady state
│   │   └── [Client C] — Day 2/14, onboarding
│   │
│   ├── 👥 Team/
│   │   ├── Closer_KPIs.md              ← Close rate, revenue, call quality
│   │   ├── Creative_Director_KPIs.md   ← Content quality, turnaround
│   │   ├── Setter_KPIs.md              ← DMs, bookings, show rate
│   │   ├── VA_KPIs.md                  ← Onboarding speed, response time
│   │   └── Hiring_Pipeline.md          ← Open roles, candidates
│   │
│   ├── 🤖 Agent/
│   │   ├── Claude_Tasks.md             ← Current + queued agent tasks
│   │   ├── Prompt_Performance.md       ← Which prompts work best
│   │   └── Tool_Changelog.md          ← Updates to tools/scripts
│   │
│   ├── ⚡ Automations/
│   │   ├── n8n_Status.md              ← Active workflows, error log
│   │   ├── n8n_Per_Client.md          ← Which automations per client
│   │   └── Automation_Ideas.md        ← Backlog of automation to build
│   │
│   └── 💰 Revenue/
│       ├── Monthly_Revenue.md          ← MRR, cash collected, churn
│       ├── Client_LTV.md              ← Lifetime value per client
│       └── Pricing_History.md         ← Price changes + reasoning
│
├── Brainstorms/                         ← STRATEGY SPACE
│   ├── Offer_Evolution.md
│   ├── New_Verticals.md
│   └── Content_Ideas.md
│
├── A Master Prompts/                    ← PROMPT TEMPLATES
│   ├── Brand_Sheet_Prompt.md
│   ├── Offer_Agent_Prompt.md
│   ├── Content_Audit_Prompt.md
│   └── Repurpose_Prompt.md
│
└── A Result/                            ← GENERATED OUTPUTS
    ├── [Client]_Offer_Sheet.md
    ├── [Client]_Content_Audit.md
    └── [Client]_Scripts_Batch_1.md
```

### Obsidian Graph View — How Everything Connects

The graph view shows relationships between:
- **Clients** ↔ their deliverables, KPIs, team members
- **Team members** ↔ their KPIs, SOPs, clients they serve
- **Automations** ↔ which clients they serve, error status
- **Prompts** ↔ which tools they power, output quality
- **Revenue** ↔ clients, pricing, churn

**Key links to maintain:**
```markdown
<!-- In Dashboard.md -->
## Active Clients
- [[Client_BusyFit]] — Day 12/14
- [[Client_MissMochi]] — Month 2

## Team
- [[Closer_KPIs]] — Close rate: 45%
- [[Setter_KPIs]] — 8 bookings this week
- [[VA_KPIs]] — All onboardings on time

## Systems
- [[n8n_Status]] — 0 errors today
- [[Claude_Tasks]] — 3 scripts queued
```

```markdown
<!-- In Client_BusyFit.md -->
## Status: Day 12/14 — Lead Activation
## Team: [[Setter_KPIs|Setter]] assigned, [[VA_KPIs|VA]] coordinating

### Deliverables
- [x] Offer Sheet — [[BusyFit_Offer_Sheet]]
- [x] VSL Funnel — live
- [x] Content Calendar — 14 slots filled
- [ ] Keyword CTA — testing
- [ ] Setter scripts — customizing

### Automations Active
- [[n8n_Per_Client|Telegram Bot]] — connected
- [[n8n_Per_Client|Content Scheduler]] — ready
- [[n8n_Per_Client|Keyword CTA]] — pending test

### Revenue
- Setup fee: Rp X — PAID
- Monthly retainer: Rp X — starts Day 15
```

### Founder's Daily Routine

| Time | Action | Tool |
|------|--------|------|
| 08:00 | Check Obsidian Dashboard — overview | Obsidian |
| 08:15 | Check n8n — any errors overnight? | n8n dashboard |
| 08:30 | Check Telegram — team EOD reports from yesterday | Telegram |
| 09:00 | VS Code — run Claude tasks (scripts, repurposing, offers) | VS Code |
| 10:00 | Content flow state — CapCut editing or creative direction | Obsidian + CapCut |
| 12:00 | Review setter inbox analysis (if scheduled) | Google Meet |
| 14:00 | Client consultation or mastermind (if scheduled) | Google Meet |
| 15:00 | Strategy work — offer refinement, new ideas | Obsidian Brainstorms |
| 17:00 | Review team outputs, approve deliverables | Excel + Telegram |
| 18:00 | Update Obsidian — project tracker, KPIs, notes | Obsidian |

---

## Role #2: Closer (Sales)

### Responsibility
Close qualified leads on sales calls. Convert booked calls into paid clients.

### Tools

| Tool | Purpose |
|------|---------|
| **Google Meet / Zoom** | Sales calls |
| **Fathom** | Auto-record + transcript every call |
| **Google Calendar** | Booking slots |
| **Excel (CEO Dashboard)** | Log call outcomes |
| **Telegram** | Receive lead briefs from setter, report to founder |
| **Offer Sheet (PDF)** | Screen-share during pitch |

### Data Flow

```
Setter qualifies lead → books call
    │
    ├── Telegram: "New booking: [Name], pain: [X], ICP score: [X]"
    │             Attached: DM log summary, IG profile link
    │
    ▼
Closer receives brief
    │
    ├── Pre-call: Review DM logs, IG profile, onboarding form (if filled)
    │
    ▼
Sales call (20-60 min)
    │
    ├── Fathom records + transcribes
    │
    ▼
Outcome logged
    │
    ├── Excel: Pipeline tab → stage updated
    ├── Telegram: Report to founder + setter
    │   "Closed: [Name] — Paket [X] — Rp [amount]"
    │   OR "No close: [Name] — Objection: [X] — Follow up [date]"
    │
    ▼
If closed → Trigger onboarding (VA takes over)
If not → Follow-up scheduled (Closer or Setter handles)
```

### Closer KPIs

| Metric | Target | Tracked In |
|--------|--------|-----------|
| Calls taken / week | 5-10 | Excel |
| Close rate (pre-sold leads) | 40-50% | Excel |
| Close rate (cold leads) | 20-30% | Excel |
| Average deal size | Rp [target] | Excel |
| Cash collected / month | Rp [target] | Excel |
| No-show follow-up rate | 100% | Manual |
| Call recording reviewed | 100% | Fathom |

### Closer's Daily Workflow

| Priority | Task |
|----------|------|
| 1 | Check today's calendar — prep for each call (review DM logs, profile) |
| 2 | Conduct calls — use sales script framework |
| 3 | Log outcomes immediately after each call |
| 4 | Report to founder via Telegram |
| 5 | Follow up no-shows (within 2 hours) |
| 6 | Review Fathom transcripts — identify objection patterns |
| 7 | Feed objection patterns to Creative Director (content team makes reels to address them) |

### SOPs

| Document | Location |
|----------|----------|
| Sales Call Script | `Fulfillment/_OFFER_BLUEPRINT/sales_call_script_indo.md` |
| Objection Bank | Inside sales script + `setter_scripts_master.md` |
| Close Report | `Fulfillment/_OFFER_BLUEPRINT/setter_close_report.md` |
| Pre-Call Checklist | Review DM logs, IG profile, pain points, ICP score |

---

## Role #3: Creative Director

### Responsibility
Ensure all content meets quality bar. Bridge between AI-generated scripts and final output. Direct filming sessions. Manage Editor.

### Tools

| Tool | Purpose |
|------|---------|
| **Excel (Content Calendar)** | Review scripts, approve/reject |
| **CapCut** | Quality check final edits, creative direction |
| **VS Code (optional)** | Review Remotion outputs |
| **Telegram** | Receive objection feedback from setter, coordinate with team |
| **Google Meet** | Creative Director calls with clients (filming prep, direction) |
| **GDrive** | Review raw footage, assets |

### Data Flow

```
Claude generates 14 scripts/month
    │
    ▼
Creative Director reviews
    │
    ├── Script quality check (hook strong? CTA clear? brand voice?)
    ├── Footage assignment (which a-roll, which b-roll per segment)
    ├── Asset requests (need new nano image? new overlay?)
    │
    ▼
Remotion generates baseline
    │
    ▼
Creative Director reviews baseline
    │
    ├── Pacing right? Captions styled? CTA overlay positioned?
    │
    ▼
Editor receives baseline + creative notes
    │
    ▼
CapCut polish (Editor does this)
    │
    ▼
Creative Director final approval
    │
    ├── Approved → Content Calendar Sheet updated → Telegram bot notifies client
    ├── Rejected → Back to Editor with notes
    │
    ▼
Setter feedback loop
    │
    ├── Setter reports: "leads keep asking about [X]"
    ├── Creative Director: "Let's make a reel addressing [X]"
    └── Adds to next month's content calendar
```

### Creative Director KPIs

| Metric | Target | Tracked In |
|--------|--------|-----------|
| Scripts reviewed / week | 3-4 | Content Calendar Sheet |
| Reels approved / week | 3-4 | Content Calendar Sheet |
| Avg turnaround (script → final) | 3 days | Content Calendar Sheet |
| Content quality score (self-assessed) | 8+/10 | Manual |
| Client revision requests | < 2 per batch | Content Calendar Sheet |
| Objections addressed (from setter feedback) | 2+ reels/month | Manual |

### Creative Director's Weekly Routine

| Day | Task |
|-----|------|
| **Mon** | Review this week's scripts from Claude → approve/edit → assign to Editor |
| **Tue** | Check Remotion baselines → send creative notes to Editor |
| **Wed** | Review CapCut finals → approve or send back |
| **Thu** | Filming session coordination (if scheduled) |
| **Fri** | Review setter feedback → plan objection-addressing content for next week |
| **Ongoing** | Monitor client revision requests → improve prompts/templates accordingly |

### SOPs

| Document | Location |
|----------|----------|
| Content Creation Workflow | `workflows/content_creation.md` |
| Script Templates | `content/library/script_templates/` |
| Viral Checklist | `content/strategy/viral_checklist.md` |
| Swipe File Index | `content/swipe_file/_index.md` |
| Filming Checklist | `content/clients/[name]/footage_checklist.md` |

---

## Role #4: Setter (DM Sales)

### Responsibility
Find ICPs, build genuine DM relationships, qualify leads, book calls for Closer.

### Tools

| Tool | Purpose |
|------|---------|
| **Instagram** | DM outreach, engagement, lead discovery |
| **TikTok** | DM monitoring, keyword comment responses |
| **Excel (CEO Dashboard)** | Log daily KPIs, update lead pipeline |
| **Telegram** | EOD reports, lead briefs to Closer, team comms |
| **Google Calendar** | Book qualified leads for calls |
| **WhatsApp** | Voice notes, reminders to prospects |

### Data Flow

```
Setter finds ICPs (4+/day)
    │
    ├── Log in Excel: Lead Pipeline tab
    │
    ▼
Engage (2-3 days: likes, comments, story replies)
    │
    ▼
Open DM conversation (3-5 days)
    │
    ▼
Surface pain point (3-7 days)
    │
    ▼
Lead discovers offer organically (1-3 days)
    │
    ▼
Lead shows interest
    │
    ├── Setter qualifies using ICP criteria
    │
    ▼
Book call
    │
    ├── Google Calendar link sent
    ├── n8n auto-triggers: WA reminder (24h + 1h)
    ├── Telegram: Brief sent to Closer
    │   "Booking: [Name], IG: @[handle], Pain: [X], ICP Score: [X/5]"
    │   "DM Summary: [key points from conversation]"
    │
    ▼
Post-booking nurture
    │
    ├── Post-booking script sent immediately
    ├── 24h phone call
    ├── Night-before voice note
    ├── 1h reminder
    │
    ▼
Show / No-show
    │
    ├── Show → Closer handles
    ├── No-show → Setter follows up (Follow-Up script)
    │
    ▼
EOD Report (21:00)
    │
    ├── Telegram bot collects: DMs sent, convos, bookings, objections
    ├── Auto-writes to Excel Setter Report tab
    └── Common objections → Creative Director (feedback loop)
```

### Setter KPIs

| Metric | Daily Target | Weekly Target | Tracked In |
|--------|-------------|--------------|-----------|
| Inbox checked | 100 msgs | 500 | Excel |
| New conversations | 2+ | 8+ | Excel |
| Follow-ups sent | 40+ | 200+ | Excel |
| YT/Long-form sent | 7+ | 35+ | Excel |
| Calls proposed | 4+ | 20+ | Excel |
| Calls booked | 1+ | 10+ | Excel |
| Qualified bookings | 1+ | 8+ | Excel |
| Show rate | — | 80%+ | Excel |
| ICP leads found | 2+ | 10+ | Excel |

### SOPs

| Document | Location |
|----------|----------|
| All 8 Scripts | `Fulfillment/_ONBOARDING/setter_scripts_master.md` |
| DM Outreach Workflow | `workflows/setter_dm_outreach.md` |
| Team Roadmap | `Fulfillment/_ONBOARDING/team_roadmap_setter.md` |
| Close Report | `Fulfillment/_OFFER_BLUEPRINT/setter_close_report.md` |
| ICP Criteria | Inside setter scripts + team roadmap |

---

## Role #5: VA (Virtual Assistant)

### Responsibility
Operational backbone. File organization, client coordination, onboarding execution, team coordination, system maintenance.

### Tools

| Tool | Purpose |
|------|---------|
| **Google Drive** | File organization, client folders |
| **Excel** | All dashboards — maintain + update |
| **Google Calendar** | Schedule management |
| **Telegram** | Team coordination, client follow-ups |
| **WhatsApp Business** | Client communication |
| **Meta Business Suite** | Keyword CTA setup, ads coordination |
| **Instagram / TikTok** | Content posting (if not automated) |
| **Wistia** | Upload VSL videos |
| **n8n** | Monitor automations (flag errors to Founder) |

### Data Flow

```
New client signs
    │
    ▼
VA creates everything (Day 0)
    ├── GDrive folder structure
    ├── Cook folders (content/clients/ + Fulfillment/)
    ├── Excel (Content Calendar + CEO Dashboard — from templates)
    ├── Welcome email sent
    ├── Community + module access granted
    ├── Telegram progress channel created
    ├── CRM updated
    │
    ▼
VA manages onboarding (Day 1-14)
    ├── Follow up on forms + materials
    ├── Organize uploaded files
    ├── Coordinate filming session
    ├── Deploy automations (with Founder)
    ├── Setup keyword CTA
    ├── Prep all Day 14 deliverables
    │
    ▼
VA runs daily ops (Post Day 14)
    ├── Morning: Check Telegram, update CRM, coordinate team
    ├── Midday: Check content schedule, organize files
    ├── Afternoon: Prep tomorrow, brief team, EOD summary
    │
    ▼
VA reports to Founder
    ├── Daily EOD summary via Telegram
    ├── Weekly compiled report
    └── Flags: errors, delays, client issues
```

### VA KPIs

| Metric | Target | Tracked In |
|--------|--------|-----------|
| Onboarding completion | Within 48h of payment | Excel |
| Materials organized | Within 24h of receipt | Manual |
| Content batch to Editor | Monday by 10:00 | Content Calendar |
| CRM updated | Daily by 17:00 | Excel |
| Client response time | Within 4h (business hours) | Manual |
| Errors flagged | Same day | Telegram |

### SOPs

| Document | Location |
|----------|----------|
| VA Setup SOP | `Fulfillment/_ONBOARDING/va_setup_sop.md` |
| Team Roadmap | `Fulfillment/_ONBOARDING/team_roadmap_va.md` |
| New Client Folder Generator | `Fulfillment/_ONBOARDING/new_client_folder_generator.md` |
| Client 14-Day Roadmap | `Fulfillment/_ONBOARDING/client_14day_roadmap.md` |

---

## Cross-Team Data Flows

```
                    ┌─────────────┐
                    │   FOUNDER   │
                    │  (Obsidian) │
                    └──────┬──────┘
                           │
              Monitors all │ via Obsidian graph +
              dashboards   │ Telegram + n8n
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│    SETTER     │  │   CREATIVE    │  │      VA       │
│               │  │   DIRECTOR    │  │               │
│ Finds leads   │  │ Quality gate  │  │ Ops backbone  │
│ Books calls   │  │ Content dir.  │  │ Coordination  │
└───────┬───────┘  └───────┬───────┘  └───────┬───────┘
        │                  │                  │
        │                  │                  │
   ┌────▼────┐        ┌───▼───┐         ┌───▼───┐
   │ CLOSER  │        │EDITOR │         │ n8n   │
   │         │        │       │         │       │
   │ Closes  │        │CapCut │         │ Runs  │
   │ deals   │        │polish │         │ auto  │
   └─────────┘        └───────┘         └───────┘
```

### Key Feedback Loops

| Loop | From → To | What Flows | How |
|------|----------|------------|-----|
| **Objection → Content** | Setter → Creative Director | Common objections from DMs | Telegram weekly summary |
| **Close Analysis → Strategy** | Closer → Founder | What sold, what objected | Close Report + Fathom transcript |
| **Content Performance → Scripts** | Analytics → Creative Director | What hooks/structures performed | Excel Performance Tracker |
| **Client Feedback → Quality** | Client (Telegram) → Creative Director | Revision requests, masukan | Content Calendar Sheet |
| **System Errors → Fix** | n8n → VA → Founder | Automation failures | Telegram alerts |
| **Pipeline → Capacity** | CEO Dashboard → Founder | Too many/few leads? | Weekly review |

---

## Shared Excel Architecture

### One Master Workbook Per Client (or separate sheets linked)

```
Client [Name] Master Sheet/
├── Tab: Content Calendar          ← Team fills, client reviews
├── Tab: Repurposed Content        ← Auto-populated from scripts
├── Tab: Footage Inventory         ← VA maintains
├── Tab: Performance Tracker       ← n8n + manual
├── Tab: CEO Dashboard             ← Auto-calculations
├── Tab: Monthly Trends            ← Auto from Dashboard
├── Tab: Setter Report             ← Setter fills via Telegram bot
├── Tab: Lead Pipeline             ← Setter + VA maintain
├── Tab: Swipe File Library        ← Team adds
├── Tab: Hook & CTA Bank           ← Team adds
└── Tab: Revenue                   ← Manual (Founder/VA)
```

### Internal Team Sheet (Not Client-Facing)

```
JO Consult Operations Sheet/
├── Tab: All Clients Overview      ← Status per client
├── Tab: Team KPIs                 ← All roles
├── Tab: Revenue Summary           ← MRR, churn, LTV
├── Tab: Automation Log            ← n8n status per client
├── Tab: Hiring Pipeline           ← Open roles
└── Tab: Capacity Planning         ← Clients per team member
```

---

## Obsidian Graph Strategy

For the Obsidian graph to be useful, maintain these **link types**:

```markdown
## In any client note:
- Links to: [[Team_Member]], [[Automation_Name]], [[Deliverable]]
- Tags: #client #active #onboarding #month-2

## In any team KPI note:
- Links to: [[Client_Name]] they serve, [[SOP_Name]] they follow
- Tags: #team #setter #va #closer #creative-director

## In any automation note:
- Links to: [[Client_Name]], [[Tool_Name]]
- Tags: #n8n #automation #active #error

## In Dashboard:
- Links to: everything relevant
- Tags: #dashboard #daily-review
```

**Result:** Obsidian graph shows clusters around:
- Each **client** (connected to their team, automations, deliverables)
- Each **team member** (connected to their clients, KPIs, SOPs)
- Each **automation** (connected to clients it serves)
- **Founder** at the center, connected to everything

---

## Capacity Planning

| Role | Clients Per Person | When To Hire Next |
|------|-------------------|-------------------|
| **Founder** | Unlimited (strategy only) | Never (delegate more) |
| **Closer** | 10-15 calls/week | When pipeline > 15 calls/week |
| **Creative Director** | 3-4 clients | When quality drops or turnaround > 5 days |
| **Setter** | 2-3 clients | When daily DM capacity maxed (100/day/account) |
| **VA** | 4-5 clients | When onboarding delays > 48h |
| **Editor** | 3-4 clients (14 reels each) | When backlog > 1 week |

---

## Quick Reference: Who Uses What

| Tool | Founder | Closer | Creative Dir. | Setter | VA |
|------|---------|--------|--------------|--------|-----|
| Obsidian | **PRIMARY** | — | — | — | — |
| VS Code (Cook) | **PRIMARY** | — | Optional | — | — |
| n8n Dashboard | Monitor | — | — | — | Monitor |
| Excel | Review | Log calls | Review scripts | Log KPIs | Maintain all |
| Telegram | Monitor all | Receive briefs | Receive feedback | EOD reports | Coordinate all |
| Instagram | — | — | Review content | DM outreach | Post content |
| Google Meet | Consultations | Sales calls | Creative calls | — | — |
| CapCut | Creative flow | — | Quality check | — | — |
| Fathom | Review calls | Record calls | — | — | — |
| Meta Business | — | — | — | — | Setup + maintain |
| GDrive | — | — | Review footage | — | Organize all |
| WhatsApp | — | — | — | Voice notes | Client comms |
