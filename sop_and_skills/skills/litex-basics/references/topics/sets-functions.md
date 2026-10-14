# Sets, mappings and callable interfaces

Use when a carrier/member distinction or function interface is central.
Keep three roles separate: a set of possible inputs, one member, and a callable
function. A predicate describes a condition rather than returning a value.

```litex
have S set = {1, 2}
1 $in S
```

The [set example](../../examples/sets.lit) also checks each displayed finite
member by enumeration. A set-valued variable does not automatically specify a
finite enumeration or choose a member for a later calculation.

For an expression-defined callable interface:

```litex
have fn reciprocal(x R: x != 0) R = 1 / x
reciprocal(2) = 1 / 2
```

1. Establish the intended input and output carriers and concept-owned guards.
2. Decide whether later code needs a value, callable function, relation or
   bundled structure. Preserve the intended mathematics before choosing syntax.
3. Probe one intended call and the nearest invalid input. A checked formula
   at `2` does not make the function total at `0`.
4. Reuse the actual application/specification facts when composing interfaces.
   Do not create a predicate wrapper only to imitate a callable value.
5. For set/function equality or function spaces, read the matching live examples
   and extensionality contract; the syntax of a function expression alone does
   not supply the needed equality proof or all domain obligations.

Use `litex-concept-modeler` when installed for reusable interfaces, and
`litex-strict-definitions` for their exact domain contract. The live showcase's
README/design/configuration comes before adapting a larger module.
