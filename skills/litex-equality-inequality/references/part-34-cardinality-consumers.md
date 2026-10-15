# Part 34 — Cardinality consumers and existing extrema support

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and tested support

Finite-set subset monotonicity, strict proper-subset size, and subset plus
equal size implying equal sets all pass directly. Arbitrary equal size does
not imply equal sets ({1} and {2}); that variant rejects. Subset alone cannot
give strict size (A=B={1}); that control rejects.

For finite nonempty real S, pointwise x<=M directly gives max(S)<=M,
and pointwise M<=x directly gives M<=min(S). Both pass; missing pointwise
max bound and empty max controls reject. Do not duplicate these native routes.

## Constructor consumer boundary

Direct size(intersect(A,B))<=size(A), size(A\B)<=size(A), and
size(A)<=size(union(A,B)) miss with A,B declared finite.
Finiteness is the first demonstrated WD boundary. After it is supplied,
intersection/difference comparisons still miss until their subset is also
published. This complete guarded control passes:
```litex
forall A,B finite_set:
    $is_finite_set(intersect(A,B))
    intersect(A,B) $subset A
    =>:
        finite_set_size(intersect(A,B)) <= finite_set_size(A)
```
Analogous difference/union-lower controls pass. These are redundant-premise
positive controls, not migrations of original theorem interfaces.
The direct union upper size bound also misses, but supplying only union
finiteness makes it pass; its dedicated comparison rule already exists.

## Improvement candidates

First enable sound reuse of existing constructor finiteness in WD. Then audit
cardinality subset-bound consumption for exact native constructor inclusions,
under bounded structural permissions, instead of adding one special size rule
per constructor or unrestricted subset search. Preserve inequality conditions
and fact/evidence owners; no new Env state is justified by these probes alone.

## Evidence

[Round 10 receipt](evidence/round-10-2026-10-08.summary.json), size and extrema cases.
Strict independent files, current working-tree release built 2026-10-08.
No canonical combinatorial proof shortening or kernel implementation.
