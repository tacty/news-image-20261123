#!/usr/bin/env python3
"""make.fun entry — "Sum up 23 November's world news in one image".

Writes the bundled front-page image to /output/entry.png.
No network access, no randomness, no clock: every run writes
exactly the same bytes.
"""

import filecmp
import shutil
from pathlib import Path


def main() -> None:
    here = Path(__file__).resolve().parent
    src = here / "image.png"
    if not src.is_file():
        # The image may have been uploaded under a different name
        # (e.g. a phone photo name); take the bundled PNG either way.
        pngs = sorted(here.glob("*.png"))
        if len(pngs) == 1:
            src = pngs[0]
    if not src.is_file():
        raise SystemExit(f"bundled image not found: {src}")
    dst = Path("/output/entry.png")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    if not filecmp.cmp(src, dst, shallow=False):
        raise SystemExit("written file does not match the bundled image")
    print(f"wrote {dst} ({dst.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
