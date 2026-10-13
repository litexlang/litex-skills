# Search round 20 — recurrence algebra and product association

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


16 independent strict probes: 7 accepted, 9 rejected. All sixteen were replayed
on resumption with the original immutable snapshot and retained their outcomes.
Rejections include true misses, mathematical controls and failed shortening
variants. The original source build succeeded; the resumed current-worktree
build is blocked by unrelated concurrent Lean compiler edits. These are dated
snapshot observations, not assertions about the current worktree binary.

## Recommendations

- Inspect bounded product reassociation before consuming an established equality:
  `a*b=c => a*(b*d)=c*d` misses, while `(a*b)*d=c*d` and the one-chain author
  `a*(b*d)=(a*b)*d=c*d` pass. [Part 58](part-58-associated-product-evidence.md).
- The corresponding weak comparison has the same tested association bridge
  under `d>=0`. Do not infer order preservation for `d<0`.
- First simplify source recurrence proofs using existing congruence and a
  meaningful calculation chain. The generic equality-congruence helper is
  removable, and a five-statement body passes; tested three/four-statement and
  previous-definition-deletion variants miss. [Part 59](part-59-summation-factor-algebra.md).
  Do not add a rule recognizing source-specific recurrence function names.

Normal statement text flattens `a*(b*d)` and `(a*b)*d` alike in these receipts.
The literal input sources distinguish the tested grouping. This is a diagnostic
observation, not proof that semantic grouping is discarded internally.

[Receipt](evidence/round-20-2026-10-09.summary.json) retains exact original sources,
commands, Normal envelopes, same-Session repairs, excluded reserved-name
authoring error and source-build identity. Runnable files are in
`evidence/round-20-cases/`. No canonical chapter or kernel was changed by this
search. No trust, full-module, global-minimality or runtime-improvement claim.
Next: native finite-product singleton/append reuse and source empty-product
wrapper consumers from Concrete Mathematics Chapter 2.
