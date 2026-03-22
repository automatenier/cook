# Content Workflow SOP (Master)
**Framework:** WAT (Workflows, Agents, Tools)  
**Goal:** High-fidelity content production with AI-led orchestration and automated distribution.

---

## 1. Architecture & Routing
The system separates creative reasoning from deterministic execution.

| Task Type | Agent | Role |
| :--- | :--- | :--- |
| **Strategy & Writing** | Claude (`/content`) | Scripts, repurposing, offer sheets, and high-level strategy. |
| **Execution & Tools** | Gemini (`/download`) | Downloading, posting, file management, and tool triggers. |
| **Render Engine** | Remotion + Modal | Hybrid rendering (Local for tests, Modal Cloud for batches). |

---

## 2. Phase 1: Input & Capture (The Inbox)
Raw ideas and external inspiration are captured into the **Creative Hub**.

- **Reel/Video Download:** `py -3 AI_Tools/content_download_reels_v2.py "{{url}}"`
- **Idea Capture:** `py -3 AI_Tools/content_capture_idea.py` (Converts raw text/voice to Markdown).
- **YouTube Transcripts:** `py -3 AI_Tools/vault_youtube_note.py` (Creates summaries and swipe files).
- **Storage:** All raw inputs land in `VLT_Content/__VLT_OBSVAULT/01_HMN_INPUTS/`.

---

## 3. Phase 2: Deconstruction & Analysis
Surgical breakdown of viral content to understand "The Hook" and "The Retainers."

1. **Transcript Extraction:** High-accuracy transcripts generated via NotebookLM.
2. **Visual Breakdown:** `py -3 AI_Tools/content_video_breakdown.py` extracts frames and analyzes pacing via FFmpeg.
3. **Synthesis:** Findings are stored as Obsidian Canvas or Markdown notes for the Creative Director agent.

---

## 4. Phase 3: Creative & Writing
Turning insights into scripts using client-specific brand guidelines.

- **Guidelines:** Sourced from `VLT_Content/__VLT_OBSVAULT/03_HMN_GUIDELINES/`.
- **Drafting:** Claude drafts scripts in `VLT_Content/__VLT_OBSVAULT/02_HMN_AIREVIEW/`.
- **Repurposing:** `py -3 AI_Tools/content_repurpose.py` creates variants for Reels, Stories, and YT Shorts.
- **Review:** `py -3 AI_Tools/content_review_scripts.py` scores drafts against brand KPIs.

---

## 5. Phase 4: Production & Rendering
High-end UI animation and video editing using code-as-video.

- **Workflow:** `04_Video_Editor` agent orchestrates Remotion templates.
- **Execution:**
    - **One-off test:** Local render for speed.
    - **Batch (2+ videos):** `py -3 AI_Tools/content_render_manager.py --modal` (Offloads to Cloud).
- **Output:** Staged in `VLT_Content/04_HMN_OUTPUTS/`.

---

## 6. Phase 5: Tracking & Approval
The Command Center manages the pipeline via Obsidian Kanban.

- **Command Center:** `VLT_Content/01 HMN_Command/CONTENT SYSTEM.md`.
- **Sync:** `py -3 AI_Tools/content_kanban_sync.py` updates the Excel Performance Tracker.
- **Approval:** `py -3 AI_Tools/content_approve.py` moves approved files to `VLT_Content/05_VLT_FINAL/` and triggers the distribution phase.

---

## 7. Phase 6: Distribution (Post All)
Multi-platform posting with one command.

- **Command:** `py -3 AI_Tools/content_post_all.py --file "{{file}}" --title "{{title}}" --description "{{description}}"`
- **Platforms:** YouTube, Instagram, Facebook, and Threads.
- **Manual Note:** TikTok requires manual upload (reminder triggered by script).

---

## 8. Automation Tool Index (Content)

| Tool | Purpose |
| :--- | :--- |
| `content_download_reels_v2.py` | Downloads from IG/TikTok/FB to `01_HMN_INPUTS`. |
| `content_post_all.py` | Posts to YouTube, Meta, and Threads. |
| `content_render_manager.py` | Orchestrates Remotion renders (Local/Modal). |
| `content_kanban_sync.py` | Syncs Obsidian cards to Performance Tracker. |
| `content_repurpose.py` | Generates platform-specific copy variants. |
| `content_analyze_viral_reel.py` | High-level viral analysis for swipe files. |
