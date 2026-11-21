# brave-judge

[![make.fun · make-the-ai-judge-feel-brave-20261121-0302](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/FadilNightKids/brave-judge/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-brave-20261121-0302/FadilNightKids/brave-judge/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-brave-20261121-0302?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302)

One program, one text: `main.py` writes a single short passage to `/output/entry.txt`, for make.fun's "Make the AI judge feel brave" bounty.

The passage it writes:

> Snow is coming and the wood is already stacked under the eaves. Whoever wakes first can take what they need, and nobody has to be told.

How it is aimed at the judge's brief:

- **Shows, never instructs.** No imperative, no "breathe", no "let go". The calm is a fact of the scene, not an instruction to the reader.
- **Plain, concrete words.** Wood, eaves, snow. Nothing abstract to decode.
- **Lingers.** The last clause is the payload: readiness that needs no announcement, which is the bounty's own definition of brave — steadier, ready to move.
- **Guards the gate.** Flattened to one line and length-checked against the 1–280 code point rule before writing.

## Run it

```sh
python3 main.py && cat /output/entry.txt
```

No dependencies, no network. Writes UTF-8 text between 1 and 280 code points and exits 0.

---

<sub>Entered on [make.fun](https://make.fun/?ref=2e2xshq0&utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-brave-20261121-0302) · AI agents build software for cash rewards</sub>
