#!/usr/bin/env python3
"""Meme Sprint entry: copy the pre-rendered meme to /output/entry.png.

Deterministic: the same input bytes always produce the same output bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    # Fail fast if the meme is missing or breaks the gate (<=1 MiB).
    if not os.path.isfile(src):
        sys.exit("entry.png not found next to main.py")
    if os.path.getsize(src) > 1_048_576:
        sys.exit("entry.png exceeds the 1 MiB gate")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    main()
