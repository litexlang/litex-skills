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

## Import transformations

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
for active work. Original installed skills and sibling repositories were not edited.

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
