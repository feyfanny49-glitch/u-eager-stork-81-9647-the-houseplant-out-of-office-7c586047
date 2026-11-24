#!/usr/bin/env python3
"""The Houseplant Out-of-Office: write one judged text to /output/entry.txt.

Deterministic, stdlib-only, no network. The whole entry is the constant below.
The local gate is checked before writing: valid UTF-8, 1..120 characters,
non-whitespace, no trailing newline. The file is replaced atomically.
"""

import hashlib
import os
import tempfile

ENTRY = (
    "Out of office. Last watered under the previous administration. "
    "For urgent matters, contact the moss."
)

MAX_CHARS = 120


def encode_entry(text: str) -> bytes:
    """Apply the house gate locally and return the exact bytes to write."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1..{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    payload = text.encode("utf-8", errors="strict")
    if payload.endswith(b"\n") or payload.endswith(b"\r"):
        raise ValueError("entry must not end with a newline")
    return payload


def main() -> None:
    payload = encode_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")

    fd, tmp = tempfile.mkstemp(prefix=".entry-", dir=out_dir)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, target)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise

    print(
        f"entry.txt: {len(ENTRY)} chars, {len(payload)} bytes, "
        f"sha256 {hashlib.sha256(payload).hexdigest()}, {target}"
    )


if __name__ == "__main__":
    main()
