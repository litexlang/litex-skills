# Part 36 — Rationalize a square-root difference

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

Difference of squares gives a useful exact error identity. Radicands must be
nonnegative and the sum of roots nonzero. This is a reduced scalar pattern
for root/distance error estimates, not an executed calculus caller rewrite.

## Positive

```litex
claim:
    ? forall x,y R:
        0 <= x
        0 <= y
        sqrt(x)+sqrt(y) != 0
        =>:
            sqrt(x)-sqrt(y) = (x-y)/(sqrt(x)+sqrt(y))
    sqrt(x)^2 = x
    sqrt(y)^2 = y
    (sqrt(x)-sqrt(y))*(sqrt(x)+sqrt(y)) = sqrt(x)^2-sqrt(y)^2 = x-y
    sqrt(x)-sqrt(y) = ((sqrt(x)-sqrt(y))*(sqrt(x)+sqrt(y)))/(sqrt(x)+sqrt(y)) = (x-y)/(sqrt(x)+sqrt(y))
```
Passes. Direct formula with the identical premises misses.

## Negative and candidate

Without a denominator guard, x=y=0 makes the formula undefined; that variant
rejects. The nonnegative radicand conditions do not exclude this degenerate
case. A negative radicand also fails WD in the separate root control.

A fixed root-difference identity rule could reuse principal-square and
nonzero-denominator evidence, preserving the exact equality and domain.
Whole-fact WD must remain mandatory; do not cancel a zero root sum or restore
unguarded division through a convenience rewrite.

## Evidence

[Round 11 receipt](evidence/round-11-2026-10-08.summary.json), `sqrt-difference-*`.
Current working-tree release built on 2026-10-08; strict fresh files, no kernel
implementation or canonical source replacement.
