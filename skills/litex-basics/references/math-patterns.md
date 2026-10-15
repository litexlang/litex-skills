# Syntax and common mathematical patterns

The linked `.lit` files are complete runnable sources. Code excerpts here are
self-contained unless explicitly called schematic. Treat the measured examples
as examples, not a promise about every generalization or executable version.

## Algebra and order

```litex
forall x R:
    (x + 1)^2 = x^2 + 2 * x + 1
```

Arithmetic expressions and fact chains state mathematics to verify; they are
not assignments. State a simple result directly before adding proof commands.
For an inequality supply the actual domain/sign assumptions. The
[algebra topic](topics/algebra.md) covers calculation steps and cancellation.
Source: [quickstart](../examples/quickstart.lit).

## Predicates and conditional statements

```litex
prop is_above_two(t R):
    t > 2
by def $is_above_two(3)

forall x R:
    x > 0
    =>:
        x != 0
```

`prop` introduces a condition; `by def` establishes the displayed positive
instance. Premises above `=>:` are local assumptions for its conclusions.
Without the arrow the body asserts every listed fact. Proof commands are
not allowed as arbitrary entries in a factual `forall` body.
Source: [logic](../examples/logic.lit).

## Sets, members and finite cases

```litex
have S set = {1, 2}
1 $in S

by enumerate finite_set:
    ? forall x {1, 2}:
        x > 0
    x > 0
```

The displayed set is the carrier of the finite check. A variable of type `set`
is a set-valued object; a variable ranging over `S` is a member of that set.
Do not treat an arbitrary set/member as an explicitly chosen finite value.
Source: [sets](../examples/sets.lit); deeper [sets/functions topic](topics/sets-functions.md).

## Products, tuples and coordinates

```litex
have points set = cart(R, R)
have fn vec(A, B cart(R, R)) cart(R, R) = (B(1) - A(1), B(2) - A(2))
have p cart(R, R) = (1, 4)
p(1) = 1
p(2) = 4
```

`cart(A, B)` is the Cartesian product. Coordinates are `p(1)`, `p(2)`.
Never encode \(R\times R\) as `R * R`, and never use `p.1` / `p[1]`.
Source: [products](../examples/products.lit).

## Functions and reusable laws

```litex
have fn reciprocal(x R: x != 0) R = 1 / x
thm reciprocal_product:
    ? forall x R:
        x != 0
        =>:
            reciprocal(x) * x = 1
    reciprocal(x) = 1 / x
    reciprocal(x) * x = (1 / x) * x = 1
by thm reciprocal_product(2) => reciprocal(2) * 2 = 1
```

The callable domain excludes zero. The theorem uses its own active binder
`x`; it does not introduce a global `x`. The selected conclusion must be one
returned atomic fact. The explicit body illustrates a real derivation; a named
theorem does not need a decorative body when its goal already verifies.
Source: [functions](../examples/functions.lit).

| Call | Effect |
| --- | --- |
| `release thm name(args)` | Publish every instantiated conclusion (and ordinary consequences). |
| `by thm name(args) => fact` | Store only `fact`, which must **match a returned atomic conclusion** (structural/α). |

`by thm ... =>` does **not** reverse an equality, rewrite arguments, or combine
conclusions. If the theorem returns `q = p` and you need `p = q`, select `q = p`
(or `release`) and add another step; do not put the flipped equation on the
arrow. Rejected control:
[by-thm-equality-orientation.lit](../examples/negative/by-thm-equality-orientation.lit).

## Existence, use and uniqueness

```litex
witness exist w R st {w^2 = 4} from 2
obtain root from exist w R st {w^2 = 4}
root^2 = 4
witness exist! w R st {w = 2} from 2
```

Giving `2` proves existence of a square root of four, but does not prove a
unique real square root. `obtain` checks its source existential; it does not
invent an unproved witness. Source: [existence](../examples/existence.lit).

A witness can depend on a universal parameter:

```litex
claim:
    ? forall x R:
        exist y R st {y = x + 1}
    witness exist y R st {y = x + 1} from x + 1
```

Choose it inside the active parameter scope. This exports the quantified fact,
not a global `x` or `y`. See [existence](topics/existence.md) and
[logic/scope](topics/logic-scope.md) for the next level.

## A sequence as an indexed function

```litex
have fn successor(n N) R = n + 1
successor(2) = 3
```

A natural-indexed function expresses a sequence of values. This example checks
a concrete value; it is not a convergence theorem. `N` includes zero in the
measured version. Use the live subject module when limits, sequence carriers or
reusable analysis interfaces matter. Source: [sequences](../examples/sequences.lit).

## Induction and modules

The [induction example](../examples/induction.lit) proves `2^n >= n + 1` from
a base and a step. Read [the topic](topics/induction.md) before adapting binder
or recursion shapes. For several files use [the module topic](topics/modules.md)
and [the two-file module](../examples/modules/README.md); preceding registered
exports are part of the target's context.
