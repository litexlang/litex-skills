# Part 64 — Expose a coordinate template result with one chain

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Exact source context

linear_algebra_done_right Chapter 1A defines coordinate_add and coordinate_smul
as templates over a nonempty scalar carrier, an actual ScalarSystem value and
a positive dimension. Each returns a finite sequence represented by a pointwise
callback. The exact source definitions and named original addition theorem are
in [the original probe](evidence/round-24-cases/coordinate-add-exact-original-thm.lit).
No alternative scalar laws or strengthened premises were introduced.

## Before and checked shorter body

The original addition proof has these two statements:

```litex
\coordinate_add<s,scalars,n> = fn(u,w finite_seq(s,n)) finite_seq(s,n) {fn(k closed_range(1,n)) s {scalars.add(u(k),w(k))}}
result=\coordinate_add<s,scalars,n>(x,y)=fn(k closed_range(1,n)) s {scalars.add(x(k),y(k))}
```

The first statement is removable in the isolated exact interface. The second
alone proves the original entry target under its unchanged result equation and
idx N+, idx<=n guards. Scalar multiplication has the same one-chain shortening.

The [complete shortened addition probe](evidence/round-24-cases/coordinate-add-no-template-equality.lit)
and [scalar probe](evidence/round-24-cases/coordinate-smul-no-template-equality.lit)
pass independently. This does not yet establish chapter/caller deletion safety.

## Negative shortening and current capability boundary

The zero-body claim and direct forall both miss. A template-function equality
alone misses. Replacing the chain by either just `result=literal_callback` or
just `template_call=literal_callback` also misses. The intermediate template
call therefore matters in the checked variants; it is not a mathematical
extra assumption or a globally minimal proof claim.

If the result premise itself supplies the literal callback, the original
ScalarSystem field entry passes directly. Thus the nomination is consumption
of the instantiated function return definition through an alias, rather than
a duplicate field/callback beta rule. Preserve inherited permissions, actual
definition/alias citations, index bounds and all field/argument WD.

## Mathematical and domain controls

Missing idx<=n rejects even with the accepted chain. For idx>n the finite
sequence application is outside its domain. Changing the addition result to
x(idx), or the scalar result to multiplication by scalars.zero, is false for
ordinary real scalar systems and rejects. Do not manufacture index or zero
conditions to shorten the source statement.

## Evidence

[Round 24](search-round-24.md) records 24 unique-source strict files and the
complete live transcript. Warm shorter successes inherit previously proved
claims and are not cold capability evidence. Original theorem statements and
definitions were preserved in dedicated probes; canonical chapter code was
not edited. Current release snapshot/build identity is retained; no whole-book
or runtime-improvement claim.
