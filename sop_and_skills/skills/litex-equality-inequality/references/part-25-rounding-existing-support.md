# Part 25 — Existing rounding and remainder support

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and checked positives

Concrete Mathematics Chapter 3 expands several native identities into bound
and theorem calls. These self-contained direct forms already pass:
```litex
forall x R:
    floor(-x) = -ceil(x)
    ceil(-x) = -floor(x)
forall x R,n Z:
    floor(x+n) = floor(x)+n
    ceil(x+n) = ceil(x)+n
forall x,y R:
    x <= y
    =>:
        floor(x) <= floor(y)
        ceil(x) <= ceil(y)
forall a,b Z:
    a < b
    =>:
        a+1 <= b
forall a Z,d N+:
    0 <= a%d
    a%d < d
```
Individual family probes were run in fresh files. No whole-chapter proof
replacement or consumer check was performed; source-facing theorems and
pedagogical proofs may still be intentionally retained.

## Negatives

Floor translation by arbitrary real n is false: x=0,n=1/2.
Strict order need not survive rounding: x=0.1,y=0.2.
An arbitrary real gap need not be at least one: a=0,b=1/2.
A remainder need not be positive: a=0,d=1.
The positive-divisor bound cannot be reused as a%d<d for negative d.
All corresponding negative variants reject. Modulo accepts nonzero integer
divisors, while the tested interval bound specifically assumes positive d.

## Improvement status

Do not add duplicate rules for the identities above. Prefer direct reuse in
authoring, preserving declarations and source meaning. Alternate translated
rounding bounds x-1<floor(x) and ceil(x)<x+1 currently miss directly, but
two-line definition/translation routes pass; bounded alternate-shape support
is a secondary proposal, not proof of missing defining floor/ceil bounds.

## Evidence

[Round 7 receipt](evidence/round-07-2026-10-08.summary.json), direct negation/shift/
monotonicity, `integer-gap-*`, `mod-remainder-*`, and outer-unit-bound cases.
Successful working-tree release build, strict fresh files, 2026-10-08.
