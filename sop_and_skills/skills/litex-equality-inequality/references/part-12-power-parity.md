# Part 12 — Integer-power parity signs

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

Even natural powers of a real are nonnegative. A negative real raised to an
odd positive natural power remains negative. Anchor: Manual R15 parity proofs.

## Positive

```litex
claim:
    ? forall x R, n N:
        x^(2*n) >= 0
    x^(2*n) = (x^n)^2 >= 0
claim:
    ? forall x R, n N:
        x < 0
        =>:
            x^(2*n+1) < 0
    x != 0
    x^n != 0
    x^(2*n+1) = x^(2*n)*x^1 = x^(2*n)*x = (x^n)^2*x < (x^n)^2*0 = 0
```
Both pass. Both direct universal targets without these bodies miss.

## Negative and domain boundary

Changing the odd negative conclusion to >0 rejects; x=-1,n=0 refutes it.
Treating 2*t as even for arbitrary real t is invalid: x=-1,t=1/4 gives an
unsupported real square-root domain. That probe rejects, but is a WD/domain
control rather than a false well-defined comparison.
Litex's 0^0 convention makes the even natural n=0 case valid. Negative integer
exponents require nonzero bases; that broader parity rule is not tested here.

## Candidate

A parity-sign leaf can recognize certified even/odd integer exponent shapes,
check exponent domain and base sign, and assemble power-law/square evidence.
Do not infer parity merely from multiplication by 2 on arbitrary real input,
nor use a special symbolic spelling instead of actual integer-domain evidence.

## Evidence

[Round 4 receipt](evidence/round-04-2026-10-08.summary.json), `even-*`, `odd-*`;
current working-tree release, strict fresh files on 2026-10-08.
No capability implementation or whole-source cleanup.
