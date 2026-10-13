# Part 15 — Strict absolute-value and interval bounds

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

For real x,r, -r<x<r is equivalent to abs(x)<r. The weak equivalence is a
different supported surface; never infer strictness from weak endpoint facts.
Anchors: Manual R10 and Analysis epsilon-neighborhood estimates.

## Positive explicit routes

```litex
claim:
    ? forall x,r R:
        -r < x
        x < r
        =>:
            abs(x) < r
    0 <= x or x < 0
    by cases:
        ? abs(x) < r
        case 0 <= x:
            abs(x) = x < r
        case x < 0:
            x <= 0
            0-x = -r+(r-x) < x+(r-x) = r
            abs(x) = 0-x < r
claim:
    ? forall x,r R:
        abs(x) < r
        =>:
            -r < x
            x < r
    x <= abs(x) < r
    0-x <= abs(0-x) = abs(x-0) = abs(x) < r
    -r = (0-x)+(x-r) < r+(x-r) = x
```
Both pass. This is a reduced scalar capability probe, not a chapter replacement.

## Ideal forms and negatives

Direct abs(x)<r from either interval endpoints or x<r,0-x<r misses.
Direct projection of abs(x)<r to either -r<x or x<r also misses.
The weak interval-to-abs(x)<=r direct route passes: do not duplicate it.

Weak endpoints cannot give a strict result (x=r=1); only x<r is insufficient
(x=-2,r=1). Both controls reject. An extra r>0 premise is not mathematically
necessary: either consistent strict premise package already forces r>0.

## Candidate

Add a strict symmetric-bound leaf and strict absolute-bound projections,
preserving the actual strict comparisons as proof evidence. Reuse supported
real sign/interval mechanisms and bounded orientation normalization; no case
search is mathematically needed for this fixed equivalence. Do not convert
weak input to strict output or require authors to supply redundant radius signs.

## Evidence

[Round 5 receipt](evidence/round-05-2026-10-08.summary.json), `abs-*` cases.
Release built successfully from working tree on 2026-10-08; independent strict
files, exact source and output retained. No implementation or canonical edits.
