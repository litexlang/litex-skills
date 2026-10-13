# Search round 33 — native scalar interval-intersection formulations

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


Keep the exact legacy finite-wrapper failure from rounds30–32, then test the
same source mathematics in native scalar max/min form. Original hypotheses,
endpoint prop and shortened source dependency remain. No new distinctness,
finite or nonempty assumption is introduced.

Native spelling removes the earlier wrapper WD failure, but direct scalar
bounds still miss. Two theorem calls and two checked diagonal chains provide
a four-line proof. Both bare and release call spellings pass. Deleting either
chain or the second source call fails cold. The following closed-hull theorem
passes with one call to that checked dependency; its bodyless version fails.
The original long native hull body also passes, so its echoes can be deleted.

[Part73](part-73-native-interval-intersection-bounds.md) records the positive
and negative routes. [Receipt](evidence/round-33-2026-10-09.summary.json): 25 unique
strict files,8 accepted/17 rejected; exact adaptation, source identity and
immutable binary commands retained, promoted copies rechecked. Three initial
hull files have failed dependencies and must not be counted as independent hull
proof misses. Warm Session after scalar lemma publication can accept some
deletions that fail cold. No source or kernel mutation/trust, complete legacy
expression repair, whole-book or performance claim.

Next held-out work: actual min/max bound and magnitude consumers in maintained
examples/showcases/textbooks, checking direct support and whether the same
coordinate-to-scalar bridge recurs. Full search goal remains active.
