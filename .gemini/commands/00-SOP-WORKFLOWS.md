# Command: /00-SOP-WORKFLOWS

**Objective:** Provide a launchpad and summary of all "Cook" Content Workflows.

---

## 🚀 Active Workflows

### 🎬 1. Visual Storyboarding (Canvas)
You design the video visually in Obsidian Canvas; I render it exactly as you laid it out.
**Run Command:** `/render-canvas`

### 🧪 2. Bulk Hook A/B Testing (Production Batch)
Test multiple text hooks on one video for performance.
**Run Command:**
```powershell
py -3 -m modal run AI_Tools/modal_hook_renderer.py --hooks-file "Z Brainstorm\Production_Batch.md"
```

### 📤 3. Post to All Platforms
Once a render is done, post it to YouTube, Instagram, and Facebook.
**Run Command:** `/posts`

### 🧹 4. Maintain Workspace Cleanliness
Ensure the root directory stays clean and folder-only.
**Run Command:** `/clean-root`

---

## 📁 Key Folder Guides
Use the READMEs in `______Readme/` for deeper documentation:
- **`01 HMN__Command.md`** (Management)
- **`PDCT_Real_Estate.md`** (Real Estate Brand)
- **`AI_Tools.md`** (Logic Engine)
- **`.gemini.md`** (AI Config)
