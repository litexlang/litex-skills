# Current Litex execution contract

This edition was checked against an existing Litex 1.0.6-beta release binary.
Use the target executable's -version and -help and its version-matched
[CLI](../../../references/litex/docs/cli.md) and
[Agent Guide](../../../references/litex/docs/AgentGuide.md) before applying recipes.
The hub imports documentation; it does not build or update a user's compiler.

## File and Session

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

## Acceptance

For a saved artifact run a clean -lang en -f gate. Require exit 0 and parsed
Normal JSON with kind: run, success: true and session_error: null. Add -strict
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
