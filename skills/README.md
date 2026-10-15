# Litex SOPs and Skills

Load a small foundation, choose the task, then read the mathematical topic or
live source needed for the next decision. Skill directories remain flat so
existing references keep working; [profiles.json](../profiles.json) determines
which material is exported.

**Author in one live `-session`.** Ordinary failed statements retain earlier
accepted work. Repair the failed statement and continue in that process. Run
the saved file cleanly at a coherent checkpoint or final delivery. The
[comparison](litex-reference/references/execution.md#file-and-session)
shows the difference between independent commands and a retained context.

## Layer 1: language competence (layered)

| Skill | Role |
| --- | --- |
| [litex-basics](litex-basics/SKILL.md) | Session, core syntax, `cart` / coordinates, small defs & short proofs (API smoke default) |
| [litex-intermediate](litex-intermediate/SKILL.md) | Cases, induction, richer proof methods (stub → filling) |
| [litex-advanced](litex-advanced/SKILL.md) | Modules, large interfaces, multi-skill workflows (stub → filling) |

For pure-API skill evaluation inject **only** `litex-basics/SKILL.md` until the
basic layer passes a mini suite. See
[examples/skill-api-smoke](../examples/skill-api-smoke/README.md).

## Layer 2: choose the task

| Task | Skill |
| --- | --- |
| Write, repair or simplify a proof | [litex-proof-writer](litex-proof-writer/SKILL.md) |
| Model a concept, definition or reusable interface | [litex-concept-modeler](litex-concept-modeler/SKILL.md) |
| Translate a textbook, chapter or source batch | [litex-math-textbook-translator](litex-math-textbook-translator/SKILL.md) |
| Review mathematical intent, checking and trust | [litex-review](litex-review/SKILL.md) |
| Diagnose failures after a version change | [litex-example-migration](litex-example-migration/SKILL.md) |
| Explain Litex, document a module or compare systems | [litex-research-writer](litex-research-writer/SKILL.md) |
| Record a source-owned blocker or solved experience | [todo-writer](todo-writer/SKILL.md) |
| Consume generated proofs through Adapter/Final | [Lean adapter writer](litex-generated-lean-to-standard-lean-adapter-writer/SKILL.md) |

Review is read-only unless changes are requested. Proof authoring does not
implicitly authorize changing the parser, verifier, mathematical statement or
trust assumptions. The [geometry SOP](../sops/imo-geometry/README.md) combines
selected skills for a specific task. For a complete install-to-answer walkthrough,
use the [Generic Agent geometry experiment](../examples/generic-agent/README.md).

## Layer 3: read the needed mathematical topic

The foundation's [topic index](litex-basics/references/topics.md) routes
to six short guides. They are conditional references rather than six mandatory
skills loaded for every problem.

| Topic | Guide | Further skill when needed |
| --- | --- | --- |
| Algebra and inequalities | [algebra](litex-basics/references/topics/algebra.md) | [equality/inequality](litex-equality-inequality/SKILL.md) |
| Sets, carriers and function domains | [sets/functions](litex-basics/references/topics/sets-functions.md) | [strict definitions](litex-strict-definitions/SKILL.md) |
| Witnesses, existence and uniqueness | [existence](litex-basics/references/topics/existence.md) | Concept modeling |
| Quantifiers, proof blocks and scope | [logic/scope](litex-basics/references/topics/logic-scope.md) | Proof writing |
| Induction, indexed functions and recursion | [induction](litex-basics/references/topics/induction.md) | Proof writing / concept modeling |
| Modules, export names and context | [modules](litex-basics/references/topics/modules.md) | Reference / migration |

[Misconception cards](litex-basics/references/misconceptions.md) connect
common wrong interpretations to corrected patterns and runnable controls.

## Live reference depth: a separate choice

[litex-reference](litex-reference/SKILL.md) owns corpus resolution and
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
installation directory. See [actual reading routes](litex-reference/references/live-reading.md).
Do not load entire trees. [Bundled snapshots](../references/litex/README.md) and
expanded `source-guide.md` archives are dated fallbacks, not required startup
reading; their historical command recipes may differ from the target version.

## Maintainer skills: explicit selection

These six skills concern the golitex repository or implementation and are
excluded from the default author pack. Within golitex, its repository policy
still applies to all work there.

| Skill | Purpose |
| --- | --- |
| [golitex-repository-policy](golitex-repository-policy/SKILL.md) | Repository working agreements |
| [litex-kernel-engineer](litex-kernel-engineer/SKILL.md) | Parser, verifier, runtime and mathematical rules |
| [litex-ast-struct-authorization](litex-ast-struct-authorization/SKILL.md) | Authorization for AST representation changes |
| [litex-pipeline-result-types](litex-pipeline-result-types/SKILL.md) | Verify/exec result architecture |
| [litex-to-lean-compiler](litex-to-lean-compiler/SKILL.md) | Compiler and semantic bridge |
| [litex-to-lean](litex-to-lean/SKILL.md) | Compatibility entrypoint for the compiler skill |

## Export and validation

From the repository root, export `basics`, `author` (default), or the full
`maintainer` edition to a new external directory:

```sh
python3 scripts/export_skills.py --profile author --output /tmp/litex-author-pack
python3 scripts/check_hub.py
```

The lightweight packs preserve all their local Markdown dependencies and omit
historical archives, full language snapshots and maintainer skills. The full
maintainer edition preserves the source scopes, including shared references;
keep that layout when following its links. No exporter changes agent settings
or overwrites an existing installation.

See [contribution rules](../CONTRIBUTING.md), [source provenance](../references/sources.md)
and [validation](../references/validation.md). Package checks do not verify every
historical theorem or establish agent behavior. The golitex snapshots include
the upstream license; importing personal skills adds no new license grant.
