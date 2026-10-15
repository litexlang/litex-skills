# Equality, algebra and order

Use when a calculation jump, cancellation or estimate fails. Start with the
actual domains/signs and the mathematical argument, not a search for a theorem
name. Keep one authoring Session and consume its exact feedback.

The [quickstart](../../examples/quickstart.lit) checks:

```litex
forall x R:
    (x + 1)^2 = x^2 + 2 * x + 1
```

1. State the natural direct fact with the required premises.
2. If it fails, identify whether the expression is well-defined or proof
   evidence is missing. Check the exact input and first failing phase.
3. Split a genuine mathematical jump into intermediate equalities; each link
   must follow from accepted context. Avoid repeating already accepted facts.
4. **Repair loop:** change only the first rejected fact. Insert a smaller
   equality or lemma call immediately before it. If the same jump fails twice,
   split again; do not rewrite the whole proof with the same oversized step.
5. Prefer an existing `release thm` / `by thm ... =>` interface over re-expanding
   the same algebra at the call site. Hand expansion belongs in a lemma body or
   when no suitable interface exists.
6. For cancellation, make the nonzero/sign condition available before the
   consuming equality. Preserve factor positions; do not assume arbitrary
   reassociation or alias matching is one direct inference step.
7. For an estimate, identify the bound, its domain and the order-preserving
   operation. A false special input is a useful control, not proof debt to hide.
8. Verify downstream use of the resulting equality direction/representation.
   `by thm name(args) => fact` must use a directly returned atomic conclusion;
   it does not reverse an equality. To reverse, `release` or select the returned
   orientation, then write a separate step (see
   [by-thm orientation](../../examples/negative/by-thm-equality-orientation.lit)).

When installed, `litex-equality-inequality` owns calculation cleanup and dated
case selection. Use `litex-reference` for the live `examples/proof_nodes/` and
`examples/infer/` families; read a specific Manual contract when unclear.
Old case receipts supplement the live source, not current verification.

The [reciprocal law](../../examples/functions.lit) shows a guarded calculation
inside a reusable theorem. Its nonzero premise must survive any simplification.
Stop once the next justified step is known; return to the proof Session.
