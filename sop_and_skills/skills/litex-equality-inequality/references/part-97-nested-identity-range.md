# Part 97 — Nested identity versus a range-restricted identity consumer

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Current source and domain

The inspected chapter04 defines identity:R->R and identity_on_range on
fn_range(identity), returning its input. Current source has separate forall x
blocks for ordinary nesting and range-restricted nesting. The anticipated old
malformed strict-order block is not present in this inspected version; do not
report that historical concern as a current source defect. Source hash retained.
No imported HighSchoolCite predicate, inverse-existence theorem or witness was
included in this isolated comparison slice.

## Positive: ordinary nested identity has a direct endpoint

With the two exact definitions, the original identity(identity(x))=identity(x)=x
chain passes, and this direct central equation passes independently:

```litex
forall x R:
    r57_identity(r57_identity(x))=x
```

[Full direct slice](evidence/round-57-cases/nested-direct.lit).
This removes one intermediate equality from the same one-statement calculation;
it is not a statement-count reduction or a global nested-function shortcut.

## Range-restricted nesting: retain the chain or one local value fact

The original source chain passes independently:

```litex
forall x R:
    r57_identity_on_range(r57_identity(x))=r57_identity(x)=x
```

Its direct endpoint misses. This alternative checked claim needs only one
proof-body statement, without repeating the claimed endpoint:

```litex
claim:
    ? forall x R:
        r57_identity_on_range(r57_identity(x))=x
    r57_identity(x)=x
```

[Complete local-value claim](evidence/round-57-cases/range-inner-value-only.lit).
The two-body value-plus-target candidate also passes, so the target echo is
removable. The source chain already uses one statement; the claim alternative
is an explanation of a live local bridge, not a recommendation to replace that
short source chain with more scaffolding. Preserve the range-restricted domain.

## Scope and range controls

The direct image membership identity(x) in fn_range(identity) passes, as does
identity_on_range(y)=y for y in that range. Publishing the global image membership
before the direct nested endpoint does not repair it. Publishing the global
forall identity(x)=x before that endpoint also does not repair it, while the
local claim-body value fact does. Treat these as exact scope/consumer outcomes;
no internal storage, WD or matcher cause is established by the Normal search
failure alone. A different outer-value bridge candidate also fails.

Offsetting either nested identity target to x+1 is false and rejects. The
constant-five function's range does not contain0; the positive membership claim
0 in fn_range(constant) rejects. These are mathematical negative controls;
they do not justify changing the image carrier to all of R.

## Evidence and next source item

[Round57 receipt](evidence/round-57-2026-10-09.summary.json):15 independent current-built
strict files,8 accepted/7 rejected; all promoted paths rerun on the fixed fresh
release snapshot. Source hash, build log and literal warm journal retained.
Current build completed before snapshot creation. Session99217 remains the older
round51 executable and is labeled; cold current files own all scope/direct claims.
No canonical scripts/kernel/protected-owner/trust edit, imported inverse-property,
whole-chapter or performance acceptance. Next inspect source odd/even/zero
function equations independently of their imported predicate folds.
