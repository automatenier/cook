---
tags:
  - automation
---
# Booking-Email-1h-Reminder

> Sends email reminder 1 hour before a discovery call with Zoom link, agenda, and prep tips.

---

## Trigger
- **Type:** Google Calendar Trigger (event starting)
- **Calendar:** Consulting calendar (same as Calendar-Assign-Setup)
- **Timing:** 1 hour before event start

## Flow

```
Google Calendar Trigger (1h before event)
  → Edit Fields: Extract attendee email, name, event time
  → IF: Has attendee email?
      → YES:
          → Gmail: Send reminder email
          → Telegram: Log "Reminder sent to {name}" to internal channel
      → NO:
          → Telegram: Alert "No email found for booking at {time}"
```

## Nodes Detail

### 1. Google Calendar Trigger
```json
{
  "type": "n8n-nodes-base.googleCalendarTrigger",
  "parameters": {
    "calendarId": "{consulting_calendar_id}",
    "triggerOn": "eventStarted",
    "options": { "minutesBefore": 60 }
  }
}
```

### 2. Edit Fields — Extract Data
```
attendee_name = event.attendees[0].displayName
attendee_email = event.attendees[0].email
event_time = event.start.dateTime (format to "HH:MM WIB")
event_date = event.start.dateTime (format to "DD MMM YYYY")
zoom_link = event.hangoutLink OR event.description (extract Zoom URL)
```

### 3. Gmail — Send Reminder
- **To:** `{attendee_email}`
- **Subject:** `Reminder: Call kita hari ini jam {event_time} 👋`
- **Body:**

```html
<p>Hey {attendee_name}!</p>

<p>Ini reminder — kita ada call <b>hari ini jam {event_time} WIB</b>.</p>

<p><b>🔗 Join di sini:</b> <a href="{zoom_link}">{zoom_link}</a></p>

<p><b>📋 Agenda (15-17 menit):</b></p>
<ol>
  <li>Kenalan singkat (2 min)</li>
  <li>Gue mau dengerin situasi coaching bisnis lo sekarang (5 min)</li>
  <li>Gue share gimana gue bisa bantu (5 min)</li>
  <li>Q&A + next steps (3-5 min)</li>
</ol>

<p><b>💡 Prep tips:</b></p>
<ul>
  <li>Siapkan: berapa klien sekarang, target klien, biggest challenge</li>
  <li>No need to prepare anything formal — this is a casual chat</li>
  <li>Pastikan internet stabil + headphone ready</li>
</ul>

<p>See you soon! 🙌</p>

<p>— Jordan<br>JO Consult</p>
```

### 4. Telegram — Log Confirmation
- **Chat ID:** Internal team channel
- **Message:** `📧 Email reminder sent to {attendee_name} ({attendee_email}) for call at {event_time}`

## Dependencies
- Google Calendar OAuth (already configured in Calendar-Assign-Setup)
- Gmail OAuth (already configured in Form-B-Invoice)
- Telegram Bot (existing)

## Pairs With
- `Notif-SalesCall-WA Reminder` — WA reminder (24h before, already exists)
- `Notif-NOSHOW-WA` — No-show follow-up (already exists)
- `Booking-NoShow-MultiChannel` — Enhanced no-show (to build)

## Error Handling
- If no email in attendee → Telegram alert to manually send
- If Gmail fails → Telegram fallback with attendee details so you can manually email
- Connect to `Notif-Error`
