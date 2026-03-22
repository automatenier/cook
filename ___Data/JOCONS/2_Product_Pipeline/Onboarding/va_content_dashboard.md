---
tags:
  - consulting
---
# VA Content Dashboard — Quick Access

> All tools, files, and links the VA needs for the content system. Organized chronologically following the SOP flow.

---

## Phase 1 — Research & Strategy (Before Content Creation)

| Resource | Type | What It's For |
|---|---|---|
| [[Content System Steps]] | Canvas | Full visual flow of the content system |
| Content Notebook LM | Notebook | Research notes, trends, niche insights |
| Swipe Files Content Copy | Doc | Winning captions, hooks, CTAs to reference |
| Strategy Pillar Content | Doc | Content pillar framework (Education, Authority, Connection, Social Proof) |

---

## Phase 2 — Swipe File & Inspiration

| Resource | Type | What It's For |
|---|---|---|
| Swipe Files Content Canvas | Canvas | Visual board of winning content references |
| Reel Analyzer Bot (Telegram) | n8n Bot | Analyze viral reels → structure breakdown |
| `.tmp/reels/` | Folder | Downloaded reference reels |

---

## Phase 3 — Content Calendar & Planning

| Resource | Type | What It's For |
|---|---|---|
| Content Calendar (all) | Excel | Master calendar — all clients, all platforms, all dates |
| Weekly Content Calendar Template | Markdown | 4-week template with daily breakdown per platform |
| Content Gap Analysis | Markdown | Identify missing pillars/formats in current mix |

---

## Phase 4 — Content Production

| Resource | Type | What It's For |
|---|---|---|
| `tools/analyze_viral_reel.py` | Script | Reel analysis → JSON structure |
| `tools/repurpose_content.py` | Script | Claude repurposing → Threads, email, YouTube, TikTok |
| Remotion templates | Code | ValueCTAReel + AuthenticityReel draft generation |
| CapCut | App | Final editing (transitions, music, captions) |
| Follow up Pic | Design | Follow-up image templates / visual assets |

---

## Phase 5 — Scheduling & Publishing

| Platform | Scheduler | Manual? |
|---|---|---|
| Instagram | Meta Business Suite Scheduler | Auto via Meta API (n8n) |
| Facebook | Meta Business Suite Scheduler | Auto via Meta API (n8n) |
| TikTok | TikTok Business Center | **Manual upload** (no public API) |
| YouTube | YouTube Studio / n8n auto-post | Auto via YouTube Data API |
| Threads | Meta API (separate) | Can be automated later |

### Scheduler Links

| Tool | Link |
|---|---|
| Meta Scheduler | Meta Business Suite → Content → Planner |
| TikTok Scheduler | [TikTok Biz Center Post](https://business.tiktok.com/manage/tiktokAccount/uploadContent) |
| YouTube Scheduler | YouTube Studio → Content → Upload |

---

## Phase 6 — Tracking & Reporting

| Resource | Type | What It's For |
|---|---|---|
| Content Calendar (all) | Excel | Track status: Drafted → Editing → Approved → Posted |
| Content Audit Checklist | Markdown | Score each piece (Hook/CTA/Niche/Engagement/Pillar out of /50) |
| n8n Metrics Pull | Automation | Daily IG/FB/YT metrics → Google Sheets |

---

## Daily VA Content Checklist

```
□ 08:00 — Check content calendar: what's due today?
□ 08:30 — Confirm scheduled posts went live (IG, FB, YT)
□ 09:00 — Upload TikTok manually (mirror IG reel)
□ 09:30 — Brief Editor on today's production batch
□ 10:00 — Review swipe files: add any new winning content found
□ 12:00 — Check post performance (engagement, comments to reply to)
□ 14:00 — Prep tomorrow's content: captions, thumbnails, scheduling
□ 16:00 — Update content calendar status (Drafted → Posted)
□ 17:00 — EOD: flag any missing/delayed content to Jordan
```

---

## New Client Content Setup Checklist

When onboarding a new client, run through this in order:

```
□ 1. Create client content folder in GDrive
□ 2. Duplicate Content Calendar (Excel) for client
□ 3. Run Content Audit (last 20 posts) → fill checklist
□ 4. Run Content Gap Analysis → identify missing pillars
□ 5. Build Strategy Pillar Content doc for client
□ 6. Fill 4-week Content Calendar from audit results
□ 7. Collect swipe files for client's niche → add to Canvas
□ 8. Request Meta Business Suite access (Admin role)
□ 9. Request TikTok Business Center access
□ 10. Request YouTube channel access (if applicable)
□ 11. Setup Meta Scheduler for client
□ 12. Setup TikTok Scheduler bookmark
□ 13. Setup YouTube Scheduler (n8n auto-post or manual)
□ 14. First batch of content → Editor for production
□ 15. First post goes live → confirm all platforms working
```

---

## File Locations

| Item | Path |
|---|---|
| Content Creation Workflow | `workflows/content_creation.md` |
| Weekly Calendar Template | `Fulfillment/_CONTENT_AUDIT/audit_templates/weekly_content_calendar_template.md` |
| Content Audit Checklist | `Fulfillment/_CONTENT_AUDIT/audit_templates/content_audit_checklist.md` |
| Content Gap Analysis | `Fulfillment/_CONTENT_AUDIT/audit_templates/content_gap_analysis.md` |
| VA Team Roadmap | `Fulfillment/_ONBOARDING/team_roadmap_va.md` |
| Editor Team Roadmap | `Fulfillment/_ONBOARDING/team_roadmap_editor.md` |
| Reel Analyzer Bot | `n8n/_CLIENT_SYSTEMS/All/Reel Analyzer.md` |
| YouTube Auto-Post | `n8n/_HTS_AGENCY/Content/YouTube-AutoPost.md` |
| FB/IG Auto-Post | `n8n/_HTS_AGENCY/Content/FB-IG-AutoPost.md` |
