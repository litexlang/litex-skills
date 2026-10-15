# Induction and recursive constructions

Use for an indexed invariant or recursive construction. First distinguish the
mathematical function being defined from an induction proving a proposition;
one does not supply the other's obligations.

The [complete checked induction](../../examples/induction.lit) proves
`2^n >= n + 1` for `n N`: the base is `n = 0`; the step derives the next
inequality from the current induction hypothesis. Read the entire claim and
its active binders before adapting it.

1. Establish the actual index carrier and starting value. `N` includes zero
   in the measured version; use a different intended domain explicitly.
2. State an invariant that the downstream goal actually consumes.
3. Prove the base independently and use the induction hypothesis only inside
   the step where it is available.
4. In the step, separate the recurrence equation from arithmetic/order work.
   Supply necessary domain and nonzero conditions for recursive applications.
5. For a recursive function, inspect the current supported declaration and
   decreasing/coverage obligations in live docs/examples. Do not assume that
   every mathematically terminating definition or nested binder shape is
   implemented by the measured verifier.
6. Read a relevant showcase's source and recorded limitations for a larger
   construction. Concrete unrolling, induction and general recursive
   definitions establish different scopes; label the actual one.

The introductory example does not establish all forms of recursion or general
induction automation. A blocked true construction remains an explicit gap;
do not silently replace it by a weaker finite case or a trusted result.
