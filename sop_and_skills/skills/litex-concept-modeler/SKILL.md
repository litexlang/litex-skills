---
name: litex-concept-modeler
description: Choose Litex interfaces for mathematical definitions and reusable concepts before proof writing. Use for carrier, function, predicate, struct and module design decisions.
---

# litex-concept-modeler

Start from the intended mathematics and downstream uses. Separate the role
of a carrier, value, callable function, relation, structure and theorem from
its implementation and proof status. The desired conclusion does not justify
inventing a premise or weakening a definition.

For one interface read [concept forms](references/concept-forms.md). For a
canonical selected value or a non-obvious function-versus-predicate choice also
read [construction and selection](references/construct-selection.md). For a
chapter or domain read [dependencies](references/dependency-dag.md); for module
documentation read [the documentation guide](references/module-documentation.md)
and use [the inventory template](assets/math_collections.template.md).

Apply [strict definitions](../litex-strict-definitions/SKILL.md). Put exact
carriers and concept-owned nondegeneracy in the definition. For data bundled
with laws prefer a primary struct when the intended interface consumes values;
use propositions for independent relations. Treat this as a modeling choice,
not a restriction on supported syntax.

Show one intended use and the nearest unsuitable alternative before scaling
up the model. Distinguish designed, checked, assumed and blocked interfaces.
The [source guide](references/source-guide.md) retains the full modeling modes.

## Execution and scope

Use [the current execution contract](../litex-reference/references/execution.md)
and the target version's Manual and CLI. Repository rules in the imported notes
apply inside golitex; outside that repository use the owning project's paths
and user-authorized trust policy. Existing skill references are conditional
reading routes, not instructions to load every skill.
