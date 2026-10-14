# Adding SOPs, skills and usage examples

The repository has two current content boundaries:

- sop_and_skills/ owns reusable Litex instructions and shared references.
- generic_agent_example/ demonstrates one agent using those instructions.

## Shared content

Add a skill under sop_and_skills/skills/<name>/ with SKILL.md frontmatter
containing name and description. Keep essential task guidance in that entrypoint;
put conditional detail in its references, reusable helpers in its scripts and
output templates in its assets. The folder name matches the declared name.

Keep source skills flat to preserve sibling references. Classify each in
`sop_and_skills/profiles.json` and the hub index: foundation, reference, task,
topic or maintainer. Foundation owns the minimum working knowledge; task
entries own workflows; short topic guides load only when needed. Keep the
foundation's dependencies inside its own directory so `basics` works alone.

Register portable payloads explicitly. The default `author` pack includes all
non-maintainer skills, with closed relative Markdown dependencies; no task
should depend on an omitted source-guide or evidence archive. Retain archives
in source and the explicit full `maintainer` edition. Do not copy the entire
golitex documentation tree into a new skill. Inspect existing personal skills
before merging local guidance; the exporter only creates new directories.

Ordinary tasks start with `skills/litex-basics/SKILL.md`, which must teach the
working model, execution, major syntax, common mathematics and misconception
boundaries. Keep its complete positive examples runnable and label negative
controls explicitly. Specialized task entries build on it without loading all
topics at once. Prefer a small reference inside that foundation for a new
topic; create a separate skill only when it owns a distinct task workflow.

Deeper source discovery is owned by `skills/litex-reference/SKILL.md` and
its `references/live-reading.md`: resolve the live corpus, choose a reading
level, and read actual docs/examples/showcases. Keep other skills' routes
short and task-specific. Do not turn copied snapshots into the default source.
Personal installed root hints belong in the installed reference skill's
`references/local-corpus.md`; shared instructions must remain portable.

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
A reproducible example fixes a concrete problem and source revisions, provides
actual install/run/skill-loading commands, preserves candidate feedback and
checks the original goal. Distinguish reference proof replay from model-driven
generation and state which parts of the end-to-end path were actually tested.

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
labels and profile membership. Exercise the exporter with each profile, verify
the lightweight packs' dependency closure and examples outside the paired
checkout, and check its refusal to overwrite an existing destination. Run a
new/changed executable helper through its actual use path. Verify
changed mathematical sources with the chosen Litex version and their real config;
record expected negatives separately. A link check does not verify mathematics.
