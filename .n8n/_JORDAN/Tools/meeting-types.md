---
tags:
  - automation
---
# Meeting Types — Google Calendar

> All recurring meeting types that need calendar + notification automation.

---

| Meeting Type | Frequency | Who | Purpose |
|---|---|---|---|
| **Sales Meet** | Per booking | Jordan + Prospect | Discovery / closing call |
| **Support Meet** | 5x / month | Jordan + Client | Support & troubleshooting |
| **Weekly Meet 1st** | Once (first week) | Jordan + Client | First weekly onboarding |
| **Weekly Meet** | Weekly (ongoing) | Jordan + Client | Recurring weekly check-in |
| **Coach Meet 1st** | Once (first week) | Jordan + Client's coach | First coach integration call |
| **Coach Meet** | Recurring | Jordan + Client's coach | Ongoing coach sync |
| **Team Meet** | Weekly | Jordan + VA + Editor + Setter | Internal team sync |

---

## Automation Needed Per Type

Each meeting type needs:
1. Google Calendar event creation
2. WA reminder (24h before) — existing: `Notif-SalesCall-WA Reminder`
3. Email reminder (1h before) — TO BUILD: `Booking-Email-1h-Reminder`
4. Telegram notification (internal) — existing: `Notif-Sales Call`
5. No-show follow-up — TO BUILD: `Booking-NoShow-MultiChannel`

## Calendar Label System

Use Google Calendar color codes to differentiate:
- **Red:** Sales Meet (revenue)
- **Blue:** Support Meet (client care)
- **Green:** Weekly Meet (recurring)
- **Purple:** Coach Meet (coaching)
- **Yellow:** Team Meet (internal)
