# Search round 4 — Minimum radii, power signs and logarithms

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


Current working-tree release build succeeded on 2026-10-08. 37 isolated strict
file probes, with exact sources, outcomes and failed shorter attempts retained.
Existing source edits were preserved; no kernel or canonical theorem changes.

## Candidates

1. Nested minimum positivity and bound composition: direct nested R+ binding
   misses; typed inner minimum then outer binding passes. Direct nested upper
   endpoint misses; adjacent-bound chain passes. Scalar and singleton-union
   finite minimum positive-binding variants agree. Prefer bounded structural
   descent, not one rule per nesting length. [Part 10](part-10-minimum-bounds.md).
2. General-base log order reflection: a>1 and log(a,x)<=log(a,y) should imply
   x<=y. Direct misses; contradiction proof passes. Existing ln reflection
   and forward decreasing log order for 0<a<1 pass directly, so no duplicate
   recommendation for those cases. [Part 11](part-11-log-reflection.md).
3. Power parity signs: even natural exponent nonnegativity and odd negative
   base negativity both miss directly, but power-law/square chains pass.
   Arbitrary real 2*t has no parity guarantee. [Part 12](part-12-power-parity.md).
4. Successor integer exponent order: strict growth for a>1 and strict decay
   for 0<a<1 miss directly; one chain through a^n*a passes. Preserve a=1
   strictness and negative-exponent WD boundaries. [Part 13](part-13-power-successor.md).
5. Positive-base real-power strict monotonicity: x>y, q>0 should imply
   x^q>y^q. Direct misses; a complete log/contra proof passes after power R+
   memberships are published. The shorter failures distinguish premise
   consumption from complement/domain evidence. [Part 14](part-14-real-power-order.md).

## Additional boundary observations

Strict lower bound x<min(a,b) from x<a,x<b needs a case proof in the current
probe. Selecting the right minimum from a>b misses unless b<=a is published;
the isolated weak guard passes. Audit guard consumption separately from
adding new mathematical minimum laws.

The real-exponent growth direct target a^u<=a^v for a>=1,u<=v misses. No
explicit route for that general target was accepted in this round; it remains
a capability observation rather than a promoted authoring recipe.

## Coverage and next work

Anchors: Manual R15, Analysis Chapters 6/9/10 power and radius arguments,
existing positive-minimum and exp/ln rule examples. These are isolated
capability probes, not complete chapter cleanup or measured runtime wins.

Next: source repeated strict/weak absolute interval bounds, unit-interval power
bounds, and reciprocal-order envelopes. Continue working through ranked
corpus families; do not equate lexical candidate counts with verified savings.

Evidence: [receipt](evidence/round-04-2026-10-08.summary.json),
[build log](../../../references/sources.md#unbundled-local-material). Fourteen dated skill parts now exist.
