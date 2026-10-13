# Adding SOPs, skills and usage examples

The repository has two current content boundaries:

- sop_and_skills/ owns reusable Litex instructions and shared references.
- generic_agent_example/ demonstrates one agent using those instructions.

## Shared content

Add a skill under sop_and_skills/skills/<name>/ with SKILL.md frontmatter
containing name and description. Keep essential task guidance in that entrypoint;
put conditional detail in its references, reusable helpers in its scripts and
output templates in its assets. The folder name matches the declared name.

Import supporting files with the entrypoint. Keep skills flat to preserve
sibling references and classify them in sop_and_skills/README.md. Distinguish
required reading, conditional reading and historical evidence. Do not silently
overwrite an installed personal skill while adding a hub copy.

Add a task SOP under sop_and_skills/sops/<task>/ when it owns a distinct action
sequence or acceptance scope. Keep the workflow independent of a particular
agent's memory format or logging engine.

Use sop_and_skills/references/ for selected common material and record origins,
source revisions/worktree state and transformations in sources.md and
provenance.json. Provenance file keys are relative to the repository root.
When an intentional layout or snapshot edit changes those files, update the
packaged hash and transformation while retaining the original source hash.

Check version/help before making an old recipe current guidance. Preserve dated
observations and trust boundaries. Large corpora can stay external with a concrete
source/version. Do not invent a public URL for local notes or treat a receipt
summary as a complete archive. Preserve source attribution and licensing scope.

## Agent examples

Put an agent's setup pointers, loading instructions and worked usage prompts in
its example directory. Reference shared skills instead of maintaining another
copy. Obtain agent code and startup instructions from that agent's upstream.
Further agent examples can be added when needed without changing the core skills.

The historical Generic Agent IMO package remains under
[generic_agent_example/legacy_imo_package](generic_agent_example/legacy_imo_package/README.md).
Keep it visibly historical; inspect its version-specific tools before reusing them.
Runtime logs, answers and local agent state belong in the user's task project.

## Validation

From the repository root run:

```sh
python3 sop_and_skills/scripts/check_hub.py
```

This checks skill entries, internal file links, provenance hashes and receipt
labels. Run a new/changed executable helper through its actual use path. Verify
changed mathematical sources with the chosen Litex version and their real config;
record expected negatives separately. A link check does not verify mathematics.
