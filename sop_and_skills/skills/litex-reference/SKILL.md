---
name: litex-reference
description: Find the version-matched Litex language rules, commands, proof examples and complete mathematical projects. Use when writing Litex needs authoritative reference material rather than guessing syntax.
---

# Litex reference

Find the smallest relevant reference before guessing syntax, command flags or
builtin support. [The corpus index](../../references/litex/README.md) names the
bundled sources and complete upstream collections. [Source provenance](../../references/sources.md)
records their versions, transformations and unbundled material.

| Need | Read |
| --- | --- |
| First authoring move | [Learner Cheatsheet](../../references/litex/docs/Litex_Learner_Cheatsheet.md) |
| Exact language/domain/proof contract | [Manual](../../references/litex/docs/Manual.md) |
| Commands, JSON and module loading | [CLI](../../references/litex/docs/cli.md) |
| Session context and recovery | [Agent Guide](../../references/litex/docs/AgentGuide.md) and [execution](references/execution.md) |
| A small source example | The relevant file in [the corpus index](../../references/litex/README.md) |
| A complete mathematical interface | Its module README, math_collections.md and selected .lit source |
| Builtin, trust and negative boundaries | [Manual](../../references/litex/docs/Manual.md); retain the actual premises and check the local example |
| Lean export usage | [Compiler Guide](../../references/litex/docs/Litex_To_Lean_Compiler_Guide.md) |

Check the executable version/help and choose references for that version. The
bundled snapshot is not a promise about every installed release. Search a local
corpus with rg, then read only the matching section and complete source context.
Set LITEX_REFERENCE_ROOT to an optional full corpus checkout when this subset
does not cover the task; otherwise follow the recorded upstream source links.
Do not ingest the complete corpus into the prompt.

Language contracts and CLI syntax come from version-matched golitex sources.
Skills supply authoring choices; dated receipts supply historical observations.
A normal proof miss is not a counterexample. Dated success needs replay before
a current-support claim; never silently reinterpret an expected-negative example.

Use [proof writing](../litex-proof-writer/SKILL.md) for the authoring loop,
[concept modeling](../litex-concept-modeler/SKILL.md) for an unsettled interface,
and [migration](../litex-example-migration/SKILL.md) for a version discrepancy.
