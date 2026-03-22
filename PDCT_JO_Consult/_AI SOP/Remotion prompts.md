# SOP: Video Reconstruction Execution

Use this instruction set to turn a **Unified Content Blueprint** (like `Untitled.md`) into a finished video using the Bedah Digital toolstack.

---

## The Directive (Copy & Paste this to an Agent)

**Task:** Act as a Senior Video Editor and Automation Engineer. Recreate the video blueprint from `[Path to your Blueprint.md]` using the following logic and resources.

### 1. Resource Mapping
- **The Blueprint:** Use the `Unified Content Table` in the blueprint file to map the script, footage, and graphics.
- **The Visuals:**
    - **A-Roll:** Identify the talking-head clips from the `GDrive/[Client]/A-Roll/` folder that match the script.
    - **B-Roll:** Match the B-Roll descriptions in the `Footage` column to the appropriate clips in the `GDrive/[Client]/B-Roll/` library.
- **The Graphics:** Use the `Remotion JSON Blueprint` section in the blueprint file as the data source for the overlay.

### 2. Automation Execution
- **Step A (JSON Generation):** Parse the `Remotion JSON Blueprint` from the blueprint file.
- **Step B (Render):** Execute the Remotion render tool:
    ```bash
    py -3 AI_Tools/content_remotion_md_to_json.py --input "[Path to Blueprint]"
    py -3 AI_Tools/content_render_manager.py --composition "reproduction-video"
    ```
- **Step C (Assembly):** Import the raw footage and the rendered transparent overlay into the editing environment (CapCut/Remotion).

### 3. Editorial Standards (Mimicking the Style)
- **Pacing:** Align all footage cuts exactly to the `Time (Est)` column (scene changes every 2-4 seconds).
- **Audio Alignment:** Place a "Whoosh" SFX on every transition identified in the `Technical Summary`.
- **Text Sync:** Ensure word-by-word captions are perfectly synced to the audio waveform.

### 4. Output Goal
Deliver a high-retention, brand-aligned video that replicates the visual rhythm and narrative architecture of the original viral source.

---

## When to use this SOP:
1.  **After** you have run the `Prompt.md` to analyze a video and create a blueprint.
2.  **After** you have repurposed the script for your brand in that blueprint.
3.  **When** you are ready to start the technical production phase.
