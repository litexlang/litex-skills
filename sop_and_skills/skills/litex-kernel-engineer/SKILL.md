---
name: litex-kernel-engineer
description: Develop the golitex Rust parser, verifier, runtime and mathematical rules. Use for authorized kernel implementation and focused acceptance; ordinary proof authoring has a separate skill.
---

# litex-kernel-engineer

Apply [golitex repository policy](../golitex-repository-policy/SKILL.md)
before implementation. Start from a minimal real caller and the established
mathematical/current contract; trace the earliest unsupported owner.

Do not modify Runtime, Env, their state contracts, or Stmt/Obj/Fact payload
structures without the user's authorization for that concrete change. Read
[the AST gate](../litex-ast-struct-authorization/SKILL.md). A general feature
request does not authorize these representation changes.

Use Runtime::exec_stmt for statement entry so the temporary environment owns
commit/discard. Use nested verify/store APIs for proof work. Read
[pipeline result types](../litex-pipeline-result-types/SKILL.md) when changing
typed stage evidence and [rule patterns](references/rule-patterns.md) for a
mathematical rule. The [source guide](references/source-guide.md) retains the
full kernel conventions and focused acceptance obligations.

Retain a representative positive and the nearest invalid or unsupported
negative. Choose verification by semantic impact; use the current execution
contract rather than historical flags. Migration triage uses
[example migration](../litex-example-migration/SKILL.md).

## Execution and scope

Use [the current execution contract](../litex-reference/references/execution.md)
and the target version's Manual and CLI. Repository rules in the imported notes
apply inside golitex; outside that repository use the owning project's paths
and user-authorized trust policy. Existing skill references are conditional
reading routes, not instructions to load every skill.
