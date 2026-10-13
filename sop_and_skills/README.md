# Litex SOPs and Skills

This directory contains the reusable Litex skills, SOPs, and reference material
at the core of the repository. People and agents with the required file and
execution capabilities can use them.

- `skills/`: task-specific skills and their supporting documents.
- `sops/`: workflows that combine skills to complete a task.
- `references/`: shared language docs, examples, provenance, and validation.
- `scripts/`: package checks.

## Start here

1. Look up language rules, commands, or examples: [litex-reference](skills/litex-reference/SKILL.md).
2. Write or repair a proof: [litex-proof-writer](skills/litex-proof-writer/SKILL.md).
3. Design a definition or mathematical interface: [litex-concept-modeler](skills/litex-concept-modeler/SKILL.md).
4. Solve a geometry problem: [IMO geometry SOP](sops/imo-geometry/README.md).

A complete checkout includes the skills, reference documents, and selected
examples. This import used local sources and Litex 1.0.6-beta. With another
version, check `litex -version`, `litex -help`, and matching documentation.
Original skill guides are retained as source-guide.md references; the
[current execution contract](skills/litex-reference/references/execution.md)
supersedes their historical command recipes.

## Main authoring skills

| Skill | When to use it |
| --- | --- |
| [litex-reference](skills/litex-reference/SKILL.md) | Language rules, CLI, small examples, and complete mathematical projects |
| [litex-proof-writer](skills/litex-proof-writer/SKILL.md) | Proof construction, debugging, and verification |
| [litex-concept-modeler](skills/litex-concept-modeler/SKILL.md) | Concepts, definitions, and reusable interfaces |
| [litex-strict-definitions](skills/litex-strict-definitions/SKILL.md) | Carriers, domains, and nondegeneracy |
| [litex-equality-inequality](skills/litex-equality-inequality/SKILL.md) | Equality chains, inequalities, and calculations |
| [litex-math-textbook-translator](skills/litex-math-textbook-translator/SKILL.md) | Textbooks, lecture notes, and batches of mathematical material |
| [litex-example-migration](skills/litex-example-migration/SKILL.md) | Example failures after a version change |

## Supporting skills

| Skill | Purpose |
| --- | --- |
| [litex-research-writer](skills/litex-research-writer/SKILL.md) | Explanations, module docs, research material, and comparisons |
| [todo-writer](skills/todo-writer/SKILL.md) | Source-owned blockers and solved experiences |
| [Lean Adapter / Final](skills/litex-generated-lean-to-standard-lean-adapter-writer/SKILL.md) | Native Lean/Mathlib consumers of generated proofs |

## golitex development and maintenance

These skills cover the kernel, result types, and compiler. An ordinary proof
task uses their material only when relevant; writing Litex does not by itself
require kernel development.

| Skill | Purpose |
| --- | --- |
| [golitex-repository-policy](skills/golitex-repository-policy/SKILL.md) | This maintainer's repository working agreements |
| [litex-kernel-engineer](skills/litex-kernel-engineer/SKILL.md) | Rust kernel, parsing, verification, and mathematical rules |
| [litex-pipeline-result-types](skills/litex-pipeline-result-types/SKILL.md) | Verify/exec results and typed evidence |
| [litex-ast-struct-authorization](skills/litex-ast-struct-authorization/SKILL.md) | Authorization boundary for AST representation changes |
| [litex-to-lean-compiler](skills/litex-to-lean-compiler/SKILL.md) | Compiler and semantic bridge; litex-to-lean remains a compatibility entrypoint |

## References and SOPs

- [Curated references](references/litex/README.md): docs, small examples, and teaching modules.
- [Source provenance](references/sources.md): origins, versions, hashes, and receipt summaries.
- [IMO geometry workflow](sops/imo-geometry/README.md): skills combined for a specific task.
- Use `LITEX_REFERENCE_ROOT` for a full version-matched local corpus. The local
  litex-resources checkout currently points to litexlang/litex-doc; that GitHub
  entrypoint remains unconfirmed. The public language source repository is
  [golitex](https://github.com/litexlang/golitex).

## Adding content

Add a skill under `skills/<name>/SKILL.md` with its own references, scripts,
and assets. Link related skills and shared material where the task needs them.
Update this index and source provenance, and preserve local reference targets.
See the [contribution guide](../CONTRIBUTING.md).

From this directory:

```sh
python3 scripts/check_hub.py
```

The checker verifies skill entries, local file links, and recorded hashes. It
does not rerun all historical mathematical cases. Verify a source with the
actual Litex version before relying on it. The golitex reference material
includes its upstream license; this import adds no new license grant for the
personal skills. See [source provenance](references/sources.md).
