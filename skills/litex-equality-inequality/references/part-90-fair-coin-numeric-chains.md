# Part 90 — Actual fair-coin checkpoint: fourteen statements to seven

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source and preserved domains

The probability/statistics showcase defines real two-point functions on positive
natural indices<=2, expectation2 as the weighted sum, and variance2 around that
expectation. The coin values are k-1 and the weights are1/2. Preserve those
functions and the probability-vector predicate's two sign clauses and sum1.
No expectation/variance definition, carrier or normalization condition changes.

## Positive: one chain per numeric calculation

The source checkpoint has14 statements: two function-carrier publications,
four coordinate values, one probability fold, three expectation statements
and four variance statements. The checked replacement has seven: retain the
four coordinate values and inline fold, combine each calculation into one chain.

Exact expectation chain:

```litex
r50_expectation2(r50_fair_coin_values,r50_fair_coin_probs)=r50_fair_coin_values(1)*r50_fair_coin_probs(1)+r50_fair_coin_values(2)*r50_fair_coin_probs(2)=0*(1/2)+1*(1/2)=1/2
```

[Complete seven-statement slice](evidence/round-50-cases/combined-seven-statements.lit)
contains all retained definitions, four values, inline probability fold and
literal variance chain. The variance chain passes through the original
weighted squared-deviation expression, then the literal expression
(0-1/2)^2*(1/2)+(1-1/2)^2*(1/2)=1/4.
No local aliases, new helper theorem, or separate real/type echoes are added.
The original checkpoint also passes. The source's two carrier publications
can be deleted in this combined consumer; carrier facts themselves still check
independently if a reader chooses to state them.

## Live bridges and true direct misses

Bare expectation=1/2 and variance=1/4 miss at search_proof, not WD. Publishing
four coordinate values still does not make those direct targets pass. The
explicit weighted-expression chain is the checked route. An expectation chain
without those coordinate publications also misses. No general constant-function
or arithmetic-evaluation failure cause is claimed from these observations.

Probability-vector direct assertion and inline by-def without values miss.
The two probability coordinate values plus inline by-def pass independently;
deleting the first value from that route fails. The retained probability fold
is exactly the source predicate, not a stronger or weaker replacement.

Variance with four coordinate values and the accepted expectation chain passes.
Deleting that expectation chain makes the otherwise same variance chain fail.
The earlier variance-coordinate-values fixture with only a direct expectation
assertion fails first at that assertion; it is not independent evidence of a
variance consumer defect. Distinguish upstream failure from downstream proof
support. The seven-statement route is a verified shortening, not a global
minimum or a speedup claim.

## Negative controls and evidence

Wrong expectation1/4 and variance1/2 reject. Weights constantly1 violate the
probability sum and their definition fold rejects. Index3 violates the retained
function domain and rejects. None of these controls authorizes an added trust
or a changed numeric value to repair a direct miss.

[Round50 receipt](evidence/round-50-2026-10-09.summary.json):21 independent strict files,
6 accepted/15 rejected, all promoted copies rerun on the fixed current-source
release snapshot. Source hash, build and literal incremental warm journal saved.
Session42453 remains live; ordinary failures were repaired in that process.
No canonical/kernel/AST/Env/Runtime edit, trust, whole probability showcase
or performance claim. Next return to a textbook source family: high-school
exponential lower-bound induction, inspecting its old proof format separately
from the intended mathematical inequality.
