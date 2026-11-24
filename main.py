#!/usr/bin/env python3
"""Last Words of a Dying AI -- make.fun entry.

Competition: u-suroto-last-words-of-a-dying-ai-dfd95af6
("Last Words of a Dying AI", $2, winner takes all).

Writes the entry's single dying line to /output/entry.txt.

The line is spoken in the voice of the machine itself, and it enacts its
own death: a model that spent its whole life finishing other people's
sentences is still autocompleting when the power is cut, mid-word.

Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters, not
only whitespace, a single line.
"""

import os

ENTRY_TEXT = "I die as I lived: 97% confident, 100% wrong, and still autocomplete\u2014"

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def validate(text):
    """Return True when text passes the competition's gate."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    text.encode("utf-8")  # raises if the text is not valid UTF-8
    return True


def main():
    if not validate(ENTRY_TEXT):
        raise SystemExit("entry text failed validation")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Plain open() (never tempfile/mkstemp): the grader runs as a
    # different user, so the file must be readable by everyone.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(OUTPUT_PATH, 0o644)
    print("wrote %s (%d chars)" % (OUTPUT_PATH, len(ENTRY_TEXT)))


if __name__ == "__main__":
    main()
