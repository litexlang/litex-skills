# Litex Cross-File Reference Mechanism

**Historical summary from debugging IMO 1960 Problem 3**

---

## Main findings

### Predicates can be used across files

**Mechanism:**
```litex
# Configure the export in litex.config.
[export]
predicate = "./predicate.lit"

# Define the predicate in predicate.lit.
prop my_predicate(x, y R):
    x * x + y * y = 1

# Reference it in solution.lit, with the required $ prefix.
$predicate::my_predicate(a, b)
```

**Historical verification:**
- problem_207 defined predicates in translation.lit.
- solution.lit successfully used `$translation::is_right_triangle(...)`.

### Theorems can be cited across files

Order `theorem = "./theorem.lit"` before `solution = "./solution.lit"` in `[export]`. Use `by thm theorem::my_theorem(x, y)` without a $ on its name. IMO problem_1 cited central_coordinate this way and passed the recorded `-runner -r . -all -json` gate.

---

## File organization

### Structure tested in IMO problem_1

```
solutions/problem_X/
├── predicate.lit         # New predicates only when the library lacks them.
├── theorem.lit           # New helper theorems and proofs.
├── solution.lit          # Final problem statement and answer.
└── litex.config          # Exports ordered by dependency.
```

Use `$predicate::name(...)` and `by thm theorem::name(...)` for earlier exports. Prefer the designated library's predicates over expanded coordinate premises or conclusions.

---

## litex.config

**Order existing exports by dependency:**
```toml
[export]
predicate = "./predicate.lit"
theorem = "./theorem.lit"
solution = "./solution.lit"
```

Paths are relative to litex.config. Follow the actual problem's dependencies; include both theorem and solution when they exist.

---

## Common errors and repairs

- `by thm $theorem::my_helper_theorem(a)` is incorrect: omit $ from the theorem name and use `by thm theorem::my_helper_theorem(a)`.
- If theorem::... is missing, check the theorem.lit export, its position before solution.lit, and the exact name and arguments.
- An old misuse of $theorem:: led to the false conclusion that helpers must be inline. The recorded problem_1 later passed with cross-file theorems; do not migrate lemmas based on the obsolete claim.

---

## Reference cases

### problem_207: cross-file predicates

```
problem_207/
├── solution.lit          # Uses $translation::is_right_triangle(...).
├── translation.lit       # Defines is_right_triangle.
└── litex.config          # [export] predicate = "./translation.lit"
```

**Key points:**
- translation.lit defines a prop, not a thm.
- solution.lit can use `$translation::is_right_triangle(...)`.
- This old case used translation.lit; new predicates in this archived project belong in predicate.lit.

### IMO 1960 Problem 3: predicates and helper lemmas

The configuration exports predicate.lit, theorem.lit, and solution.lit. Calls such as `by thm theorem::central_coordinate(...)` connect the helpers. Six lemmas and the main theorem passed ordinary module verification, with external geo imports trusted. The earlier all-inline state was obsolete debugging history.

---

## Historical module verification commands

**From more than 115 debugging rounds on IMO 1960 Problem 3, 2026-09-22**

### Whole-problem acceptance through all configured exports

Check imports, names, and export order in solutions/problem_X/, then follow stage 4 of the archived workflow for its complete module gate:

```bash
<YOUR_LITEX_REPO>/<YOUR_LITEX_REPO>/golitex/target/release/litex -runner -r . -all -json > litex_verified.json
jq '{result, ok, error, target}' litex_verified.json
jq -r '.trace' litex_verified.json
```

A -f FILE gate checks only the prefix through FILE; -target likewise narrows debugging scope. An old translation.lit success does not prove the whole problem passed. For fact-not-defined errors, inspect export order, names, and target scope before concluding cross-file use is unsupported. Report ordinary-mode trusted imports from the trace and check strict mode separately.

---

## Best practices

### 1. Predicates

- This archived workflow permits only IMO/Litex/geo/library_final.lit as its geometry source, not another library or same-content alias, including a hard link. Check the imported module's export points to that file.
- If it lacks a needed predicate, define one in this problem's predicate.lit rather than borrowing another geometry library.
- Configure `[export] predicate = "./predicate.lit"`.
- Use `$predicate::prop_name(...)` in solution.lit.

### 2. Theorems

- Put new helpers and proofs in theorem.lit, exported before solution.lit.
- Keep the final statement and proof in solution.lit, citing helpers as `by thm theorem::bridge_1(...)`.
- Do not prefix theorem names with $ in by thm.

### 3. Responsibilities

predicate.lit defines missing relations, theorem.lit proves helpers, and solution.lit states and proves the final problem. Stage 4 owns complete acceptance.

---

## Interface checks before cross-file calls

Inspect each exported interface before treating a failed reference as a language limitation:

- Match the theorem's parameter count, order, and types exactly.
- Dependencies precede their consumers in exports. Check actual export names and namespaces, not merely file existence.
- A local -f success checks a prefix, not all configured exports.

## Summary

Use $predicate::name for predicates and by thm theorem::name for theorems. Check interfaces and export order, verify the entire module, and report ordinary/strict trust boundaries separately.


---

## Path and environment lookup

### Main paths

```bash
# Working directory.
cd <YOUR_WORK_DIR>/IMO

# Litex executable.
<YOUR_LITEX_REPO>/<YOUR_LITEX_REPO>/golitex/target/release/litex

# Geometry library.
Litex/geo/library_final.lit

# Problem JSON.
Math_Problem/problems_natural_language.json

# Output directory.
solutions/problem_X/
```

### Common path errors

**Error 1: executable not found**

Symptom: `litex: command not found`.

Use the full executable path:
```bash
<YOUR_LITEX_REPO>/<YOUR_LITEX_REPO>/golitex/target/release/litex \
  -runner -r . -all -json > litex_verified.json
```

**Error 2: library_final.lit not found**

Run from the IMO directory:
```bash
cd <YOUR_WORK_DIR>/IMO
grep "is_right_angle" Litex/geo/library_final.lit
```

**Error 3: inconsistent working directory**

Use IMO as the workspace root and relative paths for the library and problems.

---

**Environment requirements:**
- Working directory: IMO root.
- Paths in a problem's litex.config are relative to that problem directory.
- Geometry import paths follow the IMO workspace layout.
