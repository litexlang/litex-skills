# Part 45 — Compare a positive-denominator quotient with a scalar

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Later implementation acceptance (2026-10-09)

The user-selected `QuotientScalarUpperBound / QuotientScalarStrictUpperBound` rule has completed scoped implementation acceptance:

```litex
forall a,b,M R:
    b>0
    a<=M*b
    =>:
        a/b<=M
```

Both the weak target and its strict sibling are implemented and have dedicated accepted examples. Negative-denominator forms are outside that implementation update.
See [selected-rule acceptance](https://github.com/litexlang/golitex/blob/e6f0fb6cab0bb69f99eb9a33b30deceae6d0a74a/tests/unit/execute/selected_scalar_bt_rules/acceptance.md) and its paired machine receipt for
actual working-tree strict example and guard/negative tests. Prefer the direct
form in this accepted scope; do not duplicate it as a new kernel candidate.
The sections below retain the earlier pilot's binary/date and describe its
former behavior, not a permanent current proof-step requirement. Current
round36 build failure does not undo that dated acceptance or establish a new
source gate. No full-corpus, Lean adapter or runtime claim is added.

## Mathematical situation

For real a,b,M with b>0, a<=M*b implies a/b<=M. The numerator and scalar M may be negative. Weak and strict forms share the denominator sign guard. Positive-total normalized weighted averages are an actual consumer of this interface; earlier fraction-vs-fraction comparison is a different source shape.

## Ideal direct form: historical miss

```litex
forall a,b,M R:
    b > 0
    a <= M*b
    =>:
        a/b <= M
```

Even a<=b to a/b<=1 misses. Strict a<M*b to a/b<M also misses.

## Positive: historical continuous chain

```litex
claim:
    ? forall a,b,M R:
        b > 0
        a <= M*b
        =>:
            a/b <= M
    a/b <= (M*b)/b = M
```
```litex
claim:
    ? forall a,b,M R:
        b > 0
        a < M*b
        =>:
            a/b < M
    a/b < (M*b)/b = M
```

Both repaired the direct soft miss in the same synchronized quotient Session. The chain uses existing common-positive-denominator comparison and exact cancellation.

## Existing reverse support

The reverse conversion already passes directly:

```litex
forall a,b,M R:
    b > 0
    a/b <= M
    =>:
        a <= M*b
```

Do not propose a duplicate reverse rule. The explicit reverse chain is a comparison control, not a permanent authoring requirement.

## Negatives

With b<0, the forward inequality direction reverses. a=-1,b=-1,M=0 refutes the same-direction bound even though a<=M*b. The executable negative-denominator control rejects. Zero total in the normalized-weight consumer is rejected at the undefined division boundary. Do not turn a nonzero-only guard into a positive-denominator guarantee.

## Historical candidate — positive forms subsequently implemented

For a/b<=M or a/b<M, check real domains and b>0, then the matching a<=M*b or a<M*b child. Retain exact positivity, WD and comparison certificates; generate no intermediate quotient expression. Existing shared-denominator comparison strategy is a read-only owner anchor; the total internal cause of the missing scalar form has not been audited. Negative-denominator variants require an explicitly reversed child relation and separate acceptance evidence; they are outside this positive-only nomination.

## Evidence and scope

Dated 2026-10-08. Fresh current-worktree release build succeeded. [Round 15 receipt](evidence/round-15-2026-10-08.summary.json) retains immutable binary identity, full sources, commands, exits, Normal JSON and synchronized Session responses. Durable sources in `evidence/round-15-cases/` have replay commands. One malformed generated least-squares candidate is separately retained as excluded authoring-error evidence; its corrected version was tested and passes. It is not a kernel miss.

No trust, kernel/canonical source changes, enclosing showcase verification or performance claims. These are scoped cases and nominations, not universal rules or implemented enhancements.
