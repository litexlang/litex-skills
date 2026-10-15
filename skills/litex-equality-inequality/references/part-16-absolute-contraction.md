# Part 16 — Absolute value is nonexpansive

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

The two reverse-triangle inequalities combine into
abs(abs(x)-abs(y))<=abs(x-y). Anchor: Analysis Chapter 9
`absolute_value_continuous`, around lines 6351–6358.

## Positive

```litex
claim:
    ? forall x,y R:
        abs(abs(x)-abs(y)) <= abs(x-y)
    abs(x)-abs(y) <= abs(x-y)
    abs(y)-abs(x) <= abs(y-x) = abs(x-y)
    0-(abs(x)-abs(y)) = abs(y)-abs(x) <= abs(x-y)
    abs(abs(x)-abs(y)) <= abs(x-y)
```
Passes. The source chapter separately publishes both directions and negation
transport. Its complete caller has not been rewritten or checked by this probe.

## Ideal form and negative

```litex
forall x,y R:
    abs(abs(x)-abs(y)) <= abs(x-y)
```
Direct target misses. The reversed inequality is false and rejects:
x=1,y=-1 gives 2<=0.

## Candidate

A fixed absolute-contraction leaf can return the two reverse-triangle
certificates and their symmetric-bound combination under real WD. This is
one general metric estimate rather than a special continuity theorem.
Do not weaken it to magnitude equality or discover arbitrary centers.

## Evidence

[Round 5 receipt](evidence/round-05-2026-10-08.summary.json), `reverse-triangle-*`.
Current working-tree release built on 2026-10-08, strict fresh files.
