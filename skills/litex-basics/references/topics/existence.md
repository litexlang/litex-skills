# Existence, unique existence and selection

Use when witnesses depend on parameters, uniqueness is needed, or an existence
specification should become a reusable function. Preserve the quantifier order.

```litex
witness exist w R st {w^2 = 4} from 2
obtain root from exist w R st {w^2 = 4}
root^2 = 4
```

This [complete example](../../examples/existence.lit) distinguishes supplying
a witness from extracting a name. `obtain` checks its source; it is not a way
to assume an unproved existential. `exist!` also needs uniqueness. The
[negative control](../../examples/negative/nonunique-witness.lit) must fail.

1. State the full target, including carriers and each witness dependency.
2. Supply a concrete witness or derive an existential through an actual
   established interface. Put real intermediate reasoning in its proof body.
3. Choose the witness inside the scope of parameters it depends on; see
   [the dependent witness](../../examples/logic.lit).
4. When uniqueness is required, compare arbitrary satisfying candidates, not
   just the chosen witness. Existence of a square root does not make it unique.
5. For `have fn ... by exist!`, inspect the live
   `examples/have_fn_by_unique_existence.lit` through `litex-reference`.
   Verify its full input-to-unique-output specification before declaration.
6. Use the resulting property interface at the selected value; do not invent
   an expression body for a function specified only by unique existence.

After the source is verified, keep the mathematical selection interface clear
for downstream callers. A reusable construction decision belongs to
`litex-concept-modeler`; a local witness belongs to the current proof.
