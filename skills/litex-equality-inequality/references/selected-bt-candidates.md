# User-Selected Builtin-Rule Candidates

> Imported reference snapshot (2026-10-13). Use [the hub execution contract](../../litex-reference/references/execution.md). Repository conventions apply to the source project; dated examples remain historical until replayed.
> Receipt links contain summaries, not full verifier output. Original hashes, commands, and recorded outcomes remain available; see [evidence packaging](evidence-packaging.md).

This list records the user's selection from six summaries at a paused search
checkpoint and the later implementation checks. The selected rules were
authorized, then round 20 and subsequent searches resumed. Original failure
dates remain historical; later acceptance records determine the listed status.

| No. | Target and premises | User decision |
| --- | --- | --- |
| 1 | `a<=b, c<=d` imply `a-d<=b-c` | Include; [Part 2](part-02-subtraction-order.md). |
| 2 | `k!=0, a*k=b*k` imply `a=b` | Exclude from this selection; retain the historical case. |
| 3 | `v!=0` implies `abs(v)!=0` | Focus on this direction rather than the full absolute quotient identity. Existing evidence already shows a rule; inspect its denominator-WD consumer instead of proposing a duplicate. See [Part 9](part-09-absolute-quotient.md) and [Part 47](part-47-magnitude-nonzero.md). |
| 4 | `r>=0, x^2<=r^2` imply `abs(x)<=r` | Include; [Part 42](part-42-absolute-square-radius.md). |
| 5 | `b>0, a<=M*b` imply `a/b<=M` | Include; the user clarified that this meant implementing a builtin rule. |
| 6 | Integer `a,b`, `b!=0, a%b=0` imply `a/b $in Z` | Include; the user clarified that this meant implementing a builtin rule. |

For item 3, explicit `abs(v)!=0` acceptance does not prove every nested
denominator context can omit the bridge. The historical record did not locate
all WD consumer gaps. The reverse implication `abs(v)!=0 => v!=0` is a separate
direction and was not part of this selection.

Implementation record, 2026-10-09: items 1, 4, 5 (including its strict form),
and 6 entered the kernel source. An isolated matching-source copy passed 36
Rust tests and six strict release examples. Item 3 and its `u/abs(v) $in R`
consumer passed with existing support. Unrelated concurrent Lean compiler
changes initially prevented a worktree build, so integration was incomplete.
See `tests/unit/execute/selected_scalar_bt_rules/acceptance.md` in golitex.
Isolated acceptance did not mean the worktree executable was updated.

Later integration: the worktree built, target/release/litex passed those six
strict files, and the 36 focused Rust tests passed on current source. The
historical build blocker was resolved; see worktree_integration in the paired
acceptance.md / acceptance.json. This adds no Lean or full-repository claim.

Round 36 encountered another build blocker from concurrent Lean changes;
new probes needed independent acceptance. That did not revoke the completed
selected-rule checks or establish a passing round-36 source build.
Parts 2/42/45/56 record the update; do not propose implementing them again from
an older candidate paragraph.
