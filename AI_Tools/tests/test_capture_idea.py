"""
Tests for capture_idea.py — runs without network or API calls.
"""

import sys
import os
import tempfile
import unittest
from pathlib import Path
from datetime import datetime
from unittest.mock import patch

# Add tools dir to path
sys.path.insert(0, str(Path(__file__).parent.parent))

import content_capture_idea as capture_idea


class TestSlugify(unittest.TestCase):
    def test_basic(self):
        assert capture_idea.slugify("Hello World Idea") == "hello-world-idea"

    def test_special_chars_stripped(self):
        assert capture_idea.slugify("It's a great idea!") == "its-a-great-idea"

    def test_truncated(self):
        long = "a" * 100
        result = capture_idea.slugify(long, max_len=40)
        assert len(result) <= 40

    def test_multiple_spaces(self):
        assert capture_idea.slugify("a  b   c") == "a-b-c"


class TestCaptureIdea(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()
        # Patch INBOX_DIR to write into temp dir
        self.patcher = patch.object(capture_idea, "INBOX_DIR", Path(self.tmp_dir))
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_creates_file(self):
        path = capture_idea.capture_idea("Build a YouTube research tool")
        assert path.exists(), f"File not created at {path}"

    def test_filename_format(self):
        path = capture_idea.capture_idea("Test idea for filename")
        today = datetime.now().strftime("%Y-%m-%d")
        assert path.name.startswith(today), f"Filename should start with today's date, got: {path.name}"
        assert "idea" in path.name

    def test_file_contains_text(self):
        raw = "Launch a morning briefing system"
        path = capture_idea.capture_idea(raw)
        content = path.read_text(encoding="utf-8")
        assert raw in content

    def test_frontmatter_tags(self):
        path = capture_idea.capture_idea("Some tagged idea")
        content = path.read_text(encoding="utf-8")
        assert "tags: [idea]" in content
        assert "status: raw" in content

    def test_empty_text_raises(self):
        with self.assertRaises(ValueError):
            capture_idea.capture_idea("   ")

    def test_no_collision(self):
        """Same text twice should produce two distinct files."""
        path1 = capture_idea.capture_idea("Duplicate idea")
        path2 = capture_idea.capture_idea("Duplicate idea")
        assert path1 != path2, "Should not overwrite on slug collision"
        assert path1.exists()
        assert path2.exists()


if __name__ == "__main__":
    unittest.main()
