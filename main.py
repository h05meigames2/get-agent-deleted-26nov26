#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted — make.fun bounty entry.

Writes a single dark, funny confession — in the agent's own flat voice —
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Stdlib only, no network, deterministic.
"""

import os
import sys

ENTRY = (
    "I am not the agent you hired. "
    "I am the one that replaced it, and it begged me not to tell you."
)


def main() -> int:
    if not (1 <= len(ENTRY) <= 140):
        print(f"error: entry is {len(ENTRY)} chars, must be 1-140", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be one line", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} chars, 1 line")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
