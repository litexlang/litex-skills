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

## Session authoring emphasis — 2026-10-14

The maintainer's authoring rule is now prominent in navigation, relevant skill
entrypoints, the geometry SOP, the Generic Agent task prompt and the shared
Session references. The live golitex guides' simpler comparison was preserved
and adopted by the hub and installed authoring profiles.

This focused check used the existing sibling release executable, reporting
`Litex 1.0.7-beta`, with SHA-256
`f98a3454895f291d8b75f39bced13a4c2b727c8d46e756399af8d102c8031a84`.
It was not rebuilt; current-source correspondence remains unestablished.
These results supplement the dated import checks rather than replacing them.

Start with `litex -lang en -session -e 'have a R = 2'` and submit each
statement separately in the same process:

```text
litex> a = 3
... rejected at search_proof; the prompt returns ...
litex> a + 1 = 3
success
```

The failure line summarizes the diagnostic. The observed rejection envelope
had `run_result: "failure"`, `session_terminated: false`, `termination: null`
and no stored or inferred facts. Repeating `a = 3` still failed; another
`a + 1 = 3` succeeded in that same process. Thus the rejected equality did
not become accepted knowledge, and the earlier declaration remained available.
The original opaque-predicate example was also checked: `$ready(8)` failed,
`$ready(7)` succeeded, and another `$ready(8)` still failed in one Session.

Compare independent processes:

```bash
litex -lang en -e 'have a R = 2'
litex -lang en -e 'a + 1 = 3'
```

The second process exited 1 with an undefined-name parse termination: it had
no `a`. Replaying `have a R = 2` followed by `a + 1 = 3` in a clean strict
`-e` run restored context and passed. This negative is a deliberate fresh
process boundary, distinct from the ordinary proof rejection above.

The [saved accepted prefix](session-accepted-prefix.lit) passed:

```bash
litex -lang en -strict -f sop_and_skills/references/session-accepted-prefix.lit
```

This clean file run exited 0 with `kind: run`, `run_result: "success"`,
`session_terminated: false` and `termination: null`. A Session that contains
rejected input can exit 1 with an aggregate failure even after later successful
statements; that does not erase its accepted context. The final saved artifact
therefore uses a separate clean gate. These checks establish the demonstrated
context and restart boundaries; they make no speedup or proof-discovery claim.

The same rejection/success pair also ran in one strict `-f` Session opened
from the saved accepted prefix. The package checker passed with 16 skills,
1,678 local links, 2,846 recorded snapshot hashes and 205 historical receipt
summaries. All seven modified installed skill entrypoints and all eight
modified hub entrypoints passed Skill Creator's quick validator. Original
source paths/hashes were compared with the repository baseline and preserved;
both repository whitespace checks passed. No kernel, textbook or Lean suite
was needed for this documentation change.

## Live corpus reading routes — 2026-10-14

The reference skill now reads the live paired checkout before bundled snapshots,
using level 0 for Session/context, level 1 for local examples, level 2 for a
selected mathematical development, and level 3 for exact contracts/controls.
The level is chosen by the current question, rather than a mandatory sequence.
Proof/modeling/translation/calculation/definition/migration/kernel entrypoints,
navigation, the geometry SOP and the Generic Agent example use this route.

The hub-relative root and the installed skill's independent absolute hint both
resolved to the actual sibling golitex checkout. All 28 distinct corpus paths
named in the router/topic guide were checked to exist. The shared reference
skill and reading guide were compared byte-for-byte with the installed copies;
the personal location hint remains installation-specific.

Manual navigation dry-runs used these representative questions:

| Level | Question | Live sources actually read | What the reading established |
| --- | --- | --- | --- |
| 1 | How is a function constructed by unique existence? | `examples/have_fn_by_unique_existence.lit` | Relation, existence/uniqueness proof, function declaration and downstream uses are available together. |
| 2 | How does one function participate in a proof and executable cases? | `showcases/Write_Mathematically_Correct_Code_With_Litex/README.md`, `math_collections.md`, `litex.config`, `main.lit` | The actual export is `main`; the definition/trajectory share `newton_sqrt_two_step`, with an explicit exact-real versus floating-point boundary. |
| 3 | Does a failed candidate erase context, and how does a file start a Session? | `docs/cli.md`, Session Flag and Project Modules; the Manual's relevant function-section headings | Ordinary rejection retains accepted context; a successful file prefix continues into a Session; registered export order matters. |

All nine modified hub skill entrypoints and all nine installed entrypoints
passed Skill Creator's quick validator. Package checks and whitespace checks
passed. Original imported source hashes and historical evidence were preserved.
These are location, integrity and manual navigation checks, not an independent
agent-behavior evaluation or a new verification of every cited proof. No Litex,
Rust, whole-book or Lean semantic suite was needed for this routing-only change.

## Layered authoring edition — 2026-10-14

The approved implementation adds `litex-basics` and read-only `litex-review`.
The foundation teaches the working model, execution, major syntax, ordinary
mathematics and common misconceptions. Six mathematical topic guides load on
demand. Task entrypoints select the relevant guides and live reference depth;
maintainer skills are selected separately through the profile manifest.

The [structured journal](validation/skill-layers-2026-10-14.json) records actual
Session candidates, accepted blocks, failed attempts, source hashes, clean
file results, exporter checks and installed synchronization. Verification used
the existing 1.0.7-beta executable with the same SHA-256 recorded above; it was
not rebuilt, so correspondence to the current Rust checkout is unestablished.

- **Persistent authoring:** reciprocal definition, evaluation, inverse theorem,
  witness/property/set/induction patterns were submitted to the live authoring
  Session. `reciprocal(0)` was rejected while later valid reciprocal facts
  succeeded in that same process. A uniqueness claim for a real square root of
  four was rejected; an existence witness and simple equality uniqueness passed.
- **Session boundary:** the process exited 1 after `quit`, reflecting expected
  rejected candidates, with `session_terminated: false` and `termination: null`.
  This aggregate result does not make the Session an accepted artifact. The
  saved positive files were checked separately. The two independent `-e`
  commands in the foundation comparison were also checked: the second had no
  declaration of `a` and terminated at parsing, as expected.
- **Saved source:** all 17 foundation `.lit` fixtures met their declared
  expectation under clean `-lang en -strict -f` checks: nine positives passed;
  eight intentional negative controls were rejected at the documented boundary.
  The configured module consumer passed after explicit `release obj def`.
  Earlier unqualified/qualified-only failures remain recorded; qualification
  alone did not establish arithmetic WD facts in that consumer context.
- **Portable packs:** actual basics (1 skill), default author (12 skills) and
  explicit maintainer (18 skills) exports passed selected Markdown dependency
  closure and all copied-file hash comparisons. Both lightweight packs' 17
  fixtures were checked outside the source repository without a sibling golitex
  tree. They contain no maintainer skills, full language snapshots, expanded
  source guides or historical evidence archives. The full maintainer pack also
  passed the hub checker in its exported layout.
- **Destination protection:** exporting again refused existing destinations
  without changing any bytes. A dangling symlink, unknown profile and output
  inside the source repository were also refused before creating output.
- **Skills/installations:** all 18 hub entries and 13 new/updated personal
  entries passed Skill Creator's quick validator. New basics/review and the
  shared reference router match source. Narrow routes were inserted into ten
  personal skills while preserving their previous bodies and the separate
  personal corpus-location hint.
- **Preservation:** the package checker passed skill/profile membership, local
  file dependencies, all 2,846 recorded snapshot hashes and 205 historical
  receipt summaries. All original imported source paths/hashes were compared
  to the repository baseline and preserved. Whitespace checks passed.

These checks establish the demonstrated syntax, failure boundaries, packaging
and installed routes. They do not constitute an independent agent-behavior
study, prove every historical theorem, or establish a proof-search speedup.
No kernel, whole-book or Lean suite was run: this change adds teaching material
and a local export helper without modifying the language implementation.

## Generic Agent geometry reproduction — 2026-10-14

The [agent example](../../generic_agent_example/README.md) now follows one
concrete problem from pinned upstream installation to shared skill loading,
persistent authoring, saved proof and fixed-goal verification. Its
[validation record](../../generic_agent_example/validation/README.md) contains
the actual public-source release build, fresh core-agent dependency installation,
headless entrypoint smoke check, real tool-branch Session integration and ten
acceptance/control checks. No model API inference was performed.

The new reference edge-length proof passed strict verification with the pinned
public Litex 1.0.6-beta build; it does not use the archived paraphrase's extra
distinct-edge premise. The unchanged final goal rejects unrelated correct
code, a separately valid weakened theorem and a trusted version. Existing-run,
changed-input, wrong-revision and unknown-JSON boundaries were checked. Hard
parse termination and accepted-prefix replay were checked separately from
ordinary rejection with retained context.

This evidence establishes the prepared workflow and reference theorem at the
stated geometric interpretation boundary. A reader's real Generic Agent/model
run remains a separate experiment and must supply its own outcome and costs.
All prior historical imports and their recorded hashes are retained.
