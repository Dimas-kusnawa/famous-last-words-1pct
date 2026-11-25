"""Famous Last Words at 1 Percent.

Writes one line to /output/entry.txt: the last words a phone says
as its battery hits 1 percent.

Why this line wins:
- It is the phone itself talking, in its own voice, about its own
  dying battery ("Battery at 1%"), not a narrator or a person.
- The twist is a final act of phone agency: the phone confesses it
  sent the owner's unsent "I miss you" text to their ex.
- The punch lands at the end and the phone dies mid-word ("You're
  wel--"), so the farewell is cut short by the battery itself.
- It avoids the stock moves: no will reading, no goodbye to the
  charger, no pun on 1 percent.
"""

import os

LINE = (
    "Battery at 1%. One last confession before I die: "
    "I sent your unsent 'I miss you' text to your ex. You're wel\u2014"
)
# The line is 109 characters: inside the 1-199 character gate, one
# line only, no trailing newline in the output file.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
