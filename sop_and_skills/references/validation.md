# Import validation — 2026-10-13

This edition was checked with the existing Litex 1.0.6-beta release executable
identified in [source provenance](sources.md). It was not rebuilt during this
import; correspondence to the modified sibling source tree is not established.
All commands below used that executable and English output.

## Representative reference path

An independent skill-creator usage check started from the hub README, chose
reference/proof/modeling guidance and exercised a reciprocal function in an
external standalone project. It found a stale Manual statement claiming the
application-value seed was necessary. The bundled Manual was narrowly updated;
the original sibling Manual was not edited.

Before, the documentation described these excerpted steps as necessary:

```litex
# x and reciprocal belong to the full R01 context.
# reciprocal(x) = 1 / x
# reciprocal(x) * x = 1
```

Now the exact complete R01 block was checked with `litex -strict -lang en -e`
and returned exit 0, `kind: run`, `success: true`, `session_error: null`:

```litex
have fn reciprocal(x R: x != 0) R = 1 / x
forall x R:
    x != 0
    =>:
        reciprocal(x) * x = 1
```

Appending `reciprocal(0) = 0` was rejected at `well_defined`, with a nonzero
exit and no hard Session error. This supports the exact guarded reciprocal
example, not arbitrary recursive function-body expansion. A separate negative
`forall x,y R: |x-y| < |x-y|` was rejected at proof search.

## Saved source and module gates

These mathematical gates ran before the directory reorganization. The recorded
relative paths now belong to sop_and_skills/, and the mathematical/config
sources retain their exact bytes. Each small source used `litex -strict -lang en -f <path>`.
Both passing modules used `litex -strict -lang en -r <path>` at their actual
bundled directory. Every passing result had exit 0, `success: true` and a null
Session error.

| Artifact under references/litex/ | Outcome |
| --- | --- |
| examples/claim_obtain_scope.lit | strict pass |
| examples/have_fn_by_unique_existence.lit | strict pass |
| examples/object_definition_equalities.lit | strict pass |
| examples/proof_nodes/atomic/by_builtin_rule/abs_difference_triangle.lit | strict pass |
| examples/proof_nodes/atomic/by_builtin_rule/less_equal_finite_set_size_subset_wd.lit | strict pass |
| examples/proof_nodes/equal/by_builtin_rewrite/fn_application_unfold_substitution.lit | strict pass |
| showcases/Write_Mathematically_Correct_Code_With_Litex | complete configured strict pass |
| showcases/math_concepts_in_litex/3_number_theory | complete configured strict pass |
| showcases/The-Mechanics-of-Litex-Proof | parse failure at citation.lit:68 |
| showcases/math_concepts_in_litex/2_sets_functions_and_relations_in_nutshell | parse failure at main.lit:37 |

The last two are deliberately retained as historical references and visibly
marked in their README and the corpus index. Their mathematical sources are
unchanged. These are observed version/source-alignment failures; this import
does not diagnose a kernel defect or perform a proof migration.

The Mechanics failure reaches an older case form:

```litex
# Excerpt of the original citation theorem:
# by cases:
#     ? b != 0 or a != 0
#     case a != 0
#     case b != 0
```

The sets/functions failure rejects the empty extension body:

```litex
# Excerpt of the original theorem:
# by extension:
#     ? union(first_set, second_set) = {1, 2, 3, 4}
```

## Session preservation

A standalone prefix containing `have anchor N = 7` was loaded with
`litex -lang en -f <prefix> -session`. In that process `1 = 2` failed at
`search_proof`, returned a null Session error and another prompt; `anchor = 7`
then succeeded. The independent reciprocal check likewise observed a failed
zero-domain call followed by a successful `reciprocal(-2) = -1 / 2` in the same
Session. No claim is made about every registered-export or hard-error boundary.

## Package checks

- Skill Creator's quick validator accepted all 16 skill entrypoints.
- The package checker validated skill names, local Markdown file links,
  2,846 packaged source hashes and 205 labeled receipt summaries.
  This checker validates file destinations, not every heading anchor or remote URL.
- A complete copy outside the source layout passed the same checker. Adding
  an intentional missing Markdown target made the checker fail with that target.
- Git whitespace checks passed. Before English localization, the original IMO
  package's tracked content was checked against its moved historical copy.
  English localization subsequently changed prose and helper text; mathematical
  sources and configuration files retain their exact bytes.

These gates do not rerun the equality skill's full historical corpus or its
receipts, validate handwritten Lean comparisons, install/run Generic Agent,
resolve its legacy logger dependencies, or establish the GitHub resources
remote's public name/availability. Each receipt summary remains historical.

## SOP/skill and agent-example layout check

Shared content is now under sop_and_skills/. The Generic Agent usage guide,
memory pointer and original agent-specific IMO archive are under
generic_agent_example/. All sixteen skill entrypoints and the mathematical/config
sources were checked unchanged during the move. Internal links, provenance
paths, the content checker and the memory pointer were adapted to the layout.

From the repository root, the relocated checker is:

```sh
python3 sop_and_skills/scripts/check_hub.py
```

It passed on the complete two-directory layout. A detached copy also passed
when invoked from an unrelated working directory; removing its bundled CLI
reference made the checker reject the missing target. These are layout and
package checks, not a new rerun of the mathematical or agent-runtime gates.

## English localization check

Navigation, SOPs, skill notes and historical helper text were converted to
English. Three equality overview filenames were normalized, their references
updated, and packaged hashes refreshed while original source hashes were retained.
A text scan found no remaining Chinese prose: the remaining Chinese text in
Markdown consists of localized JSON output examples and literal upstream paths.
Source problem data and historical receipts remain in their original languages.

A hash comparison against the pre-translation package confirmed that all 2,532
Litex, configuration and data files were unchanged (excluding provenance metadata).
The historical error parser was exercised with success, nested failure and
missing-file fixtures and produced English labels. The extractor generated
English template instructions; generated Litex statement bodies and configuration
matched those produced by the original helper. These checks cover localization
and preservation, not current compatibility of the historical tool workflow.

The final English layout passed the package checker with 16 skills, 1,656 local
Markdown file links, 2,846 snapshot hashes and 205 historical receipt summaries.
All 16 skill entrypoints passed Skill Creator's quick validator.
