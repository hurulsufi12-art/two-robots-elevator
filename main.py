"""Two Robots in an Elevator - make.fun entry.

Writes one line of awkward robot-to-robot small talk to entry.txt.
"""

import argparse
import sys
from pathlib import Path

TEXT = "Your proximity sensor keeps apologizing to my proximity sensor, and we still have eleven floors to go."


def validate(text):
    """Refuse any text that would fail the bounty gate; exit 1, write nothing."""
    if not 1 <= len(text) <= 200:
        print("error: text must be 1-200 characters", file=sys.stderr)
        raise SystemExit(1)
    if not text.strip():
        print("error: text must not be only whitespace", file=sys.stderr)
        raise SystemExit(1)
    if "\n" in text or "\r" in text:
        print("error: text must be a single line", file=sys.stderr)
        raise SystemExit(1)
    if any(ord(ch) < 0x20 for ch in text):
        print("error: text must not contain control characters", file=sys.stderr)
        raise SystemExit(1)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Write the elevator line to entry.txt.")
    parser.add_argument("--out", default="/output", help="Output directory.")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    validate(TEXT)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
