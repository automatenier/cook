import os
import json
import requests
from dotenv import load_dotenv
from datetime import datetime, timezone
from supabase import create_client

# Load environment variables (Token should be in .env)
load_dotenv()

CLICKUP_API_TOKEN = os.getenv("CLICKUP_API_TOKEN")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_KEY")

BASE_URL = "https://api.clickup.com/api/v2"
HEADERS = {"Authorization": CLICKUP_API_TOKEN, "Content-Type": "application/json"}

def clickup_get(endpoint):
    """Utility to make GET requests to ClickUp."""
    response = requests.get(f"{BASE_URL}/{endpoint}", headers=HEADERS)
    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return None
    return response.json()

def clickup_post(endpoint, data):
    """Utility to make POST requests to ClickUp."""
    response = requests.post(f"{BASE_URL}/{endpoint}", headers=HEADERS, json=data)
    if response.status_code not in [200, 201]:
        print(f"Error {response.status_code}: {response.text}")
        return None
    return response.json()

def get_teams():
    """Get the workspaces (Teams) you belong to."""
    return clickup_get("team")

def get_spaces(team_id):
    """Get all spaces in a workspace."""
    return clickup_get(f"team/{team_id}/space")

def get_folders(space_id):
    """Get all folders in a space."""
    return clickup_get(f"space/{space_id}/folder")

def get_lists(folder_id):
    """Get all lists in a folder."""
    return clickup_get(f"folder/{folder_id}/list")

def get_folderless_lists(space_id):
    """Get lists that aren't in folders."""
    return clickup_get(f"space/{space_id}/list")

def create_task(list_id, name, description="", status="to do", priority=None, due_date=None):
    """Create a task in a specific list."""
    payload = {
        "name": name,
        "description": description,
        "status": status
    }
    if priority: payload["priority"] = priority
    if due_date: payload["due_date"] = int(due_date.timestamp() * 1000)
    
    return clickup_post(f"list/{list_id}/task", payload)

def list_tasks(list_id, archived=False):
    """List all tasks in a specific list."""
    return clickup_get(f"list/{list_id}/task?archived={str(archived).lower()}")

def sync_clickup_to_supabase():
    """
    Fetches all tasks from ClickUp and syncs them to Supabase 
    to maintain the live Dashboard feed.
    """
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("Supabase credentials missing. Skipping sync.")
        return

    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    teams = get_teams()
    if not teams: return

    all_tasks_payload = []

    for team in teams['teams']:
        team_id = team['id']
        spaces = get_spaces(team_id)
        if not spaces: continue

        for space in spaces['spaces']:
            space_id = space['id']
            # Get folderless lists
            folderless = get_folderless_lists(space_id)
            lists = folderless.get('lists', []) if folderless else []
            
            # Get lists in folders
            folders = get_folders(space_id)
            if folders:
                for folder in folders['folders']:
                    folder_lists = get_lists(folder['id'])
                    if folder_lists:
                        lists.extend(folder_lists.get('lists', []))

            for lst in lists:
                list_id = lst['id']
                tasks = list_tasks(list_id)
                if not tasks: continue

                for t in tasks.get('tasks', []):
                    unique_id = f"clickup_{t['id']}"
                    payload = {
                        "name": unique_id,
                        "phone": t['name'][:250],
                        "status": t['status']['status'].upper(),
                        "context": json.dumps({
                            "source": "ClickUp",
                            "list_name": lst['name'],
                            "space_name": space['name'],
                            "description": t.get('description', ''),
                            "url": t.get('url', '')
                        }),
                        "updated_at": datetime.now(timezone.utc).isoformat()
                    }
                    all_tasks_payload.append(payload)

    if all_tasks_payload:
        print(f"Syncing {len(all_tasks_payload)} ClickUp tasks to Supabase...")
        # We don't delete everything here to avoid wiping GSheet data, 
        # but we upsert based on the 'name' (unique_id)
        supabase.table("leads").upsert(all_tasks_payload, on_conflict="name").execute()
        print("ClickUp Sync Complete.")

if __name__ == "__main__":
    # Test run
    print("ClickUp Bridge initialized.")
    # sync_clickup_to_supabase()
