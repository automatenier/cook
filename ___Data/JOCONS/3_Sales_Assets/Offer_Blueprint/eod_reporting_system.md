---
tags:
  - consulting
---
# EOD Reporting System — n8n Forms → Excel Sheets → CEO Dashboard

> Every role fills an n8n form daily. Data auto-writes to their role-specific sheet. CEO Dashboard pulls from all sheets.
> Weekly: n8n compiles a presentation-style weekly report.

---

## Architecture

```
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Setter EOD   │   │ VA EOD       │   │ Closer EOD   │   │ Creative Dir │
│ (n8n Form)   │   │ (n8n Form)   │   │ (n8n Form)   │   │ (n8n Form)   │
└──────┬───────┘   └──────┬───────┘   └──────┬───────┘   └──────┬───────┘
       │                  │                  │                  │
       ▼                  ▼                  ▼                  ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Setter EOD   │   │ VA EOD       │   │ Closer EOD   │   │ Creative Dir │
│ Sheet        │   │ Sheet        │   │ Sheet        │   │ EOD Sheet    │
│ (Google)     │   │ (Google)     │   │ (Google)     │   │ (Google)     │
└──────┬───────┘   └──────┬───────┘   └──────┬───────┘   └──────┬───────┘
       │                  │                  │                  │
       └──────────────────┴────────┬─────────┴──────────────────┘
                                   │
                                   ▼
                          ┌────────────────┐
                          │  CEO DASHBOARD  │
                          │  (Google Sheet) │
                          │                │
                          │  Auto-pulls    │
                          │  from all 4    │
                          │  EOD sheets    │
                          └────────┬───────┘
                                   │
                          Every Sunday 20:00
                                   │
                                   ▼
                          ┌────────────────┐
                          │ WEEKLY REPORT  │
                          │ (n8n compiled) │
                          │                │
                          │ Sent to Founder│
                          │ via Telegram   │
                          └────────────────┘
```

---

## n8n Form #1: Setter EOD

**Trigger:** Daily at 21:00 — n8n sends Telegram prompt with form link.
**URL:** `https://[n8n-instance].app/form/setter-eod`

### Form Fields

| Field | Type | Required | Options |
|-------|------|----------|---------|
| `date` | Date | Auto-fill today | — |
| `client` | Dropdown | Yes | [List of active clients] |
| `productivity_score` | Slider | Yes | 1-10 |
| `hours_worked` | Number | Yes | — |
| `inbox_checked` | Number | Yes | — |
| `new_conversations` | Number | Yes | — |
| `follow_ups_sent` | Number | Yes | — |
| `yt_longform_sent` | Number | Yes | — |
| `calls_proposed` | Number | Yes | — |
| `calls_booked` | Number | Yes | — |
| `qualified_bookings` | Number | Yes | — |
| `unqualified_bookings` | Number | Yes | — |
| `icp_leads_found` | Number | Yes | — |
| `convos_nurtured` | Number | Yes | — |
| `calls_on_calendar` | Number | Yes | — |
| `calls_showed` | Number | Yes | — |
| `closed_today` | Number | Yes | — |
| `what_went_well` | Long text | Yes | — |
| `what_could_be_better` | Long text | Yes | — |
| `common_objections` | Long text | Yes | — |
| `situation_update` | Long text | No | — |

### n8n Flow

```
Trigger: Schedule (21:00 daily)
    │
    ├── Send Telegram: "Setter EOD time! Fill form: [link]"
    │
    ▼
Webhook: Form submitted
    │
    ├── Write row to Excel: "Setter EOD Sheet" → new row
    ├── Send confirmation Telegram: "EOD submitted ✅"
    ├── If productivity_score < 5 → alert Founder: "Low productivity flagged"
    ├── If calls_booked = 0 → alert Founder: "Zero bookings today"
    └── Forward common_objections to Creative Director Telegram
```

---

## n8n Form #2: VA EOD

**Trigger:** Daily at 17:00
**URL:** `https://[n8n-instance].app/form/va-eod`

### Form Fields

| Field | Type | Required |
|-------|------|----------|
| `date` | Date | Auto |
| `productivity_score` | Slider 1-10 | Yes |
| `hours_worked` | Number | Yes |
| `clients_serviced` | Multi-select | Yes |
| `onboardings_in_progress` | Number | Yes |
| `onboarding_tasks_completed` | Checklist text | Yes |
| `materials_organized` | Number | Yes |
| `follow_ups_sent_to_clients` | Number | Yes |
| `content_batches_distributed` | Number | Yes |
| `crm_updated` | Yes/No | Yes |
| `n8n_errors_flagged` | Number | Yes |
| `n8n_error_details` | Long text | No |
| `filming_sessions_coordinated` | Number | No |
| `pending_client_approvals` | Number | Yes |
| `what_went_well` | Long text | Yes |
| `what_could_be_better` | Long text | Yes |
| `blockers` | Long text | No |

### n8n Flow

```
Trigger: Schedule (17:00 daily)
    │
    ├── Send Telegram: "VA EOD time! [link]"
    │
    ▼
Webhook: Form submitted
    │
    ├── Write to Excel: "VA EOD Sheet"
    ├── Confirmation Telegram
    ├── If n8n_errors_flagged > 0 → alert Founder with error details
    ├── If pending_client_approvals > 3 → alert: "Multiple approvals pending"
    └── If onboarding delayed (date check) → alert: "Onboarding behind schedule"
```

---

## n8n Form #3: Closer EOD

**Trigger:** After each call day (or daily at 20:00)
**URL:** `https://[n8n-instance].app/form/closer-eod`

### Form Fields

| Field | Type | Required |
|-------|------|----------|
| `date` | Date | Auto |
| `calls_scheduled_today` | Number | Yes |
| `calls_taken` | Number | Yes |
| `no_shows` | Number | Yes |
| `closed_deals` | Number | Yes |
| `total_cash_collected` | Number (Rp) | Yes |
| `deal_details` | Long text | If closed > 0 |
| `packages_sold` | Multi-select | If closed > 0 |
| `objections_encountered` | Long text | Yes |
| `follow_ups_scheduled` | Number | Yes |
| `call_quality_self_score` | Slider 1-10 | Yes |
| `fathom_recording_saved` | Yes/No | Yes |
| `what_went_well` | Long text | Yes |
| `what_could_be_better` | Long text | Yes |
| `notes` | Long text | No |

### n8n Flow

```
Trigger: Schedule (20:00 daily)
    │
    ├── Send Telegram: "Closer EOD time! [link]"
    │
    ▼
Webhook: Form submitted
    │
    ├── Write to Excel: "Closer EOD Sheet"
    ├── If closed_deals > 0:
    │   ├── Telegram to Founder: "🎉 DEAL CLOSED: [details] — Rp [amount]"
    │   ├── Telegram to VA: "New client incoming — start onboarding"
    │   ├── Telegram to Setter: "Nice set! [deal details]"
    │   └── Update CEO Dashboard: Revenue tab
    ├── If no_shows > 0:
    │   └── Alert Setter: "No-show: [names] — follow up needed"
    └── Forward objections to Creative Director
```

---

## n8n Form #4: Creative Director EOD

**Trigger:** Daily at 18:00
**URL:** `https://[n8n-instance].app/form/creative-director-eod`

### Form Fields

| Field | Type | Required |
|-------|------|----------|
| `date` | Date | Auto |
| `productivity_score` | Slider 1-10 | Yes |
| `hours_worked` | Number | Yes |
| `scripts_reviewed` | Number | Yes |
| `scripts_approved` | Number | Yes |
| `scripts_sent_back` | Number | Yes |
| `remotion_baselines_reviewed` | Number | Yes |
| `capcut_finals_approved` | Number | Yes |
| `client_revisions_received` | Number | Yes |
| `filming_sessions_directed` | Number | No |
| `new_swipe_structures_added` | Number | No |
| `objections_from_setter` | Long text | No |
| `content_ideas_from_objections` | Long text | No |
| `what_went_well` | Long text | Yes |
| `what_could_be_better` | Long text | Yes |
| `quality_concerns` | Long text | No |

### n8n Flow

```
Trigger: Schedule (18:00 daily)
    │
    ├── Send Telegram: "Creative Director EOD! [link]"
    │
    ▼
Webhook: Form submitted
    │
    ├── Write to Excel: "Creative Director EOD Sheet"
    ├── If scripts_sent_back > 2 → alert Founder: "High reject rate today"
    ├── If client_revisions_received > 2 → alert: "Multiple revision requests"
    └── If content_ideas_from_objections not empty → add to content backlog
```

---

## Excel: Per-Role EOD Sheets

### Setter EOD Sheet

| Column | Source | Type |
|--------|--------|------|
| Date | Auto | Date |
| Client | Form | Text |
| Productivity | Form | 1-10 |
| Hours | Form | Number |
| Inbox Checked | Form | Number |
| New Convos | Form | Number |
| Follow-ups | Form | Number |
| YT/LF Sent | Form | Number |
| Calls Proposed | Form | Number |
| Calls Booked | Form | Number |
| Qualified | Form | Number |
| Unqualified | Form | Number |
| ICP Leads | Form | Number |
| Nurtured | Form | Number |
| On Calendar | Form | Number |
| Showed | Form | Number |
| Closed | Form | Number |
| What Went Well | Form | Text |
| Could Be Better | Form | Text |
| Objections | Form | Text |
| **7-Day Avg Bookings** | Formula | `=AVERAGE(last 7 rows of Calls Booked)` |
| **Booking Rate** | Formula | `=Calls Booked / Calls Proposed` |
| **Show Rate (rolling)** | Formula | `=SUM(Showed last 7d) / SUM(Booked last 7d)` |

### VA EOD Sheet

| Column | Source | Type |
|--------|--------|------|
| Date | Auto | Date |
| Productivity | Form | 1-10 |
| Hours | Form | Number |
| Clients Serviced | Form | Text |
| Onboardings Active | Form | Number |
| Tasks Completed | Form | Text |
| Materials Organized | Form | Number |
| Follow-ups to Clients | Form | Number |
| Content Batches Out | Form | Number |
| CRM Updated | Form | Y/N |
| n8n Errors | Form | Number |
| Error Details | Form | Text |
| Pending Approvals | Form | Number |
| What Went Well | Form | Text |
| Could Be Better | Form | Text |
| Blockers | Form | Text |
| **Avg Response Time** | Manual | Hours |
| **Onboarding On-Track** | Formula | Y/N based on day count |

### Closer EOD Sheet

| Column | Source | Type |
|--------|--------|------|
| Date | Auto | Date |
| Calls Scheduled | Form | Number |
| Calls Taken | Form | Number |
| No-Shows | Form | Number |
| Deals Closed | Form | Number |
| Cash Collected (Rp) | Form | Number |
| Deal Details | Form | Text |
| Packages | Form | Text |
| Objections | Form | Text |
| Follow-ups Scheduled | Form | Number |
| Call Quality | Form | 1-10 |
| Fathom Saved | Form | Y/N |
| What Went Well | Form | Text |
| Could Be Better | Form | Text |
| **Close Rate (rolling 7d)** | Formula | `=SUM(Closed 7d) / SUM(Taken 7d)` |
| **Show Rate** | Formula | `=Taken / Scheduled` |
| **Avg Deal Size** | Formula | `=Cash / Closed` |
| **Monthly Revenue** | Formula | `=SUM(Cash this month)` |

### Creative Director EOD Sheet

| Column | Source | Type |
|--------|--------|------|
| Date | Auto | Date |
| Productivity | Form | 1-10 |
| Hours | Form | Number |
| Scripts Reviewed | Form | Number |
| Scripts Approved | Form | Number |
| Scripts Rejected | Form | Number |
| Remotion Reviewed | Form | Number |
| CapCut Approved | Form | Number |
| Client Revisions | Form | Number |
| Filming Sessions | Form | Number |
| New Swipe Structures | Form | Number |
| Setter Objections | Form | Text |
| Content Ideas | Form | Text |
| What Went Well | Form | Text |
| Could Be Better | Form | Text |
| Quality Concerns | Form | Text |
| **Approval Rate** | Formula | `=Approved / Reviewed` |
| **Avg Turnaround (days)** | Formula | Script date → Approval date |
| **Revision Rate** | Formula | `=Client Revisions / Total Approved` |

---

## CEO Dashboard — How It Pulls From EOD Sheets

### Tab: `Team Overview` (The One Page)

```
┌─────────────────────────────────────────────────────────────────┐
│                     CEO DASHBOARD — TODAY                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  REVENUE               │  PIPELINE                              │
│  ─────────             │  ────────                              │
│  MTD: Rp XX,XXX,XXX   │  Total Leads: XX                      │
│  Deals This Month: X   │  Qualified: XX                        │
│  Avg Deal: Rp X,XXX   │  Booked This Week: XX                 │
│  MRR: Rp XX,XXX,XXX   │  Show Rate: XX%                       │
│                        │  Close Rate: XX%                       │
│  (from Closer EOD)     │  (from Setter + Closer EOD)           │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CONTENT               │  TEAM HEALTH                           │
│  ───────               │  ───────────                           │
│  Reels Produced: XX/14 │  Setter Productivity: X/10            │
│  Approved: XX          │  VA Productivity: X/10                │
│  Posted: XX            │  Closer Call Quality: X/10            │
│  Avg Views: X,XXX      │  CD Approval Rate: XX%                │
│  Revision Rate: X%     │  n8n Errors Today: X                  │
│                        │  Blockers: [from VA]                   │
│  (from CD EOD +        │  (from all EOD sheets)                │
│   Content Calendar)    │                                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Formulas That Pull From EOD Sheets

| CEO Dashboard Cell | Formula Logic | Source Sheet |
|-------------------|--------------|-------------|
| MTD Revenue | `=SUM(Closer EOD!Cash Collected WHERE month=current)` | Closer EOD |
| Deals This Month | `=SUM(Closer EOD!Deals Closed WHERE month=current)` | Closer EOD |
| Close Rate | `=SUM(Closed) / SUM(Calls Taken)` | Closer EOD |
| Bookings This Week | `=SUM(Setter EOD!Calls Booked WHERE week=current)` | Setter EOD |
| Show Rate | `=SUM(Showed) / SUM(Booked)` | Setter + Closer EOD |
| Setter Productivity | `=AVERAGE(Setter EOD!Productivity last 7d)` | Setter EOD |
| VA Productivity | `=AVERAGE(VA EOD!Productivity last 7d)` | VA EOD |
| CD Approval Rate | `=SUM(Approved) / SUM(Reviewed)` | Creative Dir EOD |
| n8n Errors | `=SUM(VA EOD!n8n Errors today)` | VA EOD |
| Reels Produced | `=COUNTIF(Content Calendar!Edit Status="Done")` | Content Calendar |
| Revision Rate | `=CD EOD Client Revisions / Total Approved` | Creative Dir EOD |

---

## Weekly Report (n8n Compiled)

**Trigger:** Every Sunday 20:00
**Format:** Telegram message — structured, visual, scannable.

### n8n Flow

```
Trigger: Schedule (Sunday 20:00)
    │
    ├── Read: Setter EOD Sheet (last 7 rows)
    ├── Read: VA EOD Sheet (last 7 rows)
    ├── Read: Closer EOD Sheet (last 7 rows)
    ├── Read: Creative Director EOD Sheet (last 7 rows)
    ├── Read: CEO Dashboard (current values)
    │
    ▼
Compile into formatted message
    │
    ▼
Send to Founder via Telegram
```

### Weekly Report Template (Telegram Message)

```
📊 WEEKLY REPORT — Feb 10-16, 2026

━━━━━━━━━━━━━━━━━━━━━━━

💰 REVENUE
Revenue this week: Rp X,XXX,XXX
Deals closed: X
MTD total: Rp XX,XXX,XXX
Close rate: XX%

━━━━━━━━━━━━━━━━━━━━━━━

📈 PIPELINE
New leads found: XX
Conversations opened: XX
Calls booked: XX
Show rate: XX%
Follow-ups sent: XXX

━━━━━━━━━━━━━━━━━━━━━━━

🎬 CONTENT
Reels produced: X/14
Scripts approved: X
Client revisions: X
Avg views (posted): X,XXX
Best performer: "[hook]" — X,XXX views

━━━━━━━━━━━━━━━━━━━━━━━

👥 TEAM HEALTH
Setter avg productivity: X/10
VA avg productivity: X/10
Closer avg call quality: X/10
CD approval rate: XX%
n8n errors this week: X

━━━━━━━━━━━━━━━━━━━━━━━

⚠️ FLAGS
- [Any low scores, missed targets, blockers]
- [Setter: "Low booking rate — review scripts"]
- [VA: "Client X approval pending 3 days"]

━━━━━━━━━━━━━━━━━━━━━━━

🏆 WINS
- [Notable achievements from EOD "what went well"]

📋 NEXT WEEK FOCUS
- [Auto-generated from patterns + flags]
```

---

## n8n Workflow Specs Summary

| Workflow | Trigger | Input | Output |
|----------|---------|-------|--------|
| `setter-eod-form` | 21:00 daily | Telegram prompt | Form link |
| `setter-eod-process` | Form webhook | Form data | Sheet row + alerts |
| `va-eod-form` | 17:00 daily | Telegram prompt | Form link |
| `va-eod-process` | Form webhook | Form data | Sheet row + alerts |
| `closer-eod-form` | 20:00 daily | Telegram prompt | Form link |
| `closer-eod-process` | Form webhook | Form data | Sheet row + alerts + revenue notify |
| `cd-eod-form` | 18:00 daily | Telegram prompt | Form link |
| `cd-eod-process` | Form webhook | Form data | Sheet row + alerts |
| `weekly-report` | Sunday 20:00 | All 4 EOD sheets + CEO Dashboard | Telegram report to Founder |
| `alert-low-performance` | Any EOD with score < 5 | EOD data | Telegram alert to Founder |
| `alert-deal-closed` | Closer reports close | Closer EOD | Telegram blast to team |
| `alert-n8n-error` | VA reports error | VA EOD | Telegram alert to Founder |

---

## Setup Checklist

| # | Task | Tool | Status |
|---|------|------|--------|
| 1 | Create Setter EOD Sheet (Excel) | Sheets | |
| 2 | Create VA EOD Sheet | Sheets | |
| 3 | Create Closer EOD Sheet | Sheets | |
| 4 | Create Creative Director EOD Sheet | Sheets | |
| 5 | Create CEO Dashboard with IMPORTRANGE formulas | Sheets | |
| 6 | Build n8n form: setter-eod | n8n | |
| 7 | Build n8n form: va-eod | n8n | |
| 8 | Build n8n form: closer-eod | n8n | |
| 9 | Build n8n form: cd-eod | n8n | |
| 10 | Build n8n: form → Sheet writer (×4) | n8n | |
| 11 | Build n8n: daily Telegram reminders (×4) | n8n | |
| 12 | Build n8n: alert workflows | n8n | |
| 13 | Build n8n: weekly report compiler | n8n | |
| 14 | Connect CEO Dashboard formulas to all sheets | Sheets | |
| 15 | Test end-to-end: form → sheet → dashboard → report | All | |
