# Part 29 — Reuse sum interfaces instead of redoing induction

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

Pointwise real bounds over a finite index set give a bound on totals. Existing
native theorem calls provide this route; a background search miss does not
justify rebuilding induction or silently widening search.
Anchor: Analysis Chapter 7 `finite_set_sum_monotone`, finite-series comparison.

## Positive

```litex
claim:
    ? forall S finite_set,f,g fn(x S) R:
        forall x S:
            f(x) <= g(x)
        =>:
            finite_set_sum(S,f) <= finite_set_sum(S,g)
    release thm finite_set_sum_le_from_pointwise(finite_set_sum(S,f),finite_set_sum(S,g))
```
Passes; bare total comparison misses. The corresponding interval call
sum_le_sum_from_pointwise also passes with complete pointwise bounds on the
range; no new rule needed to make these authoring routes concise.

## Constant-sum orientation and estimates

```litex
forall S finite_set,M R:
    finite_set_sum(S,fn(x S) R {M}) = finite_set_size(S)*M
forall S finite_set:
    finite_set_sum(S,fn(x S) R {0}) = finite_set_size(S)*0 = 0
```
Both independently checked forms pass. Starting with sum_const=M*size misses
while the size*M orientation passes; a zero total without its size*0 bridge
also misses. This is current matching behavior, not a mathematical restriction.

These constant chains plus the existing comparison call verify a nonnegative
total and the uniform upper bound sum f<=size(S)*M. Both direct endpoints
miss. The canonical interface routes in the receipt pass without trust.
Likewise the existing finite_set_summand_le_sum call closes a summand bound
under pointwise nonnegative terms; the bare summand comparison misses.

## Negatives and boundary

One pointwise bound is not a bound on the entire two-element sum: f=(0,2),
g=(0,0) refutes the missing-second-bound variant, which rejects.
A summand may exceed the total with negative other terms: f=(1,-1); that
variant rejects. Empty sum is zero, so positivity without nonemptiness fails;
the explicit empty positive-total control rejects.

Prefer the existing one-call APIs here; do not characterize them as missing
mathematics. Automatic reuse of quantified premises would be a separate
policy/performance choice, not a mandatory kernel repair from these misses.

## Evidence

[Round 9 receipt](evidence/round-09-2026-10-08.summary.json), finite/range pointwise,
constant/nonnegative/uniform/summand cases. Current working-tree release,
strict fresh files on 2026-10-08. No canonical chapter cleanup.
