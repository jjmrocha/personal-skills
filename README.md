# personal-skills

Agent skills I use with [Claude](https://claude.com/claude).

Each directory is a self-contained skill: a `SKILL.md` the agent loads, plus a `README.md` for humans browsing here.

## The skills

| Skill | Use it when |
|-------|-------------|
| [applying-terseness](applying-terseness/) | Text is wordy — trim filler, cut redundancy, collapse prose into tables. Rewrites or audits without rewriting. |
| [grill-me](grill-me/) | You want the agent to understand *why* you think something before it acts. It interviews you, one question at a time. |
| [removing-ai-tells](removing-ai-tells/) | Text reads as machine-generated — fixes the stance and rhythm that give it away, not just the vocabulary. |
| [socratic-mentor](socratic-mentor/) | You're learning a concept — explained first, then questioned, calibrated to what you already know. |

## Install

Skills live in `~/.claude/skills/`. Clone once, then symlink the ones you want:

```bash
git clone https://github.com/jjmrocha/personal-skills.git ~/SOURCES/personal-skills

mkdir -p ~/.claude/skills
ln -s ~/SOURCES/personal-skills/applying-terseness ~/.claude/skills/
ln -s ~/SOURCES/personal-skills/grill-me           ~/.claude/skills/
ln -s ~/SOURCES/personal-skills/removing-ai-tells  ~/.claude/skills/
ln -s ~/SOURCES/personal-skills/socratic-mentor    ~/.claude/skills/
```

Symlinks mean `git pull` updates the installed skills. To install all of them:

```bash
for d in ~/SOURCES/personal-skills/*/; do
  [ -f "$d/SKILL.md" ] && ln -sfn "${d%/}" ~/.claude/skills/
done
```

Restart Claude Code, or run `/doctor` to confirm they loaded.

Project-scoped instead of personal: put them in `.claude/skills/` inside the repo and commit them, so the whole team gets them.

## Using them

Skills load automatically when the agent judges the description to match what you're doing. You can also invoke one by name — `/applying-terseness`, `/grill-me`, `/removing-ai-tells`, `/socratic-mentor`.

## License

[MIT](LICENSE)

`socratic-mentor` began as a rewrite of an agent from the [SuperClaude Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) (MIT) and borrows one idea from Matt Pocock's [skills](https://github.com/mattpocock/skills) (MIT) — see [its credits](socratic-mentor/README.md#credits).
