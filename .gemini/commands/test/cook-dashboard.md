Open the Cook Agent Terminal Dashboard to monitor real-time agent progress.

1. Ensure Python 3 is installed (`py -3`).
2. Run the dashboard script:
   ```bash
   py -3 AI_Tools/terminal_dashboard.py
   ```

The dashboard will:
- Refresh every 5 seconds.
- Show the most recent agent activities.
- Highlight **PENDING** tasks that need your confirmation.
- Show **SUCCESS** for finished tasks and **ERROR** for failures.
