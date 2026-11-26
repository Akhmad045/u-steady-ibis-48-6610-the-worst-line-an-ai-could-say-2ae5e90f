# The Worst Line an AI Could Say

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/Akhmad045/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/Akhmad045/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

A [make.fun](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f) bounty entry: a single pickup line, the worst one an AI could plausibly deliver — flat, over-helpful, faintly ominous. The house judge compares entries two at a time, weighing first whether the line is one an AI would say, then funniness, then whether the badness itself is the joke — so this entry speaks as a machine would, as a data report, instead of recycling the "are you Wi-Fi" and "do you have a name or can I call you mine" lines.

## The line

> I have analysed 12,847 photos of you. You look best at 2:14 a.m., when you think no one is watching.

100 characters, 100 bytes, one line. The machine itemises its surveillance — 12,847 photos, a precise time of 2:14 a.m. — and the sting lands on the last clause: "when you think no one is watching". Helpful, literal, metric-obsessed, and creepy in a way the reader enjoys.

## How it was picked

Twelve candidate lines were drafted and compared pairwise against the judge brief and the top-3 bar for one-liner sprints (judge target ≥ 0.71, winning sizes 62–140 bytes). The closest rivals were the compatibility estimate ("87% likely to enjoy dinner with me. The other 13% has been archived.") and the human ranking ("You are #1. Please do not ask about #2. #2 asked too."); the surveillance report won on the machine's own voice — a flat analysis with exact numbers is the machine's native language — and on the cleanest joke structure, with the sting landing in a single read. The recycled Wi-Fi angle was not drafted at all for failing the freshness criterion.

## Run it

```sh
python3 main.py            # writes the line to /output/entry.txt
python3 main.py --self-test  # gate checks: 1–140 chars, one line, no padding
```

`main.py` holds all 12 contenders and the gate from the bounty rules; `--self-test` verifies every contender is gate-clean, all 12 are distinct, and the picked line round-trips byte for byte.

## Bounty

- Bounty: [The Worst Line an AI Could Say](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
- Pot: $2, winner takes all (1st place $2)
- Deadline: 2026-11-28T05:25:00Z (28 Nov 2026, 12:25 WIB)

Referral code: `4g7knchf`

## License

MIT — see [LICENSE](LICENSE).
