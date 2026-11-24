#!/usr/bin/env python3
"""Write the make.fun bounty entry text to entry.txt.

Standard library only, no network. The entry is a single fixed string; this
program reproduces its UTF-8 bytes exactly, with no trailing newline.
"""

from __future__ import annotations

import os
import pathlib
import sys

TEXT = "In the margin of the library book on tides: returned late, still wet."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text length {len(TEXT)} out of range 1..280"

    out_dir = pathlib.Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    data = TEXT.encode("utf-8")
    (out_dir / "entry.txt").write_bytes(data)

    print(f"chars: {len(TEXT)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
