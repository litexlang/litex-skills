# Equality and Inequality: Problem and Improvement Status

> Imported reference snapshot (2026-10-13). Use [the hub execution contract](../../litex-reference/references/execution.md). Repository conventions apply to the source project; dated examples remain historical until replayed.
> Receipt links contain summaries, not full verifier output. Original hashes, commands, and recorded outcomes remain available; see [evidence packaging](evidence-packaging.md).

This overview distinguishes existing support, shorter proofs that have been
found, and direct forms that remain unverified. Each entry is scoped to its
linked case's date, premises, binary, and context. Historical acceptance does
not establish support in newer unbuilt source. The original case and receipt
retain the positives, negatives, failure phases, and commands.

## User-selected builtin-rule candidates

| No. | Mathematical target in the original selection | Recorded acceptance |
| --- | --- | --- |
| 1 | `a<=b, c<=d ⇒ a-d<=b-c` | Implemented and integration-checked; [Part 2](part-02-subtraction-order.md). |
| 2 | `k!=0, a*k=b*k ⇒ a=b` | Excluded by the user from that implementation scope; do not add it again based on the old candidate. |
| 3 | `v!=0 ⇒ |v|!=0` | Existing rule; its `u/|v| $in R` consumer was checked too. No duplicate implementation. |
| 4 | `r>=0, x^2<=r^2 ⇒ |x|<=r` | Implemented and integration-checked; [Part 42](part-42-absolute-square-radius.md). |
| 5 | `b>0, a<=M*b ⇒ a/b<=M` | Implemented, including the strict variant; [Part 45](part-45-quotient-scalar-bound.md). |
| 6 | `a,b $in Z, b!=0, a%b=0 ⇒ a/b $in Z` | Implemented for positive and negative divisors; [Part 56](part-56-exact-integer-quotient.md). |

See [the selection record](selected-bt-candidates.md) for the decisions and
historical build boundaries, and [repository acceptance](https://github.com/litexlang/golitex/blob/e6f0fb6cab0bb69f99eb9a33b30deceae6d0a74a/tests/unit/execute/selected_scalar_bt_rules/acceptance.md)
for implementation evidence. This table does not widen the selection or claim
new Lean adapters or repository-wide coverage.

## Short forms found: reuse before expanding

| Situation | Checked short form or reduction | Complete context and boundary |
| --- | --- | --- |
| Actual Bayes substitution | Retain `evidence>0, joint=likelihood*prior`; the theorem body may be empty. | [Part 88](part-88-bayes-definition-substitution.md) |
| Newton numeric error endpoint | One `gap(2)<=bound(2)=1/64` chain; the symbolic theorem remains in the prefix. | [Part 86](part-86-newton-numeric-checkpoint.md) |
| AM-GM | Four statements: square certificate, square bound, nonnegative half-sum, and root chain; the source contradiction block can be removed. | [Part 92](part-92-textbook-am-gm-root-chain.md) |
| Simple function order | `x<=y ⇒ identity(x)<=identity(y)` checks from the definition. | [Part 96](part-96-simple-function-order.md) |
| Ordinary nested identity | `identity(identity(x))=x` checks directly. | [Part 97](part-97-nested-identity-range.md) |
| Actual Pascal identity | Preserve the recurrence and premises; 16 body steps become 6. The native theorem call also passes. | [Part 108](part-108-showcase-pascal-identity.md), rounds 68–69 |
| Actual uniqueness of sequence limits | Positivity/radius preparation goes from 7 steps to 2; later common-tail, symmetry, and comparison chains remove another 6 steps. Keep both limits and radii. | [Part 113](part-113-showcase-limit-gap-positivity.md), rounds 74–75 |
| Actual coordinate difference quotients | Each direction goes from 8 facts to 2 function-value equations; later partial-derivative proofs pass. | [Part 114](part-114-showcase-coordinate-quotients.md), round 76 |
| Actual linear-algebra showcase | Real-field laws go from 18 statements to 1; projection calculations from 28 to 10. The complete shorter draft passed strict checks on its fixed snapshot. | [Part 120](part-120-showcase-real-field-laws.md), [Part 125](part-125-showcase-projection-linearity.md) |

Unqualified function names summarize the mathematics; each Part provides the
actual declarations and premises. Where a bare target already passes, do not
add value equations, type echoes, or helper theorems merely for uniform style.

## Observed boundaries: locate the cause before calling it a kernel defect

| Original form | Observation | Checked route | Evidence |
| --- | --- | --- | --- |
| `y^2+1!=0`; `a>=0,b>0 ⇒ a+b!=0` | Positivity checks directly, while the nonzero query misses. Stating `0<y^2+1` or `a+b>0` first succeeds. | Keep one positivity bridge. The general positive-to-nonzero implication already works; the internal cause is undetermined. | [Part 131](part-131-textbook-positive-to-nonzero.md) |
| `a>1, x<y ⇒ log(a,x)<log(a,y)`, with positive arguments/base | The `a>1` spelling misses; equivalent `1<a` passes. Cause unknown. | Prove `1<a` locally in the claim, preserving the original premise, then check the target. | [Part 93](part-93-textbook-log-interfaces.md) |
| `sqrt(u)<=r`, with `u>=0, r>=0, u<=r^2` | The mixed root/scalar target misses directly. | Use `sqrt(u)<=sqrt(r^2)=r` with the nonnegative bridges actually needed. | [Part 35](part-35-square-root-bounds.md), [Part 92](part-92-textbook-am-gm-root-chain.md) |
| `tan(x+1*pi)=tan(x+pi)`, with the source cosine-nonzero conditions | Direct transport with the original argument spelling misses. | Prove `x+1*pi=x+pi` first; retain both original tangent results. | [Part 95](part-95-textbook-trig-periods.md) |
| `identity_on_range(identity(x))=x` | The original chain passes; the bare endpoint and global value/range prepublication still miss. | Publish only local `identity(x)=x` in the claim, with no repeated goal. | [Part 97](part-97-nested-identity-range.md) |
| Squared endpoint of a named secant | The bare endpoint misses; an earlier forall equality does not repair it. | Use local `secant(x)=1/cos(x)`, then the squared equality chain. | [Part 94](part-94-textbook-trig-consumers.md) |

With known coordinate values, the two scalar sums check but the corresponding
tuple equality initially missed; see [Part 99](part-99-plane-vector-projection-tuples.md).
Round 80 showed the native `tuple_equal_from_coordinates` theorem proves that
same tuple equality and composes with the original addition unfolding chain;
four coordinate publications are unnecessary. The source `kernel_problem`
entry now records only a direct-consumption observation, not a missing explicit
proof route. The internal cause remains unknown; no new builtin was added.

A missed direct query is not mathematical falsity. A working bridge does not
establish internal correctness or become a permanent authoring obligation.
A builtin candidate needs its trigger, guards, subgoals, and negatives stated
separately. This overview authorizes no kernel, AST, or Env changes.

## Pending checks and case navigation

Round 58 completed a fresh build and 14 strict file replays; see
[Part 98](part-98-function-parity-zero.md). Evenness and zero equations can be
direct; isolated oddness uses the checked local value bridge. Five round-47
cold-file timeouts remain unknown, not rejected or accepted.
Find maintained cases through [the mathematical index](parts-index.md).
Update source acceptance first, then the overview, keeping old failures,
implementation choices, and new-binary support separate.
