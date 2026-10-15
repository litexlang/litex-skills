# Solve the frozen geometry task using Litex skills

This is one independent Generic Agent task. Work in `@@RUN@@`.
Read `problem.md`, `prefix.lit`, `goal.lit` and `run.json` there first.
Prove the complete universal edge-length formulation of IMO 1968 P4. Preserve
equal-edge cases, positivity, all three triangle inequalities and all four
possible vertices. Explain the geometric interpretation and its formal boundary.

## Load the skills

The prepared author pack is `@@RUN@@/materials/skills/`.
Read `litex-basics/SKILL.md` first, then `litex-proof-writer/SKILL.md` and the
foundation's `references/topics/algebra.md` and `logic-scope.md`. Use
`litex-concept-modeler` only if another mathematical interface is needed.
For the saved artifact apply `litex-review` to check scope and assumptions.
Read other topics only when they answer the next concrete question.

Use `litex-reference` for the live corpus at `@@CORPUS@@`. Read its actual CLI
contract and the relevant small cases/order/definition examples. The pinned
executable is 1.0.6-beta; its JSON uses `success` and `session_error`. Follow
that version's actual contract rather than newer fields in teaching notes.
Do not load the entire corpus or substitute the old planar geometry library.

## Retain one real Litex Session across tool calls

Generic Agent's ordinary `code_run` starts a fresh process. For this task,
explicitly use its supported `inline_eval: true` mode to retain a connection
on the same `handler` during this one task. This is the intended use of that
mode here. In `code_run`, with `type: "python"` and `inline_eval: true`, run:

```python
import sys
sys.path.insert(0, @@RUN_PY@@)
from litex_session import LitexSession
handler.litex = LitexSession(@@RUN_PY@@)
_r = {"pid": handler.litex.child.pid, "ready": handler.litex.usable}
```

Write one complete top-level statement to `candidate.lit`, then use a separate
`code_run` call, again with `type: "python"` and `inline_eval: true`:

```python
from pathlib import Path
_r = handler.litex.submit((Path(@@RUN_PY@@) / "candidate.lit").read_text())
```

No internal blank lines: the REPL uses one to end an indented statement.
A full theorem/claim and its proof is one statement. Read the complete result
before the next candidate. `accepted: false, session_ready: true` means repair
that statement in the same process; earlier accepted knowledge is retained.
Do not instantiate another connection or rerun a growing full file after a
normal rejection. The bridge saves accepted source to `accepted.lit` and exact
verifier feedback, candidate text, timestamps and PID to `session.jsonl`.

Hard termination or timeout makes the connection unusable. Close it and
deliberately reopen `LitexSession` only then, or to replace a committed name.
Reopening replays `prefix.lit` plus the saved accepted source once; inspect
the startup result and record why the restart was needed. To replace a
committed statement, first revise the accepted source and its dependent suffix
deliberately; do not blindly redeclare it. A new user task gets a new handler.

## Deliver and verify

Write a brief mathematical proof outline before formalizing. Reuse the frozen
triangle definition; add meaningful checked lemmas if needed. Keep skills,
verifier and corpus read-only, with task files inside the run. Add no user
`trust`, axioms, extra assumptions, kernel edits or weakened goal. If blocked,
preserve the attempted source and exact diagnostic and report the blocker.
Do not read a reference answer or ask another agent to solve the task.

At a coherent checkpoint/final delivery copy the accepted proof statements
from `accepted.lit` into `solution.lit`. Leave the frozen prefix and goal out
of that proof file; the checker supplies both. Run this using ordinary
`code_run` (the final gate is intentionally a separate process):

```python
import subprocess, sys
from pathlib import Path
run = Path(@@RUN_PY@@)
result = subprocess.run([sys.executable, @@CHECKER_PY@@, "check",
                         "--run", str(run), "--proof", str(run / "solution.lit")],
                        text=True, capture_output=True)
print(result.returncode, result.stdout, result.stderr)
```

Then close the live Session through `inline_eval: true`:

```python
_r = handler.litex.close()
```

Write `result.md` with the mathematical idea, what was formally checked,
the final status, saved gate location, model/provider label, any human help,
and surviving blockers. Use actual token/cost data when available; otherwise
write unknown. Do not claim a successful agent experiment from a verifier
replay alone. Preserve failed candidates and replays in the journal. Log
source, visible actions and tool evidence; do not request or publish private
model reasoning, API keys or raw credential configuration.
