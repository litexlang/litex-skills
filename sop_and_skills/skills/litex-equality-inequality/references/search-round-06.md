# Search round 6 — Quadratic certificates and zero consequences

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


Current working-tree release build succeeded on 2026-10-08. 38 isolated strict
file probes with sources, failed shorter routes and controls retained.
No kernel or canonical mathematical source edits.

## Recommended rule improvements

1. Nonpositive real square to zero base: a^2<=0 should imply a=0 directly.
   Direct misses; contradiction against a nonzero base's positive square
   passes. Preserve the real-base guard, not merely a real-square guard;
   i^2=-1 is the mathematical complex counterexample. Both a^2>=0 implies
   a=0 and the complex nonpositive-square implication were run and rejected.
   [Part 20](part-20-nonpositive-square.md).
2. Nonnegative zero-sum component consumption: a,b>=0 and a+b=0 should imply
   a=b=0. Direct misses; two subtraction-bound chains pass. Two real squares
   summing to zero already work directly, but three do not; a grouped proof
   passes. Prefer structural/general consumption over a rule per number of
   squares. [Part 21](part-21-nonnegative-zero-sum.md).
3. Zero squared difference to endpoint equality: (a-b)^2=0 should imply a=b.
   Direct misses; publishing a-b=0 makes the claim pass. This fixed target-
   driven bridge is more general than bespoke AM-GM/Cauchy equality rules.
   [Part 22](part-22-zero-square-difference.md).

## Current authoring improvement, not mandatory new bt

Cauchy–Schwarz in 2D, weighted Young, and squared-sum estimates all have
checked one-chain certificate proofs when 0<=certificate=upper-lower is
written in the consumed orientation. Their bare targets miss, but the earlier
two-statement certificate plus reversed sign echo can be replaced by one
statement. Do not claim an unrestricted polynomial certificate search.
[Part 19](part-19-quadratic-certificates.md).

Existing square-zero, two-square-zero, zero-product with a nonzero factor, and
real-order antisymmetry all pass directly. Do not propose duplicate rules for
those surfaces. Failed alternate contradiction routes are kept as attempt
evidence; they do not establish a general rejection of contradiction proofs.

## Coverage and next work

Anchors: Manual R12/R13; coordinate geometry dot/determinant identity,
squared-distance positivity, and equality-case calculations. Reduced scalar
probes were verified, not enclosing geometry modules or downstream callers.
No runtime improvement or source-level line savings in canonical files claimed.

Next: integer floor/ceil/mod comparison families in number-theory and concrete-
mathematics examples, checking existing rules and type/refinement boundaries
before proposing more bt. Corpus queue remains unfinished.

Evidence: [receipt](evidence/round-06-2026-10-08.summary.json),
[build log](../../../references/sources.md#unbundled-local-material). Twenty-two dated skill parts exist.
