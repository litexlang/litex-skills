# Litex SOP & Skill Hub

This repository collects SOPs, skills, and reference material for people and
AI agents writing Litex. Reusable content lives in `sop_and_skills/` and is
selected according to the task.

## Main directories

```text
sop_and_skills/                # Reusable content
├── README.md                  # Capability index and reading entrypoint
├── skills/                    # 16 skills and their supporting material
├── sops/                      # Task-specific workflows
├── references/                # Shared docs, examples, provenance, and validation
└── scripts/                   # Content checks

generic_agent_example/        # One example of using the content
├── README.md                  # Using the skills with Generic Agent
├── memory-entry.txt           # Example reference pointer
└── legacy_imo_package/        # Historical IMO problem-solving package
```

## Usage

Start with the [SOP and skill index](sop_and_skills/README.md), then read the
skills and references needed for your task. People can use these materials
directly; an agent needs the corresponding file and execution capabilities.

The [Generic Agent example](generic_agent_example/README.md) demonstrates how
one agent can read the skills, write Litex, and verify results. Its source,
installation, and startup instructions are maintained in the
[upstream repository](https://github.com/lsdefine/GenericAgent).

## Adding content and checking the package

Add reusable SOPs, skills, and reference material under `sop_and_skills/`.
Keep an agent's configuration, loading steps, and usage examples in its example
directory. See the [contribution guide](CONTRIBUTING.md).

Run from the repository root:

```sh
python3 sop_and_skills/scripts/check_hub.py
```

[Source provenance](sop_and_skills/references/sources.md) records versions and
import transformations. [Validation](sop_and_skills/references/validation.md)
distinguishes checked examples from historical references.
# litex-skills
