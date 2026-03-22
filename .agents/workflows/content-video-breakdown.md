# Workflow: Video Breakdown & Transcription

## Goal
To decompose a video into its constituent parts (visuals and audio) to allow for easy script rewriting and trend analysis.

---

## Steps

### 1. **NotebookLM Analysis**
- **Action:** Create a notebook and import the video URL or file.
- **Goal:** Extract a clean, high-accuracy transcript and a high-level narrative storyboard.
- **Command:** 
  ```bash
  py -3 -m notebooklm create "Video Title"
  py -3 -m notebooklm source add [NotebookID] "path/to/video.mp4"
  py -3 -m notebooklm ask "Extract the visual text and the full transcript."
  ```

### 2. **Visual Frame Extraction**
- **Action:** Use `ffmpeg` to detect scene changes and save frames as JPGs.
- **Goal:** Get "visual proof" of every shot change for the storyboard.
- **Command:**
  ```bash
  ffmpeg -i "video.mp4" -filter:v "select='gt(scene,0.4)',showinfo" -vsync vfr "Assets/frames/scene_%03d.jpg"
  ```

### 3. **Obsidian Canvas Generation**
- **Action:** Arrange the frames in a grid within a `.canvas` file.
- **Goal:** Rapid visual scanning of the video's pacing and shot types.

### 4. **Markdown Breakdown**
- **Action:** Pair each extracted frame with the corresponding section of the transcript in a single `.md` file.
- **Goal:** Create a "Copy-Paste Ready" document for scripting.

---

## Preferred Tooling
- **NotebookLM:** For the "Big Picture" and high-quality text extraction.
- **FFmpeg:** For the "Surgical" visual breakdown.
- **Obsidian:** The "Command Center" for review and drafting.
