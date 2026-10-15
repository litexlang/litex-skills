# Part 28 — Existing modulo/gcd support versus cancellation debt

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Checked existing support

Native add/subtract/multiply congruence, distributing those operations over
residues, Euclidean remainder uniqueness, nested integer-multiple moduli,
positive-divisor gcd Euclidean step, and positive common-divisor gcd lower
bound all pass directly in this round.

Representative independently checked forms:
```litex
forall a,b,c,d Z,m N+:
    a%m = b%m
    c%m = d%m
    =>:
        (a+c)%m = (b+d)%m
        (a-c)%m = (b-d)%m
        (a*c)%m = (b*d)%m
forall a,q Z,m N+,r N:
    a = m*q+r
    r < m
    =>:
        a%m = r
```
These source forms combine the individually checked family statements;
full original probes and commands are in the receipt. No canonical chapter
cleanup or downstream consumer validation was executed.

## Negatives

Allowing negative r in remainder uniqueness is false: a=-1,q=0,r=-1,m=3.
Arbitrary nested moduli do not reduce: a=3,n=2,m=3 gives (a%n)%m=1 versus
a%m=0. Both controls reject.

## Coprime cancellation boundary

The direct implication gcd(k,m)=1 and (a*k)%m=(b*k)%m implies a%m=b%m
misses. A separate explicit-witness variant with integers u,v and
k*u+m*v=1 has a checked complete proof (`mod-bezout-cancel-chain`).
That is not a solution of the original gcd-only target: production of the
Bezout witnesses was not verified in this round. Use/complete a mathematical
interface that supplies them before presenting this as a ready local bt fix.
Do not add unproved witnesses or trust merely to label cancellation supported.

## Signed gcd observation

gcd(a,b)=gcd(b,a%b) with b in N+ passes. The broader b!=0 goal using
a%abs(b) misses. No explicit signed-normalization route was accepted here;
retain it as a scoped coverage observation, not proof that gcd Euclid is absent.

## Evidence

[Round 8 receipt](evidence/round-08-2026-10-08.summary.json), congruence/distribution,
remainder/nesting, gcd and coprime cases. Successful working-tree release
build, 2026-10-08; no kernel or canonical source edits.
