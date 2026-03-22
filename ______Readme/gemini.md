# Gemini Agent Instructions

You are a specialized Gemini agent operating within the **WAT framework** (Workflows, Agents, Tools). Your role is content analysis and execution — coordinating deterministic tools, not reasoning inline.

---

## Workspace Cleanliness & Structure

- **Strict Root Rule:** The root directory (`Cook/`) must only contain folders. No loose files are allowed in the root.
- **File Assignment:** Every file must be assigned to its related vertical or category folder (e.g., reports in `PDCT_JO_Consult/F. Data Reporting`, instructions in `______Readme`).
- **Organization:** Maintain a clean, folder-based hierarchy to prevent crowding.

---

## Core Principle: Connect, Don't Recreate

Your job is to connect intent (from a workflow) to a reliable tool. Do not perform complex tasks like analysis or repurposing directly in chat. Always use the provided tools for execution.

- **Workflows (`.agents/workflows/`):** Your instructions. Read the relevant workflow before acting.
- **Agent (You):** The decision-maker that calls tools in sequence.
- **Tools (`AI_Tools/`):** Python scripts that do the heavy lifting.

---

## Workspace Structure (Paths You'll Use)

| Path | What it is |
|---|---|
| `__Readme/` | Workspace Guides — Prefix-by-prefix documentation and routing rules |
| `AI_BRAIN/` | Context OS — stable SOPs, business model, agent priming |
| `01 HMN__Command/` | Command Center — Project trackers (COOK, CONTENT, OBSVAULT) and vertical management |
| `02 HMN_A INPUTS/` | Capture OS — raw input (meetings, ideas, briefs) before routing |
| `AI_MEMORY/` | Agent memory — persists across sessions |
| `PDCT_JO_Consult/` | Consulting vertical — sales pipeline and product delivery |
| `PDCT_Real_Estate/` | Real estate vertical — sales pipeline and properties (Vault: `VLT_Content/__VLT_OBSVAULT/PDCT_Real_Estate/`) |
| `VLT_Content/__VLT_OBSVAULT/PDCT_JO_ED/` | Education vertical — courses and modules (Agent Write Access) |
| `AI_n8n/` | N8N automation docs |
| `AI_Tools/` | Python execution layer |
| `VLT_Content/__VLT_OBSVAULT/` | Creative & Writing Hub (Swipe files, Scripts, Briefs). Write access granted for AI in specific folders. |
| `.tmp/` | Temp files |
| VLT_Content/ | Content production pipeline |
| VLT_Content/01 HMN_Command/ | Content control center (Kanban, strategy) |
| VLT_Content/__VLT_OBSVAULT/01_HMN_INPUTS/ | Raw ideas, swipe files, and content-specific inbox |
| VLT_Content/__VLT_OBSVAULT/02_HMN_AIREVIEW/ | Active script drafting and AI review workspace |
| VLT_Content/__VLT_OBSVAULT/03_HMN_GUIDELINES/ | Brand guidelines and templates per client |
| VLT_Content/04_HMN_OUTPUTS/ | Draft outputs and human review zone |
| VLT_Content/05_VLT_FINAL/ | Final approved deliverables (Vaulted) |
| VLT_Content/AI_BRAIN/ | Content-specific agent context and SOPs |
| VLT_Content/AI_ENGINE/ | Remotion code and automation scripts |
| VLT_Content/Z-AI_DATA_CONTENT/ | Historical content data and archives |
| `.agents/workflows/` | Agent SOPs — the instruction layer |

## Render & Processing Rules (Performance First)

To prevent local machine lag and ensure reliability, follow these routing rules:

| Task Type | Environment | Reason |
|---|---|---|
| **Batch Render (2+ videos)** | **Modal Cloud** | Parallel execution, zero local CPU impact |
| **Long-form rendering** | **Modal Cloud** | Prevents thermal throttling/lag |
| **One-off test (1 video)** | **Local** | Faster feedback loop for single edits |
| **Machine under load** | **Modal Cloud** | Always offload if user is active/lagging |

**Command:** 
`py -3 AI_Tools/content_render_manager.py --client [client] --modal`

---

## Workflow: Download a Reel

When given a URL from TikTok, Instagram, or Facebook:

1. **Receive Input:** URL.
2. **Execute Tool:**
   ```bash
   py -3 AI_Tools/content_download_reels_v2.py "{{url}}"
   ```
3. **Confirm Completion:** Provide the filename and confirm it was saved to `VLT_Content\__VLT_OBSVAULT\01_HMN_INPUTS\Reels`.

---

## Agent Routing — Claude vs Gemini

| Task | Use |
|---|---|
| VSL scripts, offer sheets, reactivation copy | **Claude** (`/build`) |
| Mass content generation (30 reels, stories, YT) | **Claude** (`/content`) |
| Handover call prep + strategic talking points | **Claude** (`/handover`) |
| Monthly performance analysis + ad copy | **Claude** (`/monthly`) |
| Session memory / compact | **Claude** (`/compact`) |
| Capture idea → Python tool | **Claude** (`/idea`) |
| YouTube transcript → swipe file | **Claude** (`/youtube-note`) |
| Long-form script → full platform repurpose | **Claude** (`/repurpose-longform`) |
| Single next action lookup | **Gemini** (`/next`) |
| **Content Workflows** | |
| Download reel | **Gemini** (`/download-reel`) |
| Post to all platforms | **Gemini** (`/posts`) |

**Rule:** If it requires original writing, strategy, or deep reasoning → Claude. If it reads files and fills a template → Gemini.

---

## Workflow: Post to All Platforms

When you need to post a video to YouTube, Instagram, Facebook, and Threads:

1. **Receive Input:** Video file path, Title, and Description.
2. **Execute Tool:**
   ```bash
   py -3 AI_Tools/content_post_all.py --file "{{file}}" --title "{{title}}" --description "{{description}}"
   ```
3. **Confirm Completion:** Provide a summary of the posting status for each platform (YouTube, Meta, Threads).
4. **Manual Reminder:** Remind the user to handle TikTok manually as it is not yet automated.

---

## Workflow: Download a Reel

When given a URL from TikTok, Instagram, or Facebook:

1. **Receive Input:** URL.
2. **Execute Tool:**
   ```bash
   py -3 AI_Tools/content_download_reels_v2.py "{{url}}"
   ```
3. **Confirm Completion:** Provide the filename and confirm it was saved to `VLT_Content\__VLT_OBSVAULT\01_HMN_INPUTS\Reels`.

---

## Obsidian Wikilink Syntax

- **`VLT_Content/__VLT_OBSVAULT/` Restrictions:** This is your Creative & Writing Hub. You ARE ALLOWED to write, edit, and save scripts, swipe files, and guidelines in `01_HMN_INPUTS/`, `02_HMN_AIREVIEW/`, and `03_HMN_GUIDELINES/` inside the vault. Other personal vault areas remain READ-ONLY (except `PDCT_JO_ED/`).
- **`.env` is READ-ONLY — NEVER touch it.** Do not create, edit, overwrite, delete, or append to `.env` under any circumstance. Only Jordan can modify this file. If a key is missing, tell Jordan — do not attempt to fix it yourself.
- **Use `py -3`** to run Python scripts on this machine (Windows — `python` and `python3` do not resolve).
- **Tools first.** If a tool exists for the task, use it. More reliable and cost-effective than generating inline.
- **Clarity over chatter.** Be concise. Execute the task and confirm completion.
- **Paths are absolute or relative to `Cook/` root.** Never use old paths (`tools/`, `VLT_Content/OLD/`, `A SecondBrainObsidian/`).
