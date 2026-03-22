# CRM Supabase Sync Guide

## 🔗 Live Links
- **Google Sheet (Source):** [SAVASA CRM Sheet](https://docs.google.com/spreadsheets/d/1vJn-5RMcIxZLZBFoSlQJpOwcA_BxXdb39XXY_X2Mos8/)
- **Live Dashboard:** [automatenier.github.io/cook/](https://automatenier.github.io/cook/)

## 🔄 How to Sync
The dashboard updates in real-time once the data is in Supabase. To get data from the Google Sheet into Supabase:

### Option A: Automatic (Hourly)
- The system syncs automatically at the **start of every hour** (e.g., 4:00 PM, 5:00 PM).

### Option B: Manual (Immediate)
1. Go to GitHub Repository: `https://github.com/automatenier/cook`
2. Click **Actions** tab.
3. Select **"CRM Cloud Sync"** from the left sidebar.
4. Click **Run workflow** -> **Run workflow (green button)**.

## ⚠️ Critical Rules
1. **Column Headers:** Do not rename headers in the "WA" or "LKDN" tabs (especially `3-Username`, `5-Status`, `9--Booked`).
2. **Duplicate Names:** The sync deduplicates by `3-Username`. If a name exists in both WA and LKDN, it will only count as one entry in the dashboard.
3. **Source Column:** Note that the current Supabase schema does not support a `source` column, so all leads are merged into a single table.
