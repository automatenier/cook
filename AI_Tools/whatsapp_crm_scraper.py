import sys
import time

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("[ERROR] Playwright is not installed. Please install it by running:")
    print("pip install playwright")
    print("playwright install chromium")
    sys.exit(1)

try:
    import pyperclip
except ImportError:
    print("[ERROR] pyperclip is not installed. Please install it by running:")
    print("pip install pyperclip")
    sys.exit(1)

SHEET_URL = "https://docs.google.com/spreadsheets/d/1vJn-5RMcIxZLZBFoSlQJpOwcA_BxXdb39XXY_X2Mos8"

def main():
    print("=" * 60)
    print("WhatsApp to CRM Scraper")
    print("=" * 60)

    with sync_playwright() as p:
        print("[1/5] Connecting to Chrome on port 9222...")
        try:
            # Connect to Chrome running in remote debugging mode
            browser = p.chromium.connect_over_cdp("http://localhost:9222")
            print("      Connected successfully.")
        except Exception as e:
            print("\n[!] COULD NOT CONNECT TO CHROME")
            print("Make sure you launched Chrome with the remote debugging port.")
            print("\nInstructions:")
            print("1. Completely Close Google Chrome.")
            print("2. Press Windows Key + R to open 'Run'.")
            print("3. Paste the following and press Enter:")
            print('   "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --remote-debugging-port=9222')
            print("4. Try running this script again.")
            sys.exit(1)

        contexts = browser.contexts
        if not contexts:
            print("No browser contexts found. Make sure Chrome is open.")
            sys.exit(1)
        
        default_context = contexts[0]
        
        wa_page = None
        sheet_page = None

        print("[2/5] Looking for WhatsApp Web and CRM Google Sheet tabs...")
        for page in default_context.pages:
            url = page.url
            if "web.whatsapp.com" in url:
                wa_page = page
            if SHEET_URL in url:
                sheet_page = page

        if not wa_page:
            print("\n[!] WhatsApp Web is not open in your Chrome tabs.")
            print("Please open web.whatsapp.com, open the specific chat you want to copy, and try again.")
            sys.exit(1)
            
        print("      WhatsApp Web found!")

        print("[3/5] Extracting messages from active WhatsApp chat...")
        wa_page.bring_to_front()
        time.sleep(1) # Extra buffer for UI rendering
        
        # WhatsApp represents each message as a row div
        message_elements = wa_page.locator('div[role="row"]').all()
        
        if not message_elements:            
            print("\n[!] No messages found.")
            print("Please make sure you have actively clicked on a chat so the messages are visible.")
            sys.exit(1)

        print(f"      Found {len(message_elements)} message rows. Processing the last 15 messages...")
        
        text_snippets = []
        for el in message_elements[-15:]:
            text = el.inner_text().strip()
            if text:
                # Replace newlines with a separator so the CRM row doesn't break
                text_snippets.append(text.replace('\n', ' | '))
                
        final_text = "  ||  ".join(text_snippets)
        
        if not final_text.strip():
            print("\n[!] Attempted extraction, but no text was found. This may happen if WhatsApp's layout updated.")
            sys.exit(1)
            
        # Copy to clipboard
        pyperclip.copy(final_text)
        print("      Extraction complete! The conversation has been copied to your clipboard.")

        print("[4/5] Navigating to Google Sheet CRM...")
        if not sheet_page:
            print("      CRM Google Sheet not open. Opening it in a new tab...")
            sheet_page = default_context.new_page()
            sheet_page.goto(SHEET_URL)
        else:
            print("      CRM Google Sheet already open. Switching to its tab...")
            sheet_page.bring_to_front()

        try:
            print("      Waiting for Google Sheets canvas to load...")
            sheet_page.wait_for_selector('canvas', timeout=15000)
            time.sleep(2) # Give it a brief moment to initialize the current cell selection
        except Exception:
            print("\n[!] Warning: Timed out waiting for Google Sheets to fully load. Will try to paste anyway.")

        print("[5/5] Pasting text into Google Sheet...")
        # Since Google Sheets UI differs based on active selection,
        # typing or pressing standard keys usually types directly into the active cell.
        
        try:
            # We don't press Ctrl+Down here because CRM data might have empty columns, 
            # and it's safer to just paste into whatever row the user had selected or first active cell.
            # But the user specifically asked for "paste in the CRM".
            # We will use Ctrl+V to paste the clipboard we just copied!
            sheet_page.keyboard.press("Control+v")
            print("\n✅ Successfully triggered the paste operation in your CRM!")
        except Exception as e:
            print(f"\n[!] Could not trigger automatic paste: {e}")
            print("But don't worry! The text is in your clipboard. You can press Ctrl+V yourself.")

        print("=" * 60)
        print("All Done!")

if __name__ == "__main__":
    main()
