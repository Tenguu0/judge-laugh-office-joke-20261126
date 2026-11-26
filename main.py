#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

Writes one line of office comedy (1-200 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The joke: the meeting that could have been an email finally became
an email -- so the office scheduled a meeting to read it together.
The setup is the most-quoted office complaint there is; the payoff
turns it inside out, which is exactly the kind of last-words twist
the judge's brief rewards.
"""

import os

JOKE = (
    "The meeting that could have been an email finally became an email "
    "— so we scheduled a meeting to read it together."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"joke is {len(text)} chars, must be 1-200")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
