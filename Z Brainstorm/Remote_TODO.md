# Remote Management & Vibe Coding Guide

This document tracks the setup and tasks for managing the Cook business system remotely via mobile (Telegram / SSH).

## 1. Remote Connectivity Stack
- [x] **Telegram Bridge:** `AI_Tools/gemini_remote.py` (Authorized: 6228081299)
- [ ] **Tailscale Mesh:** Install on PC + Phone for secure SSH/Remote Desktop.
- [ ] **OpenSSH Server:** Enable on Windows for low-bandwidth terminal access.

## 2. Mobile "Vibe Coding" Tasks
| Task | Command Category | Status |
|------|-----------------|--------|
| Content Download | `content_download_reels_v2.py` | Ready |
| Lead Monitoring | `check_leads()` in bridge | Active |
| Daily Summaries | `check_daily_summary()` | Scheduled 20:00 |
| CRM Updates | `cook_crm_manager.py` | Ready |
| YouTube Insights | `vault_youtube_note.py` | Ready |

## 3. High-Value Mobile Use Cases
- **The Content Capture:** Send a TikTok/IG link to the bot -> PC downloads and analyzes.
- **The Lead Alert:** Bot pings phone when a new row is added to `lead_attribution.csv`.
- **The System Check:** Send `/status` to see if the PC is alive and tasks are running.
- **The Quick Edit:** Ask Gemini to modify script parameters (font size, API keys, etc.).

## 4. Maintenance
- [ ] Ensure PC "Sleep" mode is disabled when away.
- [ ] Check `GEMINI_BOT_TOKEN` environment variable if bridge fails.
- [ ] Review `.tmp/gemini_remote.log` for execution errors.

---
*Last Updated: 2026-03-18*
