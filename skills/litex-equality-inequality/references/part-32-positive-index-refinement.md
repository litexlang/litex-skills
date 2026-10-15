# Part 32 — Integer index refinement and callback preflight

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

An integer at least a positive integer is positive. This is relevant to
calling an N+-domain function on a range index, including the aggregate
pointwise helper's fresh Z-index with lower/upper assumptions.
Anchor: Analysis Chapter 7 positive-range scalar aggregate and
`aggregate_pointwise_proof` in search_equal_fact_by_aggregate_identities.rs.

## Positive and direct gap

```litex
claim:
    ? forall m N+,range_index Z:
        m <= range_index
        =>:
            range_index $in N+
    0 < m <= range_index
```
Passes. Direct membership from the same premises misses; even explicit
0<lower and lower<=range_index with both integers misses direct N+ membership.
Ordinary real positivity propagation lower in R+,lower<=x implies 0<x
already passes directly. Do not add a duplicate real sign-propagation rule.

## Earlier WD boundary

```litex
forall m N+,range_index Z,f fn(x N+) R:
    m <= range_index
    =>:
        f(range_index) $in R
```
Fails WD at range_index in N+. Putting a membership proof inside a claim
body does not repair this preflight: the call-containing goal is checked first.
An explicitly supplied membership premise or a declared N+ index makes the
call pass. Those are positive controls, not repaired versions of the original
Z-index interface. Do not weaken source theorem parameters to hide the gap.

## Negatives and candidate

Replacing m in N+ by m in N is false at m=range_index=0; probe rejects.
Calling an N+-only function at zero is invalid and rejects.

Consider a bounded positive-integer refinement proof available to WD, consuming
integer type plus a checked positive lower bound/order relation. Reuse known
real positivity instead of expanding global search depth. The aggregate helper
constructs a fresh Z-index and stores start<=index<=end; confirm its consumer
can use the refinement certificate before applying N+-domain callbacks.
No full producer/consumer repair or current aggregate acceptance is claimed.

## Evidence

[Round 10 receipt](evidence/round-10-2026-10-08.summary.json), positive lower/index/
call cases. Strict fresh files, working-tree release built on 2026-10-08.
Discarded generated binder i was reserved; corrected range_index tests, not
that parse error, establish capability results.
