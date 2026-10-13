# Part 89 — Actual expectation linearity: twelve statements to five

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source situation and mathematical spine

The probability/statistics showcase uses a two_point_vector carrier of real
functions on positive natural indices<=2. A template constructs a*X+b*Y,
then expectation2 is a two-coordinate weighted sum. The theorem holds for
arbitrary real weights: no probability-vector predicate or normalization
premise is required. This card preserves the carrier, template and theorem.
Names are prefixed r49 only for the Session.

## Positive: remove the combined alias and repeated template publications

The source proof has12 statements, including a local combined function,
template-coordinate facts, repeated alias-coordinate facts and separate
algebraic steps. This checked five-statement replacement needs no local alias:

```litex
r49_expectation2(X,probs)=X(1)*probs(1)+X(2)*probs(2)
r49_expectation2(Y,probs)=Y(1)*probs(1)+Y(2)*probs(2)
r49_affine_combine2(X,Y,a,b)(1)=a*X(1)+b*Y(1)
r49_affine_combine2(X,Y,a,b)(2)=a*X(2)+b*Y(2)
r49_expectation2(r49_affine_combine2(X,Y,a,b),probs)=r49_affine_combine2(X,Y,a,b)(1)*probs(1)+r49_affine_combine2(X,Y,a,b)(2)*probs(2)=(a*X(1)+b*Y(1))*probs(1)+(a*X(2)+b*Y(2))*probs(2)=a*(X(1)*probs(1)+X(2)*probs(2))+b*(Y(1)*probs(1)+Y(2)*probs(2))=a*r49_expectation2(X,probs)+b*r49_expectation2(Y,probs)
```

[Full runnable short source slice](evidence/round-49-cases/affine-five-statements.lit)
contains the function carrier, expectation definition, coordinate template and
constructor. The original source proof also passes independently. This is an
actual function-valued constructor consumer, not a scalar replacement lemma.
The five statements are the shortest version verified in this round, not a
global lower bound on proof length or a runtime optimization claim.

## Deletion evidence: two different live bridges

The bodyless theorem misses cold. A chain-only proof misses at adjacent index1,
where named constructor coordinates are replaced by linear coordinate formulas.
Deleting either coordinate publication from the five-statement proof fails
at that same link. Keep the two exact constructor-call equations in this route.

Deleting either expectation value publication, or both, fails at adjacent
index3, the final equality replacing the expanded weighted sums with named
expectations. The polynomial distribution link before it is not the first
failure. These are true-target proof-search misses with all domains unchanged,
not mathematical counterexamples or WD failures in those chain links.
Warm bodyless success after the original theorem is stored is contaminated;
independent files determine deletion behavior. No universal mandatory-publication
rule is inferred from this one consumer; see Part64 for related dated template
entry evidence, not a replacement for the current constructor probe.

## Mathematical and domain negatives

Replacing the right-side coefficient a by2*a is false and rejects; choose
X constantly1,Y constantly0,a=1,b=0 and weights(1)=1,weights(2)=0 to see it.
Index3 violates the retained <=2 function domain, and an explicit third-coordinate
claim rejects. Neither negative justifies weakening the two-coordinate carrier.
No assumptions about probability weights were added to make the proof pass.

## Evidence and next source item

[Round49 receipt](evidence/round-49-2026-10-09.summary.json):11 independent strict files,
2 accepted/9 rejected; all promoted paths rerun with the fixed current-source
release snapshot. Source hash, build and incremental literal warm journal saved.
Session42453 remains live on the current-source release used after round48's
restart. Ordinary failures were retained in that Session. No canonical source,
kernel, AST/Env/Runtime, trust, whole showcase or performance change.
Next check the actual fair-coin expectation/variance numeric calculations and
probability-vector fold before moving to another corpus item.
