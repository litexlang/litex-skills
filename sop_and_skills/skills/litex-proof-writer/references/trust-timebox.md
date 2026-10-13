# Two-Pass Trust Timebox

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.


Use this workflow to keep one hard proof obligation from blocking a larger
Litex translation or theorem chain.

## What the clock measures

Measure active proof-search time on one unresolved item, statement, theorem,
or substep, including its focused verifier-feedback attempts. Exclude the
initial release build, known long-running file or module gates, and ordinary
waiting for an already-issued verifier command. Three and five minutes are
ceilings, not targets: stop earlier when the decisive blocker is already clear.

## First pass: at most three minutes

1. State the natural mathematical move and try it in the real caller context.
2. Make only the smallest corrections justified by verifier feedback.
3. At three active minutes, preserve the intended theorem and replace only the
   blocked substep with the narrowest legal `trust`.
4. Mark it immediately with this source shape:

```litex
# trust: first-pass timebox; revisit after mainline checkpoint; <missing fact or capability>
trust <smallest blocked fact>
```

5. Record the path, theorem, exact trusted fact, attempted routes, and decisive
   output in the proof-block journal. Do not invent another blocker label.
6. Continue until the intended chain reaches its registered checkpoint. A run
   containing direct trust is not `checkable`.

## Review after the chain runs

Inventory every direct source trust with a source scan and the verifier's trust
summary. Group repeated shapes in prose, such as a missing reusable theorem,
carrier or well-definedness bridge, one-step unfolding boundary,
representation transport, or suspected kernel behavior. Look for one genuine
shared repair before revisiting isolated sites; do not hide repeated trusts
behind wrapper theorems.

## Second pass: at most five minutes per trust

1. Revisit every direct trust one at a time, using its first-pass journal
   evidence instead of restarting the same blind search.
2. If several trusts share a real interface or a small in-scope kernel/library
   repair, test that repair first. Otherwise try the smallest local checked
   replacement.
3. When a trust is discharged, remove its marker, update the journal, and run
   the appropriate registered checkpoint.
4. At five active minutes, stop and hold the second review. Keep the narrow
   trust and create or update the source-owned todo through `$todo-writer`.
   Include the concrete Litex example, exact output, both rounds attempted,
   desired unblock, primary label `trust` or `kernel_problem`, and the
   acceptance command.

After the second pass, report the trusts removed, the recurring mechanisms
learned, and the exact debts deferred. Promote only patterns supported by the
collected sites. Do not begin a third proof-search round unless the user
explicitly expands the budget.
