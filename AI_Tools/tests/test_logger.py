"""
Tests for logger.py — runs without network or API calls.
"""

import csv
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parent.parent))
import cook_logger as logger


class TestLogAgentRun(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = Path(tempfile.mkdtemp())
        self.tmp_log = self.tmp_dir / "agent_log.csv"
        self.patcher_dir = patch.object(logger, "DATA_DIR", self.tmp_dir)
        self.patcher_log = patch.object(logger, "AGENT_LOG", self.tmp_log)
        self.patcher_dir.start()
        self.patcher_log.start()

    def tearDown(self):
        self.patcher_dir.stop()
        self.patcher_log.stop()

    def _read_rows(self):
        with self.tmp_log.open(newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))

    def test_creates_file_with_header(self):
        logger.log_agent_run("Test-workflow", "test_tool.py", 1.23, "success")
        assert self.tmp_log.exists()
        rows = self._read_rows()
        assert len(rows) == 1

    def test_header_written_once(self):
        logger.log_agent_run("Test-workflow", "tool.py", 0.5, "success")
        logger.log_agent_run("Test-workflow", "tool.py", 0.6, "success")
        with self.tmp_log.open(encoding="utf-8") as f:
            lines = f.readlines()
        header_count = sum(1 for line in lines if line.startswith("timestamp"))
        assert header_count == 1, "Header should appear exactly once"

    def test_row_fields(self):
        logger.log_agent_run(
            "Ops-inbox-triage", "capture_idea.py", 2.5, "success", notes="test run"
        )
        rows = self._read_rows()
        row = rows[0]
        assert row["workflow"] == "Ops-inbox-triage"
        assert row["tool"] == "capture_idea.py"
        assert row["duration_sec"] == "2.5"
        assert row["status"] == "success"
        assert row["error_msg"] == ""
        assert row["notes"] == "test run"

    def test_error_row(self):
        logger.log_agent_run(
            "Writer-write-scripts", "repurpose_content.py", 0.1, "error",
            error_msg="FileNotFoundError: brief.md missing"
        )
        rows = self._read_rows()
        assert rows[0]["status"] == "error"
        assert "FileNotFoundError" in rows[0]["error_msg"]

    def test_appends_multiple_rows(self):
        for i in range(5):
            logger.log_agent_run("workflow", "tool.py", float(i), "success")
        rows = self._read_rows()
        assert len(rows) == 5

    def test_timestamp_format(self):
        import re
        logger.log_agent_run("workflow", "tool.py", 1.0, "success")
        rows = self._read_rows()
        ts = rows[0]["timestamp"]
        assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", ts), f"Bad timestamp: {ts}"

    def test_duration_rounded(self):
        logger.log_agent_run("workflow", "tool.py", 1.23456789, "success")
        rows = self._read_rows()
        assert rows[0]["duration_sec"] == "1.235"


class TestClientLog(unittest.TestCase):
    def setUp(self):
        self.tmp_root = Path(tempfile.mkdtemp())
        self.tmp_data = self.tmp_root / "03_AgentMEMORY"
        self.tmp_log = self.tmp_data / "agent_log.csv"
        self.patcher_root = patch.object(logger, "ROOT", self.tmp_root)
        self.patcher_dir = patch.object(logger, "DATA_DIR", self.tmp_data)
        self.patcher_log = patch.object(logger, "AGENT_LOG", self.tmp_log)
        self.patcher_root.start()
        self.patcher_dir.start()
        self.patcher_log.start()

    def tearDown(self):
        self.patcher_root.stop()
        self.patcher_dir.stop()
        self.patcher_log.stop()

    def test_client_log_created(self):
        logger.log_agent_run("content-write-scripts", "content_repurpose.py", 1.0, "success", client="fadli")
        client_log = self.tmp_root / "Content" / "02_WORKSPACE" / "jocons" / "fadli" / "LOG.md"
        assert client_log.exists(), "LOG.md should be created for client"

    def test_client_log_contains_entry(self):
        logger.log_agent_run("content-write-scripts", "content_repurpose.py", 1.0, "success",
                             notes="3 scripts drafted", client="fadli")
        client_log = self.tmp_root / "Content" / "02_WORKSPACE" / "jocons" / "fadli" / "LOG.md"
        content = client_log.read_text(encoding="utf-8")
        assert "content_repurpose.py" in content
        assert "success" in content

    def test_client_log_appends(self):
        for i in range(3):
            logger.log_agent_run("workflow", "tool.py", 1.0, "success", client="ruth")
        client_log = self.tmp_root / "Content" / "02_WORKSPACE" / "jocons" / "ruth" / "LOG.md"
        lines = [l for l in client_log.read_text(encoding="utf-8").splitlines() if l.strip()]
        assert len(lines) == 3

    def test_unknown_client_no_error(self):
        # Should not raise — just skip silently
        logger.log_agent_run("workflow", "tool.py", 1.0, "success", client="unknown_client_xyz")

    def test_no_client_no_log(self):
        logger.log_agent_run("workflow", "tool.py", 1.0, "success")
        workspace = self.tmp_root / "Content" / "02_WORKSPACE"
        assert not workspace.exists(), "No client folders should be created when client not specified"


if __name__ == "__main__":
    unittest.main()
