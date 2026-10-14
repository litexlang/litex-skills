# Litex SOP & Skill Hub

Skills for people and agents writing Litex, with a runnable foundation,
selected task workflows and deeper source reading on demand.

**Write Litex in one persistent `-session`.** Keep earlier accepted definitions
and facts after an ordinary rejection; repair the next statement there. Do not
rerun the whole file after adding a few lines. See the
[short command comparison](sop_and_skills/skills/litex-reference/references/execution.md#file-and-session).

Start with [litex-basics](sop_and_skills/skills/litex-basics/SKILL.md): overview,
execution, main syntax, common mathematics and misconception checks. Its
[examples](sop_and_skills/skills/litex-basics/examples/README.md) run with a
Litex executable without a golitex checkout. Then select a task skill and the
needed topic from the [layered index](sop_and_skills/README.md).

## Choose an installation

| Profile | Content | Intended use |
| --- | --- | --- |
| `basics` | 1 skill, six topic guides and checked teaching examples | First Litex task or minimal installation |
| `author` (default) | 12 skills covering the foundation, references, tasks and specialized topics | Ordinary mathematical authoring |
| `maintainer` | All 18 skills and the full source reference/archive scopes | Explicit kernel/compiler/repository work |

Export to a new directory outside this repository:

```sh
python3 sop_and_skills/scripts/export_skills.py --output /tmp/litex-author-pack
python3 sop_and_skills/scripts/export_skills.py --profile basics --output /tmp/litex-basics-pack
```

The command refuses existing destinations. Read the exported `INSTALL.md` and
inspect existing personal skills before merging anything. The default packs
contain selected authored instructions and teaching examples; historical
archives remain in this source checkout. Selection is explicit in
[profiles.json](sop_and_skills/profiles.json).

For deeper questions, [litex-reference](sop_and_skills/skills/litex-reference/SKILL.md)
reads actual `docs/`, `examples/` and `showcases/` in the paired `../golitex`.
An explicit `LITEX_REFERENCE_ROOT` selects another matching checkout. It reads
by question and depth; no full golitex documentation copy is required.

## Repository layout and checks

- [sop_and_skills/](sop_and_skills/README.md): reusable skills, SOPs, selected references and scripts.
- [generic_agent_example/](generic_agent_example/README.md): install Generic Agent, load these skills and reproduce the IMO 1968 P4 geometry task, with a persistent Session and frozen-goal verification.
- [CONTRIBUTING.md](CONTRIBUTING.md): adding content and maintaining portable profiles.

```sh
python3 sop_and_skills/scripts/check_hub.py
```

[Provenance](sop_and_skills/references/sources.md) records origins and
transformations. [Validation](sop_and_skills/references/validation.md) separates
current executable checks from historical evidence and navigation checks.
