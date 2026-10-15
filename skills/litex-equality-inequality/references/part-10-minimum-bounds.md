# Part 10 — Nested minimum radii and bounds

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

A minimum of positive radii remains positive and lies below every operand.
Anchor: Analysis Chapters 9/10 nested minimum radius estimates and their
existing local trusts. These reduced probes do not verify removal of chapter trust.

## Positive and ideal form

```litex
have a,b,c R+
have first R+ = min(a,b)
have delta R+ = min(first,c)
```
Passes. The ideal direct binding fails:
```litex
have a,b,c R+
have delta R+ = min(min(a,b),c)
```
The finite_set_min(union(singletons)) counterparts reproduce this distinction.
For arbitrary real a,b,c, this endpoint chain passes:
```litex
forall a,b,c R:
    min(min(a,b),c) <= min(a,b) <= a
```
The direct goal min(min(a,b),c)<=a misses. Immediate child bounds
min(min(a,b),c)<=min(a,b) and <=c pass.

## Strict lower bound and negative controls

x<a and x<b imply x<min(a,b). Direct target misses; an explicit case proof
passes only after the a>b case publishes b<=a before selecting min(a,b)=b.
Full positive and failed shorter cases are in the receipt.
The isolated equality b=min(a,b) passes from b<=a but misses from a>b.
This is a guard-consumption difference, not different mathematics.

With only x<a, x<min(a,b) is false (x=0,a=1,b=-1), and rejects.
Weak bounds cannot imply a strict bound (x=a=b=0); that variant rejects.
Nonnegative operands cannot supply positive minimum membership (a=b=0);
the corresponding direct R+ control rejects.

## Improvement candidates

Prefer structural positive-member checks descending through nested min over
a three-operand special case. For a nested minimum upper bound, inspect its
children under bounded structural descent; retain exact evidence for the
selected path. Alternatively a fixed strict lower-bound leaf checks both
x<a and x<b. Audit strict-to-weak guard consumption separately before adding
duplicate min-selection rules. No global search-depth expansion is implied.

## Evidence

[Round 4 receipt](evidence/round-04-2026-10-08.summary.json), `nested-*` and `min-*`.
Current working-tree release built on 2026-10-08; strict independent files.
No canonical module cleanup, trust removal or new kernel behavior claimed.
