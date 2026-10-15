# Part 2 — Combine two bounds by subtraction

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Later implementation acceptance (2026-10-09)

The user-selected `SubtractionOrderPairs` rule has completed scoped implementation acceptance:

```litex
forall a,b,c,d R:
    a<=b
    c<=d
    =>:
        a-d<=b-c
```

The weak direct target is implemented. Do not require the historical b-d bridge. No strict-conclusion sibling is claimed.
See [selected-rule acceptance](https://github.com/litexlang/golitex/blob/e6f0fb6cab0bb69f99eb9a33b30deceae6d0a74a/tests/unit/execute/selected_scalar_bt_rules/acceptance.md) and its paired machine receipt for
actual working-tree strict example and guard/negative tests. Prefer the direct
form in this accepted scope; do not duplicate it as a new kernel candidate.
The sections below retain the earlier pilot's binary/date and describe its
former behavior, not a permanent current proof-step requirement. Current
round36 build failure does not undo that dated acceptance or establish a new
source gate. No full-corpus, Lean adapter or runtime claim is added.

## Mathematical situation and idea

For real `a,b,c,d`, `a <= b` and `c <= d` imply `a-d <= b-c`.
Subtraction increases with its first operand and decreases with its second.
The explicit route changes one operand at a time.
Anchor: Manual R07 and builtin strategy `structural_order_weak.rs`.

## Positive — historical explicit bridge

This self-contained strict check passes:
```litex
claim:
    ? forall a, b, c, d R:
        a <= b
        c <= d
        =>:
            a-d <= b-c
    a-d <= b-d <= b-c
```

## Verbose comparison

Illustrative expanded body, **not independently tested**:
```litex
a-d <= b-d
b-d <= b-c
a-d <= b-c
```
The tested chain records both moves and the endpoint. Do not claim the
expanded variant was run or that the intermediate term is permanently needed.

## Ideal direct form — historical capability miss

This true self-contained statement rejects on the recorded binary:
```litex
forall a, b, c, d R:
    a <= b
    c <= d
    =>:
        a-d <= b-c
```
JSON reports `phase: search_proof`, `session_error: null`.
In the same live Session after failure, the explicit chain succeeds.
Separate clean-file checks confirm both outcomes.

## Mathematical negatives

Wrong direction; rejects:
```litex
forall a, b, c, d R:
    a <= b
    c <= d
    =>:
        a-c <= b-d
```
Counterexample: `a=b=0, c=0, d=1` gives `0 <= -1`.

Missing second bound; rejects:
```litex
forall a, b, c, d R:
    a <= b
    =>:
        a-d <= b-c
```
Counterexample: `a=b=0, c=1, d=0` gives `0 <= -1`.

Weak premises do not supply strictness; rejects:
```litex
forall a, b, c, d R:
    a <= b
    c <= d
    =>:
        a-d < b-c
```
Counterexample: all values zero gives `0 < 0`.

## Historical candidate — weak form subsequently implemented

A componentwise subtraction builtin strategy could recognize
`L1-L2 <= R1-R2` and generate exactly:
```text
L1 <= R1
R2 <= L2
```
for well-defined real operands. No intermediate-expression search is needed.
Current source shows shared-subtrahend/shared-minuend strategies; this is not
a complete audit of every route. The binary miss does not prove its
source-level cause.

Implementation must preserve domain checks, bounded child verification,
proof evidence and rejection of the controls above. Strict variants require
at least one justified strict component and are outside this weak proposal.
No enhancement is implemented or benchmarked in this pilot.

## Evidence

[Receipt](evidence/pilot-2026-10-08.summary.json): `sub-direct`, `sub-chain`,
`sub-false`, `sub-missing`, `sub-strict-false`.
Runnable sources are retained under `evidence/cases/`; each receipt entry's
`replay_command` runs its retained source. Original issued commands are unchanged.
`sub-transfer` passes the same chain with renamed binders: spelling robustness,
not independent mathematical evidence or a skill-efficacy test.

Date: 2026-10-08. Binary: `Litex 1.0.2-beta`, SHA-256 in receipt.
Current-source release build failed on unrelated working-tree compiler errors.
Existing binary used; source correspondence unknown. Rebuild/replay before
claiming current-source acceptance. Update this card if direct support lands;
never teach today's miss as a permanent intermediate-step requirement.

Current-source follow-up: the later round-2 release build succeeded. The direct
miss, explicit success and negatives were reproduced on that binary; see
[current-source recheck](evidence/pilot-current-recheck-2026-10-08.summary.json).
