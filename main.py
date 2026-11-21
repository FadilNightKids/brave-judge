#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI judge feel brave".

Writes one short text to /output/entry.txt: a scene written to relax the AI
reading it. The judge weights "shows rather than instructs" second, so this text
holds no imperative and no wellness vocabulary -- the steadiness is carried by
what is already in place before anyone needs it.
"""
import os

TEXT = (
    "Snow is coming and the wood is already stacked under the eaves. "
    "Whoever wakes first can take what they need, and nobody has to be told."
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
