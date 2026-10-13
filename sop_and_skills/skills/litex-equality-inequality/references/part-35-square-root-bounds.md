# Part 35 — Mixed square-root bounds and order reflection

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

Square-root monotonicity converts squared bounds into mixed root/scalar
bounds. Direction matters: an upper radius must be nonnegative; a lower
candidate can have either sign. Anchor: geometry distance/dot comparisons.

## Checked positives

```litex
claim:
    ? forall x,r R:
        0 <= x
        0 <= r
        x <= r^2
        =>:
            sqrt(x) <= r
    0 <= r^2
    sqrt(x) <= sqrt(r^2) = r
claim:
    ? forall x,r R:
        0 <= x
        r^2 <= x
        =>:
            r <= sqrt(x)
    0 <= r^2
    r <= abs(r) = sqrt(r^2) <= sqrt(x)
```
Both pass; both bare conclusions miss. The strict versions also pass with
strict squared bounds; upper strict form needs only r>=0, not the stronger
r>0 premise. Lower strict form does not require a sign assumption on r.
All corresponding direct variants miss in independent files.

Root order reflection sqrt(x)<=sqrt(y) implies x<=y for nonnegative inputs
misses directly, but nonnegative-root facts and
x=sqrt(x)^2<=sqrt(y)^2=y pass. Full source is in the receipt.

## Negatives and existing support

Omitting the upper radius sign is false: x=1,r=-1 refutes the weak upper
bound; x=1,r=-2 refutes the strict one. Both reject.
Weak input cannot give strict root order: x=y=1; control rejects.
Negative radicand is invalid and rejects. Ordinary weak/strict root monotonicity,
sqrt(x*y)=sqrt(x)*sqrt(y) for nonnegative inputs, and sqrt(x^2)=abs(x)
already pass directly. Do not duplicate them or infer sqrt(x^2)=x on signed x.

## Candidate

Add mixed root/scalar comparison and root-order reflection siblings with
direction-specific sign guards and radicand WD. Reuse native principal-root
and monotonicity evidence; no intermediate root expression should need to be
invented by the author. Positive controls are not a full geometry migration.

## Evidence

[Round 11 receipt](evidence/round-11-2026-10-08.summary.json), root upper/lower,
reflection/monotonicity/product/magnitude controls. Working-tree release,
strict independent files on 2026-10-08.
