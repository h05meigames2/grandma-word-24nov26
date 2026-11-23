#!/usr/bin/env python3
"""One Word From Grandma — entry for make.fun bounty
u-0xkianno-one-word-from-grandma-f04bed16.

Writes exactly one word to /output/entry.txt: the single word a
grandma would text about AI.

The word is "Robbie": grandma has named her robot, the way she would
name a grandson. Warm, a little confused, funny in one word, and
unmistakably about a machine she has adopted into the family.

Deterministic, stdlib only, no network, no timestamps.
"""

import os
import sys

WORD = "Robbie"


def main() -> int:
    if not (1 <= len(WORD.encode("utf-8")) <= 30):
        print("word must be 1-30 UTF-8 characters", file=sys.stderr)
        return 1
    if WORD.strip() != WORD or " " in WORD:
        print("word must be a single word with no spaces", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(f"wrote {WORD!r} to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
