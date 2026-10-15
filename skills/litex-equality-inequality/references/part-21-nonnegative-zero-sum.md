# Part 21 — Zero components of a nonnegative sum

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

A sum of nonnegative reals is zero only when every summand is zero.
Squared components are an important geometric instance. Anchors: Manual R12
two-square zero sum, coordinate geometry squared-distance positivity.

## Positive

```litex
claim:
    ? forall a,b R:
        0 <= a
        0 <= b
        a+b = 0
        =>:
            a = 0
            b = 0
    a = (a+b)-b = 0-b <= 0
    b = (a+b)-a = 0-a <= 0
```
Passes. No separate final a=0,b=0 restatements are needed: existing real-order
antisymmetry consumes these bounds with the original nonnegative premises.
The direct universal target with the same premises misses.

For a^2+b^2=0, both zero components already verify directly. For
a^2+b^2+c^2=0, the direct three-component target misses; the receipt's grouped
six-statement proof passes by bounding a^2+b^2 and c^2 above by zero, recovering
those zeros, then consuming the existing square-zero rules.

## Negatives and candidate

Without nonnegative summands, a+b=0 does not imply a=0 (a=1,b=-1); the
corresponding probe rejects. Existing zero-product and real-order
antisymmetry direct routes pass and should not be duplicated.

Prefer a general nonnegative-zero-sum consumer that descends through a saved
sum, proving each child nonnegative and retaining the exact zero-sum evidence,
over separate three-square/four-square special cases. The target omits other
summands, so use bounded visible saved-relation matching rather than arbitrary
sum discovery. Propagating nonnegative evidence is separate from finding an
unknown sum-of-squares representation.

## Evidence

[Round 6 receipt](evidence/round-06-2026-10-08.summary.json), `nonnegative-sum-*`,
`square-sum-zero-*`, `order-antisymmetry-*`, `zero-product-*`.
Current working-tree release, independent strict files, 2026-10-08.
No canonical source trust removal or geometry theorem migration.
