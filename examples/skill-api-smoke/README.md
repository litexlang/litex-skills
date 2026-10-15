# Litex-basics API mini smoke

Small pure-API check that the **basic** skill teaches the dialects that previously
failed geo defs (`cart`, `p(1)`, guarded `have fn`, …) before any large B0/B1 run.

## Layout

| Path | Role |
| --- | --- |
| [tasks.json](tasks.json) | Five mini prompts + must/must-not string checks |
| [run_mini.py](run_mini.py) | Inject `litex-basics/SKILL.md`, call chat completions, run Litex |
| `results/<stamp>/` | Per-task response, candidate, verify JSON, summary |

## Offline harness check (no API)

```sh
cd examples/skill-api-smoke
python3 -B run_mini.py --offline-fixture
```

## Live Claude (gateway)

Uses the benchmark `.env.local` by default (`CLAUDE_API_KEY3`). Override as needed.

```sh
cd examples/skill-api-smoke
env NO_PROXY='*' no_proxy='*' python3 -B run_mini.py \
  --api-key-env CLAUDE_API_KEY3 \
  --max-tokens 2048
```

Expect `5/5 passed` before scaling to full geo B0. Intermediate/advanced skills
are intentionally **not** injected here.
