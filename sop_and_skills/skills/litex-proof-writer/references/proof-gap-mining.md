# Proof-Gap Mining

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.


Use proof attempts as evidence about the distance between ordinary
mathematical reasoning and checkable Litex. Definitions state what the
mathematics means; the verifier trace shows which formal bridges, interfaces,
and kernel behavior make that meaning usable.

## Contents

1. Evidence model
2. Journal fields
3. Promotion rule
4. Reusable proof-gap patterns
5. Blockers and consumers

## Evidence model

Produce two artifacts:

- Keep one chronological JSON proof-block journal per task. Record a candidate
  before changing `.lit`, append the result before repairing it, and preserve
  accepted source before materialization.
- Distill recurring mechanisms into short rules that future proof writers can
  search before trying the same proof shape.

Preserve materially different strategies and representation choices. Collapse
identical retries, formatting-only changes, and diagnostics that add no new
evidence. Record concise mathematical intent and decision evidence; never
record hidden chain-of-thought.

Treat a successful final proof as one result, not the whole experiment. Failed
attempts often contain the only evidence for a missing carrier conversion,
contextual rewrite, executable interface, or kernel phase distinction.

## Journal fields

Use the base schema in `litex-repl-try-workflow.md`. Add these optional fields
when a proof is nontrivial or fails:

```json
{
  "proof_spine_move": "unfold one recursive step",
  "failed_phase": "well_definedness",
  "failure_mechanism": "the quotient is positive mathematically but is not an N+ term",
  "minimal_fix": "select a typed quotient and prove strict decrease separately",
  "lesson_candidate": "refined recursive arguments require typed data plus termination evidence",
  "promotion_evidence": ["source-item-a", "source-item-b"]
}
```

Use `failed_phase` only to locate the failure:

- `transport`: session framing or process protocol;
- `parse`: block grammar or command placement;
- `name_or_type`: scope, imports, binders, or carrier mismatch;
- `well_definedness`: domain, closure, refined carrier, or division evidence;
- `proof`: a genuine mathematical or rewrite obligation;
- `generated_fact_storage`: a definition verifies but its stored equation does
  not retain required evidence;
- `later_use`: the declaration is accepted but a consumer cannot use it as
  expected;
- `clean_replay`: session blocks pass but the required clean file or module
  gate fails or does not terminate.

These phases are diagnostic coordinates, not blocker labels. Keep the formal
blocked status exactly `trust` or `kernel_problem`.

## Promotion rule

The miner nominates; it never promotes. Apply the repository policy's full
Task SOP -> journal -> miner -> acceptance -> permanent-skill pipeline.

Before a candidate enters reusable skill knowledge:

1. Normalize it as a decision rule with its context, earliest failed phase,
   preferred move, and nearest boundary. Remove source-specific names.
2. Require multiple independent source-item or task journals. Retries, raw
   transcripts, replay files, liveness variants, and copied drafts of one
   target form one evidence family. Prefer evidence across workspaces.
3. Preserve a verified positive example, an executable negative or deletion
   control for the boundary, exact commands, and the supporting journal ids.
4. Test the candidate on held-out work not used to formulate it. Compare the
   prior skill or recorded baseline using appropriate measures such as phase
   diagnosis, attempts to first acceptance, proof bloat, trust delta, or clean
   replay. Require no boundary regression.
5. Route the result correctly: authoring decisions to this skill or its error
   cards, mechanical smells to a linter, missing mathematics to a library,
   unclear phases to diagnostics, and stable verifier behavior to a kernel
   regression. Do not promote a kernel workaround as authoring style.

A single interface-impacting failure or stable control experiment can make a
candidate urgent, but cannot independently satisfy permanent-skill promotion.
Keep one-off syntax repairs in the local journal. Promote the mechanism, not a
book-specific name, and retain source ids so later kernel or library changes
can retest and retire the rule.

## Reusable proof-gap patterns

The following rules were extracted from the Concrete Mathematics Chapters
1--2 experiment.

### Recursion and contextual rewriting

- Unfold recursive definitions one stored equation at a time. Concrete
  evaluation does not imply deep normalization.
- Normalize an inner recursive argument such as `(m + 1) - 1 = m` before
  rewriting the enclosing function application.
- Materialize the exact atomic function value or changed operand before
  rewriting it under addition, multiplication, a function call, or a fold.
  Then use one continuous equality or order chain.
- Separate mixed solver work. Isolate recursive rewriting, nonlinear
  arithmetic, and the thin induction assembly instead of sending one large
  opaque chain.

Evidence: `CM-1.1-HANOI`, `CM-1.1-E1.2`, `CM-1.1-E1.3`,
`CM-1.2-E1.5-CLOSED`, and `CM-1.2-E1.7-CLOSED`.

### Carriers are construction obligations

- Do not treat mathematical nonnegativity or integrality as a Litex carrier
  proof. For an `N`-valued closed form containing subtraction or division,
  prefer a carrier-preserving recurrence or sum as the construction and keep
  the closed form as a theorem or specification.
- For `sum(first, last, term)`, establish `first <= last` or encode the empty
  case explicitly. Choose the anonymous function's return carrier to match
  the intended aggregate carrier.
- Introduce a refined result as typed data plus a representation equality.
  Arithmetic positivity of `n / 2` does not itself create an `N+` recursive
  argument; selection, carrier evidence, and strict decrease are distinct
  obligations.
- Separate admissible digit data from arithmetic evaluation. Membership in a
  finite digit set may require an explicit conversion into `N` or `Z`.

Evidence: `CM-1.2-E1.5`, `CM-1.2-E1.7`, `CM-1.3-E1.8`,
`CM-1.3-E1.15`, `CM-1.3-E1.16`, and `CM-2.2-E2.7-8`.

### Scope and block grammar are proof constraints

- Bind every symbolic parameter explicitly; mathematical prose does not
  create module scope.
- Keep dependent and nested anonymous-function binder names distinct when an
  outer binder remains active.
- Test proof commands at their actual indentation and grammar position. A
  `forall ... =>:` consequent accepts facts and may reject a `by thm` or
  `by def` command that is legal in a surrounding theorem, case, witness, or
  claim body.
- When induction must generalize another variable, package the strengthened
  statement as a named prop and induct on that atomic proposition.

Evidence: `CM-1.2-E1.7-NAMED-BRIDGES`, `CM-1.3-E1.9`,
`CM-1.3-E1.10`, and `CM-1.3-E1.11-12`.

### Callability is not executability

- Distinguish three capabilities: a function can be called in a proposition,
  its stored facts can support rewriting, and its body can be consumed by a
  new checked definition. Do not infer the third from the first two.
- Treat opaque trusted functions as public interfaces, not executable
  definitions. Declare a related opaque object group and the symbolic laws
  that compose it contiguously before later consumers rely on those laws.
- When one checked definition consumes another, test them in one contiguous
  transaction. A helper loaded by `-before` may be visible in facts yet fail as
  a new definition-body dependency.

Evidence: `CM-1.3-E1.13-14`, `CM-1.3-E1.16`, and
`CM-1.3-E1.17-18`.

### Folds and higher-order refinements need phase tests

- Unfold a concrete fold through each representation boundary: safe wrapper,
  builtin fold, endpoint recurrence, anonymous-function value, then
  arithmetic. Do not infer a generic fold theorem from one concrete
  normalization.
- Test higher-order definitions in separate phases: expression
  well-definedness, recursive verification, generated-fact storage, and later
  use. A refinement such as `b(n) != 0` may pass the definition and disappear
  while its recursive equation is stored.
- Compare with the closest direct control. If branch-local `n > 0` preserves
  the evidence for `1 / n` but a refined function result does not preserve
  evidence for `1 / b(n)`, diagnose higher-order refinement propagation rather
  than division or recursion in general.

Evidence: `CM-2.1-E2.1-5`, `CM-2.2-E2.6`,
`CM-2.2-E2.9-11`, and `CM-2.2-E2.12-14`.

### Session proof and clean replay are separate claims

- Record session acceptance and clean file replay separately. A proof can pass
  block by block yet make the cold registered-file path non-terminating.
- Preserve the full checked block sequence in the journal when replay fails.
  Keep the smallest exact source-facing interface or proposition under narrow
  trust only when required to restore the clean gate; retain checked consumers
  whenever possible.
- Classify a silent clean replay as `kernel_problem` only after segmented
  blocks or a control establish that the mathematics itself verifies.
- Distinguish the Litex transaction from its transport. In the current
  machine-readable session protocol, frame the literal outermost `try:` source
  as `run <id> <utf8-byte-count>`; raw multiline source alone is not a session
  request.

Evidence: `SESSION-PROTOCOL`, `CM-1.2-E1.7-CLOSED`,
`CM-1.3-E1.8`, `CM-1.3-E1.9`, and `CM-1.3-E1.11-12`.

### Proof-liveness boundaries in algebraic and lattice proofs

- Distinguish local quantified premises from named theorem results. A local
  `forall` assumption may instantiate inside an equality chain, while a named
  commutativity, associativity, or absorption theorem often needs an explicit
  `by thm` call before its equality can rewrite a subterm contextually.
- Treat universal meet/join rules as one-step consumers of known premise
  facts. Materialize the primitive operand bounds before the endpoint bound;
  do not expect endpoint checking to recursively synthesize those premises.
- When a scalar equality must rewrite under an outer operation, deletion-probe
  both the scalar fact and its lifted contextual equality. The latter may be
  the smallest live bridge even though ordinary congruence makes it
  mathematically immediate.
- Do not assume product or pair congruence is available from coordinate
  equalities. If relation membership changes both endpoints, retain the two
  scalar equalities when a direct pair-equality probe fails.
- Record these failed shorter candidates as the current-verifier practical
  floor, not as `kernel_problem`. Promote a kernel or inference request only
  after the same bridge recurs broadly and a control isolates stable missing
  behavior.

Evidence: `C02-LIVE-034` through `C02-LIVE-045` in
`scripts/mathematics_in_litex/experiments/chapter02_proof_liveness_2026-8-6.json`.

## Blockers and consumers

Use `trust` when the current proof, formulation, library, syntax, or
organization remains incomplete. Use `kernel_problem` only when a minimal
reproduction or control isolates verifier, storage, runtime, or replay
behavior.

Route distilled evidence to its real consumer:

- add a proof rule here when it changes how future Litex should be written;
- add or repair a reusable theorem when the mathematics is repeatedly absent;
- create a diagnostic improvement when the failure phase is hard to locate;
- create a minimal kernel regression when controls isolate verifier behavior;
- update concept modeling when the failure came from choosing the wrong
  mathematical interface rather than from proving it.
