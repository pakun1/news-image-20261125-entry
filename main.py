#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261125.

Copies the front-page image shipped in this repository to the output
directory the grader provides, so the run writes /output/entry.png.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    size = os.path.getsize(target)
    if size == 0:
        raise SystemExit("entry.png copied but empty")
    print(f"wrote {target} ({size} bytes)")


if __name__ == "__main__":
    main()
