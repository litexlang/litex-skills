# Logic, premises and scopes

Use when the next correction concerns a quantified statement, local assumption,
proof body or unavailable name. Separate the fact being proved from commands
that establish it.

```litex
forall x R:
    x > 0
    =>:
        x != 0
```

Without `=>:` both facts would be asserted for all real inputs. The binder and
the premise here remain local; they do not create a global positive real `x`.

```litex
claim:
    ? forall x R:
        exist y R st {y = x + 1}
    witness exist y R st {y = x + 1} from x + 1
```

The [logic example](../../examples/logic.lit) uses the goal's active binder
inside its proof. The claim exports the quantified fact, not a global `x`/`y`.
A factual `forall` body cannot contain arbitrary proof commands. Refer to
misconception cards M3/M4/M8 for executable rejection controls.

1. Write the intended binder order and local hypotheses before implementation.
2. Check whether each line is a fact or a proof command.
3. Use the active goal binder; avoid a renamed duplicate universal that merely
   repeats the target instead of deriving it.
4. Track the scope of introduced helpers and witnesses. Extract an exported
   existential through `obtain` instead of using a hidden helper name.
5. For cases or contradiction use the target version's exact proof-command
   form, with a nonempty mathematical proof process. Do not infer arbitrary
   Boolean grammar from a supported flat `and`/`or` spelling.

A rejection is not a proof of the opposite proposition. Diagnose syntax, WD
and proof failure separately. Use live Manual/CLI sections for an exact boundary.
