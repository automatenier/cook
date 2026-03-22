# Prompt 1: Video Analysis & Blueprint Extraction

Use this prompt with a multimodal AI (Gemini 1.5 Pro / GPT-4o) to extract a complete, tool-ready reconstruction plan from any viral video.

---

## The Prompt

**Task:** Act as a Senior Content Strategist and Video Editor. Analyze the attached video [or provided transcript] to create a **Unified Video Reconstruction Blueprint.**

**Formatting Requirement:** You MUST output the analysis in a Markdown table with these exact columns:
1. **Time (Est):** The timestamp range for each segment (e.g., 00:00 - 00:07).
2. **The Script (Original English):** The verbatim spoken words.
3. **Footage (The Camera):** A breakdown of A-Roll vs B-Roll, shot types (Medium, Close-up, Wide), and the specific action occurring.
4. **Graphics (The Overlay):** Instructions for the digital layer, including captions, headers, progress bars, and UI icons.

**Analysis Rules:**
- Identify scene cuts (segments should usually be 2-4 seconds long for high retention).
- Note the exact moment transitions or graphics appear.
- If the script is in a different language, translate it to English for this column but keep the pacing.

---

### Technical Summary
After the table, provide a **Technical Summary** with these 3 categories:
- **CapCut (Base Layer):** Instructions for cutting and layering the raw footage.
- **Remotion (Overlay Layer):** Instructions for the code-based graphics and text layers.
- **Audio (SFX Layer):** Specific timestamps for "Whoosh," "Ding," or background music shifts.

**Output Language:** English.

---

## Workflow Integration
1. **Analyze:** Upload your target video to an AI and paste the prompt above.
2. **Save:** Save the output as a `.md` file in your `01_HMN_INPUTS/Reels/` folder.
3. **Next Step:** Proceed to the **Repurpose Prompt** to swap the script for your own brand message.
