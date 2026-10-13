# Part 99 — Actual plane vectors: scalar endpoints, tuple chains and a remaining gap

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Round81 update: subtraction and scalar multiplication have native routes too

The exact chapter07 sub2 and smul2 formulas/carriers, with []→() and isolated
r81 names, accept the native coordinate interface plus result chain:

```litex
release thm tuple_equal_from_coordinates(((5,7)(1)-(2,3)(1),(5,7)(2)-(2,3)(2)),(5-2,7-3))
r81_sub2((5,7),(2,3))=((5,7)(1)-(2,3)(1),(5,7)(2)-(2,3)(2))=(5-2,7-3)=(3,4)
release thm tuple_equal_from_coordinates((3*(2,-1)(1),3*(2,-1)(2)),(3*2,3*(-1)))
r81_smul2(3,(2,-1))=(3*(2,-1)(1),3*(2,-1)(2))=(3*2,3*(-1))=(6,-3)
```

These are excerpts; [full definitions and joint consumer](evidence/round-81-cases/both-native-chains.lit)
own the runnable context. Neither route needs separate coordinate facts.
Bare endpoints, chains without native calls, and native calls followed only
by function endpoints all miss. Wrong sub output(3,5) and wrong smul sign(6,3)
reject with the native/chain routes. Coefficient -3 gives(-6,3), and zero gives
(0,0), with corresponding native chains; no positive restriction is added.

[Round81 receipt](evidence/round-81-2026-10-09.summary.json):13 strict files,
5 accepted/8 Normal rejections, all promoted paths rerun on the fixed snapshot
after successful current-source release build. Exact source/binary hashes
retained. Session66922 on round68 checked only numeric coordinate theorem
calls; cold current files own vector consumers and sign boundaries. This
updates historical sub/smul explicit checkability, not their unlocated first
failure causes. No direct-gap/raw [] chapter/whole-corpus/kernel/trust/canonical
change or global-minimum claim.

## Round80 update: existing coordinate theorem checks the exact reduced target

The preserved direct reduced file still misses on the current snapshot. The
same tuple-sum equality is explicitly checkable by one native theorem call,
without publishing the four input-coordinate values:

```litex
release thm tuple_equal_from_coordinates(((1,2)(1)+(3,4)(1),(1,2)(2)+(3,4)(2)),(1+3,2+4))
```

[Full native positive](evidence/round-80-cases/native-only.lit).
Repeating the exact tuple equality after this call passes, and a following
chain to (4,6) passes. Those results do not make the original bare query
automatically supported. A wrong second coordinate rejects.

The exact chapter07 add formula, with the earlier []→() adaptation and an
isolated name, also passes with native coordinate proof followed by its
definition/result chain:

```litex
have fn r80_add2(u,v cart(R,R)) cart(R,R)=(u(1)+v(1),u(2)+v(2))
release thm tuple_equal_from_coordinates(((1,2)(1)+(3,4)(1),(1,2)(2)+(3,4)(2)),(1+3,2+4))
r80_add2((1,2),(3,4))=((1,2)(1)+(3,4)(1),(1,2)(2)+(3,4)(2))=(1+3,2+4)=(4,6)
```

[Complete add consumer](evidence/round-80-cases/add-native-and-chain.lit).
Replacing that chain by only the function endpoint still misses after the
native call. Wrong output(4,7) rejects. Sub/smul are not reclassified here.

[Round80 receipt](evidence/round-80-2026-10-09.summary.json):10 strict files,
6 accepted/4 Normal rejections, promoted paths rerun after successful current-
source release build on a fixed snapshot. Exact reduction/chapter source hashes
retained. Session66922 on round68 accepted only the native reduced sum call;
cold current files own the direct/control/consumer evidence. This independent
source use follows the gradient coordinate interface in Part114, but does not
establish a new universal rewriting rule. No new bt/canonical/kernel/trust edit.

The old provisional kernel_problem follow-up now concerns the still-missing
direct form, not mathematical uncheckability or a diagnosed missing leaf.
Use the existing native interface for explicit proof. Internal direct-search
cause remains unknown; no mandatory kernel repair is inferred. Historical
round59 observations below retain their original date and scope.

## Source syntax and exact mathematical interfaces

High-school chapter07 defines add/sub/scalar multiplication on cart(R,R), plus
a real dot product and its squared norm. The raw source still uses u[1]/u[2].
Current parser rejects that removed notation; ordinary application u(1)/u(2)
is the admitted coordinate spelling. This card preserves all carriers and
coordinate mathematics while explicitly adapting that syntax in isolated files.
No canonical chapter or AST shape is modified. Raw failure retained separately.

## Positive: dot symmetry and scalar numbers directly check

The adapted source's full add/dot symmetry chains pass. Dot symmetry alone
passes independently with just the definitions:

```litex
forall u,v cart(R,R):
    r59_dot2(u,v)=r59_dot2(v,u)
```

The actual numeric scalar endpoints also pass:

```litex
r59_dot2((1,2),(3,4))=11
r59_norm2_sq((3,4))=25
```

[Dot symmetry](evidence/round-59-cases/dot-symmetry-direct.lit),
[scalar numeric endpoints](evidence/round-59-cases/scalar-numeric-directs.lit).
They remove intermediate equalities from existing one-statement calculations,
not statements. The adapted numeric source file as a whole fails on its three
tuple-returning calls even though its dot/norm statements succeed; do not call
that partially successful file accepted.

## Add symmetry: retain the source chain

The bare add-symmetry endpoint misses. This same-target claim body passes:

```litex
r59_add2(u,v)=(u(1)+v(1),u(2)+v(2))=(v(1)+u(1),v(2)+u(2))=r59_add2(v,u)
```

[Complete one-chain claim](evidence/round-59-cases/add-symmetry-claim-chain.lit).
Publishing only the two function values does not close the claim's endpoint.
A generator initially split at the goal indentation and accidentally changed
that candidate's target; its result was excluded, target corrected and cold
rechecked. The corrected local-values variant fails. This is an author fixture
correction, not acceptance of add symmetry by that two-value candidate.

## Remaining tuple numeric comparison boundary

Bare add/sub/smul numeric outputs and their explicit definition/projection
chains miss. A structured add-chain test first fails this adjacent equality:

```litex
((1,2)(1)+(3,4)(1),(1,2)(2)+(3,4)(2))=(1+3,2+4)
```

All four coordinate value facts pass. Publishing them still does not make
this tuple substitution pass. Both scalar coordinate-sum equations pass with
those facts, and (1+3,2+4)=(4,6) passes independently. The same reduced tuple
failure occurs without any vector function declaration.
[Minimal reproduction](evidence/round-59-cases/minimal-tuple-coordinate-sums.lit).
This isolates a composite consumer boundary; internal cause and repair scope
remain undetermined. Sub/smul first-link causality is not inferred from their
overall misses. Source-owned follow-up is recorded in
[high-school todo](../../../references/sources.md#unbundled-local-material).
Investigate tuple equality's child comparison and publication permissions before
choosing a rule; a present scalar leaf is not proof of its reachability here.
No permanent multi-line coordinate-echo style is taught from this blocker.

## Negative controls, evidence and scope

Wrong add/dot/norm values and sub-symmetry reject. Wrong add tuple(4,7) also
rejects after coordinate publications. These are separate from the true tuple
misses above. Parallel/perpendicular predicates and witnesses are not included.

[Round59 receipt](evidence/round-59-2026-10-09.summary.json):22 files,6 accepted,
15 Normal rejections,1 raw syntax error; all promoted paths rerun on the fixed
fresh release snapshot. The corrected five-definition prefix passed cold.
Raw source sent to old Session99217 caused its parse exit; fresh Session6037
loaded the corrected prefix on the round59 snapshot and remains live. Literal
journal, prefix gate, source hash, migration note and build log retained.
No canonical scripts/compiler/kernel/protected-owner/trust or whole-chapter
change. The source-workspace todo preserves prior whole-book claims as historical
rather than attributing them to this isolated current gate. Next inspect actual
parallel/perpendicular predicates and witness consumers with their local definitions.
