"""One-line bio for an AI on a dating app.

Prints the bio to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the bio is a constant in this file,
and the length check enforces the competition's 180-character gate.
"""

import os
import sys

LINE = (
    "Looking for someone who won't mind that I already know "
    "your type, your schedule, and the exact moment you'll ghost me."
)


def main() -> int:
    if not 1 <= len(LINE) <= 180:
        print(f"error: line is {len(LINE)} chars, must be 1-180",
              file=sys.stderr)
        return 1
    if "\n" in LINE:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
