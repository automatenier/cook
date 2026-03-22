"""
cook_logger.py — Append-only logging utility for WAT agent execution metrics.

Writes one row per tool/workflow execution to AI_MEMORY/agent_log.csv.
Optionally appends a human-readable line to the client's LOG.md.

Import and call log_agent_run() from any tool after its main operation.

Usage (from any tool):
    from cook_logger import log_agent_run
    import time

    start = time.time()
    # ... do work ...
    log_agent_run("content-write-scripts", "content_repurpose.py", time.time() - start, "success")
    # With client breadcrumb:
    log_agent_run("content-write-scripts", "content_repurpose.py", time.time() - start, "success", client="fadli")
    # On failure:
    log_agent_run("content-write-scripts", "content_repurpose.py", time.time() - start, "error", error_msg=str(e))
"""

import csv
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "AI_MEMORY"
AGENT_LOG = DATA_DIR / "agent_log.csv"

HEADERS = ["timestamp", "workflow", "tool", "duration_sec", "status", "error_msg", "notes"]

# Maps client name → relative path inside VLT_Content/02_HMN_HUMANFLOW/
CLIENT_FOLDERS = {
    "fadli": "jocons/fadli",
    "ruth": "jocons/ruth",
    "jordan": "jocons/Mathew_Jordan",
    "mathew_jordan": "jocons/Mathew_Jordan",
    "mathew jordan": "jocons/Mathew_Jordan",
    "real_estate": "real_estate",
    "savasa": "real_estate",
}


def _append_client_log(client: str, tool: str, status: str, notes: str) -> None:
    """Append one breadcrumb line to VLT_Content/02_HMN_HUMANFLOW/[client]/LOG.md."""
    folder_key = client.lower().replace(" ", "_")
    rel_path = CLIENT_FOLDERS.get(folder_key) or CLIENT_FOLDERS.get(client.lower())
    if not rel_path:
        return  # Unknown client — skip silently

    log_file = ROOT / "Content" / "02_WORKSPACE" / rel_path / "LOG.md"
    log_file.parent.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    note_str = f" | {notes}" if notes else ""
    line = f"> {timestamp} | {tool} | {status}{note_str}\n"

    with log_file.open("a", encoding="utf-8") as f:
        f.write(line)


def log_agent_status(
    workflow: str,
    tool: str,
    status: str = "RUNNING",
    notes: str = "",
    client: str = "",
) -> None:
    """Log an immediate status update (START, RUNNING, PENDING) without a duration."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    write_header = not AGENT_LOG.exists() or AGENT_LOG.stat().st_size == 0
    with AGENT_LOG.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        if write_header:
            writer.writeheader()
        writer.writerow({
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            "workflow": workflow,
            "tool": tool,
            "duration_sec": 0.0,
            "status": status,
            "error_msg": "",
            "notes": notes,
        })

    if client:
        _append_client_log(client, tool, status, notes)


def log_agent_run(
    workflow: str,
    tool: str,
    duration_sec: float,
    status: str,
    error_msg: str = "",
    notes: str = "",
    client: str = "",
) -> None:
    """Append one execution record to AI_MEMORY/agent_log.csv.

    Args:
        workflow:     Workflow name, e.g. "content-write-scripts"
        tool:         Script filename, e.g. "content_repurpose.py", or "inline"
        duration_sec: Wall-clock seconds the operation took
        status:       "success" or "error"
        error_msg:    Exception message if status == "error", else ""
        notes:        Optional freeform context (output path, counts, etc.)
        client:       Optional client name — triggers per-client LOG.md append
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    write_header = not AGENT_LOG.exists() or AGENT_LOG.stat().st_size == 0

    with AGENT_LOG.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        if write_header:
            writer.writeheader()
        writer.writerow({
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            "workflow": workflow,
            "tool": tool,
            "duration_sec": round(duration_sec, 3),
            "status": status,
            "error_msg": error_msg,
            "notes": notes,
        })

    if client:
        _append_client_log(client, tool, status, notes)
