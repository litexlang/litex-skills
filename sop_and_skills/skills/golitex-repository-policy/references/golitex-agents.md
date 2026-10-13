# Litex Local Instructions

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.


Always apply these rules when working in this repository.

## Persistent Session: preserve accepted work

**A normal failed statement is not a reason to restart Litex. Keep the same
live process, repair that statement, and retain the accepted context.** The
repository's `docs/AgentGuide.md` starts with a checked artificial example:
`ready_at_seven` supplies `$ready(7)`; `$ready(8)` fails; `$ready(7)` still
succeeds in that process. A fresh process with only the predicate declaration
cannot use the missing axiom until the accepted prefix is replayed.

This is an explicit maintainer workflow instruction, not a kernel change or a
performance claim. The current `docs/cli.md` owns CLI syntax and output and
supersedes historical command recipes in other skills. A failed top-level
statement discards its tentative state; successful statements remain. A
compound claim is one statement, but a pasted multi-statement frame is not one
transaction. A hard error can end the process; use the restart/replay protocol
below rather than promising in-place recovery.

## User authorization for Env and Runtime changes

The user's explicit rule is: without their permission, do not modify `Env`
or `Runtime`. This applies to `Env`, `ExecEnv`, `Environment`, and `Runtime`
in both the legacy code and `src/`, including their owned state
containers and state-management contracts.

- Before modifying these owners, require explicit user authorization for the
  concrete change. Protected changes include adding, deleting, renaming,
  moving, or retyping fields; replacing state containers; changing ownership,
  constructors or initialization; and changing storage, cache, ID allocation,
  scope lifetime, merge, commit, or rollback behavior. Moving the same change
  into a helper, wrapper, side table, or new parallel store does not bypass
  this boundary.
- A request to plan, implement a feature, fix a bug, or build a tracer does
  not by itself authorize these changes. Present them as proposals, with the
  exact affected types, fields or methods, necessity, consequences, and the
  option of using existing interfaces. If authorization is missing, stop
  before the protected edit and ask the user; continue independent work.
- Honor explicit authorization already given in the conversation within its
  stated scope; do not request the same permission again. An assistant's own
  proposed design or plan is not user approval. Obtain further authorization
  before expanding beyond an approved change.
- Read-only inspection, design, and use of unchanged existing APIs remain
  allowed. Prefer the existing Env and Runtime contracts when they support
  the task; do not redesign them merely to simplify a local implementation.

## User authorization for Stmt / Obj / Fact AST structs

The user's explicit rule is: **Do not change Stmt / Obj / Fact structs on your own.**

This applies to `Stmt`, `Obj`, `Fact`, and their payload / leaf structs in
both legacy AST and `src/` AST (including shared leaves such as
`Identifier`, binder payloads such as `SetBuilder`, and fact/statement
payloads).

- Before adding, deleting, renaming, moving, or retyping fields, or reshaping
  enum variants of these types, stop and present an AST Struct Change
  Proposal. Wait for explicit user confirmation of that concrete change.
- A request to implement alpha_normalize, display, parse, verify, or a tracer
  does not authorize changing these structs. Prefer value-level rewrites and
  binder-local representations over changing shared leaf structs.
- Read-only inspection and code that uses existing fields remain allowed.
- See skill `litex-ast-struct-authorization` for the full gate.

## Task-Specific SOP Before Execution

For every substantive task that will mutate the repository, run several
dependent steps, issue a long verification gate, or plausibly span turns,
generate a one-screen Task SOP. A minimal read-only inspection may happen
first so the SOP names real files, commands, and baselines rather than generic
guesses. Finish the SOP before the first mutation or long-running gate and
announce its compact form to the user.

Use the format and lifecycle in [`task-sop.md`](task-sop.md). Persist it at
`todo/<YYYY-M-D>/<task-slug>.md` with status `active`. Treat it as the task's
control contract, not as a chronological log:

- **Intent and anchors** fix the exact goal, targets, user constraints,
  known baseline, assumptions still to test, and explicit non-goals.
- **Action protocol** fixes the evidence-driven order, applicable skills and
  instructions, mutation boundary, stop/escalation conditions, and explicitly
  skipped work.
- **Completion evidence** fixes the exact gates, artifact/delta audits, and
  cleanup needed before claiming completion.
- **Contract deviations** are added only when tool evidence materially changes
  one of those three sections. Do not record every command, attempt, or local
  proof correction there.

At the end, reread the Task SOP and audit every completion item. If complete,
transfer durable results to the owning acceptance note, proof journal, source
todo, or maintained artifact, then delete the root execution ledger. If work
is interrupted or genuinely unfinished, retain the ledger with the last
verified checkpoint, current blocker, and exact next command.

Do not confuse artifacts: the Task SOP is the before/during control contract;
the proof journal is attempt evidence; the acceptance note is the verified
after-state; the source todo owns surviving blockers. Follow the full
evidence-to-skill pipeline in [`task-sop.md`](task-sop.md): task -> temporary
SOP -> execution and verification -> factual journal -> cross-journal miner
nomination -> independent evidence -> positive, negative, and behavioral
acceptance -> permanent skill. The miner never edits skills or establishes
causality. One local surprise, several retries of one target, or several replay
files from one task are not independent evidence and must not become a skill
rule.

## User-Mandated Two-Pass Trust And Session Policy

This policy overrides any lower-priority instruction in this file that asks an
agent to keep searching for a proof before admitting a localized proof debt.

1. Timebox active proof search on one unresolved Litex obligation. In the
   first pass, spend at most three minutes on the natural direct proof and
   feedback-directed corrections. At that cap, or earlier when the blocker is
   already decisive, keep the intended source-facing statement and replace
   only the blocked substep with the narrowest legal `trust`. Mark the exact
   debt nearby and in the proof journal, then continue until the whole intended
   chain reaches its registered checkpoint. After the chain runs, inventory
   all direct trusts, summarize recurring shapes, and revisit each trust for at
   most five active minutes. Remove solved trusts; record every survivor in the
   applicable source-owned todo with a concrete example, both rounds' evidence,
   desired unblock, primary label `trust` or `kernel_problem`, and acceptance
   command. Do not begin a third proof-search round unless the user explicitly
   expands the budget. Exclude the initial release build, known long-running
   file/module gates, and ordinary waiting for an issued verifier command from
   these active-search limits. A declaration containing `trust` is not
   `checkable`.
2. For iterative Litex edits, retain one release process opened with
   `target/release/litex -f <accepted-prefix.lit> -session`. The initial
   registered prefix/target must pass before entering the REPL. For an
   unfinished registered target, allocate a task-owned scratch module that
   preserves the exact preceding imports/exports and has an empty target;
   submit the target's statements there in source order. Do not change the
   canonical configuration merely to register that probe.
   Submit one top-level statement per input, without a literal `try:` wrapper.
   Consume the response before sending another candidate. If statement 5
   fails normally and another `litex>` prompt appears, repair and resubmit
   statement 5 in the same process. Once it succeeds, journal the accepted
   source and reusable lesson before statement 6. Record each materially
   distinct failed attempt with its actual output. A multi-statement input
   can contain committed successful statements even when overall success is
   false; inspect those results before resubmitting declarations.
   Put the journal in the source- or task-owned working area, normally its
   existing machine-artifact or `proof_journals/` directory. For a textbook
   target, use `scripts/<Workspace>/proof_journals/`, not the canonical
   `textbook/` tree. Never create `<golitex-root>/proof_journals/`; resolve an
   ambiguous owner before the first proof attempt.
   Do not edit the canonical `.lit` during this inner loop. At a coherent
   checkpoint, materialize a contiguous accepted prefix from the journal into
   `.lit` in source order, then run its clean release file gate. A normal
   soft failure does not require restarting or reloading the registered prefix.
3. Restart only if the session process exits, cannot accept input, or its
   registered prefix must deliberately change, or an already committed
   declaration must be replaced under the same name. Record an unexpected
   session failure as `kernel_problem`. After restarting, reload the intended
   module context and replay the journal's accepted statements in order before
   retrying the pending one; check each replay result. Use a clean `-f` gate for
   the saved artifact, not as the ordinary per-candidate proof-debug loop.

## Git Repository And Draft Boundaries

These are explicit maintainer instructions:

- Do not create an independent or nested Git repository in the user's main
  folder unless the user explicitly requests that repository. Do not run
  `git init` in a translation workspace, copied project, or draft directory
  merely to support a task. Reuse an existing authorized repository.
- Preserve existing nested repositories and their histories. Never delete
  `.git` or reinitialize a repository as a cleanup shortcut.
- The entire `<golitex-root>/scripts/` directory is local-only: keep `/scripts/`
  ignored and remove accidentally tracked scripts paths from parent tracking
  while preserving local files unless the user explicitly requests deletion.
  There are no file or subtree exceptions and no
  `git add -f` bypass. Publish requested final deliverables in the appropriate
  public directory (`textbooks/`, `examples/`, `docs/`, or `showcases/` as
  appropriate). Never add, commit, push, or expose any scripts path through
  the parent golitex repository's GitHub tree.
- Keep disposable `.draft/` artifacts ignored and untracked in the repository
  that actually owns them. Check the owning Git root and staged paths before
  staging; the parent repository's ignore rules do not protect a nested repo.
  A draft becomes a deliverable only through explicit user promotion, and
  promotion never overrides the parent repository's local-only scripts rule.
- Removing a file in a new commit does not remove it from history. When the
  user explicitly requests history removal, inspect the exact paths, refs,
  remote state, and local changes, then clean only the authorized scope while
  preserving local source files unless deletion was also requested. Do not
  claim history removal based only on untracking or a deletion commit.

For example, `scripts/mathematics_in_litex/.draft/migrate_zero_trust_chapters_2026_10_08/`
must stay out of both parent commits and commits in an existing `scripts/`
repository. Failed-proof logs and `prepared-c06*.lit` files remain local
drafts; creating another repository to hold them is not authorized.

## Workspace-local private cleanup

`private/` means only the directory directly under the current Git root. It
never means `~/private`, `/private`, `/private/tmp`, or a private directory
under the current subdirectory. This cleanup rule does not authorize creating
drafts there; use the draft locations specified below.

Before recursive deletion, confirm the target was created for the current
task or explicitly placed in scope by the user. Do not invoke `rm -rf` for
these targets. Run `/Users/shenjiachen/.codex/bin/codex-clean-private
private/<direct-child>` from the Git root, passing one or more direct children.
Delete the top-level task directory rather than a nested target. Never pass an
absolute path, `private/` itself, `..`, a wildcard, a nested path, or a home
directory path. Preapproval does not authorize unrelated deletion.

## Proof Journal And Temporary Artifact Hygiene

Treat repository cleanliness as a completion gate, not optional housekeeping.

1. Treat every agent-authored preliminary file as a draft: disposable probes,
   transcripts, scratch projects, copied modules, temporary reports, and
   intermediate generated output all qualify. Before writing any draft,
   allocate exactly one task area. If the task concerns writing textbook
   `<Workspace>`, use `<golitex-root>/scripts/<Workspace>/.draft/`; resolve the
   workspace through `scripts/.textbooks` when applicable. For every other
   task, use `<golitex-root>/tmp/<YYYY-MM-DD>/<task-slug>/`, where the date is
   the current local date and the task slug is stable and filesystem-safe.
   Reuse that area for the whole task instead of scattering files.
2. A persistent proof journal is a source-owned artifact. Put it in the
   corresponding draft, dataset, or task workspace, normally an existing
   machine-artifact directory or `<workspace>/proof_journals/`. For textbook
   modules under `scripts/<Workspace>/textbook/`, use the owning workspace
   `scripts/<Workspace>/proof_journals/`. If ownership is ambiguous, stop before the
   first proof attempt and resolve the location instead of guessing.
3. Never put drafts in `<golitex-root>/private/`, absolute `/private`, the
   repository root, a canonical `.lit` tree, or an arbitrary source directory.
   Do not manually author drafts in a system temporary directory; an external
   tool's internally managed system-temp files are outside this rule. Never
   edit a production `litex.config` merely to register a disposable probe; use
   an isolated draft project or the persistent session instead. A canonical
   source, test, todo, persistent journal, or requested final deliverable is
   not a draft and retains its documented source-owned location.
4. Keep intended drafts in their allocated task area. Remove task-created
   disposable residue when it is no longer useful, including after a failed or
   interrupted check. Use only explicit task-owned paths; do not delete unknown
   or user-owned files. Do not stage, commit, export, render, or register a
   draft unless the user explicitly promotes it.
5. Before reporting completion, scan the repository root and all touched
   source/module directories plus the allocated draft area for task-created
   journal folders, temp-name markers, copied projects, probes, and temporary
   config entries. Relocate any misplaced draft into the allocated area or
   report its exact path and do not claim that the workspace is clean.

## User-Facing Tracer Bullet Contract

For every substantive Litex kernel, parser, verifier, proof, interface,
textbook, example, diagnostic, or documentation change, select one real
task-specific example that makes the change observable. Call it the tracer
bullet. Choose it after the first targeted inspection or reproduction and
before broad implementation. Prefer an actual caller, source item, theorem, or
failure over a detached toy.

Record and communicate one compact tracer card:

1. **Why representative:** which central behavior of this task the example
   exercises.
2. **Before:** the exact code shape, output, failure, proof route, or reader
   experience before the change.
3. **After:** the intended or implemented code shape and behavior.
4. **Evidence:** the focused positive gate, and for widened kernel semantics a
   negative boundary test that must remain rejected.
5. **Boundary:** what the example does not establish and where the change must
   not generalize.

Announce the selected tracer bullet to the user before substantial edits. Use
it as the first regression or use probe and keep it live through the final
gate. Lead the final response with its before/after outcome, then explain the
rest of the change through that example. Whenever using an abstract term such
as elaboration, carrier, inference, provenance, trust boundary, or interface,
immediately identify the concrete line or behavior in the tracer that exhibits
it.

Use one primary tracer bullet. Add at most two secondary examples only when the
task contains genuinely independent behavior changes. If investigation shows
that the original tracer is not representative, replace it once, tell the user
why, and retain the abandoned example only as negative evidence when useful.
The fixed examples in task-specific skills teach selection; do not mechanically
reuse them when they do not exercise the current task.

### Persistent acceptance artifact for large changes

For every user-visible kernel, parser, runtime, verifier, inference, or builtin
capability change, and for every major Litex code or interface migration, keep
one durable acceptance artifact for the tracer bullet. Choose and announce its
path before broad implementation. A terminal transcript or a file under a
temporary directory does not satisfy this requirement.

The artifact must make the capability delta readable in this order:

1. **Before:** preserve the former Litex code as Litex comments, with every old
   code line prefixed by `#`, followed by the exact former rejection, failure,
   or limitation.
2. **Now:** show the current code without comment prefixes and state exactly
   what it now verifies, parses, infers, or computes.
3. **Boundary:** name the nearest behavior that remains unsupported or must
   still be rejected.
4. **Evidence:** record the exact focused verification command and the current
   implementation or registered-source path. Record broader gates separately.

Use this minimal shape, adapting the code rather than the headings:

```litex
# Tracer: <capability>
#
# Before (did not work):
# <old Litex line 1>
# <old Litex line 2>
# Former behavior: <exact failure or missing capability>
#
# Now (verified):
<active Litex line 1>
<active Litex line 2>
# Current behavior: <exact accepted capability>
#
# Boundary: <nearest unsupported or rejected case>
# Evidence: <command and test/source path>
```

For kernel work, prefer a small runnable `.lit` artifact under the nearest
existing `examples/` feature or proof-pattern directory. It must be collected
by the examples harness. A commented `Before` block is explanatory evidence,
not a regression test: when semantics widen, also keep an executable negative
Rust regression or negative fixture for the boundary. The active `Now` block
must pass both its focused release gate and the applicable examples harness.

When a task adds a new capability or updates / widens an existing one, add a
**new** dedicated `.lit` in that matching `examples/` folder in the same turn.
Do not leave acceptance only in `examples/tmp.lit` or a draft path; name the
file for the feature/update and follow the folder README. See
`$litex-kernel-engineer` (“New or updated feature → new examples `.lit`”).

For a major Litex proof, interface, library, or textbook migration, do not
paste obsolete implementation history into the canonical mathematical `.lit`
source. Put the durable comparison note in the source/task-owned paired
workspace as
`scripts/<Workspace>/experience/problem_notes/<slug>_acceptance.md`. Inside a
`litex` fence, prefix every former code line with `#` and leave the current
code unprefixed. Link the current block to its actual registered `.lit` path
and record the clean command that verified that registered source. If a small
standalone runnable example already has a natural home, prefer or additionally
use that `.lit` artifact. The note must not claim that a Markdown excerpt was
executed when only the linked registered source was executed.

In the final response, lead with this artifact, link its path, quote only the
smallest useful before/now pair, and state the focused gate result. Do not call
a major change accepted if the artifact is missing or stale.

## Project Direction Through September

The main project direction through September is to use real mathematical
translation work as a pressure test for Litex. The target sources include
Mathematics in Lean, Terry Tao's miniF2F, MATH500, high-school
mathematics datasets, and Weil's Number Theory for Beginners.

The purpose is twofold:

1. Build strong evidence that Litex can express and verify meaningful
   mathematics quickly.

2. Use translation failures to discover real language, standard library,
   kernel, inference, automation, and diagnostic gaps.

Treat this as a structured feedback loop, not as a line-by-line porting
project. For each source, start with a small vertical slice before attempting
large-scale coverage. A useful slice is around 20-50 representative problems,
definitions, or theorem statements.

For each translated item, follow this loop:

1. Understand the mathematics first.

2. Write a natural Litex statement and proof attempt that matches the current
   verifier style.

3. Run the verifier and read the exact output.

4. Make the next smallest correction.

5. Classify the result as one of:
   - `translated`: the mathematical statement is naturally expressed in Litex.
   - `checkable`: the statement and proof are fully verified by Litex.
   - `blocked`: the failure reason is understood and recorded with a minimal
     reproduction.

Classify blockers explicitly with only these labels:

1. `trust`: the current proof is not complete. Use this for missing
   definitions, lemmas, theorem organization, automation, syntax, diagnostics,
   formulation work, or any case where the honest statement is that we do not
   yet know how to finish the proof in Litex.

2. `kernel_problem`: the issue appears to be in Litex's verifier, runtime,
   well-definedness logic, core proof model, or another kernel-level behavior
   rather than in the current proof attempt.

Prefer early work on low-dependency, high-feedback corpora such as MATH500,
high-school math, and small miniF2F slices. Use Mathematics in Lean as a
standard library roadmap. Use Tao's Analysis I and Weil's Number Theory for
Beginners as deeper stress tests for structured definitions, chapter
dependencies, and long-form mathematical development.

Successful translations should become examples, benchmarks, or documentation
snippets when appropriate. Failed translations should become minimal blockers
that guide standard library work, language design, kernel improvements, or
better diagnostics. It is acceptable to use `trust` or `abstract_prop` only when
the blocked part is clearly labeled and the rest of the development remains
explicit and checkable.

When a textbook theorem overlaps with Litex builtin behavior, kernel support,
or a broad standard-library theorem, keep both roles visible. Preserve the
source theorem as a local textbook-facing statement so chapter coverage and
dependencies remain traceable. Use the Litex/std theorem as the main proof
source when it exists or is the intended trusted interface. If the source proof
is pedagogically important but not yet the main checked path, place its proof
shape in a local `prove` block, proof sketch, or nearby todo as an alternate
route/proof debt rather than replacing the chapter statement.

For textbook chapter files, follow the source order when introducing local
definitions. Do not put a large block of chapter-wide `prop` or
`abstract_prop` declarations at the top unless the source itself starts that
way. If Litex already has a builtin concept or standard predicate such as
membership, subset, finite sets, `finite_set_size`, tuples, Cartesian products, or
function equality, use it directly instead of adding a Tao-specific wrapper.
Record broad proof debt in nearby comments or todo files; only introduce a
named prop when it is a real source definition or a reusable local interface
that later checked statements actually depend on.

Use source-local cite packages for substantial unresolved supporting facts.
This is the preferred workflow for textbook and dataset formalization when the
main mathematical line is clear but a surrounding fact remains genuinely
unproved after a direct attempt and has a substantial or library-shaped proof.
Keep the main chapter or problem file focused on the source-facing definitions,
theorem statements, core proof route, and checked derivations. Put the
surrounding fact into an adjacent module such as
`chap7_cite/main.lit`, `<source>_cite/main.lit`, or a local `cite/main.lit`.
The main file should import this module with `import "../chap7_cite"` or the
analogous relative module import. For repository projects, declare the cite
package with `export mod` and import its root name. Represent source-order file
reuse by placing the source earlier in the ordered `[export]` table and citing
its canonical name in the dependent source; Litex has no statement for loading
an arbitrary `.lit` path.

Before adding or calling a cite theorem, test the intended fact directly in the
real caller context without a wrapper theorem or `trust`. If builtin or infer
rules verify it, use the fact directly and do not create a `thm` merely so later
code can cite it. Never put a trusted duplicate of a builtin-supported fact in
cite. This includes elementary set algebra such as commutativity of `intersect`
or `union`, arithmetic normalization, comparisons, and automatic type or
membership consequences. Repetition alone does not make such a fact
cite-worthy. If the source itself names the result, keep the source-facing
theorem in source order and let its body verify directly. If a simple expected
fact fails, classify the missing builtin, infer, standard-library, or kernel
support instead of hiding the gap as citation debt.

Cite packages are explicit proof-debt interfaces, not completed standard
library modules. Facts in a cite package should be named `thm` or `claim`
interfaces whose unproved step is marked with `trust`, and each such debt should
be journaled during the first pass and tracked in the nearby `todo.md` or
unfinished notes if it survives the five-minute second pass. An imported cite module
must be self-contained: import the std modules it needs, and put shared source
vocabulary in a small real `prop`/`have` module such as `chap9_vocab/main.lit`
rather than copying existing chapter definitions as `abstract_prop` inside the
cite package. Use `abstract_prop` only for genuinely external background
interfaces that do not yet have a usable definition. Only move a cite theorem
into `std` after its statement is stable, its proof or intended trusted
interface is understood, and multiple files genuinely need it.

By September, a good outcome is not only a large number of translated items. A
good outcome is a working translation pipeline, checkable examples across the
main source families, a clear standard library gap map, a benchmark set for
Litex's mathematical ability, and minimal reproductions for the important
blockers.

For every source folder under `scripts/` or a similar local translation
workspace, maintain a nearby `todo.md` as the local blocker list for that
source. When translation work reveals a missing definition, theorem, infer
rule, builtin rule, syntax feature, or diagnostic gap, append a concise item to
that folder's `todo.md`. When one of those items is implemented or no longer
blocks the work, remove it from that `todo.md`. For example, if work in
`scripts/minif2f_tmp/` hits a missing feature, record it in
`scripts/minif2f_tmp/todo.md`; if the feature is later added, delete the
completed item.

## Textbook Artifact Boundaries

Treat `scripts/.textbooks` as the authoritative textbook-workspace registry.
Each non-comment entry names one direct child workspace of `scripts/`; its one
canonical Litex module lives at `scripts/<Workspace>/textbook/`. That directory
contains chapter `.lit` files, `litex.config`, the module-owned `README.md` and
`math_collections.md`, and every other artifact intended to ship with the book.
All textbook edits, proof iteration, chapter checkpoints, whole-book checks,
and module-documentation updates happen there.

There is no central `scripts/textbooks_drafts/` mirror and no repository-root
`textbooks/` snapshot. Do not recreate either tree, copy a workspace-owned
module into a second publication directory, or treat an older note naming one
of those paths as the current target. Resolve the owning workspace through
`scripts/.textbooks` and update stale operational paths when they are touched.

Keep source material, translation-item records, todos, audits, experience
notes, generated Markdown, and durable verifier captures in the owning
workspace beside `textbook/`, such as `scripts/Analysis/`. For Analysis I,
chapter tracking remains in `scripts/Analysis/todo/`. Every preliminary file
for writing textbook `<Workspace>`, including disposable probes and scratch
copies, belongs under `scripts/<Workspace>/.draft/`. Do not treat that folder
as the canonical module, publish it, or scatter its contents elsewhere.

The module-owned `README.md` and `math_collections.md` live beside
`litex.config` in `textbook/`. Do not export, import, render, or pass them to
the Litex kernel.

## Litex Module Documentation

For every new top-level Litex module or project, maintain exactly one
`README.md` and one `math_collections.md`. When an existing module gains or
changes a core mathematical interface, add or refresh this pair as part of the
same work. Do not backfill untouched modules merely to satisfy this convention.

Here “module” means the top-level maintained package or project, even when it
contains many `.lit` files, exports, or submodules. Do not create another pair
for every chapter or submodule.

- Put the pair in the root of a reusable directory module such as
  `std/basics/`.
- For a textbook or translation project, put the pair in
  `scripts/<Workspace>/textbook/` beside `litex.config`. They are part of the
  module, not the owning workspace root such as `scripts/Analysis/`.
- Write both files in English.

The textbook pair is repository documentation, not chapter content. Do not
list it in `[export]`, import it from Litex, add it to a rendered chapter
manifest, or otherwise send it through the Litex kernel or textbook renderer.
Keep todos, audits, verifier captures, and other working Markdown in
`scripts/<Workspace>/`.

`README.md` describes the current implemented module. Keep it factual: purpose,
import or run entrypoint, namespace, actual public objects/functions/templates,
predicates and main theorems, visible checked/trusted/axiom boundaries, and a
small real use example. Do not put unimplemented wish-list interfaces there.

`math_collections.md` is the mathematical design manual. Record only the
important concepts and intermediate nodes that shape later work. For each one,
explain its mathematical meaning, why it matters, the ideal Litex form and a
short representative signature, the nearest rejected form, dependencies,
downstream uses, and which proof/existence/uniqueness/well-definedness holes may
remain. It is a narrative guide, not a machine-readable schema or exhaustive
theorem inventory.

Before generating substantial module code, read both files and compare the
candidate declarations with `math_collections.md`. If they differ, decide
whether the code misunderstood the intended mathematics or the design note is
now wrong. Fix the code in the first case; update `math_collections.md` first
and then migrate the code in the second. Do not preserve incompatible shapes
through a wrapper, alias, `abstract_prop`, or `trust`. After the implementation
and representative use probes verify, update `README.md` to reflect the actual
public interface.

## Dataset And Textbook Problem-Solving Loop

Use this loop for MiniF2F, MATH500, high-school datasets, Mathematics in
Lean, Tao Analysis, Weil Number Theory, and any other dataset or textbook
translation work. The goal is a pressure-test workflow, not only a final
answer.

For every dataset, textbook, contest, exam, or generated-math item that is
newly created or touched, maintain a structured translation item record with
this shape:

```yaml
source:
problem:
proof_idea:
litex_code:
comments:
```

Use these fields consistently:

- `source`: dataset, book, exam, contest, or source name.
- `problem`: source problem, theorem, exercise, or a reusable reformulation if
  the source text cannot be redistributed.
- `proof_idea`: the mathematical idea before Litex code.
- `litex_code`: the current runnable or intended Litex code.
- `comments`: verifier command, proof attempt notes, blocker label, source or
  license caveats, and follow-up work.

Do not submit only raw Litex code for a translation item. Record the
mathematical idea and, in `comments` or local tracking, the current status. Do
not mark an item `checkable` unless the relevant Litex code has been run and
verified. If source text cannot be redistributed, record a reusable
mathematical reformulation and put the license concern in `comments`. Existing
datasets do not need to be migrated all at once, but newly created or modified
records should follow this contract.

If a workspace needs dashboard or batch-tracking fields such as `id`, `topic`,
`difficulty`, `status`, or `blocker`, add them locally, but do not treat them
as required fields for ordinary translation records.

For each item, proceed in this order:

1. First explain the natural-language mathematical idea. Work out the key
   transformations, cases, witnesses, estimates, or theorem dependencies before
   writing Litex.

2. Translate that mathematical plan into a natural Litex formulation. Prefer a
   proof shape that the current verifier can check: explicit equality chains,
   small intermediate facts, finite case splits, witnesses, named theorem
   calls, and local reusable lemmas.

3. For textbook work, if the source theorem can be proved by following the
   text but Litex also has builtin/kernel/stdlib support for the same fact,
   record both routes. Keep the source theorem statement in the chapter file,
   use the named Litex/std interface as the main checked route when available,
   and keep the textbook proof idea in a local `prove` block, proof sketch, or
   nearby todo until it is checkable.

4. If a supporting fact remains genuinely unproved after a direct real-context
   attempt, has a substantial or library-shaped proof, and is needed to keep
   the current source item moving, put it in a source-local cite package and
   import that package from the main file. This keeps the main file readable
   while preserving a named theorem interface and explicit proof debt. Do not
   put builtin-supported or other elementary automatic facts in cite.

5. If an item, statement, theorem, or substep reaches the three-active-minute
   first-pass cap, write the best partial Litex proof and use `trust` only for
   the blocked step. Next to that trust, mark the first-pass timebox and state
   the missing fact or capability. Continue the mainline instead of spending
   the rest of the batch on that one obligation.

6. After the whole chain runs, review the trust shapes and spend at most five
   active minutes on each trust. Put survivors in the local
   unfinished-explanation area. In
   MiniF2F this is
   `scripts/litex-minif2f/unfinished_dataset/problem_notes/`.
   For another dataset or textbook workspace, create the analogous nearby
   folder if it does not already exist. Name the file by the problem or theorem
   id. Record the proof idea, the current Litex attempt, the exact verifier
   failure if any, every remaining `trust`, and the primary blocker label.

7. During that second pass, remove proof debt one step at a time. Run the
   verifier after each small change and use the exact output to decide the next
   correction. Try splitting algebraic or numeric jumps into smaller equalities
   before searching for new theorems. Stop at the five-minute cap, hold a
   second review, and defer the remaining concrete debt to todo.

8. When the item becomes checkable, move it out of the unfinished area and into
   the finished area for that source. Delete the matching unfinished-explanation
   file, update any local JSONL/status/todo bookkeeping, and keep the final
   `.lit` file runnable.

9. After solving a formerly unfinished item, write a short "war story" in the
   local solved-experience area. In MiniF2F this is
   `scripts/litex-minif2f/experience/problem_notes/`. For another
   source, create the analogous nearby folder if needed. Record the natural
   idea, where the attempt got stuck, the exact trick or Litex pattern that
   solved it, and any reusable lesson for later items.

When splitting backlog work, use disjoint ranges or families. Use read-only
triage passes to classify unfinished items, and use workers only on clearly
separated write scopes. Each worker should return the status for each item it
touched: `checkable`, `translated`, or `blocked` with one primary blocker
label.

## General Engineering Style

1. Read the nearby code before editing. Follow the existing data model, naming, and control flow unless the user asks for a redesign.

2. Write simple code, not clever code. Avoid fancy Rust syntax when a direct expression is clearer.

3. Keep changes scoped to the request. Do not rewrite unrelated code or clean up unrelated files.

4. Use English for comments and documentation. Comments should be concise and explain the purpose of non-obvious logic.

5. Do not add many comments. If the code is simple, make the code clear instead of adding comments.

6. Prefer the smallest coherent data model. A new struct or wrapper must own a
   distinct invariant, lifecycle, invalidation rule, trust boundary, or
   independently reusable behavior. Do not add a container merely to hold an
   existing options/config struct plus one or two fields with the same owner
   and lifetime. Put those fields on their actual semantic owner and remove
   parallel parameters or duplicate sources of truth. For example, prefer
   `RunOptions { is_isolated, ... }` over
   `GlobalOptions { run: RunOptions, isolated }`.

7. Model legal states directly. Use enum variants for mutually exclusive modes
   instead of combinations of booleans, unrelated `Option` fields, placeholder
   labels, or unresolved variants that leak into resolved result types. Parse
   uncertain input at the boundary; once resolution succeeds, downstream data
   structures should contain only the selected, valid state.

8. Data-structure minimalism removes conceptual layers and impossible states;
   it does not justify a God struct. Keep types separate when their ownership,
   lifetime, invalidation, security or trust boundary, or state transitions
   genuinely differ. During design and review, be able to state the independent
   semantic reason for every new struct and wrapper layer.

## Rust Kernel And Codebase Rules

1. Use `use crate::prelude::*;` for repository imports. Import only `std` items directly.

2. Use `.into()` to convert between types instead of directly wrapping a struct with an enum variant such as `Enum::Variant(value)`.

3. Do not write code in `mod.rs`; `mod.rs` is only for module definitions.

4. Use a static `new` function to create a new instance of a struct instead of using the struct literal constructor directly.

5. Do not write static functions inside a struct when the struct is not needed. Use a free function instead.

6. Do not write too many functions. If a piece of code is simple and only called once, write it inside the function that calls it.

7. Write shared helper functions in a `helper.rs` file, not at the head of a file.

8. Do not write new helper functions at the beginning of a file. Put them near the end of the file. The beginning of a file should contain major functions or struct definitions.

9. When implementing a builtin rule, write comments about what mathematical property the rule is for, and include an example.

10. When implementing an infer rule, write comments about the condition under which the rule is applied and what new fact is inferred. Include an example.

11. All runtimes created within one top-level run must share the same module manager. In particular, imported-module runtimes should be created with `Runtime::new_for_import_from_parent` so nested imports, cycle checks, source labels, and stopped-module state all update the same `Rc<RefCell<ModuleManager>>`.

## Litex Language And Proof Style

Default to the one-line definition-folding form `by def <FACT>`. In
particular, write:

```litex
by def $P(args)
```

Do not normally expand the same step into a goal block:

```litex
by def:
    ? $P(args)
```

Use the multi-line goal-block form only when the surrounding construct or a
real verifier run shows that the one-line form is insufficient.

Named `thm` proof bodies are optional. When the theorem's own `? forall ...`
binders, setting expansion, premises, or ordinary verifier rules already
discharge every then-clause, leave the body empty. Never copy a then-clause
into the body merely to make the theorem look nonempty:

```litex
thm setting_law:
    ? forall [SomeSetting], x S:
        $law(x)
```

Deletion-probe the bodyless form in the real registered context before
materializing it. Keep a body whenever it performs a genuine derivation,
selection, fold, witness, case split, or representation bridge. An empty body
does not waive proof: the verifier must still reject an unsupported
then-clause.

1. Litex examples should expose a tight verifier feedback loop: write a small proof, run it, read the exact verifier output, and make the next smallest correction until the proof is checkable.

2. Before writing Litex code, first explain the proof idea in natural language and look for the local proof pattern. Prefer starting from the mathematical move that should work in Litex rather than searching for theorem names as if the task were Lean.

3. When several formulations are possible, prefer the most Litex-native and
   simplest checkable formulation. Do not preserve a source text's original
   shape, or Litex's lower-level raw expression shape, if doing so creates
   special cases or a harder proof. If preserving the source shape is important
   for comparison, record it separately and keep the main checked proof simple.

4. Do not rely on external mathematical libraries when writing Litex examples unless the user explicitly asks for that. Prefer proof steps that the current Litex verifier can check directly.

5. Make documentation and Mechanics of Litex Proof `litex` fenced blocks self-contained. A snippet should not depend on a previous snippet sharing the same environment. If a block is illustrative only, mark it with `<!-- litex:skip-test -->`.

6. Any time the user asks for code that makes some Litex code verifiable, write
   the runnable draft in the task's allocated draft area and test that exact
   file. Promote it to a canonical example only when the task calls for a
   maintained regression or the user explicitly requests promotion.

7. When writing ordinary Litex `forall` facts, do not write an empty implication body. Write:

```litex
forall x R:
    ...
```

instead of:

```litex
forall x R:
    =>:
        ...
```

The current `forall ... <=>:` syntax is an exception: if there are no shared hypotheses, keep the required `=>:` block for the left side of the iff.

8. Avoid restating type and membership facts that Litex has already introduced. For example, `forall s finite_set:` already gives the finite-set typing for `s`, and `forall a s:` or `have a s` already gives `a $in s`. Prefer `forall s finite_set, a s:` over `forall s finite_set, a set:` plus a separate `a $in s` premise when the theorem is only about members of `s`.

9. Avoid proof scaffolding that only repeats the same proposition. When one
   named theorem application contributes one atomic fact, prefer
   `by thm theorem_name(args) => fact`, choosing the exact equality direction
   or representation consumed next. Use `release thm theorem_name(args)`
   only when several returned results are genuinely live or the needed result
   is not an allowed atomic target. Bare `by thm theorem_name(args)` remains
   supported for compatibility; it is not the recommended new-source spelling.
   Do not follow a release call with an identical
   conclusion line or wrap it in a `claim` / `?` goal block merely to expose
   that atomic result.

10. Avoid duplicate nearby facts such as repeating `$is_finite_set(T)` after it was just established, or writing both `finite_set_size(s) >= 1` and `finite_set_size(s) $in N_pos` when a typed binding such as `have n N_pos = finite_set_size(s)` can be made directly. Keep these restatements only when they are the smallest verifier-checkable bridge.

11. Prefer explicit intermediate equalities and facts over large proof jumps. Each line should be something the verifier can justify from the current context.

12. When a direct algebraic or numeric equality does not verify, first try adding more intermediate equalities instead of looking for a new theorem. Split the proof into small verifier-checkable steps: an algebraic identity, then local simplifications, then the final arithmetic. For example, do not stop at `(3 - 2 * sqrt(2)) * (3 + 2 * sqrt(2)) = 1`; try a chain like `(3 - 2 * sqrt(2)) * (3 + 2 * sqrt(2)) = 3^2 - (2 * sqrt(2))^2 = 9 - 8 = 1`, where the first step is polynomial simplification and later steps use small equalities such as `3^2 = 9` and `(2 * sqrt(2))^2 = 8`.

13. For zero-product arguments, prefer the explicit division step instead of a direct jump. If you know `u * v = 0` and `v != 0`, first write `u = 0 / v`, then close it with `u = 0 / v = 0`. Example: from `(2 * a - b) * (3 * a + b) = 0` and `2 * a - b != 0`, prefer `3 * a + b = 0 / (2 * a - b) = 0` over jumping straight to `3 * a + b = 0`.

14. Keep examples minimal but complete. Include required definitions, assumptions, and imports in the same runnable context.

15. Do not use `trust` to hide a proof obligation in an example. Use `trust` only when the example is explicitly introducing background mathematics, demonstrating known facts, or stating a deliberately assumed theorem.

## Dataset Translation To Litex

1. When translating a dataset problem into Litex, first reason about the mathematics of the problem before writing Litex code.

2. Do not mechanically translate Lean code, tactic steps, or theorem prover syntax into Litex. Use the source only as reference for the mathematical meaning.

3. After understanding the mathematics, design a Litex formulation that matches the current verifier and proof style of this repository.

4. Prefer the most Litex-native simple formulation as the main checked
   version. A formulation closer to the source text, or closer to Litex's raw
   underlying expression, is secondary unless the user explicitly asks for that
   comparison.

5. The translation process should be iterative: write a small Litex proof, run it, inspect the verifier output, and make the next smallest correction.

6. Before using `trust` or `abstract_prop`, first try at least one direct Litex formulation and use verifier feedback to narrow the gap.

7. If part of the formalization is temporarily blocked, it is acceptable to use `trust` or `abstract_prop` as a temporary placeholder, but only for the blocked part. Keep the rest of the proof explicit and checkable.

8. Prefer a mathematically natural Litex proof over a source-language-shaped translation. The goal is a verifiable Litex development, not a line-by-line transcription.

## Testing And Verification

### Litex execution routing

For all Litex work in this repository, distinguish mathematical artifact
verification from Rust unit testing and use the smallest release-mode
execution surface that proves the current claim:

1. Use `target/release/litex -lang en -f <registered-file.lit>` for a
   one-file baseline, checkpoint, or final gate. Registered `-f` executes the
   ordered prefix through its target. Require exit 0 and parsed Normal JSON
   with `kind: run`, `success: true`, and `session_error: null`. Add `-strict`
   when the intended artifact excludes user trust and axioms.
2. Use `target/release/litex -lang en -r <module>` only for an explicit
   whole-module, whole-book or repository-wide gate; not while iterating on
   one file. Read its overall success boundary from the current CLI contract.
3. Use one `-f <accepted-prefix.lit> -session` process and statement-by-statement
   source-order submissions for the inner proof loop. Follow the Session policy
   above for an unfinished registered target, journal ownership and restart
   recovery. Ordinary failures retain earlier accepted context. Keep a durable
   journal outside the process and materialize at coherent checkpoints.
4. Do not use default-profile `cargo test` as the Litex verifier. Use the
   release CLI; run focused `cargo test --release` gates only when the selected
   semantic impact justifies Rust testing.
5. Session reuse preserves accepted work and avoids rebuilding the same context
   for each candidate. It does not make an individual proof search cheaper by
   itself. The current CLI has no `-compact`, `-runner`, or `-before`, and no
   literal `try:` recipe is needed; consult `docs/cli.md` instead of older notes.

### Change-impact classification gate

Classify the change before selecting tests. Use semantic fan-out, not diff size:

- **L0 documentation-only:** comments or prose with no executable semantic
  change. Run only the touched documentation/snippet gate.
- **L1 leaf behavior:** one isolated builtin rule, infer rule, matcher branch,
  diagnostic case, or equivalent leaf implementation. Require the exact
  positive regression, the nearest executable negative boundary, and the
  directly affected runnable tracer. Do not run a family, examples/docs,
  To-Lean, or repository-wide suite merely for reassurance.
- **L2 subsystem behavior:** several leaves in one family or shared code
  confined to one subsystem, such as one parser family or one arithmetic-rule
  family. Run that subsystem's focused Rust tests and only its directly
  affected runnable artifacts.
- **L3 cross-contract behavior:** a boundary consumed by another subsystem,
  including proof evidence, well-definedness IDs/DAGs, `FactId` replay,
  runtime memo/rollback, compiler capture, module import state, or a public
  output contract. Run the focused producer and consumer contract suites.
- **L4 architecture:** a core AST/fact/object representation, global
  dispatcher, proof-search order, recursion policy, transaction/cache model,
  module system, public syntax, or test harness whose behavior fans out across
  several domains. Run the repository full-kernel gate.
- **L5 release:** version, dependency/toolchain, package, deployment, or
  release-candidate work. Run the full-release gate, including the explicitly
  registered real-Lean, textbook, and packaging gates.

Do not automatically promote L1 or L2 to L4. A large change within one leaf
may remain local, while a one-line change to a shared enum or dispatcher may be
architectural. Escalate only when inspection or focused-test evidence shows a
wider contract; record that reason. If a touched shared file cannot be
classified confidently, inspect its consumers before choosing the gate rather
than treating full testing as the default.

Before running tests, record this compact impact card in a progress update:

```text
Change class: <L0-L5 and name>
Affected domain: <domain>
Shared contracts changed: <none or exact contracts>
Focused tracer: <path/test>
Selected gates: <commands or suite names>
Explicitly skipped: <broader gates and why>
Escalation: <none or evidence-backed reason>
```

### Leaf builtin and infer-rule contract

A new or repaired builtin/infer rule is L1 only when it changes a leaf handler
or schema plus rule-specific tests/artifacts and does not change dispatch,
search order, recursion/fuel, cache/transaction state, evidence types,
compiler IR, or public output shape. Its required completion evidence is:

1. one exact positive Rust regression or generated rule-contract test;
2. one nearest executable negative boundary;
3. one direct release runner gate for the corresponding persistent `.lit`
   example/tracer.

For this L1 case, do not run `run_examples`, docs, `run_all`, all Rust tests,
or the To-Lean suite. If the rule has a paired generated Lean adapter, run only
that adapter's generated contract/real-Lean gate; do not promote it to the
whole To-Lean suite. Run To-Lean domain tests only when the change modifies
proof evidence, Litex-to-Lean IR/lowering/emission, a shared Lean theorem/ABI,
or explicitly adds compiler support. An unsupported builtin route must remain
an explicit fail-closed compiler result.

### Broader gates

- Run the examples harness only when a change affects the example collector,
  shared syntax/semantics used across examples, or several example artifacts.
  A single changed example normally needs only its direct runner gate.
- Run the Markdown/docs harness only when executable documentation changed or
  shared syntax/semantics can migrate existing snippets.
- Run `python3 scripts/textbook_gate.py The-Mechanics-of-Litex-Proof` only
  after changing that registered textbook, its runner, or a shared semantic
  contract known to affect it.
- Use a real To-Lean/Mathlib gate only for the To-Lean impact described above.
- Use a full-kernel gate only for L4, an explicitly requested repository-wide
  checkpoint, or an evidence-backed escalation. Use full-release only for L5.
- Do not infer coverage from a test name. In particular, the repository's
  current `run_all` entry may be an examples/docs aggregate rather than every
  Rust, compiler, Lean, textbook, and packaging gate. State the exact commands
  and coverage until a canonical full runner exists.

If a verifier failure occurs, report the exact file, snippet label, or line
shown by the test output before changing code. If any verifier or CLI output
looks strange, misleading, too indirect, or hard to understand, report it to
the user explicitly, including successful `verified_by` / explanation output.

## Documentation Rules

1. Any time you enhance a feature, check whether the documentation needs to be updated. If it does, update it in the same change.

2. If you change Litex syntax or semantics, update the documentation at the same time.

3. If a feature is new, put it into the preview feature section of the documentation.

4. Documentation claims about the verifier should be modest and evidence-based. It is fine to say a proof demonstrates a useful feedback loop; do not imply the theorem is difficult for mature proof assistants unless that is the point being argued.

5. For a kernel semantic change, audit documentation by role rather than by
   keyword alone. Search-order or automation-boundary changes normally affect
   Manual, FAQ, and the system map; explicit statement interfaces affect the
   Manual. When they change authoring decisions, update both
   `docs/cheatsheet.md` and the `litex-proof-writer` authoring cheat sheet.
   Removed implicit behavior affects every runnable Markdown/example proof
   shape, including README and comparison guides.

6. When automation is tightened, show the supported explicit migration at the
   original point of use and keep a focused negative example for the removed
   behavior. Do not make old snippets pass by adding unrelated assumptions or
   weakening their mathematical claim.

7. If a verification route gains a distinct public provenance label, update
   prose, detailed/JSON output expectations, summaries, and graph/trust
   descriptions together. Run the executable documentation harness; prose
   review or keyword search alone is not sufficient.

8. For semantic migrations, compare against a named baseline and classify the
   documentation diff as contract prose, executable proof migrations,
   output/provenance, or incidental cleanup. For each failed snippet, identify
   the lost route before editing: definition introduction normally becomes
   `by def`; a rule with quantified or compound requirements normally becomes
   explicit `by thm`; repeated, mathematically uniform constructor-decreasing
   decomposition may expose a missing builtin strategy, even when child and
   parent fact families differ; a non-structural semantic implication remains
   an explicit bridge. If many docs require the same mechanical bridge, pause
   the batch migration and audit the automation boundary instead of adding
   assumptions everywhere.

## Anti-Patterns

1. Do not make markdown examples pass only because prior snippets polluted the environment.

2. Do not add broad abstractions before a repeated pattern is clear.

3. Do not hide proof gaps by weakening examples or skipping tests unless the block is intentionally illustrative.

4. Do not change generated, temporary, or user-edited files unless the task requires it.
