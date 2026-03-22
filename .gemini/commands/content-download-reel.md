# Command: /download-reel

**Objective:** Download a single reel or video from TikTok, Instagram, or Facebook using the new scraping logic.

**Workflow:**

1.  **Receive Input:** Provide a URL from TikTok, Instagram, or Facebook.
2.  **Execute Tool:** Run the `AI_Tools/content_download_reels_v2.py` script.
    ```bash
    py -3 AI_Tools/content_download_reels_v2.py "{{url}}"
    ```
3.  **Output:** The video will be saved to `VLT_Content\__VLT_OBSVAULT\01_HMN_INPUTS\Reels`.
4.  **Confirm:** Notify the user when the download is complete and provide the filename if possible.

**Supported Platforms:**
- TikTok
- Instagram
- Facebook / FB Watch
