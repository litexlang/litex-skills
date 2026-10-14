# Litex SOPs and Skills

Load a small foundation, choose the task, then read the mathematical topic or
live source needed for the next decision. Skill directories remain flat so
existing references keep working; [profiles.json](profiles.json) determines
which material is exported.

**Author in one live `-session`.** Ordinary failed statements retain earlier
accepted work. Repair the failed statement and continue in that process. Run
the saved file cleanly at a coherent checkpoint or final delivery. The
[comparison](skills/litex-reference/references/execution.md#file-and-session)
shows the difference between independent commands and a retained context.

## Layer 1: foundation

Read [litex-basics](skills/litex-basics/SKILL.md) before an unfamiliar Litex task.
It teaches the working model, a runnable start, major syntax, ordinary
mathematical expression and common easy-to-misread boundaries. It includes
complete positive examples and explicitly rejected controls. A Litex executable
is enough to run the starter; a sibling source checkout is optional here.

## Layer 2: choose the task

| Task | Skill |
| --- | --- |
| Write, repair or simplify a proof | [litex-proof-writer](skills/litex-proof-writer/SKILL.md) |
| Model a concept, definition or reusable interface | [litex-concept-modeler](skills/litex-concept-modeler/SKILL.md) |
| Translate a textbook, chapter or source batch | [litex-math-textbook-translator](skills/litex-math-textbook-translator/SKILL.md) |
| Review mathematical intent, checking and trust | [litex-review](skills/litex-review/SKILL.md) |
| Diagnose failures after a version change | [litex-example-migration](skills/litex-example-migration/SKILL.md) |
| Explain Litex, document a module or compare systems | [litex-research-writer](skills/litex-research-writer/SKILL.md) |
| Record a source-owned blocker or solved experience | [todo-writer](skills/todo-writer/SKILL.md) |
| Consume generated proofs through Adapter/Final | [Lean adapter writer](skills/litex-generated-lean-to-standard-lean-adapter-writer/SKILL.md) |

Review is read-only unless changes are requested. Proof authoring does not
implicitly authorize changing the parser, verifier, mathematical statement or
trust assumptions. The [geometry SOP](sops/imo-geometry/README.md) combines
selected skills for a specific task. For a complete install-to-answer walkthrough,
use the [Generic Agent geometry experiment](../generic_agent_example/README.md).

## Layer 3: read the needed mathematical topic

The foundation's [topic index](skills/litex-basics/references/topics.md) routes
to six short guides. They are conditional references rather than six mandatory
skills loaded for every problem.

| Topic | Guide | Further skill when needed |
| --- | --- | --- |
| Algebra and inequalities | [algebra](skills/litex-basics/references/topics/algebra.md) | [equality/inequality](skills/litex-equality-inequality/SKILL.md) |
| Sets, carriers and function domains | [sets/functions](skills/litex-basics/references/topics/sets-functions.md) | [strict definitions](skills/litex-strict-definitions/SKILL.md) |
| Witnesses, existence and uniqueness | [existence](skills/litex-basics/references/topics/existence.md) | Concept modeling |
| Quantifiers, proof blocks and scope | [logic/scope](skills/litex-basics/references/topics/logic-scope.md) | Proof writing |
| Induction, indexed functions and recursion | [induction](skills/litex-basics/references/topics/induction.md) | Proof writing / concept modeling |
| Modules, export names and context | [modules](skills/litex-basics/references/topics/modules.md) | Reference / migration |

[Misconception cards](skills/litex-basics/references/misconceptions.md) connect
common wrong interpretations to corrected patterns and runnable controls.

## Live reference depth: a separate choice

[litex-reference](skills/litex-reference/SKILL.md) owns corpus resolution and
progressive reading. Select the source depth by the current question, regardless
of which task or topic skill is active.

| Depth | Read |
| --- | --- |
| 0 | Corpus location, Agent Guide and relevant CLI contract |
| 1 | Relevant cheatsheet section and a small live example |
| 2 | A selected showcase's interfaces, source and dependencies |
| 3 | Exact Manual/CLI sections and positive/negative controls |

In this repository the default is `../golitex` from the **hub repository root**.
An explicit `LITEX_REFERENCE_ROOT` overrides it. Installed skills use an explicit
root or a verified personal location hint, never a relative sibling of their
installation directory. See [actual reading routes](skills/litex-reference/references/live-reading.md).
Do not load entire trees. [Bundled snapshots](references/litex/README.md) and
expanded `source-guide.md` archives are dated fallbacks, not required startup
reading; their historical command recipes may differ from the target version.

## Maintainer skills: explicit selection

These six skills concern the golitex repository or implementation and are
excluded from the default author pack. Within golitex, its repository policy
still applies to all work there.

| Skill | Purpose |
| --- | --- |
| [golitex-repository-policy](skills/golitex-repository-policy/SKILL.md) | Repository working agreements |
| [litex-kernel-engineer](skills/litex-kernel-engineer/SKILL.md) | Parser, verifier, runtime and mathematical rules |
| [litex-ast-struct-authorization](skills/litex-ast-struct-authorization/SKILL.md) | Authorization for AST representation changes |
| [litex-pipeline-result-types](skills/litex-pipeline-result-types/SKILL.md) | Verify/exec result architecture |
| [litex-to-lean-compiler](skills/litex-to-lean-compiler/SKILL.md) | Compiler and semantic bridge |
| [litex-to-lean](skills/litex-to-lean/SKILL.md) | Compatibility entrypoint for the compiler skill |

## Export and validation

From the repository root, export `basics`, `author` (default), or the full
`maintainer` edition to a new external directory:

```sh
python3 sop_and_skills/scripts/export_skills.py --profile author --output /tmp/litex-author-pack
python3 sop_and_skills/scripts/check_hub.py
```

The lightweight packs preserve all their local Markdown dependencies and omit
historical archives, full language snapshots and maintainer skills. The full
maintainer edition preserves the source scopes, including shared references;
keep that layout when following its links. No exporter changes agent settings
or overwrites an existing installation.

See [contribution rules](../CONTRIBUTING.md), [source provenance](references/sources.md)
and [validation](references/validation.md). Package checks do not verify every
historical theorem or establish agent behavior. The golitex snapshots include
the upstream license; importing personal skills adds no new license grant.
