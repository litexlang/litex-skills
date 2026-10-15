# Part 86 — Consume the actual Newton bound at n=2 with one chain

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source and proof idea

The numerical-analysis showcase ends with a four-statement checkpoint:
release the symbolic bound at2, repeat g_2<=B_2, evaluate B_2=1/64, and state
g_2<=1/64. Retain the checked recursive definitions, induction and comparison
bound from Part85. The numeric checkpoint changes no theorem or premise.

## Positive: four statements to one

This exact standalone checkpoint passes with the retained full symbolic prefix:

```litex
r44_sqrt_two_newton_gap(2)<=r45_sqrt_two_newton_gap_bound(2)=1/64
```

[Full runnable dependency slice and one-line checkpoint](evidence/round-46-cases/numeric-chain-without-call.lit).
The symbolic bound theorem remains defined; its known interface checks the first
adjacent comparison, while the second adjacent equality evaluates the numeric
bound. Explicit theorem release is removable in this tested chain. The original
four statements, release-plus-chain and bound value alone also pass cold.
No claim that all theorem calls or numerical value bridges are redundant follows.

## True direct misses and negative controls

These two reduced alternatives miss independently:

```litex
r44_sqrt_two_newton_gap(2)<=1/64
```

```litex
release thm r45_final_short(2)
r44_sqrt_two_newton_gap(2)<=1/64
```

Keep the intermediate bound expression in the chain for this consumer. The
same direct target succeeds late in a warm Session after the bound value and
comparison have been published; that warm success is not standalone capability.
The first warm direct attempt missed. Cold files settle the publication/deletion
question without assuming a cause in an uninspected kernel path.

The strengthened g_2<=1/256 rejects (mathematically g_2=1/144), as does
changing the index to0 while keeping1/64 (g_0=1). These are false numerical
bounds, separate from the true direct misses above. Exact g_2 evaluation was
not the acceptance target of this round; the retained bound theorem plus its
numeric consumer is the verified route.

## Evidence and remaining corpus scope

[Round46 receipt](evidence/round-46-2026-10-09.summary.json):8 cold strict files,
4 accepted/4 rejected; promoted copies rerun with the fixed current-source
release snapshot. Source hash, warm journal and build command retained.
The selected short recursive Newton mathematics now composes through the
actual numeric checkpoint. No canonical/kernel/protected-owner edit, new
trust, extractor, whole numerical-showcase or performance claim.
Next source family: probability/statistics showcase's three-point least-squares
certificate and mean constructor consumer, preserving the real candidate domain.
