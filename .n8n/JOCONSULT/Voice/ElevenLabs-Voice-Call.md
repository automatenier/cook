---
tags:
  - automation
---
# ElevenLabs Voice Call — HTS Agency

> AI voice agent for inbound/outbound calls using ElevenLabs Conversational AI.

---

## Purpose
- Handle inbound calls from VSL page ("Talk to Jule" button)
- Same persona as chatbot Jule — female, Jakarta, witty, casual
- Qualify leads via voice, then book meeting

## Setup
- **ElevenLabs Agent:** Conversational AI agent
- **Voice:** Female Indonesian voice (or clone from team member)
- **Language:** Indonesian primary, English fallback
- **Trigger:** Phone number on VSL page OR "Call us" button

## Voice Agent System Prompt
Same as VSL-Chatbot-Jule.md with these additions:
```
You are speaking on a phone call, not a chat. Keep responses very short (1-2 sentences max).
Pause naturally between sentences. Use filler words like "Hmm", "Oke", "Jadi gini".
If you can't understand them, say "Maaf, bisa diulang? Gue kurang denger tadi."
Never say you're an AI unless directly asked.
```

## Flow
```
Inbound Call (ElevenLabs)
  → Voice Agent: Greet + qualify
  → IF booking:
      → ElevenLabs → Webhook to n8n
      → n8n: Create Google Calendar event
      → n8n: Send WA confirmation
      → n8n: Telegram notification
      → n8n: Log to Google Sheets
  → Call ends
```

## N8N Integration
- **Webhook:** ElevenLabs sends call transcript + booking data to n8n webhook
- **n8n processes:** Same as chatbot flow (Calendar + Gmail + Telegram + Sheets)

## Dependencies
- ElevenLabs Conversational AI (from your 1-year plan)
- n8n webhook endpoint
- Google Calendar, Gmail, Telegram, Google Sheets (existing)
