# Part 26 — Equal residues and a zero residue difference

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

For integers a,b and positive integer modulus m,
a%m=b%m iff (a-b)%m=0. One direction distributes subtraction modulo m;
the other reconstructs a from b and an integer multiple of m.
Anchors: Concrete Mathematics Chapter 4 Euclidean identities and native
mod_congruence/euclidean_remainder examples.

## Positive routes and ideal forms

```litex
claim:
    ? forall a,b Z,m N+:
        a%m = b%m
        =>:
            (a-b)%m = 0
    b%m-b%m = 0
    (a-b)%m = (a%m-b%m)%m = (b%m-b%m)%m = 0%m = 0
```
Passes. Without the explicit polynomial-zero bridge, the original chain
misses at (b%m-b%m)%m=0%m. The direct (a-b)%m=0 target also misses.

The reverse direct a%m=b%m misses from (a-b)%m=0. A complete quotient-
reconstruction/distribution proof passes; its exact self-contained source is
the receipt's `mod-zero-difference-implies-equal-bridged` case. Its original
shorter attempt fails before quotient reconstruction is transported to a.

## Negative and candidate

Equal residues do not imply a=b: a=0,b=3,m=3 refutes it and the probe rejects.
Modulus zero is outside modulo WD; signed nonzero moduli were not tested here.

Add a fixed residue/difference equivalence consumer for the tested integer/
positive-modulus domain. Both endpoints and modulus are supplied by the goal,
so no quotient/witness discovery should be required from the author.
Preserve Euclidean domain/evidence and do not conflate congruence with equality.
Arithmetic normalization under modulo is a separate supporting mechanism;
do not turn the current explicit-zero bridge into permanent source style.

## Evidence

[Round 8 receipt](evidence/round-08-2026-10-08.summary.json), valid `mod-equal-*`,
`mod-zero-difference-*` cases. Two accidental goal-changing generated probes
are explicitly excluded, not capability failures; corrected tests preserve
the original target. Current release build, independent strict files, 2026-10-08.
