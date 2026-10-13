# Part 68 — Consume a preimage definition equality and known membership

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source and mathematics

The topology showcase defines inverse_image by a typed set builder. A member
has both the source carrier and the predicate f(p) in U; conversely, a legal
source point satisfying that predicate belongs to the builder. The exact
declaration is retained in all round-27 sources.

## Shortened same-premise value proof

```litex
claim:
    ? forall X,Y set,f fn(x X) Y,U power_set(Y),p X:
        p $in \inverse_image<X,Y,f,U>
        =>:
            f(p) $in U
    \inverse_image<X,Y,f,U> = {x X: f(x) $in U}
    p $in \inverse_image<X,Y,f,U>
```

This passes cold. The original additionally repeats f(p) in U; that final line
is removable. Deleting either retained statement misses. Replacing the member
statement with p in the literal builder also misses in the tested variants.
Do not interpret mathematically redundant replay as permanent authoring style.

## Introduction and already-supported interfaces

```litex
claim:
    ? forall X,Y set,f fn(x X) Y,U power_set(Y),p X:
        f(p) $in U
        =>:
            p $in \inverse_image<X,Y,f,U>
    \inverse_image<X,Y,f,U> = {x X: f(x) $in U}
```

One definition equation suffices here. Direct source-carrier, subset and
powerset statements already pass. Literal builder introduction and condition
extraction also pass directly. The gap is joint consumption of the named set's
checked equality and existing membership, not a missing builder primitive.

## Additional alias and nomination

For E=the preimage, member introduction passes after one
E=template=builder chain. Body extraction passes with that chain followed by
p in E, or with the template definition followed by p in the template. Those
complete checked variants are in the receipt.

Inspect a bounded consumer of actual set equality/member evidence, with
capture-preserving binder instantiation and unchanged domain/WD obligations.
No global inference replay, new Env indexes, arbitrary predicate search or
template-name rule is justified by these cases. Implementation cause and a
checked kernel repair remain unproved.

## Nearest negatives and scope

A member of f's preimage need not map into U under unrelated g. A legal source
point without preimage membership need not map into U. A point declared only
in Y cannot automatically be applied to f on X. All corresponding controls
reject. Preserve the source's arbitrary sets and supplied function signature.

[Round 27 receipt](evidence/round-27-2026-10-09.summary.json) retains exact original,
shortened, deletion and negative sources with cold strict envelopes. No
canonical module/kernel edit, trust, complete showcase or speed claim.

## Refined chronology follow-up

Round 28 shows plain aliases do work when the builder equality precedes the
member fact. Reversing those same premises misses, and member replay repairs
it; functional predicates show the same distinction. Therefore the nomination
must not become a blanket claim that set aliases lack support. See
[Part 69](part-69-set-builder-fact-chronology.md) for the bounded consumer and
read-only membership-projection evidence; no kernel repair was implemented.
