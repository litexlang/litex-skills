# Imported source guide

Source snapshot imported on 2026-10-13. Read this for the author's mathematical methods and scoped repository conventions. Historical CLI recipes and result fields are not current execution instructions; use [the hub execution contract](../../litex-reference/references/execution.md). Apply golitex-specific paths and maintainer rules only when working in that repository. Dated examples require replay before making a current-support claim.


# Litex Equality and Inequality

Write the mathematical argument with the fewest useful author steps supported
in the real context. Shorter source is not automatically faster; do not claim
globally minimal proofs.

## Choose a part

For a compact overview of implemented selections, checked shortcuts and
remaining observations, read [problem status](problem-status.md).

For the first two layout examples, read [two pilot cases](two-example-pilot.md). They separate existing concise support from a proposed subtraction rule.

Select a mathematical topic in the [case index](parts-index.md).
Read only the chosen index section and its relevant Parts.

- [Algebra and order](parts-index.md#algebra-and-order).
- [Absolute values and neighborhoods](parts-index.md#absolute-values-and-neighborhoods).
- [Roots powers logarithms and factorials](parts-index.md#roots-powers-logarithms-and-factorials).
- [Integers rounding and modulo](parts-index.md#integers-rounding-and-modulo).
- [Finite sums and products](parts-index.md#finite-sums-and-products).
- [Functions coordinates and expression transport](parts-index.md#functions-coordinates-and-expression-transport).
- [Sets intervals and extrema](parts-index.md#sets-intervals-and-extrema).
- [Quadratics and derivative proofs](parts-index.md#quadratics-and-derivative-proofs).
- [Newton iteration and numerical bounds](parts-index.md#newton-iteration-and-numerical-bounds).
- [Probability and statistics](parts-index.md#probability-and-statistics).
- [Trigonometric interfaces](parts-index.md#trigonometric-interfaces).

These are dated cases, not an exhaustive rule catalogue. Load only the
relevant card. Replay its examples when relying on their recorded capability.

## Solve or simplify

1. Establish the domains, premises and short mathematical proof idea. Preserve
   the statement; do not manufacture premises to shorten it.
2. Look for existing builtin support or a genuinely reusable mathematical
   interface. Try the natural direct target before expanding a manual trace.
3. If that fails, try the shortest meaningful equality/order chain or supported
   explicit proof. Locate the first failed phase: a search miss is not a
   mathematical counterexample.
4. Test removal of the entire candidate waterfall in the original enclosing
   context, then check downstream consumers. Restore only the necessary bridge
   demonstrated by failure. Retain conceptual reader explanations in teaching.
5. Record source, negative controls, exact commands and binary identity. State
   unknown source correspondence. Never add trust to label a pilot checkable.
   Measure time only when performance is claimed, with equal binary/context.

In golitex apply `golitex-repository-policy`; use `litex-proof-writer` for the
broader workflow. Current `docs/cli.md` governs commands. Keep a live release
Session across ordinary failed statements, without historical `try:`,
`-before`, `-compact`, or `-runner` recipes. Final file acceptance requires
exit 0 and Normal `kind: run`, `success: true`, `session_error: null`.

## Distinguish support from improvement opportunities

When proposing kernel additions from the search, honor the
[user-selected candidates](selected-bt-candidates.md).
Keep historical evidence separate from selection and implementation status.

Every part separates ideal direct form, current verified form, checkable but
verbose source, mathematical negatives, true-but-unsupported direct targets,
and bounded improvement candidates. Missing premises, invalid domains and
false strictness are different from capability misses. Current bridges are
not permanent authoring requirements.

For an improvement candidate identify trigger, generated obligations and
soundness boundaries. Kernel work is a separate scoped task using
`litex-kernel-engineer`; this skill does not authorize kernel edits by itself.

Arrange each part as mathematical situation, proof idea, positive, verbose
comparison, negatives, capability gap and evidence. Use self-contained code
or link the exact full context; label excerpts and untested proposals.
General technical recommendations beyond these scoped cases need independent
evidence and held-out acceptance, not one successful repair.
