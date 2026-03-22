---
tags:
  - consulting
---
# Setter DM Outreach Workflow

## Objective
Find ICPs on Instagram, build genuine relationships through DMs, and book qualified sales calls. Never be salesy.

## Required Inputs
- Access to JO Consult Instagram account
- Excel CRM (generated via `tools/create_excel_crm.py`)
- Target ICP criteria (fitness coaches, 1K-10K followers, posting content but inconsistent)

## Tools Used
- Instagram (manual - no automation for outreach, must be human and organic)
- Excel CRM (for tracking)
- Google Calendar (for booking)
- WhatsApp (for voice notes and reminders)

## The 9-Stage Process

### Stage 1: Discovery (Daily - find 4+ new ICPs)

**Where to search:**
- Competitor followers: @wefit_id, @kelasfitness.id, @lifecoach.idn
- Hashtags: #personaltrainerindonesia #fitnesscoachindonesia #onlinecoachingid
- Location tags: Gym locations in Jakarta, BSD, Surabaya
- Post engagers: People asking questions on competitor content
- Your own reel viewers who watched but didn't follow

**ICP checklist (must match 3+):**
- [ ] Posts fitness content but inconsistently
- [ ] 1K-10K followers with low engagement
- [ ] Has a link in bio to coaching services
- [ ] Comments/asks questions about business growth
- [ ] Located in Indonesia (or Indonesian market)

**Action:** Add to Excel CRM → leadType: ICP, stage: Discovery, source: [method used]

### Stage 2: Engaged (2-3 days per prospect)

**Actions:**
1. Like 3-5 of their recent posts (genuine, not rapid-fire)
2. Leave 2-3 meaningful comments showing you watched their content
3. Watch and react to their stories
4. Reply to one story with something conversational

**Comment examples (adapt to their content):**
- "That superset combo is underrated - do you program it for hypertrophy or strength?"
- "Your client's posture improvement is insane. How long did that take?"
- "This is the kind of content the fitness space needs more of"

**Do NOT DM yet.** Let them notice you first.

**Action:** Update Excel → stage: Engaged, last contact: [date]

### Stage 3: Conversation (3-5 days)

**Goal:** Open a natural DM conversation about THEM.

**How to open:**
- Reply to their story with a genuine question
- Reference a specific recent post in DM
- Ask about their coaching approach

**Opener templates:**
- "Saw your client's transformation - what was the biggest mindset shift they had?"
- "Your reel about [topic] was spot on. Curious - does that work better for beginners?"
- "That gym setup is sick - are you training out of your own space?"

**Rules:**
- Talk about THEM, not you
- Match their energy
- Keep it conversational, not interview-style
- Minimum 3 genuine back-and-forth exchanges

**Action:** Update Excel → stage: Conversation

### Stage 4: Problem Aware (3-7 days)

**Goal:** They naturally share a business pain point.

**How to guide there:**
- "How long have you been doing online coaching?"
- "What's been the hardest part about scaling?"
- "Are you doing this full time?"

**Listen for pain signals:**
- "I can't get consistent leads"
- "I post content but nobody DMs me"
- "I'm stuck at X clients"
- "I spend all day creating content"

**Response:** Validate and empathize. Do NOT offer solutions.
- "Yeah that's literally the #1 thing coaches at your stage deal with"
- "Makes sense - that's a capacity problem, not a skill problem"

**Action:** Update Excel → stage: Problem Aware, problem identified: [their pain]

### Stage 5: Solution Aware (1-3 days)

**Goal:** They discover what you do ORGANICALLY.

**How this happens:**
- They visit your profile and see your Value & CTA reels
- You mention it naturally: "Yeah I actually help coaches build their systems"
- They see your Threads lead magnet content
- Another coach mentions you

**Key:** They discover your offer. You don't pitch it.

**Action:** Update Excel → stage: Solution Aware

### Stage 6: Interested (1-2 days)

**Signals they're ready:**
- "Wait, you help coaches with this?"
- "How does your program work?"
- "Can you help me?"

**Response framework:**
1. Acknowledge their specific pain (show you listened)
2. Brief overview (casual, not a pitch deck)
3. Social proof: "I just helped [name] go from X to Y"
4. Soft CTA: "Want to jump on a quick call? I can show you how we'd do it for your situation"

**Action:** Update Excel → stage: Interested

### Stage 7-9: Booked → Showed → Closed

1. Send Google Calendar link
2. n8n auto-triggers: WA reminder (24h + 1h), email with VSL
3. Optional: ElevenLabs voice note ("excited to chat about [their pain]")
4. Conduct closing call
5. Payment → Onboarding
6. **Within 24 hours of payment:** Fill out the Deal Close Report → `Fulfillment/_OFFER_BLUEPRINT/setter_close_report.md`

**Action:** Update Excel through each stage

## Setter Daily Report (fill in Excel "Setter Report" sheet)

| Metric | Daily Target |
|--------|-------------|
| New discoveries added | 4 |
| Engagements started | 3 |
| DM convos opened | 1-2 |
| Stages advanced | 2-3 |
| Calls booked | 0-1 |

## Edge Cases
- If prospect goes cold: move back one stage, re-engage with stories/comments. Do NOT follow up with "hey just checking in"
- If prospect asks for price too early: redirect to value first. "Before I share that, let me understand your situation better"
- If prospect is not ICP: politely disengage. Don't waste time on bad fits
- If prospect objects: do NOT handle in DM. Book a call instead. "This is way easier to explain on a quick chat"

## KPIs (Weekly)
| Metric | Target |
|--------|--------|
| New discoveries | 20 |
| Conversations opened | 8 |
| Problem Aware (new) | 4 |
| Calls booked | 2 |
| Show rate | 80%+ |
