# Part 59 — Keep summation-factor algebra on a short proof spine

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and source

Concrete Mathematics Chapter 2 equations (2.9)–(2.11) scale a first-order
linear recurrence by a summation factor. The mathematical moves are substitution,
distribution, the factor equation, and folding the previous scaled value.
There is no need to discover a recurrence solution automatically.

The exact isolated source interface and original proof are in
[source-recurrence-original](evidence/round-20-cases/source-recurrence-original.lit).
Only that extracted theorem context was tested, not the registered chapter.

## Scalar direct miss and one-chain author

```litex
claim:
    ? forall lhs_value,coef,offset,previous_value,new_coef,scale R:
        lhs_value=coef*previous_value+offset
        scale*coef=new_coef
        =>:
            scale*lhs_value=new_coef*previous_value+scale*offset
    scale*lhs_value=scale*(coef*previous_value+offset)=(scale*coef)*previous_value+scale*offset=new_coef*previous_value+scale*offset
```

The chain passes; the direct forall with the same premises misses. Removing
the coefficient equation rejects a false conclusion. Ordinary same-grouped
congruence already works and should not be proposed as a duplicate rule.

## Verified source shortening

Deleting the source's generic `left_value=right_value =>
left_value+added_value=right_value+added_value` helper passes.
[Five proof statements](evidence/round-20-cases/source-recurrence-five-statements.lit)
also pass: the original recurrence equation, factor equation, previous scaled
definition, explicitly grouped scaled-product equation and one final chain.
Tested three/four-statement alternatives and deletion of the previous scaled
definition miss. This is the best checked variant here, not a global minimum.

The prior-value definition line is a demonstrated current representation bridge,
not a permanent mathematical requirement. A generic consumer improvement may
be worth inspecting together with Part 58's association evidence. No rule
should recognize the user-defined `scaled_recurrence_value_210` name.

## Evidence and limits

[Round 20 receipt](evidence/round-20-2026-10-09.summary.json), `scalar-substitution-*`
and `source-recurrence-*`. Same-Session misses and repairs are retained.
An initial reserved-name `C` parse error is excluded from mathematical findings.
The original immutable snapshot was rechecked on resumption; current worktree
build is blocked elsewhere. No canonical edits, trust, full chapter acceptance
or measured speed improvement.
