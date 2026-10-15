# Load Litex skills in Codex

Codex consumes the same `SKILL.md` directories. Export from this hub and copy
them into Codex's skill directory.

## Export

```sh
python3 scripts/export_skills.py --profile author --output /tmp/litex-author-pack
```

## Install

```sh
mkdir -p ~/.codex/skills
cp -R /tmp/litex-author-pack/skills/. ~/.codex/skills/
```

If your Codex build also reads `~/.agents/skills/` or a project
`.agents/skills/`, those roots work too—keep one copy and avoid divergent
edits.

Start a new Codex session in your Litex project, mention `litex-basics`, and
continue with the task skill you need (`litex-proof-writer`,
`litex-concept-modeler`, …).
