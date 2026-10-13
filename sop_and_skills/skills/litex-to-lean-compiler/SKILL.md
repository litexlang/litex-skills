---
name: litex-to-lean-compiler
description: Develop and audit the Litex-to-Lean compiler and its semantic bridge. Use for typed-result replay, supported routes and generated example pairs.
---

# litex-to-lean-compiler

Use the existing verified typed execution results, scoped fact citations
and well-definedness evidence to replay a supported Litex proof into Lean.
Read the [source guide](references/source-guide.md) for the active compiler
contract, unsupported routes and generated-pair acceptance requirements.

Apply [kernel engineering](../litex-kernel-engineer/SKILL.md) for changes in
the Rust pipeline and [result-type design](../litex-pipeline-result-types/SKILL.md)
for evidence interfaces. Generated files remain compiler owned. A successful
Litex run does not establish Lean compilation or Mathlib-facing acceptance.

For handwritten native consumers after output exists use
[the Adapter/Final skill](../litex-generated-lean-to-standard-lean-adapter-writer/SKILL.md).
For ordinary CLI usage read the target version's compiler guide through
[reference routing](../litex-reference/SKILL.md).

## Execution and scope

Use [the current execution contract](../litex-reference/references/execution.md)
and the target version's Manual and CLI. Repository rules in the imported notes
apply inside golitex; outside that repository use the owning project's paths
and user-authorized trust policy. Existing skill references are conditional
reading routes, not instructions to load every skill.
