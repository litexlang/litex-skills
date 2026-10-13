# Part 37 — Root of a nonnegative sum

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

For nonnegative real x,y, sqrt(x+y)<=sqrt(x)+sqrt(y). Squaring the right
side adds a nonnegative cross term. This is a general scalar bound related
to geometry norm/triangle estimates, not a substitute for noncollinearity.

## Checked route and ideal form

The full `sqrt-sum-bound-expanded-route` case passes after publishing root
nonnegativity, their squares, the cross-term sign, and a staged expansion of
(sqrt(x)+sqrt(y))^2. The final root-monotone chain closes the target.
The first shorter expansion attempt failed at an equality, before its order
step; preserve that phase rather than calling the whole issue a sign rule miss.

The direct target misses:
```litex
forall x,y R:
    0 <= x
    0 <= y
    =>:
        sqrt(x+y) <= sqrt(x)+sqrt(y)
```
Exact positive source and intermediate failed attempt are in the receipt.

## Negative and candidate

Equality is false at x=y=1; its universal variant rejects. Root-of-sum is not
distributive. Negative radicands have no real-root WD.

Consider a fixed root-subadditivity leaf or checked mathematical interface
to avoid repeating this square expansion. Do not promote it to a strict
triangle theorem or automatically discover arbitrary root estimates. Existing
root product and monotonicity laws already work; this is a composed bound.

## Evidence

[Round 11 receipt](evidence/round-11-2026-10-08.summary.json), `sqrt-sum-*`.
Successful working-tree release build, strict independent files, 2026-10-08.
No enclosing geometry theorem edits or performance claims.
