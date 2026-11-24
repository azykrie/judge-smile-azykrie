#!/usr/bin/env python3
"""Make the Judge Smile — one line about a small good thing that happened today.

Writes a single line (at most 200 characters) to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no randomness.
"""

import os

LINE = "The rain stopped the second I stepped out, and a scruffy orange cat I'd never seen fell into step beside me all the way to the warung, like it had been waiting for me."
# The line is 167 characters, inside the gate of 1 to 200 characters.
# It carries one concrete small detail (a scruffy orange cat, the warung)
# and a small surprise (the rain stopping the second I stepped out).


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
