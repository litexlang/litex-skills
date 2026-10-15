# Reproduce a geometry experiment with Generic Agent + Litex skills

Install Generic Agent, give it this repository's skills, and ask it to solve
**IMO 1968 problem 4** (problem 16 in the archived dataset): every tetrahedron
has a vertex whose three incident edge lengths form a triangle. The
[problem and formal scope](problem.md) fix exactly what the agent must prove.

The experiment makes one Litex behavior observable: the agent can add checked
mathematical knowledge, receive a rejected candidate, and repair the next step
while keeping earlier accepted context in the **same `-session`**. The final
proof, failed candidates and verifier feedback remain available for inspection.
A completed run demonstrates that behavior on this task; it does not by itself
establish an advantage over another agent or proof language.

Generic Agent is installed from [its upstream repository](https://github.com/lsdefine/GenericAgent).
This example fixes its source revision and Litex's source revision in
[experiment.json](experiment.json), and runtime dependency versions in
[requirements.txt](requirements.txt). It uses the agent's existing headless
entrypoint and tool interface; there is no bundled agent fork.

## 1. Install the three repositories

These commands are for macOS/Linux with Git, Python **3.11 or 3.12**, and a
Rust toolchain with Cargo. The Session bridge uses a Unix PTY; Windows users
can follow the Linux commands inside WSL. Validation here used macOS/Python
3.12; other platforms need their own check. Rust installation is documented
by [rustup](https://rustup.rs/); agent setup details are in the
[upstream installation guide](https://github.com/lsdefine/GenericAgent/blob/8b7d4e0a82849ccda2c83b85d4391ed7b912ec7f/docs/installation.md).

Start in a new parent directory. If you already have this hub, reuse its
absolute path and install the other checkouts separately; the preparation
command refuses to overwrite an existing run.

```sh
mkdir litex-geometry-demo
cd litex-geometry-demo
git clone https://github.com/litexlang/litex-skills.git
git clone https://github.com/lsdefine/GenericAgent.git
git -C GenericAgent checkout --detach 8b7d4e0a82849ccda2c83b85d4391ed7b912ec7f
git clone https://github.com/litexlang/golitex.git
git -C golitex checkout --detach 3c5befb5605193a53827b472b15462714ee8690b

HUB_ROOT="$(cd litex-skills && pwd -P)"
AGENT_ROOT="$(cd GenericAgent && pwd -P)"
LITEX_ROOT="$(cd golitex && pwd -P)"
RUN_ROOT="$(pwd -P)/run-01"

python3.12 -m venv "$AGENT_ROOT/.venv"
. "$AGENT_ROOT/.venv/bin/activate"
python -m pip install -r "$HUB_ROOT/examples/generic-agent/requirements.txt"
python -m pip install --no-deps -e "$AGENT_ROOT"
cargo build --release --locked --manifest-path "$LITEX_ROOT/Cargo.toml"
"$LITEX_ROOT/target/release/litex" -version
```

Use `python3.11` for the venv if that is your installed supported version.
Keep the virtual environment active for the remaining commands. The pinned
public Litex build reports **1.0.6-beta**; its JSON contract differs from newer
1.0.7-beta examples elsewhere in the hub. The checker uses the pinned fields.
Source revisions are fixed; each run records its actual platform, binary hash
and copied skill hashes. A future update is a separately identified experiment.

## 2. Configure the agent's model

You need your own model provider/API key with tool calling. Copy the upstream
configuration template once, then edit the local file:

```sh
cp -n "$AGENT_ROOT/mykey_template_en.py" "$AGENT_ROOT/mykey.py"
```

Keep one provider configuration with your actual model, endpoint and key;
remove unused placeholder configurations so the default index 0 selects the
intended provider. The upstream template explains the supported fields.
Keep `mykey.py` local. This example never reads or copies its contents.
Use that exact provider/model label in the next step; it is recorded for
comparison, not used to configure or select the agent automatically.

Check the entrypoint without requesting a model response:

```sh
cd "$AGENT_ROOT"
python agentmain.py --help
```

## 3. Prepare the problem and loadable skills

In the same terminal:

```sh
python "$HUB_ROOT/examples/generic-agent/experiment.py" prepare \
  --agent "$AGENT_ROOT" \
  --litex-root "$LITEX_ROOT" \
  --output "$RUN_ROOT" \
  --model 'YOUR_PROVIDER/YOUR_MODEL'
```

Replace the model label. Preparation does not call a model or change the agent's
memory. It checks the pinned revisions and relevant tracked runtime/reference
files, records the executable identity, and creates a new isolated directory:

```text
run-01/
├── problem.md              Mathematical statement and scope
├── prefix.lit              Frozen triangle definition
├── goal.lit                Frozen universal conclusion
├── materials/              Portable author skills, with their file hashes
├── litex_session.py         Connection retained across agent tool calls
├── prompt.md               Complete task prompt with absolute paths
├── run.json                Source/model labels, inputs and executable identity
└── solution.lit            Empty answer for the agent to fill
```

The generated prompt explicitly tells the agent to read `litex-basics`, then
proof-writing and the algebra/logic topics, with live reference lookup in the
pinned golitex checkout as needed. This is how the skills participate in the
experiment. Merely placing skill files in a directory does not load them.
The copied pack preserves sibling links and does not include a reference proof.

## 4. Run Generic Agent on this problem

Read the generated `prompt.md`, then launch the upstream agent:

```sh
cd "$AGENT_ROOT"
python agentmain.py --func "$RUN_ROOT/prompt.md" --nobg --no-user-tools --nolog
```

This sends the supplied task to your configured model. `--nobg` keeps the run
in the foreground; `--no-user-tools` disables interactive questions and the
dedicated long-term-memory tool for this task; `--nolog` disables the raw model-response
log. The visible result is written by upstream to `run-01/prompt.out.txt`.
The proof/feedback journal is captured separately by the Session bridge.

The pinned agent allows up to 180 turns for this task; this is not a guaranteed
token, time or price limit. Set provider limits to your intended budget before
launching, and report interruption or exhaustion honestly. Model choice and
stochastic generation can change the proof and whether the run completes.

### Why the Session bridge is needed

Ordinary Generic Agent `code_run` calls are separate processes. Running these
independently loses `a` before the second command:

```sh
litex -e 'have a R = 2'
litex -e 'a + 1 = 3'
```

The generated prompt instead explicitly uses Generic Agent's existing
`code_run` with `inline_eval: true`, retaining `handler.litex` across tool calls
in this one task. The bridge keeps one real strict Litex `-session`:

```text
have a R = 2    -> accepted
a = 3          -> rejected; same process remains ready
a + 1 = 3      -> accepted using the original declaration
```

Submit one complete top-level statement per call and inspect its result.
The bridge saves accepted statements without rerunning the growing proof.
Only a hard termination, a deliberately changed prefix or replacement of a
committed declaration requires reopening and accepted-source replay. A new
user task creates a new handler, so the process object is not persistent across
arbitrary later conversations. Checkpoints/final gates are separate clean runs.

## 5. Verify the saved answer and inspect evidence

After the agent finishes, run the gate yourself:

```sh
python "$HUB_ROOT/examples/generic-agent/experiment.py" check \
  --run "$RUN_ROOT" \
  --proof "$RUN_ROOT/solution.lit"
```

The checker constructs **unchanged prefix + agent proof + unchanged goal** in
an isolated directory, then runs the pinned binary with `-lang en -strict -f`.
A trivial passing file or a weakened theorem is insufficient. The measured
1.0.6-beta acceptance envelope requires exit 0, `kind: run`, `success: true`
and `session_error: null`. Unknown JSON shapes fail this gate. Strict mode
rejects user trust/axioms; the mathematical interpretation still needs review.

Inspect these artifacts:

| Artifact | What it establishes |
| --- | --- |
| `run.json`, `materials/pack-manifest.json` | Selected sources/model label, binary identity and skill file hashes |
| `session.jsonl` | Candidate source, exact verifier output, PID, acceptance, time and restart events |
| `accepted.lit`, `solution.lit` | Accepted source and delivered proof |
| `checks/0001/` (then 0002, ...) | Exact composed source, stdout, stderr and parsed gate result, without overwriting old checks |
| `result.md`, `prompt.out.txt` | Agent's visible report; review its assumptions, scope, help and blockers |

A successful check proves the [frozen edge-length theorem](problem.md#frozen-mathematical-task).
The Euclidean interpretation is explained; construction of 3D distances is not
formalized here. The original problem permits equal edges, and so does this
contract. Record actual provider token/cost usage if available, otherwise
unknown. Keep failed/interrupted runs and any human help in the report.

## Optional replay and verified scope

If you want to test the installation first, use the separately labeled
[reference replay](reference/README.md). It supplies a checked proof and must
not be counted as independent agent generation. For an independent attempt,
start a fresh run and do not give that answer to the agent.

[Validation](validation/README.md) records the public-source release build,
preparation, real agent tool-branch Session test, positive frozen-goal replay
and negative acceptance controls. This preparation did **not** make a model
API call or establish an autonomous Generic Agent success rate. The run above
is the actual model experiment for the reader to perform.

The [historical package](legacy_imo_package/README.md) preserves the old workflow
and data. Its machine-specific paths, missing logging engine and planar library
are historical evidence; this walkthrough uses the shared current skills and
its explicitly pinned verifier contract.
