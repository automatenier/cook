import time
import subprocess
import requests
import os
import json
import csv
from datetime import datetime, date
from pathlib import Path

# --- CONFIGURATION ---
GEMINI_BOT_TOKEN = os.getenv("GEMINI_BOT_TOKEN") 
API_URL = f"https://api.telegram.org/bot{GEMINI_BOT_TOKEN}/"

# Paths
ROOT = Path(__file__).resolve().parent.parent
LEAD_LOG = ROOT / "___Data" / "A JOCONS" / "lead_attribution.csv"
STATE_FILE = ROOT / ".tmp" / "gemini_remote_state.json"

# --- HELPERS ---
def send_message(chat_id, text):
    try:
        url = API_URL + "sendMessage"
        payload = {"chat_id": chat_id, "text": text}
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print(f"Error sending message: {response.text}")
        return response.json() if response.status_code == 200 else None
    except Exception as e:
        print(f"Error sending message: {e}")
        return None

def update_message(chat_id, message_id, text):
    try:
        url = API_URL + "editMessageText"
        payload = {"chat_id": chat_id, "message_id": message_id, "text": text}
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print(f"Error editing message: {response.text}")
    except Exception as e:
        print(f"Error editing message: {e}")

def get_updates(offset=None):
    try:
        url = API_URL + "getUpdates"
        params = {"timeout": 30, "offset": offset}
        response = requests.get(url, params=params)
        return response.json()
    except Exception as e:
        print(f"Error getting updates: {e}")
        return None

def run_gemini_command(prompt, chat_id=None, msg_id=None):
    """Executes the gemini cli command with the prompt, optimized for speed and reliability."""
    try:
        # Using the absolute path to gemini.cmd for Windows stability
        gemini_path = r"C:\Users\natha\AppData\Roaming\npm\gemini.cmd"
        
        # -p: Prompt (non-interactive)
        # -y: Auto-approve all tools (YOLO)
        # -r latest: Resume session to save context and speed up startup
        cmd = [gemini_path, "-p", prompt, "-y", "-r", "latest"]
        
        print(f"Executing: {' '.join(cmd)}")
        
        # Start the process
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            shell=True
        )
        
        # Collect output while it runs
        full_output = []
        start_time = time.time()
        last_update = time.time()
        
        while True:
            # Check for timeout (5 mins)
            if time.time() - start_time > 300:
                process.kill()
                return "⚠️ Task timed out (took > 5 minutes)."
                
            # Read stdout
            line = process.stdout.readline()
            if line:
                full_output.append(line)
                # Every 10 seconds, update the user with progress
                if chat_id and msg_id and time.time() - last_update > 10:
                    update_message(chat_id, msg_id, f"⚡ Still processing... ({int(time.time() - start_time)}s elapsed)")
                    last_update = time.time()
            
            # Check if process finished
            if line == '' and process.poll() is not None:
                break
        
        stdout, stderr = process.communicate()
        if stdout: full_output.append(stdout)
        
        result = "".join(full_output).strip()
        if not result and stderr:
            result = f"❌ Error: {stderr.strip()}"
            
        return result if result else "✅ Task completed (no output)."
        
    except Exception as e:
        return f"❌ System Error: {str(e)}"

# --- STATE MANAGEMENT ---
def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {"authorized_chat_id": None, "last_lead_count": 0, "last_summary_date": None}

def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f)

# --- MONITORING LOGIC ---
def check_leads(chat_id, state):
    if not LEAD_LOG.exists():
        return state

    try:
        with open(LEAD_LOG, "r", encoding="utf-8") as f:
            lines = list(csv.DictReader(f))
            current_count = len(lines)
            
            if current_count > state["last_lead_count"]:
                new_leads = lines[state["last_lead_count"]:]
                for lead in new_leads:
                    priority = "🚨 HIGH PRIORITY" if "high" in lead.get("notes", "").lower() or "high" in lead.get("status", "").lower() else "🆕 New Lead"
                    msg = f"{priority} ALERT!\nName: {lead['lead_name']}\nSource: {lead['source']}\nStatus: {lead['status']}\nNotes: {lead['notes']}"
                    send_message(chat_id, msg)
                
                state["last_lead_count"] = current_count
                save_state(state)
    except Exception as e:
        print(f"Error checking leads: {e}")
    return state

def check_daily_summary(chat_id, state):
    now = datetime.now()
    today_str = str(date.today())
    
    if now.hour >= 20 and state["last_summary_date"] != today_str:
        print(f"Generating Daily Summary for {today_str}...")
        summary = run_gemini_command("Generate a summary of today's work, including new leads and content processed.")
        send_message(chat_id, f"📅 DAY RECAP ({today_str}):\n\n{summary}")
        
        state["last_summary_date"] = today_str
        save_state(state)
    return state

# --- MAIN LOOP ---
def main():
    if not GEMINI_BOT_TOKEN:
        print("CRITICAL: GEMINI_BOT_TOKEN not found. Set it in your environment or the script.")
        return

    state = load_state()
    
    if state["authorized_chat_id"]:
        send_message(state["authorized_chat_id"], "Gemini Exhibition Bridge is LIVE! Send me any command to vibe code from your phone.")

    print("Gemini Exhibition Bridge is LIVE. Listening for Telegram commands...")
    last_update_id = None
    last_check_time = time.time()

    while True:
        updates = get_updates(last_update_id)
        if updates and "result" in updates:
            for update in updates["result"]:
                last_update_id = update["update_id"] + 1
                if "message" in update and "text" in update["message"]:
                    chat_id = update["message"]["chat"]["id"]
                    user_text = update["message"]["text"]
                    
                    if state["authorized_chat_id"] is None:
                        if user_text == "/start":
                            state["authorized_chat_id"] = chat_id
                            save_state(state)
                            send_message(chat_id, "🔓 Access Granted. You are now the Admin of this Gemini Instance.")
                        else:
                            send_message(chat_id, "🔒 Unauthorized. Send /start to claim this bot.")
                        continue
                    
                    if chat_id != state["authorized_chat_id"]:
                        send_message(chat_id, "⛔ Unauthorized. Access Denied.")
                        continue

                    print(f"[{datetime.now().strftime('%H:%M:%S')}] Received: {user_text}")
                    
                    if user_text.lower() == "/status":
                        send_message(chat_id, f"✅ Online. Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\nLeads Tracked: {state['last_lead_count']}")
                    else:
                        # Send initial status and get message ID
                        status_msg = send_message(chat_id, f"⚡ Gemini Processing: \"{user_text}\"...")
                        status_msg_id = status_msg['result']['message_id'] if status_msg and 'result' in status_msg else None
                        
                        response = run_gemini_command(user_text, chat_id, status_msg_id)
                        
                        # Delete the status message or update it
                        if status_msg_id:
                            # We'll send the response and try to edit the original message if it's short, 
                            # or just leave it and send new messages if it's long.
                            if len(response) <= 4000:
                                update_message(chat_id, status_msg_id, response if response else "✅ Task completed.")
                            else:
                                update_message(chat_id, status_msg_id, "✅ Task completed. See output below:")
                                for i in range(0, len(response), 4000):
                                    send_message(chat_id, response[i:i+4000])
                        else:
                            # Fallback if we couldn't get status_msg_id
                            for i in range(0, len(response), 4000):
                                send_message(chat_id, response[i:i+4000])

        if time.time() - last_check_time > 300: # 5 minutes
            if state["authorized_chat_id"]:
                state = check_leads(state["authorized_chat_id"], state)
                state = check_daily_summary(state["authorized_chat_id"], state)
            last_check_time = time.time()

        time.sleep(1)

if __name__ == "__main__":
    main()
