# Load Litex skills in DeepSeek Harness

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`)
loads the same `SKILL.md` bundles used by other Agent Skills hosts. Skills are
filesystem instructions, not plugins: do not install them with
`dsh plugin add`. Official skill discovery is documented in the
[skills subsystem](https://deepseek-harness.github.io/deepseek-harness/en/reference/subsystems/skills).

## 1. Start dsh

Needs Node.js `^22.19.0` or `>=24`:

```sh
npx @deepseek-ai/dsh web
```

Open the printed local URL (default `http://127.0.0.1:3080`), choose a
workspace, and configure a model/API key under **Settings → Models**.

## 2. Export Litex skills

From this hub repository root:

```sh
python3 scripts/export_skills.py --profile author --output /tmp/litex-author-pack
```

## 3. Install into a dsh discovery root

dsh scans **one directory level only**. Each skill must be a direct child:

```text
<root>/<skill-name>/SKILL.md
```

Nested trees such as `root/skills/litex-basics/SKILL.md` are **not** found if
`skills/` is an extra nesting under the discovery root. Copy the exported
siblings into the root itself.

Priority (lower rank wins):

| Rank | Root |
| --- | --- |
| 100 | `<project>/.dsh/skills` |
| 200 | `<project>/.agents/skills` |
| 400 | `~/.dsh/skills` |
| 500 | `~/.agents/skills` |

Project root means the nearest ancestor with `.git`, else the workspace cwd.

### Project install

```sh
mkdir -p .agents/skills
cp -R /tmp/litex-author-pack/skills/. .agents/skills/
```

### User-global install (also visible to Claude Code)

```sh
mkdir -p ~/.agents/skills
cp -R /tmp/litex-author-pack/skills/. ~/.agents/skills/
```

Restart `dsh web` after copying. In the session, open `/` and confirm names
such as `litex-basics` appear under Skills. The model also receives a skill
catalog and can load instructions with the `skill` tool.

## 4. Invoke a skill

Explicit user invocation:

```text
/litex-basics
```

Then ask for the Litex task. Or name the skill in ordinary prose and let the
model call `skill` after reading the catalog.

## Notes

- Keep `litex` available in the workspace shell environment.
- Set `LITEX_REFERENCE_ROOT` when using `litex-reference` against a live
  golitex checkout.
- This walkthrough covers install and discovery only. It does not pin a
  geometry theorem; see [generic-agent/](../generic-agent/README.md) for a
  frozen-goal Session experiment.
