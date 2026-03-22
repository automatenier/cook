"""
pipeline.py — Run multiple Cook tools in sequence, passing outputs between steps.

Implements Programmatic Tool Calling: instead of the agent babysitting each
tool call and manually passing results, a YAML pipeline definition runs the
entire chain deterministically — loops, conditionals, and output passing handled
by code, not by the LLM.

Usage:
    py -3 AI_Tools/pipeline.py <pipeline.yaml>

Pipeline YAML format:
    steps:
      - tool: youtube_note.py
        args:
          - "https://youtu.be/VIDEO_ID"
      - tool: repurpose_content.py
        args:
          - "--text"
          - "{prev_output}"
        capture: true   # saves stdout to .tmp/pipeline_output_<n>.txt

Token economy: the agent triggers one command, not N sequential tool calls.
Each intermediate result stays in files, not in the LLM context window.

Examples:
    py -3 AI_Tools/pipeline.py .tmp/pipeline_examples/youtube_to_repurpose.yaml
"""

import sys
import subprocess
import argparse
from pathlib import Path

import yaml

TOOLS_DIR = Path(__file__).parent
PROJECT_ROOT = TOOLS_DIR.parent
TMP_DIR = PROJECT_ROOT / ".tmp"


def load_pipeline(yaml_path: str) -> list[dict]:
    """Load and validate a pipeline YAML file. Returns list of steps."""
    path = Path(yaml_path)
    if not path.exists():
        print(f"Pipeline file not found: {yaml_path}", file=sys.stderr)
        sys.exit(1)

    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict) or "steps" not in data:
        print("Invalid pipeline: must have a top-level 'steps' key.", file=sys.stderr)
        sys.exit(1)

    steps = data["steps"]
    if not isinstance(steps, list) or len(steps) == 0:
        print("Invalid pipeline: 'steps' must be a non-empty list.", file=sys.stderr)
        sys.exit(1)

    return steps


def interpolate(args: list, prev_output: str) -> list:
    """Replace {prev_output} tokens in args with the previous step's stdout."""
    return [arg.replace("{prev_output}", prev_output) for arg in args]


def run_step(step: dict, step_num: int, prev_output: str) -> str:
    """
    Execute a single pipeline step.
    Returns stdout of the step as a string.
    Exits on non-zero return code.
    """
    tool = step.get("tool")
    if not tool:
        print(f"Step {step_num}: missing 'tool' field.", file=sys.stderr)
        sys.exit(1)

    raw_args = step.get("args", [])
    # Ensure all args are strings
    raw_args = [str(a) for a in raw_args]
    args = interpolate(raw_args, prev_output)

    tool_path = TOOLS_DIR / tool
    if not tool_path.exists():
        print(f"Step {step_num}: tool not found: {tool_path}", file=sys.stderr)
        sys.exit(1)

    cmd = [sys.executable, str(tool_path)] + args
    print(f"[pipeline] Step {step_num}: {tool} {' '.join(args)}", file=sys.stderr)

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        cwd=str(PROJECT_ROOT),
    )

    if result.returncode != 0:
        print(
            f"[pipeline] Step {step_num} FAILED (exit {result.returncode}):\n{result.stderr}",
            file=sys.stderr,
        )
        sys.exit(result.returncode)

    output = result.stdout.strip()

    # Optional: capture output to a file
    if step.get("capture"):
        TMP_DIR.mkdir(parents=True, exist_ok=True)
        capture_path = TMP_DIR / f"pipeline_output_{step_num}.txt"
        capture_path.write_text(output, encoding="utf-8")
        print(f"[pipeline] Step {step_num} output saved to {capture_path}", file=sys.stderr)

    return output


def main():
    parser = argparse.ArgumentParser(
        description="Run a sequence of Cook tools defined in a YAML pipeline."
    )
    parser.add_argument("pipeline", help="Path to pipeline YAML file")
    args = parser.parse_args()

    steps = load_pipeline(args.pipeline)
    prev_output = ""

    for i, step in enumerate(steps, start=1):
        prev_output = run_step(step, i, prev_output)

    # Print final output to stdout so the agent can read it
    print(prev_output)


if __name__ == "__main__":
    main()
