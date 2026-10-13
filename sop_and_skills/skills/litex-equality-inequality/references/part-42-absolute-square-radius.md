# Part 42 — Absolute-value bounds from squared bounds

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Later implementation acceptance (2026-10-09)

The user-selected `AbsSquareRadius` rule has completed scoped implementation acceptance:

```litex
forall x,r R:
    r>=0
    x^2<=r^2
    =>:
        abs(x)<=r
```

The weak radius target is implemented. Strict conclusions and composed unit-circle probes are separate; no new direct support is asserted for those variants.
See [selected-rule acceptance](https://github.com/litexlang/golitex/blob/e6f0fb6cab0bb69f99eb9a33b30deceae6d0a74a/tests/unit/execute/selected_scalar_bt_rules/acceptance.md) and its paired machine receipt for
actual working-tree strict example and guard/negative tests. Prefer the direct
form in this accepted scope; do not duplicate it as a new kernel candidate.
The sections below retain the earlier pilot's binary/date and describe its
former behavior, not a permanent current proof-step requirement. Current
round36 build failure does not undo that dated acceptance or establish a new
source gate. No full-corpus, Lean adapter or runtime claim is added.

## Mathematical situation and proof idea

For real x,r with r>=0, x^2<=r^2 implies abs(x)<=r; strict squared comparison implies the strict bound. A source rotation parameter pair satisfies c^2+s^2=1. Anchor: coordinate geometry `rotation_preserves_distance`, main.lit:1610.

## Existing support

The unit-circle identity directly supplies c^2<=1, and with s!=0 supplies c^2<1. The general identity x^2+y^2=A*B directly supplies x^2<=A*B. Weak and strict reflection between two absolute values already work when the exact squared comparison is available. Do not add duplicate square-sum extraction or absolute-vs-absolute rules.

## Ideal direct form: historical miss

```litex
forall x,r R:
    r >= 0
    x^2 <= r^2
    =>:
        abs(x) <= r
```

Even the numeric special cases x^2<=1 -> abs(x)<=1, x^2<=4 -> abs(x)<=2 and x^2<1 -> abs(x)<1 miss.

## Positive: historical explicit interface

```litex
claim:
    ? forall x,r R:
        r >= 0
        x^2 <= r^2
        =>:
            abs(x) <= r
    abs(x) <= abs(r) = r
```
```litex
claim:
    ? forall x,r R:
        r >= 0
        x^2 < r^2
        =>:
            abs(x) < r
    abs(x) < abs(r) = r
```

This removes the need for roots and keeps the right-hand sign condition inside the usable interface. Strict form needs only r>=0 as a sufficient guard; do not add unnecessary r>0.

## Unit-circle application

The following two chains pass:

```litex
claim:
    ? forall c,s R:
        c^2+s^2 = 1
        =>:
            abs(c) <= 1
    c^2 <= 1 = 1^2
    abs(c) <= abs(1) = 1
```

With s!=0, the same shape with strict comparison passes. Direct abs bounds fail, even after an explicit c^2<=1 statement. The magnitude-repair Session reproduces both weak and strict soft misses then accepts their repairs without restarting.

## Negatives

The radius sign cannot be omitted: x=0,r=-1 refutes abs(x)<=r even though x^2<=r^2. Weak squared order cannot supply strictness: x=r=1. A unit-circle point c=1,s=0 refutes abs(c)<1 and abs(c)<=1/2. Executable controls reject.

## Historical improvement candidates

1. Priority: bounded `abs(x)<=r` / `abs(x)<r` strategy with checked real domains, r>=0, and corresponding x^2<=r^2 / x^2<r^2 obligations. Preserve child WD and exact certificates; reject missing sign and weak-to-strict controls. The existing two-absolute-value strategy in structural_order_weak.rs / structural_order_strict.rs literally requires `as_abs` on both sides; a plain radius is outside that particular matcher. Other possible routes have not been completely audited.
2. Lower priority: compose square-sum-bound extraction with an exactly equivalent closed endpoint within existing permissions. `c^2+s^2=1 -> c^2<=1^2` misses, while the meaningful intermediate c^2<=1 succeeds. This is not grounds for increasing global search depth.

## Narrowing the numeric nomination

Generic closed endpoint transport already works:

```litex
forall x R:
    x^2 <= 1
    =>:
        x^2 <= 1^2
```

Its strict sibling, x<=1 -> x<=1^2 and x<=4 -> x<=2^2 also pass. A change to the unequal endpoint x<=4 -> x<=1^2 rejects. Do not nominate a new generic endpoint-normalization rule from the composed circle miss. Today's two-chain bridge is not a permanent source requirement.

## Evidence and scope

Dated 2026-10-08. Fresh current-worktree release build succeeded. [Round 14 receipt](evidence/round-14-2026-10-08.summary.json) retains immutable binary SHA-256/version, sources, commands, exits, Normal JSON, Session responses and durable replay commands. Cases are retained in `evidence/round-14-cases/`.

No trust, kernel/canonical proof edits or runtime claims. These are dated reduced interfaces; enclosing geometry replacement and downstream consumers were not checked. New strategies remain proposals, not implemented or causally diagnosed fixes.
