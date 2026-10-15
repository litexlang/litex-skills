# Litex Problem Solving: Historical SOP and Skills Package

Packaged: 2026-10-12 09:21:16
Task: Problem 16 (IMO 1968 P4), the tetrahedron edge-length triangle inequality.

This is an English edition of the archived package. Its recorded syntax and
commands are historical; use the shared skills and version-matched execution
contract for current work. The mathematical resources remain unchanged.

## Package layout

### Litex/: workflow documents and tools

Main workflow and navigation:

- `litex_problem_solving_workflow.md`: the archive's single six-stage workflow.
- `START_HERE.md`: document navigation.

Syntax and translation:

- `litex_syntax_quick_reference.md`: syntax and builtin reference, updated in the original task.
- `litex_solution_translation_spec.md`: solution translation requirements.
- `litex_geometry_pitfalls.md`: geometry pitfalls and reserved identifiers.

Proof and debugging:

- `litex_proof_guide.md`: proof mechanisms and decision rules, updated in the original task.
- `litex_coordinate_solving_sop.md`: coordinate-solving SOP.
- `litex_incremental_debugging_guide.md`: Session/REPL incremental debugging.

Cross-file use and paths:

- `litex_cross_file_reference_mechanism.md`: module references and path lookup.

Tools:

- `extract_problem.py`: extract a problem and generate its directory structure.
- `start_full_logging.py`: start the archive's full-dialogue capture before solving.
- `parse_litex_error.py`: recursively extract the complete error chain.

### reference_resources/: source material

- `citation.lit`: proof examples from The Mechanics of Litex Proof.
- `library_final.lit`: geometry axioms and definitions, without proofs.
- `problems_natural_language.json`: IMO problem data.

## Updates recorded by the original task

### Contradiction pattern in litex_proof_guide.md

The task recorded the complete `by contra:` constraints, the restriction on
have/obtain/release in its body, and a full `? forall ... =>:` example.
These are historical observations, not guarantees about a newer verifier.

### Syntax quick reference

The original update recorded that the `--` separator was no longer needed,
summarized contradiction constraints, and linked to the proof guide.

## Historical findings

1. `by contra:` was recorded inside the theorem body, indented four spaces at
   the same level as `? forall`, followed by a restated `? <goal>`. Its body was
   described as equality/inequality chains ending in `impossible`, without
   have, obtain, release, by def, or by thm statements.
2. `--` was absent from library_final.lit; the recorded syntax moved from a
   theorem declaration directly to its proof strategy.
3. library_final.lit supplied axioms rather than proofs. Actual proof patterns
   were taken from citation.lit and other textbook sources.

## Reading and tool order

The archived entrypoint is `Litex/litex_problem_solving_workflow.md`.
Use `Litex/START_HERE.md` to find a relevant document and citation.lit for
uncertain syntax. The original tool order was start_full_logging.py,
extract_problem.py, then parse_litex_error.py.

## Path configuration

Replace the placeholders before attempting to reuse an archived tool:

- `<YOUR_LITEX_REPO>`: the Litex repository root, for example
  `/path/to/LITEX-Geo/original/Geometry-Codex`; the recorded executable was
  `<YOUR_LITEX_REPO>/golitex/target/release/litex`.
- `<YOUR_WORK_DIR>`: the problem workspace, for example
  `/path/to/LItex_vs_Lean_new-2/IMO`, containing Math_Problem and solutions.

The original configuration checklist names Litex/extract_problem.py and its
executable-path variable, the cross-file guide's paths, and the main workflow's
paths. Inspect the actual variable names in the retained scripts when reusing them.

```text
<YOUR_LITEX_REPO>/
├── golitex/target/release/litex
└── ...

<YOUR_WORK_DIR>/
├── Math_Problem/
│   └── problems_natural_language.json
├── Litex/geo/
│   └── library_final.lit
└── solutions/
    └── problem_X/
```

Originally generated after Problem 16 (IMO 1968 P4) was completed.
