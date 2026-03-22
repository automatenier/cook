---
tags:
  - automation
---
# Booking-NoShow-MultiChannel

> Multi-channel follow-up when a prospect no-shows a discovery call. WA → wait → Email → wait → DM. Extends existing Notif-NOSHOW-WA.

---

## Trigger
- **Type:** Webhook (manual trigger from Jordan or auto-detect from calendar)
- **Alternative:** Manual trigger in n8n when you confirm a no-show

## Flow

```
Webhook / Manual Trigger (no-show detected)
  → Edit Fields: Extract prospect name, email, WA number, IG handle
  → Step 1: WhatsApp (Wassenger) — Empathetic reschedule message
  → Wait: 2 hours
  → IF: No reply on WA?
      → Step 2: Gmail — Email follow-up with reschedule link
      → Wait: 24 hours
      → IF: Still no reply?
          → Step 3: Telegram Alert — "DM {IG_handle} manually with rescue script"
          → Google Sheets: Update CRM → status: "No-Show-Followup"
  → IF: Reply received at any step
      → Telegram: Notify "{name} replied! Reschedule in progress"
      → Google Sheets: Update CRM accordingly
```

## Nodes Detail

### 1. Webhook Trigger
```json
{
  "type": "n8n-nodes-base.webhook",
  "parameters": {
    "path": "noshow-followup",
    "httpMethod": "POST"
  }
}
```

**Payload expected:**
```json
{
  "prospect_name": "Coach Andi",
  "wa_number": "628123456789",
  "email": "andi@email.com",
  "ig_handle": "@coachandi",
  "original_time": "2026-02-17T14:00:00",
  "reschedule_link": "https://calendar.google.com/..."
}
```

### 2. WhatsApp (Wassenger API) — Step 1 (Immediate)

**Message:**
```
Hey {prospect_name}! 👋

Gue notice kita missed call tadi jam {original_time}.

No worries — gue tau kadang jadwal berubah mendadak.

Mau reschedule? Pilih waktu yang paling enak buat lo:
{reschedule_link}

Atau reply di sini — gue flexible 🙌
```

### 3. Wait Node — 2 Hours
```json
{
  "type": "n8n-nodes-base.wait",
  "parameters": { "amount": 2, "unit": "hours" }
}
```

### 4. Gmail — Step 2 (2h after WA)

**Subject:** `Missed you today — let's reschedule? 🙌`
**Body:**
```html
<p>Hey {prospect_name},</p>

<p>Kita punya jadwal call hari ini tapi gak sempet connect.</p>

<p>Gue totally get it — life happens. Gue masih excited buat ngobrol sama lo tentang coaching bisnis lo.</p>

<p><b>Reschedule di sini:</b> <a href="{reschedule_link}">{reschedule_link}</a></p>

<p>Kalau situasinya berubah dan lo gak lagi butuh bantuan, that's cool too — just let me know dan gue gak akan follow up lagi.</p>

<p>All the best,<br>Jordan</p>
```

### 5. Wait Node — 24 Hours
```json
{
  "type": "n8n-nodes-base.wait",
  "parameters": { "amount": 24, "unit": "hours" }
}
```

### 6. Telegram Alert — Step 3 (24h after email)

**Message to internal team channel:**
```
⚠️ NO-SHOW FOLLOW-UP — Step 3

Prospect: {prospect_name}
IG: {ig_handle}
Status: No reply on WA (2h ago) + Email (24h ago)

ACTION NEEDED:
→ Setter: DM {ig_handle} with rescue script:

"Hey {prospect_name}! Gue Jordan dari JO Consult. Kita punya call kemarin tapi gak sempet connect. Gue mau pastiin semuanya OK. Kalau masih tertarik ngobrol, reply aja di sini — gue flexible banget soal waktu 🙌"

→ If no reply after 48h: archive in CRM.
```

### 7. Google Sheets — Update CRM
- Update prospect row: `status = "No-Show-Step-{1/2/3}"`
- Add `last_followup_date = NOW()`

## Timing Summary

| Step | Channel | Timing | Action |
|---|---|---|---|
| 1 | WhatsApp | Immediate | Empathetic reschedule |
| 2 | Email | +2 hours | Formal reschedule |
| 3 | IG DM (manual via Setter) | +24 hours | Last attempt |
| 4 | Archive | +48 hours | Move to cold nurture |

## Dependencies
- Wassenger API (for WhatsApp — or use existing WA integration)
- Gmail OAuth (existing)
- Telegram Bot (existing)
- Google Sheets CRM (existing)

## Pairs With
- `Notif-NOSHOW-WA` — Existing WA-only no-show (this replaces/extends it)
- `Notif-SalesCall-WA Reminder` — Pre-call WA reminder (prevention)
- `Booking-Email-1h-Reminder` — Pre-call email (prevention)

## Error Handling
- If WA fails → skip to email immediately
- If email fails → skip to Telegram alert immediately
- All failures → `Notif-Error` workflow
- Never send more than 3 total follow-ups (3 strikes rule from reactivation SOP)
