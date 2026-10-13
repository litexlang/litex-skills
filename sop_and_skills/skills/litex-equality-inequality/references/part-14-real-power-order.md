# Part 14 — Compare positive bases under real powers

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

For positive x>y and real q>0, x^q>y^q. Logarithms translate the positive
power law into multiplication by q. Anchor: Analysis Chapter 6
`real_power_base_strict_mono` around line 4559.

## Positive route and ideal form

The self-contained `power-real-base-order-typed` case in the receipt passes:
it explicitly publishes x^q and y^q in R+, then log(2,y)<log(2,x), scales
by q, uses log(2,z^q)=q*log(2,z), and closes a contradiction against reversed
power order. See the receipt for exact source; it is not a theorem call
depending on the chapter environment.

The ideal target is a search miss:
```litex
forall x,y R+, q R:
    q > 0
    x > y
    =>:
        x^q > y^q
```
Shorter explicit attempts failed first at log-order premise consumption;
adding 1<2 and y<x moved the failure into the contra complement. Publishing
the powers' R+ memberships made the complete route pass. These are observed
phase differences, not a full diagnosis of the internal cause.

## Negative and candidate

The same increasing direction with q<0 is false and rejects:
x=2,y=1,q=-1 gives 1/2>1. Positive bases and exponent sign are essential.

A positive-base real-power monotonicity rule could directly consume q>0 and
x>y while preserving WD/evidence, eliminating log and complement scaffolding.
The negative-exponent reversed law and arbitrary real exponent-order law are
separate variants; the latter direct probe misses but was not proved here.
Do not promote an unverified real-exponent recipe.

## Evidence

[Round 4 receipt](evidence/round-04-2026-10-08.summary.json), `power-real-base-order-*`
and `power-real-exponent-order-direct`, strict clean files on 2026-10-08.
Current-source release build succeeded. No native power rule or chapter
consumer migration implemented.
