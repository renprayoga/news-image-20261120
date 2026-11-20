#!/usr/bin/env python3
"""Entry point for news-image-20261120.

Copies the pre-rendered entry.png (built by draw.py) byte for byte
into MAKEFUN_OUTPUT_DIR as entry.png. Standard library only, no
network, no randomness: two runs write identical bytes.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
