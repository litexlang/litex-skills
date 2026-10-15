# Load Litex skills in Claude Code

Claude Code uses the standard Agent Skills layout: one directory per skill with
`SKILL.md`. Export from this hub, then copy the sibling skill directories into
Claude's skill root.

## Export

```sh
python3 scripts/export_skills.py --profile author --output /tmp/litex-author-pack
```

## Install

User-global (common):

```sh
mkdir -p ~/.claude/skills
cp -R /tmp/litex-author-pack/skills/. ~/.claude/skills/
```

Or project-local, if your Claude Code setup reads `.claude/skills/` /
`.agents/skills/` in the repository:

```sh
mkdir -p .claude/skills
cp -R /tmp/litex-author-pack/skills/. .claude/skills/
```

Restart or reload the agent session, then ask it to follow `litex-basics`
before writing Litex. Prefer an explicit mention of the skill name on the first
turn.

`~/.agents/skills/` is a shared root also scanned by DeepSeek Harness; you can
install once there if both tools should see the same copy.
