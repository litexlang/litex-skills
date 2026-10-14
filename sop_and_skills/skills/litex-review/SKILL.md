---
name: litex-review
description: Review Litex mathematical meaning, domains, proof completeness, assumptions and verification evidence without changing source. Use when asked to audit or assess whether a Litex artifact establishes its intended mathematics.
---

# Litex review

Review is read-only by default. Read [the foundation](../litex-basics/SKILL.md)
and [misconception cards](../litex-basics/references/misconceptions.md) when
unfamiliar with the language. Use [live reference routing](../litex-reference/SKILL.md)
for exact contracts and the relevant mathematical topic.

1. Anchor the intended mathematical statement, actual source, dependencies,
   executable and requested scope. Separate the user's intention from the
   proposition the file actually expresses.
2. Inspect carriers, guards, nondegeneracy, quantifier order and witness
   dependencies. Look for vacuous premises, a scalar/special-case model
   presented as a general theorem, or conclusions weakened to obtain acceptance.
3. Inspect the real proof route and any `trust`, axioms or abstract interfaces.
   A defined predicate is not an assumed instance. Distinguish a checked proof,
   an explicit assumption and surviving proof debt.
4. Check evidence at the needed scope: an old receipt is dated, a Session is
   context-dependent, and a saved-file check must use its actual configuration.
   Run a read-only focused CLI gate when permitted; otherwise state what is
   unverified. Do not run a whole book for a local review without a reason.
5. Report actionable findings with the smallest relevant code, source location,
   observed behavior and mathematical consequence. Label verified issues,
   suspected defects and missing evidence separately. If proposing a change,
   show the proposed code but do not apply it as part of a read-only review.

Acceptance has two independent questions: did the verifier accept the source,
and does that accepted statement represent the intended mathematics? Passing
one does not answer the other. Check downstream use when an interface matters.

Use `litex-proof-writer` for an authorized proof repair, `litex-concept-modeler`
for an unsettled definition, and `litex-example-migration` for version drift.
Kernel repairs require their own task and applicable maintainer policy.
