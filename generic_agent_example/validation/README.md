# What was checked — 2026-10-14

This is preparation and verifier evidence for the
[reproduction walkthrough](../README.md). It contains **no model API run** and
does not establish autonomous Generic Agent success, token cost or speedup.

## Installed upstreams and real entrypoints

- Generic Agent commit `8b7d4e0a82849ccda2c83b85d4391ed7b912ec7f` was fetched into an isolated temporary checkout.
- Its core was installed in a fresh Python 3.12 virtual environment with the runtime versions in [requirements.txt](../requirements.txt); `agentmain.py --help` succeeded.
- Public golitex commit `3c5befb5605193a53827b472b15462714ee8690b` was built with `cargo build --release --locked`. It reports Litex 1.0.6-beta. Build warnings were not changed.
- Preparation was exercised with a fresh run path containing spaces. It copied the author skill pack, rendered absolute paths in the actual prompt and recorded source/input/binary identities.

Source and environment identity, plus ten acceptance/control checks, are in
[reproduction-checks.json](reproduction-checks.json). Binary hashes identify
this local build; binaries built on another platform need not have identical
bytes. The source commits and mathematical input remain fixed.

## Actual Generic Agent tool branch, without inference

[bridge-smoke.json](bridge-smoke.json) exercises upstream
`GenericAgentHandler.do_code_run` with `inline_eval: true` across calls. The
model client and next-prompt hook were stubbed; the real tool implementation,
Session bridge and actual Litex process were used. This checks integration,
not a model's decision to select the skill or follow the prompt.

One PID accepted `have a R = 2`, rejected `a = 3`, then accepted `a + 1 = 3`.
The bridge refused multiple top-level statements before touching source/state.
An undefined-name parse failure stopped a later Session; deliberate restart
replayed accepted source and the same arithmetic consequence passed again.
[bridge-session.jsonl](bridge-session.jsonl) preserves the raw verifier events.
The pinned public build's final Session exit can be 0 despite earlier ordinary
rejections; it is not a substitute for the independent final file gate.

## Reference mathematics and acceptance boundaries

The [reference proof](../reference/proof.lit) was developed against the public
release binary. [reference-session.jsonl](reference-session.jsonl) preserves
full later candidates/feedback; [reference-authoring.json](reference-authoring.json)
preserves the earlier candidate attempts with explicitly partial tool output.
These are reference-authoring records, not Generic Agent model traces.

The exact [composed source](reference-check.lit), [stdout](reference-stdout.json),
[stderr](reference-stderr.txt) and [gate record](reference-result.json) show
strict acceptance of frozen prefix + reference proof + frozen goal. The task
allows equal lengths and concludes a vertex incident triple from the four face
conditions. The natural geometric interpretation is given in
[problem.md](../problem.md#geometry-boundary); 3D coordinate/distance foundations
are not separately formalized here.

Meaningful controls used the same actual checker entrypoint:

| Control | Observed result |
| --- | --- |
| Complete reference | Frozen goal passes |
| Unrelated valid `1 = 1` file | Frozen goal fails |
| Reference weakened by an extra `ab != ac` premise | The weaker file passes independently; frozen original goal fails |
| Goal admitted with `trust` | Ordinary check passes; strict frozen-goal check fails |
| Edited frozen goal | Refused before invoking Litex |
| Existing run destination | Refused with every existing file byte unchanged |
| Wrong source revision | Refused without creating output |
| Synthetic executable emitting a different JSON shape | Refused as an unknown contract; this transport guard is simulated, not proof evidence |

The final user-driven experiment still requires the reader's real provider,
model and API configuration. Preserve its actual failures, source, final gate,
help and costs; do not copy these reference results into its generation record.
