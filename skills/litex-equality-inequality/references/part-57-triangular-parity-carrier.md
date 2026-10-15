# Part 57 — Consecutive parity and triangular-number carriers

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and actual source

Consecutive integers have even product. For natural n, n*(n+1)/2 is a natural number. Concrete Mathematics chapter02:88–97 defines triangular_coefficient recursively in N and notes the separate divisibility obligation for the quotient form. This round proves the quotient carrier as an independent interface, preserving the source definition.

## Direct misses

```litex
forall n Z:
    (n*(n+1))%2 = 0
```
```litex
forall n N:
    n*(n+1)/2 $in N
```

The integer quotient target also misses. Even explicitly assuming the even-product fact does not solve the integer type target; Part 56 isolates that separate exact-division consumer.

## Positive: a complete two-residue proof

```litex
claim:
    ? forall n Z:
        (n*(n+1))%2 = 0
    have q Z = quot(n,2)
    n = 2*quot(n,2)+n%2 = 2*q+n%2
    n%2 = 0 or n%2 = 1
    by cases:
        ? (n*(n+1))%2 = 0
        case n%2 = 0:
            n = 2*q+n%2 = 2*q
            n*(n+1) = (2*q)*(n+1) = 2*(q*(n+1))
            (n*(n+1))%2 = (2*(q*(n+1)))%2 = 0
        case n%2 = 1:
            n = 2*q+n%2 = 2*q+1
            n+1 = 2*q+1+1 = 2*(q+1)
            n*(n+1) = n*(2*(q+1)) = 2*(n*(q+1))
            (n*(n+1))%2 = (2*(n*(q+1)))%2 = 0
```

Complete residues, native Euclidean quotient and explicit zero-modulo multiplication suffice. Initial attempts failed at shortened n=2*q+n%2 and then n=2*q; the accepted source keeps the Euclidean equality endpoint and each case's remainder on the chain. They are observed current bridges, not permanent source requirements.

## Positive: compose checked interfaces

The retained `triangular-integer-checked-interface` file defines checked parity and exact-integer-quotient theorems, then uses two calls to prove the integer carrier. `triangular-natural-no-echo` proves the natural carrier with those two calls, a numerator-nonnegative fact and a quotient-nonnegative fact. All helper bodies are checkable; no trust or extra source assumption.

Deleting the final repeated natural type statement passes. Deleting the numerator sign statement makes the shorter tested variant miss. This liveness distinction narrows the remaining bridge; do not repeat the type merely to close the claim. Full sources and outputs are in the receipt.

## Negatives

n/2 is not always integral (n=1); the unguarded half theorem rejects. The triangular expression is not always in N+ on all N (n=0); that control rejects. Do not strengthen the input to positive n or change the recursive source definition merely to avoid the zero case. Missing divisibility/nonzero-division controls are in Part 56.

## Improvement candidates

A bounded consecutive-integer parity rule can recognize n*(n+1) (with separately checked equivalent order/shift forms), require integer n and certify zero remainder modulo 2. It should not silently discover arbitrary polynomial congruences or generalized factorial divisibility.

Compose that certificate with the conditional integer-quotient carrier and existing nonnegative arithmetic evidence to type the triangular expression. A checked reusable parity theorem is an acceptable current interface; no triangular-function-name special case or replacement of the source recurrence is recommended. Further N+ bounds require their own positive-input/boundary acceptance.

## Evidence and limits

Dated 2026-10-09. Fresh current-worktree release build succeeded; an immutable binary snapshot was used throughout. [Round 19 receipt](evidence/round-19-2026-10-09.summary.json) retains exact sources, commands, exits, Normal JSON, binary identity, synchronized Session responses and durable replay commands. Runnable sources are in `evidence/round-19-cases/`.

No trust, kernel/canonical mathematical source changes, whole-textbook gate or performance claims. These are source-adjacent scoped observations and rule nominations; source comments are not independent verifier evidence.
