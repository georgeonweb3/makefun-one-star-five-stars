#!/usr/bin/env python3
"""Entry for make.fun "One Star, Five Stars for the Food".

Writes one sentence to /output/entry.txt: a one-star review of planet
Earth written by an alien tourist that still slips in a real compliment
about the food. Gate: UTF-8 text of 1 to 200 characters, not only
whitespace. Deterministic, no network, no randomness.
"""

import os

ENTRY = (
    "One star: the locals argued with rectangles all day and chose their "
    "rulers by shouting, but the ice cream was so good I ate three before "
    "remembering I was supposed to be angry."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} characters")


if __name__ == "__main__":
    main()
