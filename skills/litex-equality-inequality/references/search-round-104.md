# Round104 — actual textbook sign-to-nonzero bridge

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


Chapter 2 §2.2's first nonzero claim shrinks to its mixed equality/order
calculation alone; its second shrinks to `0<y^2+1` alone. Both pass together
with the source's direct equality-from-two-inequalities example.

Independent generic and source-derived controls show strict sign⇒nonzero
works once the sign fact is supplied. `0<y^2+1` passes as a direct query,
while direct `y^2+1!=0` rejects; likewise under `a>=0,b>0`, direct `a+b>0`
passes and direct `a+b!=0` rejects, but sign then nonzero passes. This is a
small surface proof-search boundary, not a proposed or implemented bt.

[Part131](part-131-textbook-positive-to-nonzero.md),
[receipt](evidence/round-104-2026-10-10.summary.json),
[combined short source](evidence/round-104-cases/both-short.lit).
20 promoted strict Normal files:12 accepted/8 rejections. Exact source and
fixed binary hashes recorded, promoted reruns matched. No canonical edits.
