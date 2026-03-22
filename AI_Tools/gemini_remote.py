import time
import subprocess
import requests
import os
import json
import csv
import threading
from datetime import datetime, date
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

# --- CONFIGURATION ---
GEMINI_BOT_TOKEN = os.getenv("GEMINI_BOT_TOKEN") 
API_URL = f"https://api.telegram.org/bot{GEMINI_BOT_TOKEN}/"
FILE_URL = f"https://api.telegram.org/file/bot{GEMINI_BOT_TOKEN}/"

# Paths
ROOT = Path(__file__).resolve().parent.parent
LEAD_LOG = ROOT / "___Data" / "A JOCONS" / "lead_attribution.csv"
STATE_FILE = ROOT / ".tmp" / "gemini_remote_state.json"
UPLOAD_DIR = ROOT / ".tmp" / "telegram_uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# Global executor for background tasks
executor = ThreadPoolExecutor(max_workers=4)
active_tasks = {} # chat_id -> future

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
        # Telegram limit is 4096 chars. If text is longer, we truncate or append.
        if len(text) > 4000:
            text = text[:3900] + "\n... (truncated, see full output below)"
            
        url = API_URL + "editMessageText"
        payload = {"chat_id": chat_id, "message_id": message_id, "text": text}
        response = requests.post(url, data=payload)
        return response.json()
    except Exception as e:
        print(f"Error editing message: {e}")
        return None

def get_updates(offset=None):
    try:
        url = API_URL + "getUpdates"
        params = {"timeout": 20, "offset": offset}
        response = requests.get(url, params=params)
        return response.json()
    except Exception as e:
        print(f"Error getting updates: {e}")
        return None

def download_file(file_id, dest_name):
    try:
        # Get file path
        res = requests.get(API_URL + "getFile", params={"file_id": file_id}).json()
        if not res.get("ok"): return None
        
        file_path = res["result"]["file_path"]
        download_url = FILE_URL + file_path
        
        dest_path = UPLOAD_DIR / dest_name
        r = requests.get(download_url, stream=True)
        with open(dest_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        return dest_path
    except Exception as e:
        print(f"Error downloading file: {e}")
        return None

def run_gemini_command_worker(prompt, chat_id, status_msg_id, resume=True, attachment_path=None):
    """Executes the gemini cli command with real-time feedback."""
    try:
        gemini_path = r"C:\Users\natha\AppData\Roaming\npm\gemini.cmd"
        
        # Build command
        cmd = [gemini_path, "-p", prompt, "-y"]
        if resume:
            cmd += ["-r", "latest"]
        
        if attachment_path:
            # We assume the CLI can take a path as part of the prompt or as a separate arg
            # Based on standard usage, we append the path to the command
            cmd.append(str(attachment_path))
            
        print(f"[{chat_id}] Executing: {' '.join(cmd)}")
        
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            shell=True,
            bufsize=1
        )
        
        full_output = []
        last_update_time = time.time()
        start_time = time.time()
        
        # Process output in real-time
        while True:
            line = process.stdout.readline()
            if line:
                full_output.append(line)
                # Update Telegram every 3 seconds to avoid rate limits but stay snappy
                if time.time() - last_update_time > 3:
                    current_text = "".join(full_output).strip()
                    if current_text:
                        update_message(chat_id, status_msg_id, f"⚡ GEMINI RUNNING...\n\n{current_text[-3500:]}")
                    else:
                        update_message(chat_id, status_msg_id, f"⚡ Still processing... ({int(time.time() - start_time)}s)")
                    last_update_time = time.time()
            
            if line == '' and process.poll() is not None:
                break
                
            if time.time() - start_time > 600: # 10 min timeout
                process.kill()
                update_message(chat_id, status_msg_id, "⚠️ Task timed out (10 mins).")
                return

        stdout, stderr = process.communicate()
        if stdout: full_output.append(stdout)
        
        result = "".join(full_output).strip()
        if not result and stderr:
            result = f"❌ Error: {stderr.strip()}"
            
        final_text = result if result else "✅ Task completed."
        
        # Final update
        if len(final_text) <= 4000:
            update_message(chat_id, status_msg_id, final_text)
        else:
            update_message(chat_id, status_msg_id, "✅ Task completed. See output below:")
            for i in range(0, len(final_text), 4000):
                send_message(chat_id, final_text[i:i+4000])
                
    except Exception as e:
        send_message(chat_id, f"❌ System Error: {str(e)}")
    finally:
        if chat_id in active_tasks:
            del active_tasks[chat_id]

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
    if not LEAD_LOG.exists(): return state
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

# --- MAIN LOOP ---
def main():
    if not GEMINI_BOT_TOKEN:
        print("CRITICAL: GEMINI_BOT_TOKEN not found.")
        return

    state = load_state()
    if state["authorized_chat_id"]:
        send_message(state["authorized_chat_id"], "🚀 Gemini Remote 2.0 is LIVE!\n\n- Multimodal support (send photos!)\n- Real-time streaming output\n- Async task execution\n- Use /reset to clear context")

    print("Gemini Remote 2.0 is LIVE. Listening...")
    last_update_id = None
    last_check_time = time.time()

    while True:
        updates = get_updates(last_update_id)
        if updates and "result" in updates:
            for update in updates["result"]:
                last_update_id = update["update_id"] + 1
                
                # Extract message info
                msg = update.get("message")
                if not msg: continue
                
                chat_id = msg["chat"]["id"]
                user_text = msg.get("text", "")
                photo = msg.get("photo")
                document = msg.get("document")
                
                # Auth
                if state["authorized_chat_id"] is None:
                    if user_text == "/start":
                        state["authorized_chat_id"] = chat_id
                        save_state(state)
                        send_message(chat_id, "🔓 Access Granted. Admin assigned.")
                    continue
                
                if chat_id != state["authorized_chat_id"]:
                    send_message(chat_id, "⛔ Unauthorized.")
                    continue

                # Commands
                if user_text == "/status":
                    send_message(chat_id, f"✅ Online. {len(active_tasks)} tasks running.")
                    continue
                
                if user_text == "/reset":
                    status_msg = send_message(chat_id, "🧹 Resetting session (starting fresh)...")
                    executor.submit(run_gemini_command_worker, "Hello, start fresh.", chat_id, status_msg['result']['message_id'], resume=False)
                    continue

                # Handle Input (Text or Photo)
                attachment_path = None
                prompt = user_text
                
                if photo:
                    # Get largest photo
                    file_id = photo[-1]["file_id"]
                    attachment_path = download_file(file_id, f"photo_{int(time.time())}.jpg")
                    prompt = msg.get("caption", "Analyze this image.")
                    send_message(chat_id, f"📸 Image received. Downloaded to {attachment_path.name}")
                elif document:
                    file_id = document["file_id"]
                    fname = document.get("file_name", f"doc_{int(time.time())}")
                    attachment_path = download_file(file_id, fname)
                    prompt = msg.get("caption", "Analyze this document.")
                    send_message(chat_id, f"📄 Document received: {fname}")

                if prompt or attachment_path:
                    status_msg = send_message(chat_id, f"⚡ Gemini: \"{prompt[:50]}...\"")
                    if status_msg:
                        msg_id = status_msg['result']['message_id']
                        active_tasks[chat_id] = executor.submit(
                            run_gemini_command_worker, prompt, chat_id, msg_id, True, attachment_path
                        )

        # Periodic checks
        if time.time() - last_check_time > 300:
            if state["authorized_chat_id"]:
                state = check_leads(state["authorized_chat_id"], state)
            last_check_time = time.time()
        
        time.sleep(0.1) # Fast loop for responsiveness

if __name__ == "__main__":
    main()
