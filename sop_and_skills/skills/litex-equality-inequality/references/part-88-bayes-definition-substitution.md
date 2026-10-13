# Part 88 — Actual Bayes substitution needs no theorem proof body

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source situation and domain

The probability/statistics showcase defines conditional_probability(joint,evidence)
as joint/evidence and bayes_posterior(prior,likelihood,evidence) as
likelihood*prior/evidence. Both definitions require real evidence>0.
The source theorem assumes joint=likelihood*prior, then expands two function
values and states quotient equality. This is definition substitution, not an
additional probability axiom; the source does not impose probability-range
premises on its real arguments, and this card adds none.

## Positive: three proof statements to a bodyless theorem

This exact shortened theorem passes independently with both definitions:

```litex
thm r48_bayes_bodyless:
    ? forall prior, likelihood, evidence, joint R:
        evidence > 0
        joint = likelihood * prior
        =>:
            r48_conditional_probability(joint, evidence) = r48_bayes_posterior(prior, likelihood, evidence)
```

[Full runnable bodyless slice](evidence/round-48-cases/bayes-bodyless.lit).
The original three-statement proof, full one-chain proof and each one-statement
value/quotient variant also pass. Since the whole body can be deleted, those
individual bridges are optional here. Preserve the real premises and reusable
function definitions; do not add a Bayes-specific bt rule for this case.

## Numeric source checkpoint: five statements to one

The source publishes a product equality, releases the Bayes theorem, states
function equality and evaluates each side. With just the two definitions,
this single chain checks all numeric conclusions:

```litex
r48_conditional_probability(1/4,1/2)=r48_bayes_posterior(1/3,3/4,1/2)=1/2
```

[Full independent numeric slice](evidence/round-48-cases/numeric-direct-chain.lit).
This file contains no Bayes theorem or product publication. Its literals satisfy
the positive evidence guard, and the arithmetic is closed. The original numeric
checkpoint also passes. This does not imply symbolic premises can be dropped.

## Negative boundaries and author error

Without joint=likelihood*prior the symbolic theorem is false; e.g. evidence=1,
prior=likelihood=1,joint=2. Replacing that premise by joint=2*likelihood*prior
is also false with those values. Both reject. Removing evidence>0 leaves the
function-domain guard unproved; zero evidence explicitly violates the domain.
Those controls reject separately from the mathematical false product cases.

The initial generator matched the conclusion line when splitting the proof
body and left an empty then-clause. The malformed warm candidate triggered a
parse error and ended Session25852; it is excluded from capability results.
The split was corrected to the exact four-space proof line, then a new current-
source Session42453 replayed the two definitions and original theorem. Corrected
candidates and numeric chain passed there. The restart follows process death,
not an ordinary proof miss; unrelated historical contexts were not claimed
replayed. Exact author error/restart and literal responses are retained.

## Evidence and scope

[Round48 receipt](evidence/round-48-2026-10-09.summary.json):12 independent strict files,
8 accepted/4 rejected, all promoted copies rerun on the fixed current-source
release snapshot. Source hash, build/restart and warm journal retained.
No canonical mathematics/kernel/AST/Env/Runtime edit, new trust, whole probability
showcase, probability-range extension, or performance claim. Next check actual
expectation linearity through its two-coordinate template interface.
