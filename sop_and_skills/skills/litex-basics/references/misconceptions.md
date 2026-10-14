# Common misconception cards

Each card states the mistaken model, a concrete candidate, a checked route and
its boundary. Rejections are intentional; do not turn negative fixtures into
positive examples by adding assumptions or weakening the goal. Examples were
checked with the measured 1.0.7-beta executable; larger claims need a new check.

## M1. Rejection does not erase accepted context or prove a negation

**Mistaken model:** one wrong line invalidates the previous work, or the rejected
proposition has now been disproved.

Start `litex -lang en -strict -session -e 'have a R = 2'`. Enter `a = 3`
(rejected), then `a + 1 = 3` (accepted) in that same process. Repair only the
failed statement. Its rejection is not a newly stored `a != 3` proof.

**Boundary:** hard errors can terminate the process. A new process needs
accepted-source replay. A multi-statement input may contain committed successes.
Saved evidence: [quickstart](../examples/quickstart.lit) and the separate
interactive acceptance record in the hub's validation notes.

## M2. Defining a property proves no arbitrary instance

**Mistaken model:** after declaring `prop is_above_two`, every instance is known.
The [negative candidate](../examples/negative/property-instance.lit) declares
the property, then asks for `$is_above_two(1)`; it is rejected.

```litex
prop is_above_two(t R):
    t > 2
by def $is_above_two(3)
```

**Why:** definition folding checks the defining facts for that input.
**Boundary:** `abstract_prop` supplies a signature without such a body; it is
not a substitute for the intended mathematical definition.

## M3. A universal body is not an implicit list of hypotheses

**Mistaken model:** putting a fact first makes it an assumption. The
[unguarded universal](../examples/negative/missing-premise.lit) `forall x R:`
with only `x != 0` asserts that every real is nonzero and is rejected.

```litex
forall x R:
    x > 0
    =>:
        x != 0
```

**Why:** premises precede `=>:`; conclusions follow it. Without it all body
facts are conclusions. **Boundary:** premises and the binder are local to the
universal; neither creates a global `x` or a global positivity assumption.

## M4. A factual forall body cannot execute arbitrary proof commands

**Mistaken model:** a `witness` command can be pasted directly into the body of
any universal fact. The [negative form](../examples/negative/fact-body-command.lit)
is rejected. Put the command in an actual proof body:

```litex
claim:
    ? forall x R:
        exist y R st {y = x + 1}
    witness exist y R st {y = x + 1} from x + 1
```

**Why:** the claim activates the quantified goal's binder for its proof.
**Boundary:** an empty/decorative claim body is not a general escape; write the
real proof process. Named theorem bodies have their own optional-body contract.

## M5. A function's input domain is part of its interface

**Mistaken model:** the formula can be applied at any syntactically valid input.
[The zero call](../examples/negative/function-domain.lit) is rejected at WD.

```litex
have fn reciprocal(x R: x != 0) R = 1 / x
reciprocal(2) = 1 / 2
```

**Why:** the nonzero condition is checked before the result. **Boundary:** do
not redefine the function at zero to make the same theorem appear proved;
that would change the mathematics and needs an explicit design decision.

## M6. Existence alone is not uniqueness

**Mistaken model:** checking one witness proves `exist!`. The
[unique square-root candidate](../examples/negative/nonunique-witness.lit)
is rejected because `2` and `-2` both square to four.

```litex
witness exist w R st {w^2 = 4} from 2
witness exist! w R st {w = 2} from 2
```

**Why:** uniqueness concerns every satisfying candidate, not just the displayed
one. **Boundary:** `have fn ... by exist!` needs the complete unique-output
specification, not an existence claim with its quantifiers rearranged.

## M7. An arbitrary member is not a chosen numeral

**Mistaken model:** `have n N` secretly chooses the value needed next. The
[arbitrary-member candidate](../examples/negative/arbitrary-member.lit) then
asserts `n = 2` and is rejected. For the concrete value use `have n N = 2`;
for a universal law keep the variable arbitrary and prove that law.

**Boundary:** membership and nonemptiness information are not a specific value.
Check the source goal before specializing its input.

## M8. Claim helpers are local

**Mistaken model:** a name introduced inside a claim becomes a global object.
The [scope candidate](../examples/negative/local-name.lit) proves an existential
using a local `helper`, then refers to `helper` outside; the name is unavailable.
Use the exported existential through `obtain`, as in
[the existence example](../examples/existence.lit).

**Boundary:** a missing-name parse error can terminate a Session. It is not the
same recovery case as an ordinary rejected proposition; preserve and replay
accepted source if the process stops.

## M9. let is an alias, not mutable state

**Mistaken model:** mathematical `let name = expression` is an imperative
assignment to update later. It introduces an equality alias. Use a new name
for a different mathematical value; use a supported function/sequence interface
to describe variation. Replacing a committed declaration under the same name
can require a deliberate restart and replay.

**Boundary:** this card states the language role; the exact name-reuse diagnostic
depends on the target version. Consult its declaration contract before editing
an already accepted interface.

## M10. Acceptance and mathematical intent are separate questions

**Mistaken model:** an accepted file automatically proves the intended theorem.
Review actual carriers, premises, quantifier order, imported assumptions and
any `trust`/axioms. A statement about positive inputs or a scalar geometry model
has exactly that scope. A proof containing declared debt is not fully checkable.

**Boundary:** a historical receipt does not verify today's file or executable.
Use the read-only `litex-review` workflow when available, and keep the final
clean-file command and output with the source-owned evidence.

## M11. Loaded exports do not make their short names global

**Mistaken model:** after the prefix file runs, its `module_anchor` can be
written unqualified in any later export. In the [two-file module](../examples/modules/README.md),
the unqualified consumer is rejected; the checked consumer releases
`prefix::module_anchor` with `release obj def` before checking
`prefix::module_anchor + 1 = 3`. The qualified arithmetic alone was rejected
at WD in the measured consumer context.

**Why:** the producer's export namespace remains part of its identity, and
the consumer needs the object's defining facts available for its calculation.
**Boundary:** both namespace and loaded dependencies matter. Writing the
qualified name in a completely unrelated empty context does not import it.
