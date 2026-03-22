"""
Tests for cook.py — runs without network, API calls, or user input.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import cook


TOOLS_DIR = Path(__file__).parent.parent
INDEX_FILE = TOOLS_DIR / "tools_index.md"


class TestParseTools(unittest.TestCase):
    def setUp(self):
        assert INDEX_FILE.exists(), f"tools_index.md missing at {INDEX_FILE}"
        self.groups = cook.parse_tools(INDEX_FILE)

    def test_all_groups_present(self):
        for prefix in cook.GROUP_ORDER:
            self.assertIn(prefix, self.groups, f"Group '{prefix}' missing from parsed output")

    def test_each_group_has_tools(self):
        for prefix in cook.GROUP_ORDER:
            tools = self.groups[prefix]
            self.assertGreater(len(tools), 0, f"Group '{prefix}' has no tools")

    def test_tool_has_name_and_purpose(self):
        for prefix in cook.GROUP_ORDER:
            for tool in self.groups[prefix]:
                self.assertIn("name", tool)
                self.assertIn("purpose", tool)
                self.assertTrue(tool["name"].endswith(".py"), f"Tool name should end in .py: {tool['name']}")
                self.assertTrue(len(tool["purpose"]) > 0, f"Tool '{tool['name']}' has empty purpose")

    def test_tools_match_prefix(self):
        for prefix in cook.GROUP_ORDER:
            for tool in self.groups[prefix]:
                self.assertTrue(
                    tool["name"].startswith(prefix),
                    f"Tool '{tool['name']}' is in wrong group '{prefix}'"
                )

    def test_all_listed_tools_exist_on_disk(self):
        missing = []
        for prefix in cook.GROUP_ORDER:
            for tool in self.groups[prefix]:
                script = TOOLS_DIR / tool["name"]
                if not script.exists():
                    missing.append(tool["name"])
        self.assertEqual(
            missing, [],
            f"Tools listed in tools_index.md but missing on disk: {missing}"
        )


class TestPrintMenu(unittest.TestCase):
    def test_returns_flat_list(self):
        groups = cook.parse_tools(INDEX_FILE)
        flat = cook.print_menu(groups)
        total = sum(len(v) for v in groups.values())
        self.assertEqual(len(flat), total)

    def test_flat_list_order_matches_group_order(self):
        groups = cook.parse_tools(INDEX_FILE)
        flat = cook.print_menu(groups)
        # First tool should be from content_ group
        if groups.get("content_"):
            self.assertTrue(flat[0]["name"].startswith("content_"))


if __name__ == "__main__":
    unittest.main()
