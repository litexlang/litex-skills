# Litex Problem Solving Workflow

**Historical end-to-end IMO geometry workflow: problem JSON to verified answer files**

---

## Workflow ownership and document responsibilities

This archived document is the single orchestration entrypoint for its problem-solving process. Specialist notes are read as needed and do not replace its ordering or whole-problem acceptance rules.

- Syntax/parsing: litex_syntax_quick_reference.md and its builtin appendix.
- Geometry translation/modeling: the translation specification, exact library-result matching, and geometry pitfalls/reserved names.
- Modules/paths: litex_cross_file_reference_mechanism.md.
- Proof construction/decisions: litex_proof_guide.md.
- Coordinate methods: litex_coordinate_solving_sop.md.
- Incremental debugging: the Session and historical REPL-try guide.

### Minimum reading before starting

1. Read this workflow and follow its stages.
2. Before formalizing, consult syntax and translation notes and inspect library_final.lit.
3. During proof construction, consult the proof guide.
4. Read coordinate, Session, REPL, or error-diagnostic notes only when relevant.
5. Check old commands, statistics, and cases against the chosen executable and the complete acceptance scope rather than trusting old text.

---

---

## Working environment

```bash
Working directory: <YOUR_WORK_DIR>/IMO
Problem JSON: Math_Problem/problems_natural_language.json
Designated geometry source: Litex/geo/library_final.lit
Output directory: solutions/problem_X/ (one directory per problem)
Historical executable: /Users/judy-zhu/.../<YOUR_LITEX_REPO>/golitex/target/release/litex
```

**Problem artifacts:**
```text
solutions/problem_X/
├── solution.lit                   # Single-part answer.
├── solution_part_a.lit            # First answer in a multipart problem.
├── solution_part_b.lit            # Second answer; extend for further parts.
├── predicate.lit                  # Shared custom predicates, if needed.
├── theorem.lit                    # Shared helper theorems, if needed.
├── litex.config                   # Shared sources and all answers in dependency order.
├── agent_session.log              # Runtime dialogue log.
├── litex_verified.json            # Whole-problem ordinary gate.
├── litex_strict.json              # Whole-problem strict gate.
├── litex_part_a_verified.json     # Part-a independent ordinary gate.
├── litex_part_a_strict.json       # Part-a independent strict gate.
├── litex_part_b_verified.json     # Part-b independent ordinary gate.
├── litex_part_b_strict.json       # Part-b independent strict gate.
└── README.md                      # Problem and workflow information.
```

Use solution.lit for one part. In multipart work, create separate solution_part_*.lit sources and exports from the start rather than overwriting one file with successive answers. Name reports for the actual parts, not only a/b.

---

## Stage 0: start full-dialogue capture (one minute)

The archived process requires capture before solving. Run it in a separate terminal:

```bash
cd <YOUR_LITEX_REPO>/generic agent

# Example: capture the complete prompt/response stream for problem 1.
python3 memory/Litex/start_full_logging.py 1
```

Recorded default output:

```text
<YOUR_LITEX_REPO>/generic agent/temp/Litex/result_simplify/verified/problem_1/agent_session.log
```

**Captured material:**
- Original prompt and response structure for each turn.
- Visible thinking, text, tool_use, and tool_result content.
- WORKING_MEMORY, timestamps, and model name.
- The response stream under temp/model_responses/.
- Adjacent metadata: source, byte count, stop reason, and SHA-256.

**Operational notes:**
- Start capture in one terminal and solve in another.
- By default, begin at the latest response file's end, recording only new material for this problem.
- Stop with Ctrl+C in the capture terminal so metadata is written and capture closes.
- Add --from-start to capture the current source from its beginning.
- Replacing an existing problem log requires explicit --overwrite.
- At completion, check that the tail covers final acceptance. A response file may rotate while capture still follows the old file. Capture the new source from offset zero into a separate agent_session_continuation*.log with its own metadata, source offset, and hash; record segment order in the problem README. To refresh a continuation, overwrite a complete snapshot rather than append: the old append metadata counts only the increment while its SHA covers the whole output, so file-size equality to bytes is not an integrity check.

---

## Stage 0.5: precheck the designated geometry library

Run an independent strict library gate before translating or proving, separating library domain errors from problem-proof errors.

**Library-edit boundary:** repair library_final.lit only when this independent gate locates a real error in the designated library. After it passes, problem difficulties must be handled in this problem's predicate, theorem, answer, or configuration files. Do not add library predicates, weaken premises, alter call semantics, or switch copies for convenience. A permitted library repair needs another independent strict gate before proof work resumes.

```bash
cd <YOUR_WORK_DIR>/IMO/Litex/geo
<YOUR_LITEX_REPO>/<YOUR_LITEX_REPO>/golitex/target/release/litex -runner -r . -all -strict -json > /tmp/library_final_strict.json
jq '{result, ok, error, target}' /tmp/library_final_strict.json
```

The historical gate requires result=success and ok=true. Predicates calling guarded functions such as angle_cos_num/den must supply their nondegeneracy conditions first. For not-well-defined errors, inspect the signature and error chain before changing the problem proof.

---

## Stage 1: extract the problem (two minutes)

### Extraction tool

```bash
cd <YOUR_WORK_DIR>/IMO

# Extract the problem and generate the complete template structure.
python3 /path/to/memory/Litex/extract_problem.py <problem_id>

# Show the problem without generating templates.
python3 /path/to/memory/Litex/extract_problem.py <problem_id> --no-template
```

**Generated files under solutions/problem_X/:**
- solution.lit: main answer template with translation reminders.
- predicate.lit: custom predicate template.
- theorem.lit: helper-theorem template.
- litex.config: module imports and export order matching problem_1.
- README.md: problem information and instructions.

The extractor generates this module configuration; the .lit templates do not contain file-level imports. Re-extracting an existing problem overwrites its templates, so inspect the destination before replacing a completed proof:

```toml
[hierarchy]
module

[import]
geo = "../../Litex/geo"

[export]
predicate = "./predicate.lit"
theorem = "./theorem.lit"
solution = "./solution.lit"
```

The geo module's main export must point to the designated original library_final.lit. Imports use module directories, not .lit paths or copy/hard-link aliases. Retain the geo namespace and predicate → theorem → solution ordering. Use the full stage-4 gate and report strict versus trusted-import results separately.

Read the complete problem and count its parts immediately. Give each part its own answer source and export; keep shared definitions and helpers in predicate.lit/theorem.lit. Do not overwrite an earlier solution with a later part. Preserve the full source problem in each answer header when requested, while proving only that file's part.

Hash existing formal sources before continuation. Add an export for a new part without rewriting an old answer. Complete the whole-module gate and any requested independent-part gates. Use new, semantically accurate report names and do not overwrite earlier reports.

---

## Stage 2: formalize (15–30 minutes)

### 2.1 Define geometric objects

```litex
have a, b, c cart(R, R):
    # NL: Points A, B, C
```

### 2.2 Define real parameters

```litex
have r, rho R:
    # NL: circumradius r, inradius rho
    r > 0
    rho > 0
```

### 2.3 Express conditions as predicates

```litex
prop conditions(a, b, c, r, rho cart(R, R)):
    # NL: Triangle ABC is isosceles with AB = AC
    distance_sq(a, b) = distance_sq(a, c)
```

### 2.4 Express the goal as a predicate

```litex
prop statement(o, i, r, rho cart(R, R)):
    # NL: d = sqrt(r(r - 2*rho))
    distance_sq(o, i) = r * (r - 2 * rho)
```

**Main rules:**
- Align each NL comment with one Litex statement.
- Translate the given facts in prop definitions without adding reasoning.
- Reuse geometry predicates only from the designated library_final.lit; do not switch libraries or aliases. Define a missing relation in this problem's predicate.lit.
- Imports require module directories. Check the export points to the original source. If that configuration cannot load, report the blocker and obtain the project-code authorization needed to fix it rather than silently selecting another library.

---

## Stage 3: prove (30–60 minutes)

### 3.1 Construct the main theorem

```litex
thm problem_X:
    forall a, b, c, r, rho cart(R, R):
        conditions(a, b, c, r, rho) => statement(...)
--
    # Proof here
```

### 3.2 Choose a proof method
**Prefer a synthetic geometry route in this archived workflow.**

**Synthetic route:**
1. Use existing geometric predicates; define a genuinely missing one in predicate.lit.
2. Use existing library theorems; prove a genuinely missing helper in theorem.lit.

**Coordinate route:**
1. Choose a coordinate system.
2. Compute coordinates.
3. Simplify.

### 3.3 Proof patterns, with the historical writing SOP

## Example
```litex
have fact_1: some_property
    by thm some_theorem

claim step_1:
    target_equation
    --
    # detailed proof
```

---

## Stage 4: verify (10–30 minutes)

### 4.1 Run verification and retain output

**Historical complete-module gate, tested on problem_1 on 2026-09-22:**

1. Confirm all problem sources are exported, dependencies precede consumers, and each answer's namespace matches its export key.
2. Run the following command from the problem directory. The recorded -r gate covers all exports; -f covers only the prefix through a file. Historical -isolated and -target debug modes do not establish complete acceptance.

```bash
cd <YOUR_WORK_DIR>/IMO/solutions/problem_X/
<YOUR_LITEX_REPO>/<YOUR_LITEX_REPO>/golitex/target/release/litex -runner -r . -all -json > litex_verified.json
```

**Separate ordinary and strict results.** Ordinary success is relative to the listed trusted imports; -all reports warnings without removing trust. For a no-assumptions delivery, run strict mode on the same module separately:

```bash
<YOUR_LITEX_REPO>/<YOUR_LITEX_REPO>/golitex/target/release/litex -runner -r . -all -strict -json > litex_strict.json
jq '{result, ok, error, target}' litex_strict.json
jq -r '.trace' litex_strict.json
```

Inspect strict results and all expected exports. A strict failure in the original library is a library blocker, not a completed strict proof. Retain litex_strict.json separately from the ordinary report, without switching entrypoints to hide the error.

#### Multipart acceptance at two levels, tested on problem_2 on 2026-09-23

1. The formal whole-problem module must export shared dependencies and every answer. Retain ordinary and strict reports. Joint loading does not establish that an individual part was checked independently.
2. When independence matters, create a disposable sibling module under solutions/, containing unchanged shared sources and only the target answer. Do not nest it in the formal problem directory: the old problem_2 experiment found a parent-configuration conflict there, while a sibling isolated successfully.
3. Run ordinary and strict complete gates in that temporary module and save part-specific reports in the formal problem directory. Do not overwrite whole-problem evidence.
4. A filename is not evidence. Check result=success, ok=true, and the complete trace. All target-part theorems must appear; other parts' main and exclusive helper theorems must not. Explain ordinary trusted imports separately from strict results.
5. Check formal-source SHA-256 before and after the temporary gate. Delete only the module created for this attempt after confirming unchanged hashes. Keep the formal sources and all evidence classes; no wildcard cleanup.

### 4.2 Inspect results

```bash
cd <YOUR_WORK_DIR>/IMO/solutions/problem_X/

# Inspect structured results and read the trace's dependencies and checked theorems.
jq '{result, ok, error, target}' litex_verified.json
jq -r '.trace' litex_verified.json
# Ordinary acceptance requires result=success, ok=true, and every expected export/theorem.
# Absence of trust in an answer file does not prove zero trust in imported dependencies.
```

### 4.3 Debug errors

**Use the parser to inspect the complete error chain:**

```bash
cd <YOUR_WORK_DIR>/IMO/solutions/problem_X/

# Recursively format every previous_error.
python3 '<YOUR_LITEX_REPO>/generic agent/memory/Litex/parse_litex_error.py' litex_verified.json
```

**Common diagnostics, following the historical decision guide:**
- cannot prove goal: inspect missing proof steps.
- unknown fact: inspect references to nonexistent facts.
- type mismatch: inspect predicate argument types.
- module not found: inspect import paths.

---

## Stage 5: stop capture and archive (five minutes)

### 5.1 Inspect trust in the sources and their dependencies

```bash
cd <YOUR_WORK_DIR>/IMO/solutions/problem_X/
# Search direct trust only; this does not establish zero trust in imports.
grep -n 'trust' -- solution*.lit predicate.lit theorem.lit 2>/dev/null
```

Report trusted imports from the stage-4 trace. Complete no-assumptions acceptance requires strict mode on the same module; record a library blocker honestly rather than relabeling ordinary success as zero trust.

### 5.2 Stop logging

Press Ctrl+C in the capture terminal.

If the wrapper is in the background, identify its unique imo_litex_log.py capture child by process relationships and send SIGINT only to that child. A targeted signal to the wrapper may not propagate while it waits in subprocess.call. Confirm both exit, then confirm the log size stops growing.

### 5.3 Clean disposable debugging artifacts
Enumerate candidates first and inspect ownership and purpose. Do not delete by filename pattern or touch other problems or shared tools at the IMO root.

```bash
# List candidates from any directory; this command does not delete them.
find <YOUR_WORK_DIR>/IMO/solutions/problem_X -maxdepth 1 -type f \( \
  -name 'DEBUGGING_*.md' -o -name 'VERIFICATION_*.md' -o \
  -name 'temp_*' -o -name 'test_*' -o -name '*_DEBUG*.md' \
\) -print
```

Inspect every candidate and git status for this problem. Remove only confirmed disposable task artifacts. Retain user files, formal tests, logs, and unexplained changes; ask when their ownership is unclear instead of wildcard deletion.

### 5.4 Final artifacts

List the problem directory. Retain the single answer or all part answers/exports, config, ordinary whole-problem evidence, used predicate/theorem files, log, and problem information. Also retain any strict and independent-part reports, including failures and library blockers. Mark a misleading old report superseded; remove it only after a correct replacement exists and it is no longer referenced. A filename absent from this list is not a reason to delete its file.

### 5.5 Quality checks

1. Inspect result, ok, error, and trace with jq, checking every expected export/theorem. Counting text lines containing success is not acceptance.
2. Merge reusable experience into existing syntax, translation, reference, or workflow documents. Keep problem source, evidence, and necessary logs locally; old retry counts, commands, or success statistics do not establish current acceptance.
3. For uncertain syntax, inspect the reference and isolate one feature in a minimal probe for parsing, ordinary checking, and strict behavior. One failure does not establish an entire syntax rule.
4. Report direct trust and imported trust separately in ordinary/strict results.
5. Confirm complete, stopped capture. Retain and disclose unresolved failures; a tidy directory does not mean the proof is complete.

---

## Stage 6: review the log and maintain reusable knowledge

In the original workflow this stage is required after each problem, once stage 5 confirms capture has stopped. Do not update experience while the log is still being written.

### 6.1 Review the task log

Typical historical location:

```text
<agent_root>/temp/Litex/result_simplify/verified/problem_<id>/agent_session.log
```

Extract actual recorded events rather than reconstructing from memory. Inspect:

1. The first error, issued command, and eventually verified correction.
2. Wrong assumptions that caused rework: treating prefix checks as full acceptance, overwriting answers, confusing trust modes, or using unverified syntax.
3. Rules confirmed by the chosen executable or successful tool use that may transfer to another problem.
4. Unresolved failures, library blockers, and details specific to this task.

Only category 3 nominates a reusable lesson. Categories 1/2 inform diagnosis; category 4 stays in task logs and evidence rather than becoming a general rule.

### 6.2 Merge into existing documents

Organize by topic; do not create a problem_<id>_lessons_learned.md, standalone lessons file, or duplicate SOP:

| Topic | Existing destination |
|---|---|
| Syntax, parsing, names, and proof syntax boundaries | litex_syntax_quick_reference.md |
| NL translation, predicate choice, and public theorem interface | litex_formalization_sop.md or litex_solution_translation_spec.md |
| Geometry modeling and coordinates | litex_geometry_pitfalls.md or litex_coordinate_solving_sop.md |
| Cross-file references, exports, configuration, and paths | litex_cross_file_reference_mechanism.md or litex_path_and_environment.md |
| Local proof moves, strategies, and automation boundaries | litex_proof_writing_sop.md, litex_proof_decision_rules.md, or litex_builtin_verification_skills.md |
| Session/REPL incremental debugging | litex_session_verification_sop.md or litex-repl-try-workflow.md |
| Complete workflow, logging, acceptance, archiving, and updates | This document |

Choose one specific stable owner for a lesson and link it elsewhere instead of copying. Do not promote task IDs, retry counts, temporary paths, or one-off bridge theorems into a universal SOP.

### 6.3 Check before and after updating

1. Read the existing destination and choose an insertion point without overwriting or duplicating guidance.
2. Write only concise rules supported jointly by logs and tool results, not guesses, unsuccessful trials, or unverified syntax.
3. Reread the new passage and inspect git diff -- memory/Litex; confirm no problem-specific lessons/SOP file appeared.
4. If no reusable new rule exists, retain task evidence without changing guidance.

In this archived process, completion includes stage 6. Start the next problem at stage 0 with a new log and select its required documents afresh.

---

## References to consult while solving

### Verification failures
- litex_proof_writing_sop.md: proof patterns and debugging checklist.
- litex_proof_decision_rules.md: cannot-prove-goal decision tree.
- litex_builtin_verification_skills.md: recorded automation support.

### Specialist situations
- litex_coordinate_solving_sop.md: coordinate geometry.
- litex_session_verification_sop.md: Session and trust tracking.
- litex-repl-try-workflow.md: interactive REPL debugging.
