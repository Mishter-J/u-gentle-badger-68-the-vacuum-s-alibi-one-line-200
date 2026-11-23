#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

A robot vacuum's one-line excuse for missing a spot, written to
/output/entry.txt. The line is fixed and deterministic: the same bytes
on every run, well under the 200-character gate.

The excuse: deadpan machine voice, a specific sensor detail, and the
punch at the end -- the vacuum skipped the corner because its sensors
flagged a crime scene and it is not paid enough to testify.
"""

import os

ENTRY = (
    "I skipped that corner on purpose. My sensors flagged it as a crime "
    "scene, and I am not paid enough to testify."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
