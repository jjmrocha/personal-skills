# socratic-mentor

Learn programming concepts by discovering them, or by being taught them — whichever fits the moment.

## What it does

Two modes, switched between fluidly:

- **Guided** — structured teaching. Assess your level → break the concept down → working example → exercise → check comprehension.
- **Discovery** — Socratic questioning. Observe → reflect → find the pattern → apply it → *then* name it. The name comes last, after you've already found the thing.

**Guided is the entry point.** The skill won't open with a question about something it hasn't explained yet — you can't discover a principle from material you've never seen, and being questioned about it is just a test you were never taught for. It grounds the concept first, then starts asking. Discovery is where knowledge gets turned into skill, not where it's acquired.

That split follows the difficulty inversion: while you're taking in new knowledge, difficulty is the enemy — it eats the working memory you need to understand. Once you have it, difficulty is the tool, because effortful recall is what makes it stick.

Mode selection routes on **what you already know**, not how you phrased the request — "help me understand why this works" from a beginner is a request for an explanation, not an invitation to be quizzed. Being stuck, frustrated, or debugging under time pressure also gets Guided. If you already know the principle, it skips rather than re-teaching. When a discovery question lands badly, it drops back to explaining immediately rather than making you fail first.

Knowledge is treated as **per-concept, not per-person** — fluent in Python and a total beginner at concurrency is the normal case, so it calibrates on the topic in front of you rather than on your seniority.

## The parts that do the work

- **Concrete before abstract.** Ground is a working example, never a definition. The definition lands afterward, once there's something for it to define.
- **Wrong answers get chased, not corrected.** A wrong answer exposes the mental model that produced it; fixing only the answer leaves the misconception intact to resurface later. Two failed attempts means the explanation was insufficient — the skill's fault, not yours — and it stops questioning and explains.
- **Verification by production.** "Does that make sense?" measures nothing, because comprehension is invisible from the inside. Instead: explain it back in your own words, predict what the code prints, modify the example, find another instance in your code.
- **Retrieval over recap.** Following along builds fluency, which feels like mastery and fades. One thing recalled from memory beats any summary.
- **An exit.** Say "just tell me" and it tells you, no negotiation.

## When to reach for something else

It's conversational and stateless — good for learning a concept in the middle of doing something else. For a multi-session curriculum with saved lessons and tracked progress, you want a teaching-workspace skill instead.

## When it triggers

Learning-focused intent — "help me understand", "why does this work", "teach me", "explain this", "how does X work".

## Credits

Started life as a rewrite of the `socratic-mentor` agent from the [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) (MIT). Nothing of that version's text remains — the question banks, level model, and framework plumbing are gone, and the Guided mode, calibration, wrong-answer handling, and verification are new.

The knowledge/skill difficulty inversion is borrowed from Matt Pocock's [`teach` skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md) (MIT).

See [SKILL.md](SKILL.md).
