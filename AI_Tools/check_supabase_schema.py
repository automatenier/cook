from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://xmfkewjxjsrffvmlcsid.supabase.co")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhtZmtld2p4anNyZmZ2bWxjc2lkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3MzkxNTI2MSwiZXhwIjoyMDg5NDkxMjYxfQ.Ra00Q2VbWhp-303XVjn4-94D1QUjFv-2rb9-sarrk98")

def check_schema():
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    try:
        # Try to select one row including the 'source' column
        res = supabase.table("leads").select("name, source").limit(1).execute()
        print("Success: 'source' column exists!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_schema()
