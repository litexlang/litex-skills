# Part 93 — Actual textbook log interfaces: concise support and bounded bridges

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source and preserved mathematics

High-school chapter03 states product/quotient and positive-real-power log laws,
base-dependent monotonicity, log(a,b)=c iff a^c=b, and two numerical chains.
Retain positive bases/arguments, base!=1 where stated, side-of-one monotonicity
guards and unrestricted real c in the equation interface. No base or exponent
domain was weakened to make a proof pass.

## Already concise support and numeric endpoints

The source product/quotient and positive-real-power identities pass directly.
For0<a<1, x<y gives log(a,x)>log(a,y) directly. Do not expand these working
interfaces into proof waterfalls or propose duplicate mathematical rules.
Both source numeric chains pass, and their direct endpoints pass independently:

```litex
log(2,8*4)=5
log(4,64)=3
```

These shorten equality chains, not statement counts: the original examples are
already one statement each, with three/four adjacent equality checks. The direct
forms have one adjacent equality each. No theorem/dependency prefix is needed.
[Product endpoint](evidence/round-53-cases/numeric-product-direct.lit),
[base endpoint](evidence/round-53-cases/numeric-base-direct.lit).

## Increasing base: observed orientation boundary

The exact source a>1,x<y=>log(a,x)<log(a,y) misses cold, while the mathematically
equivalent guard1<a passes. Preserve the original theorem using this tested
explicit two-step body:

```litex
1<a
log(a,x)<log(a,y)
```

[Full original-guard claim](evidence/round-53-cases/increasing-original-guard-bridge.lit).
This is a current expression/matching boundary, with internal cause undetermined;
it is not evidence that increasing log mathematics is absent. Do not teach a
permanent global preference for one guard spelling or insert a new premise.
A separate ln quotient route missed first at log(a,x)=ln(x)/ln(a); its later
fraction inequality was not the first failure and is not classified from it.

## Equation/power equivalence and actual combined consumer

The isolated original conditional iff misses. Its forward implication is
checkable by one chain, retaining a,b in R+,c in R,a!=1 and log(a,b)=c:

```litex
a^c=a^log(a,b)=b
```

The reverse implication is also checkable with the original domains and premise
a^c=b; this tested two-statement route works:

```litex
log(a,a)=1
log(a,b)=log(a,a^c)=c*log(a,a)=c
```

Without log(a,a)=1, that explicit reverse chain fails its final adjacent equality
c*log(a,a)=c; the substitution and power-log links before it pass.

[Forward proof followed by the original iff](evidence/round-53-cases/equivalence-forward-only.lit)
passes independently. A prefix containing both direction proofs also passes;
the reverse proof alone followed by iff misses. These are observed composition
outcomes, not a claim about which internal iff branch failed in the bare source.
No extra public named helper or changed mathematical equivalence is required.

## False/domain controls and composition safeguard

The small-base increasing direction is false and rejects. Wrong numeric6 for
log(4,64), base1 and argument0 reject; missing base!=1 leaves the product-law
domain unproved. Do not treat invalid logarithms as true proof-search misses.
A false conditional iff u=v iff u^2=v^2 rejects both alone and after the true
forward implication is published; its tautological0=0 guard only uses the same
conditional iff syntax. Values u=1,v=-1 refute the reverse direction. The
forward prefix itself passes, so this is a genuine one-way-versus-iff control,
not failure of its dependency. Success for the log iff does not establish a
blanket conversion of implications into equivalences.

## Evidence and next source family

[Round53 receipt](evidence/round-53-2026-10-09.summary.json):25 independent strict files,
13 accepted/12 rejected; all promoted paths rerun with the fixed current-source
release snapshot. Source hash, build and literal warm journal retained.
Session99217 remains live and ordinary misses retain its accepted context.
No canonical scripts/kernel/protected-owner/trust, whole-chapter or performance
change. Next inspect chapter05 trigonometric identities and numeric degree/
cosine-law consumers, preserving singularity guards and all exported identities.
