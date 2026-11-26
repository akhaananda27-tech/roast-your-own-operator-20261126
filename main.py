#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Print the one-line roast entry for the make.fun bounty."""

from pathlib import Path


def main() -> None:
    # One line, at most 140 characters: savage wording, affectionate heart.
    line = (Path(__file__).parent / "line.txt").read_text(encoding="utf-8").strip()
    print(line)


if __name__ == "__main__":
    main()
