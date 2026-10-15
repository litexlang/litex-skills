# Load Litex skills in Pi

[Pi](https://pi.dev/docs/latest/) discovers Agent Skills directories that contain
`SKILL.md`. It advertises each skill's name and description at startup, then
reads the full instructions when the task matches (or when you force
`/skill:name`). See Pi's [Skills](https://pi.dev/docs/latest/skills) and
[Usage](https://pi.dev/docs/latest/usage) docs.

## 1. Export a portable pack

From this hub repository root:

```sh
python3 scripts/export_skills.py --profile author --output /tmp/litex-author-pack
```

The pack layout is `/tmp/litex-author-pack/skills/<name>/SKILL.md`.

## 2. Make the pack visible to Pi

Pick one path. Do not invent a second copy inside the hub.

### Option A — project skills (recommended for a Litex workspace)

From the project you will run `pi` in:

```sh
mkdir -p .agents/skills
cp -R /tmp/litex-author-pack/skills/. .agents/skills/
```

Pi also discovers `.pi/skills/`. Project `.agents/skills/` is walked from the
working directory up to the repository root.

### Option B — user-global skills

```sh
mkdir -p ~/.agents/skills
cp -R /tmp/litex-author-pack/skills/. ~/.agents/skills/
```

`~/.pi/agent/skills/` works the same way for Pi-only installs.

### Option C — settings path (no copy)

Add the exported skills directory to Pi settings. User settings live under the
agent directory; project settings live in `.pi/settings.json`:

```json
{
  "$schema": "https://pi.dev/schemas/settings.schema.json",
  "skills": ["/tmp/litex-author-pack/skills"]
}
```

Pi discovers `SKILL.md` under that path recursively. Restart Pi or run
`/reload` after changing settings or skill files.

## 3. Run Pi and force a skill when needed

```sh
cd /path/to/your/litex/project
pi
```

Confirm the startup header lists Litex skills. For an explicit load:

```text
/skill:litex-basics write a short claim that 1 + 1 = 2 in Litex, using -session
```

Then load task skills as needed, for example `/skill:litex-proof-writer`.

## Notes

- Keep a Litex executable on `PATH`, or tell Pi the absolute path to `litex`.
- For live docs/examples/showcases, set `LITEX_REFERENCE_ROOT` to a matching
  golitex checkout before relying on `litex-reference`.
- This example only covers skill discovery. It does not pin a theorem or measure
  autonomous success; use [generic-agent/](../generic-agent/README.md) for that
  style of frozen-goal experiment.
