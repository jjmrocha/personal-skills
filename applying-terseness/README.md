# applying-terseness

Make text shorter without changing what it means.

## What it does

Trims filler, collapses wordy phrases, and — the part word-level editing usually misses — restructures prose into tables and lists where the shape allows it. A four-sentence comparison paragraph becomes a three-row table.

Two modes:

| Mode | Say | You get |
|------|-----|---------|
| **Rewrite** | "tighten this", "make this terser" | The rewritten text |
| **Audit** | "where is this wordy?", "flag verbosity" | A table of spans → suggestion → rule #, no rewrite |

## When it triggers

Wordy docs, bloated comments, padded commit messages, verbose instructions or prompts, flabby prose of any kind.

## What it won't cut

Load-bearing qualifiers ("usually", "up to", "approximately"), code and identifiers, required legal/safety/security caveats, and anything whose terser form reads two ways. For procedures and specs it preserves every step in order, every branch, and every parameter — a downstream reader must be able to execute the tightened version alone.

## Example

> Due to the fact that the cache is variable and unpredictable, it is important to note that you will want to make use of a retry.

becomes

> The cache is unpredictable, so use a retry.

See [SKILL.md](SKILL.md) for the full rule set.
