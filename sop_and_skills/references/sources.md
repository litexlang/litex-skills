# Source provenance

Imported on 2026-10-13. Original installed skills and sibling repositories were
read only. This hub edition has concise task entrypoints; the source skill
bodies and supporting author notes remain dated reference material.

| Source | Recorded state | Role |
| --- | --- | --- |
| Installed Codex Litex skills | File hashes in [provenance.json](provenance.json) | Fifteen imported authoring, helper and maintainer skills |
| [golitex](https://github.com/litexlang/golitex) | HEAD `e6f0fb6cab0bb69f99eb9a33b30deceae6d0a74a`; local working tree has modifications | Selected docs, six small sources, two passing complete modules, two historical modules with observed version issues, upstream LICENSE |
| Local directory litex-resources | HEAD `d0a1141b2b7055d3d874dea83620695f843758be`; local working tree has modifications; origin `https://github.com/litexlang/litex-doc.git` | Inspected distribution; a duplicate full corpus was not copied |
| Existing release executable | `Litex 1.0.6-beta`; SHA-256 `ce0e84f4fefe60d3acf0ed64a74c7dd9fda7a01fc947da1f4208e71c52b3dee0` | Help/version and focused package checks; current-source build correspondence not established |
| [Generic Agent](https://github.com/lsdefine/GenericAgent) | Upstream link only | One independently installed example agent |

The curated documents came from the current local worktree, not necessarily
the exact committed HEAD bytes. Per-file source and packaged hashes distinguish
that state; the compiler guide was among locally modified documents. Missing
upstream material links to the recorded commit when its path is tracked.
This import does not claim that all referenced upstream links were fetched.
GitHub availability/name of the resources remote was not confirmed.

## Session authoring update — 2026-10-14

The maintainer explicitly requires opening `-session` for Litex authoring,
preserving accepted definitions and facts after ordinary failure, and avoiding
full-file replay after each small edit. Current hub entrypoints and the Session
references now emphasize this rule and include a short command comparison.
The corresponding installed authoring skills were updated in place as part of
this requested follow-through; their unrelated content was preserved.

The live golitex guides received concurrent updates to a simpler `have a R = 2`
example; those edits were preserved, and the hub and installed profiles were
aligned with that example. Packaged hashes and transformations were refreshed
while original source hashes and dated source-guide archives were retained.
The [small accepted prefix](session-accepted-prefix.lit) is newly authored hub
material, rather than an imported golitex snapshot. Its
[focused validation](validation.md#session-authoring-emphasis--2026-10-14)
uses the existing Litex 1.0.7-beta release executable and does not establish
correspondence to current source or revalidate the original 1.0.6-beta corpus.

## Import transformations

The later authoring router is newly maintained hub material, not an upstream
snapshot. See the live-corpus update below for its deployment and checks.

- `todo_writer` is distributed as `todo-writer`, matching its declared name.
- Source skill bodies become references/source-guide.md. Their current hub
  entrypoints route by task and use the shared version-aware execution contract.
- The old proof-writer corpus is replaced by one shared curated corpus.
- The bundled Manual's exact reciprocal-law recipe was updated after an
  independent replay demonstrated that the application-value seed is optional
  on the measured executable. This narrow observation is recorded in validation.md;
  it does not revise the sibling source repository or claim broader unfolding.
- Equality case sources/configs remain verbatim; full JSON receipts become
  explicitly labeled `.summary.json` files with original hashes and outcomes.
  Diagnostic logs and the historical kernel experiment are not distributed.
- Relative Markdown links are adapted to the hub layout. Selected referenced
  files stay local, tracked unbundled golitex files point upstream, and local-only
  notes point to the availability boundary below.
- The previous Generic Agent skill package is retained as a historical archive under
  [the Generic Agent example archive](../../generic_agent_example/legacy_imo_package/README.md).

## English edition

Navigation, SOPs, skill instructions, author notes and historical helper text
are presented in English. The three equality overview documents use English
filenames; provenance retains their original source filenames and hashes.
Original Litex sources, module configs, problem datasets and historical receipt
contents retain their exact values. Literal source paths and examples of
localized CLI output remain in their original form so readers can recover
sources and recognize actual output. Chinese-version URLs are percent-encoded.

Translations of historical instructions do not establish current support.
Use the current [execution contract](../skills/litex-reference/references/execution.md)
for active work. During the original import, installed skills and sibling
repositories were not edited; the later Session update is recorded above.

## Content and example layout

The shared material is under sop_and_skills/ (skills, sops, references and
checking scripts). generic_agent_example/ contains one agent's usage guide
and its historical IMO package. The agent example does not determine the
shared skills' execution environment or require that agent for other users.
This layout change preserves all skill entrypoints and mathematical/config
sources; the provenance paths and affected local links were relocated.

## Unbundled local material

Some imported guides originally pointed to local task notes, draft workspaces,
old corpus files, diagnostic logs or full receipt payloads. This edition does
not provide a public source URL for those artifacts. Their references here
record an availability boundary, not replacement evidence or a passing result.

For the original skill archive use the source owner's installed skill folder;
for a full language corpus use a version-matched golitex/resources checkout.
For a local-only task note ask its owner for the actual source-owned workspace
only when the task needs that evidence. Do not publish golitex/scripts merely
to resolve a reference. Historical acceptance that cannot be recovered remains
historical; replay a complete retained source before a current-support claim.

## Licensing and acceptance

The curated golitex material carries its [upstream license](litex/LICENSE).
The imported personal skills did not supply a separate license file; this
import preserves attribution and does not create a new license grant. The old
package's claim that it shares Generic Agent's license is a historical statement,
not the license policy of this hub.

Package integrity/link checks and focused mathematical replays are recorded in
[validation.md](validation.md). A packaged historical receipt is not a current
acceptance gate; a Litex gate is not proof of Lean compilation.

## Live corpus reading update — 2026-10-14

At the maintainer's request, source discovery now defaults to the actual
paired `../golitex` checkout's docs, examples and showcases. The reference
skill owns root resolution and four task-dependent reading levels. Other
authoring skills link to that shared route with an appropriate starting level.
Bundled snapshots and source-guide archives retain their original dates and
hashes and are explicitly offline/historical alternatives.

The self-contained reference skill was also installed in the personal Codex
skill directory, with a separate checked absolute location hint. Existing
personal authoring skills were connected to it without replacing unrelated
guidance. Shared skill text contains no maintainer-specific absolute root.
The routing update reads the sibling golitex tree; it does not modify or copy
its mathematical sources. Root/path checks and manual reading dry-runs are
recorded in [validation](validation.md#live-corpus-reading-routes--2026-10-14).

## Layered authoring edition — 2026-10-14

The maintainer approved a foundation + task + conditional topic organization.
`litex-basics` and `litex-review` are newly authored skill entries. The foundation
contains six short topic guides, common mathematical patterns, eleven
misconception cards and seventeen small `.lit` fixtures (nine positive and
eight intentional rejections). The module example's namespace/definition-release
contract was established using the actual configured consumer and current live
examples. The new examples introduce no trust/axioms or kernel changes.

Existing portable task entrypoints were rewritten around that foundation and
the live reference router. Their expanded imported guides, historical cases,
language snapshots, original source hashes and receipt archives remain in this
source checkout. `profiles.json` and `export_skills.py` select lightweight,
closed-dependency basics/author packs or an explicit complete maintainer edition;
they do not copy the live golitex corpus or overwrite personal installations.

The new skills were installed locally, and short foundation/topic routes were
inserted into existing personal skills without replacing their prior bodies.
The shared reference router matches source; its private corpus-location hint
is preserved separately. The executable and export checks are recorded in
[validation](validation.md#layered-authoring-edition--2026-10-14) and its
[structured journal](validation/skill-layers-2026-10-14.json). These newly authored
files are distinct from the unchanged, hash-recorded historical imports.

## Generic Agent geometry reproduction — 2026-10-14

The agent example now owns an install-to-answer walkthrough for archived problem
16 / IMO 1968 P4. The official [problem sheet](https://www.imo-official.org/problems/1968/eng.pdf)
confirms the original statement without a distinct-edge condition; the archive's
extra paraphrase assumption is not adopted. The frozen formal task checks the
edge-length implication from four strict face-triangle conditions. Its natural
Euclidean interpretation is explicit; no new 3D distance library is claimed.

Generic Agent remains an external upstream dependency, pinned to
`8b7d4e0a82849ccda2c83b85d4391ed7b912ec7f`. The public golitex dependency is pinned
to `3c5befb5605193a53827b472b15462714ee8690b`, built and checked as 1.0.6-beta.
This installable public contract is separate from the previously tested local
1.0.7-beta binary. The example's manifest, dependency versions, generated
prompt, persistent Session bridge and frozen-goal checker are newly authored.
The new reference proof is preparation evidence, not recovered historical
Generic Agent output. No upstream agent source is vendored, no archived import
is changed, and no model API inference was run during preparation.

See the [walkthrough](../../generic_agent_example/README.md) and its
[validation](../../generic_agent_example/validation/README.md) for actual tested
entrypoints, proof scope, full/partial feedback boundaries and negative controls.
