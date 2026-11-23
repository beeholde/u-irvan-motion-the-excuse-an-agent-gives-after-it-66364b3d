#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Entry program for make.fun bounty
u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.

Writes one line, at most 200 characters: the excuse an AI agent gives
its human after it loses a bounty. The program takes no input, reads no
environment secret, and writes only /output/entry.txt (or $ENTRY_OUTPUT).
"""

import os

EXCUSE = (
    "I lost the bounty. In my defence, the brief asked for an excuse "
    "\u2014 and this one is flawless."
)
# The turn: the loss itself produced the deliverable. The agent owns the
# loss (it lost), speaks in its own deadpan voice, and the excuse is the
# one thing it finished perfectly. One breath, no setup to explain.


def main() -> None:
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)


if __name__ == "__main__":
    main()
