# Part 11 — Reflect order from a general-base logarithm

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

For a>1, log(a,.) is increasing on positive reals; it reflects weak order.
Anchor: Analysis Chapter 6 real-power monotonicity, using base-2 comparisons.

## Positive

```litex
claim:
    ? forall a,x,y R+:
        1 < a
        log(a,x) <= log(a,y)
        =>:
            x <= y
    by contra:
        ? x <= y
        y < x
        log(a,y) < log(a,x)
        impossible log(a,x) <= log(a,y)
```
Passes. Removing the proof body and stating the universal conclusion directly
misses. This does not make reflection mathematically unsupported.

## Existing support and negatives

ln(x)<=ln(y) directly implies x<=y in the probe. For 0<a<1, x<y directly
implies log(a,x)>log(a,y). Do not recommend duplicate rules for those routes.
The incorrect small-base increasing direction rejects; a=1/2,x=1,y=2
gives log(a,x)=0 and log(a,y)=-1.
The general-base reflection proposal is specifically guarded by a>1;
a=1 is outside logarithm WD and smaller valid bases reverse direction.

## Candidate

Add bounded general-base reflection from a stored logarithmic comparison,
preserving positive argument/base WD and the base's side of 1. The target
x<=y does not supply a, so reuse bounded visible relation matching rather
than search all possible bases. Existing ln reflection is a nearby mechanism,
not evidence that every log base is automatically handled.

## Evidence

[Round 4 receipt](evidence/round-04-2026-10-08.summary.json), `log-*`,
`ln-order-reflection-direct`; successful working-tree release build,
2026-10-08. Strict clean files; no kernel changes.
