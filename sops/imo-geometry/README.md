# IMO geometry workflow

Start with [litex-basics](../../skills/litex-basics/SKILL.md); use its sets/functions
and logic/scope topics when the geometry interface or proof requires them.

Use this workflow for a contest geometry problem. The hub's general skills
also support other mathematics; this workflow is not their universal entrypoint.

Resolve the live corpus with [reference routing](../../skills/litex-reference/SKILL.md).
Start at level 2 with `showcases/2D_Geometry/README.md`, choose the actual
library/solution entry and inspect its configuration, assumptions and model.
Use level 1 for local proof steps and level 3 for uncertain semantics.

1. Read the original problem, identify its carriers/nondegeneracy and state the
   mathematical proof idea. Resolve the actual geometry library and its trust
   boundary; validate that intended dependency before using it.
2. Use [concept modeling](../../skills/litex-concept-modeler/SKILL.md) and
   [strict definitions](../../skills/litex-strict-definitions/SKILL.md) for the
   formal statement, retaining the source's conditions and conclusion.
3. Use [proof writing](../../skills/litex-proof-writer/SKILL.md) and relevant
   [calculation cards](../../skills/litex-equality-inequality/SKILL.md). Preserve
   accepted context in one live `-session` across ordinary failed statements.
   Load it once, repair the failed statement there, and never rerun the whole
   file after adding a few lines. See the [command comparison](../../skills/litex-reference/references/execution.md#file-and-session).
4. Save each problem's source and actual module configuration in its owning
   project. For several parts keep separate answer sources and ordered exports.
   Verify the saved sources and the intended complete module; use strict mode
   when the delivery must exclude assumptions. Record remaining proof debt.
5. Retain source statements, the proof idea, verifier version/commands and
   final evidence. Summarize reusable lessons only from verified behavior.

Use [reference routing](../../skills/litex-reference/SKILL.md) for current
language and CLI rules. A full version-matched corpus supplies the larger
2D_Geometry collection; curated snapshots are an explicit offline fallback.

## Historical package

[The previous package](../../examples/generic-agent/legacy_imo_package/README.md) and its documents, Python tools,
geometry library and question JSON remain together for source traceability.
They were moved without editing their mathematical content. Their Generic
Agent-specific logging engine is not included; old command flags, paths,
syntax claims and workflow prerequisites are historical rather than the current
hub execution contract. Do not run a legacy tool as a fresh supported workflow
without reviewing its dependencies and generated templates against your version.

Runtime logs and generated answers belong in the user's project. This hub
does not make an agent-specific log format a prerequisite for all proof writing.
