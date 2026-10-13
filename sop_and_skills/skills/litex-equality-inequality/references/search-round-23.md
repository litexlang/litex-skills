# Search round 23 — pointwise coordinate interfaces on a fresh release

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


29 independent strict files: 15 accepted, 14 rejected. Source anchor:
linear_algebra_done_right Chapter 1A coordinate_add/coordinate_smul callbacks.
The round checks real pointwise specializations and generic supplied-operation
entry interfaces; it does not run the original ScalarSystem/template theorem
or a registered chapter.

## Existing support: avoid duplicate entry rules

Anonymous pointwise addition and scalar-combination beta endpoints pass.
Legal finite-index applications and the matching `finite_seq(R,n)` carrier
pass. A result alias for the pointwise callback directly supplies its entry:

```litex
forall n N+,u,v,result finite_seq(R,n),idx closed_range(1,n):
    result=fn(k closed_range(1,n)) R {u(k)+v(k)}
    =>:
        result(idx)=u(idx)+v(idx)
```

The analogous supplied operation on an arbitrary nonempty carrier also passes.
No second beta/finite-sequence-entry rule is nominated. Original struct-field
and template unfolding are separate consumers and were not checked here.
[Part 63](part-63-pointwise-coordinate-interfaces.md).

## Recommendations and mathematical proof ownership

- Retain Part 62's bounded anonymous-atom/equality consumer investigation:
  pointwise anonymous calls still miss under multiplication/scaling, even with
  their beta value stated. Checked generic scalar theorem invocation repairs
  the same scaled or commutative target. No additional kernel rule was added.
- Whole pointwise function equalities for addition commutativity and scalar
  association miss directly but pass with `by fn_extension` and one pointwise
  chain. This is a meaningful mathematical route, not a reason to recognize
  coordinate function names in the kernel.
- Index zero, wrong sequence length, changed captured function/coefficient and
  changed full function domain remain rejected. Preserve these boundaries when
  considering any binder-aware normalization.

## Current-source revalidation

The previously blocked worktree now builds. All 25 round-22 files were rerun
on a fresh current-source binary with identical outcomes. All 29 round-23 files
were independently checked on immutable current-release snapshots. A deliberate
source-correspondence rebuild also succeeded and its binary retained the same
29 outcomes. Five source files changed across that build window, so an exact
immutable-checkout correspondence is not claimed; file hashes and changed
paths are preserved, rather than silently calling them unchanged.

The nine accepted early round-23 statements were replayed when adopting the
new executable, along with the retained round-22 prefix. Warm Session successes
are not cold capability evidence: some inherit diagnostic theorem interfaces.

[Receipt](evidence/round-23-2026-10-09.summary.json), complete `evidence/round-23-cases/`,
build logs and [round-22 current recheck](evidence/round-22-current-recheck-2026-10-09.summary.json).
No canonical mathematical or kernel edits, new trust, whole-chapter or runtime
claim. Next: original coordinate template/field consumers, separating literal
callback support from declaration-owned definition unfolding.
