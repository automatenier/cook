---
tags:
  - automation
---
# Facebook & Instagram Auto-Posting — HTS Agency

> Automates content publishing to Facebook Pages and Instagram Business accounts via Meta Graph API.

---

## Purpose
- Auto-publish reels, posts, and stories to client IG and FB accounts
- Coordinate with content calendar in Google Sheets
- Reduce manual posting work — VA just marks "Ready" in sheet

---

## API Setup

```
Requirements:
  - Meta Developer App (developers.facebook.com)
  - Facebook Graph API v19+ (or latest)
  - Permissions needed:
      pages_manage_posts (FB Page posting)
      pages_read_engagement (FB metrics)
      instagram_basic
      instagram_content_publish (IG posting)
      instagram_manage_insights (IG metrics)
  - Long-lived Page Access Token (60-day, auto-refresh via n8n)
  - Instagram Business Account linked to Facebook Page
  - Media must be hosted on public URL (GDrive public link or cloud storage)
```

---

## Flow — Auto-Publish Instagram Reel

```
Trigger: Google Sheets row updated (status = "Ready" AND platform includes "IG")

  → Google Drive: Get video file → generate public URL
      (or upload to cloud storage for public access)
  → HTTP Request (Meta Graph API):
      POST /{ig-user-id}/media
      {
        media_type: "REELS",
        video_url: "{public_video_url}",
        caption: "{caption_from_sheet}",
        share_to_feed: true
      }
  → Wait: 30 seconds (Meta needs time to process video)
  → HTTP Request: Check container status
      GET /{creation_id}?fields=status_code
  → IF status == "FINISHED":
      → HTTP Request: Publish
          POST /{ig-user-id}/media_publish
          { creation_id: "{creation_id}" }
      → Google Sheets: Update status = "Published", add IG URL
      → Telegram: "✅ IG Reel published: {caption_preview}..."
  → IF status == "ERROR":
      → Telegram: "❌ IG Reel failed: {error_message}"
      → Google Sheets: Update status = "Failed"
```

## Flow — Auto-Publish Instagram Carousel

```
Trigger: Google Sheets (status = "Ready" AND type = "Carousel")

  → Google Drive: Get all images (up to 10)
  → FOR EACH image:
      → HTTP Request: Create item container
          POST /{ig-user-id}/media
          { image_url: "{public_url}", is_carousel_item: true }
  → HTTP Request: Create carousel container
      POST /{ig-user-id}/media
      { media_type: "CAROUSEL", children: [container_ids], caption: "{caption}" }
  → HTTP Request: Publish carousel
  → Google Sheets + Telegram: Update + notify
```

## Flow — Auto-Publish Facebook Post

```
Trigger: Google Sheets (status = "Ready" AND platform includes "FB")

  → IF type == "Video/Reel":
      → HTTP Request:
          POST /{page-id}/videos
          { file_url: "{public_url}", description: "{caption}" }
  → IF type == "Image":
      → HTTP Request:
          POST /{page-id}/photos
          { url: "{public_url}", message: "{caption}" }
  → IF type == "Text Only":
      → HTTP Request:
          POST /{page-id}/feed
          { message: "{caption}" }
  → Google Sheets: Update status
  → Telegram: Notification
```

## Flow — Scheduled Publishing

```
Cron (every 30 min)
  → Google Sheets: Find rows with status = "Scheduled" AND publish_time <= now
  → FOR EACH:
      → Route to correct publish flow (IG Reel / IG Carousel / FB Post)
  → Log results
```

## Flow — Metrics Pull (Daily)

```
Cron (09:00 WIB daily)
  → HTTP Request (IG Insights):
      GET /{ig-user-id}/insights
      metrics: impressions, reach, follower_count, profile_views
      period: day
  → HTTP Request (Per post — last 7 days):
      GET /{media-id}/insights
      metrics: engagement, impressions, reach, saved, shares
  → HTTP Request (FB Page Insights):
      GET /{page-id}/insights
      metrics: page_impressions, page_engaged_users, page_fans
  → Google Sheets: Write to "Social Metrics" tab
  → IF: Any post hit engagement milestone:
      → Telegram: Alert
```

## Flow — Weekly Social Report

```
Cron (Monday 09:30 WIB)
  → Google Sheets: Pull last 7 days metrics
  → Code Node: Calculate WoW changes
  → Anthropic (Claude Haiku): Generate insights
  → Telegram:
      "📊 Social Media Weekly — {client_name}

       INSTAGRAM
       Followers: {count} (+{new})
       Reach: {reach} ({delta}%)
       Engagement Rate: {rate}%
       Top Post: {caption_preview} — {likes} likes, {comments} comments

       FACEBOOK
       Page Likes: {count} (+{new})
       Reach: {reach} ({delta}%)
       Top Post: {caption_preview} — {engagements} engagements

       {ai_insight}"
```

## Google Sheets Structure — Content Calendar Tab

| Column | Description |
|---|---|
| client_name | Client identifier |
| platform | IG, FB, or Both |
| content_type | Reel, Carousel, Image, Text |
| caption | Full caption with hashtags |
| gdrive_file_ids | Comma-separated GDrive file IDs |
| status | Draft / Ready / Scheduled / Published / Failed |
| publish_time | Scheduled publish datetime |
| ig_media_id | IG media ID after publish |
| fb_post_id | FB post ID after publish |
| impressions | Updated daily |
| engagement | Updated daily |
| created_at | Timestamp |

## Token Refresh Flow

```
Cron (every 50 days — before 60-day expiry)
  → HTTP Request:
      GET /oauth/access_token
      ?grant_type=fb_exchange_token
      &client_id={app_id}
      &client_secret={app_secret}
      &fb_exchange_token={current_token}
  → n8n Credentials: Update stored token
  → Telegram: "🔑 Meta API token refreshed successfully"
```

## Important Notes
- **Instagram Reels**: Video must be 3-90 seconds, MP4, H.264, max 1GB
- **Carousel**: 2-10 images, all same aspect ratio recommended
- **Rate limits**: 25 API calls per user per hour for content publishing
- **TikTok**: No public upload API — must be done manually (as noted by Jordan)
- **Threads**: Uses separate Threads API (threads.net) — can be added later

## Integrations
- Meta Graph API (Facebook + Instagram publishing & insights)
- Google Drive (media storage)
- Google Sheets (content calendar + metrics)
- Telegram Bot (notifications, VA commands)
- Anthropic Claude Haiku (weekly insights)
