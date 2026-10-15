# Part 106 — Actual radians and cosine-law calculations: scoped direct endpoints

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source and mathematical situation

The middle-school showcase converts degrees to radians and computes a squared
third side by the cosine law. The exact scalar definitions are retained:

```litex
have fn radians_from_degrees(theta R) R = theta * pi / 180
have fn cosine_law_third_side_sq(a, b, gamma R) R = a^2 + b^2 - 2 * a * b * cos(gamma)
```

These are scalar formulas on R, not geometric triangle objects. Do not add
positivity or angle constraints to make the isolated calculations easier.
The case checks only the source scalar section, not the whole showcase.

## Degrees: shorten 180, retain the checked 60 chain

```litex
radians_from_degrees(180)=pi
radians_from_degrees(60)=60*pi/180=pi/3
```

The source's 180*pi/180 intermediate is removable in the independent 180
file. The bare 60 endpoint misses search_proof; its original chain passes in
the source calculation slice and in the literal warm journal. The combined
two-direct-endpoint file is rejected because its 60 statement fails, even
though its 180 statement passes.
[Direct 180](evidence/round-66-cases/radians-180-direct.lit),
[bare 60 miss](evidence/round-66-cases/radians-60-direct.lit),
[source calculation slice](evidence/round-66-cases/source-calculations.lit).
This is not evidence that arbitrary degree inputs can omit unfolding.

## Right-angle cosine law: retain the useful bridges

```litex
cos(pi/2)=0
cosine_law_third_side_sq(3,4,pi/2)=3^2+4^2-2*3*4*cos(pi/2)=25
cosine_law_third_side_sq(5,12,pi/2)=5^2+12^2-2*5*12*cos(pi/2)=169
```

[Complete accepted route](evidence/round-66-cases/cosine-chains-with-cos.lit).
The degree calculations can be removed from this slice; the first triangle
alone with the cosine fact also passes. Bare numeric function endpoints miss
even with cos(pi/2)=0 published. Keeping the original chains but deleting the
cosine fact also misses. The expanded scalar expression itself misses without
that fact. Distinguish this scalar boundary from the outer named-function
endpoint boundary; their internal causes are not established here.

The symbolic right-angle identity on arbitrary real a,b and the numeric
pi/3 target with value13 also miss in their direct probes. Both are true
formulas, not mathematical negatives. No rule addition is inferred from these
observations; preserve the checked source route while investigating if needed.

## Negatives and evidence

Wrong 60-degree value pi/2 rejects. Wrong right-triangle result24 rejects,
including with the same cosine fact and full formula chain that accepts25.
The purported identity cosine_law_third_side_sq(a,b,gamma)=a^2+b^2 for all
real gamma rejects; the subtracted cosine term need not vanish.
[Wrong expanded chain](evidence/round-66-cases/cosine-wrong-chain-with-cos.lit).
The rejection of a bare wrong function endpoint alone would not distinguish
mathematical checking from the observed true-endpoint search misses.

[Receipt](evidence/round-66-2026-10-09.summary.json):16 strict files,
4 accepted/12 Normal rejections, all promoted paths rerun on the fixed snapshot
after a successful current-source release build. That build waited on another
process's lock for part of its3m38s; no competing process was stopped and this
is not a proof performance measurement. Exact source hash and logs retained.
Round65 prechecks agreed but do not own current acceptance. Session9174 stays
on round61 and journals failed direct60/false60 and accepted explicit60 chain.
No canonical source, kernel, trust, protected owner or whole-showcase claim.
