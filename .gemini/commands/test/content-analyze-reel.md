# Command: /analyze_reel

**Objective:** To process a markdown analysis of a viral reel, convert it to structured JSON, and add it to the swipe file.

**Workflow:**

1.  **Identify Input:** The user must provide the path to a markdown file (`.md`) containing the reel analysis.
2.  **Execute Tool:** Run the `AI_Tools/content_analyze_viral_reel.py` script, passing the file path as the input argument.
    ```bash
    py -3 AI_Tools/content_analyze_viral_reel.py --input "<path_to_analysis_file.md>"
    ```
3.  **Process Output:** The script will return a structured JSON object.
4.  **Store Result:** Save the JSON output to `VLT_Content/01_HMN_INPUTS/Swipe Files/` as a new file or append to the index.
5.  **Confirm Completion:** Report back to the user that the analysis is complete and the swipe file has been updated.
