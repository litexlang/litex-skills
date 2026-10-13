# Search round 9 — Finite aggregates and callback domains

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


Successful current working-tree release build, 2026-10-08; 41 independent
strict file probes. No kernel or canonical mathematical source edits.

## Recommended improvements

1. Interval-sum triangle sibling: finite-set triangle is native and passes;
   the valid Z-domain range triangle misses. A complete exact-interval-domain
   range-to-finite route passes, while wider-domain/anonymous callback adapters
   still fail. Inspect precise callback/domain matching rather than redoing
   induction in every source. [Part 30](part-30-range-sum-callbacks.md).
2. Finite-product comparison interface: arbitrary finite-set pointwise order
   with nonnegative factors misses directly. Two-factor explicit nonnegative/
   order proofs pass, and unsigned product-order controls reject. Consider a
   native explicit interface analogous to the existing sum comparison API;
   general certificate/runtime support is still to implement and verify.
   [Part 31](part-31-finite-product-order.md).

Positive-index scalar distribution also exposes an earlier WD/index-carrier
boundary: Z-domain callbacks pass, N+-domain direct goal misses, and the
attempted interval adapter fails at proving the fresh index in N+. This needs
producer/consumer investigation, not another scalar truth rule that bypasses
callback WD. Invalid N+-callback sum starting at zero rejects.

## Reuse existing support

Finite/range pointwise sum comparisons and summand<=total have checked
one-call native interfaces. Constant sums work in size(S)*M orientation;
that orientation plus the existing comparison call closes nonnegative totals
and uniform upper bounds. Do not restore implicit quantified search simply
because the bare goal misses. [Part 29](part-29-sum-interface-reuse.md).

Pointwise function equality closes finite-product equality using only
by fn_extension f=g; removing the repeated product goal was checked.
Empty product remains one and finite-set triangle already passes.

## Coverage and next work

Anchors: Analysis Chapter 7 finite_series_triangle/scalar-positive-range
trusts and finite-set monotonicity; native sum/summand/triangle examples and
aggregate constant/product identities. Reduced probes do not establish trust
removal or enclosing-chapter acceptance. The exact-domain triangle control is
a different interface from the original Z-domain statement.

Next: focus on the remaining named-callback/anonymous-callback and positive
index WD consumers with small independent controls; then audit recurring
set-size/extremum inequalities in combinatorial examples. Preserve working-tree
changes and do not turn a failed adapter into permanent source boilerplate.

Evidence: [receipt](evidence/round-09-2026-10-08.summary.json),
[build log](../../../references/sources.md#unbundled-local-material). Thirty-one dated skill parts exist.
