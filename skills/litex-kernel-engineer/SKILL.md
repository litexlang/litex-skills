---
name: litex-kernel-engineer
description: Develop the golitex Rust parser, verifier, runtime and mathematical rules. Use for authorized kernel implementation and focused acceptance; ordinary proof authoring has a separate skill.
---

# litex-kernel-engineer

**When iterating on Litex reproducers or examples, keep one live `-session`.**
Ordinary failure preserves accepted context; do not rerun the full file for
each small edit. To adopt a rebuilt executable, save accepted source, restart
and replay it as described in the [Session contract](../litex-reference/references/execution.md#file-and-session).

Apply [golitex repository policy](../golitex-repository-policy/SKILL.md)
before implementation. Start from a minimal real caller and the established
mathematical/current contract; trace the earliest unsupported owner.

Use [live reference routing](../litex-reference/SKILL.md) to inspect the actual
caller: level 1 for a minimal example, level 2 for its showcase/interface,
and level 3 for the exact documented semantics and rejection boundary.
Source inspection does not authorize kernel changes or imply a fixture passed.

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
