---
tags:
  - automation
---
# Telegram Bot — Setter Command Reference

> Share this with your setter team. Bot name: @HTSSetterBot (or whatever you name it)

---

## Commands

### `/suggest` — Get reply options for a DM conversation
**Use when:** Lead sent a message and you're not sure what to say next.

```
/suggest
LEAD: @[their_username]
STAGE: [Discovery / Engaged / Conversation / Problem Aware / Solution Aware / Interested]
PAIN: "[their exact words about their problem, if known]"

CONVO:
Them: [their last message]
Me: [your last reply]
Them: [their reply]
... (paste as many lines as needed, most recent last)
```

**Example:**
```
/suggest
LEAD: @ahmadfitnessid
STAGE: Problem Aware
PAIN: "posting tiap hari tapi ga ada yang DM"

CONVO:
Them: Udah 8 bulan online coaching, klien cuma 2 orang
Me: Nah itu wajar banget di stage itu. Yang paling bikin capek apanya?
Them: Kontennya sih. Tiap hari bikin tapi engagement nya flat terus
```

---

### `/stage` — Ask Claude what stage a lead is at
**Use when:** You've been talking to someone but lost track of where they are.

```
/stage
LEAD: @[username]

CONVO:
[paste full conversation]
```

---

### `/openers` — Get 3 cold opener options for a new lead
**Use when:** You've finished the Engage phase (liked posts, commented) and ready to open DM.

```
/openers
LEAD: @[username]
NICHE: [their niche, e.g. "fitness coach, bodybuilding focus"]
RECENT POST: "[describe or paste their most recent post topic]"
FOLLOWERS: [approx follower count]
```

**Example:**
```
/openers
LEAD: @coach.budi
NICHE: fitness coach, weight loss for busy moms
RECENT POST: "Posted a reel about her client losing 8kg in 3 months"
FOLLOWERS: 2,400
```

---

### `/reactivate` — Revive a cold lead
**Use when:** Lead went silent after 3+ days and you need to re-open the conversation.

```
/reactivate
LEAD: @[username]
STAGE: [stage when they went cold]
LAST MESSAGE: "[what they last said]"
DAYS SILENT: [number]
```

---

### `/book` — Get booking CTA options
**Use when:** Lead is clearly at Stage 6 (Interested) and ready to be offered a call.

```
/book
LEAD: @[username]
PAIN SUMMARY: [2-3 words describing their main problem]
CONVO TONE: [casual / formal / mixed]
```

---

## Quick Cheat Sheet for Setters

| Situation | Command |
|---|---|
| They just replied, not sure what to say | `/suggest` |
| Not sure which stage they're at | `/stage` |
| Ready to open DM for first time | `/openers` |
| They went cold 3+ days | `/reactivate` |
| They said "how does it work?" | `/book` |

---

## Tips

- **Paste the last 4-6 messages** in CONVO — more context = better suggestions
- **Include their exact words** in PAIN field — Claude uses their language to mirror it back
- **Don't over-edit Claude's suggestions** — they're designed to sound human already
- **Always review before sending** — you know the vibe of the conversation better than Claude does
- If Claude's suggestion feels off, just type back: `try again, make it more [casual/direct/warm]`
