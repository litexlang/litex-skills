# Part 111 — Actual normal-kernel proof: native calls replace result echoes

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and original interfaces

The abstract-algebra showcase proves that a group homomorphism's kernel
{candidate A: f(candidate)=one_B} is a normal subgroup. Preserve the exact
generic carriers, group/homomorphism predicates and subgroup definitions.
The proof establishes identity membership, product/inverse closure and
conjugation closure. Reuse native group theorems and set_builder_member;
do not replace the kernel by a private predicate or stronger assumptions.

The baseline includes Part110's already checked shorter homomorphism bodies.
The original source through the kernel theorem and this baseline both pass.
The source's later struct APIs are outside this gate.

## Checked joint deletion

Eight result echoes can be removed together from the kernel proof:

- f(one_A)=one_B after homomorphism_maps_identity.
- f(inv_A(kernel_x))=inv_B(f(kernel_x)) after the inverse theorem.
- inv_B(one_B)=one_B after group_inverse_unique.
- f(inv_A(conjugator))=inv_B(f(conjugator)) after the inverse theorem.
- Four member assertions after set_builder_member: identity, product,
  inverse and conjugate membership.

The final `by def $is_normal_subgroup(...)` action can also be removed from
that jointly shortened route. The complete unchanged theorem goal closes
from the already stored subgroup fact and conjugation law. Nine statements
or actions are removed; no native theorem call is removed.
[Full preferred source](evidence/round-72-cases/short-delete-normal-fold.lit).

For example, inverse closure now keeps only these four proof statements
inside the source's original kernel_x membership binder:

```litex
release thm homomorphism_maps_inverse(A,mul_A,one_A,inv_A,B,mul_B,one_B,inv_B,f,kernel_x)
release thm group_inverse_unique(B,mul_B,one_B,inv_B,one_B,one_B)
f(inv_A(kernel_x))=inv_B(f(kernel_x))=inv_B(one_B)=one_B
release thm set_builder_member(inv_A(kernel_x),{candidate A: f(candidate)=one_B})
```

This is an excerpt; the linked full context owns its carriers, assumptions
and all earlier theorem declarations. The chain remains a mathematical move
showing that the inverse maps to the target identity. Its result is then
converted to kernel membership by the native theorem call.

## Retained bridges and nearest false target

Two source facts remain necessary in the shortened conjugation proof:
f(mul_A(conjugator,kernel_h))=mul_B(f(conjugator),f(kernel_h)), and
mul_B(f(conjugator),one_B)=f(conjugator). Deleting either separately fails.
The explicit by-def action for is_subgroup inside its claim also remains
necessary: deleting it fails. Do not infer that all definition actions or
all implied equalities are removable from the final normal-fold deletion.

Replacing only the theorem goal's kernel equation by f(candidate)!=one_B
rejects, both with the eight-echo deletion route and with the final-fold
deletion route. The complement excludes the image of the source identity
and is not a subgroup. These false-goal controls are distinct from valid
bridge-deletion misses.
[Short false complement](evidence/round-72-cases/short-wrong-complement.lit).

## Evidence and limits

[Receipt](evidence/round-72-2026-10-09.summary.json):14 strict cold files,
9 accepted/5 Normal rejections. All promoted paths rerun on the fixed snapshot
after successful current-source release build. Exact source/binary identities
and build log retained. Exact-line body deletion asserted the original theorem
header was intact; no accidental goal alteration counted as capability evidence.
Session66922 stays on round68 and accepted the two source subgroup predicates
and complete preferred theorem as single blank-line-free frames. Cold round72
owns joint-deletion and negative evidence. No canonical source, kernel, trust,
protected owner, timing or whole-showcase change.
