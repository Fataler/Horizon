#!/usr/bin/env python3
"""Run Ren'Py lint for the current project.

Usage: python lint.py

Setup:
1. Set RENPY env var: export RENPY=/path/to/renpy.sh
2. Or set RENPY_PATH below
3. Or add renpy.sh to PATH:

   Windows (CMD):
   set PATH=%PATH%;C:\\Path\\To\\RenPy\\SDK

   Windows (PowerShell):
   $env:Path += ";C:\\Path\\To\\RenPy\\SDK"

   macOS/Linux:
   echo 'export PATH="/path/to/renpy-8.x.x-sdk:$PATH"' >> ~/.zshrc
   source ~/.zshrc

   macOS temp session:
   export PATH="/path/to/renpy-8.x.x-sdk:$PATH"
"""

import os
import shutil
import subprocess
import sys
from typing import Optional


# Fallback if RENPY env var not set
# RENPY_PATH = "/path/to/renpy.sh"
RENPY_PATH: Optional[str] = None


def main() -> int:
    renpy_executable = os.environ.get("RENPY") or RENPY_PATH or "renpy"
    if shutil.which(renpy_executable) is None:
        print(
            f"Ren'Py executable '{renpy_executable}' not found. Set RENPY_PATH "
            "constant or the RENPY environment variable to its location.",
            file=sys.stderr,
        )
        return 1

    project_dir = os.path.dirname(os.path.abspath(__file__))

    process = subprocess.run(
        [renpy_executable, project_dir, "lint"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    print(process.stdout)
    if process.stderr:
        print(process.stderr, file=sys.stderr)

    return process.returncode


if __name__ == "__main__":
    raise SystemExit(main())
