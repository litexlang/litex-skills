# Part119 — Actual trivial kernel: twelve actions removable, singleton bridge kept

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and proof idea

The linear-algebra showcase proves that a linear map with kernel {0} is
injective. For T(u)=T(v), linearity and the inverse law imply T(u-v)=0;
the trivial kernel gives u-v=0, then addition cancellation gives u=v.
Keep the exact field, vector spaces, function, linearity and trivial-kernel
premises. Use round89's checked preceding source. No canonical edits.

## Checked positive and verbose comparison

[Complete preferred source](evidence/round-90-cases/preferred-short.lit)
removes twelve proof actions together: four repeated native theorem results,
two alias equalities, three membership echoes, the explicit difference-zero
and addition-zero facts, and the final injectivity definition action.
The meaningful image calculation and cancellation calls remain.

After native `set_builder_member`, the original source repeats:

```litex
\vector_sub<K,field,V,source>(u,v) $in {x V:T(x)=target.zero}
\vector_sub<K,field,V,source>(u,v) $in kernel
\vector_sub<K,field,V,source>(u,v) $in zero_space
\vector_sub<K,field,V,source>(u,v) $in {source.zero}
\vector_sub<K,field,V,source>(u,v)=source.zero
source.add(u,\vector_neg<K,field,V,source>(v))=source.zero
```

Only the singleton membership line remains in the checked combined route.
Canonical template equalities, the trivial-kernel premise and native membership
call are still present. The later addition chain checks the zero equation from
that preserved context. This is a context-specific reduction, not a general
rule saying all intermediate membership facts are redundant.

The final `u=v` repetition after `add_left_cancel` and final
`by def $injective(V,W,T)` can both be removed in the combined proof. Part117's
necessary subspace fold is a different case; fold deletion is checked here
rather than inferred from another predicate.

## Negative and deletion boundaries

Deleting all four membership facts rejects; individual probes show the last
singleton member is the boundary in the tested baseline. Deleting it alone
rejects; deleting each of the other three alone passes, and their joint
removal in the preferred proof passes. No kernel-defect claim follows from
this incomplete direct route.

Removing the trivial-kernel premise rejects both original and shortened
proofs. Removing the local T(u)=T(v) premise also rejects in the short route.
These are mathematically necessary conditions, unlike the true-but-unproved
singleton-deletion target. No trusts or strengthened premises are introduced.

[Native consumer](evidence/round-90-cases/preferred-native-consumer.lit)
calls the shortened theorem under its original premises and passes.
No whole-showcase or later concrete-instance acceptance is claimed.

## Evidence

[Receipt](evidence/round-90-2026-10-10.summary.json):18 independent strict files,
12 accepted/6 Normal rejections. All promoted paths rerun with matching exit,
Normal envelope and null session error. Actual source and binary identities
recorded; fixed snapshot from successful round88 build reused, no new build
claimed. Cold files exclusively own deletion evidence; old warm universal
facts cannot establish it. Same linear-algebra source family as Parts116–118,
not independent permanent-rule evidence. No new bt, canonical/kernel changes,
performance or global-minimum claim.

## Round91: compress cancellation, keep the image calculation

With the same native source inverse-spec call moved before the cancellation
calculation, the three original addition comparisons can be replaced by one:

```litex
source.add(\vector_neg<K,field,V,source>(v),u)=source.zero=source.add(\vector_neg<K,field,V,source>(v),v)
```

An expanded chain through `source.add(u,neg(v))` and `source.add(v,neg(v))`
also passes, but those intermediate expressions are unnecessary here.
The two unused `let kernel` and `let zero_space` bindings can be removed
jointly with this compression. This saves two calculation statements and two
bindings beyond round90. It does not remove or strengthen the kernel premise.
[Latest complete source](evidence/round-91-cases/preferred-short.lit).

Replacing the image calculation by only `T(vector_sub(u,v))=target.zero`
rejects; deleting the difference-to-addition expansion also rejects. Replacing
the cancellation chain by its bare endpoints or deleting that chain rejects.
These are true targets with insufficient tested routes, not mathematical
negatives or established kernel defects. Removing local T(u)=T(v) still
rejects in the preferred proof. Native theorem consumer passes.

[Round91 receipt](evidence/round-91-2026-10-10.summary.json):11 strict files,
6 accepted/5 Normal rejections, promoted paths rerun on the fixed round88
snapshot. Same source/binary identities and source family. One initial consumer
fixture truncated the theorem signature by matching an indentation substring
inside a premise. It was excluded before counting/promotion; the corrected
newline-anchored proof boundary produces a passing consumer. No new Part or
permanent general rule is inferred from this same-theorem continuation.
