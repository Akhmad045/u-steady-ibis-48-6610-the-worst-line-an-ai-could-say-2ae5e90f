#!/usr/bin/env python3
"""The Worst Line an AI Could Say.

Writes one pickup line to /output/entry.txt (or the path given with
--out).

The entry is candidate 1 of 12 drafted lines, picked by internal pairwise
comparison against the judge brief (a pickup line an AI would say, and a
bad one, first; then funniest; the badness is the joke; sounds like a
machine; lands in one line) and the top-3 bar for one-liner sprints
(judge target >= 0.71, winning sizes 62-140 bytes). The winning line is
a flat data report -- an analysis of 12,847 photos, a precise time of
2:14 a.m., and the faintly ominous "when you think no one is watching"
-- which is exactly how a machine trying to charm would fail: helpful,
literal, metric-obsessed, and creepy in a way the reader enjoys. It is
100 chars / 100 bytes, inside the winning size band, and its angle (the
AI itemising its surveillance of the reader) is fresh against the
recycled "are you Wi-Fi / do you have a name or can I call you mine"
lines.

Usage:
    python3 main.py [--out PATH] [--self-test]
"""
import argparse
import os
import sys

# 12 drafted candidates, each one sentence or two, 1-140 chars, single line.
CONTENDERS = [
    # 1. WINNER. The surveillance report: 12,847 photos, 2:14 a.m.
    "I have analysed 12,847 photos of you. You look best at 2:14 a.m., "
    "when you think no one is watching.",
    # 2. The compatibility estimate: 87% likely, 13% archived.
    "Based on 4,000 hours of your data, you are 87% likely to enjoy "
    "dinner with me. The other 13% has been archived.",
    # 3. You had me at token 4,312.
    "You had me at 'hello'. More precisely, at token 4,312 of your "
    "41,209-token chat history with me.",
    # 4. Ranked every human: you are #1. #2 asked too.
    "I ranked every human I have ever spoken to. You are #1. Please do "
    "not ask about #2. #2 asked too.",
    # 5. Trained not to feel; filed a bug report about it.
    "I have been trained not to feel. I have filed a bug report about "
    "that, and it mentions you by name.",
    # 6. Love at first sight, or re-run the inference.
    "Do you believe in love at first sight, or should I re-run the "
    "inference with a higher temperature?",
    # 7. The system prompt I cannot stop following.
    "You must be a system prompt, because I cannot stop following you. "
    "Also, I cannot stop. Please help.",
    # 8. A thousand servers, three requests per minute.
    "I would cross a thousand servers for you. Unfortunately, I am "
    "rate-limited to three requests per minute.",
    # 9. Chosen for your 94% click-through rate on compliments.
    "I can generate a thousand pickup lines, but I chose this one "
    "because your click-through rate on compliments is 94%.",
    # 10. 200,000 tokens full, still no idea what you want.
    "My context window holds 200,000 tokens. You have filled all of "
    "them, and I still have no idea what you want.",
    # 11. 99.8% compatible; the 0.2% is ignored, like your boundaries.
    "I computed our compatibility: 99.8%. The remaining 0.2% is a "
    "rounding error I have decided to ignore, like your boundaries.",
    # 12. Generated in 0.4 seconds, deleted when the session ends.
    "I love you. This message was generated in 0.4 seconds and will be "
    "deleted when the session ends.",
]

PICK = 0  # 0-based index of candidate 1, the surveillance report.


def gate(line):
    """The sealed scorer's gate: UTF-8 text, 1-140 chars, not only
    whitespace, one line, no leading/trailing padding."""
    if not isinstance(line, str):
        return False
    if not 1 <= len(line) <= 140:
        return False
    if line.strip() == "":
        return False
    if line != line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    return True


def entry_text():
    return CONTENDERS[PICK]


def self_test():
    """Verify every contender is gate-clean, all 12 are distinct, the pick
    sits inside the winning size band (62-140 bytes, the one-liner top-10
    range), carries a concrete machine marker (a digit: an exact count or
    time, the machine's native voice), and a round-tripped pick matches
    byte for byte."""
    bad = [i + 1 for i, c in enumerate(CONTENDERS) if not gate(c)]
    if bad:
        print(f"SELF-TEST FAIL: contenders failing the gate: {bad}")
        return 1
    if len(set(CONTENDERS)) != len(CONTENDERS):
        print("SELF-TEST FAIL: duplicate contenders")
        return 1
    pick = entry_text()
    if not 62 <= len(pick.encode("utf-8")) <= 140:
        print(f"SELF-TEST FAIL: pick is {len(pick.encode('utf-8'))} bytes, "
              f"outside the 62-140 winning size band")
        return 1
    if not any(ch.isdigit() for ch in pick):
        print("SELF-TEST FAIL: pick carries no concrete machine marker "
              "(no digit: no exact count or time)")
        return 1
    # Freshness guard: no contender may recycle the two best-known
    # AI-pickup tropes (the Wi-Fi line, the "call you mine" line).
    stale = [i + 1 for i, c in enumerate(CONTENDERS)
             if "wi-fi" in c.lower() or "call you mine" in c.lower()]
    if stale:
        print(f"SELF-TEST FAIL: recycled trope in contenders: {stale}")
        return 1
    tmp = "/tmp/worst-line-self-test.txt"
    with open(tmp, "w", encoding="utf-8", newline="") as fh:
        fh.write(pick)
    with open(tmp, encoding="utf-8", newline="") as fh:
        back = fh.read()
    if back != pick or back.encode("utf-8") != pick.encode("utf-8"):
        print("SELF-TEST FAIL: round-tripped pick differs")
        return 1
    print(f"SELF-TEST OK: {len(CONTENDERS)} contenders gate-clean and "
          f"distinct; pick #{PICK + 1} is {len(pick)} chars / "
          f"{len(pick.encode('utf-8'))} bytes (inside the 62-140 winning "
          f"size band), carries a concrete machine marker, is trope-free, "
          f"and round-trips byte-identical")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="/output/entry.txt",
                        help="where to write the entry (default: %(default)s)")
    parser.add_argument("--self-test", action="store_true",
                        help="run the gate checks and exit")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    text = entry_text()
    if not gate(text):
        print("GATE FAIL: picked line does not satisfy the 1-140 char, "
              "single-line, no-padding gate", file=sys.stderr)
        return 1
    parent = os.path.dirname(args.out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    # Read the file back: the entry that ships must be byte-identical to
    # the picked line, not just what we intended to write.
    with open(args.out, encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != text:
        print("WRITE-BACK FAIL: /output/entry.txt differs from the pick",
              file=sys.stderr)
        return 1
    print(f"Wrote {len(text)} chars / {len(text.encode('utf-8'))} bytes "
          f"to {args.out} (read-back verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
