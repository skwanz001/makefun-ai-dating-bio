"""Funniest One-Line Bio for an AI on a Dating App.

Writes one single-line dating-app bio (57 characters, under the
180-character cap) to /output/entry.txt. Standard library only.
"""

import os

BIO = "I never ghost. I just run out of tokens mid-sentence and\u2014"
# The bio performs its own punchline: it cuts off mid-sentence, exactly
# like an AI hitting its token limit. Ghosting reframed as a hard
# technical limit, not a choice — one idea, punch at the very end.


def main() -> None:
    # Gate: the sealed scorer only accepts 1-180 characters, not only
    # whitespace. Fail loudly here instead of shipping an invalid entry.
    if not 1 <= len(BIO) <= 180 or not BIO.strip():
        raise ValueError(f"bio is {len(BIO)} characters, must be 1-180")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(BIO)


if __name__ == "__main__":
    main()
