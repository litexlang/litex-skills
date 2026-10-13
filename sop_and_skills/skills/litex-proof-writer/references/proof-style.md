# Litex Proof Style

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.


Use direct, local mathematical steps. Every Litex line must express a genuine
mathematical move or the smallest verifier-proven bridge; being checkable from
the current context is not by itself a reason to write the line.

## Contents

- [Proof Spine Before Syntax](#proof-spine-before-syntax)
- [Proof Liveness and Fact Cascades](#proof-liveness-and-fact-cascades)
- [Chapter-Scale Algebraic Cleanup](#chapter-scale-algebraic-cleanup)
- [Performance-Aware Liveness](#performance-aware-liveness)
- [Avoid Administrative Abstraction Chains](#avoid-administrative-abstraction-chains)
- [Selected Theorem Results and Reader Bridges](#selected-theorem-results-and-reader-bridges)
- [Equality Chains](#equality-chains)
- [Same-Context / Cancellation Chains](#same-context--cancellation-chains)
- [Zero Product](#zero-product)
- [`trust` Policy](#trust-policy)

## Proof Spine Before Syntax

Before formalization, write a short ordinary-language proof at the abstraction
level used in normal mathematical practice. Then map each Litex block back to
one of its steps. A runnable proof is still badly shaped when it manually
reimplements a construction or theorem that the mathematical proof simply
cites.

For example, suppose bijectivity gives `f : N -> X` and the target asks for an
injection `X -> N`. The concise proof spine is:

1. take the inverse `g : X -> N` of the bijection `f`;
2. use that the inverse of a bijection is injective, and witness `g`.

The injectivity of `f` alone has the wrong direction and does not close the
goal. But manually defining `g` by unique preimages, reproving existence and
uniqueness for every `x`, and then reproving inverse injectivity is also the
wrong final abstraction when an inverse-function interface already exists.
Use that interface. If the library exposes only a unique-preimage theorem, use
it to discharge the selection step instead of replaying its proof. If no
inverse interface exists, record a general-interface gap rather than treating
the repeated local reconstruction as desirable proof style.

After verification, ask:

- Which natural-language step does each code block implement?
- Is any block proving a fact already packaged by an earlier theorem or
  definition?
- Did a verifier workaround silently become the apparent mathematics?
- Can a lower-level block be replaced by one named interface and still verify?
- Does the final proof expose roughly the same decisive moves as the proof
  spine?

## Proof Liveness and Fact Cascades

Do not accept a proof merely because every line verifies or because every fact
appears to have a later consumer. Generated proofs often materialize the
verifier's internal route instead of expressing the mathematical argument.
Call this **proof-trace redundancy** and distinguish:

- an **inference echo**, which repeats a fact already stored or inferred;
- a **dead fact** or **dead chain**, which does not reach any live output; and
- a **bypassable derivation chain**, whose lines consume one another but whose
  final useful fact is reachable without the chain.

For example, a proof may expand one set declaration into a fact cascade:

```litex
have S power_set(N) = {n X: n <= a}
S = {n X: n <= a}
a <= a
a $in {n X: n <= a}
a $in S
finite_set_min(S) $in S
finite_set_min(S) <= a
```

The later lines are not justified merely because each can feed the next one.
Test whether the declaration, the ambient facts about `a`, and the
`finite_set_min` interface already discharge the live downstream obligations.
If so, delete the entire cascade. This catches the common failure that an
ordinary unused-variable scan misses.

After a candidate proof verifies, run this audit:

1. Write down the live outputs: the theorem goal, required witnesses, exported
   claim conclusions, and source-facing calculations worth showing.
2. Walk backward and mark only facts needed to reach those outputs. Delete
   unmarked facts and subproofs.
3. For every surviving chain of definition unfolding, reflexivity, membership
   conversion, theorem-result repetition, or predicate folding, ask whether
   its endpoint follows directly from the context before the chain.
4. Delete the whole chain in the real enclosing `try:` context. Do not test
   only one isolated line: removing a complete bypassable path can succeed
   even when removing one of its locally consumed links fails.
5. If the shorter form fails, add back the smallest exact bridge indicated by
   verifier evidence. Do not restore the original waterfall wholesale.
6. Run the final file or project checkpoint. A fact graph or lexical search is
   only a candidate finder because inferred dependencies may be absent.

The final Litex blocks should correspond closely to the ordinary-language
proof spine. Keep a pedagogically meaningful estimate, case split, witness, or
named theorem application; remove the trace by which the verifier happened to
rediscover its automatic consequences.

## Chapter-Scale Algebraic Cleanup

Freeze the mathematical surface before measuring a cleanup: preserve every
source-facing declaration, theorem statement, setting, export, and source-order
dependency. Replace proof bodies only. This prevents artificial savings from
silently weakening or reorganizing the chapter API.

Use one source-order session for the complete chapter. For each proof, submit
the shortest candidate matching its ordinary-language spine, record failures,
commit the accepted block in that session before testing its consumers, and
stage its source in the journal for checkpoint materialization. Probe these
patterns first:

1. **Law waterfall to one calculation.** Replace separate associativity,
   identity, inverse, and congruence states with one equality chain. Keep only
   an atomic bridge whose deletion fails in context.
2. **Direct interface instead of premise logging.** Call an existing
   transitivity, cancellation, inverse, or absorption theorem directly rather
   than first restating every premise that the call can discharge.
3. **Delete local-premise echoes.** A local universally quantified hypothesis
   may instantiate directly inside a calculation chain. Delete a standalone
   copy of that exact instance and restore it only if the chain fails.
4. **Reuse equality transport.** When a stored equality lets the next theorem
   call rewrite a membership or comparison assumption, omit the rewritten
   membership echo.
5. **Probe symmetric families independently.** A successful meet proof is
   strong evidence for the join dual, but still submit the dual candidate; do
   not infer checkability from mathematical symmetry alone.

The Mathematics in Lean Chapter 2 cleanup on 2026-08-06 is the reference
case. Its tracer `mul_inv_rev` has two mathematical moves: prove that
`b⁻¹a⁻¹` is an inverse of `ab`, then use inverse uniqueness. The accepted body
compresses the former 20-line verifier-state log to six lines:

```litex
mul(inv(a), a) = one
mul(inv(a), mul(a, b)) = mul(mul(inv(a), a), b) = mul(one, b) = b
mul(mul(inv(b), inv(a)), mul(a, b)) = mul(inv(b), mul(inv(a), mul(a, b))) = mul(inv(b), b) = one
by thm mul_inv_cancel(A, mul, one, inv, mul(a, b))
by thm _group_mul_one(A, mul, one, inv, mul(inv(b), inv(a)))
mul(inv(b), inv(a)) = mul(mul(inv(b), inv(a)), one) = mul(mul(inv(b), inv(a)), mul(mul(a, b), inv(mul(a, b)))) = mul(mul(mul(inv(b), inv(a)), mul(a, b)), inv(mul(a, b))) = mul(one, inv(mul(a, b))) = inv(mul(a, b))
```

The same pass shortened both lattice associativity proofs from 16 proof lines
to 10 by citing transitivity directly, both distributivity-transfer proofs
from 11 to 9 by deleting echoed local hypothesis instances, and one
ordered-ring monotonicity proof from 6 to 5 by reusing equality transport.
Across 19 proofs, the chapter fell from 576 to 514 physical lines while all 49
top-level declarations remained in source order.

Do not force every short proof below its verifier floor. Failed deletion probes
in the same session showed that:

- named theorem results needed for contextual rewrites still require explicit
  `by thm` instantiation even when local `forall` hypotheses instantiate in a
  chain;
- lattice commutativity needs the four primitive meet/join operand bounds and
  the two endpoint bounds under the current one-step rule boundary;
- rewriting `add(a, b)` inside `add(add(a, b), neg(a))` may require both the
  atomic commutativity fact and its lifted contextual equality; and
- pair equality is not synthesized merely from the two scalar endpoint
  equalities in the ordered-ring relation proof.

Classify those retained lines as `verifier_bridge`, not redundancy. Finish a
chapter cleanup only after the accepted journal source matches the
materialized file, the clean file and whole-module runners have top-level
`ok=true`, the registered harness passes when applicable, and the trust and
declaration counts have no unintended delta. The evidence for this case lives
in
`scripts/mathematics_in_litex/experiments/chapter02_proof_liveness_2026-8-6.json`
and
`scripts/mathematics_in_litex/experience/problem_notes/chapter02-proof-liveness-acceptance.md`.

## Performance-Aware Liveness

Do not infer hot spots from file length. Every explicit atomic fact can trigger
well-definedness work, known-`forall` search, argument checking, and storage,
but a long theorem may also spend most of its time on genuine subclaims. Find
the expensive top-level statement before rewriting it: start one release
`target/release/litex -compact -session -before <registered-file.lit>` process,
submit the target statements in source order, and record the client-observed
elapsed time of each framed block. Keep every candidate inside a literal
outermost `try:` so a failed timing probe rolls back itself.

For deletion experiments, materialize one candidate at a time in a unique
temporary project copy and compare complete release runner wall times serially
with the same binary and machine conditions. Require top-level `ok: true` and
exit code `0`, then run the canonical registered file with `-runner -f`. Do not
compare small timing changes from parallel agent runs; use those runs only for
independent pass/fail coverage.

Probe candidates in this order:

1. Remove the exact result repeated immediately after `by thm` or `by def`.
2. Remove a comparison/equality endpoint already supplied by the preceding
   chain, including an unnecessary symmetric restatement.
3. Use bodyless witness syntax when the supplied witness already establishes
   the sole witness-body fact.
4. Delete a whole suspected cascade, not an arbitrary middle line. If the next
   consumer fails, restore only the first exact representation bridge it needs.
5. Reprofile the complete candidate theorem; line count alone is not evidence.

The 2026-08-05 Analysis audit gives three useful contrasts. Removing nine
result echoes from `rectangle_partial_sum_realization` reduced an isolated
preview from 7.63 s to 5.70 s (25.2%). Removing thirteen result and comparison
echoes from `derivative_product_rule_estimate` reduced 8.59 s to 7.20 s
(16.1%). Removing twenty-three binder, witness-body, and symmetric-equality
echoes from `example_11_2_12_piece_contribution_has_values` changed 12.93 s to
12.70 s (1.8%): most of that theorem's cost remained in six genuine subset,
constant-value, and existence checks.

Failed deletions are equally important. The Chapter 8 pointwise `nested`
expansion was needed for a later `nested = column_nested` transport. The
Chapter 10 elementary derivation of the bound on `abs(g(z))` and the two-step
normalizations for `A`, `B`, and `set_C` were also required. Classify these as
`verifier_bridge`, not redundancy. The practical rule is: delete visual echoes
aggressively, but let the first downstream verifier failure decide which
representation bridge survives.

## Avoid Administrative Abstraction Chains

Do not confuse a high mathematical abstraction level with adding more local
names. A helper earns its place when it names a proof-spine operation and
exports the exact specification used later. A one-use carrier adapter that
only forwards another helper's value usually adds representation transport
without hiding a mathematical argument.

Analysis Proposition 6.6.6 originally constructed a convergent subsequence
through the local chain

```text
F -> choice_index -> pick -> phi -> b
```

The monotonicity and convergence blocks then repeatedly unfolded
`pick(F(k,s))` to `choice_index(F(k,s))`, transported membership through the
set builder, and rebuilt the same tail and closeness facts. The better shape
kept `F` and `choice_index` inside the unavoidable choice construction and
exposed one operation aligned with the ordinary proof:

```litex
have fn next_index(k N+, s N+) N+ = choice_index(F(k, s))
forall k N+, s N+:
    # Retain only the two representation bridges shown necessary by deletion probes.
    choice_index(F(k, s)) $in F(k, s)
    next_index(k, s) = choice_index(F(k, s))
    next_index(k, s) $in F(k, s)
    next_index(k, s) >= s
    abs(a(next_index(k, s)) - L) < 1 / k
```

The recursive `phi` and subsequence `b` then consume the final two properties
directly. A clean release run on 2026-08-03 reduced that theorem from 10.357 s
to 6.986 s, about 32.5%, while preserving checkability. Apply this audit:

1. Write the mathematical operation performed by the whole helper chain.
2. Keep one local helper for that operation, not one helper per representation.
3. Prove the downstream specification once next to the helper.
4. Delete repeated unfolding and transport cascades at each consumer.
5. Deletion-probe the remaining carrier or defining equalities and keep only
   bridges whose absence produces a concrete verifier failure.

Do not flatten a repeated long term blindly: duplicating a large set builder or
choice expression can be as bad as over-wrapping it. Flatten administrative
layers; retain the single name that matches the mathematical proof spine.

## Selected Theorem Results and Reader Bridges

When a theorem application contributes one atomic fact, prefer selecting that
fact on the call itself:

```litex
by thm closure_of_bounded_intervals(a, b) => closure_of_real_set('[a, b]) = '[a, b]
$is_closed_subset('[a, b])
```

The arrow says exactly which returned or inferred atomic consequence matters,
which concrete source object the theorem is instantiated at, and which
representation the next step consumes. Litex checks that fact with the
theorem's instantiated results in a temporary context, then commits only the
selected fact. Select the direction actually needed by the next calculation;
the selected fact may be an ordinary atomic inference rather than a verbatim
theorem conclusion:

```litex
by thm group_inverse_unique(B, mul_B, one_B, inv_B, one_B, one_B) => inv_B(one_B) = one_B
```

Use `release thm theorem_name(args)` only when several distinct theorem
results are genuinely consumed, or when the desired result is compound,
quantified, existential, disjunctive, conjunctive, or a chain and therefore
cannot be selected by `=>`. Bare `by thm theorem_name(args)` remains a supported
compatibility alias. The current selection surface requires the inline arrow;
do not suggest a colon goal block for a selected theorem call.

Do not release all results and then repeat the chosen atomic fact:

```litex
claim:
    ? P
    release thm p()
    P
```

Write `by thm p() => P` instead. The selected-result call may close the atomic
goal directly; no second `P` line is needed.

## Proof-Spine Alignment Example

For uniqueness of an additive inverse, the natural proof has two moves: choose
one inverse for existence, then compare two inverses by one chain through
`y2 + (x + y1)`. The formal uniqueness block should therefore be one equality
chain, not separate logs for every use of commutativity, associativity, and the
zero law. If Litex cannot rewrite `x + y2` inside `(x + y2) + y1`, keep the one
explicit inner equality needed to seed that rewrite, then write the full
mathematical chain. This is a `verifier_bridge`; the surrounding law-by-law
cascade is not.

## Formalize Easy Examples

Do not use prose as a substitute for an easy textbook example. Add a `sketch:`
that states the example's actual objects and claims, or give it a checked
theorem when the proof is direct. The source comment may explain the example,
but a comment-only numerical or endpoint illustration is incomplete
translation coverage.

## Equality Chains

Prefer chains like:

```litex
a = b = c = d
```

When a jump fails, split it:

```litex
(3 - 2 * sqrt(2)) * (3 + 2 * sqrt(2)) = 3^2 - (2 * sqrt(2))^2
(2 * sqrt(2))^2 = 8
3^2 - (2 * sqrt(2))^2 = 9 - 8 = 1
```

## Same-Context / Cancellation Chains

When a proof applies the same algebraic context to both sides of an equality
or cancels a shared term, prefer one compact chain instead of several
one-step facts plus a final equality:

```litex
n = (n + 1) - 1 = succ(n) - 1 = succ(m) - 1 = (m + 1) - 1 = m
b = (a + b) - a = (a + c) - a = c
n = (n + k) - k = (m + k) - k = m
```

Use a named cancellation theorem when the cancellation is not the main proof
move, or when an existing local theorem already expresses the repeated step.
Do not add a new theorem just to avoid a short readable chain.

## Zero Product

If `u * v = 0` and `v != 0`, prefer:

```litex
u = 0 / v
u = 0 / v = 0
```

## `trust` Policy

Do not use `trust` to finish an example that should be checkable. Once a real
blocker is identified, keep `trust` on the narrowest blocked substep, document
the debt, and continue. A declaration containing `trust` is not `checkable`.
