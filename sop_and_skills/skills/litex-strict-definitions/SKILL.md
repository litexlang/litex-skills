---
name: litex-strict-definitions
description: Review Litex definitions for exact carriers, parameter domains and concept-owned nondegeneracy. Use when defining or revising mathematical interfaces.
---

# litex-strict-definitions

Put mathematical carriers, parameter domains and concept-owned
nondegeneracy in the definition rather than leaving them to later comments.
Do not strengthen or narrow a concept beyond its intended meaning merely to
make the proof easier.

For example, a circle radius is positive; a line through two defining points
requires distinct points. A midpoint of an arbitrary pair and a segment's
midpoint may intentionally have different degeneracy contracts.

After revising a definition align dependent statements and run representative
uses with their actual imports. Never weaken the definition to preserve an old
proof. Use [concept modeling](../litex-concept-modeler/SKILL.md) for the interface
choice and the [source guide](references/source-guide.md) for the original review criteria.

## Execution and scope

Use [the current execution contract](../litex-reference/references/execution.md)
and the target version's Manual and CLI. Repository rules in the imported notes
apply inside golitex; outside that repository use the owning project's paths
and user-authorized trust policy. Existing skill references are conditional
reading routes, not instructions to load every skill.
