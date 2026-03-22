# 🛠️ AI_Tools: The "Cook" Logic Engine
This folder is the brain of your automation. It contains the Python scripts that handle video rendering, posting, and CRM management.

## 🚀 Key Content Commands
You can trigger these directly via Gemini by using the forward slash `/` followed by the command name.

| Command | Purpose | Gemini Input |
| :--- | :--- | :--- |
| **`/download-reel`** | Downloads a reel from Instagram/TikTok/FB. | `/download-reel [URL]` |
| **`/posts`** | Posts a video to IG, FB, and YouTube. | `/posts [File] [Title] [Desc]` |
| **`/render-reel`** | Triggers the Remotion/Modal render process. | `/render-reel [Canvas/MD]` |
| **`/create-captions`** | Generates text overlays for your videos. | `/create-captions [Video]` |

## 📁 Folder Structure Breakdown:
- **`content_canvas/`**: New tools for turning Obsidian Canvas into video.
- **`google-workspace-cli/`**: Tools for syncing your Kanban to Google Calendar.
- **`media/`**: Heavy lifting for captions and audio processing.
- **`tests/`**: Safety checks to ensure scripts don't break.

## 💡 How to use:
Don't worry about running these manually in the terminal. Just tell Gemini:
> "Gemini, download this reel: [URL]" or "Gemini, render my Savasa storyboard."
