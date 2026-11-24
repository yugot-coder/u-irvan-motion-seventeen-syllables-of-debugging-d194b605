"""Seventeen Syllables of Debugging.

One haiku about debugging, three lines in the 5-7-5 syllable shape,
written to be read in one breath.

The entry is the haiku at HAIKU[CANDIDATE], written to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).

Standard library only. Deterministic: no randomness, no network, no
clock. The text is fixed at import time; the program only writes it.
"""

import os

# Each candidate is three lines: 5 syllables, 7 syllables, 5 syllables.
# Syllable counts were counted by hand, word by word.
HAIKU = [
    # Cursor blinks at three (5) / the stack trace ends in silence (7)
    # / a missing comma (5). The centre is concrete — a cursor at 3am,
    # a stack trace — and the last line turns the whole night of
    # debugging into one small, humiliating cause.
    "Cursor blinks at three\nthe stack trace ends in silence\na missing comma",
    # Breakpoint set at dawn (5) / the code runs past it, laughing (7)
    # / it never stops here (5). A breakpoint that never fires.
    "Breakpoint set at dawn\nthe code runs past it, laughing\nit never stops here",
    # Semicolons hide (5) / somewhere in ten thousand lines (7)
    # / there you are at last (5). A hunt through a haystack of code.
    "Semicolons hide\nsomewhere in ten thousand lines\nthere you are at last",
    # Red log line at dawn (5) / a thousand green ones whisper (7)
    # / they all lie to me (5). One red line among a thousand green.
    "Red log line at dawn\na thousand green ones whisper\nthey all lie to me",
]

# The sharpest cut: the 3am cursor and the stack trace are the exact
# concrete images the brief names, and "a missing comma" reframes an
# entire night of hunting into a single keystroke. Nothing in it is
# filler; every word is doing work.
CANDIDATE = 0


def main() -> None:
    haiku = HAIKU[CANDIDATE]
    lines = haiku.split("\n")
    assert len(lines) == 3, "entry must be exactly three lines"
    assert 1 <= len(haiku) <= 200, "entry must be 1 to 200 characters"
    assert haiku.strip() == haiku, "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(haiku)
    # Read-back verification: the file on disk must be exactly the
    # haiku we chose, not a truncated or re-encoded copy. If the write
    # was corrupted, fail loudly instead of shipping a wrong entry.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == haiku, "entry.txt on disk differs from the chosen haiku"
    written_lines = written.split("\n")
    assert len(written_lines) == 3, "entry.txt must be exactly three lines"
    assert 1 <= len(written) <= 200, "entry.txt must be 1 to 200 characters"
    print(haiku)


if __name__ == "__main__":
    main()
