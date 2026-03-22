"""
Tests for youtube_note.py — runs without network or API calls.
All external calls (YouTubeTranscriptApi, anthropic) are mocked.
"""

import sys
import tempfile
import unittest
from pathlib import Path
from datetime import datetime
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent))

import vault_youtube_note as youtube_note


class TestExtractVideoId(unittest.TestCase):
    def test_standard_url(self):
        assert youtube_note.extract_video_id("https://www.youtube.com/watch?v=dQw4w9WgXcQ") == "dQw4w9WgXcQ"

    def test_short_url(self):
        assert youtube_note.extract_video_id("https://youtu.be/dQw4w9WgXcQ") == "dQw4w9WgXcQ"

    def test_mobile_url(self):
        assert youtube_note.extract_video_id("https://m.youtube.com/watch?v=dQw4w9WgXcQ") == "dQw4w9WgXcQ"

    def test_url_with_extra_params(self):
        url = "https://www.youtube.com/watch?v=abc123&t=30s&list=PLxxx"
        assert youtube_note.extract_video_id(url) == "abc123"

    def test_invalid_url_raises(self):
        with self.assertRaises(ValueError):
            youtube_note.extract_video_id("https://vimeo.com/12345")


class TestSlugify(unittest.TestCase):
    def test_basic(self):
        assert youtube_note.slugify("How To Go Viral") == "how-to-go-viral"

    def test_truncated(self):
        result = youtube_note.slugify("a" * 100, max_len=50)
        assert len(result) <= 50


class TestParseClaude(unittest.TestCase):
    SAMPLE_RESPONSE = """TITLE: How I Built a $10K Business in 30 Days
HOOK_TYPE: Bold claim
STRUCTURE: Opens with a shocking result, walks through 3 key steps, closes with a CTA to the course.
KEY_INSIGHTS:
- Consistency beats perfection in content
- Short-form hooks must deliver in first 3 seconds
- Repurposing one video into 5 formats saves 80% of time
SWIPE_NOTES: The "result first, method second" structure is highly replicable for client case studies."""

    def test_title_extracted(self):
        data = youtube_note.parse_claude_response(self.SAMPLE_RESPONSE, "https://youtube.com/watch?v=test")
        assert data["title"] == "How I Built a $10K Business in 30 Days"

    def test_hook_type_extracted(self):
        data = youtube_note.parse_claude_response(self.SAMPLE_RESPONSE, "https://youtube.com/watch?v=test")
        assert data["hook_type"] == "Bold claim"

    def test_insights_are_list(self):
        data = youtube_note.parse_claude_response(self.SAMPLE_RESPONSE, "https://youtube.com/watch?v=test")
        assert isinstance(data["insights"], list)
        assert len(data["insights"]) == 3

    def test_swipe_notes_extracted(self):
        data = youtube_note.parse_claude_response(self.SAMPLE_RESPONSE, "https://youtube.com/watch?v=test")
        assert "result first" in data["swipe_notes"]


class TestWriteNote(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()
        self.patcher = patch.object(youtube_note, "SWIPE_DIR", Path(self.tmp_dir))
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_creates_file(self):
        data = {
            "title": "Test Video Title",
            "hook_type": "Question",
            "structure": "Question → proof → CTA",
            "insights": ["Point A", "Point B"],
            "swipe_notes": "Worth stealing for the hook structure.",
        }
        path = youtube_note.write_note(data, "https://youtube.com/watch?v=test")
        assert path.exists()

    def test_file_contains_url(self):
        url = "https://youtube.com/watch?v=test123"
        data = {
            "title": "My Note",
            "hook_type": "Stat",
            "structure": "Stat → story → CTA",
            "insights": ["Insight 1"],
            "swipe_notes": "Good structure.",
        }
        path = youtube_note.write_note(data, url)
        content = path.read_text(encoding="utf-8")
        assert url in content

    def test_filename_starts_with_date(self):
        data = {
            "title": "Date Test",
            "hook_type": "Story",
            "structure": "Story structure",
            "insights": [],
            "swipe_notes": "Notes.",
        }
        path = youtube_note.write_note(data, "https://youtube.com/watch?v=x")
        today = datetime.now().strftime("%Y-%m-%d")
        assert path.name.startswith(today)


class TestProcessIntegration(unittest.TestCase):
    """Integration test with all external calls mocked."""

    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()
        self.swipe_patcher = patch.object(youtube_note, "SWIPE_DIR", Path(self.tmp_dir))
        self.swipe_patcher.start()

    def tearDown(self):
        self.swipe_patcher.stop()

    @patch("youtube_note.YouTubeTranscriptApi")
    @patch("youtube_note.anthropic.Anthropic")
    def test_full_process(self, mock_anthropic_cls, mock_yt_api):
        # Mock transcript
        mock_yt_api.get_transcript.return_value = [
            {"text": "Welcome to this video.", "start": 0.0, "duration": 2.0},
            {"text": "Today we discuss viral content.", "start": 2.0, "duration": 3.0},
        ]

        # Mock Claude response
        mock_client = MagicMock()
        mock_anthropic_cls.return_value = mock_client
        mock_message = MagicMock()
        mock_message.content = [MagicMock(text="""TITLE: Viral Content Secrets
HOOK_TYPE: Bold claim
STRUCTURE: Opens strong, gives 3 tips, closes with CTA.
KEY_INSIGHTS:
- Hook in first 3 seconds
- Use pattern interrupts
- End with strong CTA
SWIPE_NOTES: Clean structure worth replicating.""")]
        mock_client.messages.create.return_value = mock_message

        path = youtube_note.process("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        assert path.exists()
        content = path.read_text(encoding="utf-8")
        assert "Viral Content Secrets" in content


if __name__ == "__main__":
    unittest.main()
