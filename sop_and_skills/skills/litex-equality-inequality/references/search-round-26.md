# Search round 26 — known equality links versus implicit definition lookup

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


15 independent strict files: 10 accepted, 5 rejected. Fresh current-source
release build succeeded; all early previous-snapshot outcomes were rechecked
on the new immutable binary. Original restriction declarations are unchanged.

## Existing support: no new transitivity rule

Opaque object equality, arbitrary-carrier function application equality,
reversed source equalities and mixed-domain application equalities all compose
directly when their two links are supplied. Missing a link, changing the input
point or dropping the result's function alias rejects a false conclusion.

## Refined recommendation

The generic restriction alias target is repaired by one statement:

```litex
\restricted<X,Y,f,K>(p)=f(p)
```

The original result=restricted premise then suffices to close result(p)=f(p).
Stating only result(p)=restricted(p) does not repair it. Exporting both links
and then the target works; supplying both as premises also works. Therefore
do not nominate duplicate equality transitivity or generic head congruence.
Inspect bounded lookup/consumption of the checked definition result through
the function alias. [Part 67](part-67-restriction-definition-link.md).

## Evidence and boundaries

The exact same original premises are retained by the one-statement author;
links added as assumptions are diagnostic capability controls only. No carrier
was changed to R and no domain premise manufactured. Real-valued behavior
from Round 25 remains a contrast rather than a repair of the arbitrary carrier.

[Receipt](evidence/round-26-2026-10-09.summary.json), complete `evidence/round-26-cases/`
and release build log. The new binary was adopted deliberately with accepted
source replay. Warm Session outcomes do not determine cold support. No canonical
or kernel edits, trust, whole-showcase or performance claims.
Next: source-defined preimage/set-builder consumers in the same topology
showcase, including direct membership, introduction and subset guards.
