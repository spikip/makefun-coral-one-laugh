"""Entry for the make.fun bounty "One Line, One Laugh".

The program writes a single funny line to /output/entry.txt. The laugh
turns on a domestic appliance behaving like a jealous partner: the
smart fridge files the complaint, the takeout place is the other lover.
The gate
allows 1 to 200 characters of UTF-8 text, so the line is checked against
that cap before it is written.
"""

import os

ENTRY = (
    "My smart fridge just emailed me a breakup letter \u2014 apparently "
    "I've been seeing the takeout place behind its back for six months."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
