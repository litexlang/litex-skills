---
name: litex-ast-struct-authorization
description: Apply the maintainer authorization boundary for Litex statement, object and fact AST structures. Use before proposing a concrete AST representation change.
---

# litex-ast-struct-authorization

Do not add, remove, rename or retype Stmt, Obj, Fact, their payload/leaf
fields or enum shapes without the user's authorization for that concrete
change. Shared leaves such as Identifier and binder payloads are included.

Before a protected edit show the exact current and proposed type shape, the
state or semantics it represents, why unchanged existing fields or derived
values cannot support the task, and its ownership/lifetime consequences.
Wait for the user's concrete authorization unless that same change is already
authorized. A surrounding feature request does not waive this boundary.

Read [the source gate](references/source-guide.md) for the full scope and
[repository policy](../golitex-repository-policy/SKILL.md) for Env/Runtime
changes. Read-only inspection and code using unchanged representations remain
available while an architectural decision is pending.

## Execution and scope

Use [the current execution contract](../litex-reference/references/execution.md)
and the target version's Manual and CLI. Repository rules in the imported notes
apply inside golitex; outside that repository use the owning project's paths
and user-authorized trust policy. Existing skill references are conditional
reading routes, not instructions to load every skill.
