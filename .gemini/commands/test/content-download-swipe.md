# Command: /download-swipe

**Objective:** Automatically download all social media reels from the Social Swipe "Download Que" and mark them as DONE in the source markdown file.

**Workflow:**

1.  **Locate Source:** Identify the download queue at `VLT_Content\__VLT_OBSVAULT\PDCT_JO_Consult\Social Swipe\Download Que.md`.
2.  **Execute Tool:** Run the `AI_Tools/content_download_swipe.py` script.
    ```bash
    py -3 AI_Tools/content_download_swipe.py
    ```
3.  **Process:**
    -   The script extracts URLs from the first column of the markdown table.
    -   It skips any rows already marked as "DONE" in the second column.
    -   It downloads each reel to `VLT_Content\__VLT_OBSVAULT\PDCT_JO_Consult\Social Swipe\Social Media Format\Reels`.
    -   Upon successful download, it updates the markdown row by adding "DONE" to the second column.
4.  **Confirm Completion:** Notify the user how many reels were processed and that the queue file has been updated.
