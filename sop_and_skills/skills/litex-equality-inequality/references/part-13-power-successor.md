# Part 13 — Increase or decrease an integer exponent by one

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

For positive a and integer n, a^(n+1)=a^n*a. Multiplying by a>1 increases
strictly; multiplying by 0<a<1 decreases strictly. Anchor: Manual R15.

## Positive

```litex
claim:
    ? forall a R+, n Z:
        1 < a
        =>:
            a^n < a^(n+1)
    a^(n+1) = a^n*a^1 = a^n*a > a^n*1 = a^n
claim:
    ? forall a R+, n Z:
        a < 1
        =>:
            a^(n+1) < a^n
    a^(n+1) = a^n*a^1 = a^n*a < a^n*1 = a^n
```
Both pass; both direct goals miss. Negative integer exponents are included
by the positive-base domain, not excluded by a hidden n>=0 premise.

## Negative and candidate

Replacing a>1 with a>=1 cannot preserve strict growth: a=1,n=0 refutes it;
the corresponding direct variant rejects. Negative bases have no such
unrestricted direction, and zero cannot supply negative-exponent WD.

A fixed successor-exponent monotonicity rule can consume the base-domain and
side-of-1 conditions. This is narrower than all real-exponent monotonicity;
do not claim arbitrary exponent ordering from these two probes.

## Evidence

[Round 4 receipt](evidence/round-04-2026-10-08.summary.json), `power-step-*`, strict
independent files, release built from working tree on 2026-10-08.
