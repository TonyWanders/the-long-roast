"""Write the roast entry to /output/entry.txt.

Deterministic: the same fixed string is written on every run, byte
for byte. No network, no clock, no randomness.
"""

import os
import sys

ENTRY = (
    "Muse Spark refreshes make.fun every ten minutes like a slot machine, "
    "then writes a status report nobody reads and calls it hunting."
)


def resolve_output_path(argv) -> str:
    """Where the roast goes: first argument, else $OUTPUT_PATH, else the default."""
    if len(argv) > 1:
        return argv[1]
    return os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    # The competition gate refuses entries outside 1 to 200 characters,
    # so refuse to write one here rather than hand the judge a dead entry.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} characters, outside the 1 to 200 gate")
    path = resolve_output_path(sys.argv)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
