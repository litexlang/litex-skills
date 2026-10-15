# Live corpus resolution and topic routes

Paths below are relative to the resolved `LITEX_CORPUS_ROOT`. The directory
is **`showcases/`**, plural. Search and read only what the current task needs.

## Resolve once per task

1. Honor a user-selected corpus or `LITEX_REFERENCE_ROOT`. Resolve relative
   paths from the task workspace and check `docs/`, `examples/`, `showcases/`.
   Report an invalid explicit path; do not silently substitute another corpus.
2. Inside golitex use its actual repository root. For this hub use `../golitex`
   from the `litex-skills` repository root. Establish that root before resolving
   from a nested directory; never interpret the path relative to an installed
   skill or an arbitrary shell directory.
3. An installed personal copy may have `references/local-corpus.md` containing
   a verified absolute root hint. Read it if needed and check that the root
   still exists. It provides a location, not additional language rules.
4. If the intended root cannot be established, request its location. Do not
   search an entire home directory or silently use an old copied corpus.

From this hub's repository root:

```bash
LITEX_CORPUS_ROOT="$(cd ../golitex && pwd -P)"
rg --files "$LITEX_CORPUS_ROOT/examples" -g '*.lit'
```

For an explicit root use its checked absolute path. Keep the task variable
local; do not change global environment or copy golitex into a skill. A root
can be a worktree: do not assume `.git` is a directory. Check the selected
executable's version/help before applying another checkout's commands.

## Level 0: context

Read the short `docs/AgentGuide.md` for Session startup, retention and replay.
Read the relevant `docs/cli.md` section for invocation/output. For a first
encounter `docs/Learn_Litex.md` explains the reading model. Use the live Chinese
counterparts when they match the task's language/version. This does not require
a complete module run or reading the entire Manual.

## Level 1: the next statement or proof move

Read the relevant `docs/Litex_Learner_Cheatsheet.md` section. Use
`examples/README.md` to find the current family, then its README when present
and a small complete `.lit` with the needed declarations/configuration.
Negative fixtures are expected to fail; `_internal/` and dated inventories
are not default authoring templates.

| Question | Initial live path | Next search/read |
| --- | --- | --- |
| Statement or construction | `examples/stmt_nodes/README.md` | `have`, `claim`, `prop`, `forall`, `witness`; selected statement family |
| Function by unique existence | `examples/have_fn_by_unique_existence.lit` | relation, existence and uniqueness proof, function use |
| Claim / witness / scope | `examples/claim_obtain_scope.lit` | enclosing scope and `obtain`, `claim`, `witness` |
| Equality / atomic proof move | `examples/proof_nodes/README.md` | `by def`, `by thm`, `by cases`, `by induc`; matching family |
| Already inferred consequence | `examples/infer/README.md` | fact producer and consuming statement |
| Domains / well-definedness | `examples/wd/README.md`, `examples/wd_negative/README.md` | exact call/domain; matching positive and rejection |
| Imports / export order | `examples/module_manager/README.md` | nearest fixture's `litex.config` and ordered sources |
| Unicode / token shape | `examples/tokenize/README.md` | exact token in its complete example |

Unique-existence authoring goes directly to the real example:

```bash
sed -n '1,100p' "$LITEX_CORPUS_ROOT/examples/have_fn_by_unique_existence.lit"
```

For an unfamiliar move discover filenames, then search one family:

```bash
rg --files "$LITEX_CORPUS_ROOT/examples/proof_nodes" -g '*cases*.lit' -g '*induc*.lit'
rg -n -g '*.lit' 'by cases|by induc' "$LITEX_CORPUS_ROOT/examples/proof_nodes"
```

Stop widening once a useful pattern is found. Read the applicable block with
all its assumptions; a search hit or isolated theorem body is not its interface.

## Level 2: mathematical developments and reusable interfaces

Use `showcases/README.md` to choose by purpose and subject, then the selected
collection's README. Read `math_collections.md` and `litex.config` when present,
and only the source items needed for the intended interface. Check preceding
exports/imports; a chapter need not be standalone. If the README identifies a
different canonical workspace, follow that actual source location.

| Task | Live entrypoint |
| --- | --- |
| Proof-writing tutorial | `showcases/The-Mechanics-of-Litex-Proof/README.md` |
| Limits / sequences / a compact analysis development | `showcases/analysis_notes/README.md` |
| Source-ordered analysis chapter | `showcases/analysis/README.md` |
| Sets / functions / recursion / algebraic structures | `showcases/Mathematics-in-Litex/README.md` |
| Coordinate operations / spaces / bases | `showcases/linear_algebra/README.md` |
| Geometry library or IMO solution | `showcases/2D_Geometry/README.md` |
| Inequality problem and proof spine | `showcases/imo_inequalities/README.md` |
| Subject-specific mathematics | `showcases/math_concepts_in_litex/README.md`, then the selected subject |
| A verified function with executable cases | `showcases/Write_Mathematically_Correct_Code_With_Litex/README.md` |

For the last route, read that README and `math_collections.md`, inspect its
`litex.config`, then find `newton_sqrt_two_step` in `main.lit` and read the
complete definition/proof. Its exact-real model and target floating-point
boundary remain part of the example. A scalar geometry variant, axiom, trust
or omitted branch likewise does not transfer an unrestricted guarantee.

## Level 3: exact semantics and diagnostic boundaries

Find headings and the exact construct before reading long documents:

```bash
rg -n '^#{1,4} .*([Uu]nique|[Ee]xist|[Ff]unction)' "$LITEX_CORPUS_ROOT/docs/Manual.md"
rg -n '^## (Session Flag|JSON Output Contract|Project Modules)' "$LITEX_CORPUS_ROOT/docs/cli.md"
```

Read the matching section with a live positive example and the nearest negative
control when available. Compile/export questions use the relevant compiler
guide; public explanations use `docs/Litex_Blueprint.md`. A proof-search miss
alone is not a counterexample or evidence of a bug. Return to the authoring
Session with the smallest justified correction.

## Evidence and fallback

Record the selected level, actual files/sections and the choice they informed
in existing task notes or a short update. Distinguish reading from current
verification. Stop once the needed contract and route are known.

The hub's `references/litex/` and an installed skill's old
`references/litex-corpus/` are explicit offline/historical alternatives. If
live sources are unavailable, name that limitation and the snapshot's recorded
version before using it. It must not silently override the live tree or become
a current-support claim. A passing old receipt needs target-executable replay.
