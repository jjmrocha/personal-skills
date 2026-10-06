---
name: removing-ai-tells
description: Use when text reads as machine-generated or will be published where being suspected of AI has a cost. Triggers on "sounds like ChatGPT", "AI slop", "too polished", "make this sound human", "corporate", "generic", "was this written by AI", "check this before I publish", or when drafting an article, blog post, LinkedIn post or newsletter.
---

# Removing AI Tells

## Overview

Make text read as though a competent person wrote it on purpose.

Most of what marks text as machine-written is in its stance, its shape and its rhetorical habits. Vocabulary is the smallest part. Swapping "delve" for "explore" changes nothing if the sentence still refuses to commit, still runs the same length as the three around it, and still illustrates nothing. The word lists below are a quick symptom check to run after the structural work.

## Three Modes

| Mode | Trigger | Output |
|------|---------|--------|
| **Draft** | "write a post about X", any new text meant for publication | The text, written from Write Toward This and the voice reference, then put through steps 7 and 8 of the Process. |
| **Rewrite** | "make this sound human", "de-slop this" | The rewritten text. Add a change list only if asked, and one line when something needs the author (no voice sample, a claim you could not check). |
| **Audit** | "does this sound like AI?", "flag the tells", "check this before I publish" | A table of spans, why each reads as AI, and the fix. Leave the text unchanged. |

If the request is ambiguous between Rewrite and Audit, rewrite and offer the audit.

The audit reports which tells are present and gives no verdict on authorship. Asked "was this written by AI?", answer with what is in the text. A text with no tells may be a machine draft that had them removed, which is what this skill does, so say "no tells found" and leave "written by a human" unsaid. Authorship is settled only when the source is known, and then the source settles it.

## Write Toward This

Fix the shape first, and the vocabulary mostly follows. Prose that doesn't read as machine-written:

- **Commits.** It states which option is better and why.
- **Lets sentence length follow the content.** Most sentences are medium or long because they carry a claim together with its reason or its example. A short sentence appears where a point needs to stand alone, which is occasionally. The spread is wide and the short ones stay rare.
- **Names specifics.** Versions, numbers, real cases, actual names. One concrete instance does more than three abstractions.
- **Spends words unevenly.** Three sentences on the interesting part and half a clause on the obvious one. Even coverage means nobody chose what mattered.
- **Assumes a competent reader.** It cuts the definition they already have.
- **Has a position**, which shows in what gets emphasized.

## The Tells

### Stance

- **Hedging by default:** "can help", "may improve", "is often considered". Nothing is ever simply true.
- **Compulsive balance:** every claim gets a counterweight whether or not the sides are equal. "Both approaches have their merits."
- **No verdict:** options are presented, nothing is recommended, and the text ends on "it depends".
- **No stakes:** it never says what breaks, who is affected or what it costs.

### Shape

- **Uniform sentence length, in any band.** The classic machine band is 15 to 25 words. A draft where nearly everything is 4 to 10 words has the same problem, and it usually comes from an earlier pass that split sentences to look less like AI.
- **Staccato:** runs of very short declarative sentences ("Jev is a decision model. It writes no text at all."). Join them when the second one only completes the first.
- **Rule of three everywhere:** three adjectives, three bullets, three examples, regardless of how many there really are.
- **Symmetric paragraphs**, all within a line or two of each other.
- **Restating the question** before answering it.
- **Signposting:** "In this article we'll explore", "Let's dive in", "First… Second… Finally".
- **The closing summary** that repeats what the reader just read. If deleting the last paragraph loses nothing, delete it.
- **Identically shaped list items:** the same grammar, length and rhythm down the whole list.
- **Three-beat fragments:** "No fluff. No filler. Just results."

### Rhetorical figures

These are sentence-level moves that make prose sound written for effect. Each one is ordinary once in a long piece when the content calls for it. Machine drafts use them in every section.

- **Contrast framing.** The claim is made by first denying something nobody asserted. It has several forms, and removing one often produces another:
  - "It's not just X, it's Y." and "This isn't X. It's Y."
  - Two short sentences in opposition: "You can disagree with it. You can't ignore it."
  - A denial added at the end: "That makes it a second line of defence, not a sandbox."

  State the positive claim directly. Mention the denied alternative only when the reader is likely to believe it.
- **Aphoristic closer.** The paragraph ends on a short quotable line that restates it ("Models agree with themselves, like we do."). Delete the line and reread. If the paragraph lost nothing, leave it out. If the line carried a new fact, fold the fact into the sentence before it.
- **Pull quotes.** A blockquote or one-line paragraph that repeats a sentence from the body for emphasis.
- **Setup and reveal.** "Here's the thing:", "The result?", "And that's when it clicked." The point is delayed for effect. Say the point.
- **Self-answered questions.** "Why does this matter? Because…"
- **Paired openings.** Consecutive short sentences that begin with the same words. One pair in a piece is normal, several is a pattern.
- **Refrain.** A key phrase brought back in section after section as a motif.

**Check what you put in place of a removed tell.** These swaps keep the tell:

- "not just X but Y" becomes "X. Not Y."
- an em-dash becomes a full stop and leaves a fragment
- a pull quote becomes a one-line paragraph
- "Furthermore" becomes "On top of that"
- "delve into" becomes "dig into"

If the replacement does the same job in the sentence as the thing removed, the tell is still there. Restructure the sentence so that job is no longer needed.

### Substance

- **Abstraction with no instance.** Claims that never touch a concrete case.
- **Placeholder examples:** "imagine a company", "for example, a user might".
- **The obvious explained at the same depth as the non-obvious.** The writer had no sense of what was interesting.
- **Unrequested definitions.**

### Diction

- **Vocabulary:** delve, tapestry, realm, landscape, navigate, leverage, robust, seamless, crucial, vital, foster, underscore, testament, multifaceted, nuanced, intricate, pivotal, comprehensive, holistic, myriad, plethora, embark, unlock, harness, elevate, cornerstone, paramount.
- **Constructions:** "In today's fast-paced world" · "more than ever" · "at its core" · "Here's the thing" · "Whether you're X or Y". For "It's not just X, it's Y", see Contrast framing.
- **Trailing participial clauses:** "…, ensuring that…", "…, allowing you to…", "…, making it easier to…". They appear in machine text at a rate no human sustains.
- **Stacked empty intensifiers:** "truly transformative", "incredibly powerful".
- **Transition scaffolding:** "Furthermore", "Moreover", "Additionally", "It is important to note that". Prose that is ordered well needs almost none of these.
- **Agentless passive:** "it was determined that", "improvements were made". Passive voice is often correct. The tell is a passive whose actor cannot be recovered from anywhere in the text.
- **Softener tics:** "just" and "actually" scattered mid-sentence, several times a paragraph.

### Formatting

- **Over-bolding** inside paragraphs until nothing stands out.
- **Over-structuring:** a heading every two paragraphs, a list for three items that were a sentence, a table for two facts.

### Posts and articles

Blog posts, LinkedIn posts and newsletters have their own set, and readers of those platforms know them well.

- **Hook opening.** The first lines are engineered to stop scrolling: a confession, a small dramatic scene, a surprising claim alone on a line. Open with what happened or what the piece claims.
- **Slogan headings.** The heading states the moral ("A reviewer doesn't need to be right to be useful"). A heading should label what the section covers.
- **Lesson framing.** "What I learned", "what nobody tells you", numbered lessons wrapped around what is really a narrative.
- **One-line paragraphs for drama**, several per section.
- **Engagement ending.** The moral is restated, then a question is put to the audience ("How do you handle X?"), then "follow me for more". A specific request the author really has is fine ("if you solved this differently, tell me how").

### Folk tells

Some markers have become public shorthand for "a machine wrote this". Readers don't measure rates. They see one and decide, and the author is not there to argue.

Remove these wherever they appear, whatever their frequency, in anything where being suspected of AI has a cost:

- **Em-dashes.** They are legitimate punctuation and currently the most-cited tell. Replace each one with a comma, a colon or parentheses, or rewrite the two parts as one sentence. Use a full stop only when both halves are complete sentences of normal length, because the fragments left behind by removed dashes are a tell of their own.
- **The famous vocabulary**, "delve" above all.
- **"It's not just X, it's Y"** in any of the forms under Contrast framing.
- **Emoji section headers.**
- **Bold-lead bullets** running the length of a list.

Internal notes, code comments and anything nobody audits for provenance can keep them.

## Inherit, Don't Normalize

When the input is someone's draft, notes or transcript, it carries their idiolect. Keep it. This does more than any checklist above, and "improving the prose" destroys it by default.

- **Keep their tics.** A calque from their first language, an odd preposition, a phrase they lean on, a construction that is not quite standard. No model would generate these, so they read as human.
- **Keep their register.** If they never write "don't", never write "don't". Contraction rate is a strong stylometric fingerprint, the writer does not notice it, and it survives rewriting unless you flatten it.
- **Keep their vocabulary level.** A non-native writer's plain words and simple syntax are part of the voice. Do not upgrade them.
- **Keep their asymmetries.** The paragraph that runs long because they cared, the point they make twice, the section that stops abruptly.
- **Keep their structure choices**, including the ones a style guide would fix.

A document polished toward generic good prose is easier to spot than one that kept its author's rough edges, even when the rough version does worse on every list above.

Hold the register across the whole body of work. One document is hard to judge and a set is easy: five pieces that never contract and a sixth that always does means the sixth gets noticed.

### Voice reference

Inheriting needs a source. Before drafting or rewriting, work out which of these you have:

1. **The author's own draft in full sentences.** That is the reference. A pattern from the lists above that appears in the author's own sentences stays.
2. **Samples of the author's unaided writing**, pasted, linked, or in a `voice-samples/` folder next to this file. Read them first and note the range of sentence lengths, the contraction use, the connectors they favour, the spelling variety, traces of their first language, and how they open and close a piece. Match those.
3. **Only bullet notes or a machine draft, and no samples.** There is no idiolect to keep. In Draft mode, ask once for a sample before writing. If none comes, write plainly, do not invent a voice, and say in one line that the voice is generic because there was nothing to match.

When a text mixes the author's sentences with generated ones (a co-written piece), the same pattern is kept in the first and removed from the second. If you cannot tell which is which, ask.

## Guardrails

Sounding human is not worth being wrong.

- **Never invent specifics.** Fabricating a number, version, benchmark or name to sound concrete is far worse than sounding like AI. If no concrete instance is available, cut the claim or keep it general.
- **Keep load-bearing hedges.** "Usually", "in most cases" and "up to" carry truth conditions. Cut the reflexive hedges and keep the ones doing work, because deleting a real qualifier turns a true sentence into a false one.
- **Don't manufacture personality.** Injected quirk, jokes and fake asides read as worse AI.
- **Keep structure that earns its place.** Tables, lists and headings are fine when the content is tabular or enumerable. Turning a real table into prose is a downgrade.
- **Don't overcorrect into affectation.** Splitting sentences to create variety produces staccato, which is as uniform as what it replaced. Vary length by letting long thoughts stay long.
- **Respect the register.** Legal text, API reference and safety copy are supposed to be flat and hedged. Leave them that way.

## Process

1. Identify the mode, the register, the genre, whether claims can be checked, and which voice reference you have.
2. **Shape pass:** sentence-length spread, staccato runs, paragraph symmetry, rule of three, signposting, closing summary.
3. **Figures pass:** contrast framing in all its forms, aphoristic closers, pull quotes, setup and reveal. For posts and articles, also the headings, the opening and the ending.
4. **Stance pass:** find the hedges and the missing verdict. Commit where the source supports committing.
5. **Substance pass:** for every abstract claim, ask what the instance is. Use a real one or leave the claim general.
6. **Diction pass:** vocabulary, constructions and folk tells. This comes after the structural passes.
7. **Guardrail pass:** check whether anything became unsupported, over-committed or invented, and restore it.
8. **Re-audit:** read your output as if it were a new submission in Audit mode, and run the checker below. A rewrite adds tells of its own, mostly staccato from split sentences and the swaps listed under Rhetorical figures. Fix what you find and re-audit, at most three passes in total. If tells remain after the third, report them in one line. Keep the audit to yourself unless asked for it.

In Draft mode, write the text first and then run steps 7 and 8. In Rewrite mode, run all eight.

## Countable checks

Counting by eye is unreliable. When you can run code, save the text to a file and run the checker, before the rewrite and again in step 8:

```bash
uv run scripts/check_tells.py <file>
```

It reports dashes, listed vocabulary, blockquote lines, the sentence-length spread, the share of short sentences and the longest run of them, one-sentence paragraphs, and every short paragraph closer, paired short sentence and contrast candidate.

The numbers point you at places to look and decide nothing by themselves. As a rough guide:

- Dashes, listed vocabulary and blockquote lines should be at zero in public writing, unless a blockquote is a real quotation.
- If more than about a quarter of the sentences are short, or three short ones come in a row, check whether they were split from longer ones.
- Read every listed closer, pair and contrast candidate. Some are fine ("I haven't decided yet." is a real statement). Several in one piece is the pattern.
- Compare with the author's samples when you have them. Their own numbers are the target, and they override this guide.

The sentence splitter is approximate (abbreviations such as "e.g." split early), so treat small differences as noise.

## Audit Output Format

| Span | Why it reads as AI | Fix |
|------|--------------------|-----|
| "can help improve performance" | Hedged non-claim, no verdict | State the effect, or cut |
| "…, allowing you to scale easily" | Trailing participial clause | Make it a sentence of its own |
| 4 consecutive 20-word sentences | Uniform rhythm | Let one run long, or merge two |
| "You can disagree with it. You can't ignore it." | Contrast framing, two-sentence form | One sentence with the positive claim |
| Paragraph ends "Models agree with themselves, like we do." | Aphoristic closer | Delete, or fold into the sentence before |
| Final section: moral, question to readers, "follow me" | Engagement ending | End on the last real point |

## Common Mistakes

- **Starting with the word list.** The result is synonym-swapped slop: the sentences still hedge, still run the same length and still illustrate nothing.
- **Swapping a tell for its sibling.** The em-dash becomes a fragment, "not just X but Y" becomes "X. Not Y.". Check each replacement.
- **Splitting sentences to vary rhythm.** The draft comes out staccato, with a quotable short line at the end of every paragraph.
- **Drafting from the tell lists alone.** Avoiding every listed pattern without a voice reference gives flat, generic prose. Write toward the positive list and the author's samples, then audit.
- **Inventing detail to sound concrete.** This is the one failure worse than the original, and the first guardrail exists because it is tempting.
- **Inventing a voice** when there is no sample to match.
- **Stripping every hedge.** Reflexive hedging is a tell and accurate hedging is accuracy.
- **De-slopping text that should be flat.** Check the register before touching legal, reference or safety copy.
- **Skipping the re-audit.** The first rewrite is rarely clean.
- **Auditing when asked to rewrite, or rewriting when asked to audit.**
