# Imported source guide

Source snapshot imported on 2026-10-13. Read this for the author's mathematical methods and scoped repository conventions. Historical CLI recipes and result fields are not current execution instructions; use [the hub execution contract](../../litex-reference/references/execution.md). Apply golitex-specific paths and maintainer rules only when working in that repository. Dated examples require replay before making a current-support claim.


# Litex Proof Writer

## Supported syntax and recommended authoring

Read [the writing and teaching guide](writing-and-teaching.md)
when choosing source spellings or helping a learner. In newly authored code,
prefer `release thm` for calls without selection, multiline `forall`, and
English/ASCII keywords and operators. Keep `by thm ... => fact` for atomic
selection. These are authoring preferences, not syntax restrictions; preserve
explicit user choices and historical evidence. Teach actual language boundaries
separately, using the first failing phase and a small checked repair.
For public examples, follow the guide's facts-before-theorem-names preference:
do not introduce a short named `thm` when a direct checked `forall` suffices.
Keep genuine proof bodies and named interfaces when they serve the example.

## Critical: Repository Policy And Verifier Loop

- In the golitex repository, apply `$golitex-repository-policy` alongside this
  skill and read its canonical bundled policy completely. That repository
  policy overrides generic or older guidance here.
- Build current source once with `cargo build --release` and invoke
  `target/release/litex`; never use `target/debug/litex` for Litex work.
- For every iterative edit to a registered target, start one
  `target/release/litex -compact -session -before <current-file.lit>` process.
  This loads the configured prefix before the target, excludes the target and
  later files, and enters the target file's environment whether it is empty,
  partial, or failing.
- Submit target statements from the first one in source order, one literal
  outermost `try:` block per theorem, definition, or small proof fragment. A
  successful block commits to the session; record its accepted source and
  reusable lesson in the task's JSON proof-block journal before editing the
  `.lit` target. A failed block rolls back only itself; record each materially
  distinct attempt and its verifier evidence, then correct and resubmit that
  block in the same process. Materialize accepted blocks from JSON into the
  `.lit` file only at a coherent checkpoint, in source order and without the
  outer `try:`.
- Resolve the journal location from the source- or task-owned working area.
  Prefer its existing machine-artifact directory; otherwise use that
  workspace's `proof_journals/`. For a textbook module, use the owning source
  workspace such as `scripts/<Workspace>/proof_journals/`, not `textbook/`.
  Never create `<golitex-root>/proof_journals/`, including for golitex-owned
  targets. If no owning workspace is identifiable, resolve the location before
  the first proof attempt instead of inventing a repository-root fallback.
- Put every disposable proof copy, liveness probe, transcript, or scratch
  project in the draft area allocated by `golitex-repository-policy`:
  textbook `<Workspace>` work uses `scripts/<Workspace>/.draft/`, and every
  other task uses `<golitex-root>/tmp/<YYYY-MM-DD>/<task-slug>/`. Never put a
  draft in `<golitex-root>/private/`, absolute `/private`, the repository root,
  or a canonical module tree, and never edit a production `litex.config`
  merely to register a probe.
- Timebox one unresolved proof obligation to at most three minutes of active
  first-pass proof search. When the cap is reached, or a real proof, library,
  inference, syntax, or formulation blocker is identified earlier, keep the
  intended statement, use the narrowest legal `trust`, mark and journal that
  exact debt, and continue the mainline. After the full chain runs, perform the
  five-minute-per-trust second pass described below; do not keep searching past
  that second cap unless the user explicitly expands the budget.
- Restart only when the process exits or cannot accept another frame, the
  registered prefix deliberately changes, or an already committed declaration
  must be replaced under the same name. Replay the target from its first
  statement after a restart. Record an unexpected unusable session as
  `kernel_problem`.
- Use `target/release/litex -compact -runner -f <current-file.lit>` for a clean
  baseline, checkpoint, or final file gate. Use `-isolated -runner -f` only
  for an intentionally standalone file. Require top-level `ok: true` and exit
  code `0`.
- Reserve `target/release/litex -compact -runner -r <module>` for an explicit complete
  module or repository gate. Never use default-profile `cargo test` as the
  Litex verifier; run the smallest genuinely required
  `cargo test --release ...` harness separately.

## Tracer bullet

Select one theorem or proof block that best exposes the round's proof-writing
change. State its shortest mathematical proof spine, show the old and new
Litex shapes, identify the smallest verified bridges, and use its clean gate or
profile as the primary evidence. Lead the final response with this example and
map terms such as inference echo, representation drift, or administrative
adapter to its concrete lines.

Use `limit_point_has_convergent_subsequence` as the fixed example. Its former
administrative chain `F -> choice_index -> pick -> phi -> b` became the
mathematical interface `next_index -> phi -> b`; `next_index(k,s)` exposes only
the lower-index and closeness properties consumed downstream. This keeps the
choice machinery local and reduced the clean release theorem time from about
10.36 seconds to about 6.99 seconds. See
[`references/proof-style.md`](proof-style.md) for the measured proof
shape. Choose a task-specific theorem for actual work.

For a major proof, interface, or performance rewrite, add the repository
policy's durable
`scripts/<Workspace>/experience/problem_notes/<slug>_acceptance.md`. Show the
old representative proof route as commented Litex, the new proof route as
uncommented Litex, the exact registered theorem path, and the clean gate (plus
before/after timing when performance is the point). The note is the readable
comparison; the linked registered source and executed command are the proof.

## Derive proofs forward

Construct each proof from independently justified definitions, assumptions,
known facts, and established interfaces through the shortest meaningful
mathematical dependency chain to the conclusion. Derive intermediate lemmas,
witnesses, cases, and Litex bridges only when an upstream proof move or an
observed verifier boundary requires them. The target tells the proof what to
establish; it does not justify theorem-shaped helpers, duplicated premises,
weakened definitions, representation adapters, or `trust` chosen merely
because they make the target close.

Backward reasoning may expose necessary subgoals, counterexamples, or missing
dependencies, but every backward-discovered obligation must be independently
validated and inserted at its proper upstream point before the proof is
re-derived forward. When verification fails, repair the earliest false
premise, missing interface, carrier mismatch, or verifier bridge instead of
adding an echo next to the goal. Apply the counterfactual check: if the final
theorem were hidden, would each helper and trusted boundary still express a
real reusable mathematical fact or a precisely evidenced Litex limitation?

## Workflow

1. Write the shortest honest proof spine in ordinary mathematical language
   before editing Litex.
2. Run the Litex authoring action gate: choose the declaration kind and fact
   shape, then test whether a native proof action expresses the mathematical
   move before writing manual expansion, helper layers, or `trust`.
3. Find the existing definitions, theorems, templates, and local proof patterns
   that implement those mathematical moves.
4. Write the smallest runnable Litex proof whose blocks correspond to the
   proof spine.
5. Run the verifier, read the exact output, and record each materially
   distinct block attempt in the JSON proof-block journal.
6. Make the next smallest correction without changing the proof's abstraction
   level merely to satisfy the verifier.
7. When a block verifies, stage its accepted Litex and concise reusable lesson
   in JSON; do not edit the `.lit` target yet.
8. At a coherent theorem or file checkpoint, materialize the accepted JSON
   blocks into `.lit` in source order and run the clean file gate.
9. After it verifies, run the mandatory proof-liveness audit and remove
   inference echoes, dead facts, and bypassable derivation chains.
10. Classify the result as `translated`, `checkable`, or `blocked`.

## The Way Before The Techniques: Reader-Centered Mathematical Writing

For a reader-facing showcase, tutorial, or explanatory mathematical document,
decide the reader's intended mathematical understanding before choosing proof
syntax. This is the distinction between the way and the techniques:

- **The way** is the mathematical and pedagogical path: what conceptual model
  the reader should form, which idea is the main line, where the exposition
  should move from concrete examples to an abstract interface, and which
  contrast makes Litex's design intelligible.
- **The techniques** are the local instruments used to realize that path:
  `by enumerate finite_set`, `by cases`, theorem selection, equality chains,
  comments, helper declarations, and verifier-driven compression.

For a README accompanying a Litex textbook or showcase, also apply
`$litex-research-writer` and read
[the textbook and showcase README guide](../../litex-research-writer/references/textbook-showcase-readme.md).
Use its Mechanics pattern: positioning → mathematical progression → real
checked examples → coverage and navigation map. Keep the artifact's overall
direction connected to concrete code details.

Do not organize a showcase as a checklist of unrelated language features or
as a collection of locally minimal regression tests. Make it read like a
small mathematical chapter: choose one continuous mathematical spine, let
later objects consume earlier results, and use Litex constructs where they
express the mathematics of that spine. For example, placing finite enumeration
beside ordinary case analysis can teach the difference between exhausting a
finite domain and eliminating an already exposed disjunction; using either
construct merely because it is shorter misses the point.

Distinguish machine redundancy from reader redundancy. A line is machine-
redundant when the verifier can infer it, but it may still be a useful
`reader_bridge` when it exposes the concrete fact that closes a branch, the
representation transported by an equality, or the semantic effect of a proof
action. Prefer selective explicitness: expand the conceptual transition and
compress administrative carrier checks, wrapper echoes, and implementation
history. In a case `element = 2`, the explicit fact
`2 $in {1, 2, 3, 4}` may be better public exposition than a bodyless arm,
because it shows what the case actually proves; repeating the abstract goal
`element $in {1, 2, 3, 4}` would reveal less.

Verification and brevity remain constraints, not the highest objective of
reader-facing documentation. Test the shortest form to learn what Litex can
infer, then deliberately choose the public form that best communicates the
mathematical move. Record an intentionally retained inferable line as a
`reader_bridge` in the proof journal so a later liveness audit does not erase
it without reconsidering the teaching purpose.

## Litex Authoring Action Gate

Before writing or repairing Litex, read
[`references/litex-authoring-cheatsheet.md`](litex-authoring-cheatsheet.md).
Use it to choose the declaration kind, fact shape, native proof action, and
first failure-triage step before expanding a manual proof or adding `trust`.

When repairing a failed attempt or simplifying code that already verifies,
read
[`references/authoring-error-cards.md`](authoring-error-cards.md).
Match the observed phase and code shape to a failed-to-repaired or
passing-but-poor example; copy only the smallest repair and confirm it in the
real caller context. Do not turn a mined workaround into a universal rule when
the card identifies an interface, diagnostic, or kernel gap.

The sheet is routing guidance, not an independent language specification.
Confirm exact syntax and current semantic boundaries in the repository Manual
and a runnable nearby example, then test the smallest selected form in the real
caller context. Do not weaken the source statement merely to fit a convenient
surface.

## Two-Pass Trust Timebox

Use a fixed active-search budget so one proof obligation cannot stall the
mainline: at most three minutes before adding the narrowest marked `trust`, then
continue until the whole chain runs; review all trusts and recurring shapes;
then spend at most five active minutes on each trust. Remove solved trusts and
send every survivor to the source-owned todo through `$todo-writer`. Do not
begin a third round without an explicit user budget. Exclude the initial build,
known long file/module gates, and ordinary waiting for an issued verifier
command. Read and follow
[`references/trust-timebox.md`](trust-timebox.md) whenever a proof
obligation reaches the first-pass cap or the task reviews existing trust debt.

## Treat Verification Gaps As Primary Evidence

Treat Litex formalization as two linked outputs: the mathematical interface
states what is being defined, while the proof journal records how Litex can
actually verify it. A plausible natural-language proof is only a plan until
its statement, carriers, intermediate facts, and proof commands pass the real
verifier.

Do not let the final successful `.lit` proof erase the expensive part of the
work. Before mutating source, preserve each materially different failed
candidate, the first decisive diagnostic or silent-gate observation, the
failed verifier phase, the diagnosed mechanism, and the next smallest repair.
After success, preserve the accepted block, its dependencies, the exact bridge
that made it check, and the reusable lesson. Record concise decision evidence,
not hidden chain-of-thought.

Keep two memory layers:

1. Use the per-task JSON proof-block journal as the recoverable chronological
   evidence and staging source of truth.
2. Let the miner distill repeated or high-risk mechanisms into candidate
   rules after clean checkpoints. The miner never edits the permanent skill or
   establishes causality. Promote only after multiple independent source-item
   or task journals support the normalized mechanism, a positive example and
   nearest negative boundary are executable, and a held-out behavior check
   shows improvement without regression. Retries, transcripts, liveness
   variants, and draft copies of one target count as one evidence family. A
   single interface-impacting observation or stable control may raise the
   priority of a candidate, but cannot by itself satisfy skill promotion.

When the user wants example work, agent improvement, and possible kernel work
to form one recurring feedback cycle, read and follow
[`references/example-agent-kernel-loop.md`](example-agent-kernel-loop.md).
Use its round review boundary so every kernel candidate is shown to the user
before mutation, while one-task authoring observations remain miner
nominations until independent and held-out evidence supports promotion.

Keep diagnostic history out of mathematical `.lit` files. Read
`references/proof-gap-mining.md` before a long textbook or dataset proof
session, when the same proof shape has failed twice, or when mining experience
for a skill, library, diagnostic, or kernel improvement.

Before creating or repairing a reusable definition, apply
`litex-concept-modeler` in interface mode. State the semantic role, choose the
Litex form, preserve the source name/domain/codomain, and write one minimal
use probe before spending time on downstream proof steps. A source-defined
function or set-valued construction must remain `have fn` even when its body
contains a predicate. A `prop` may describe the relation used by that body,
but it is not a substitute for the returned function or object.

For a new top-level module, or when adding or changing a core reusable
interface, read its single `README.md` and `math_collections.md` before writing
substantial code. `README.md` is the current implemented API; the second file
is the mathematical manual for important concepts and ideal interface shapes.
Use one pair for the whole module, not one per file or submodule. Compare the
candidate declaration with that manual: repair the code when it drifted, or
update the manual first when the mathematical design genuinely changed. Do not
keep incompatible forms through wrappers, aliases, `abstract_prop`, or
`trust`. After the use probe verifies, update `README.md` with the actual API.

## Nonredundant Proof Spine Gate

For textbook data-and-law objects, honor the user's explicit 2026-10-09
struct-first convention: laws belong directly in the primary struct.
Do not expand proof access into `prop -> struct -> satisfies_prop` bridges.
Use native struct opening for definition consequences; keep actual
construction, restriction, and transport mathematics. A standalone law
predicate requires an independent source use, not a verifier workaround.

Before writing Litex, state the proof as the fewest meaningful mathematical
moves a competent reader would normally use. Name the existing interface that
justifies each move. Prefer the highest established abstraction: use an
inverse-function theorem, decomposition lemma, induction principle, or
structure law instead of rebuilding its construction locally.

During formalization, require every nontrivial code block to correspond to one
proof-spine move or to one verified Litex bridge that the verifier genuinely
needs. If a two-step mathematical argument grows into a local function,
existence proof, uniqueness proof, and helper claim, stop before accepting the
code merely because it runs. Search for the missing reusable interface and
classify the expansion as one of:

- failure to reuse an existing definition, theorem, or template;
- a missing general mathematical interface;
- an exact parser, verifier, well-definedness, or elaboration bridge; or
- mathematics that really is constructive at this level.

The block count and shape must remain visibly aligned with that spine. A
two-step proof must not turn into a line-by-line log of associativity,
commutativity, identity, and rewriting states. Put the decisive calculation in
one equality chain. If the verifier cannot rewrite an inner argument through an
outer function, add only the smallest explicit congruence or inner-rewrite fact
shown necessary by a failed shorter real-context run.

After the proof verifies, compare its blocks against the original proof spine.
Delete or replace any block that only re-proves a packaged fact, reconstructs
an existing object, or exposes implementation detail absent from the
mathematical argument. Re-run the shortened proof in its real context after
each deletion. Keep extra code only when the shorter form actually fails, and
record the exact reason; do not normalize a repeated local workaround as good
proof style.

Write the proof spine in the working analysis or item metadata. Put it into the
`.lit` source only when it is a useful mathematical comment, not as a narration
of obvious syntax. See `references/proof-style.md` for the bijection/inverse
example and the final alignment audit.

Do not leave an easy textbook or dataset example as comment-only prose. At
minimum, use a `sketch:` block to state and formalize the example's actual
objects and claims; when the facts are directly checkable, prefer a checked
theorem or a fully verified sketch. Prose may explain the example but cannot
replace its formal mathematical content.

## Clean Interface and Local-Proof Gate

Use lexical proof scope as the default boundary for proof-only machinery. Do
not create a file-level declaration simply because it makes the next lines
shorter.

Before adding a top-level `prop`, `have`, `have fn`, `template`, `claim`, or
`thm`, identify every real consumer in the current source tree:

- If the helper serves exactly one proof procedure, declare it inside that
  enclosing `claim` or `thm`. This applies to temporary predicates, witness
  relations, finite-set bounds, uniqueness criteria, recursive coefficient
  pairs, projections, and induction invariants.
- A local `have fn` may be recursive (`by induc` / `by strong_induc`). Prefer
  that form for an algorithm used only to prove one theorem, then expose only
  the theorem's mathematical conclusion.
- Promote a helper only when it is a source-facing definition, a stable cited
  theorem, or has verified use in two or more independent proofs. “It may be
  useful later” is not evidence for a public API.

For example, a Bézout theorem may define its recursive Euclidean coefficient
pair, its projections, and its measure invariant inside the theorem, while
the outside interface remains only the existential Bézout conclusion. Likewise
an implementation predicate saying that a candidate is greatest should not be
published when ordinary divisibility and algorithm theorems are the intended
reader-facing laws.

Run the candidate in its real enclosing scope. If local declaration is blocked
by an actual parser or verifier limitation, record the smallest reproduction;
do not broaden the interface merely as an untested workaround. After cleanup,
search dependent files and remove every citation of the localized helper.

For any newly created or touched dataset, textbook, contest, exam, Mechanics,
or generated-math item, follow the Translation Item Contract in
`references/dataset-translation.md`. Do not submit raw Litex code without the
source, problem, proof idea, Litex code, and concise comments when relevant.

## Mainline-First Refinement

For textbook, dataset, or long theorem-family work, prefer a mainline-first
refinement workflow over trying to write a perfect top-to-bottom proof in one
pass. First make the important mathematical spine readable and runnable. Then
isolate substantial or library-shaped supporting facts that remain genuinely
unproved as named local interfaces that can be proved later.

### Cite Eligibility Gate

Treat a cite package as a namespace for genuine, unresolved proof debt. It is
not a place to give names to facts that the verifier already proves through
builtin or infer rules.

Before adding any cite theorem, test its intended statement directly in the
real caller context, without a wrapper theorem or `trust`:

1. If the direct fact verifies, use that fact directly. Do not create a `thm`
   only so callers can write `by thm`, and never put a trusted copy in a cite
   package. Builtin provenance is already the proof source.
2. Repetition alone does not make a fact cite-worthy. Elementary set algebra,
   arithmetic normalization, comparison, type/membership consequences, and
   other builtin-supported facts stay direct even when many files use them.
3. A cite candidate must remain genuinely unproved after one direct real-context
   attempt, have a substantial or library-shaped proof that would distract
   from the mainline, and need a stable named interface while that proof is
   deferred. Record the exact missing proof and future discharge path.
4. If a simple expected fact does not verify, classify the missing builtin,
   infer, stdlib, or kernel support instead of hiding the gap in cite.

For example, do not put a trusted `set_commutativity` theorem in cite merely
to expose commutativity of `intersect` and `union`. When those equalities are
builtin-checkable, write the equalities directly at the use site. If the
source itself numbers such a theorem, keep that source-facing theorem in its
source location and let its body verify directly; it is still not citation
proof debt.

Use this pattern when a supporting fact is mathematically clear but would
distract from the current source item:

1. Keep the main `.lit` file focused on source-facing definitions, theorem
   statements, key proof route, and checked local derivations.
2. Put repeated real vocabulary in a small `*_vocab/main.lit` module using
   ordinary `prop`/`have` definitions. Do not copy real definitions into a cite
   file with `abstract_prop`.
3. Put genuinely unproved, lengthy supporting facts in a source-local cite
   package such as `chap7_cite/main.lit`, `<source>_cite/main.lit`, or
   `cite/main.lit`.
   Cite facts should be named `thm` or `claim` interfaces, with unresolved
   proof steps marked by narrow `trust` proof debt. Never add a cite wrapper
   for a fact already discharged by builtin or infer rules.
4. For repository projects, declare cite packages with `export mod`, place
   them before their consumers in the ordered `[export]` table, and cite their
   canonical imported names. Litex has no statement for loading an arbitrary
   `.lit` path.
5. Make cite theorem statements reusable and abstract enough for the local
   mathematics, not one-off facts tailored to a single proof line.
6. Consider a reusable project package only after the fact is fully checkable,
   has a stable interface used by at least three independent source families,
   and remains explicitly declared through `litex.config`. Do not create or
   restore an automatically loaded mathematical `std`.

This is the default collaboration pattern for large formalization: build the
important structure first, keep proof debt explicit and named, then refine the
surrounding facts one at a time.

## Turn Scaffolding Into Checked Proofs

The goal is not only to make files run. Existing files may use `trust` or
`abstract_prop` as temporary scaffolding so a larger translation remains
runnable while the missing mathematics stays visible.

For a newly encountered obligation, write the natural proof spine and begin a
direct real-context Litex attempt. Apply the two-pass trust timebox: spend at
most three active minutes before preserving the intended statement with trust
only on the blocked substep, then continue the mainline. Once the whole chain
runs, revisit every marked trust for at most five active minutes and defer any
survivor to the source-owned todo with concrete evidence.

When the task explicitly targets existing debt, improve it by proving an
existing `trust`, replacing a broad trust with a checked outline plus one
narrow trust, turning a clear `abstract_prop` into a real definition, or
factoring repeated debt into one stable reusable interface. Test any cite
candidate directly first; builtin-supported facts never become trusted cite
wrappers.

Keep status honest: `checkable` only after the relevant code verifies without
`trust`; `translated` when the statement has a natural Litex form; `blocked`
when the obstacle is understood and recorded with primary label `trust` or
`kernel_problem`.

## Reference Corpus

Before writing or repairing nontrivial Litex, search the bundled corpus copied from this repository's `docs/` and `examples/` trees. Start with `references/litex-corpus/INDEX.md`, then use targeted `rg` searches under `references/litex-corpus/docs` and `references/litex-corpus/examples`. Do not load the whole corpus into context; read only the matching snippets or files needed for the current proof.

Use the corpus this way:

- Prefer `docs/Manual.md` for syntax and verifier behavior.
- Prefer `examples/01_proof_patterns/README.md` for proof idioms.
- Prefer runnable `.lit` files under `examples/` when choosing a checkable proof shape.
- Treat `_internal/scratch` examples as useful experiments, not polished public style.

## Learn Litex from trial and error

### 1. Unfold recursive definitions one stored equation at a time

- Separate definition acceptance from concrete evaluation. Do not expect a
  recursive call at a numeral to normalize through several recursive layers.
- State the exact stored base or successor equation first, then substitute the
  smaller value in a following equality step.
- When the recursive argument contains an arithmetic representation such as
  `(m + 1) - 1`, establish the inner equality before rewriting the function
  application.
- Keep these equations local to the calculation. Do not create public wrapper
  theorems that merely restate a function definition.

### 2. Materialize atomic values before rewriting a compound context

- Do not assume that separate facts such as `f(x) = a` and `g(x) = b`
  automatically rewrite inside `f(x) + g(x)`, a finite fold, or another
  enclosing function.
- Record the exact atomic function value or changed operand first, then use one
  continuous equality chain for the surrounding expression.
- When substituting inside a larger expression, keep the original stored
  expression on the path instead of jumping directly to the endpoint. For
  example, from `x = 3 / 2` and `n * x = 96`, prefer
  `n * (3 / 2) = n * x = 96` over the opaque endpoint
  `n * (3 / 2) = 96`. This is both a verifier-friendly contextual rewrite and
  the preferred final proof style, even when the shorter endpoint happens to
  verify.
- When one proof needs several normal forms of the same expression, connect
  them in source order rather than publishing disconnected equality states.
  Keep each consumer-facing form in one route, for example
  `d = 4*c^2*(1-c^2) = c*(4*c-4*c^3) = c*(c-1/2)` after proving the adjacent
  cubic step. Do not expect the verifier or reader to reconstruct an unstated
  path through separately stored forms.
- After the proof succeeds, deletion-probe the bridge in the real context and
  retain only the smallest atomic fact that the verifier actually needs.

### 3. Use native mathematical predicates without specialized wrapper props

- Before declaring a new `prop`, search for the native builtin or established
  source predicate that already states the same mathematics. Use it directly
  at the real theorem boundary.
- Do not create a constant-specific or one-caller prop whose body merely
  forwards one builtin, such as a predicate specialized to the divisors of one
  fixed integer whose whole body is `$dvd(fixed_value, d)`. A wrapper is
  justified only when it is a real source definition, adds mathematical
  clauses or a stable abstraction, or has independent consumers that need the
  named interface.
- Preserve builtin argument conventions instead of hiding them behind an
  alias. In particular, `$dvd(dividend, divisor)` is dividend-first.

### 4. Make finite-classification conclusions carry their classification state

- A bounded `by for` result is easiest to reuse when every enumerated
  coordinate needed by its premises also appears in the classified result.
  If a quantified coordinate occurs only in a premise such as `n*q=24` and
  disappears from a conclusion about `n` alone, do not wrap that enumeration
  inside an outer theorem and expect ordinary forall matching to recover `q`.
- Remodel the finite object instead: classify the factor pairs `(n,q)`, state
  divisibility directly with `$dvd`, or enumerate the final one-coordinate
  domain. Choose the representation that makes the proof result
  self-sufficient for its consumer.
- This is an authoring/modeling boundary, not a request for the kernel to
  search an arbitrary existential witness for a premise-only quantified
  parameter.

### 5. Distinguish session callability, stored facts, and executability

- Treat these as three separate capabilities: an object may be callable in a
  proposition, its stored facts may support rewriting, yet it may still be
  unavailable as a dependency in a new checked `have fn` body.
- Treat opaque `trust have fn` objects and helpers loaded by `-before` as
  interfaces, not automatically executable definitions.
- Test definition composability explicitly. When checked definitions depend on
  one another, submit the complete related constructor group contiguously in
  one session transaction before relying on downstream use probes.

### 6. Use a control experiment before classifying a kernel problem

- Separate the verifier phases: expression well-definedness, proof or
  recursive verification, environment mutation, and generated-fact storage.
- Compare a failing higher-order case with the closest direct case. For
  example, if `1 / b(n)` loses a nonzero refinement but `1 / n` under
  `n > 0` passes every phase, diagnose higher-order refinement propagation
  rather than recursive division in general.
- Preserve both traces in the JSON proof-block journal. Classify
  `kernel_problem` only when the control case and minimal reproduction isolate
  verifier behavior; otherwise use the narrowest `trust` boundary.

### 9. Classify the failed phase before changing the proof

- Read the first decisive verifier error and classify whether the candidate
  failed during parsing, name or type resolution, well-definedness,
  proof search, generated-fact storage, or later use. Do not treat every
  rejected block as evidence that the mathematical theorem is missing.
- Reduce only the failing phase. Compare with a nearby accepted statement and
  use the smallest control that preserves the suspect binder, carrier,
  operator, or theorem call. Record the candidate, phase, evidence, and next
  change in the proof-block journal.
- Change the proof's mathematical route only after the statement is known to
  be well formed and the failure is genuinely a proof obligation. Classify
  `kernel_problem` only after a minimal reproduction and control experiment
  isolate verifier behavior.

### 10. Normalize shifted indices before rewriting the sequence value

- Treat an index shift and the value at that index as two proof steps. First
  prove the exact index equality or range fact, such as the normalization of
  `(k + 1) - 1`, `i + h`, or the successor/predecessor boundary; then rewrite
  the enclosing sequence, sum, or recursive call.
- Keep the shifted index in its declared carrier. Prove positivity,
  boundedness, or membership before applying a function whose domain is
  `N_pos`, a finite range, or another refined index set.
- Prefer the established shift, tail, or reindexing interface when one exists.
  Do not expand a routine index change into a fresh recursive proof, and do
  not ask outer-function congruence to discover an unproved inner index
  equality.

### 11. Prove set equality by extensionality

- Use `by extension A = B` for genuine set equality and prove the two
  membership directions in the element scope. If both subset facts are
  already available, use the bodyless form directly.
- Unfold only the membership predicates needed for each direction. Do not try
  to normalize two set builders syntactically, enumerate finite sets, or route
  the goal through equality of construction histories.
- Keep element-carrier and well-definedness facts explicit when the set
  builders use refined domains. Use function extensionality, not set
  extensionality, when the objects are functions returning sets.

### 12. Stop small wrapper goals from triggering broad proof search

- For a tiny wrapper theorem, predicate fold, or one-step consequence, cite
  the exact definition clause or theorem result that closes the goal. Do not
  leave a broad unqualified search to rediscover a fact through the whole
  imported environment.
- If the small goal is unexpectedly slow or explodes, test the body directly
  at the call site, qualify the intended theorem, reduce irrelevant context,
  and isolate a minimal reproduction. Do not add more wrapper layers or a
  chain of near-duplicate helper facts.
- Delete wrappers for builtin-, infer-, or definition-supported facts. Keep a
  named wrapper only when it is source-facing or has independent consumers,
  and ensure its proof follows one narrow deterministic route.

## Verification Loop

For repeated proof iteration, build current source with `cargo build --release`
and start one persistent
`target/release/litex -compact -session -before <current-file.lit>` process.
If the current source cannot produce the release binary, report that build
failure and stop verification; do not substitute an older or debug binary.
Submit the target's statements from the first one in source order, with each
candidate protected by a literal outermost `try:`. This is the default inner
loop because failed attempts normally roll back only themselves and do not
replay the already-loaded project prefix.

Do not use Python-side `sandbox_run()` as the primary workflow when direct
Litex `try:` is available. Do not rerun a release `-f long_file.lit` target
after every small edit; use it only for file checkpoints and final file
verification. Use the persistent `-session -before` loop for suffix work, and
use `-r` only for an explicit complete-module gate.

Keep one statement or small proof fragment per outer `try:`. Before the first
attempt, initialize one JSON proof-block journal for the target and proof
spine. After failure, record the candidate, exact concise verifier evidence,
diagnosis, and next smallest change, then repair and resubmit only that
fragment in the same process. After success, record the accepted source
without the wrapper, its dependencies, and a reusable lesson in JSON before
submitting the next statement. Do not edit the `.lit` target during this inner
loop.

At a coherent theorem or file checkpoint, materialize accepted blocks from
the journal into `.lit` in source order, then run the clean release
`-runner -f` gate and record its parsed top-level result. If the file gate fails, keep the JSON record as the
recoverable source of truth and return to the same block-oriented workflow.
Read `references/litex-repl-try-workflow.md` for the journal location,
schema, attempt-compression rule, and materialization contract.

Before reporting completion, run a residue check over the repository root and
every touched source/module directory. Confirm that the task left no root
`proof_journal*`, `.codex_tmp_*`, probe, scratch copy, temporary transcript, or
temporary `litex.config` entry. Remove only task-created artifacts. If cleanup
cannot be completed, report every remaining path and do not claim a clean
completion.

## Explicit Semantic Boundary Triage

For requests to find examples that cannot run or diagnose previously checkable
proofs after a version change, first apply
[`litex-example-migration`](../../litex-example-migration/SKILL.md). Classify the
root cause and earliest failing phase before choosing an authoring workaround;
use the same concrete issue framing when reporting or discussing the failure.
Do not infer a kernel defect, required proof migration, or intended semantic
change from the failed assertion alone.

When choosing between explicit steps and broader automation, read the shared
[search and explicit proof boundary](../../golitex-repository-policy/references/search-explicit-proof-boundary.md).
For proof writing, find the shortest meaningful route for the same target and
premises, verify it, then reuse its checked results. Keep automatic discovery
separate from explicit checkability. Repeated mechanical carrier/transport
steps warrant a support audit; they are not automatically permanent style.
Constructor decrease is a design criterion for bounded structural support,
not a claim that every current strategy supports recursive descent. Inspect
the current dispatcher and leaf permissions rather than imposing an older
search order or reopening higher stages inside a premise.

Use the source boundary that matches the failed edge:

- After proving the body of a positive user or builtin predicate, normally
  write the one-line bodyless form `by def $P(args)` (or the supported infix
  `by def` form). An indented `? $P(args)` target by itself is not a proof
  statement and does not justify spelling the same step as a block. If
  intermediate proof statements are needed, write them before the final
  one-line `by def` in the enclosing proof. Treat `by def:` followed only by
  `? $P(args)` as compatibility or minimal-reproduction syntax, never as
  normal generated or touched proof style; retain it only when a real verifier
  run rejects the one-line form, and record that evidence. Known positive
  instances may still eliminate to their definition clauses. Prove negative
  instances with ordinary logic such as `by contra`.
- When membership or equality needs a semantic object rule with compound
  premises, use its explicit builtin theorem interface. In particular,
  introduce set-builder membership with
  `by thm set_builder_member(x, {n S: P(n)}) => x $in {n S: P(n)}` after the
  base and substituted predicate hold, and reconstruct a tuple with
  `by thm tuple_equal_from_coordinates(...)`. Keep automatic constructor
  elimination and equality transport; do not repeat the theorem after a known
  conclusion has merely been transported.
- Unfold nested function applications one stored definition at a time. If the
  immediate argument is compound, materialize its domain carrier before the
  evaluation step. Do not turn recursive function unfolding into a direct
  builtin rule.
- Give a recurring nontrivial object a role-based lexical name when ordinary
  mathematics treats it as one atom. Use `let name = value` for a pure
  abbreviation and `have name S = value` when the carrier `S` is useful
  evidence. When the repeated atom is a fixed template specialization that is
  later applied, prefer naming the callable specialization itself, for example
  `let neg = \vector_neg<K, field, V, space>` followed by `neg(x)`, rather than
  naming one result if the operation is what recurs. Transparent `let` names
  can normally be used directly in function-head, equality/comparison, theorem
  argument, selected atomic theorem-result, set-valued binder, and other object
  contexts; add a canonical-to-alias equality bridge only when a real caller
  rejects the direct form. This is one-step inspection of the object, not an
  automatic congruence tactic: a stored equality about `alias(x)` need not be
  lifted through `outer(alias(x))`, and alias-spelled proof evidence need not
  satisfy a later canonical matcher. Keep public theorem statements and any
  quantified or structural fact consumed later by a canonical matcher or
  definition fold in canonical spelling: directional reduction expands an
  inspected alias, but a canonical goal does not search backward for stored
  alias-spelled clauses. Do not apply
  this by character count, alias a one-use transparent calculation, or hide a
  constructor such as `fn_range` when a later proof action must inspect that
  constructor. `fn_range(image_map)` is useful; aliasing the whole `fn_range`
  before `have by preimage` is not. If naming introduces a growing unpack/repack
  adapter stack, keep the canonical expression or name a more appropriate
  outer mathematical object. See P7 in
  `references/authoring-error-cards.md` for the verified callable-template
  example and both canonical-fold and constructor-sensitive boundaries.
- Before adding an explicit theorem call, inspect which known `forall` sources
  are actually visible in the current runtime and whether automatic matching
  finds the intended instance. Use qualified `by thm` when an explicit theorem
  dependency is clearer or automatic matching does not supply it; do not infer
  a local-only boundary from one failed import example.

A bare top-level `forall` is an automatically verified fact declaration. If its
proof needs `by cases`, `by def`, `by thm`, a witness, or another proof-control
statement, convert it to a `claim` whose goal is the universal fact and put the
proof commands in the claim body. Do not try to embed proof-control syntax in a
forall conclusion list.

These distinctions are directional. For a set builder, known membership may
still expose the base carrier and predicate even though constructing that
membership is explicit. For a named proposition, known truth may still expose
its clauses even though folding the clauses is explicit. Preserve that
direction instead of compensating with duplicate theorem calls or inference
echoes.

## Mandatory Proof-Liveness Audit

Treat proof-trace redundancy as a failed completion criterion even when the
file verifies. Write the mathematical proof, not a log of verifier states.
Classify and remove all five forms:

- **Result or context echo:** restates a `by thm` conclusion only to mirror the
  current goal, or repeats an existential before `obtain`, an obtained body,
  case premise, binder-derived type fact, witness body, definition equation,
  reflexivity, or builtin/infer consequence.
- **Wrapper echo:** uses an empty or one-line `claim` for a fact that should be
  written directly, or wraps proved definition clauses in an atomic prop goal
  and then repeats the folded target.
- **Equality or comparison waterfall:** prints every rewrite state and then
  repeats an endpoint equality/inequality already supplied by the chain.
- **Representation drift:** creates alpha-equivalent lambdas, aliases, or other
  local variants and then adds pointwise/extensional transport to reconcile them.
- **Dead or bypassable chain:** has no live mathematical consumer, or its local
  links consume one another even though an earlier declaration, infer rule, or
  established interface reaches the endpoint without the whole chain.

Run two passes after every new or touched proof verifies:

1. Work backward from the final target, witnesses, and exported claim results;
   remove facts with no live consumer.
2. Inspect every remaining multi-line bridge for a bypass. Delete the whole
   candidate chain in a literal `try:` block in the real enclosing context.
   If deletion fails, restore only the smallest exact bridge demonstrated by
   the failure, not the original cascade.

Apply a hard echo ban after declarations, binders, `obtain`, witnesses, and
cases in proof-development and library source. Use stored conclusions directly
and do not republish obtained or case facts. In reader-facing documentation,
retain a concrete branch fact only when it is a deliberate `reader_bridge`
under the way-before-techniques rule above; do not retain a mere repetition of
the abstract goal. Apply the same rule to named theorems: if a real-context
deletion probe shows that the `? forall ...` then-clause is already discharged
from the theorem's settings, binders, premises, or ordinary verifier rules,
leave `prove_process` empty. Never repeat the then-clause as the sole body
statement. Keep the proof body when it performs any genuine proof move, and
pair promotion of this style with an unsupported bodyless theorem that remains
rejected. After proving a concrete prop's instantiated clauses,
finish with bodyless `by def $P(args)` on one line from the inside out. This is
a completion gate: new or touched proof code must not spell a bodyless
definition fold as `by def:` plus an indented `? $P(args)`. That target line is
not a proof body. Put any genuine intermediate proof statements before the
final inline `by def`; retain the multi-line compatibility spelling only in an
isolated parser/verifier reproduction where the inline spelling demonstrably
fails, and record that evidence. Do not force builtin, abstract, or
theorem-supplied facts through `by def`.

Review theorem-result selection separately. When one atomic result matters,
write it in `by thm theorem_name(args) => fact` instead of releasing every
result and repeating the chosen fact afterward. Keep a bare call only when
several distinct returned results are live or the desired transition is not an
allowed atomic target. Delete a separate pure current-goal restatement; the
selected-result call itself may close that atomic goal.

Reuse one canonical function expression or named helper throughout a proof.
Do not introduce extensionality merely to reconcile binder renaming or an
equivalent lambda spelling created locally. Keep an implied line only when a
real-context deletion probe proves that it is the smallest necessary bridge or
a source-facing mathematical move. Dependency graphs and lexical scans may
nominate candidates, but cannot prove liveness because they may omit inferred
facts. See `references/proof-style.md` for the full cascade test and examples.

For a slow theorem, make the liveness audit performance-aware. Locate the hot
top-level statement by timing source-ordered frames in one release
`-session -before` process, then compare materialized deletion candidates
serially with the same release binary and environment. Do not use parallel
chapter wall times for small before/after claims. Delete immediate
theorem/definition result echoes and transitive chain endpoints first, then
probe larger chains. A shorter proof is not necessarily faster, and a line
that looks repetitive may be the exact representation bridge needed later.
Finish with a clean registered `-runner -f` gate. Read the measured procedure
and examples in `references/proof-style.md` before optimizing a hot proof.

For a chapter-scale algebraic cleanup, also read
[`references/proof-style.md#chapter-scale-algebraic-cleanup`](proof-style.md#chapter-scale-algebraic-cleanup).
Freeze declarations, statements, settings, and source order; measure savings
only from accepted proof-body replacements; and treat failed whole-chain
deletion probes as evidence for the current-verifier practical floor.

## Catastrophic Bloat Gate

Treat the following recurring shapes as stop-ship proof bloat, not harmless
verbosity:

- **Definition-equation facade:** a `have fn` definition is followed by public
  zero/successor/evaluation theorems that merely restate its stored equations,
  and callers then cite those wrappers instead of using the definition.
- **Administrative adapter stack:** one mathematical operation passes through
  a chain such as `F -> choice_index -> pick -> phi -> b`, while each consumer
  replays the same function, membership, and equality representation. Keep
  unavoidable choice or carrier machinery local; replace one-use adapters
  with one helper named for the mathematical operation and prove only the
  specification consumed downstream. In Analysis Proposition 6.6.6, exposing
  `next_index(k,s)` instead of replaying `choice_index(F(k,s))` reduced the hot
  theorem's clean release time by about one third. See
  `references/proof-style.md` for the measured example and audit rule.
- **Expanded micro-pattern:** a routine move such as choosing a midpoint,
  turning two-sided bounds into an absolute-value bound, preserving order at a
  limit, shifting a finite prefix, or using an involution is rederived as a
  long local trace instead of using one existing mathematical interface.
- **Mirror-copy proof:** lower/upper, positive/negative, forward/reverse, or
  limsup/liminf arguments duplicate the same case tree or algebra with signs
  reversed instead of sharing the genuine common lemma.
- **Proof-only public sprawl:** one-consumer aliases, witness packagers,
  evaluation lemmas, or induction machinery become top-level API. Keep them
  local, use the underlying interface directly, or delete them; promote only a
  source-facing item or a helper with at least two independent consumers.
- **Premise and interface tax:** a theorem carries parameters or hypotheses
  unused by both its mathematical proof and conclusion. Remove genuinely
  redundant premises rather than making every caller manufacture them.
- **Recursive proof log:** finite enumeration, running maxima, dyadic blocks,
  or recursive constructions print every index-range, type, reflexive, and
  constructor consequence. State the invariant once and retain only the base,
  recursive mathematical move, and final use.
- **Non-mathematical source cargo:** generated metadata, audit counters,
  verifier-debug history, or a source-free language tutorial lives inside a
  mathematical proof file. Move machine data to an artifact and design notes
  to documentation; keep the proof source reader-facing.

Before accepting a touched file, inspect every `claim` with at most three body
lines, every run of at least five equality/comparison lines, every new or
touched helper with fewer than two independent consumers, and every theorem
premise not referenced in its proof or conclusion. Also compare repeated
lambdas and mirrored proof families for representation drift or copy-paste.
These are mandatory review triggers, not automatic deletion rules. Probe the
whole candidate path in the real enclosing `try:` context, keep source-facing
calculations, and restore only the smallest bridge that failure evidence shows
is necessary. Never apply a broad regex deletion to equality or comparison
lines.

## Quantified Redundancy Audit

For a chapter- or book-wide cleanup, classify code before estimating savings:

- `source_required`: source-facing definitions, results, examples, identities,
  and source order;
- `interface_required`: stable declarations with real downstream consumers;
- `proof_spine`: mathematical cases, induction invariants, witnesses, and
  decisive theorem applications;
- `reader_bridge`: an explicit theorem result that selects, instantiates, or
  translates the fact a reader needs for the next mathematical move;
- `verifier_bridge`: the smallest type, well-definedness, representation, or
  rewrite fact whose necessity was demonstrated by a failed shorter proof;
- `verified_removable`: a removed echo, wrapper, dead chain, or redundant
  endpoint whose real-context replacement verifies; and
- `blocked_by_existing_debt` or `unknown`: candidates that have not been
  honestly tested.

Count declaration consumers and fact-graph successors only to rank candidates.
Zero later consumers does not make a source theorem removable, and a locally
consumed chain can still be bypassable. Report a structural floor separately
from the current-verifier practical floor, and label all projected savings as
estimates until deletion probes pass. Keep generated counts and dependency
metadata outside mathematical `.lit` source.

## Proof Style

- Before adding a proof-body line, ask whether the current target already
  follows from the facts the preceding statement stored. Use a literal `try:`
  block to test the shorter version in the real local context.
- Omit verifier echoes when they add no mathematical move: do not restate a
  goal after a successful `by contra`; do not manually fold a witness's
  existential body back into its enclosing `prop`; and do not restate `Q(x)`
  after `P(x)` when a known implication or iff already derives `Q(x)`.
- Let `obtain` validate its own existential source. Write
  `obtain x from exist x T st {...}` directly; do not precede it with the
  identical standalone `exist x T st {...}` fact. Keep a separate existential
  only when it has an independent later consumer or a deletion probe shows
  that the surrounding proof needs a distinct stored bridge.
- When a concrete non-abstract named proposition has exactly one positive
  ordinary existential body, prefer the shorter named boundary:
  `obtain x from $P(args)` and `witness $P(args) from x`. Keep explicit
  `exist!`, propositions with additional clauses, abstract or nested
  definitions, and any real-context case that rejects the named form. The
  source proposition must retain the spelling for which proof evidence was
  established: changing an argument inside `$P(args)` to a transparent alias
  is not justified merely because both objects are well-defined or
  definitionally equal.
- Prefer the minimal witness form when the substituted existential body is the
  whole proof obligation. For example, write
  `witness exist u, v Z st {1 = a * u + b * v} from x, y` without a `:` block;
  Litex automatically checks `1 = a * x + b * y`. Add a witness body only for
  genuine intermediate reasoning, a nontrivial bridge, or a pedagogical step.
- Keep the source-facing theorem statement and pedagogically meaningful
  calculations. Compress repeated proof-body facts, not the mathematical claim
  a reader is meant to see.
- Keep comments mathematical. Do not narrate verifier states, code-generation
  decisions, cleanup history, local debugging, or audit counts in proof source.
- Do not delete a bridge merely because it is mathematically implied. In
  particular, conjunctions may need explicit component facts for `obtain`, a
  named package fact may be needed by a later substitution chain, and a
  function-definition equality may seed inference even when direct equality
  checking can unfold the function. Verify every proposed deletion in the
  surrounding proof, not only in a toy snippet.
- When several formulations are possible, use the most Litex-native and
  simplest checkable formulation as the main proof. Treat source-text shape or
  lower-level raw Litex expression shape as secondary unless the user asks for
  that comparison.
- When defining mathematical vocabulary, use names that stay close to standard
  mathematical wording. Do not simplify a conventional term into a private
  shorthand, and do not invent a new phrase when the usual one is clear.
- Name predicates by how they read in ordinary mathematics. Use `prop is_xxx`
  or `abstract_prop is_xxx` for judgment/property predicates, and use
  `prop has_xxx` or `abstract_prop has_xxx` when the declaration is a relation
  about existence, a witness, a candidate value, or a package. If the source
  introduces the value/function itself and later code must apply or cite it,
  use `have`, `have fn`, or `have fn ... by exist!`; do not hide that interface
  behind a `has_xxx(..., value)` predicate.
- Avoid suffixes such as `_R` or `_Q` when the parameter types already say the
  domain. If a distinction is genuinely needed, spell it out in the name, such
  as `is_close_in_Q` or `has_limit_in_R`. Avoid `_value` in predicate names;
  write `has_riemann_integral(I, f, s)` rather than
  `riemann_integral_value_R(I, f, value)`.
- Keep an explicit intermediate fact only when it is a mathematical move or
  the smallest verified bridge; checkability alone is not a reason to write it.
  Prefer one readable equality chain over a waterfall of one-step facts.
- When definition replay leaves a field of a tuple-backed struct, first try a
  Litex representation bridge instead of classifying it as missing kernel
  projection. Name the value as a typed local object, expose the needed
  coordinate-to-field facts and tuple reconstruction, then write the common
  representative chain in the form
  `(a, b) = obj = (obj.first, obj.second)`. For example:

```litex
have obj &Pair = make_pair
obj[1] = obj.first
obj[2] = obj.second
obj = (obj[1], obj[2])
(a, b) = obj = (obj.first, obj.second)
```

  This deliberately seeds known non-forall equalities so Tuple-to-Tuple
  comparison can expose the field equality. If the original expression is
  not itself the local symbol, connect its indexed coordinate through `obj`
  and keep the original object in interfaces that name it canonically. Only
  propose a builtin after this exact source-level bridge fails in the real
  caller or proves genuinely repetitive across independent callers.
- Prefer direct universal facts over redundant `claim: prove:` scaffolding
  when the `forall` statement already expresses the intended semantic fact.
  For example, write:

```litex
forall a, b R, x oc(a, b):
    x $in R
    a < x
    x <= b
```

  instead of:

```litex
claim:
    prove:
        forall a, b R, x oc(a, b):
            x $in R
            a < x
            x <= b
    x $in R
    a < x
    x <= b
```

  Use `claim:` only when the current proof needs to introduce a concrete
  local consequence that is not already being stated directly, or when a
  sub-proof is genuinely needed to export a final fact into the surrounding
  context.
- For cancellation, substitution under a larger expression, changing normal
  form, or applying the same algebraic context to both sides, prefer one
  equality/order chain that passes through the original stored expression.
  Add a named theorem only when the pattern is reused non-locally.
- For algebraic/numeric failures, split large jumps into smaller equalities before looking for new rules.
- For zero-product reasoning, use explicit division steps.
- Do not use `trust` to hide ordinary proof obligations. When a blocker
  requires `trust`, keep it on the narrowest substep, document it, and keep the
  rest explicit.
- Keep runnable snippets self-contained.
- For ordinary `forall` facts, do not write an empty `=>:` body.

Example naming pattern:

```litex
prop has_point_in_epsilon_neighborhood(X set, x R, epsilon R_pos):
    X $subset R
    exist y X st {y $in R, abs(x - y) < epsilon}

prop is_adherent_point(X set, x R):
    X $subset R
    forall epsilon R_pos:
        $has_point_in_epsilon_neighborhood(X, x, epsilon)

prop is_closure_of(C, X set):
    C $subset R
    X $subset R
    forall x C:
        $is_adherent_point(X, x)
    forall x R:
        $is_adherent_point(X, x)
        =>:
            x $in C

prop is_closed_subset(X set):
    $is_closure_of(X, X)

prop is_epsilon_neighborhood_inside(X set, x R, epsilon R_pos):
    forall y R:
        abs(x - y) < epsilon
        =>:
            y $in X

prop is_open_subset(X set):
    X $subset R
    forall x X:
        exist epsilon R_pos st {$is_epsilon_neighborhood_inside(X, x, epsilon)}

prop is_sequence_in_subset(a seq(R), X set):
    X $subset R
    forall n N_pos:
        a(n) $in X
```

## Blockers

When an item remains incomplete after the two-pass trust timebox, record the
smallest reproduction and choose exactly one primary label: `trust` or
`kernel_problem`. Explain the concrete
cause in prose—such as a missing definition or theorem interface, proof debt,
file organization, syntax, diagnostics, or suspected verifier behavior—but do
not create another coded blocker taxonomy. Keep the intended statement and the
narrowest legal `trust`; do not begin a third proof-search round without an
explicitly expanded user budget.

For source work under `scripts/` or a local translation workspace, update the nearby `todo.md` with concise blocker notes. Remove completed blocker notes when they no longer block the work.

## References

- Read `references/litex-corpus/INDEX.md` when searching bundled Manual/docs/examples.
- Read `references/proof-style.md` for common Litex proof moves.
- Read `references/function-set-composition-case-record.md` for function-set,
  template-alias, callable-field and returned-function examples: explicit value
  chains, checked typed views, general constructor facts, controls and public
  entry corrections. Treat it as dated case evidence and a scoped user
  preference, not an unconditional workaround or permanent kernel contract.
- Read `references/authoring-error-cards.md` after a failed attempt or when
  reviewing code that verifies but may be poorly shaped.
- Read `references/litex-repl-try-workflow.md` when running iterative verification.
- Read `references/proof-gap-mining.md` when recording, comparing, or
  promoting proof-attempt experience.
- Read `references/example-agent-kernel-loop.md` when a real example is meant
  to drive a recurring example, agent, and user-reviewed kernel improvement
  round.
- Read `references/litex-authoring-cheatsheet.md` before choosing declarations,
  fact shapes, proof actions, or the first repair after a verifier failure.
- Read `references/trust-timebox.md` whenever adding, reviewing, discharging,
  or deferring proof trust.
- Read `references/dataset-translation.md` when translating benchmark or dataset items.

## Persistent Task Ledger

When a proof, textbook slice, dataset batch, or needed kernel follow-up cannot
be completed in this turn, create or update
`todo/<YYYY-M-D>/<project>.md` at the repository root, using the current
environment date without zero padding. Record the current verified prefix,
the exact remaining theorem/proof step or minimal repro, its status and
blocker boundary, the next smallest action, and the verifier command. This
ledger complements the source's own todo, unfinished, and experience records;
delete it only when the scoped task is complete and verified.
