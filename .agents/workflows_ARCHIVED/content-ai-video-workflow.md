---
description: Agent workflow for high-end AI UI animation using Nano Banana Pro and Veo 3.1.
---

# Workflow: AI Video UI Animation

When user asks to `/ai-video-workflow` or implement the high-end UI animation process:

1. **Asset Generation (Nano Banana Pro)**:
   - Use a "Reference Image" (e.g., a shoe card or UI element).
   - Prompt Nano Banana Pro to break the design into "layers" or swap products while keeping the UI style identical.
   - Goal: High-fidelity text and crisp UI elements.

2. **Animation (Veo 3.1)**:
   - Take the assets from Step 1.
   - Prompt Veo 3.1 with: "Create a smooth UI style animation for this design."
   - Goal: Let the AI handle physics and motion (sliding cards, pulsing buttons).

3. **Post-Production (CapCut)**:
   - Bring the generated clip into CapCut.
   - Apply **Speed Ramping**: Fast at the start, slow at the end (ease-out effect).
   - Goal: Make the motion feel snappy and professional ("premium" feel).

## Execution Notes
- These models (Nano Banana Pro and Veo 3.1) are currently accessed via InVideo or similar hosted platforms.
- If automated tools become available in `AI_Tools/`, update this workflow to include script calls.
