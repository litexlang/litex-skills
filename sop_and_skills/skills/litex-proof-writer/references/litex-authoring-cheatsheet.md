# Litex Authoring Cheat Sheet

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.


Use this sheet to choose the next authoring action. It is a decision aid, not
the language specification: confirm exact syntax and current boundaries in the
repository's `docs/Manual.md` and a runnable nearby example before finalizing a
proof.

For concrete failed-to-repaired and passing-but-poor code pairs, read
[`authoring-error-cards.md`](authoring-error-cards.md) after choosing the
failure phase or during the proof-liveness pass.

Within the golitex repository, keep the authoring choices aligned with the
public `docs/Litex_Learner_Cheatsheet.md`. This sheet may retain agent-only probing, failure
classification, and trust-journaling guidance that does not belong in the
public quick reference.

Read [writing-and-teaching.md](writing-and-teaching.md) for supported versus
recommended syntax and learner repair guidance. Default to multiline `forall`
and English/ASCII source; use `release thm` for unselected theorem calls.

## Choose What To Introduce

| Need | Use | Result or boundary |
|---|---|---|
| An arbitrary object in a nonempty set | `have x S` | Introduces `x` and `x $in S` |
| A local abbreviation for an already well-defined object | `let name = value` | Stores `name = value`; it does not declare a carrier |
| A name for a specific value | `have x S = value` | Checks the carrier, then stores membership and equality |
| A callable mathematical value | `have fn f(x S) T = body` | Use a function declaration, not a predicate encoding its graph |
| All legal inputs mapped to one object `y` | `preimage(f, y)` | Returns a set; `y` may itself be a set |
| All legal inputs mapped into a set `Y` | `preimage_set(f, Y)` | Returns a set and retains the function's carriers and guards |
| A concrete named property | `prop P(x S): ...` | Gives a foldable definition; declaring it does not prove an instance |
| A genuinely external property interface | `abstract_prop P(x)` | Does not supply truth or replace an unfinished concrete definition |
| One nearby derived fact | `claim:` with an indented `? fact` goal | Keeps proof machinery local and exports only the target |
| A stable reusable mathematical result | `thm name: ...` | Creates an explicit theorem interface and a reusable universal fact |
| An explicit assumption or localized proof debt | `trust fact` | Never use as ordinary proof automation; the result is not `checkable` |

Function parameter domains and the complete return object must not reference
the current signature's parameters. Those names are visible only in domain
conditions and bodies: `fn(x R: x > 0) R {x + 1}` is valid;
`fn(x R) {x}` and `fn(S power_set(R)) fn(x S) R` are parse errors. Use a fixed
return carrier and a separate precise output fact, or an enclosing template
parameter for a family. Ordinary forall/exist dependencies are unchanged.
This is the maintainer's explicit 2026-10-03 language rule; acceptance lives in
`examples/wd/fixed_function_signature_scopes.lit` and
`tests/unit/parse/function_signature_scopes.rs` in golitex.

For both preimage objects, membership checks the legal input conditions and
the output equality or membership; it does not solve for a root. Multiple
function parameters use an ordered input tuple, while a unary tuple parameter
receives the whole tuple. See `examples/wd/function_preimages.lit` and the
preimage preview in the current Manual for checked syntax and boundaries.

Promote a helper only when it is source-facing or has real independent
consumers. Keep one-proof functions, predicates, witnesses, and induction
machinery inside the enclosing `claim` or `thm` whenever the language permits.

Name a recurring nontrivial object when the proof treats it as one mathematical
atom. Prefer a role-based name. If one fixed template specialization is the
operation being repeated, alias that callable value itself:

```litex
let neg = \vector_neg<K, field, V, space>
neg(x)
```

Use the alias directly in ordinary atomic and object contexts; add an equality
bridge only after the direct real-context form fails. Keep public statements
and canonical quantified/structural fold boundaries canonical, because
directional reduction does not make a canonical goal search backward for a
stored alias-spelled fact. Do not name by character count or hide a constructor
that a later proof action must inspect: keep `fn_range(image_map)` explicit for
`have by preimage`. See P7 in
[`authoring-error-cards.md`](authoring-error-cards.md) for the checked callable
inverse and the canonical-fold/constructor boundaries.

## Required Proof Processes

The maintainer's 2026-10-12 syntax rule requires nonempty processes for
`claim`, `sketch`, `strategy`, block extensionality, finite enumeration,
range proofs and induction. Every proof `case` branch and explicit induction
base/step section also requires a body. A goal is not a process step;
comments do not count. A checked `impossible fact` tail counts as a step.
Named `thm` processes remain optional when their goals already verify.

Use a direct fact or bare `forall` for an automatically checked result rather
than padding a claim. Inline extension/definition/witness/Choice/Zorn commands
retain their syntax; an optional trailing proof-body colon requires actual
indented statements. All comment-only colon blocks are rejected before
statement parsing. See golitex `docs/Manual.md` (Proof Process),
`examples/stmt_nodes/proof_block/nonempty_proof_bodies.lit`, and
`tests/unit/parse/nonempty_proof_bodies.rs` for the accepted boundaries.

## Write The Fact Shape

| Mathematical shape | Canonical Litex shape |
|---|---|
| Atomic fact | `a = b`, `a $in A`, `$P(a)` |
| Equality or order chain | `a <= b = c < d` |
| Flat conjunction | `atomic and atomic` |
| Outer disjunction | `branch or branch` |
| Existence | `exist x S st {facts}` |
| Unique existence | `exist! x S st {facts}` |
| Universal fact | `forall x S:` with indented facts; use `=>:` only when there are assumptions. Inline syntax is supported but not the default style. |
| Negated existence or universal | `not exist ...`, `not forall ...` |

`and` is a flat atomic list, while `or` combines supported completed branches;
neither is an arbitrary recursively nested Boolean grammar. Existential and
set-builder bodies do not contain a direct `forall`: define a concrete `prop`
for the quantified condition and use its atomic call in the body.

## Choose The Proof Action

Dated capability acceptance, 2026-10-12: the repository's
`examples/proof_nodes/equal/by_builtin_rule/add_zero_from_equalities.lit`
verifies `plane_add((0,0),x)=(x(1),x(2))=x` without projection facts.
The fixed numeric addition builtin retains `b=c`, `a=0` (or the right-zero
pair); literal numeric tuple-coordinate carriers retain closed calculation
evidence. Existing WD and premise ceilings remain in force. Focused tests:
`tests/add_zero_builtin.rs`; Lean replay of the new evidence is unsupported.
This is a dated native-capability record, not a general normalization heuristic.

| Goal or available fact | Try first | Boundary |
|---|---|---|
| Direct carrier, arithmetic, equality, membership, or inferred consequence | State the target directly | Do not wrap a fact Litex already knows |
| Real absolute-difference symmetry or triangle; two-coordinate min/max error bound | State the distance or extremum bound directly | The extrema leaf consumes both checked coordinate error bounds; parent WD and the inherited premise ceiling remain required |
| A common positive radius from two checked positive reals | `have delta R+ = min(a,b)` | Both operands need checked positive membership; a nested minimum may use a typed intermediate |
| Positive concrete predicate whose definition body is proved | `by def $P(args)` | Folds only the matching positive definition target |
| Properties or tuple bridges of a declaration-owned struct expression | `by struct def expression` | Verifies the already-selected struct membership and opens exactly one layer; only a direct `x &Struct` symbol binding opens automatically |
| One directly returned atomic conclusion of a named theorem | `by thm name(args) => fact` | Requires structural/alpha matching; use `release thm name(args)` and separate proof steps to rewrite, reverse or combine results |
| Semantic constructor with compound requirements | The matching reserved `release thm` interface | Do not expect one-layer atomic automation to synthesize quantified premises |
| Existential target | `witness ... from ...` | Supply witnesses of the exact target shape and carrier |
| Known existential that must expose witnesses | `obtain ... from ...` | Do not restate the identical existential immediately before `obtain` |
| Universal fact over `range` / `closed_range` | `by for` | Bounded integer range, not an arbitrary set |
| Universal fact over a supported finite Cartesian product | `by for` | Requires the supported finite product shape |
| Universal fact over displayed finite domains | `by enumerate finite_set` | Every quantified domain must be concretely enumerable |
| Known member of an integer range | `by enumerate range` / `by enumerate closed_range` | Produces equality alternatives for that member |
| Equality of sets | `by extension` | Requires both membership directions; use function extensionality for functions |
| Known disjunction or exposed alternatives | `by cases` | Requires an exhaustive case source already in context |
| Negative goal | `by contra` | Must end with an actual contradiction, not a bare `impossible` |
| Discrete or finite-set induction | `by induc` / `by strong_induc` | Parameter, base, and invariant must match the supported induction shape |
| Bare universal whose proof needs proof-control statements | Wrap it in `claim` or name it with `thm` | Do not put `release thm`, `by thm`, `by def`, witnesses, or cases in a bare `forall` conclusion list |

Apply this order:

1. State the ordinary mathematical move.
2. Test whether the exact target is already known, builtin, or inferred.
3. Choose the matching native proof action above.
4. Search existing standard-library and source-local interfaces.
5. Try the smallest form in the real caller context.
6. Add only the smallest bridge demonstrated necessary by verifier evidence.
7. Use a manual proof spine only when the native boundary genuinely does not
   fit; apply the repository trust timebox before introducing proof debt.

## Triage A Failure Before Rewriting The Proof

| First failing phase | Check next | Do not conclude yet |
|---|---|---|
| Parse | Indentation, binder form, supported fact nesting, and current Manual syntax | The mathematical statement is unsupported |
| Name or type resolution | Import visibility, fresh binders, arity, callable metadata, and exact declared carrier | A theorem is missing |
| Well-definedness | Domain membership, refined carrier, nonzero divisor, index bound, and argument well-definedness | The target is false or unprovable |
| Proof search reports `unknown` | Direct known fact, one native surface, existing theorem/definition, then the smallest intermediate equality or carrier fact | `trust` is required |
| A statement verifies but later use fails | What was stored, whether the object is callable, and whether it has an executable definition | The earlier proof did nothing |
| Output is strange or a phase behaves inconsistently | Preserve the exact attempt, add the nearest accepted control, and isolate a minimal reproduction | `kernel_problem` without comparative evidence |

For algebraic failures, split a large jump into a short equality chain before
searching for another theorem. When rewriting inside a function, sequence,
sum, product, or recursive call, establish the changed inner value or index
first. Keep the original stored expression on the path, for example
`n*(3/2) = n*x = 96`, instead of writing only the endpoint. If several normal
forms are needed later, connect them in one continuous chain in the order in
which they are consumed. Keep a verifier-only bridge only if a real-context
deletion probe shows that it is needed.

Direct scalar cancellation is an infer route: stored `a+k=b+k` publishes
`a=b`; differences `a-k=b-k` and `k-a=k-b` do the same. Stored `a*k=b*k`
or `a/k=b/k` does so when `k!=0` is already available. For `k/a=k/b`, also
require `a!=0` and `b!=0`; a zero common numerator cannot cancel. Subtraction
and division allow same-position operands only, not crossed operands. State the
remaining equality directly instead of adding a division chain for these
exact shapes. The common operand must match directly; there is no alias/AC
search. If the nonzero certificate arrives later, restate the product equality.
Acceptance: `examples/infer/equal/additive_cancellation.lit`,
`examples/infer/equal/nonzero_factor_cancellation.lit`, and the positive,
negative, premise-ceiling and scope controls in `equality_cancellation` tests.
Subtraction and division have dedicated `subtractive_cancellation.lit`,
`common_denominator_cancellation.lit`, `nonzero_numerator_cancellation.lit`
tracers in the same directory.
Lean replay of these inferred citations remains unsupported and fail-closed.

Use a native predicate directly when it already states the mathematics. Do not
publish a one-use, constant-specific prop that merely forwards a builtin such
as `$dvd(dividend, divisor)`. For bounded enumeration, make the conclusion
retain every classification coordinate needed downstream; otherwise classify
the full tuple or choose a one-coordinate predicate instead of expecting
forall matching to reconstruct a premise-only parameter.

## Hard Boundaries

- `by def` is definition folding, not general automation.
- `by struct def e` cannot select a view from later membership, equality, or
  field-name search; `e` must already have a declaration-owned struct view.
- A legal field path proves only well-definedness. It does not release field
  carriers, tuple/index bridges, or struct laws, and opening an outer struct
  never recursively opens its struct-valued fields.
- A theorem call that selects one fact should not be followed by the identical
  fact as an echo.
- A named theorem whose then-clauses already follow from its own settings,
  binders, premises, or ordinary verifier rules should have no proof statements;
  never repeat a then-clause only to make the body nonempty. Verify the
  bodyless form in the real context, and keep a body for every genuine proof
  move.
- `claim` proves a fact; it does not introduce a callable value.
- A `prop` names a property; it does not replace `have` or `have fn` when later
  code must use the value itself.
- `unknown` calls for phase classification and the next smallest bridge before
  proof debt.
- Any surviving `trust` must remain localized, journaled, and honestly
  classified; code containing it is not `checkable`.
