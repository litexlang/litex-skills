# Part 8 — Bound a difference of products

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

Expand u*v-x*y as u*(v-y)+y*(u-x), then apply triangle inequality and the
absolute-value product identity. Anchors: Analysis Chapter 6 product limit
around lines 862–865, Chapter 9 product limit around lines 3848–3861.

## Positive

```litex
forall u,v,x,y R:
    abs(u*v-x*y) = abs(u*(v-y)+y*(u-x)) <= abs(u*(v-y))+abs(y*(u-x)) = abs(u)*abs(v-y)+abs(y)*abs(u-x)
```
This chain passes. Chapter 9 prints the decomposition and each transported
bound separately. Replacing the actual chapter block and checking consumers
is pending; this is a reduced scalar capability demonstration.

## Ideal direct form and negative

```litex
forall u,v,x,y R:
    abs(u*v-x*y) <= abs(u)*abs(v-y)+abs(y)*abs(u-x)
```
Direct target misses. The false shortcut omitting the second error term also
rejects; u=0,x=1,v=y=1 makes its left side 1 and right side 0.

## Candidate

A fixed product-difference estimate leaf can recognize the displayed RHS,
check real WD, and return the decomposition/triangle/product-abs evidence.
Alternatively expose a checked mathematical interface if maintainers prefer
explicit invocation. Repetition justifies considering it, not unbounded
search for optimal error decompositions. Do not silently assert epsilon bounds
or choose product bounds/radii for the author. Symmetric decompositions are
separate matching cases; they were not tested here.

## Evidence

[Round 3 receipt](evidence/round-03-2026-10-08.summary.json), `product-error-*`.
Current working-tree release built successfully on 2026-10-08, strict clean
files. No canonical source rewrites or kernel changes.
