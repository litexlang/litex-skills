# Imported source guide

Source snapshot imported on 2026-10-13. Read this for the author's mathematical methods and scoped repository conventions. Historical CLI recipes and result fields are not current execution instructions; use [the hub execution contract](../../litex-reference/references/execution.md). Apply golitex-specific paths and maintainer rules only when working in that repository. Dated examples require replay before making a current-support claim.


# Golitex Repository Policy

Use this skill as a constraint layer alongside the task-specific Litex skill.
It does not replace proof writing, translation, modeling, kernel engineering,
research writing, or todo workflows.

## Git repository boundaries

**Never create an independent or nested Git repository in the user's main
folder unless the user explicitly requests that repository.** Reuse existing
authorized repositories; a migration or scratch-work request does not authorize
`git init`. Preserve existing nested repositories and their histories.

The entire root `scripts/` workspace is local-only and must remain ignored and
untracked in the parent golitex repository, with no file or subtree exceptions.
Never use `git add -f` to bypass this rule. Remove accidentally tracked scripts
paths from parent tracking while preserving local source files unless the user
explicitly requests their deletion. Publish requested deliverables in
`textbooks/`, `examples/`, `docs/`, or `showcases/` as appropriate; never expose
the local scripts workspace through the parent repository's GitHub tree.
Keep `.draft/` artifacts ignored
and untracked in their owning repository too: a parent ignore rule does not
protect an existing nested repository. Never force-add drafts or use blanket
staging without inspecting the staged paths. Read
[Git Repository And Draft Boundaries](golitex-agents.md#git-repository-and-draft-boundaries)
before repository creation, staging, or history cleanup.

For recursive cleanup of workspace-local `private/`, use the required helper
and direct-child scope in
[Workspace-local private cleanup](golitex-agents.md#workspace-local-private-cleanup).

## Keep accepted context after a proof failure

**Keep one live Session across ordinary failed statements. Repair and retry
in that process; earlier successful statements remain available.** Read the
checked repository `docs/AgentGuide.md` example and restart/replay boundary.
The live `docs/cli.md` owns command syntax and output; it overrides historical
`-before`, `try:`, `-compact`, `-runner`, and `ok` recipes in older skill notes.
A failed statement discards its own tentative state. A multi-statement frame
is not one transaction: its successful statements can still commit.

All user-facing replies must be careful, responsible, and honest: never
overstate results or completion, and explicitly disclose relevant conventions,
assumptions, unsupported boundaries, deferred work, and risks that could become
future maintenance traps.

## Explain every issue with concrete code

Whenever communicating a bug, improvement suggestion, technical problem, or
question for the user's decision, show the relevant Litex or Rust code in the
message itself. This applies to each distinct issue in progress updates,
reviews, proposals, decision questions, and final replies, not merely one
tracer for the entire task. Prose, terminology, file links, and a statement
that tests pass do not substitute for the code comparison.

- **Before / current:** show the smallest relevant existing snippet and the
  concrete input, current result, error, or state transition. Link the actual
  source when available; label a reduced reproduction as such.
- **After / proposed:** show the corresponding changed snippet and explain
  exactly what result or behavior changes for the same case. If Litex source
  stays identical while verifier behavior changes, show it once and put the
  old and new outcomes alongside it; include the Rust branch when needed to
  explain the cause or implementation choice.
- **Decision:** if alternatives remain open, show the concrete code or
  interface shape and resulting behavior of each material option. If a fix is
  not yet known, show the failing code and expected behavior, identify what is
  unresolved, and do not invent an implemented after-state.
- **Evidence:** clearly distinguish observed current behavior, suspected bugs,
  proposed code, implemented code, and verified results. Mark illustrative or
  unverified snippets explicitly; never present invented syntax, output, or
  an unrun example as repository evidence.

Prefer Litex to explain proof authoring and language behavior, Rust to explain
internal control flow, interfaces, or ownership, and both when connecting a
user-visible symptom to its kernel cause. Keep snippets short but retain the
conditions that explain the difference. The user must be able to see what
exists now, what would change, and why it matters without reconstructing the
code from a paragraph. Pure status updates with no new issue need not repeat
an already shown comparison.

## Finish before you report

Do not stop mid-task and report in a way that makes the user think the work is
done. Only report completion when the accepted work is actually finished
(implementation, wiring, tests/tracers or other acceptance evidence called for
by the task, and any promised follow-through).

If you must pause (blocked, need a decision, context limit, or out of scope),
say so explicitly: what is done, what is not done, and what remains — never
phrase a partial stop as “done / complete.”

## Required policy loading

1. Read
   [`references/golitex-agents.md`](golitex-agents.md) completely
   before taking task actions. It is the canonical detailed policy.
2. Treat a repository `AGENTS.md` as a bootstrap that activates this skill,
   not as a second copy of the detailed rules.
3. If a live repository instruction conflicts with the bundled policy, follow
   the live higher-priority instruction and report the drift so the skill can
   be refreshed.

User instructions take precedence over this skill. The golitex repository
policy takes precedence over generic or older workflow advice in another
Litex skill.

## Env and Runtime authorization gate

Without the user's explicit authorization, do not modify `Env`, `ExecEnv`,
`Environment`, or `Runtime`, including their owned state and state-management
contracts. Apply the concrete-change approval boundary in
[`User authorization for Env and Runtime changes`](golitex-agents.md#user-authorization-for-env-and-runtime-changes)
before proposing an implementation that changes these owners.

## Stmt / Obj / Fact AST struct authorization gate

Without the user's explicit authorization, do not modify `Stmt`, `Obj`,
`Fact`, or their payload / leaf structs (legacy or `src/`), including
shared leaves such as `Identifier`. Apply
[`User authorization for Stmt / Obj / Fact AST structs`](golitex-agents.md#user-authorization-for-stmt--obj--fact-ast-structs)
and skill `$litex-ast-struct-authorization`. A feature request is not
authorization to change those structs.

## Forward-derivation gate

For every substantive repository task, construct the work forward from
independently established repository evidence, source mathematics, user-owned
semantics, and compatibility constraints. Derive the relevant invariants,
then the orthogonal owners or dependency boundaries, then the smallest
interfaces or proof steps, and only then the requested artifact. A desired
output, passing example, or current failure may define the target but must not
be used to invent premises, trust, helper layers, aliases, special cases, or
architecture.

Use backward reasoning only as an audit: extract acceptance conditions, search
for counterexamples, and trace a failure to the earliest unsupported premise
or boundary. Repair that upstream point and re-derive its consequences rather
than appending a downstream patch. As a target-leakage check, ask whether each
new premise, interface, abstraction, theorem, and dependency would still be
justified if the final requested result were hidden. Scale the recorded
derivation to the task, but keep its evidence and dependency direction visible
in the task SOP or task-specific skill output.

## Search and explicit proof boundary

Authors supply meaningful proof routes; Litex checks them with bounded local
reasoning. Distinguish expression, explicit checkability and automatic
discovery. A bare search miss alone is not a bug, and an explicit workaround
alone does not establish verifier correctness. When assessing failed goals,
repeated mechanical bridges or proposed automation, read the shared
[search and explicit proof boundary](search-explicit-proof-boundary.md).
Use it as the common decision basis for proof writing, migration and kernel
work; current source determines the actual supported permissions and routes.

## Task SOP gate

For every bug-investigation or repair plan, apply the maintainer's
[two execution categories and discussion boundary](task-sop.md#bug-repair-plan-ownership):
Litex authoring improvements and justified local Rust semantic repairs are
delegated to Codex; nonlocal or unsettled contract changes require discussion.
Keep diagnosis confidence and repair ownership separate. This does not waive
the concrete AST/Env/Runtime authorization gates.

For substantive execution work, generate a compact task-specific SOP after the
first focused read-only anchoring and before the first repository mutation or
long-running gate. Read and follow
[`references/task-sop.md`](task-sop.md) for its format and
lifecycle.

The SOP fixes three things before execution drifts: the user's intent and exact
anchors, the ordered action protocol and stopping boundaries, and the evidence
that will count as completion. Keep it to one screen. Update it only when real
tool evidence changes the task contract; proof attempts still belong in the
proof journal, not in the SOP.

For a multi-step, mutating, long-running, or cross-turn task, persist the SOP as
the existing root execution ledger at `todo/<YYYY-M-D>/<task-slug>.md`. A
simple read-only answer or one-step inspection can use the same three-part
shape only in commentary without creating a file. At completion, audit the
result against the SOP. Delete a completed execution ledger after durable
results have been transferred to their source-owned acceptance, journal, or
todo artifact; retain an unfinished ledger with the exact next step and last
verified evidence.

## Evidence-to-skill promotion gate

Use this one-way evidence pipeline; never jump directly from one task or one
surprising failure to permanent instructions:

```text
single task -> temporary Task SOP -> execution and verification
            -> proof journal with factual evidence
            -> miner nominates a cross-journal pattern
            -> independent evidence review
            -> positive, negative, and behavior acceptance gates
            -> permanent skill rule only when the pattern is stable
```

The miner proposes candidates; it does not edit skills or establish causality.
Count evidence by independent source item or task, not by raw retry, transcript,
or replay-file count. Before promotion, state the reusable decision rule and
its nearest boundary, preserve multiple independent journal references, prove
the preferred route on a positive example, prove the boundary with a negative
or deletion control, and show that the candidate improves agent behavior on
held-out work without teaching a source-level workaround for a kernel or
library defect. Read the full lifecycle and routing rules in
[`references/task-sop.md`](task-sop.md).

## Tracer bullet reporting

Apply the canonical tracer-bullet contract in
[`references/golitex-agents.md`](golitex-agents.md). Before a
substantive change, select and announce one real example that shows the task's
central before/after behavior. Keep it as the first focused gate and lead the
final response with it before generalizing.

For a user-visible kernel capability or a major Litex code/interface update,
also apply the contract's persistent acceptance-artifact gate. Announce the
stable path up front; keep old Litex code commented, current code active, and
the focused command recorded. A commented old failure never substitutes for
an executable negative regression.

Use the Mechanics Chapter 6 mirror-`forall` cleanup as the fixed policy
example: show the renamed nested universal before, the direct active-binder
proof after, then follow that same example through persistent session, clean
file, whole-book, harness, trust-delta, and draft/public-boundary gates. This
example demonstrates the repository lifecycle; choose a task-specific tracer
for actual work.

For **proof-node / WD tracers**, also apply
`$litex-kernel-engineer`: do not use `trust` to fake ambient facts; prefer real
`have` / `let` / store paths (see that skill's "no trust" section).

## Verification quick contract

- Before choosing test commands, classify the change by semantic impact using
  the impact levels in
  [`references/golitex-agents.md`](golitex-agents.md). Record the
  selected level, affected domain, changed shared contracts, focused tracer,
  selected gates, and explicitly skipped broader gates. Do not escalate a
  leaf or subsystem change to repository-wide testing without a concrete
  cross-domain or architectural reason.
- Use one release `target/release/litex -f <accepted-prefix.lit> -session`
  process for the iterative loop. The initial file/prefix must pass. For an
  unfinished registered target, use an isolated task-owned configuration with
  its exact preceding exports and an empty target; do not modify the canonical
  configuration to register a probe.
- Submit one top-level statement at a time in source order, without a `try:`
  wrapper. Read each response. Retry an ordinary failed statement in the same
  live process; journal materially distinct attempts and accepted source.
  Materialize a contiguous accepted prefix only at a coherent checkpoint.
  Restart only at the canonical policy's explicit restart boundary and replay
  the journal's accepted prefix before continuing.
- Put that journal in the source- or task-owned working area, normally its
  existing `proof_journals/` or machine-artifact directory. For a textbook
  module at `scripts/<Workspace>/textbook/`, this is the owning workspace such
  as `scripts/<Workspace>/proof_journals/`, not the module tree. Never
  create `<golitex-root>/proof_journals/`, even when the target is part of
  golitex. If no owning workspace is identifiable, resolve it before the
  first proof attempt; do not invent a repository-root fallback.
- Timebox each unresolved proof obligation: use at most three active minutes
  before adding the narrowest marked source `trust` and continuing the
  mainline. After the chain runs, revisit each trust for at most five active
  minutes; record every survivor in the source-owned todo and do not start a
  third round without an explicit user budget.
- Finish a file with a clean `target/release/litex -lang en -f <file>`
  run. Require exit 0 and the parsed Normal envelope's `kind: run`,
  `success: true`, and `session_error: null`; use `-strict` when the artifact
  must exclude user assumptions. Reserve `-r <module>` for an explicit
  whole-module or whole-book gate. Interactive `-session` stdout is a REPL
  transcript, not one batch JSON document.
- When a mandated Rust harness currently targets a different tree from the
  artifact named by the repository policy, still run the mandated command, but
  do not misreport its coverage. Add the smallest release CLI gate against the
  intended artifact and report the harness drift as `kernel_problem`.

## Workspace hygiene hard gate

- Treat every agent-authored preliminary file as a draft, including disposable
  probes, copied projects, raw transcripts, scratch modules, temporary reports,
  and intermediate generated output. Allocate one draft area before writing:
  textbook `<Workspace>` work goes under
  `<golitex-root>/scripts/<Workspace>/.draft/`; every other task goes under
  `<golitex-root>/tmp/<YYYY-MM-DD>/<task-slug>/`, using the current local date
  and one stable filesystem-safe task name. Reuse that area instead of
  scattering files.
- Never put drafts in `<golitex-root>/private/`, absolute `/private`, the
  repository root, a canonical module tree, or an arbitrary source directory.
  Do not manually author drafts in a system temporary directory; tool-managed
  system temp files are outside this rule. A persistent proof journal, todo,
  canonical source, test, or requested final deliverable is not a draft and
  keeps its documented source-owned location.
- Do not assume `scripts/<Workspace>/.draft/` is publishable or tracked. Never
  stage, commit, export, render, or register a draft unless the user explicitly
  promotes it. Never edit a production `litex.config` merely to register a
  disposable probe.
- Before reporting completion, inspect the repository root and every touched
  source/module directory plus the allocated draft area for task-created
  journals, probes, temp files, copied projects, and config entries. Keep
  intended drafts in the allocated area, remove only task-owned disposable
  residue that is no longer useful, and report the exact path of anything that
  remains outside its allowed location.
