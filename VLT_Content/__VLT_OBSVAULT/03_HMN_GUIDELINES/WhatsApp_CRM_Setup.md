# WhatsApp to CRM Automation Guide

To allow the AI script to copy your active WhatsApp Web messages directly from your browser, you must start Chrome in **Debug Mode**. This securely allows the local script to control your active Chrome profile without logging you out of your accounts.

### 1. Close Chrome Completely
You must fully exit Chrome. If it runs in the background, you can close it via the System Tray (bottom right of Windows) or task manager.

### 2. Launch Chrome with Debugging Port
1. Press `Win + R` to open the Windows "Run" dialog.
2. Paste the exact following command:
   ```cmd
   "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
   ```
3. Press **Enter**. Chrome will open normally with all your logged-in profiles.

### 3. Usage
Once Chrome is open:
1. Go to `web.whatsapp.com` and click on the chat conversation you want to copy.
2. Run the AI Script from your command line:
   ```cmd
   py -3 AI_Tools/whatsapp_crm_scraper.py
   ```
3. The script will:
   - Connect to Chrome perfectly securely.
   - Look at the visible messages in your WhatsApp window and copy them.
   - Bring up your CRM Google Sheet tab (or open it).
   - Automatically trigger a `Ctrl+V` to paste the context exactly where you are clicked!

> **Note:** If the script ever says "cannot connect to Chrome", just remember to completely close Chrome and re-open it using the `Win+R` command above!
