# Persistent Session and proof journal

**Open `-session` and keep one process for the entire authoring loop.** An
ordinary failed statement does not discard earlier accepted definitions or
facts. Repair it there; never reload the full file after each small addition.
The [short command comparison](../../litex-reference/references/execution.md#file-and-session)
distinguishes authoring from clean checkpoint and final runs.

The historical filename remains so existing skill links continue to resolve.
Current execution uses [the shared contract](../../litex-reference/references/execution.md),
with one top-level statement per input and no literal try wrapper.

Load a passing prefix, submit the target in source order and keep that process
after ordinary failure. Record materially distinct attempts with the exact
candidate, diagnostic, outcome and smallest next correction. Record accepted
source and dependencies before continuing. Materialize a contiguous accepted
prefix at a coherent checkpoint and run its clean file gate. Do not mistake
a Session's overall response for rollback of every statement in a mixed frame.

Resolve the source-owning workspace for the journal; this need not be the
compiler checkout. A minimal record includes target, executable version and
identity, session command, mathematical proof idea, ordered attempts, accepted
source, dependencies and saved-artifact acceptance. Keep concise rationale and
tool evidence, not private reasoning transcripts or unrelated environment data.

Restart only when the process is unusable, the prefix changes, or a committed
name must be replaced. Replay the accepted prefix after restart and inspect
each response. Keep the journal outside the process so interruption cannot
erase the accepted source. Use the owning repository's draft/journal layout;
inside golitex follow [its repository policy](../../golitex-repository-policy/SKILL.md).
