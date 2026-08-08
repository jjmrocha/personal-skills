---
name: removing-ai-tells
description: Use when text reads as machine-generated — "sounds like ChatGPT", "AI slop", "too polished", "make this sound human", "corporate", "generic". Covers rewriting drafts to remove the tells and auditing text to flag them without rewriting.
---

# Removing AI Tells

## Overview

Make text read as though a competent person wrote it on purpose.

**Core principle:** the tell is **stance and shape**, not vocabulary. Swapping "delve" for "explore" changes nothing if the sentence still refuses to commit, still runs 22 words like the three around it, and still illustrates nothing. Word lists are a *symptom check* — fast, useful, and never sufficient.

## Two Modes

| Mode | Trigger | Output |
|------|---------|--------|
| **Rewrite** | "make this sound human", "de-slop this" | Rewritten text only (change list if asked). |
| **Audit** | "does this sound like AI?", "flag the tells" | Table of spans → why it reads as AI → fix. Do NOT rewrite. |

Ambiguous request → default to Rewrite, offer the audit.

**The audit reports tells, never authorship.** Asked "was this written by AI?", answer with what is present, not with a verdict on who wrote it. Absence of tells is not evidence of a human author — it is equally consistent with a machine draft that had its tells removed, which is the entire purpose of this skill. Say "no tells found", never "written by a human". A clean document with a known-human source is the one case where authorship is settled, and it is settled by the source, not by the text.

## Write Toward This

Fix the shape first; the vocabulary mostly follows. Prose that doesn't read as machine-written:

- **Commits.** States which option is better and why. A verdict, not a survey.
- **Varies rhythm hard.** A 30-word sentence, then a 4-word one. That variance *is* the human signal — uniform length is the loudest tell in the file.
- **Names specifics.** Versions, numbers, real cases, actual names. One concrete instance outweighs three abstractions.
- **Spends words unevenly.** Three sentences on the interesting part, half a clause on the obvious one. Even coverage means nobody chose what mattered.
- **Assumes a competent reader.** Cuts the definition they already have.
- **Has a position**, and lets it show in what gets emphasized.

## The Tells

### Stance
- **Hedging by default** — "can help", "may improve", "is often considered". Nothing is ever just true.
- **Compulsive balance** — every claim gets a counterweight whether or not the sides are equal. "Both approaches have their merits."
- **No verdict.** Presents options, recommends nothing, ends on "it depends."
- **No stakes.** Never says what breaks, who's affected, what it costs.

### Shape
- **Uniform sentence length.** Everything lands between 15 and 25 words.
- **Rule of three everywhere** — three adjectives, three bullets, three examples, regardless of how many there actually are.
- **Symmetric paragraphs**, all within a line or two of each other.
- **Restating the question** before answering it.
- **Signposting** — "In this article we'll explore", "Let's dive in", "First… Second… Finally".
- **The closing summary** that repeats what the reader just read. If deleting the last paragraph loses nothing, it was a tell.
- **Identically-shaped list items** — same grammar, same length, same rhythm, down the whole list.
- **Three-beat fragments** — "No fluff. No filler. Just results." Reads as punchy; is now its own AI signature. Note this is uniform rhythm too, just at a shorter length.

### Substance
- **Abstraction with no instance.** Claims that never touch a concrete case.
- **Placeholder examples** — "imagine a company", "for example, a user might". Nobody, nowhere, doing nothing.
- **The obvious explained at the same depth as the non-obvious** — the writer had no sense of what was interesting.
- **Unrequested definitions.**

### Diction
- **Vocabulary:** delve, tapestry, realm, landscape, navigate, leverage, robust, seamless, crucial, vital, foster, underscore, testament, multifaceted, nuanced, intricate, pivotal, comprehensive, holistic, myriad, plethora, embark, unlock, harness, elevate, cornerstone, paramount.
- **Constructions:** "It's not just X, it's Y" · "In today's fast-paced world" · "more than ever" · "at its core" · "Here's the thing" · "Whether you're X or Y".
- **Trailing participial clauses** — "…, ensuring that…", "…, allowing you to…", "…, making it easier to…". Badly underrated as a tell; they appear at a rate no human sustains.
- **Stacked empty intensifiers** — "truly transformative", "incredibly powerful".
- **Transition scaffolding** — "Furthermore", "Moreover", "Additionally", "It is important to note that". Prose that's actually ordered well needs almost none of these.
- **Agentless passive** — "it was determined that", "improvements were made". Not passive voice as such, which is often correct; the tell is passive with no actor recoverable anywhere.
- **Softener tics** — "just" and "actually" scattered mid-sentence, several times a paragraph, softening claims that weren't hard to begin with.

### Formatting
- **Over-bolding** inside paragraphs until nothing stands out.
- **Over-structuring** — a heading every two paragraphs, a list for three items that were a sentence, a table for two facts.

### Folk Tells

Some markers have become public shorthand for "a machine wrote this." Readers don't measure rates — they see one, and decide. Whether that judgment is statistically fair is beside the point: it happens in your absence and you don't get to argue with it.

**Remove these on sight, not by frequency**, in anything where being suspected of AI carries a cost:

- **Em-dashes.** The most-cited tell there is. Legitimate punctuation, genuinely useful, and currently radioactive in public prose. A comma, colon, parenthesis, or full stop covers every case; a spaced hyphen keeps the same rhythm if you want it.
- **The famous vocabulary** — "delve" above all. Flagged on sight, whether or not the sentence needed the word.
- **"It's not just X, it's Y."** Recognized by people who couldn't name another tell.
- **Emoji section headers.**
- **Bold-lead bullets** running the length of a list.

The cost is contextual, the perception isn't. Internal notes, code comments, and anything nobody audits for provenance can keep them. Public writing can't.

## Inherit, Don't Normalize

When the input is someone's draft, notes, or transcript, it carries their idiolect. **Keep it.** This is the highest-leverage move in the skill and the easiest to destroy by accident, because "improving the prose" destroys it by default.

- **Keep their tics.** A calque from their first language, an odd preposition, a phrase they lean on, a construction that is not quite standard. These read as human precisely because no model would generate them.
- **Keep their register.** If they never write "don't", never write "don't". Contraction rate is among the strongest stylometric fingerprints there is, it is invisible to the writer, and it survives any amount of rewriting unless you flatten it.
- **Keep their asymmetries.** The paragraph that runs long because they cared. The point they make twice. The section that stops abruptly.
- **Keep their structure choices**, including the ones a style guide would fix.

Smoothness is the tell. A document that has been polished toward generic good prose is more detectable than one that kept its author's rough edges, even when the rough version scores worse on every checklist above.

**Hold the register across the whole body of work.** A single document is hard to judge; a set is not. Five pieces that never contract and a sixth that always does means the sixth gets caught, however clean it is alone.

## Guardrails

**Sounding human is not worth being wrong.**

- **Never invent specifics.** Fabricating a number, version, benchmark, or name to sound concrete is far worse than sounding like AI. No concrete instance available? Cut the claim or keep it general and say so.
- **Keep load-bearing hedges.** "Usually", "in most cases", "up to" carry truth conditions. Cutting hedging means cutting the *reflexive* kind — not the kind doing work. Deleting a real qualifier converts a true sentence into a false one.
- **Don't manufacture personality.** Injected quirk, jokes, and fake asides read as *worse* AI, not less. The goal is a competent writer, not a character.
- **Keep structure that earns its place.** Tables, lists, and headings aren't tells when the content is genuinely tabular or enumerable. Prose-ifying a real table is a downgrade.
- **Don't overcorrect into affectation.** Every sentence clipped to five words is its own uniform rhythm, and just as obvious.
- **Respect the register.** Legal text, API reference, and safety copy are *supposed* to be flat and hedged. Don't humanize them.

## Process

1. Identify the mode, the register, and whether claims can be checked.
2. **Shape pass** — sentence-length variance, paragraph symmetry, rule-of-three, signposting, closing summary.
3. **Stance pass** — find the hedges and the missing verdict. Commit where the source supports committing.
4. **Substance pass** — every abstract claim, ask: what's the instance? Use a real one or leave the claim general.
5. **Diction pass** — vocabulary and constructions. Last, not first.
6. **Guardrail pass** — did anything become unsupported, over-committed, or invented? Restore it.

## Audit Output Format

| Span | Why it reads as AI | Fix |
|------|--------------------|-----|
| "can help improve performance" | Hedged non-claim, no verdict | State the effect, or cut |
| "…, allowing you to scale easily" | Trailing participial clause | Split into its own sentence |
| 4 consecutive 20-word sentences | Uniform rhythm | Break one to <8 words |

## Common Mistakes

- **Starting with the word list** → synonym-swapped slop. The sentences still hedge, still run the same length, still illustrate nothing. Shape first.
- **Inventing detail to sound concrete** → the one failure that's worse than the original. Guardrail 1 exists because this is the tempting move.
- **Stripping every hedge** → confident falsehoods. Reflexive hedging is a tell; accurate hedging is accuracy.
- **De-slopping text that should be flat** → check the register before touching legal, reference, or safety copy.
- **Auditing when asked to rewrite, or rewriting when asked to audit.**
