# Current Litex execution contract

Resolve the live corpus with [the reading routes](live-reading.md). Use the
target executable's `-version` and `-help`, then that corpus's `docs/cli.md`
and `docs/AgentGuide.md` before applying recipes. They own current commands
and output. The hub's original 1.0.6-beta documentation is an explicit
[offline snapshot](../../../references/litex/README.md); later focused checks
are recorded separately. This hub does not build or update a user's compiler.

## File and Session

**Writing or repairing Litex code requires one live `-session`.** Load an
accepted prefix once, then submit each new statement to that same process.
An ordinary failed statement leaves earlier accepted definitions and facts
available; repair only the failed statement there. Never rerun the whole
file from the beginning whenever you add a few new lines.

Compare the authoring commands (the filenames are workflow placeholders):

```sh
# Wrong per-edit loop: each invocation reloads and checks the whole prefix.
litex -lang en -f solution.lit  # after adding a statement
litex -lang en -f solution.lit  # after repairing it or adding another
```

```sh
# Required loop: load the passing prefix once; keep this process open.
litex -lang en -f accepted-prefix.lit -session
# Submit new/corrected statements to its REPL, one at a time.
```

The [Agent Guide example](../../../references/litex/docs/AgentGuide.md#see-why-keeping-the-session-matters)
shows `a = 3` failing and `a + 1 = 3` still succeeding from the accepted
`a = 2` in that process.
Use separate full-file runs for the baseline, coherent checkpoints and final
verification; keep the authoring Session open while checking saved source.

The [small accepted prefix](../../../references/session-accepted-prefix.lit)
provides a concrete two-line saved source for this comparison. See the
[focused receipt](../../../references/validation.md#session-authoring-emphasis--2026-10-14)
for the tested executable and outcomes.

With the intended litex executable on PATH:

```sh
litex -version
litex -help
litex -lang en -f solution.lit
litex -lang en -f accepted-prefix.lit -session
```

In a golitex development checkout, build the requested source version with
cargo build --release and use target/release/litex. External users can use an
installed release; do not require a Rust checkout merely to author a proof.

The initial Session prefix must pass. For an unfinished configured target,
use a task-owned scratch module with the exact preceding imports/exports and
an empty target. Submit one complete top-level statement, read the result,
then continue. Do not wrap it in historical try syntax.

An ordinary failed statement discards its own tentative state; earlier
successful statements stay in the same process. A frame containing several
statements is not one transaction. Journal the accepted source in order,
repair the failed statement in that process, and materialize a contiguous
accepted prefix at a coherent checkpoint. Restart when the process stops,
the loaded prefix must change, or a committed declaration must be replaced;
replay the durable accepted prefix after restarting.

Replacing an already accepted declaration under the same name or deliberately
adopting a verified rebuilt executable requires saving accepted source and
restarting with replay. Replacing the executable on disk does not update an
existing process. A build or ordinary proof failure alone does not require
discarding the live Session.

## Acceptance

For a saved artifact run a clean `-lang en -f` gate. Require exit 0 and parsed
Normal JSON using the target executable's output contract:

| Checked executable | Successful envelope |
| --- | --- |
| 1.0.7-beta, checked 2026-10-14 | `kind: run`, `run_result: "success"`, `session_terminated: false`, `termination: null` |
| 1.0.6-beta bundled snapshot, checked 2026-10-13 | `kind: run`, `success: true`, `session_error: null` |

Follow the matching CLI for other versions; do not require fields from a
different executable. The [focused receipt](../../../references/validation.md#session-authoring-emphasis--2026-10-14)
records the newer boundary. Add `-strict`
when the artifact must exclude user trust and axioms. Session output is a REPL
transcript, not one batch JSON value. Reserve -r for an explicit whole-module
gate. Mathematical verification and Lean export are separate claims.

This binary has no -compact, -runner, -before or -isolated entrypoints.
Old command strings and ok fields inside imported source guides and receipt
summaries are historical evidence, not current execution instructions.

Use [the persistent journal guide](../../litex-proof-writer/references/litex-repl-try-workflow.md)
for proof iteration. For repository-specific trust budgets, draft locations
and authorization apply the owning repository's instructions; golitex uses
[its maintainer profile](../../golitex-repository-policy/SKILL.md).
