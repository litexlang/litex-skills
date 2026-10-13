# Part 100 — Plane-vector perpendicularity and a named parallel witness

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and source

Actual high-school chapter07 defines perpendicularity by a zero dot product
and parallel2(u,v) by u=k*v. Preserve these exact local definitions and
cart(R,R) carriers. As in Part99, the isolated probes adapt removed []
coordinate syntax to ordinary application (). No canonical chapter is edited.

```litex
have fn r60_dot2(u,v cart(R,R)) R = u(1)*v(1)+u(2)*v(2)

prop r60_parallel2(u,v cart(R,R)):
    exist k R st {u(1)=k*v(1),u(2)=k*v(2)}

prop r60_perpendicular2(u,v cart(R,R)):
    r60_dot2(u,v)=0
```

The mathematical moves are definition folding for the zero dot product and
the scalar witness 2 for (2,4)=2*(1,2). They do not require new axioms or bt rules.

## Checked short positives

```litex
by def $r60_perpendicular2((1,0),(0,1))
```

An explicit preceding dot-product equality is removable: this line alone
passes after the declarations. The bare predicate assertion misses.
[Complete positive](evidence/round-60-cases/perpendicular-by-def.lit).

```litex
(1,2)(1)=1
(1,2)(2)=2
witness $r60_parallel2((2,4),(1,2)) from 2
```

[Complete named witness](evidence/round-60-cases/parallel-second-coordinates-only.lit).
Publishing both vectors' four coordinate values also passes, but both first
vector values can be removed together. Deleting either second-vector value
from the four-value version fails at witness_atomic. This is scoped liveness
evidence, not a universal obligation to publish coordinates before witnesses.

## Verbose comparison and direct misses

After all four coordinate values, explicitly witnessing the expanded
existential and then folding by definition passes. Named witness replaces
that two-action route without repeating the predicate. The adapted source's
expanded witness without coordinate facts fails; adding coordinates makes
the existential pass, but its following bare predicate still misses at
search_proof. Coordinate publication followed only by a bare predicate also
misses. Warm stored predicates do not own any of these deletion conclusions.
[Expanded accepted route](evidence/round-60-cases/parallel-coordinates-exist-and-fold.lit),
[expanded witness plus bare predicate](evidence/round-60-cases/parallel-coordinates-exist-and-bare.lit).

## Mathematical negatives and zero-vector boundary

```litex
# Rejected with the same declarations:
by def $r60_perpendicular2((1,0),(1,0))
```

The explicit fold rejects a dot product of 1. In a separate file, the short
parallel route with witness 3 also rejects after both second-vector values.
[False perpendicularity](evidence/round-60-cases/false-perpendicular-by-def.lit),
[wrong witness](evidence/round-60-cases/parallel-second-coordinates-wrong-witness.lit).

The source relation allows a zero first vector: the two second-vector values
and `witness $r60_parallel2((0,0),(1,2)) from 0` pass. A nonzero first vector
with zero second vector is mathematically false and its bare assertion
rejects, although bare rejection alone does not isolate that mathematical
reason. Do not infer symmetry in the zero-vector case or strengthen the
source definition with nonzero assumptions.
[Zero witness](evidence/round-60-cases/zero-first-second-coordinates-only.lit).

## Evidence and improvement boundary

[Receipt](evidence/round-60-2026-10-09.summary.json): 27 independent strict cold files,
9 accepted and 18 Normal rejections, all promoted paths rerun with the fixed
round60 release snapshot. Build succeeded; source and binary hashes retained.
Session6037 stayed live across an ordinary false-fold rejection; its literal
journal identifies the older round59 snapshot and is not the cold acceptance.
No whole-chapter, imported-interface, global minimality or performance claim.

The nested coordinate multiplication consumer is a bounded investigation
candidate: named witness alone misses while explicit second-vector values
repair it. Internal cause is unknown. No additional bt implementation is
proposed from this single source family; Part99's separate tuple gap remains.
