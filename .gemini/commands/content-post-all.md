# Command: /posts

**Objective:** Post a video or reel to multiple platforms (YouTube, Instagram, and Facebook) simultaneously.

**Workflow:**

1.  **Receive Input:** Requires a video file path, a title, and a description.
2.  **Execute Tool:** Run the `AI_Tools/content_post_all.py` orchestrator script.
    ```bash
    py -3 AI_Tools/content_post_all.py --file "{{file}}" --title "{{title}}" --description "{{description}}"
    ```
3.  **Confirmation:** The script will provide a summary of successes and failures for each platform.
4.  **Note:** Threads and TikTok are not currently supported by this automation and may require manual posting.

**Required Parameters:**
- `file`: Path to the video file.
- `title`: The title of the post (used for YouTube and IG/FB captions).
- `description`: The caption or description for the post.

**Platforms Covered:**
- YouTube
- Instagram (Reels)
- Facebook (Page)
