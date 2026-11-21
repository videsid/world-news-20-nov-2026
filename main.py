#!/usr/bin/env python3
"""Entry for the make.fun bounty "Sum up 20 November's world news in one image".

The entry image (image.jpg, 1024x1024, under 1 MiB) was produced by an AI
agent from a verified news brief for 20 November 2026: the overnight
strikes on Kyiv, the Poland airspace breach, the delayed Iran decision in
Washington, Houthi missiles on Riyadh, the COP31 deadlock in Antalya, and
GTA VI's record-breaking launch.

This program is intentionally deterministic and offline: it copies the
bundled image to output.jpg. Running it twice produces identical bytes,
as the bounty rules require. Python 3.13, standard library only.
"""

import hashlib
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "image.jpg"
OUTPUT = HERE / "output.jpg"


def main() -> int:
    if not SOURCE.is_file():
        print("image.jpg is missing from the repo root.", file=sys.stderr)
        return 1
    shutil.copyfile(SOURCE, OUTPUT)
    digest = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
    print(f"Wrote {OUTPUT.name} ({OUTPUT.stat().st_size} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
