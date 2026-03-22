# Supabase Live CRM Dashboard: Setup & Workflow Guide

This guide explains how to maintain your live cloud dashboard using Google Sheets as the Source of Truth, Supabase as the Realtime Engine, and GitHub Pages as the Hosting Layer.

---

## 🚀 Setup Checklist (One-Time)

### 1. Initialize the Database (Supabase)
1.  Go to your [Supabase SQL Editor](https://xmfkewjxjsrffvmlcsid.supabase.co/project/default/sql).
2.  Click **New Query** and run the following command to create your table and enable Realtime updates:

```sql
-- Create the leads table
create table leads (
  id uuid default gen_random_uuid() primary key,
  name text unique, -- Prevents duplicates
  status text,
  booked boolean,
  close_status text,
  context text,
  updated_at timestamp with time zone default now()
);

-- Enable Realtime for the table
alter publication supabase_realtime add table leads;
```

### 2. Enable Hosting (GitHub Pages)
1.  Push your changes to GitHub: `git add . && git commit -m "Setup cloud dashboard" && git push`.
2.  On GitHub.com, go to **Settings** > **Pages**.
3.  Set **Branch** to `main` and folder to `/(root)`. Click **Save**.
4.  Wait 60 seconds. Your dashboard will be live at: `https://[your-username].github.io/Cook/CRM_Vibe_Dashboard.html`.

---

## 🔄 Daily Workflow (Syncing Data)

Whenever you edit your **Google Sheet**, you must "push" those changes to the cloud.

### 1. Run the Sync Script
Open your terminal in the `Cook/` folder and run:
```powershell
py -3 AI_Tools/sync_crm_to_cloud.py
```

### 2. View the Live Updates
Open your GitHub Pages URL on any device (phone, tablet, laptop). 
*   **Realtime Magic:** You do **not** need to refresh the page. As soon as the script above finishes, the dashboard charts and tables will jump and update automatically.

---

## 🛠️ Troubleshooting

| Issue | Solution |
| :--- | :--- |
| **"Sync Error" on Dashboard** | Check if the Supabase URL and Anon Key in `CRM_Vibe_Dashboard.html` match your project settings. |
| **Data not updating** | Ensure the `leads` table in Supabase has "Realtime" enabled (Step 1.2 above). |
| **Script fails** | Ensure you are in the root `Cook/` directory so the script can find `.pass/service_account.json`. |

---

## 🔐 Credentials Location
All keys (Supabase URL, Secret Key, Anon Key) are stored securely in:
`Cook/.pass/A_PASS.md`
