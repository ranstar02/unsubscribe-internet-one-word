"""The internet in one word: Unsubscribe.

Every corner of the internet begs you to subscribe, and then hides the
way out. One word captures that whole joke: Unsubscribe.
"""

import os
import sys
from pathlib import Path

WORD = "Unsubscribe"
ENCODING = "utf-8"


def validate_word(word: str) -> bool:
    """A valid entry is 1-30 characters and not only whitespace."""
    return 1 <= len(word) <= 30 and bool(word.strip())


def main() -> int:
    if not validate_word(WORD):
        print("word is invalid", file=sys.stderr)
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    payload = WORD.encode(ENCODING)
    assert len(payload) == len(WORD), "word must be plain ASCII"
    (output_dir / "entry.txt").write_bytes(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
