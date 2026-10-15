# Part 103 — Integer strict order gives a successor gap

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source situation and existing direct support

Actual examples/proof_nodes/less_equal/by_builtin_rule/integer_successor_gap.lit
states x in Z, x>4 implies 5<=x. Integers have no values strictly between 4
and 5. Preserve the integer carrier; an arbitrary real need not have this gap.

```litex
forall x Z:
    x>4
    =>:
        5<=x
```

[Exact source](evidence/round-63-cases/source.lit). The opposite spellings
4<x and x>=5 pass, as do the negative threshold x>-4 implies -3<=x and
the natural-number version. No predecessor calculation or contradiction
block is needed for these tested targets.

The symbolic integer forms also pass independently:

```litex
forall a,b Z:
    a<b
    =>:
        a+1<=b
```

The alternative conclusion 1<=b-a passes too.
[Successor](evidence/round-63-cases/integer-symbolic-successor.lit),
[difference](evidence/round-63-cases/integer-symbolic-difference.lit).
These are current existing capabilities, not proposals to add another bt rule.

## Avoid scaffolding for the directly supported source

A current `claim: ? forall ...` block with a repeated 5<=x proof-body fact
passes but provides no additional mathematical move over the direct source.
[Expanded comparison](evidence/round-63-cases/current-expanded-claim.lit).
The initial author candidate mistakenly used old `prove:` syntax; it is
preserved as a separate parse control, corrected before mathematical comparison.
Do not interpret that syntax failure as an integer-order capability result.

## Rational threshold: preserve a meaningful comparison chain

The true bare implication x in Z, x>9/2 implies 5<=x misses search_proof.
This same-target claim passes:

```litex
claim:
    ? forall x Z:
        x>9/2
        =>:
            5<=x
    4<9/2<x
```

[Complete short route](evidence/round-63-cases/half-threshold-bridge-chain.lit).
The chain exposes 4<x while retaining the given threshold. The existing
integer gap then closes the claim; a repeated 5<=x body line is unnecessary.
Replacing the chain with only 4<x fails at proof_body step0/search_proof,
not merely the final claim conclusion. This does not establish general
floor/ceiling automation or the reason the direct rational-threshold goal misses.

## Negative controls

The following attempted changes reject in separate strict files:

- x in R, x>4 implies 5<=x; the checked numeric facts 9/2>4 and 9/2<5
  provide a concrete counterexample.
- x in Z, x>=4 implies 5<=x; x=4 violates it.
- x in Z, x>4 implies 5<x or 6<=x; x=5 violates them.
- a,b in R, a<b implies a+1<=b; arbitrary real gaps need not reach 1.

[Real counterexample facts](evidence/round-63-cases/numeric-real-counterexample.lit),
[false strictness](evidence/round-63-cases/false-strict-conclusion.lit).
These mathematical negatives differ from the true rational-threshold search miss.

## Evidence and boundaries

[Receipt](evidence/round-63-2026-10-09.summary.json):17 strict files,
9 accepted/7 Normal rejections/1 author syntax error. All promoted paths
rerun on a fixed snapshot after a successful current-source release build.
Exact source hash, build log and literal Session journal retained. Session9174
uses round61: it accepted the source and rejected the real-carrier generalization
without restarting. Cold files own the symbolic and rational-threshold results.
No canonical source, kernel, trust, protected owner, timing or whole-corpus
claim. Retain the scoped chain for the rational threshold rather than teaching
an unnecessary expansion of already direct integer targets.
