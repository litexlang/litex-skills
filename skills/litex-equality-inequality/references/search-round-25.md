# Search round 25 — composition, restriction and generic aliases

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


29 independent strict files: 20 accepted, 9 rejected. The exact composition
and restricted templates and original type/value theorem bodies were extracted
from showcases/math_concepts_in_litex/9_topology/main.lit. Current release build
succeeded; an immutable executable and source excerpt hash are recorded.

## Existing support: substantial source shortening

Composition/restriction function-space membership and direct application
equations pass on the original arbitrary-set domains. In particular, the
original five-statement restriction_value proof can become the direct fact:

```litex
forall X,Y set,f fn(x X) Y,K power_set(X),p K:
    \restricted<X,Y,f,K>(p)=f(p)
```

The two type theorem bodies invoking fn_set_member are also unnecessary in
these isolated interfaces. No duplicate membership, composition or restriction
evaluation rule is proposed. [Part 65](part-65-composition-restriction-reuse.md).

## Narrower consumer recommendations

- Generic restriction through a result alias still misses, while the immediate
  head-congruence equation passes. One application chain
  `result(p)=\restricted<X,Y,f,K>(p)=f(p)` repairs the exact target. Composition
  aliases and real-valued restriction aliases already pass. Inspect this
  generic carrier/definition consumer before proposing broad alias machinery.
- Empty restriction function-space membership passes, but its bare empty-graph
  identity misses. Naming it with the already checked empty-domain function
  type repairs the same identity. Do not duplicate the existing named empty
  function graph law. [Part 66](part-66-restriction-alias-consumers.md).

Neither adding nor explicitly stating p in X repairs the generic alias target;
the checked p in X line itself succeeds and the final equality misses. The
empty literal callback chain fails at the template-to-literal equality. These
observations keep the first failed facts separate from speculative causes.

## Boundary and evidence

Wrong composition order, missing restriction membership and calls outside an
empty domain reject. Full-domain restriction equality is checkable with one
explicit by fn_extension proof. Full function equality and point application
are not interchangeable default capabilities.

[Receipt](evidence/round-25-2026-10-09.summary.json), complete `evidence/round-25-cases/`
and source build log. An authoring parse error (`>=` instead of separate
template closing `>` and equality `=`) was excluded; the Session restarted
with ten accepted statements replayed. The shortened reference spelling in
Part 64 was corrected to retain required whitespace as well.

No canonical/kernel edits, new trust, whole-showcase or runtime claim. Next:
generic equality consumers after two checked function-application links,
comparing numeric and arbitrary carriers without weakening the original target.
