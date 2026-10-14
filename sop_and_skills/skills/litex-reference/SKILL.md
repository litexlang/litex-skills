---
name: litex-reference
description: Read the live golitex docs, examples and showcases at the depth needed for Litex authoring. Use before writing .lit code, choosing a proof or interface shape, or diagnosing language and CLI behavior.
---

# Litex reference

For the working model, runnable starter, main syntax, common mathematical
patterns and misconception checks, start with
[litex-basics](../litex-basics/SKILL.md). This skill owns deeper source lookup;
do not require a sibling checkout merely to run the packaged starter examples.

**Before writing Litex, resolve the live corpus and read the relevant source.**
For this hub's paired checkout it is `../golitex`, resolved from the
`litex-skills` repository root, not this skill's directory. Follow the
[root resolution and topic routes](references/live-reading.md); retain the
checked absolute path as `LITEX_CORPUS_ROOT` for the task.

The live tree supplies three complementary sources: `docs/` owns language,
CLI and authoring contracts; `examples/` supplies small concrete patterns and
rejection controls; `showcases/` supplies mathematical developments, reusable
interfaces and worked proofs.

## Choose the reading depth

| Level | Trigger | Read | Stop when |
| --- | --- | --- | --- |
| 0 — Orient | Start authoring or switch corpus/executable | Resolve the root; read `docs/AgentGuide.md` and the relevant CLI contract. | Corpus, Session command and task context are known. |
| 1 — Local move | A statement, definition or proof step | Relevant Learner Cheatsheet section, matching examples family and a small complete `.lit`. | Syntax, premises and a suitable local move are understood. |
| 2 — Development | Reusable interface, long proof, chapter or dependencies | Selected showcase README, `math_collections.md` and `litex.config` when present; selected source and preceding dependencies. | Interface, proof spine, imports and assumptions are understood. |
| 3 — Exact boundary | Unclear semantics, unexplained failure or a support claim | Relevant Manual/CLI section plus matching positive and negative examples. | The supported contract or concrete unresolved gap is identified. |

Levels control depth, not source authority. Jump to level 3 for an exact
syntax/CLI question; a chapter may start at level 2. Do not force every task
through every level or load entire trees. Search filenames, then the smallest
topic directory/document heading. Read enough surrounding declarations and
assumptions to understand the selected source; a search hit is not its interface.

## Use what you read

State the mathematical idea, adapt the pattern to actual domains and premises,
and verify it in the target context. Preserve its assumption/negative boundary.
A showcase with trust, axioms, scalar models or omitted branches does not prove
an unrestricted checked theorem.

**Author in one live `-session`.** Load accepted context once; repair ordinary
failed statements there, retaining earlier accepted definitions and facts.
Never rerun the whole file after adding a few lines. The live Agent Guide/CLI
own Session behavior and the separate clean-file acceptance gate.

Record the selected level, actual source paths/sections and what choice they
informed in existing task notes or a short update. Reading is not current
verification. Stop once the needed contract and route are known; return to the
next unresolved question after actual feedback.

## Authority and fallback

Use target-version live docs for contracts, live examples for usage/controls,
and the chosen showcase for its mathematical interface. Skills guide choices;
dated receipts and copied corpora describe their recorded version.

If the live root is unavailable, report it before using an explicitly named
offline snapshot. Do not silently substitute bundled docs or an unrelated
checkout. Current support still needs verification with the target executable.

Use [proof writing](../litex-proof-writer/SKILL.md) for the authoring loop,
[concept modeling](../litex-concept-modeler/SKILL.md) for an unsettled interface,
and [migration](../litex-example-migration/SKILL.md) for version discrepancies.
