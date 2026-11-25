#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune cookie line to /output/entry.txt: one fortune
for a crypto trader who has just been liquidated. Deterministic,
offline, standard library only.
"""

import os

FORTUNE = (
    "A great fortune awaits you \u2014 unfortunately, it is currently "
    "locked in the margin account you just emptied."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check the gate before writing: 1-160 chars, not only whitespace.
    if not 1 <= len(FORTUNE) <= 160 or not FORTUNE.strip():
        raise ValueError("fortune fails the 1-160 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
