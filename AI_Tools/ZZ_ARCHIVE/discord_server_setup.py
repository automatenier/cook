import requests
import json
import os
import time

# --- CONFIGURATION ---
# It is recommended to set these as environment variables
TOKEN = os.getenv("DISCORD_BOT_TOKEN") 
GUILD_ID = os.getenv("DISCORD_GUILD_ID")

BASE_URL = f"https://discord.com/api/v10"
HEADERS = {
    "Authorization": f"Bot {TOKEN}",
    "Content-Type": "application/json"
}

# --- SERVER STRUCTURE ---
STRUCTURE = [
    {
        "category": "🏁 START HERE",
        "channels": [
            {"name": "👋-welcome", "topic": "Rules and navigation guide."},
            {"name": "🚀-onboarding", "topic": "Checklist for new clients (Notion, n8n, Telegram)."},
            {"name": "📢-announcements", "topic": "Major product updates and schedule changes."}
        ]
    },
    {
        "category": "🧠 THE SYSTEM (INFRASTRUCTURE)",
        "channels": [
            {"name": "📋-notion-hub", "topic": "Direct links and tutorials for Content Calendar & Swipe Library."},
            {"name": "🤖-ai-prompts", "topic": "Claude prompt library repository."},
            {"name": "⚡-automation-n8n", "topic": "Monitoring for n8n workflows and notifications."},
            {"name": "📊-dashboards", "topic": "Sales HQ and KPI tracker discussion."}
        ]
    },
    {
        "category": "📹 CONTENT ENGINE",
        "channels": [
            {"name": "🎬-reel-production", "topic": "Discussion for the 14 monthly reels and production status."},
            {"name": "📚-swipe-library", "topic": "Newly analyzed viral structures (Gemini JSON)."},
            {"name": "🎣-hooks-ctas", "topic": "Testing and feedback for hooks and keyword CTAs."},
            {"name": "📤-content-approval", "topic": "Client previews for approval."}
        ]
    },
    {
        "category": "🎓 EDUCATION & GROWTH",
        "channels": [
            {"name": "🎥-ai-video-module", "topic": "Discussion threads for the AI Video course."},
            {"name": "📈-strategy-consult", "topic": "Pre-call prep for monthly 1-on-1s."},
            {"name": "🤝-mastermind-calls", "topic": "Schedule and recordings for bi-weekly group calls."},
            {"name": "💡-hot-seats", "topic": "Request Hot Seat advice here."}
        ]
    },
    {
        "category": "👥 COMMUNITY & SUPPORT",
        "channels": [
            {"name": "💬-general-chat", "topic": "Networking for program members."},
            {"name": "🏆-wins-results", "topic": "Share success stories and KPI wins."},
            {"name": "🛠️-tech-support", "topic": "Troubleshooting for Notion, n8n, or AI tools."},
            {"name": "❓-q-and-a", "topic": "General questions for the team."}
        ]
    }
]

def create_channel(name, channel_type, parent_id=None, topic=None):
    url = f"{BASE_URL}/guilds/{GUILD_ID}/channels"
    data = {
        "name": name,
        "type": channel_type,
        "parent_id": parent_id
    }
    if topic:
        data["topic"] = topic
        
    response = requests.post(url, headers=HEADERS, json=data)
    if response.status_code == 201:
        print(f"✅ Created {'Category' if channel_type == 4 else 'Channel'}: {name}")
        return response.json()["id"]
    else:
        print(f"❌ Failed to create {name}: {response.text}")
        return None

def setup_server():
    if not TOKEN or not GUILD_ID:
        print("❌ Error: DISCORD_BOT_TOKEN or DISCORD_GUILD_ID not found in environment.")
        return

    print(f"🚀 Starting server setup for Guild ID: {GUILD_ID}...")
    
    for item in STRUCTURE:
        # Create Category (Type 4)
        category_id = create_channel(item["category"], 4)
        if category_id:
            for channel in item["channels"]:
                # Create Text Channel (Type 0) under Category
                create_channel(channel["name"], 0, parent_id=category_id, topic=channel.get("topic"))
                time.sleep(0.5) # Avoid rate limiting

if __name__ == "__main__":
    setup_server()
