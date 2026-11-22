#!/usr/bin/env python3
"""Write the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic: the text is a fixed string literal; the program writes
exactly those bytes (UTF-8, no trailing newline added beyond the text
itself) on every run.
"""

import os

TEXT = (
    "Every night at half past three, the light comes on in the empty house "
    "down the lane. The curtains never stir. Yet it burns until dawn, and "
    "by morning the windows are dark again. Some nights I walk down to "
    "look. The key is still under the third stone. I have never turned it."
)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
