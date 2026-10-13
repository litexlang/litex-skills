# Part 53 — Canonicalize finite-sum translation endpoints

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and actual source

Shift a nonempty integer summation interval by one while translating the callback. Source: Concrete Mathematics chapter02 `finite_integer_sum_shift`, with its explicit empty-sum wrapper. Native sum is nonempty; wrapper empty values must remain distinct.

## Original migration issue

The isolated original theorem fails parsing at:

```litex
by def $fn_eq(term, fn(lambda_index Z) Z {term(lambda_index)})
```

The current parser explicitly says $fn_eq is removed and directs ordinary equality or by fn_extension. A copied current-syntax rewrite using by fn_extension parses and establishes the eta equality, then misses at its reindex equation. Do not call the parse failure a missing mathematical rule or prescribe removed syntax.

## Ideal direct form: observed miss

```litex
forall a,b Z,f fn(k Z) Z:
    a <= b
    =>:
        sum(a,b,f) = sum(a-1,b-1,fn(k Z) Z {f(k+1)})
```

Explicitly supplying a-1<=b-1 does not solve the direct target. An anonymous eta-expanded source callback also misses. The fixture orientation sum(a,b,fn(k Z)R{f(k+t)})=sum(a+t,b+t,f) with legal ranges already passes; do not duplicate its translation law.

## Positive: keep the offset endpoint visible

```litex
claim:
    ? forall a,b Z,f fn(k Z) Z:
        a <= b
        =>:
            sum(a,b,f) = sum(a-1,b-1,fn(k Z) Z {f(k+1)})
    a-1 <= b-1
    (a-1)+1 = a
    (b-1)+1 = b
    sum(a-1,b-1,fn(k Z) Z {f(k+1)}) = sum((a-1)+1,(b-1)+1,f) = sum(a,b,f)
```

Deleting the two endpoint equalities makes this shortened route miss. The native literal-offset version itself passes:

```litex
forall a,b Z,f fn(k Z) Z:
    a <= b
    a-1 <= b-1
    =>:
        sum(a-1,b-1,fn(k Z) Z {f(k+1)}) = sum((a-1)+1,(b-1)+1,f)
```

The total wrapper target passes with interval legality, those endpoint equalities, a reverse sum chain and a wrapper chain. See receipt `wrapper-shift-reverse-bridge`. It avoids the original eta-function equality and tautological pointwise waterfall; no entire registered chapter was checked.

## Negatives and empty convention

Changing callback f(k+1) to f(k-1) rejects (take f(k)=k). Native sum on a>b rejects; the wrapper returns zero and passes. A callback declared only on N+ cannot be applied to a shifted interval including zero even if its body f(k+1) is meaningful there; the declared callback domain control rejects.

## Improvement candidate and source anchor

Inspect translation offset/endpoints and the consumer of their checked affine equalities. The existing direct_shift helper in search_equal_fact_by_aggregate_identities.rs only recognizes an Add on the after side. Subtraction and reverse-offset shapes fall back to symbolic differences; the aggregate dispatcher already tries both orientations. Therefore adding another reversed dispatcher attempt is not justified.

A bounded endpoint/offset normalization can recognize exact affine +/- integer translations and retain the corresponding equality/WD/pointwise certificates. Callback argument affine cancellation is a related candidate from Part 39, but its precise causal contribution here has not been established. No global function unfolding, new interval convention or broad recursion increase is implied.

## Evidence and limits

Completed 2026-10-09; started 2026-10-08. The successful source release build and all probes use one immutable binary snapshot; individual wall timestamps were not captured. [Round 18 receipt](evidence/round-18-2026-10-09.summary.json) retains source, exact command/exit/Normal JSON, binary identity, synchronized Session responses and durable replay commands. Sources are in `evidence/round-18-cases/`.

No kernel/canonical textbook edits, trust, whole-book gate or performance claims. These are dated scoped observations and nominations; current-syntax source probes are independent copies, not registered chapter repairs.
