# Search round 7 — Rounding cells and integer thresholds

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


Current working-tree release built successfully on 2026-10-08. 45 isolated
strict file probes; exact source and Normal outcomes retained. No kernel or
canonical mathematical source edits.

## Principal bt recommendations

1. Floor/ceil cell characterization: integer n and n<=x<n+1 should directly
   give floor(x)=n; n-1<x<=n should give ceil(x)=n. Direct targets miss;
   original explicit integer squeeze proofs pass. Shorter candidates that
   discard typed/weak-bound bridges miss. Preserve integrality and the correct
   half-open endpoint. [Part 23](part-23-rounding-characterization.md).
2. Rounded/real threshold conversion: floor(x)<n implies x<n and n<ceil(x)
   implies n<x for integer n. Weak rounded directions also miss directly and
   have checked explicit routes. Integer gap itself works: this is composition
   at the rounding consumer. [Part 24](part-24-rounding-thresholds.md).

Forward strict directions x<n implies floor(x)<n and n<x implies n<ceil(x)
also miss directly, but their one-chain proofs work for all real thresholds.
Do not impose integrality on forward directions because a converse requires it.

## Existing capability and secondary shape support

Negation, integer translation, weak monotonicity, integer successor gap and
positive-divisor remainder bounds pass directly. They are source-cleanup
opportunities, not new-rule gaps. Integer shifts must not be widened to real
shifts; floor/ceil are not strictly monotone.
[Part 25](part-25-rounding-existing-support.md).

Alternate defining bounds x-1<floor(x), ceil(x)<x+1 miss directly; definition
plus translation passes. Those two fixed orientations are secondary proposals,
not a demand for arbitrary affine inequality normalization.

## Coverage and next work

Anchors: Concrete Mathematics Chapter 3 equations 3.4–3.7; native rounding,
integer-gap and modulo bounds. Reduced proofs verified, not complete chapter
shortening, module-wide success or runtime improvement.

Next: remainder/congruence and divisibility cancellation in Concrete
Mathematics Chapter 4 and number-theory showcases; inspect existing Euclidean
uniqueness, modulo congruence and gcd/native theorem interfaces.
Corpus ranking queue remains unfinished.

Evidence: [receipt](evidence/round-07-2026-10-08.summary.json),
[build log](../../../references/sources.md#unbundled-local-material). Twenty-five dated skill parts exist.
