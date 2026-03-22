# Cook Tools Index
> **Agent lookup rule:** Grep this file before reading any workflow.
> Example: `grep -i "repurpose" AI_Tools/tools_index.md`

## `content_` — Content Production Tools

| Tool | Purpose | Invocation |
|------|---------|-----------|
| `content_analyze_viral_reel.py` | Convert a reel analysis (markdown or manual notes) into structured JSON for Remotion. | `py -3 AI_Tools/content_analyze_viral_reel.py` |
| `content_kanban_sync.py` | Sync Obsidian Kanban board ("Scheduled" lane) to Excel performance tracker. Auto-populates with title, platform, date; deduplicates by title. Creates `01 HMN__Command/00_CONTENT/Content_Performance_Tracker.xlsx` with Log, Summary, and Sync Log sheets. | `py -3 AI_Tools/content_kanban_sync.py` |
| `content_approve.py` | Content Approval — reads Content_Tracker.xlsx, moves Status=approved files from 06_REVIEW/[client]/ to 07_FINAL/[client]/[month]/, updates Final_Path and Approved_Date. | `py -3 AI_Tools/content_approve.py` |
| `content_batch_proof_images.py` | Reads Authority_Proof_Planner.csv and generates story images for every row with a Photo_Path filled in. | `py -3 AI_Tools/content_batch_proof_images.py` |
| `content_capture_idea.py` | Write a raw idea to Content/01_INBOX as a timestamped Markdown note. | `py -3 AI_Tools/content_capture_idea.py` |
| `content_extract_clips.py` | Extract repurposable clips from a long-form YouTube script. | `py -3 AI_Tools/content_extract_clips.py` |
| `content_figma_manager.py` | Figma Manager — Unified interface for Figma data extraction, image exports, and design tokens. | `py -3 AI_Tools/content_figma_manager.py` |
| `content_performance_tracker.py` | Content Performance Tracker Excel. | `py -3 AI_Tools/content_performance_tracker.py` |
| `content_query_footage.py` | Footage Library Query Tool. | `py -3 AI_Tools/content_query_footage.py` |
| `content_remotion_md_to_json.py` | Convert Remotion markdown script to JSON props. | `py -3 AI_Tools/content_remotion_md_to_json.py` |
| `content_render_brief.py` | Render Brief Generator. | `py -3 AI_Tools/content_render_brief.py` |
| `content_render_bridge.py` | Master render bridge — orchestrates Remotion render pipeline. | `py -3 AI_Tools/content_render_bridge.py` |
| `content_render_manager.py` | Render Manager — Unified interface for Remotion video rendering. | `py -3 AI_Tools/content_render_manager.py` |
| `content_repurpose.py` | Repurpose finished content into multiple platform formats using Claude. | `py -3 AI_Tools/content_repurpose.py` |
| `content_review_scripts.py` | Review and score drafted scripts before approval. | `py -3 AI_Tools/content_review_scripts.py` |
| `content_template_proof_image.py` | Generate a single proof/authority image from a template. | `py -3 AI_Tools/content_template_proof_image.py` |
| `content_tracker_setup.py` | One-time setup — creates Content/Content_Tracker.xlsx seeded with existing approved files. Run once only. | `py -3 AI_Tools/content_tracker_setup.py` |
| content_video_manager.py | Video Manager — Unified interface for video asset acquisition and processing. | `py -3 AI_Tools/content_video_manager.py` |
| `content_download_reels_v2.py` | Reel Downloader — TikTok, Instagram, and Facebook downloader using yt-dlp or fallback scrapers. | `py -3 AI_Tools/content_download_reels_v2.py` |
| `content_download_swipe.py` | Swipe Downloader — Downloads reels from Download Que.md and marks them as DONE. | `py -3 AI_Tools/tests/content_download_swipe.py` |

## `media/` — Specialized Media Processing

| Tool | Purpose | Invocation |
|------|---------|-----------|
| `create_captions.py` | Generate captions for videos. | `py -3 AI_Tools/media/create_captions.py` |
| `create_captions_transparent.py` | Generate transparent captions for video overlays. | `py -3 AI_Tools/media/create_captions_transparent.py` |
| `convert_whisper_to_remotion.py` | Convert Whisper transcript (JSON) to Remotion-compatible format. | `py -3 AI_Tools/media/convert_whisper_to_remotion.py` |

## `cook_` — Business Ops Tools

| Tool | Purpose | Invocation |
|------|---------|-----------|
| `cook_add_n8n_sheet.py` | Add a new sheet to the n8n tracking spreadsheet. | `py -3 AI_Tools/cook_add_n8n_sheet.py` |
| `cook_client_status.py` | Sprint Status Checker — shows today's agenda for all active clients. | `py -3 AI_Tools/cook_client_status.py` |
| `cook_crm_manager.py` | CRM Manager — Unified interface for JO Consult CRM & Tracking infrastructure. | `py -3 AI_Tools/cook_crm_manager.py` |
| `cook_csv_to_excel.py` | Convert CSV files to formatted Excel workbooks. | `py -3 AI_Tools/cook_csv_to_excel.py` |
| `cook_extend_kpi_tracker.py` | Extend KPI tracker with new metrics or clients. | `py -3 AI_Tools/cook_extend_kpi_tracker.py` |
| `cook_generate_sprint_sop.py` | Generate the 14-Day Client Sprint SOP as a formatted Excel file. | `py -3 AI_Tools/cook_generate_sprint_sop.py` |
| `cook_lead_magnet_manager.py` | Lead Magnet Manager — Unified interface for Lead Magnet production and tracking. | `py -3 AI_Tools/cook_lead_magnet_manager.py` |
| `cook_logger.py` | Append-only logging utility for WAT agent execution metrics. | `py -3 AI_Tools/cook_logger.py` |
| `cook_migrate_to_sheets.py` | Migrate Data/JO_Consult_Dashboard.xlsx → Google Sheets (exact replica). | `py -3 AI_Tools/cook_migrate_to_sheets.py` |
| `cook_modal_app.py` | Cook Tools — Modal cloud deployment (repurpose + web UI). Redeploy: `PYTHONIOENCODING=utf-8 py -3 -m modal deploy AI_Tools/cook_modal_app.py` | `py -3 AI_Tools/cook_modal_app.py` |
| `cook_offer_agent.py` | Offer Agent — Generate high-ticket fitness offer sheets using Claude. | `py -3 AI_Tools/cook_offer_agent.py` |
| `cook_ops_manager.py` | Operations Manager — Unified interface for dashboards, KPIs, and terminal monitoring. | `py -3 AI_Tools/cook_ops_manager.py` |
| `cook_pipeline.py` | Run multiple Cook tools in sequence, passing outputs between steps. | `py -3 AI_Tools/cook_pipeline.py .tmp/pipeline_examples/youtube_to_repurpose.yaml` |
| `cook_pipeline_manager.py` | Pipeline Manager — Unified interface for lead logging, revenue tracking, and CRM summaries. | `py -3 AI_Tools/cook_pipeline_manager.py` |
| `cook_read_excel_summary.py` | Read and summarize an Excel file for quick inspection. | `py -3 AI_Tools/cook_read_excel_summary.py` |
| `cook_roi_simulation.py` | ROI Simulation Generator — Create professional property investment simulations. | `py -3 AI_Tools/cook_roi_simulation.py` |
| `cook_setter_cash_dashboard.py` | Setter & Cash Dashboard — Excel Infrastructure. | `py -3 AI_Tools/cook_setter_cash_dashboard.py` |
| `cook_sync_jocons_calendar.py` | Sync JO Consult sprint schedule to Google Calendar. | `py -3 AI_Tools/cook_sync_jocons_calendar.py` |
| `cook_kanban_gcal_sync.py` | Parse 00_KANBAN_COMMAND.md and push tasks to Google Calendar. HMN_Meetings → individual timed events. HMN_Main → individual events stacked from 12:00. HMN_Content + HMN_OBS → combined deep work block per day (min 4hr). Requires `credentials.json` in Cook/ root for first-run OAuth. | `py -3 AI_Tools/cook_kanban_gcal_sync.py` / `--dry-run` / `--clear` |
| `cook_kanban_prefix_sync.py` | Sync Obsidian Kanban board prefixes in Command.md based on lane. 🤙 Meetings -> [MEET], :LiBrain: Deepwork -> [DEEP], 🟧 Claude 1/2 -> [CLAUDE], :LiTerminalSquare: Gem 1/2/3/4 -> [GEM]. | `py -3 AI_Tools/cook_kanban_prefix_sync.py` |
| `cook_web_fetch.py` | Fetch a URL and return clean text (HTML stripped, noise removed). | `py -3 AI_Tools/cook_web_fetch.py` |

## `re_` — Real Estate Tools

| Tool | Purpose | Invocation |
|------|---------|-----------|
| `re_crm_setup.py` | One-time setup — creates `01 HMN__Command/11_Real_Estate/Dash/RE_CRM.xlsx` with Pipeline, Revenue_Log, and Lead_Source sheets. Run once only. | `py -3 AI_Tools/re_crm_setup.py` |

## `vault_` — Knowledge Capture Tools

| Tool | Purpose | Invocation |
|------|---------|-----------|
| `vault_youtube_note.py` | Fetch a YouTube transcript, summarize key insights with Claude Haiku, save to vault. | `py -3 AI_Tools/vault_youtube_note.py https://youtu.be/VIDEO_ID` |
