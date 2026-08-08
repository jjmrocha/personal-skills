# removing-ai-tells

Make text read as though a competent person wrote it on purpose.

## What it does

Rewrites or audits prose to remove the patterns that mark it as machine-generated.

The premise is that **the tell is stance and shape, not vocabulary**. Swapping "delve" for "explore" changes nothing if the sentence still refuses to commit, still runs 22 words like the three around it, and still illustrates nothing. Word lists are a symptom check — fast, useful, never sufficient. So the passes run in order: shape, then stance, then substance, then diction last.

| Mode | Say | You get |
|------|-----|---------|
| **Rewrite** | "make this sound human", "de-slop this" | The rewritten text |
| **Audit** | "does this sound like AI?", "flag the tells" | A table of spans → why it reads as AI → fix, no rewrite |

The audit reports tells, never authorship. "No tells found" is the strongest thing it will say, because a clean document is equally consistent with a machine draft that had its tells removed. That is what the skill is for.

## What it looks for

Grouped by what's actually wrong, not by keyword:

- **Stance** — hedging by default, compulsive balance, no verdict, no stakes.
- **Shape** — uniform sentence length (the loudest tell there is), rule of three everywhere, symmetric paragraphs, restating the question, signposting, the closing summary that repeats what you just read.
- **Substance** — abstraction with no instance, placeholder examples, the obvious explained at the same depth as the interesting.
- **Diction** — the vocabulary list, "it's not just X, it's Y", trailing participial clauses (`…, allowing you to…`), transition scaffolding, agentless passive.
- **Formatting** — over-bolding, over-structuring (a heading every two paragraphs, a table for two facts).
- **Folk tells** — markers the public reads as proof on sight, regardless of rate: em-dashes, "delve", "it's not just X, it's Y", emoji headers, bold-lead bullets. These get removed by presence, not by frequency.

## The part that actually works

When the input is your own draft or notes, it carries your idiolect, and **keeping it is worth more than every checklist above**. Your contraction habits, the phrasing that comes from your first language, the paragraph that runs long because you cared. No model generates those, so they read as human by default.

The failure mode is polishing them away. Smoothness is the tell: a document rewritten toward generic good prose is more detectable than one that kept its author's rough edges, even when the rough version scores worse on every tell in the list.

This was measured, not assumed. Given seven articles and asked which were machine-written, an audit correctly flagged the two that skipped this step and wrongly cleared all five that kept it.

## What it won't do

The guardrails matter more than the checklist:

- **Never invents specifics.** Fabricating a number, benchmark, or name to sound concrete is worse than sounding like AI. No real instance available? The claim gets cut or stays general.
- **Keeps load-bearing hedges.** "Usually" and "up to" carry truth conditions. Reflexive hedging is a tell; accurate hedging is accuracy, and stripping it turns true sentences false.
- **Doesn't manufacture personality.** Injected quirk reads as worse AI, not less.
- **Doesn't prose-ify real tables.** Structure isn't a tell when the content is genuinely tabular.
- **Respects register.** Legal text, API reference, and safety copy are supposed to be flat.

Em-dashes get a specific ruling, and it's the strict one: gone on sight in public writing. They're legitimate punctuation and the statistical case for them is fine, but that argument happens in your absence. Readers don't measure rates — they see one and decide. A comma, colon, parenthesis, or full stop covers every case.

## Pairs with

[applying-terseness](../applying-terseness/) — same two-mode shape, and the two guardrail sets agree. Terseness cuts words; this fixes stance and rhythm. Run terseness second if you run both.

See [SKILL.md](SKILL.md).
