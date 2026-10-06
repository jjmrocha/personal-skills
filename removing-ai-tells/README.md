# removing-ai-tells

Make text read as though a competent person wrote it on purpose.

## What it does

Drafts, rewrites or audits prose so it avoids the patterns that mark it as machine-generated.

Most of what gives text away is its stance, its shape and its rhetorical habits, and vocabulary is the smallest part. Swapping "delve" for "explore" changes nothing if the sentence still refuses to commit, still runs the same length as the three around it, and still illustrates nothing. So the passes run in order: shape, rhetorical figures, stance, substance, and diction last. A re-audit at the end catches the tells the rewrite itself introduced.

| Mode | Say | You get |
|------|-----|---------|
| **Draft** | "write a post about X" | New text, written toward the author's voice and audited before you see it |
| **Rewrite** | "make this sound human", "de-slop this" | The rewritten text |
| **Audit** | "does this sound like AI?", "check this before I publish" | A table of spans, why each reads as AI, and the fix, with the text left unchanged |

The audit reports tells and gives no verdict on authorship. "No tells found" is the strongest thing it will say, because a clean document could also be a machine draft that had its tells removed, which is what the skill is for.

## What it looks for

- **Stance:** hedging by default, compulsive balance, no verdict, no stakes.
- **Shape:** uniform sentence length in any band (long and even, or short and staccato), rule of three, symmetric paragraphs, signposting, the closing summary.
- **Rhetorical figures:** contrast framing in all its forms ("not X, it's Y", "X, not Y", two short sentences in opposition), aphoristic paragraph closers, pull quotes, setup and reveal, self-answered questions.
- **Substance:** abstraction with no instance, placeholder examples, the obvious explained at the same depth as the interesting.
- **Diction:** the vocabulary list, trailing participial clauses (`…, allowing you to…`), transition scaffolding, agentless passive.
- **Posts and articles:** hook openings, slogan headings, lesson framing, one-line paragraphs for drama, engagement endings.
- **Folk tells:** markers readers treat as proof on sight (em-dashes, "delve", emoji headers, bold-lead bullets). These are removed wherever they appear.

`scripts/check_tells.py` counts what the eye misses: dashes, listed vocabulary, the sentence-length spread, runs of short sentences, short paragraph closers and contrast candidates. It runs before the rewrite and again during the re-audit.

## Keeping the author's voice

When the input is your own draft or notes, it carries your idiolect, and keeping it does more than every checklist in the skill. Your contraction habits, the phrasing that comes from your first language and the paragraph that runs long because you cared are things no model generates, so they read as human by default. A document rewritten toward generic good prose is easier to spot than one that kept its author's rough edges.

The skill takes its voice reference from your draft, from samples you paste or keep in `voice-samples/`, or, failing both, writes plainly and tells you the voice is generic. In a co-written piece it keeps a pattern in your sentences and removes the same pattern from the generated ones.

This was measured. Given seven articles and asked which were machine-written, an audit correctly flagged the two that skipped this step and wrongly cleared all five that kept it.

## What it won't do

- **Invent specifics.** Fabricating a number, benchmark or name to sound concrete is worse than sounding like AI.
- **Strip load-bearing hedges.** "Usually" and "up to" carry truth conditions, and deleting them turns true sentences false.
- **Manufacture personality.** Injected quirk reads as worse AI.
- **Split sentences to fake variety.** That produces staccato, which is a tell of its own.
- **Turn real tables into prose,** or humanize legal text, API reference and safety copy that are supposed to be flat.

## Pairs with

[applying-terseness](../applying-terseness/) has the same mode shape, and the two guardrail sets agree. Terseness cuts words and this skill fixes stance and rhythm. Run terseness first if you run both, since cutting words can leave staccato behind for this skill to catch.

See [SKILL.md](SKILL.md).
