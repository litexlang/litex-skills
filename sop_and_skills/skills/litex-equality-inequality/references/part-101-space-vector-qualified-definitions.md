# Part 101 — Space-vector scalar endpoints after opening chapter definitions

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Actual source and mathematical situation

Chapter15-space-vectors uses chap09::dot3 and chap09::norm3_sq from
chapter09-solid-geometry-incidence. These functions compute the coordinate dot
product and its self-product. Isolated modules retain the export name chap09,
function names, cart(R,R,R) carriers and qualified consumer expressions.
Only the two scalar definitions are extracted; removed [] indexing becomes ().
This is a checked definition slice, not the complete registered chapter prefix.

```litex
# chap09.lit, exported before main.lit:
have fn dot3(u,v cart(R,R,R)) R = u(1)*v(1)+u(2)*v(2)+u(3)*v(3)
have fn norm3_sq(u cart(R,R,R)) R = dot3(u,u)
```

Each linked case owns a current-format litex.config. The source textbook's
legacy hierarchy entry is not carried into this isolated module. No canonical
config or chapter is edited. Opening definitions is an explicit mathematical
interface action, rather than duplicating the functions locally.

## Short positive and necessary definition actions

```litex
# main.lit:
release obj def chap09::dot3
chap09::dot3((1,2,3),(4,5,6))=32
```

[Dot endpoint](evidence/round-61-cases/dot-only-release/main.lit).
The original `=1*4+2*5+3*6=32` chain also passes after release; its intermediate
calculation is removable in this context. Omitting release fails at FnObj
well_defined with no matching function signature, before numerical comparison.

```litex
release obj def chap09::dot3
release obj def chap09::norm3_sq
chap09::norm3_sq((1,2,2))=9
```

[Norm endpoint](evidence/round-61-cases/norm-numeric-direct-released/main.lit).
The original norm-to-dot-to-sum-to-9 chain passes too. Deleting dot release
while retaining norm release misses search_proof; retaining only dot release
fails the norm call's function-signature check. Keep both actions for this
consumer. These tests do not establish a universal cross-module release recipe.

After both releases, dot symmetry and the defining norm/dot identity pass
directly with universal cart(R,R,R) binders.
[Symmetry](evidence/round-61-cases/dot-symmetry-direct-released/main.lit),
[norm identity](evidence/round-61-cases/norm-definition-direct-released/main.lit).

## Perpendicularity and source comparison

After dot release, the source predicate definition and this action pass:

```litex
prop perpendicular3(u,v cart(R,R,R)):
    chap09::dot3(u,v)=0

by def $perpendicular3((1,0,0),(0,1,0))
```

[Complete fold](evidence/round-61-cases/perpendicular-dot-release-only/main.lit).
The source's explicit zero-dot equality followed by a bare predicate also
passes after releases. A bare predicate without that equality misses.
The one-action fold replaces the two-statement source route here. Unlike the
unreleased original probe, it successfully defines the predicate before use.

## Negatives and misleading alternatives

After both definition releases, wrong dot value 31, wrong norm value 8 and
the false explicit perpendicular fold on ((1,0,0),(1,0,0)) all reject.
[Wrong scalar](evidence/round-61-cases/false-dot-value-released/main.lit),
[wrong norm](evidence/round-61-cases/false-norm-value-released/main.lit),
[false fold](evidence/round-61-cases/false-perpendicular-fold-released/main.lit).
Their unreleased variants fail earlier and are not evidence of mathematical
negative checking. Likewise a failing universal fact's outer search_proof
report does not by itself locate its nested failure.

The attempted chap09::: spelling is rejected as unknown import alias chap09.
Here chap09 is a file export, not an import alias: preserve chap09:: and open
the needed definition. Triple-colon probes are syntax controls, not repairs.

## Receipt and scope

[Round61 receipt](evidence/round-61-2026-10-09.summary.json):40 cold module files,
10 accepted/18 Normal rejections/12 syntax errors. All promoted module paths
rerun on the fixed snapshot of a successful current-source release build.
Source/binary hashes, literal Session and prefix gate are retained. The first
promotion comparison incorrectly required identical parse-error paths after
relocation; the checker was corrected to compare error cause and status while
retaining each actual path. No acceptance changed because of that correction.

Session6037 ended deliberately after saved journals to adopt the new binary;
Session9174 loaded the checked reduced qualified prefix and stayed live across
wrong dot value 31, then accepted norm9 and the perpendicular fold. Cold files
own deletion evidence. No canonical mathematics, kernel, trust, full chapter,
Lean adapter or performance change is claimed. Part99's tuple gap remains.
Next inspect a different source family rather than count these module variants
as independent mathematical discoveries.
