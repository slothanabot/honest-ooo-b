#!/usr/bin/env python3
"""make.fun entry: The Painfully Honest Out-of-Office (honest-ooo-b).

The entry is a single out-of-office auto-reply of at most 200
characters, written to /output/entry.txt. It is painfully honest
about the sender's inbox — away until Monday, and the inbox will
still be a disaster on return — and still polite enough that a
manager would let it stand: I will read yours first, I promise,
eventually. Honesty first, politeness second, and "eventually"
quietly tells the truth about the promise too.
"""

from pathlib import Path

OUT_PATH = Path("/output/entry.txt")
CHAR_LIMIT = 200


def build_entry():
    """Return the honest auto-reply, my own wording throughout."""
    # The reply survives a manager's reading because the
    # politeness is real: a return date, a promise, first
    # priority. The honesty survives because the promise is
    # undercut by one word — "eventually" — which is where the
    # line stops being a form reply and starts being true.
    return (
        "I'm away until Monday, and honestly my inbox will still "
        "be a disaster when I return \u2014 but I'll read yours "
        "first, I promise, eventually."
    )


def validate(line):
    """Raise SystemExit listing every gate problem, if there is one."""
    problems = []
    if not line.strip():
        problems.append("empty")
    if line != line.strip():
        problems.append("leading/trailing whitespace")
    if len(line) > CHAR_LIMIT:
        problems.append("too long: %d chars" % len(line))
    if "\n" in line:
        problems.append("not a single line")
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def main():
    line = build_entry()
    validate(line)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    saved = OUT_PATH.read_text(encoding="utf-8")
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT_PATH, len(saved), CHAR_LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    main()
