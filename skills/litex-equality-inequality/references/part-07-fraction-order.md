# Part 7 — Compare fractions by cross multiplication

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

For individually positive denominators b,d, a/b<=c/d is equivalent to
a*d<=c*b. The product b*d has positive sign. Both negative denominators also
give a positive product; mere nonzeroness does not control direction.
Anchor: Manual R14. These are isolated scalar probes, not whole-chapter edits.

## Positive — explicit routes

```litex
claim:
    ? forall a,b,c,d R:
        0 < b
        0 < d
        a/b <= c/d
        =>:
            a*d <= c*b
    (a/b)*b <= (c/d)*b
    a*d = ((a/b)*b)*d <= ((c/d)*b)*d = c*b
claim:
    ? forall a,b,c,d R:
        0 < b
        0 < d
        a*d <= c*b
        =>:
            a/b <= c/d
    0 < b*d
    a/b = (a*d)/(b*d) <= (c*b)/(b*d) = c/d
```
Both pass; the two-step route with b<0,d<0 also passes.

## Ideal form, negatives and candidate

Direct cross and uncross targets under positive denominators miss. Direct
cross multiplication under both negative denominators also misses.
Propose a bounded cross-multiplication order rule guarded by the denominator
product sign, preserving denominator WD. Match the fraction structure, not
arbitrary new algebraic intermediates. Opposite signs require the reversed
direction; that correct variant has not been tested in this round.

The unsigned direct variant with only b!=0,d!=0 is false and rejects:
a=1,b=-1,c=1,d=1 gives -1<=1 but 1<=-1 after incorrect cross multiplication.
Nonzeroness is necessary for division but insufficient for preserving order.

## Evidence

[Round 3 receipt](evidence/round-03-2026-10-08.summary.json), `fraction-*`, strict
clean files; current working-tree release built successfully on 2026-10-08.
No new rule, performance claim or caller simplification implemented.
