# Imported source guide

Source snapshot imported on 2026-10-13. Read this for the author's mathematical methods and scoped repository conventions. Historical CLI recipes and result fields are not current execution instructions; use [the hub execution contract](../../litex-reference/references/execution.md). Apply golitex-specific paths and maintainer rules only when working in that repository. Dated examples require replay before making a current-support claim.


# Litex Kernel Engineer

## Example failures and migration triage

When asked to find examples that cannot run, audit legacy-to-current migration,
or investigate/discuss version regressions, apply
[`litex-example-migration`](../../litex-example-migration/SKILL.md) before proposing
repairs. Use its root-cause and earliest-phase classifications throughout the
investigation and each concrete issue/decision discussion. Rule presence alone
does not establish reachable, composable, or replayable capability.

## Repair ownership in plans

Apply the maintainer's
[two execution categories and discussion boundary](../../golitex-repository-policy/references/task-sop.md#bug-repair-plan-ownership).
Diagnose and complete authorized local Rust semantic repairs without another
permission or maintainer-review round; retain soundness and focused acceptance
evidence. Escalate before a proposed change exceeds that owner or alters an
unsettled contract. The protected-structure gates below still apply.

## Critical: statement entry is only `exec_stmt`

When running or wiring Litex statements in `src/` (runners, REPL, tests, new
call sites):

- Call **`Runtime::exec_stmt` only**.
- Do **not** call `execute_fact_statement`, `exec_let_obj`, `exec_def_prop_stmt`,
  `exec_unsafe_stmt`, or any other `exec_*_stmt` from outside
  `crate::execute`.
- Those branch functions exist solely for `exec_stmt` after it opens the
  transactional temp `ExecEnv`. Bypassing `exec_stmt` breaks Failed-discard /
  Success-merge and can dirty the parent env.
- Inside a statement, use `verify_*` / `store_*` for nested proof work — not a
  second `exec_stmt` and not a direct `exec_xxx_stmt`.

See also `$litex-pipeline-result-types` (“only `exec_stmt` runs statements”).

## Critical: User Approval For Core Struct Changes

Apply the repository policy's
[Env and Runtime authorization gate](../../golitex-repository-policy/references/golitex-agents.md#user-authorization-for-env-and-runtime-changes)
for both legacy code and `src/`. It also protects state-management
contracts and owned containers when no top-level field changes.

Also apply
[Stmt / Obj / Fact AST struct authorization](../../golitex-repository-policy/references/golitex-agents.md#user-authorization-for-stmt--obj--fact-ast-structs)
and `$litex-ast-struct-authorization`: **Do not change Stmt / Obj / Fact structs on your own.** Do not add fields to shared leaves such as `Identifier` to solve a
binder/display problem unless the user explicitly authorizes that concrete
struct change.

Treat `Runtime`, `Env`, `ExecEnv`, `Environment`, `ModuleManager`, and any similarly central
state-owning or system-coordinating struct as user-owned architecture. Before
adding, deleting, moving, renaming, retyping, or changing the responsibility
of any field on one of these structs, stop before editing code and present a
prominent **Core Struct Change Proposal** to the user. State, concretely:

1. the exact struct and field change being proposed;
2. what state or behavior the field represents and which code will use it;
3. why the change is needed now; and
4. why every plausible existing field, owner, or derived/local value cannot
   provide the same capability without the new structural change.

Also describe the lifetime, ownership, initialization, invalidation, and
coupling consequences. Do not bury this notice inside a general plan or status
update. Wait for the user's explicit confirmation before making the structural
change. This approval gate applies even when the edit appears mechanically
small, is required by another requested kernel feature, or removes rather than
adds state. If the need becomes visible only during implementation, pause at
that point and ask; prior approval of the surrounding task is not approval of
the core-struct change. If the user has already explicitly authorized this
concrete change, proceed within that scope without requesting permission again.

## Derive kernel behavior forward

Construct kernel changes in this order: documented/source semantics and a
minimal real reproduction; soundness and state invariants; the owning parser,
runtime, verifier, rule, or diagnostic phase; orthogonal mechanism and policy
boundaries; implementation; positive, negative, and provenance evidence. The
requested passing snippet is a tracer and acceptance target, not a premise
from which to invent a special case.

Use backward reasoning only to extract the semantic boundary and trace a
failure to its earliest owning phase. Repair that phase and re-derive the
downstream behavior instead of adding fact-family, object-shape, call-site, or
rendered-string patches. If the motivating snippet were hidden, every new
field, rule, abstraction, cache key, and helper must still be justified by a
general invariant with a declared owner; otherwise revise the design before
editing.

## Critical: Repository Policy And Verifier Loop

- In the golitex repository, apply `$golitex-repository-policy` alongside this
  skill and read its canonical bundled policy completely. That repository
  policy overrides generic or older guidance here.
- Build current source once with `cargo build --release` and invoke
  `target/release/litex`; never use `target/debug/litex` for Litex work.
- For every iterative `.lit` edit to a registered target, start one
  `target/release/litex -compact -session -before <current-file.lit>` process.
  This loads the configured prefix before the target, excludes the target and
  later files, and enters the target file's environment whether it is empty,
  partial, or failing.
- Submit target statements from the first one in source order, one literal
  outermost `try:` block per regression, declaration, theorem, or small
  fragment. A successful block commits to the session; immediately write the
  accepted source back without the outer `try:`. A failed block rolls back
  only itself; correct and resubmit that block in the same process.
- Once a real proof, library, inference, syntax, or formulation blocker is
  identified, keep the intended statement, use the narrowest legal `trust`,
  record the debt, and continue. Do not spend further proof-search iterations
  unless the user asks to remove that trust.
- Restart only when the process exits or cannot accept another frame, the
  registered prefix deliberately changes, or an already committed declaration
  must be replaced under the same name. Replay the target from its first
  statement after a restart. Record an unexpected unusable session as
  `kernel_problem`.
- Use `target/release/litex -compact -runner -f <current-file.lit>` for a clean
  baseline, checkpoint, or final artifact gate. Use
  `-isolated -runner -f` only for an intentionally standalone repro. Require
  top-level `ok: true` and exit code `0`.
- Reserve `target/release/litex -compact -runner -r <module>` for an explicit complete
  module or repository gate. Classify Rust changes with the repository
  impact-level contract, then run the selected focused/domain/contract gates;
  do not add a broader release test without an evidence-backed escalation.
  Never use the unoptimized default profile for this workflow.

## Tracer bullet

Before changing kernel behavior, select one runnable Litex snippet that
exercises the central user-visible semantics. Preserve its exact before
behavior, make it the first positive regression, and pair any newly accepted
syntax or inference route with the nearest expression that must still fail.
Explain parser, elaboration, runtime, verifier, and provenance changes by
pointing to the exact tracer expression where each phase is visible.

Use chained default struct-view field access as the fixed example. With
`item &TaggedPoint` and `TaggedPoint.point &Coordinates`, the expression
`item.point.x` must lower to
`&Coordinates{&TaggedPoint{item}.point}.x`: the binding selects the first view
and the declared field type selects the second. Keep `point.x.value` as the
negative boundary because a scalar field must not silently acquire another
struct view. This is the model for selecting a task-specific kernel tracer; do
not reuse it for unrelated kernel changes.

### Kernel acceptance file

Every user-visible kernel update must leave a stable runnable tracer `.lit`
file under the nearest existing `examples/` feature or proof-pattern
directory. In that file, preserve the formerly rejected code line-for-line as
`#` comments, keep the newly supported code active, and label the remaining
boundary. Record the focused release command in the file and keep the file
collectible by the examples harness. Run that file directly first; run the
whole harness only when the impact class requires it.

For the fixed field-access model, the acceptance file would comment the old
`item.point.x` attempt and keep the now-valid `item.point.x` assertion active.
Its Rust regression must separately execute and reject `point.x.value`; the
commented line is history, not a test. Use the same before/now/negative shape
for the task's actual tracer.

### New or updated feature → new examples `.lit`

Whenever you add a **new** capability or **widen / update** an existing one
(parser keyword, WD route, builtin/infer rule, closed-numeric classification,
rewrite, exec stmt, …):

1. Do **not** treat `examples/tmp.lit`, chat probes, or a one-off draft path as
   the final acceptance artifact.
2. Add a **new** `.lit` under the nearest matching `examples/` directory
   (typical homes: `examples/proof_nodes/…`,
   `examples/wd/…`, `examples/stmt_nodes/…`,
   `examples/wd_negative/…`, `examples/infer/…`). Name it for the feature or update
   (e.g. `calculation_closed_decimal_arithmetic_ops.lit`), not a vague dump.
3. Prefer a **new file** for the new/updated surface. Do not silently overload
   an unrelated older tracer; only edit an existing file when it is already
   that feature's dedicated home and the change is a small fix inside the same
   contract.
4. Follow that directory's README (proof-nodes: one builtin rule / search path
   → one file when applicable; no `trust` in proof/WD tracers).
5. Run the new file with
   `target/release/litex -f <that-file>` (or the sandbox
   `$CARGO_TARGET_DIR/release/litex` equivalent) and require exit `0` before
   reporting the feature done.
6. `examples/tmp.lit` stays a scratch probe only; promote the durable cases
   into the dedicated examples file in the same turn.

### Proof-node / WD tracers: no `trust`

For `examples/proof_nodes/` and other **proof /
well-definedness tracers** (not `examples/stmt_nodes/unsafe/`):

- Do **not** use `trust` / `trust have` to fake definitions, ambient facts, or
  function-set registration.
- Prefer `have … = …`, `have … ∈ …`, `let`, and `forall` binders so the example
  exercises real exec + store + verify.
- If a positive tracer needs a capability that is not wired yet (e.g. `have fn`),
  either wire the minimal exec/store path first, or omit the tracer until that
  path exists — do not paper over it with `trust`.
- Trust-stmt coverage belongs under `examples/stmt_nodes/unsafe/`
  (or equivalent unsafe/trust stmt nodes), not in proof-node folders.

See also `examples/proof_nodes/README.md` (Writing style).

## Workflow

1. Reproduce the failing Litex snippet first in the draft area allocated by
   `golitex-repository-policy`.
2. Read the nearby Rust code before editing.
3. Decide whether the blocker belongs to syntax, parser, runtime, verifier, builtin rule, infer rule, stdlib, or diagnostics.
4. Make the smallest behavior change that matches existing architecture.
5. Add or update focused examples/tests. For a **new** or **updated**
   user-visible capability, add a **new** `.lit` under the matching
   `examples/` directory in this turn (see “New or updated feature → new
   examples `.lit`”); do not leave acceptance only in `examples/tmp.lit`.
6. Classify the impact, record the impact card, and run exactly the selected
   focused/domain/contract gates. Escalate only with concrete evidence.

## Path Discipline

- Treat relative paths in user requests, including `tmp/...`, `examples/...`,
  `scripts/...`, and source-local output paths, as relative to the active Litex
  repository/workspace unless the user gives an absolute path. Put textbook
  `<Workspace>` drafts under `scripts/<Workspace>/.draft/`; put every other
  manually managed probe or scratch build under
  `<golitex-root>/tmp/<YYYY-MM-DD>/<task-slug>/`. Never use
  `<golitex-root>/private/` or absolute `/private` for drafts. System temp is
  only for files internally managed there by an external tool.

## Repository Rules

- Use `use crate::prelude::*;` for repository imports.
- Import only `std` items directly.
- Prefer `.into()` for conversions instead of direct enum wrapping.
- Write code that is as simple and direct as possible. Do not introduce fancy Rust features when straightforward code works. Prefer plain, sequential control flow that reads from top to bottom over clever abstractions, dense iterator chains, macros, advanced type tricks, or compact syntax.
- Do not write logic in `mod.rs`.
- Prefer `new` constructors for structs.
- Put shared helpers in `helper.rs`, not at the top of major files.
- Keep edits scoped; do not refactor unrelated code.
- Do not introduce explicit lifetimes in functions or structs. In almost all cases, do not introduce templates. Before introducing a template, explain the need to the user and get confirmation.
- When designing or migrating `Verify*Result` / `Exec*Result` types, apply
  `$litex-pipeline-result-types`: sequential pipelines return stage-ordered
  structs; enum dispatchers return recursively mirrored result enums.
  If a pipeline opens a **binder/proof-scope** local env
  (`run_in_local_env_and_take_env` — not the `exec_stmt` transactional temp),
  Success evidence **must** carry `local_env: Box<ExecEnv>`; never drop it as
  `_local_env` or omit it from the Proof struct.

### Canonical Symbol And Module Lookup

- Preserve one canonical semantic key for each bound `SymbolRef` across local
  and module-qualified syntax. A module-owned symbol must retain its canonical
  owner inside compound keys such as `tuple_dim(module::pair)`; never localize
  that key merely because the lookup is running against the module's own
  environment.
- Do not repair cross-module lookup by changing `Display` so the definition and
  use sites render different keys, or by storing duplicate stripped local-key
  aliases. Treat object and atomic-fact rendering as a semantic cache contract
  until those maps are migrated to a typed key, and audit every storage and
  query caller before changing it.
- Select imported environments from the structured `Obj` or `AtomicFact`
  recursively, or from an explicit resolved module owner. Never infer module
  ownership or manufacture a local cache key with `split`, `rsplit_once`, or
  global `replace` on a rendered object or fact string.
- Splitting a validated syntactic definition name of the restricted form
  `module::definition` is allowed. This exception does not apply to rendered
  expressions, compound objects, or facts.
- For every cross-module cache fix, first assert that local and qualified forms
  bound to the same `SymbolRef` have the same full canonical key. Then test a
  direct value, a compound lookup such as `tuple_dim(module::pair)`, equal
  terminal names from two exports, and an unknown qualified-name boundary.

## Rule Changes

Before choosing a new rule, structural strategy or authoring repair, read the
shared [search and explicit proof boundary](../../golitex-repository-policy/references/search-explicit-proof-boundary.md).
For kernel work, identify the trigger, generated obligations, decreasing
structure, leaf permissions, cost and evidence owner. An accepted explicit
proof does not require a shortcut; repeated mechanical steps may still expose
missing support. Diagnose that distinction without expanding global search
to close one example. Existing ownership and authorization gates still apply.

Do not restore behavior lost during a dispatcher or verifier-state refactor by
adding a fact-family or object-shape special case to a generic orchestration
entry point. Trace the former route, identify the owning fact-family
dispatcher, and adapt the rule to the current state/depth API. When one old
helper mixes structural matching with proof search, split it into a pure leaf
comparison and a bounded semantic rule or strategy. Preserve known-fact-first
ordering, well-definedness preconditions, recursion budgets, memoization, and
proof provenance. See [`references/rule-patterns.md`](rule-patterns.md)
for the migration checklist.

For a builtin rule, include a short comment with the mathematical property and an example shape.

When adding a builtin rule, add or update a corresponding example under
`examples/01_proof_patterns/` when there is a natural proof-pattern location.
Keep the example small and runnable, and use it to show the intended user-facing
Litex proof shape for the rule.

For an infer rule, include a short comment with the triggering condition, inferred fact, and example shape.

Never add broad automation just to make one example pass. Preserve soundness boundaries and make proof debt visible.

## Semantic Documentation Propagation

Before changing verifier semantics, record the exact comparison baseline and
classify the public impact. Use this matrix instead of updating only the file
whose wording names the implementation:

- Search order, recursion boundary, or automation eligibility: update the
  normative Manual, the architecture/System Map, and the FAQ explanation.
- New or changed explicit proof command: update the Manual contract table,
  cheatsheet, reserved-name/arity/failure behavior, and at least one runnable
  example.
- Removal of an implicit proof route: search every runnable Markdown and
  example for proof shapes that depended on it, not only for the route's name.
  Put the explicit replacement at the point of use and retain a focused
  negative boundary test.
- New proof provenance or result route: update detailed/JSON output examples,
  summaries, graph/trust descriptions, and terminology consistently.
- A changed onboarding-level proof shape: update README and comparison guides
  even when parser syntax itself did not change.

Treat documentation as two coupled surfaces: prose specifies the contract,
while executable snippets test migration. A prose-only update is incomplete
when old snippets still verify for the wrong reason or now fail. After the
focused kernel test, run the Markdown/example harness and report which edits
were forced by the semantic change versus incidental cleanup.

Build that report from an explicit baseline, for example with
`git diff <baseline> -- README.md docs examples`, and keep a small impact
ledger with four buckets: contract prose, executable proof migrations,
output/provenance, and incidental cleanup. Do not describe every nearby edit
as forced merely because it landed in the same checkpoint.

Classify each failing executable snippet by the proof route it actually lost:

- If a positive predicate follows from its defining clauses, migrate it to
  explicit one-line `by def $P(args)`. Do not normally write `by def:` with an
  indented `? $P(args)` goal; retain that form only when a focused verifier run
  proves it is required by the surrounding construct.
- If an object rule needs a `forall`, `exist`, or compound requirement, use an
  explicit builtin/user `by thm` interface.
- If the proof repeatedly decomposes one constructor into a fixed collection
  of strictly smaller children, treat repeated bridge edits as evidence for a
  bounded builtin strategy. The child fact family need not equal the parent
  family when the decomposition is mathematically uniform and strictly removes
  a constructor. Judge this from the proof tree, not from one operator spelling
  or one failing example.
- If the step changes mathematical family or needs a semantic lemma rather
  than a canonical smaller syntax decomposition, keep an explicit intermediate
  fact/theorem; repetition alone does not make it a strategy.

Do not mechanically add assumptions to make migrated documentation pass.
First reproduce the smallest original snippet, then decide whether the correct
repair is an explicit proof command, a reader-meaningful bridge, or missing
structural automation. When splitting one automation route into several,
document the trigger, search position, recursion boundary, permitted leaf
provers, failure/commit behavior, and evidence/provenance label together.
Classify a computation leaf only by execution shape: the central computation
matcher decides it without generating proof obligations. Keep normalized
spellings of the same fact family on that one route. Do not add a rule-local
bypass because one operator, sign, or literal happened to exhaust the depth
boundary in a test.

## Litex Examples And Regression Snippets

When writing Litex examples, docs snippets, or regression `.lit` code, use the
smallest body that verifies in the real context. Do not add mechanical echoes:
a successful `by contra` need not be followed by its target again; a witness
need not be manually folded back into a named predicate when that is only for
closing the current target; and a known implication or iff can supply its
conclusion once its premise is present.

For a named `thm`, deletion-probe a zero-statement body when its own settings,
binders, premises, or ordinary verifier rules already close every then-clause.
Do not repeat the then-clause as the sole proof statement. Preserve the nearest
negative regression showing that an unsupported bodyless conclusion still
fails; otherwise the example may be hiding a verifier soundness defect rather
than demonstrating concise authoring.

Do not remove facts by pattern alone. Keep explicit conjunction components
needed by `obtain`, package facts needed as later rewrite bridges, and function
equations that seed inference. Reproduce the shortened snippet as a focused
test before treating an example or regression as simplified.

## Tests

- Read `references/test-matrix.md`, classify the change L0-L5, and record the
  impact card before choosing commands. Leaf behavior must not be promoted to
  full testing merely because it changes kernel code.
- Runnable `.lit` artifact: use the release CLI with `-runner -f`; use
  `-runner -r` only for the complete module gate. Automated results are valid
  only when the parsed runner envelope and process exit code agree.
- Litex example/docs harness: run
  `cargo test --release run_examples -- --nocapture` only when the harness is
  needed in addition to direct `.lit` verification.
- Mechanics textbook chapters: run
  `python3 scripts/textbook_gate.py The-Mechanics-of-Litex-Proof`, which
  resolves the workspace-owned module from `scripts/.textbooks` and requires a
  structured whole-module runner success.
- For an L1 leaf builtin/infer rule, run its exact positive regression, nearest
  negative boundary, and direct tracer `.lit` gate only. Do not run
  `run_examples`, docs, To-Lean, or `run_all` unless the change crosses one of
  their contracts.
- For whole-project, textbook, or performance-sensitive verification selected
  by the impact class, build and run the release profile:
  `cargo build --release`, `cargo test --release <target> -- --nocapture`, or
  `target/release/litex -compact -runner -r <module>` for a complete module gate.
- Do not report the duration of bare `cargo test` as Litex runtime performance:
  Cargo's default test profile is unoptimized and can be much slower than the
  shipped release binary.
- Report exact failing file, snippet, or line from test output before changing more code.

## References

- Read `references/kernel-map.md` for where common behavior lives.
- Read `references/rule-patterns.md` before adding builtin or infer rules.
- Read `references/test-matrix.md` before choosing validation commands.
- Read `../litex-proof-writer/references/function-set-composition-case-record.md`
  for dated function-set composition evidence, WD versus proof-search
  boundaries, checked body evaluation, template failure projection and the
  public-entry test correction. The case record does not authorize broader
  search or establish that unclassified input-domain observations are bugs.

## Persistent Task Ledger

For a kernel, verifier, stdlib, or diagnostics task that remains unfinished
after this turn, create or update `todo/<YYYY-M-D>/<project>.md` at the
repository root, using the current environment date without zero padding.
Record the minimal repro, affected files/rules, completed checkpoints, the
next smallest implementation step, and the exact focused/broad test commands.
This is a cross-turn execution ledger, not a replacement for source-local
translation blocker notes. Delete it only when the scoped change is complete
and its required verification has passed.
