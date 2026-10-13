# Writing Litex with Generic Agent: a Usage Example

This directory demonstrates one way to use the shared SOPs and skills.
The reusable content is in [sop_and_skills/](../sop_and_skills/README.md);
other agents with suitable capabilities can use it too.

## 1. Prepare the agent and Litex

Obtain Generic Agent separately from its
[upstream repository](https://github.com/lsdefine/GenericAgent). Follow your
version's installation, model configuration, and startup instructions.
This repository provides the reference material and usage example.

Prepare the Litex executable, check `litex -version` and `litex -help`, and read
its version-matched [execution contract](../sop_and_skills/skills/litex-reference/references/execution.md).

## 2. Make the shared material discoverable

Keep the complete checkout. Register its absolute path in the agent's memory
index and direct it to select skills from `sop_and_skills/README.md`.
[memory-entry.txt](memory-entry.txt) is an example pointer. Replace
`LITEX_HUB_ROOT` with the actual repository root and use the index format
supported by the upstream agent version.

If the agent requires files inside memory, copy the complete checkout into a
dedicated `memory/litex-hub/` directory and register its
`sop_and_skills/README.md`. The complete directory preserves references
between skills and shared material.

## 3. Give it a concrete task

For example, start in a new independent mathematical workspace:

```text
Read <hub>/sop_and_skills/README.md. Use litex-reference,
litex-proof-writer, and concept modeling when the task needs it.

In <workdir>/reciprocal.lit, define the reciprocal function on nonzero reals,
check its value at 2, and prove that the reciprocal multiplied by its
nonzero argument equals 1.
Explain the mathematical idea and domain before writing Litex. Run the
actual executable and inspect its output. Record the version and commands.
After an ordinary failed statement, keep the same Session and its accepted
context, repair that statement, and continue. Verify the saved file in a
clean run.
```

Replace `<hub>` and `<workdir>` with real paths. Read the relevant skill for
the task: the equality case index for calculations, or the
[IMO geometry SOP](../sop_and_skills/sops/imo-geometry/README.md) for geometry.
Store generated answers and runtime logs in the task workspace.

## 4. Inspect the delivered result

Check the domains, mathematical conclusion, actual commands, and verification
feedback. The bundled contract uses `litex -lang en -strict -f <file>` for
proofs that exclude user assumptions. Success requires exit 0, `kind: run`,
`success: true`, and a null `session_error`. Other versions follow their CLI.

These instructions and prompts do not claim that Generic Agent was run during
this repository preparation. The actual mathematical and package checks are
recorded in [validation](../sop_and_skills/references/validation.md).

## Historical IMO package

[legacy_imo_package/](legacy_imo_package/README.md) retains earlier Generic
Agent materials, problem data, and tools. It contains old commands and paths;
the logger wrapper also depended on `temp/imo_litex_log.py` in an agent
installation, and that capture engine is not bundled. Use this archive to
trace the old example; start current authoring from the shared SOP and skills.
