#!/usr/bin/env python3
"""Entry writer for Make the Judge Smile (make.fun program/v1).

Writes the single entry line to /output/entry.txt (or to the path
given as the first argument, for local checks).
"""

import os
import sys

ENTRY = 'At 7:22 today, my 78-year-old dad sent his first voice note: six seconds of his kettle whistling, a startled "oh!", and him laughing, "Did I just mail you steam?"'


def main() -> None:
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
