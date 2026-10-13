# Part 117 — Actual linear kernel: omit repeated facts, retain the subspace fold

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source mathematics and interface

The linear-algebra showcase defines linear_kernel as the native set builder
{x V:T(x)=target.zero}. A linear map's zero image and its addition/scalar-action
laws show this set contains source.zero and is closed under both operations.
Preserve the exact is_linear_map/is_subspace predicates, both vector spaces,
common field, kernel template and theorem goal. Use round86's checked short
image/zero-law prefix; no alternative kernel predicate or stronger assumptions.

## Checked joint deletion

The original kernel proof repeats two native theorem results:
T(source.zero)=target.zero and target.smul(a,target.zero)=target.zero.
It also repeats six member facts after set_builder_member: three literal
set-builder memberships and three memberships using the kernel alias.
All eight facts can be removed together when the original final action remains:

```litex
by def $is_subspace(K,field,V,source,\linear_kernel<V,W,target.zero,T>)
```

[Complete preferred source](evidence/round-87-cases/joint-echo-deletion-retain-fold.lit)
contains exact binders and all unchanged closure calculations. Native calls,
kernel-to-set-builder equalities, input-member bridges and image-value facts
inside the closure proofs stay in place. These were retained for round87; round88 below tests their removal. This round removes eight immediate/nested proof statements, not the
mathematical identity/product/scalar-closure argument.

For scalar closure, the remaining proof-body route is:

```litex
v $in {x V:T(x)=target.zero}
T(v)=target.zero
release thm scalar_times_zero_vector(K,field,W,target,a)
T(source.smul(a,v))=target.smul(a,T(v))=target.smul(a,target.zero)=target.zero
release thm set_builder_member(source.smul(a,v),{x V:T(x)=target.zero})
```

This excerpt sits under the original a in K, v in V, v in kernel binder and
source linear premise. Its claim exports closure in the kernel; no separate
output member repetition is needed after the native call.

## Definition-action and false-target boundaries

Removing the final subspace fold rejects, both with the baseline and with the
jointly shortened proof. Do not generalize Part111's removable final normal-
subgroup fold to this different interface/context. The complement target
{x V:T(x)!=target.zero} also rejects: it excludes the source zero vector.
That mathematical negative differs from the true no-fold capability miss.

One initial keep-fold fixture appended its indented command after a dedented
trailing source comment, causing an unexpected-indent parse error. The receipt
excludes that old fixture result. Corrected exact-line deletion keeps the fold
at its original position and passes. The earlier apparent joint-deletion
failure with a retained fold was an author fixture error, not alias coupling
or a semantic verifier diagnosis.

## Evidence

[Receipt](evidence/round-87-2026-10-10.summary.json):11 corrected strict files,
8 accepted/3 Normal rejections, all promoted paths rerun on a fixed snapshot
after successful current-source release build. Exact source/binary identities
and build log retained. Session66922 on round68 accepted exact kernel/subspace
declarations and the complete short theorem; current cold files own deletion
and negative evidence. Round87 did not check later injectivity/concrete APIs.
Same linear-algebra source family as Parts116, not independent permanent-rule
promotion evidence. No canonical source, kernel, trust, protected struct,
performance, global-minimum or new bt claim.

## Round88: input facts and alias equality also removable

Under the original input membership premises, three explicit literal input
memberships, three image-value facts and the alias equality
`kernel = {x V:T(x)=target.zero}` can all be removed together. This removes
seven further statements after round87's eight. Keep the canonical template
equality and final subspace fold; deleting the template equality rejects in
the tested baseline.

Scalar closure now uses these three statements in its original claim:

```litex
release thm scalar_times_zero_vector(K,field,W,target,a)
T(source.smul(a,v))=target.smul(a,T(v))=target.smul(a,target.zero)=target.zero
release thm set_builder_member(source.smul(a,v),{x V:T(x)=target.zero})
```

The enclosing premises still include `a $in K`, `v $in V`, `v $in kernel`
and the original linear-map property.
[Latest complete source](evidence/round-88-cases/combined-short-route.lit)
keeps the original theorem goal. The prefix through the following
`injective_linear_map_has_trivial_kernel` also passes; this is source
continuation acceptance, not a claim of direct dependency on the shortened
subspace theorem or complete-module acceptance.

[Round88 receipt](evidence/round-88-2026-10-10.summary.json):11 strict files,
8 accepted/3 Normal rejections on the fixed round88 snapshot, including both
complement-kernel negative controls. Promoted paths rerun. The old Session
already held round87's theorem; cold files exclusively own new deletion
evidence. Same source family, not independent permanent-rule promotion.
