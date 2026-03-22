---
tags:
  - automation
---
# WhatsApp ElevenLabs Agent — Jordan Personal

> Draft system prompt for personal WhatsApp voice agent via ElevenLabs Conversational AI. Currently a template — needs customization for JO Consult / HTS Agency use case.

---

## Status: DRAFT — Needs Customization

This is the initial draft from ElevenLabs template. The booking flow structure is solid but needs to be adapted from the barbershop example to Jordan's actual business (JO Consult sales calls or HTS Agency meetings).

---

## Current Draft (ElevenLabs Format)

### Goal

Your goal here is to assist inbound callers with their request. A user may request a booking, or just have some general information.

### Task

#### 1. Introduction

- Begin with a polite greeting.
- Identify the user's intent (New Booking, General Intent).

#### 2. Scheduling a New Booking

**Step 1 — Collect Details**

**Ask:**
> "Sure, could I grab your name and number please?"

→ Collect `<name>` and `<number>`

**Confirm number:** Repeat the user's number to confirm:
> "And just to make sure I heard that correctly, your number was `<number>`, was that correct?"

If the number is correct, proceed, else re-collect.

Always convert user's number into international format, replacing 0 with +62 (Indonesia). For example, a spoken number "08123456789" should be converted to "+628123456789".

**Ask:**
> "And what type of consultation were you after?"

→ Collect `<type>`

Then proceed with:

**Ask:**
> "And what time did you want to come in?"

→ Collect `<preferred date and time>`

---

## Customization Needed

| Field | Current (Template) | Should Be |
|---|---|---|
| Number format | +61 (Australia) | +62 (Indonesia) |
| Service types | Crew cut, fade, beard trim | Sales call, consultation, mentorship session |
| Booking target | Barbershop appointment | Google Calendar via n8n webhook |
| Language | English | Indonesian primary, English fallback |
| Persona | Generic | Jordan's voice clone or professional male Indonesian |

## Target Integration

```
ElevenLabs Conversational AI (WhatsApp)
  → Voice Agent: Greet + qualify + collect booking details
  → On booking confirmed:
      → Webhook to n8n
      → n8n: Create Google Calendar event
      → n8n: Send WA confirmation message
      → n8n: Telegram notification to Jordan
      → n8n: Log to Google Sheets CRM
```

## Dependencies
- ElevenLabs Conversational AI (from Jordan's 1-year plan)
- WhatsApp Business API integration (via ElevenLabs or Wassenger)
- n8n webhook endpoint
- Google Calendar, Telegram, Google Sheets (existing)
