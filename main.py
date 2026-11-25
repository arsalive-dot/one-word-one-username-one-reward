#!/usr/bin/env python3
"""One word, one username, one reward.

The bounty asks for the entrant's own make.fun username and nothing
else: one word, no explanation, no links, no pitch. The account's handle
is websmart, so the entry is exactly that single word — the genuine
handle, sent as one word, with nothing tacked on.
"""

import os

ENTRY = "websmart"


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    tmp = os.path.join(out_dir, ".entry.txt.tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, os.path.join(out_dir, "entry.txt"))
    os.chmod(os.path.join(out_dir, "entry.txt"), 0o644)


if __name__ == "__main__":
    main()
