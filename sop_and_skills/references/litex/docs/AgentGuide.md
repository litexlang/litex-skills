# Litex Agent Guide

> Curated local worktree snapshot (2026-10-13); see [source provenance](../../sources.md). Links to material outside this subset point to its upstream location or an explicitly unbundled source note.


> **Required workflow: when writing or repairing Litex code, open `-session`
> and keep the same live process throughout the iterative loop. Never rerun
> the whole file from the beginning whenever you add a few new lines.**
>
> **An ordinary failed statement does not erase the definitions and facts
> already accepted in that Session. Correct only the failed statement and
> submit it to the same process, then continue from the accepted context.**

Litex builds a mathematical context statement by statement. Reusing that
context preserves both earlier proof work and the cost of loading chapter or
module dependencies. Restarting creates a new context; editing a source file
alone does not update the running process.

Load the accepted prefix once, then submit new statements to that live Session.
Use clean full-file runs for a baseline, coherent checkpoints, and final
verification; they must not replace the Session as the per-candidate loop.

## A short command comparison

These filenames illustrate the workflow; `accepted-prefix.lit` must pass.

```bash
# Wrong per-edit loop: each command starts from the beginning again.
litex -lang en -f solution.lit  # after adding a statement
litex -lang en -f solution.lit  # after repairing it or adding another
```

```bash
# Required loop: load accepted work once and keep this process open.
litex -lang en -f accepted-prefix.lit -session
# Submit each new/corrected statement to this REPL.
```

The example below shows the reason: `a = 3` fails, but the previously
accepted `a = 2` still lets `a + 1 = 3` succeed in that same process.

## See why keeping the Session matters

This short authoring comparison was checked with Litex 1.0.7-beta on
2026-10-14; the surrounding imported reference remains version-specific.
The failure line below summarizes the diagnostic rather than quoting JSON.

Start with one accepted declaration:

```bash
litex -lang en -session -e 'have a R = 2'
```

Submit each statement separately in that same process:

```text
litex> a = 3
... rejected at search_proof; the prompt returns ...
litex> a + 1 = 3
success
```

The failed `a = 3` does not remove the accepted declaration or its fact `a = 2`.
The next statement uses that fact immediately. Do not repeat the declaration
or restart the process for the next attempt.

Compare two independent commands:

```bash
litex -lang en -e 'have a R = 2'
litex -lang en -e 'a + 1 = 3'
```

The first succeeds; the second fails because its fresh process has no `a`.
Load or replay accepted source after an unavoidable restart. Rerunning a whole
file supplies that context again but repeats earlier statements; keep the
live Session for the inner loop.

| After a candidate fails | Next attempt |
| --- | --- |
| Keep the same Session | Earlier accepted definitions and facts are immediately available. |
| Start a fresh process | Reload the module context and replay accepted statements before continuing. |

This example uses no user axiom or trust. It demonstrates context retention,
not a measured speedup or automatic proof discovery. Keep accepted source in
an external journal so an unavoidable restart can recover it.

## Use the Session as the proof-writing loop

1. Understand the intended mathematics and inspect the existing builtin,
   library and module interfaces. Open `-session` and load the required
   accepted context once.
2. Submit one top-level statement at a time to that same live Session, in
   source order. A `claim` or theorem and its entire nested proof form one
   statement. Consume its response
   before sending the next candidate; terminate multiline input with a blank line.
3. On plain-text `success`, journal the accepted source and continue. On an
   ordinary rejection with another `litex>` prompt and no hard termination
   (read the target version's failure envelope),
   keep the process and repair the current statement. Failure is missing proof
   or well-definedness evidence, not proof of the proposition's negation.
4. At a coherent checkpoint or final verification, save the accepted code and
   run a separate clean file gate while keeping the authoring Session open.
   Do not run the whole file again after each new statement or small batch.
   Interactive context is not a substitute for a reproducible file.

**The transaction boundary is the statement, not the entire pasted input.**
A failed statement discards its own tentative parse bindings and execution
state. Successful earlier statements remain. If a frame contains several
top-level statements, its successful statements can commit even when the
frame's overall `success` is false; soft failures do not stop later statements.
Do not assume a whole candidate fragment rolled back, or blindly resubmit names
that already committed. Keep the accepted prefix in a journal outside the live
process so it can be recovered after a restart or interruption.

## Start in the intended context

Use the checked-out version's [CLI contract](cli.md). In a development checkout,
build with `cargo build --release` and use `target/release/litex`.

```bash
target/release/litex -lang en -f accepted-prefix.lit -session
```

`-f` executes its target, including the ordered registered exports through that
target, before entering the REPL. The initial run must succeed; `-session` does
not skip a failing draft file. To work on an unfinished registered file, use a
task-owned scratch module with the exact preceding imports/exports and an
empty target, then submit the target's statements in order. Keep that scratch
configuration outside the canonical module and leave its export order intact.

The current CLI has no `-before`, `-runner`, or `-compact`; do not copy those
historical recipes or introduce a literal `try:` wrapper. The current runtime
already handles each statement's commit/discard boundary.

## Restart deliberately and restore the prefix

Restart when the process exits or cannot accept input, when the loaded module
prefix must change, or when replacing an already committed declaration under
the same name requires a fresh context. A normal proof miss is not a restart
condition. Parsing/tokenization errors and hard session errors can terminate
the REPL; a stopped process cannot retain usable context for the next attempt.

When deliberately adopting a verified rebuilt Litex executable, save the
accepted source first, then restart and replay it. Replacing the binary on
disk does not update the process that is already running. A build or an
ordinary proof miss alone is not a reason to discard the live Session.

Record the error, reopen the intended module context, replay the journal's
accepted statements in order, confirm their success, then retry the pending
statement. Record unexpected session termination in the source-owned blocker
notes. Do not claim that context survives process exit or that any arbitrary
internal error is recoverable in place.

## Verify the saved artifact and find the right reference

Use a clean `target/release/litex -lang en -f <file>` gate. Require exit 0 and
parsed Normal JSON matching the executable, as specified in the
[version-aware execution contract](../../../skills/litex-reference/references/execution.md#acceptance).
Use `-strict` when the intended artifact must exclude user axioms and trust;
the accepted source in the example above passes strict mode. Reserve
`-r` for an explicitly requested whole-module gate. See [CLI output](cli.md#json-output-contract).

| Need | Read |
| --- | --- |
| Language, domains, proof commands and mathematical recipes | [Manual](Manual.md) |
| First-contact authoring choices | [Learner Cheatsheet](Litex_Learner_Cheatsheet.md) |
| Small runnable examples and their assumptions | [Examples](https://github.com/litexlang/golitex/blob/e6f0fb6cab0bb69f99eb9a33b30deceae6d0a74a/examples/README.md) |
| Module interfaces and chapter dependencies | The owning module's `README.md`, `math_collections.md`, and `litex.config` |
| Repository authorization and local-only boundaries | [AGENTS.md](https://github.com/litexlang/golitex/blob/e6f0fb6cab0bb69f99eb9a33b30deceae6d0a74a/AGENTS.md) and the applicable repository policy skill |

Session boundaries include retaining accepted statements in the same process,
replaying them in a fresh process, rolling back a failed compound statement,
committing each successful statement in a mixed frame, stopping on hard errors,
and rejecting axioms in strict mode. The example above explains these
boundaries; it makes no agent-performance claim.
