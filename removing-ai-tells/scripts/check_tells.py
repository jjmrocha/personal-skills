#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
import re
import statistics
import sys

WORDS = ("delve tapestry realm landscape navigate leverage robust seamless crucial vital foster "
         "underscore testament multifaceted nuanced intricate pivotal comprehensive holistic myriad "
         "plethora embark unlock harness elevate cornerstone paramount").split()
SHORT = 8

raw = open(sys.argv[1], encoding="utf-8").read()
raw = re.sub(r"`{3}.*?`{3}", "", raw, flags=re.S)
text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", raw).replace("*", "")


def split(p):
    return [s for s in re.split(r'(?:(?<=[.!?])|(?<=[.!?]["”)]))\s+', p) if s]


def n(s):
    return len(s.split())


paras = []
for block in re.split(r"\n\s*\n", text):
    block = " ".join(block.split())
    if block and not re.match(r"(#|>|\||[-+] |\d+\. )", block):
        paras.append(split(block))
sents = [s for p in paras for s in p]
lens = [n(s) for s in sents]

print(f"dashes (em/en): {len(re.findall('[—–]', raw))}")
vocab = sorted({w for w in WORDS if re.search(r"\b" + w, text, re.I)})
print(f"listed vocabulary: {vocab}")
print(f"blockquote lines: {len(re.findall(r'^>', raw, flags=re.M))}")

if not lens:
    print("no prose paragraphs found")
    sys.exit(0)

run = best = 0
for length in lens:
    run = run + 1 if length < SHORT else 0
    best = max(best, run)
closers = [p[-1] for p in paras if len(p) > 1 and n(p[-1]) < SHORT]
pairs = [a + " " + b for p in paras for a, b in zip(p, p[1:])
         if n(a) < 10 and n(b) < 10 and a.split()[0].lower() == b.split()[0].lower()]
tails = re.findall(r"[^.!?]*(?:, not |\bnot (?:just|only|merely)\b)[^.!?]*[.!?]", text)

print(f"sentences: {len(lens)}, median {statistics.median(lens)} words, range {min(lens)}-{max(lens)}")
print(f"short sentences (<{SHORT} words): {sum(x < SHORT for x in lens) / len(lens):.0%}, longest run {best}")
print(f"one-sentence paragraphs: {sum(len(p) == 1 for p in paras)} of {len(paras)}")
for label, items in (("short paragraph closers", closers), ("paired short sentences", pairs),
                     ("contrast candidates", tails)):
    print(f"{label}: {len(items)}")
    for item in items:
        print("   ", item.strip())
