# Part 49 — Magnitude quotient bounds with separated denominators

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and source

An upper numerator magnitude and positive lower denominator magnitude give a quotient magnitude bound. This is the scalar estimate used in quotient/reciprocal continuity arguments. Analysis chapter06 contains a complete reciprocal error proof; Analysis2 has a total safe-divide definition with a zero branch and a separately unfinished continuity interface.

## Ideal direct form: observed miss

```litex
forall a,b,A R,B R+:
    b != 0
    abs(a) <= A
    abs(b) >= B
    =>:
        abs(a/b) <= A/B
```

A is an arbitrary real bound; abs(a)<=A implies its nonnegativity. Do not add unnecessary numerator nonzero/sign assumptions.

## Positive: multiply before dividing

```litex
claim:
    ? forall a,b,A R,B R+:
        b != 0
        abs(a) <= A
        abs(b) >= B
        =>:
            abs(a/b) <= A/B
    abs(a/b) >= 0
    abs(a/b)*B <= abs(a/b)*abs(b) = abs((a/b)*b) = abs(a) <= A
    abs(a/b) = (abs(a/b)*B)/B <= A/B
```

This exact-premise route repaired the direct miss in the same Session. It uses existing product absolute value and positive-denominator comparison; no unsupported quotient-absolute identity is assumed.

## Reciprocal source route

The isolated original source theorem passes. A shortened six-statement multiply-first body also passes:

```litex
claim:
    ? forall x,y R,c,epsilon R+:
        x != 0
        y != 0
        abs(x) >= c
        abs(y) >= c
        abs(x-y) <= c^2*epsilon
        =>:
            abs(1/x-1/y) <= epsilon
    abs(x*y) = abs(x)*abs(y) >= c*abs(y) >= c*c = c^2
    (1/x-1/y)*(x*y) = y-x
    abs(y-x) = abs(x-y)
    abs(1/x-1/y)*c^2 <= abs(1/x-1/y)*abs(x*y) = abs((1/x-1/y)*(x*y)) = abs(x-y) <= c^2*epsilon
    c^2 > 0
    abs(1/x-1/y) <= (c^2*epsilon)/c^2 = epsilon
```

Direct reciprocal error bound misses. Product magnitude lower bound abs(x*y)>=c^2 misses directly but its one-chain form passes. Reciprocal rational identity passes; the absolute reciprocal identity misses again, confirming earlier Part 9 observations rather than nominating a duplicate absolute-quotient rule.

## Safe-divide semantics already supported

Exact source definition checks both nonzero and zero branches; no new rule is needed for those branch equalities. `real_safe_divide(a,0)!=0` rejects. Never replace this total function by ordinary a/b at b=0. Scalar estimates do not solve Analysis2's cited continuity debt about codomain restriction to the nonzero subspace.

## Negatives

Negative B can make A/B negative while abs(a/b) is positive; the B!=0-only control rejects. Dropping denominator separation breaks reciprocal estimates: x=1/10,y=1/5,c=1,epsilon=1/10 satisfies the distance premise but gives reciprocal difference 5. Strict reciprocal bound cannot follow from weak input: x=1,y=-1,c=1,epsilon=2 gives equality. All controls reject.

## Improvement candidate

For abs(a/b)<=A/B, recognize a well-defined real quotient and verify B>0, abs(a)<=A and abs(b)>=B, preserving the nonzero denominator evidence. Assemble the bounded product/positive-division proof with exact certificates instead of searching intermediate fractions. This nomination is distinct from Part 9's equality abs(a/b)=abs(a)/abs(b) and Part 45's scalar quotient bound; implementing one does not prove all others or WD consumers.

Prefer the already named reciprocal lemma at textbook callers; no reciprocal-only/function-name special case is recommended. Product lower-bound composition may reuse existing guarded multiplication interfaces after independent ownership diagnosis.

## Evidence and limits

Date: 2026-10-08. Current-worktree release build succeeded. [Round 16 receipt](evidence/round-16-2026-10-08.summary.json) retains immutable binary identity, exact complete sources, commands, exits, Normal JSON, Session responses and durable replay commands. Runnable sources are in `evidence/round-16-cases/`.

No kernel/canonical textbook edits, added trust or runtime claims. Only isolated scalar/source-interface checks; registered chapters, continuity theorem dependencies and downstream consumers were not verified. Candidates are not implemented rules or complete causal diagnoses.
