"""
cook.py — Unified CLI entry point for Cook Tools.

Run without Claude Code open:
    py -3 AI_Tools/cook.py

Reads tool list from tools_index.md, groups by prefix, presents a numbered
menu, and runs the selected tool via subprocess.
"""

import re
import subprocess
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).parent
INDEX_FILE = TOOLS_DIR / "tools_index.md"

# Group order and display names
GROUP_ORDER = ["content_", "cook_", "vault_"]
GROUP_LABELS = {
    "content_": "Content Production",
    "cook_":    "Business Ops",
    "vault_":   "Knowledge Capture",
}


def parse_tools(index_path: Path) -> dict[str, list[dict]]:
    """Parse tools_index.md → {prefix: [{name, purpose}]}"""
    groups: dict[str, list[dict]] = {g: [] for g in GROUP_ORDER}
    current_group = None

    row_re = re.compile(r"\|\s*`([^`]+\.py)`\s*\|\s*([^|]+)\|")

    for line in index_path.read_text(encoding="utf-8").splitlines():
        for prefix in GROUP_ORDER:
            if f"`{prefix}" in line and "##" in line:
                current_group = prefix
                break
        if current_group:
            m = row_re.search(line)
            if m:
                name = m.group(1).strip()
                purpose = m.group(2).strip()
                # Only add to the matching group
                for prefix in GROUP_ORDER:
                    if name.startswith(prefix):
                        groups[prefix].append({"name": name, "purpose": purpose})
                        break

    return groups


def print_menu(groups: dict[str, list[dict]]) -> list[dict]:
    """Print numbered menu, return flat list of tools in display order."""
    flat: list[dict] = []
    idx = 1

    print("\n=== Cook Tools ===\n")
    for prefix in GROUP_ORDER:
        tools = groups.get(prefix, [])
        if not tools:
            continue
        print(f"  [{GROUP_LABELS[prefix]}]")
        for tool in tools:
            print(f"  {idx:>3}. {tool['name']:<45} {tool['purpose'][:60]}")
            flat.append(tool)
            idx += 1
        print()

    print("    0. Exit")
    return flat


def run_tool(tool_name: str, extra_args: list[str]) -> None:
    script = TOOLS_DIR / tool_name
    if not script.exists():
        print(f"  ERROR: {script} not found.")
        return
    cmd = [sys.executable, str(script)] + extra_args
    print(f"\n  Running: {' '.join(cmd)}\n{'─' * 60}")
    subprocess.run(cmd)


def main() -> None:
    if not INDEX_FILE.exists():
        print(f"ERROR: tools_index.md not found at {INDEX_FILE}")
        sys.exit(1)

    groups = parse_tools(INDEX_FILE)

    while True:
        flat = print_menu(groups)

        try:
            raw = input("  Select tool number (0 to exit): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n  Bye.")
            break

        if raw == "0":
            print("  Bye.")
            break

        if not raw.isdigit() or not (1 <= int(raw) <= len(flat)):
            print(f"  Invalid choice. Enter 1–{len(flat)} or 0 to exit.\n")
            continue

        tool = flat[int(raw) - 1]
        extra = input(f"  Args for {tool['name']} (leave blank if none): ").strip().split()
        run_tool(tool["name"], extra)
        input("\n  Press Enter to return to menu...")


if __name__ == "__main__":
    main()
