#!/usr/bin/env python3
"""Run Ren'Py lint for the current project and print output.

Usage::

    python lint.py

The script looks for a ``renpy`` executable.

- Set :data:`RENPY_PATH` below to the absolute path of the executable
  to hardcode it.
- Or set the ``RENPY`` environment variable to point to the executable
  (``renpy`` or ``renpy.sh``).
"""

import os
import shutil
import subprocess
import sys
from typing import Optional


# Absolute path to the Ren'Py executable. Leave as ``None`` to fall back to
# the RENPY environment variable or to searching ``renpy`` in ``PATH``.
RENPY_PATH: Optional[str] = "C:/Users/r.kucherenko/Downloads/renpy-8.3.4-sdk/renpy.exe"


def main() -> int:
    renpy_executable = RENPY_PATH or os.environ.get("RENPY", "renpy")
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
