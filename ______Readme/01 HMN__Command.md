# 🕹️ 01_HMN__Command: The Main Cockpit
This is where you track your whole business. It contains your Kanban boards, schedules, and trackers.

## 🚀 Key Commands for this Folder

| Command | Action | Goal |
| :--- | :--- | :--- |
| **`/next`** | Triggers `cook_client_status.py` | Shows you exactly what you need to do TODAY. |
| **`/sync-calendar`** | Triggers `cook_kanban_gcal_sync.py` | Pushes your Obsidian tasks to Google Calendar. |
| **`/crm-summary`** | Triggers `cook_pipeline_manager.py` | Shows you a summary of your lead pipeline. |

## 📁 Folder Structure Breakdown:
- **`00_CONTENT/`**: Trackers for content performance across all brands.
- **`Dash/`**: Excel Dashboards for JO Consult and Real Estate.
- **`Kanban/`**: Your central task-management boards.

## 💡 How to use:
Start your day in the **01_HMN__Command** folder. Tell Gemini:
> "Gemini, what's next?" or "Gemini, sync my tasks to Google Calendar."
