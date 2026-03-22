---
tags:
  - automation
---
# YouTube Auto-Posting & Metrics — HTS Agency

> Automates YouTube video publishing via YouTube Data API and pulls performance metrics for reporting.

---

## Purpose
- Auto-publish videos to client YouTube channels from n8n
- Pull YouTube metrics (views, watch time, subscribers) for reporting dashboards
- Reduce manual upload work for VA/editors

---

## Flow — Auto-Publish Video

```
Trigger: Google Sheets row updated (status = "Ready to Publish")
  OR
Trigger: Telegram (VA sends /publish-yt {video_id})

  → Google Drive: Get video file from client's content folder
  → YouTube Data API (v3): Upload video
      - title: {from Google Sheets}
      - description: {from Google Sheets}
      - tags: {from Google Sheets}
      - categoryId: based on niche
      - privacyStatus: "public" (or "scheduled" with publishAt)
      - thumbnail: Upload custom thumbnail from GDrive
  → Google Sheets: Update status to "Published", add YouTube URL
  → Telegram: Notify VA + Coach
      "✅ Video published on YouTube
       Title: {title}
       URL: {youtube_url}
       Scheduled: {publish_time}"
```

## Flow — Scheduled Publishing

```
Cron (check every hour)
  → Google Sheets: Find videos with status = "Scheduled" AND publish_time <= now
  → FOR EACH video:
      → YouTube Data API: Upload with privacyStatus = "public"
      → Google Sheets: Update status
      → Telegram: Notification
```

## Flow — YouTube Metrics Pull (Daily)

```
Cron (08:00 WIB daily)
  → YouTube Analytics API: Pull metrics for last 7 days
      - views, estimatedMinutesWatched, averageViewDuration
      - subscribersGained, subscribersLost
      - likes, comments, shares
  → Google Sheets: Write to "YouTube Metrics" tab
      Per video: views, watch time, CTR, avg view duration
      Channel level: total views, new subs, top performing video
  → IF: Any video hit milestone (1K, 5K, 10K, 50K, 100K views)
      → Telegram: "🎉 {video_title} just hit {milestone} views!"
```

## Flow — Weekly YouTube Report

```
Cron (Monday 09:00 WIB)
  → YouTube Analytics API: Pull last 7 days channel data
  → Code Node: Calculate week-over-week changes
  → Anthropic (Claude Haiku): Generate insight summary
  → Telegram (Coach/Client channel):
      "📊 YouTube Weekly Report — {client_name}

       Views: {views} ({delta}% vs last week)
       Watch Time: {hours}h ({delta}%)
       New Subs: +{subs}
       Top Video: {title} — {views} views

       {ai_insight}"
```

## YouTube Data API Setup

```
Requirements:
  - Google Cloud Console project with YouTube Data API v3 enabled
  - OAuth 2.0 credentials (for uploading on behalf of client)
  - YouTube Analytics API enabled (for metrics)
  - Scopes needed:
      youtube.upload
      youtube.readonly
      yt-analytics.readonly

n8n Credentials:
  - Google OAuth2 with YouTube scopes
  - Store per-client channel credentials in n8n
```

## Google Sheets Structure — YouTube Content Tab

| Column | Description |
|---|---|
| client_name | Client identifier |
| video_title | Video title |
| video_description | Full description |
| tags | Comma-separated tags |
| gdrive_file_id | Google Drive file ID |
| thumbnail_id | GDrive thumbnail file ID |
| status | Draft / Ready / Scheduled / Published |
| publish_time | Scheduled publish datetime |
| youtube_url | URL after publishing |
| views | Current view count (updated daily) |
| watch_time_min | Total watch time minutes |
| created_at | Row creation timestamp |

## Integrations
- YouTube Data API v3 (upload, manage videos)
- YouTube Analytics API (metrics, reporting)
- Google Drive (video + thumbnail storage)
- Google Sheets (content calendar + metrics tracking)
- Telegram Bot (notifications, VA commands)
- Anthropic Claude Haiku (weekly insight generation)

## Note
- YouTube API has a daily upload quota — max ~6 videos/day per project by default
- Request quota increase via Google Cloud Console if needed
- TikTok does NOT have a public upload API — must be done manually
