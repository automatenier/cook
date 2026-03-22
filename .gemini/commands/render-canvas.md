# Command: /render-canvas

**Objective:** Convert an Obsidian Canvas visual storyboard into a finished video using the Spatial Timeline logic and Modal Cloud.

**Workflow:**
1. **Identify Input:** Path to the `.canvas` file (default: `PDCT_Real_Estate/C Storyboarding/Canvas Storyboard Template.canvas`).
2. **Fetch Hook:** Automatically pulls the latest hook from `Z Brainstorm\Production_Batch.md`.
3. **Execute Tool:** Runs the Modal renderer.
    ```bash
    py -3 -m modal run AI_Tools/content_canvas/content_render_full_canvas.py --canvas-file "{{canvas_file}}"
    ```
4. **Output:** Final video saved to `VLT_Content/04_HMN_OUTPUTS/Canvas_Renders/`.

**Parameters:**
- `canvas_file`: (Optional) Path to a specific canvas.
