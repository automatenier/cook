  

Update Todos

- [ ] 
    
    Create tools/create_google_sheets.py
    
- [ ] 
    
    Add gspread to requirements.txt
    
- [ ] 
    
    Add Google credentials to .env
    

Everything is set up. Here's how to run it:

```bash
# Install gspread (if not done yet)
pip install -r tools/requirements.txt

# Create the spreadsheet
python tools/create_google_sheets.py
```

**What happens:**

1. Script writes your Google credentials to `~/.config/gspread/credentials.json`
2. Browser opens → sign in with your Google account
3. Creates **"JO Consult - Data System"** with **9 tabs**:

|Tab|What it holds|
|---|---|
|`CRM_Leads`|Full pipeline (11 columns)|
|`Setter_KPIs`|Daily setter metrics|
|`Client_Ops`|Per-client status + phase|
|`Client_Checklist`|Deliverable checkboxes per client|
|`Content_Calendar`|All 150+ pieces/month|
|`Content_Performance`|Post metrics (views, saves, DM triggers)|
|`Team_EOD`|Daily reports for every team member|
|`Finance`|Invoice tracker|
|`Finance_Monthly`|Monthly revenue + margin summary|

4. Spreadsheet ID automatically saved to `.env` as `GOOGLE_SHEETS_CRM_ID`

After that, n8n reads this sheet ID from `.env` and syncs data to local JSON for Claude to query. 