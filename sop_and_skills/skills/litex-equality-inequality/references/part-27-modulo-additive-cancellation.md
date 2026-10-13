# Part 27 — Modulo periodicity and common additive cancellation

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

Adding an integer multiple of m preserves remainder. Congruence survives
subtracting the same integer, so a common additive shift can be cancelled.
Anchors: number-theory Euclidean decomposition and existing modulo congruence.

## Positive

```litex
claim:
    ? forall a,k Z,m N+:
        (a+k*m)%m = a%m
    (k*m)%m = 0
    a%m+0 = a%m
    (a+k*m)%m = (a%m+(k*m)%m)%m = (a%m+0)%m = (a%m)%m = a%m
```
Passes; direct periodicity misses.

```litex
claim:
    ? forall a,b,k Z,m N+:
        (a+k)%m = (b+k)%m
        =>:
            a%m = b%m
    a = (a+k)-k
    b = (b+k)-k
    ((a+k)-k)%m = ((b+k)-k)%m
    a%m = ((a+k)-k)%m = ((b+k)-k)%m = b%m
```
Passes; direct cancellation misses. Omitting the explicit dividend equalities
makes the original chain fail at its first equality under modulo, rather than
at the two-operand congruence step. These are observed phases, not a complete
diagnosis of generic rewrite permissions.

## Negatives and candidates

Different offsets cannot cancel: a=0,b=1,k=1,h=0,m=3 makes
(a+k)%m=(b+h)%m but not a%m=b%m; the direct variant rejects.
Multiplicative cancellation without coprimeness is false: a=0,b=2,k=2,m=4;
that control also rejects. Do not infer multiplicative cancellation from the
checked additive case.

Fixed periodicity can match the integer-multiple expression and preserve
modulo WD. Additive cancellation needs bounded stored-relation matching,
because the eliminated k is not in the target. Arithmetic congruence under
modulo may remove current dividend-identity bridges; audit that existing
consumer rather than expanding global rewrite/search permission.

## Evidence

[Round 8 receipt](evidence/round-08-2026-10-08.summary.json), `mod-linear-shift-*`,
valid `mod-common-add-*`, `mod-product-cancel-false`.
Current-source release, strict fresh files, 2026-10-08. Incorrect generated
goal variants are excluded and have no runnable retained case files.
