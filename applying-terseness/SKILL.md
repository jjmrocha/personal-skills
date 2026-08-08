---
name: applying-terseness
description: Use when text is wordy, verbose, padded, or bloated — trimming filler, cutting redundancy, fixing flabby phrasing, or making docs/comments/messages/instructions/prose more concise. Covers rewriting text terser and auditing for verbosity without rewriting.
---

# Applying Terseness

## Overview

Make text shorter without changing what it means. Terseness works at **two levels**: trimming *within* sentences (rules 1–8) and **restructuring** across them (collapsing parallel prose into tables/lists, merging repeated-subject sentences, cutting duplicated points). Word-level trimming alone leaves the biggest wins on the table — always check for structural moves.

**Core principle:** Cut words and redundant structure, not meaning. Every change must preserve truth conditions, technical accuracy, and required caveats.

## Two Modes

| Mode | Trigger | Output |
|------|---------|--------|
| **Rewrite** | "tighten this", "make terser", "shorten" | Rewritten text only (change list only if asked). |
| **Audit** | "where is this wordy?", "flag verbosity" | Table of spans → suggestion → rule #. Do NOT rewrite. |

Ambiguous request → default to Rewrite, offer the audit.

## The Terseness Rules

1. **Cut throat-clearing:** "It is important to note that", "Needless to say", "For all intents and purposes", "Basically".
2. **One word for wordy phrases:** due to the fact that→because · in order to→to · in the event that→if · until such time as→until · make use of→use · has the ability to→can · a number of→several · at this point in time→now.
3. **Kill doublets/tautologies:** "variable and unpredictable"→unpredictable · "each and every"→every.
4. **Active voice** when the actor is known and relevant.
5. **Cut empty intensifiers/hedges:** very, quite, rather, somewhat, generally — when they add no precision.
6. **Present simple** over padding: "will attempt to retry"→retries.
7. **Drop optional "that"** when grammatical.
8. **One idea per sentence;** split run-ons, delete connective filler.

## Restructure for Density (do this, not just rules 1–8)

After trimming, look for these shapes and convert them. This is where the biggest reductions live — a 4-sentence paragraph often becomes a 3-row table.

| When you see… | Convert to… |
|---------------|-------------|
| **3+ items each described on the same axes** ("X is fast but not durable; Y is durable but slow…") | A **comparison table** (rows = items, columns = axes). |
| **Parallel sentences with one varying slot** ("To set the mode, use MODE_VAR. To set the TTL, use TTL_VAR.") | A **list or two-column table** (varying slots only). |
| **Consecutive sentences sharing a subject** ("The cache supports A. The cache supports B. The cache also supports C.") | **One sentence** ("The cache supports A, B, and C.") |
| **The same point made twice** in different words | **Keep one** (the clearer/more specific). |
| **A buried enumeration** inside prose ("first… also… in addition… as well") | A **bulleted/numbered list.** |

Restructuring must still preserve every fact and qualifier. **Exception — executable instructions:** do NOT reorder steps or branches (see below); you may still collapse parallel *parameter* descriptions into a table since that preserves order.

## Guardrails — What NOT to Cut

**Trading meaning for word-count is failure, not terseness.**

- **Load-bearing qualifiers** — "in most cases", "usually", "up to", "approximately" change truth conditions. Keep them. (Common failure: "usually retries" → "retries" silently means *always*.)
- **Code, identifiers, numbers, names, quotes** — never alter.
- **Required caveats** (legal, safety, security) — verbatim.
- **Ambiguity beats brevity** — if the terser version reads two ways, keep the longer one.

## Tightening Instructions / Procedures

When the text is a procedure, spec, or instructions another agent or person will **execute**, terseness must not cost actionability. The result must keep, unambiguously and out of context:

- **Every step**, in original order.
- **Every condition and branch** (if/then, success/failure paths).
- **Every parameter, value, name, and target.**
- **No dangling pronouns** ("it", "this", "the one above") — name the referent so the line stands alone.

Test it: could a downstream agent execute *only* the tightened version and do exactly what the original specified? If not, restore detail.

## Process

1. Identify the mode, and whether the text is executable instructions.
2. Apply rules 1–8 (within-sentence trimming).
3. **Restructure pass** (always): scan for the shapes in "Restructure for Density" and convert them. Don't stop at word-level cuts.
4. **Guardrail pass** (always): did any change alter meaning, drop a qualifier, break a step/condition, reorder instructions, or touch code/caveats? Restore it.
5. Return tightened text (Rewrite) or the flag table (Audit).

## Audit Output Format

| Span (original) | Suggestion | Rule |
|-----------------|------------|------|
| "due to the fact that" | "because" | 2 |
| "variable and unpredictable" | "unpredictable" | 3 |

## Common Mistakes

- **Stopping at word-swaps** → you trimmed each sentence but left a comparison as prose, parallel sentences un-tabled, repeated points intact. The biggest wins are structural; always run the Restructure pass.
- **Over-cutting qualifiers** → meaning drift. The #1 meaning failure.
- **Rewriting in audit mode** → the user wanted to see the cuts. (Audit may also flag restructure opportunities: span → "→ table"/"→ merge" → rule.)
- **Dropping a step, condition, or pronoun referent** in instructions → downstream agent misexecutes.
- **Flattening intentional tone** in user-facing copy — confirm first.
