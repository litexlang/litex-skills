# IMO geometry workflow

Use this workflow for a contest geometry problem. The hub's general skills
also support other mathematics; this workflow is not their universal entrypoint.

1. Read the original problem, identify its carriers/nondegeneracy and state the
   mathematical proof idea. Resolve the actual geometry library and its trust
   boundary; validate that intended dependency before using it.
2. Use [concept modeling](../../skills/litex-concept-modeler/SKILL.md) and
   [strict definitions](../../skills/litex-strict-definitions/SKILL.md) for the
   formal statement, retaining the source's conditions and conclusion.
3. Use [proof writing](../../skills/litex-proof-writer/SKILL.md) and relevant
   [calculation cards](../../skills/litex-equality-inequality/SKILL.md). Preserve
   accepted Session context across ordinary failed statements.
4. Save each problem's source and actual module configuration in its owning
   project. For several parts keep separate answer sources and ordered exports.
   Verify the saved sources and the intended complete module; use strict mode
   when the delivery must exclude assumptions. Record remaining proof debt.
5. Retain source statements, the proof idea, verifier version/commands and
   final evidence. Summarize reusable lessons only from verified behavior.

Use [reference routing](../../skills/litex-reference/SKILL.md) for current
language and CLI rules. A full version-matched corpus supplies the larger
2D_Geometry collection when the curated subset is insufficient.

## Historical package

[The previous package](../../../generic_agent_example/legacy_imo_package/README.md) and its documents, Python tools,
geometry library and question JSON remain together for source traceability.
They were moved without editing their mathematical content. Their Generic
Agent-specific logging engine is not included; old command flags, paths,
syntax claims and workflow prerequisites are historical rather than the current
hub execution contract. Do not run a legacy tool as a fresh supported workflow
without reviewing its dependencies and generated templates against your version.

Runtime logs and generated answers belong in the user's project. This hub
does not make an agent-specific log format a prerequisite for all proof writing.
