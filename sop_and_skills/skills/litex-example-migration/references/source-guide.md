# Imported source guide

Source snapshot imported on 2026-10-13. Read this for the author's mathematical methods and scoped repository conventions. Historical CLI recipes and result fields are not current execution instructions; use [the hub execution contract](../../litex-reference/references/execution.md). Apply golitex-specific paths and maintainer rules only when working in that repository. Dated examples require replay before making a current-support claim.


# Litex Example Migration

Use this framework throughout finding problems, investigating them, reporting
them, and discussing intended behavior with the user. It records the user's
requested review method, not a claim that every category is a current defect.
Apply `golitex-repository-policy` in golitex; use `litex-kernel-engineer` for
authorized kernel work and `litex-proof-writer` for authorized proof edits.

## Two independent classifications

For automatic-search versus explicit-proof findings, use the shared
[search and explicit proof boundary](../../golitex-repository-policy/references/search-explicit-proof-boundary.md).
Report expression, explicit checkability and automatic discovery separately.
A checked same-target authoring route may satisfy the maintainer's contract
while a shortcut remains unsupported; it does not erase a separately observed
defect. Keep true unsupported goals distinct from false/invalid negative
controls, and do not silently reverse fixture expectations.

For each finding, distinguish **why behavior differs** from **where the first
unsupported boundary occurs**. These classifications supplement existing
`trust` / `kernel_problem` blocker labels; do not replace their documented use.

Root-cause assessment:

- **Intended semantic change:** the new WD, carrier, domain, nondegeneracy, or
  other mathematical contract deliberately differs.
- **Intentional capability limit:** an interface was removed or an implicit
  proof route was deliberately restricted; the mathematics may be unchanged.
- **Migration omission:** a still-required legacy capability, publication,
  dispatch arm, or producer/consumer contract was not fully transferred.
- **Implementation defect:** current behavior violates an established current
  contract, including false acceptance, state corruption, or operational failure.
- **Legacy/example defect:** the old proof lacked premises, used accidental
  context, or passed through an unsound old verifier route.
- **Environment/tooling drift:** source, binary, configuration, dependencies,
  documentation, output expectations, or test collection are out of alignment.
- **Undetermined:** reproduction is established but cause or intended contract
  is not. Keep competing hypotheses visible instead of guessing a bug label.

Locate the earliest failing phase: parsing/binding, WD, verification search,
explicit proof execution, storage/inference, scope/transaction, module/cache,
computation, evidence/output/replay, or launch/test tooling. Name the earliest
owner and retain downstream symptoms as consequences of that finding.

## Repair ownership in plans

Alongside cause and earliest phase, apply the maintainer's
[two execution categories and discussion boundary](../../golitex-repository-policy/references/task-sop.md#bug-repair-plan-ownership)
whenever writing or updating a plan: Litex authoring improvement, or justified
local Rust semantic repair. Keep nonlocal proposals in needs discussion;
mark unknown scope provisional and investigate it. A migration omission may
be local or architectural, so its cause label does not establish permission.
A scan remains read-only unless repair is in the authorized task scope.

## Twelve diagnostic facets

Use these facets to organize a requested system scan. They overlap; assign a
primary facet and add secondary ones only when evidence warrants them.

| Facet | Questions that change the diagnosis |
| --- | --- |
| 1. Semantic contracts | Did object WD, an exact carrier, callable domain, nonempty requirement, or partial-operation precondition change? Is the change explicitly intended? |
| 2. Syntax and public interfaces | Did syntax, a builtin name, a declaration form, config layout, or a public feature change or disappear? Separate deliberate removal from missing migration. |
| 3. Capability coverage | Check calculation, builtin rules, builtin strategies, definition/object-definition, known facts/forall, rewrites, user strategies, infer rules, explicit proof commands, and required library interfaces separately. A builtin inventory is not full verifier coverage. |
| 4. Search policy | Did route order, depth, recursion permissions, rewrite eligibility, or cycle guards change? A present rule may be unreachable under the caller's state. Separate intended limits from accidentally lost routes. |
| 5. Wiring and composition | Does the feature work alone but fail inside a template, compound object, or nested proof? Trace dispatch, verification, publication, storage/inference, and later use; a successful declaration or stored fact alone does not prove the whole path works. |
| 6. Representation and matching | Compare equivalent orientations, literal versus alias/template expressions, bound-variable renaming, free-symbol identity, canonical keys, substitution, and dependent parameter types. Mathematical equality and syntactic identity are different contracts. |
| 7. Scope and state lifetime | Check parent/local visibility, branch and induction scopes, assumption leakage, rollback of parse bindings as well as execution state, commit behavior, ID lifetime, and reuse of failed-search evidence. |
| 8. Modules and caches | Compare local, qualified, cross-file, and imported use; definition ownership, export order, ID remapping, cache invalidation, and cold versus cached imports. Respect the actual imported definitions/facts visibility contract. |
| 9. Legacy/example correctness | Was the old statement well-defined and justified? Did it omit a premise, rely on earlier examples, or exploit a false-proof route? Correct rejection must not be restored to old acceptance. |
| 10. Computation and availability | Separate wrong computation/reduction from normal search failure, runaway recursion, stack overflow, timeout, or expensive valid search. Test relevant boundary values and use the release profile for runtime measurements. |
| 11. Evidence and output contracts | Check WD, FactId dependencies, local environments, winning proof routes, Normal/Detailed output, summaries, and downstream replay. Verification, correct explanation, and Lean export are distinct completion claims. |
| 12. Execution and test drift | Check binary/source baseline, launch flags, config/import/std context, fixture expectations, test collection, skipped items, and actual test counts. Expected known failures or zero selected tests do not establish capability success. |

## Investigation protocol

1. Anchor the user's scope and the intended mathematical/current language
   contract. Identify the actual artifact, owning config/import context, current
   source and release binary, and a named legacy baseline if available. Mark a
   missing or incomparable baseline explicitly.
2. Inspect current launch help/parser and harness before choosing commands.
   Old skill recipes such as `-runner`, `-compact`, `-before`, or `try:` are
   not evidence that the current executable supports them. If they are absent,
   report the drift and use the supported release execution surface; preserve
   isolation, source order, rollback, and journal requirements as applicable.
3. Reproduce the unchanged failing source in its real context, then reduce it
   without dropping relevant premises/imports. Record the exact command,
   process status, supported top-level success/session-error fields, statement
   outcomes, and earliest failed phase. Do not equate a parser/launch failure
   with mathematical rejection.
4. Trace the producer and consumer of the first missing obligation or evidence.
   Compare the former route with the current owner when history is available.
   Distinguish a missing leaf rule from a rule that exists but cannot be called,
   a fact that is never published, and a published fact that cannot be matched.
5. Classify root cause, phase, diagnostic facet, and observed symptom. Symptoms
   include incorrect rejection, incorrect acceptance, runtime failure, output
   mismatch, or fixture/tool mismatch. Keep observations, hypotheses, user
   decisions, historical results, and verified repairs separate.
6. Group downstream failures by their independently established upstream cause.
   Do not repair every caller separately when one shared boundary explains them.
   Do not force unrelated failures into a shared cause merely because they look
   similar. For an authorized repair, re-derive the downstream behavior from the
   corrected owner and apply that task's acceptance gates.

Do not insert `trust`, extra assumptions, weaker goals, unrestricted search, or
an object-specific dispatch exception to make a migration reproduction pass.
Preserve the failed assertion as evidence. A separate authorized proof-writing
task may track localized trust under repository policy, but that never closes
the original migration finding or establishes checkability.

## Reporting and discussions with the user

For every distinct finding or behavior decision, provide a compact issue card:

- **Code and observation:** the actual minimal Litex/Rust snippet, context,
  exact failure or state transition, source link, and tested baseline. Label
  an unrun illustration or historical result explicitly.
- **Classification and evidence:** root assessment, first failing phase,
  primary facet, and what supports the assessment. State what is still unknown.
- **Expected behavior:** derive it from established mathematics, current
  contract, or explicit user intent. Old acceptance alone is insufficient.
- **Next action or decision:** identify the upstream owner and smallest useful
  check. If a user-owned semantic/architectural choice remains, show each
  material option with code and its effect on the same case, including WD,
  soundness, compatibility, proof authoring, and evidence/replay consequences
  where relevant. Do not ask a generic "fix this?" before making the issue
  concrete; honor decisions and authorization already present in the session.

Use this same framing when proposing problems, investigating them, or talking
through them. A scan request authorizes investigation and concrete findings;
follow the user's actual requested scope for implementation. Keep protected
AST/Env/Runtime changes behind their existing authorization boundaries.

## Scan and acceptance boundaries

- For a whole-system scan, cover owners and their boundaries, not just statement
  names or leaf-rule counts. Include representative composition and context
  checks: direct/alias/template, renamed binders, local/qualified/imported,
  success/failure rollback, strict/nonstrict where relevant, and cold/cache use.
- Pair a restored positive with the nearest case that must still reject. Check
  invalid types/domains, false conclusions, missing premises, and scope leakage
  relevant to the change. A passing example alone does not establish soundness.
- Preserve known limitations and intended rejections as such. A manifest runner
  that expects a gap to fail can pass while the gap remains open. Report tested
  coverage and residual findings; do not call them all fixed.
- Select gates by the repository impact policy and the user's requested scan
  scope. A local finding does not automatically justify every full-system gate.
- Issue records are maintained observations, not permanent bug-status truth.
  Recheck them against the named current baseline before making current claims.
