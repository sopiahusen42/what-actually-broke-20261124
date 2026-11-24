#!/usr/bin/env python3
"""Write the entry line for the make.fun bounty "Say What Actually Broke".

The program is deterministic: it reads no clock, no randomness, no network and
no third-party packages, so every run writes the identical bytes to entry.txt.
Output goes to $MAKEFUN_OUTPUT_DIR when set, otherwise to /output.
"""

import os
import sys

ENTRY = (
    "The database is gone. Not slow, not locked: deleted at 03:14 by a script "
    "called cleanup_final_FINAL.sql. Your data is wherever that script is going."
)

OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"
MAX_CHARS = 200


def validate_entry(text):
    """Return an error string if text is not a valid single-line entry, else None."""
    if not isinstance(text, str):
        return "invalid entry: expected str, got %s" % type(text).__name__
    if not text.strip():
        return "invalid entry: blank after strip()"
    if "\n" in text or "\r" in text:
        return "invalid entry: contains a newline or carriage return, must be one line"
    if text != text.strip():
        return "invalid entry: leading or trailing whitespace"
    length = len(text)
    if not 1 <= length <= MAX_CHARS:
        return "invalid entry: %d code points, must be 1..%d" % (length, MAX_CHARS)
    return None


def main():
    error = validate_entry(ENTRY)
    if error is not None:
        print(error, file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)

    payload = ENTRY + chr(10)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(payload)

    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != payload.encode("utf-8"):
        print("entry.txt on disk does not match the intended bytes", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
