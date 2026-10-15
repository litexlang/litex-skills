# Mathematical collections

This module demonstrates dependency context, not a new mathematical abstraction.
The sole public object is `module_anchor R = 2`; its defining equality supplies
the arithmetic fact used by `main.lit` through `prefix::module_anchor` after
`release obj def prefix::module_anchor`. The intended source order is definition,
explicit release of the exported object's definition, then use. No supporting
theorem, existence assumption or proof debt is needed.

The nearest rejected interpretations omit the producer context or use its
unqualified short name in another export. Merely qualifying the name does not
release its defining facts for arithmetic. A registered file gate includes the
configured preceding export; the consumer uses its canonical namespace and
releases the definition. This is the interface lesson; it is not evidence of
arbitrary module imports or persistent storage across processes.
