# Litex Kernel Map

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.


Common directories:

- `src/parse/`: tokenizer and parser.
- `src/stmt/`: statement data structures.
- `src/obj/`: object and expression structures.
- `src/fact/`: fact structures and matching support.
- `src/runtime/`: environment mutation, instantiation, and execution support.
- `src/execute/`: statement execution.
- `src/verify/`: verification dispatch and rule checks.
- `src/verify/verify_builtin_rules/`: builtin mathematical rule implementations.
- `src/infer/`: inferred facts after storing or checking facts.
- `src/pipeline/`: CLI/REPL/file running and output rendering.
- `std/`: Litex standard-library files.
- `examples/`: runnable regression and demonstration examples.

Start by searching for a nearby existing rule or statement type. Follow its shape unless there is a clear reason to introduce a new pattern.
