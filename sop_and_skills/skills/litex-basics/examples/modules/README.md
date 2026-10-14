# Ordered two-file module

`prefix.lit` introduces `module_anchor R = 2`; the registered `main.lit`
uses the export-qualified name to check `prefix::module_anchor + 1 = 3`. The configuration lists
the prefix before its consumer. There are no user axioms or trust statements.

Inside the producer file the local name is `module_anchor`. Another export
uses `prefix::module_anchor` and releases that object's definition before
using its value/type facts in arithmetic. The unqualified consumer is an
expected rejection; the qualified arithmetic alone also lacks WD evidence
in the measured consumer context. The active main file records both steps.

From this directory, with the chosen Litex executable on PATH:

```bash
litex -lang en -strict -f main.lit
litex -lang en -strict -f prefix.lit -session
```

The first is a clean registered file gate. The second is the authoring entry;
submit new statements there one at a time. In a source checkout the executable
may be an absolute `target/release/litex` path. See
[the mathematical design](math_collections.md) and
[the module topic](../../references/topics/modules.md).
