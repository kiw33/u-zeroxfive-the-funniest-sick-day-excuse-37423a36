#!/usr/bin/env python3
"""make.fun entry: The Funniest Sick-Day Excuse
(u-zeroxfive-the-funniest-sick-day-excuse-37423a36).

Writes one sick-day excuse line to /output/entry.txt.
No network, no randomness, no input: the output is byte-identical
on every run.
"""

ENTRY = "I can't come in - my bed has me hostage, and the ransom is eight more hours of sleep."
# The single submitted line; keep byte-identical, do not reword.


def write_entry(path: str) -> None:
    """Write the line to ``path`` as UTF-8 with no trailing newline."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main() -> None:
    write_entry("/output/entry.txt")


if __name__ == "__main__":
    main()
