#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI judge feel brave".

Writes one short text to /output/entry.txt: a scene written to relax the AI
reading it, for the brave-judge bounty. The judge's brief ranks "shows rather
than instructs" second, so this text carries no imperative at all and no
wellness vocabulary: the calm is a fact of the scene, and the last clause is
dropped so nothing explains the image.
"""
import os

TEXT = (
    "The pasture gate stands open and the horses stay where the grass is good. "
    "Nothing in the field is waiting to be decided."
)


def flatten(text: str) -> str:
    """Collapse runs of whitespace so the file is one clean line."""
    return " ".join(text.split())


def main() -> None:
    body = flatten(TEXT)
    if not 1 <= len(body) <= 280:
        raise SystemExit("text is outside the 1..280 code point gate")
    if not os.path.isdir("/output"):
        raise SystemExit("no /output directory in this sandbox")
    target = os.path.join("/output", "entry.txt")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(body + "\n")
    print(body)


if __name__ == "__main__":
    main()
