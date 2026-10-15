# Part 30 — Interval sum triangle and callback-domain consumption

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and observed gap

Finite real sums satisfy triangle inequality. The finite-set direct theorem
passes, but the following valid interval version misses:
```litex
forall f fn(x Z) R,m,n Z:
    m <= n
    =>:
        abs(sum(m,n,fn(x Z) R {f(x)})) <= sum(m,n,fn(x Z) R {abs(f(x))})
```
Anchor: Analysis Chapter 7 `finite_series_triangle`, currently containing a
source trust. This probe does not authorize or verify removing that trust.

## Checked nearby route with an exact interval domain

```litex
claim:
    ? forall m,n Z,f fn(x m...n) R:
        m <= n
        =>:
            abs(sum(m,n,f)) <= sum(m,n,fn(x m...n) R {abs(f(x))})
    sum(m,n,f) = finite_set_sum(m...n,f)
    sum(m,n,fn(x m...n) R {abs(f(x))}) = finite_set_sum(m...n,fn(x m...n) R {abs(f(x))})
    abs(sum(m,n,f)) = abs(finite_set_sum(m...n,f)) <= finite_set_sum(m...n,fn(x m...n) R {abs(f(x))}) = sum(m,n,fn(x m...n) R {abs(f(x))})
```
Passes. It is an exact-domain positive control, not a repair of the original
Z-domain interface. Sum/finite-set conversion with unchanged callbacks also
passes; attempted wider-domain callback conversions still fail.

## Source owner and candidate

The finite_sum_triangle matcher requires the bound callback's declared domain
to alpha-match the aggregate set and compares its body with an application of
the exact original function. It does not beta-reduce anonymous source wrappers
in this pure matching helper. These structural observations explain where
to inspect; they do not establish every failed adapter's cause.

Add a bounded interval-sum triangle sibling or repair domain-aware callback
matching, consuming complete interval WD and the precise same summand under
abs. Do not accept a bound callback using a different function: f=1,g=0 on a
singleton range refutes that false variant, which rejects.

## Positive-index scalar observation

Scalar distribution passes for Z-domain callbacks, but the analogous valid
N+-domain formulation misses. Its attempted exact-interval adaptation fails
at WD of x in N+ before the scalar truth rule. Sum starting at 0 with an
N+-only callback also rejects, correctly. Investigate indexed-domain proof
consumption separately from adding another scalar-distribution truth rule;
do not bypass complete callback-domain checks.
No accepted route for the full N+-scalar statement is claimed here.

## Evidence

[Round 9 receipt](evidence/round-09-2026-10-08.summary.json), range triangle/conversion/
scalar cases and the invalid zero-start control. Release built from working
tree on 2026-10-08; strict independent files, no kernel edits.
