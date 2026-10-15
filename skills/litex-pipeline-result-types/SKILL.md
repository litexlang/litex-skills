---
name: litex-pipeline-result-types
description: Design and audit golitex verify and exec result types. Use for sequential stage structs, mirrored dispatcher enums and typed evidence consumed by downstream stages.
---

# litex-pipeline-result-types

Read the [source guide](references/source-guide.md) for the exact stage
ownership and representative Rust shapes before changing a result type.
Sequential pipelines return structs whose fields follow executed stages;
dispatch enums recursively mirror the selected execution/verification branch.

Preserve typed producer/consumer evidence instead of flattening distinct legal
states into optional fields or unrelated success flags. Read the nearby
reference examples only for the family being changed. Apply
[kernel engineering](../litex-kernel-engineer/SKILL.md) and its authorization
gates when implementation changes core representations.

## Execution and scope

Use [the current execution contract](../litex-reference/references/execution.md)
and the target version's Manual and CLI. Repository rules in the imported notes
apply inside golitex; outside that repository use the owning project's paths
and user-authorized trust policy. Existing skill references are conditional
reading routes, not instructions to load every skill.
