"""
Tests for pipeline.py — verifies step sequencing, {prev_output} interpolation,
capture flag, failure handling, and YAML validation.
"""

import sys
import os
import unittest
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent))

from cook_pipeline import load_pipeline, interpolate, run_step


class TestLoadPipeline(unittest.TestCase):

    def _write_yaml(self, content: str) -> str:
        tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False, encoding="utf-8")
        tmp.write(content)
        tmp.close()
        return tmp.name

    def test_valid_pipeline(self):
        path = self._write_yaml("""
steps:
  - tool: youtube_note.py
    args:
      - "https://youtu.be/EXAMPLE"
  - tool: repurpose_content.py
    args:
      - "--text"
      - "{prev_output}"
    capture: true
""")
        steps = load_pipeline(path)
        self.assertEqual(len(steps), 2)
        self.assertEqual(steps[0]["tool"], "youtube_note.py")
        self.assertTrue(steps[1].get("capture"))
        os.unlink(path)

    def test_missing_file_exits(self):
        with self.assertRaises(SystemExit):
            load_pipeline("/nonexistent/path/pipeline.yaml")

    def test_missing_steps_key_exits(self):
        path = self._write_yaml("tool: something\n")
        with self.assertRaises(SystemExit):
            load_pipeline(path)
        os.unlink(path)

    def test_empty_steps_exits(self):
        path = self._write_yaml("steps: []\n")
        with self.assertRaises(SystemExit):
            load_pipeline(path)
        os.unlink(path)


class TestInterpolate(unittest.TestCase):

    def test_replaces_prev_output_token(self):
        args = ["--text", "{prev_output}", "--type", "reel-value"]
        result = interpolate(args, "my transcript text")
        self.assertEqual(result, ["--text", "my transcript text", "--type", "reel-value"])

    def test_no_token_unchanged(self):
        args = ["--raw", "https://example.com"]
        result = interpolate(args, "ignored")
        self.assertEqual(result, ["--raw", "https://example.com"])

    def test_multiple_tokens_in_one_arg(self):
        args = ["prefix_{prev_output}_suffix"]
        result = interpolate(args, "VALUE")
        self.assertEqual(result, ["prefix_VALUE_suffix"])


class TestRunStep(unittest.TestCase):

    def _make_step(self, tool="capture_idea.py", args=None, capture=False):
        step = {"tool": tool}
        if args:
            step["args"] = args
        if capture:
            step["capture"] = True
        return step

    @patch("pipeline.subprocess.run")
    def test_successful_step_returns_stdout(self, mock_run):
        mock_proc = MagicMock()
        mock_proc.returncode = 0
        mock_proc.stdout = "output text\n"
        mock_proc.stderr = ""
        mock_run.return_value = mock_proc

        # Mock the tool path existence check
        with patch("pipeline.TOOLS_DIR") as mock_tools_dir:
            mock_tool_path = MagicMock()
            mock_tool_path.exists.return_value = True
            mock_tools_dir.__truediv__ = MagicMock(return_value=mock_tool_path)

            result = run_step(self._make_step(), step_num=1, prev_output="")
            self.assertEqual(result, "output text")

    @patch("pipeline.subprocess.run")
    def test_failed_step_exits(self, mock_run):
        mock_proc = MagicMock()
        mock_proc.returncode = 1
        mock_proc.stdout = ""
        mock_proc.stderr = "Error: something went wrong"
        mock_run.return_value = mock_proc

        with patch("pipeline.TOOLS_DIR") as mock_tools_dir:
            mock_tool_path = MagicMock()
            mock_tool_path.exists.return_value = True
            mock_tools_dir.__truediv__ = MagicMock(return_value=mock_tool_path)

            with self.assertRaises(SystemExit) as ctx:
                run_step(self._make_step(), step_num=1, prev_output="")
            self.assertEqual(ctx.exception.code, 1)

    def test_missing_tool_exits(self):
        step = {"tool": "nonexistent_tool_xyz.py", "args": []}
        with self.assertRaises(SystemExit):
            run_step(step, step_num=1, prev_output="")

    def test_missing_tool_key_exits(self):
        step = {"args": ["something"]}
        with self.assertRaises(SystemExit):
            run_step(step, step_num=1, prev_output="")

    @patch("pipeline.subprocess.run")
    def test_capture_writes_file(self, mock_run):
        mock_proc = MagicMock()
        mock_proc.returncode = 0
        mock_proc.stdout = "captured content\n"
        mock_proc.stderr = ""
        mock_run.return_value = mock_proc

        with tempfile.TemporaryDirectory() as tmp_dir:
            with patch("pipeline.TOOLS_DIR") as mock_tools_dir, \
                 patch("pipeline.TMP_DIR", Path(tmp_dir)):
                mock_tool_path = MagicMock()
                mock_tool_path.exists.return_value = True
                mock_tools_dir.__truediv__ = MagicMock(return_value=mock_tool_path)

                step = {"tool": "capture_idea.py", "args": [], "capture": True}
                run_step(step, step_num=2, prev_output="")

                capture_file = Path(tmp_dir) / "pipeline_output_2.txt"
                self.assertTrue(capture_file.exists())
                self.assertEqual(capture_file.read_text(encoding="utf-8"), "captured content")


class TestPrevOutputPassthrough(unittest.TestCase):

    @patch("pipeline.subprocess.run")
    def test_prev_output_interpolated_into_args(self, mock_run):
        mock_proc = MagicMock()
        mock_proc.returncode = 0
        mock_proc.stdout = "final output"
        mock_proc.stderr = ""
        mock_run.return_value = mock_proc

        with patch("pipeline.TOOLS_DIR") as mock_tools_dir:
            mock_tool_path = MagicMock()
            mock_tool_path.exists.return_value = True
            mock_tools_dir.__truediv__ = MagicMock(return_value=mock_tool_path)

            step = {"tool": "repurpose_content.py", "args": ["--text", "{prev_output}"]}
            run_step(step, step_num=2, prev_output="transcript content here")

            cmd_called = mock_run.call_args[0][0]
            self.assertIn("transcript content here", cmd_called)


if __name__ == "__main__":
    unittest.main()
