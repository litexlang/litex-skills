# Agent examples

These walkthroughs show how to load Litex skills into particular agents.
Shared skill content stays in [`../skills/`](../skills/README.md); export a
portable pack first when the agent expects a flat skill directory.

```sh
python3 ../scripts/export_skills.py --profile author --output /tmp/litex-author-pack
```

The exported pack contains `skills/<name>/SKILL.md` siblings. Most agents want
those sibling directories copied (or pointed at), not the hub source tree.

| Example | What it shows |
| --- | --- |
| [pi/](pi/README.md) | Point Pi at the exported skills via settings or `.pi` / `.agents` skill roots |
| [deepseek-harness/](deepseek-harness/README.md) | Drop skills into dsh discovery roots (one level deep; no recursive nesting) |
| [claude-code/](claude-code/README.md) | Copy skills into Claude Code's skill directory |
| [codex/](codex/README.md) | Copy skills into Codex's skill directory |
| [generic-agent/](generic-agent/README.md) | Full geometry experiment with Session bridge and frozen-goal check |

Claude Code and Codex need only the export-and-copy steps. Pi and DeepSeek
Harness add agent-specific discovery roots and invocation commands. The Generic
Agent example is the only one that pins revisions and verifies a frozen theorem.
