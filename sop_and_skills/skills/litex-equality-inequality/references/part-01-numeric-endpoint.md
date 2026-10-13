# Part 1 — A closed numeric bound after an established equality

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and idea

The Newton sqrt(2) showcase's accepted prefix establishes the second step
residual as `1/144`. The remaining move is an exact rational comparison with
`1/64`; it does not require constructing a positive difference.
Anchor: `showcases/Write_Mathematically_Correct_Code_With_Litex/main.lit`.

## Positive and verbose comparison

These are **excerpts** sharing the identical original preceding context.
The receipt contains complete tested sources. Both versions pass strict
clean-file checks on the recorded binary.

Before:
```litex
80 / 9216 > 0
1 / 144 + 80 / 9216 > 1 / 144
1 / 64 = 1 / 144 + 80 / 9216
1 / 64 > 1 / 144
1 / 144 < 1 / 64
1 / 144 <= 1 / 64
square_root_two_residual(newton_sqrt_two_step(3 / 2)) = 1 / 144 <= 1 / 64
```

Preferred tested replacement:
```litex
square_root_two_residual(newton_sqrt_two_step(3 / 2)) = 1 / 144 <= 1 / 64
```

Six proof statements are removed. The preceding residual computation is
unchanged. Full-proof optimality and execution-time improvement are untested.

## Negative and capability boundary

With the same prefix, this **excerpt** rejects:
```litex
square_root_two_residual(newton_sqrt_two_step(3 / 2)) = 1 / 144 <= 1 / 256
```
It is false: `1/144 > 1/256`.

This separate self-contained numeric leaf passes:
```litex
1 / 90 <= 1 / 80
```
It is not independent evidence for arbitrary user-function unfolding or
equality substitution.

## Ideal form and improvement status

The ideal endpoint chain already works here: simplify the authoring rather
than invent a numeric builtin. Further compression of the preceding residual
computation is untested.

## Evidence

[Receipt](evidence/pilot-2026-10-08.summary.json): `newton-original`, `newton-short`,
`newton-false`, `numeric-transfer`; complete sources, commands, exits, JSON.
Runnable sources are retained under `evidence/cases/`; each receipt entry's
`replay_command` runs its retained source. Original issued commands are unchanged.
The short candidate also succeeded in a live Session loaded only through the
preceding prefix, before any comparison waterfall.

Date: 2026-10-08. Binary: `Litex 1.0.2-beta`, SHA-256 in receipt.
Current-source release build failed on unrelated working-tree compiler errors.
Results use the existing binary; source correspondence is unknown. Rebuild
and replay before claiming current-source acceptance.

Current-source follow-up: the later round-2 release build succeeded. All ten
pilot outcomes were reproduced on that newly built binary; see
[current-source recheck](evidence/pilot-current-recheck-2026-10-08.summary.json).
The earlier failed build and its binary receipt remain historical evidence.
