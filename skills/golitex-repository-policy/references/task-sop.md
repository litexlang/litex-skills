# Golitex Task SOP

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.


Use this compact contract for substantive Golitex execution tasks. It is not a
plan essay or a session transcript. Its job is to keep the task aligned while
real evidence changes the implementation route.

## When to generate it

After one focused read-only anchoring pass, but before the first mutation or
long-running gate, write the SOP in commentary. Also persist it at
`todo/<YYYY-M-D>/<task-slug>.md` when any of these is true:

- the task will edit repository files;
- it has three or more dependent execution stages;
- it includes a long verifier/build/publication gate;
- it may span turns, compaction, interruption, or handoff;
- failure would otherwise leave the next agent unable to identify the exact
  checkpoint and next command.

A one-step read-only inspection can use the three headings only in commentary.
Do not create ledger files for ordinary questions or status reports.

## Required shape

Keep the working file to roughly one screen:

```markdown
# <task name>

Status: active

## Intent and anchors

- Goal: <one observable outcome>
- Exact targets: <real paths, module, chapter, API, or command surface>
- User constraints: <explicit limits and required choices>
- Known baseline: <facts already observed by tools>
- Assumptions to test: <clearly labeled; never present these as facts>
- Non-goals: <nearby work that is outside authorization or acceptance>

## Action protocol

1. <first evidence-producing step>
2. <smallest mutation or proof loop>
3. <checkpoint and promotion/publication order>
- Tracer: <one representative before/after behavior>
- Stop/escalate when: <decision, authority, destructive, or stable blocker>
- Explicitly skipped: <broader gates or adjacent work and why>

## Completion evidence

- [ ] <exact focused command and required exit/envelope/result>
- [ ] <negative/liveness/boundary gate when semantics widened>
- [ ] <trust/API/statement/artifact delta audit>
- [ ] <publication or mirror consistency when in scope>
- [ ] <journal/todo/acceptance and draft-hygiene audit>

## Contract deviations

- None yet.
```

Remove fields that genuinely do not apply; do not replace them with filler.
For Litex runner gates, name the exact command surface and require both process
exit `0` and top-level runner `ok: true`. If the user explicitly excludes
`-r`, publication, kernel changes, trust, or another nearby action, put that in
both `Non-goals` and `Explicitly skipped` so it cannot disappear during work.

## Bug-repair plan ownership

For Litex/golitex bug investigation and repair plans, use two execution
categories. This records the maintainer's delegation; it is independent of
root-cause labels, `trust` / `kernel_problem`, and L0-L5 test impact.

1. **Litex authoring improvement.** The same mathematical goal verifies with
   better Litex code: intermediate equalities, an explicit proof command,
   an existing lemma, or a justified missing premise. Repair and verify the
   proof within the authorized task. Do not call an untried workaround a
   solution, weaken the goal, insert trust to close a bug, or impose elaborate
   authoring scaffolding to hide a genuine kernel defect.
   Check existing explicit proof routes, including `by contra`, before treating
   a missing automatic logical conversion as a bug. The maintainer accepts
   such checked explicit proofs; automatic shortcuts are not required merely
   because the formulas are logically equivalent. If the explicit command
   itself is unsupported, record that actual coverage boundary separately
   rather than claiming the proof already works.
2. **Local Rust semantic repair.** Evidence establishes the intended contract
   and a bounded implementation owner: a leaf builtin/infer rule, a missing
   WD obligation, one statement branch, a local matcher, or its evidence/output
   wiring. The maintainer delegates these repairs to Codex without requiring
   another permission round or maintainer code review. Codex owns soundness,
   implementation, focused positive/negative tests, and record cleanup.

Show **needs discussion** separately for a proposed repair that exceeds local
ownership: global search/recursion policy, shared representation, storage or
scope lifecycle, broad syntax/compatibility changes, or an unsettled
mathematical/public contract. Before editing that part, show the concrete
before/after code, the affected owners, why a local route is insufficient,
and the decision the maintainer must make. A small diff is not proof of
locality; a shared helper is not automatically nonlocal when it restores one
established contract and its consumers are bounded.

For each open item, record the category (or **provisional, diagnosing**),
observed evidence, intended invariant, smallest owner/next action, acceptance
checks, and the condition that would move it to needs discussion. Diagnose
unknowns autonomously; do not guess that a rule addition will suffice or ask
the maintainer to investigate facts Codex can discover. Reclassify and notify
the user when evidence changes the scope. Verification remains Codex's duty
even when the maintainer chooses not to inspect the code.

Honor the requested task scope: a read-only scan stays read-only. For an
authorized repair, categories 1/2 proceed under this standing delegation;
do not ask again about routine implementation choices. Exact authorization
requirements for Stmt/Obj/Fact AST structs and Env/Runtime owned state or
state-management contracts remain in force. Inspecting these types or using
their unchanged APIs does not itself cross that boundary.

Keep the live classification in the source-owned plan/todo, linked from the
temporary SOP. On completion, retain solution evidence and remove the open
item. Do not erase historical failures or mark pending acceptance as solved.

## Update discipline

Update the SOP only when executed evidence changes the contract, for example:

- the first real failure is in an earlier registered dependency rather than
  the named target;
- the task changes from a proof repair to a kernel contract repair;
- a required publication boundary or acceptance gate becomes reachable;
- a stable blocker forces a stop condition or exact next command.

When this happens, preserve the old observation briefly under `Contract
deviations`, update the affected section, and tell the user. Do not append
ordinary progress, repeated waits, every proof candidate, raw errors, or a
command history. Put materially distinct Litex proof attempts in the strict
proof journal and raw transcripts in the allocated draft/experiments area.

## Completion and memory boundary

Before the final response, reread the SOP and check every completion item
against tool output. Then:

1. transfer durable verified results to the source-owned acceptance note,
   proof journal, source todo, example, or maintained code;
2. retain unresolved blockers in the appropriate source todo;
3. delete the completed root Task SOP ledger;
4. retain an unfinished ledger only with its last verified checkpoint, current
   blocker, and exact next command.

Use the artifacts for different purposes:

| Artifact | Time | Purpose |
|---|---|---|
| Task SOP | Before and during | Intent, order, boundaries, acceptance contract |
| Proof journal | During | Materially distinct attempts and verifier evidence |
| Acceptance note | After | Durable verified before/after result |
| Source todo | After/incomplete | Surviving concrete blockers |
| Permanent skill | Cross-task | Recurring, executed, reusable patterns only |

## Evidence-to-skill promotion pipeline

Use this as a one-way evidence flow:

```text
single task
  -> generate a temporary Task SOP
  -> execute and verify
  -> preserve factual evidence in the proof journal
  -> mine recurring patterns across journals
  -> nominate a candidate rule
  -> collect independent journal evidence
  -> build positive, negative, and behavioral acceptance gates
  -> promote only a stable common rule into the permanent skill
```

No execution, no skill rule. Never promote a speculative plan, one local
failure, one theorem name, or the final repair from one task directly into
permanent instructions. The miner is read-only with respect to skills and
produces candidates, not causal conclusions.

An explicit user instruction changing workflow, delegation, or approval
boundaries is authoritative and may be recorded directly. It is not a mined
technical repair pattern and does not justify promoting an unverified fix.

Apply this promotion gate to every candidate:

1. **Normalize the mechanism.** State the context, earliest failing phase,
   wrong default move, preferred decision or repair, and nearest boundary.
   Remove book-specific and theorem-specific names from the proposed rule.
2. **Require independent evidence.** Cite multiple independent journals from
   distinct source items or tasks; prefer multiple workspaces. Retries, replay
   transcripts, liveness variants, and copied drafts of one target count as one
   evidence family, not as independent confirmations.
3. **Route the lesson to the right consumer.** A recurring authoring decision
   may belong in the proof-writer skill or authoring cards. A mechanical smell
   belongs in a linter. Missing reusable mathematics belongs in the library.
   Stable verifier behavior belongs in a kernel regression. Do not teach a
   long source workaround as permanent style when the actual defect is in the
   kernel, parser, diagnostic, or standard library.
4. **Construct an acceptance bundle.** Keep at least one positive example that
   verifies the preferred route, one negative or deletion control that
   demonstrates the nearest boundary, the exact focused commands, and the
   supporting journal ids. A commented old failure is explanation, not a
   negative regression.
5. **Verify behavior improvement.** Exercise the candidate on held-out work
   not used to formulate it. Compare against the prior skill or recorded
   baseline using task-appropriate measures such as correct first-phase
   diagnosis, attempts to first accepted block, proof length and echo count,
   trust delta, or reaching the clean gate. Require no regression at the
   negative boundary. Do not claim improvement from aggregate keyword counts.
6. **Promote and re-audit.** Add the smallest decision rule and boundary to the
   owning permanent skill only after the preceding gates pass. Record its
   evidence ids and acceptance artifact. Re-mine after relevant kernel,
   library, syntax, or skill changes; retire or narrow rules whose premise no
   longer holds.

The permanent skill should contain the decision procedure and boundary, not a
chronological war story. Journals retain the attempts; acceptance artifacts
retain the tests; the miner retains nominations.

## Short Litex example

For “refresh Analysis Chapter 11 with the current binary; `-f` only”, the SOP
should read like this:

```markdown
## Intent and anchors
- Goal: source and formal Chapter 11 pass the current release binary's registered `-f`.
- Exact targets: the two registered `chapter11-riemann-integral.lit` files.
- User constraints: use the current-source release binary.
- Known baseline: prior release gates were green; the current baseline is not yet known.
- Assumptions to test: the first failure may be in Chapter 11 or its registered prefix.
- Non-goals: no `-r`, no unrelated proof cleanup, no new trust.

## Action protocol
1. Build current source and record the binary version.
2. Run source registered `-f`; classify the first real failure before editing.
3. Use a persistent source-order session only for an actual target proof repair.
4. Run source and formal registered `-f` after the smallest accepted repair.
- Tracer: the first current-binary failure and the same line after repair.
- Stop/escalate when: the fix needs new user authority or a core-struct change.
- Explicitly skipped: whole-module `-r`, because the user excluded it.

## Completion evidence
- [ ] Source `-f`: exit 0 and top-level `ok: true`.
- [ ] Formal `-f`: exit 0 and top-level `ok: true`.
- [ ] Source/formal, trust, statement/API, and draft-residue audits.
- [ ] Durable acceptance record; completed Task SOP removed.
```
