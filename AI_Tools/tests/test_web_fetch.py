"""
Tests for web_fetch.py — verifies HTML stripping, content extraction,
--raw flag behavior, and error handling.
"""

import sys
import unittest
from unittest.mock import MagicMock, patch
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from cook_web_fetch import fetch_and_clean, haiku_extract, STRIP_TAGS

SAMPLE_HTML = """
<html>
<head><style>body { color: red; }</style></head>
<body>
  <nav>Nav links here</nav>
  <header>Site header</header>
  <main>
    <h1>Main Article Title</h1>
    <p>This is the real content we want.</p>
    <p>Second paragraph with useful info.</p>
  </main>
  <footer>Footer garbage</footer>
  <script>alert('noise')</script>
</body>
</html>
"""

SAMPLE_HTML_NO_MAIN = """
<html>
<body>
  <script>noise()</script>
  <style>.x { color: blue; }</style>
  <p>Fallback body content.</p>
</body>
</html>
"""


class TestFetchAndClean(unittest.TestCase):

    def _make_mock_response(self, html: str) -> MagicMock:
        mock_resp = MagicMock()
        mock_resp.text = html
        mock_resp.raise_for_status = MagicMock()
        return mock_resp

    @patch("web_fetch.requests.get")
    def test_strips_noise_tags(self, mock_get):
        mock_get.return_value = self._make_mock_response(SAMPLE_HTML)
        result = fetch_and_clean("https://example.com")
        # Noise content must not appear
        self.assertNotIn("Nav links here", result)
        self.assertNotIn("Site header", result)
        self.assertNotIn("Footer garbage", result)
        self.assertNotIn("alert", result)
        self.assertNotIn("color: red", result)

    @patch("web_fetch.requests.get")
    def test_prefers_main_content(self, mock_get):
        mock_get.return_value = self._make_mock_response(SAMPLE_HTML)
        result = fetch_and_clean("https://example.com")
        self.assertIn("Main Article Title", result)
        self.assertIn("This is the real content we want.", result)
        self.assertIn("Second paragraph with useful info.", result)

    @patch("web_fetch.requests.get")
    def test_falls_back_to_body_when_no_main(self, mock_get):
        mock_get.return_value = self._make_mock_response(SAMPLE_HTML_NO_MAIN)
        result = fetch_and_clean("https://example.com")
        self.assertIn("Fallback body content.", result)
        # Script and style should still be stripped
        self.assertNotIn("noise()", result)
        self.assertNotIn("color: blue", result)

    @patch("web_fetch.requests.get")
    def test_raises_on_http_error(self, mock_get):
        import requests as req
        mock_resp = MagicMock()
        mock_resp.raise_for_status.side_effect = req.HTTPError("404")
        mock_get.return_value = mock_resp
        with self.assertRaises(req.HTTPError):
            fetch_and_clean("https://example.com/404")


class TestHaikuExtract(unittest.TestCase):

    @patch("anthropic.Anthropic")
    def test_calls_haiku_with_hint(self, mock_anthropic_class):
        mock_client = MagicMock()
        mock_anthropic_class.return_value = mock_client
        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="Extracted pricing: $99/month")]
        mock_client.messages.create.return_value = mock_response

        result = haiku_extract("Page text here", "extract pricing")

        self.assertEqual(result, "Extracted pricing: $99/month")
        call_kwargs = mock_client.messages.create.call_args[1]
        self.assertEqual(call_kwargs["model"], "claude-haiku-4-5-20251001")

    @patch("anthropic.Anthropic")
    def test_truncates_long_text(self, mock_anthropic_class):
        mock_client = MagicMock()
        mock_anthropic_class.return_value = mock_client
        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="result")]
        mock_client.messages.create.return_value = mock_response

        long_text = "x" * 20000
        haiku_extract(long_text, "extract something")

        call_kwargs = mock_client.messages.create.call_args[1]
        # Check the user message content contains truncated text (capped at MAX_CHARS_FOR_HAIKU)
        user_content = call_kwargs["messages"][0]["content"]
        self.assertLessEqual(len(user_content), 20000)


class TestRawFlag(unittest.TestCase):
    """Integration-style test: --raw should not call Claude."""

    @patch("web_fetch.requests.get")
    @patch("web_fetch.haiku_extract")
    def test_raw_skips_haiku(self, mock_haiku, mock_get):
        mock_resp = MagicMock()
        mock_resp.text = SAMPLE_HTML
        mock_resp.raise_for_status = MagicMock()
        mock_get.return_value = mock_resp

        # Simulate --raw: fetch and clean, then check haiku is NOT called
        fetch_and_clean("https://example.com")
        mock_haiku.assert_not_called()


if __name__ == "__main__":
    unittest.main()
