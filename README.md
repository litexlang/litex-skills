# Litex SOP & Skill Hub

Skills for people and agents writing Litex, with a runnable foundation,
selected task workflows and deeper source reading on demand.

**Write Litex in one persistent `-session`.** Keep earlier accepted definitions
and facts after an ordinary rejection; repair the next statement there. Do not
rerun the whole file after adding a few lines. See the
[short command comparison](skills/litex-reference/references/execution.md#file-and-session).

Start with [litex-basics](skills/litex-basics/SKILL.md) (basic language layer:
Session, `cart` / coordinates, small defs). Then
[litex-intermediate](skills/litex-intermediate/SKILL.md) /
[litex-advanced](skills/litex-advanced/SKILL.md) as needed. Runnable teaching
examples: [skills/litex-basics/examples](skills/litex-basics/examples/README.md).
Pure-API mini smoke before large benchmarks:
[examples/skill-api-smoke](examples/skill-api-smoke/README.md). Task skills:
[layered skill index](skills/README.md).

## Choose an installation

| Profile | Content | Intended use |
| --- | --- | --- |
| `basics` | 1 skill, six topic guides and checked teaching examples | First Litex task or minimal installation |
| `author` (default) | 12 skills covering the foundation, references, tasks and specialized topics | Ordinary mathematical authoring |
| `maintainer` | All 18 skills and the full source reference/archive scopes | Explicit kernel/compiler/repository work |

Export to a new directory outside this repository:

```sh
python3 scripts/export_skills.py --output /tmp/litex-author-pack
python3 scripts/export_skills.py --profile basics --output /tmp/litex-basics-pack
```

The command refuses existing destinations. Read the exported `INSTALL.md` and
inspect existing personal skills before merging anything. The default packs
contain selected authored instructions and teaching examples; historical
archives remain in this source checkout. Selection is explicit in
[profiles.json](profiles.json).

For deeper questions, [litex-reference](skills/litex-reference/SKILL.md)
reads actual `docs/`, `examples/` and `showcases/` in the paired `../golitex`.
An explicit `LITEX_REFERENCE_ROOT` selects another matching checkout. It reads
by question and depth; no full golitex documentation copy is required.

## Repository layout and checks

| Path | Role |
| --- | --- |
| [skills/](skills/README.md) | Reusable Litex agent skills |
| [sops/](sops/README.md) | Task SOPs that combine skills |
| [references/](references/sources.md) | Shared snapshots, provenance and validation notes |
| [scripts/](scripts/) | Export and hub checks |
| [examples/](examples/README.md) | Agent install walkthroughs (Pi, DeepSeek Harness, Claude Code, Codex, Generic Agent) |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Adding content and maintaining portable profiles |

```sh
python3 scripts/check_hub.py
```

[Provenance](references/sources.md) records origins and
transformations. [Validation](references/validation.md) separates
current executable checks from historical evidence and navigation checks.
