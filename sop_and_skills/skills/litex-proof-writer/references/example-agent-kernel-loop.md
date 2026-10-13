# Example-Agent-Kernel Improvement Loop

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.


Use this loop when one Litex task is intended to improve three things together:

1. a real mathematical source example;
2. the future Litex-writing agent;
3. only the kernel capabilities that survive explicit user review.

The loop coordinates existing artifacts. It does not replace the Task SOP,
proof journal, miner, acceptance example, or source todo.

## Round state machine

```text
choose one real tracer
  -> generate temporary Task SOP
  -> write/repair and verify the example
  -> preserve attempts in its source-owned proof journal
  -> classify round findings by destination
  -> show every kernel candidate to the user
  -> implement only explicitly approved kernel candidates
  -> send agent candidates to the cross-journal miner
  -> close the round from verified evidence
  -> choose the next tracer from the remaining mathematical gap map
```

The three improvement lanes have different gates:

- **Example:** improve the source-facing statement or proof and require a clean
  release runner `-f` gate. The example is the point of the round, not a toy
  excuse for changing the kernel.
- **Agent:** record the wrong default move, preferred move, and nearest
  boundary. Default to `mine`, not `promote`. Permanent skill mutation still
  requires independent journal families, positive and negative evidence, and
  a held-out behavior evaluation.
- **Kernel:** treat every observation as unauthorized until the user records
  `approve`. A pending, rejected, deferred, or `agent_only` candidate does not
  authorize kernel work. An approved implementation still requires a positive
  regression and the nearest executable negative boundary.

Library and diagnostic findings may be routed separately. Do not disguise a
missing reusable theorem as an agent workaround or a confusing error as a new
semantic rule.

## Conversation checkpoint

After the example and journal reach a coherent checkpoint, show the user one
compact review packet:

```text
Tracer: <before -> after, exact file gate>

Agent candidates:
- <decision rule>; evidence status: one-task / mined / held-out verified

Kernel candidates requiring your decision:
- <candidate>; benefit; nearest unsound or unsupported boundary;
  recommendation: approve / reject / defer / agent_only

No-decision work:
- example, documentation, library, or diagnostic follow-ups

Next tracer if this round closes: <one real source item and why>
```

Do not bury kernel candidates among ordinary progress notes. If a kernel
candidate is pending, pause only that mutation lane; continue safe example,
journal, miner, library, or documentation work that does not pre-empt the
decision.

## Deterministic round validator

Inside golitex, encode the checkpoint in a source-owned round manifest and
run:

```bash
python3 scripts/litex_improvement_loop.py review path/to/round.json --root .
python3 scripts/litex_improvement_loop.py close path/to/round.json --root .
```

`review` renders the user decision packet. It may succeed while closure is
blocked by a pending decision. `close` exits nonzero until the tracer gate,
strict journal evidence, reviews, and any approved implementation boundaries
are complete. The tool is read-only over examples, journals, kernel code, and
skills. Its report always keeps `automatic_kernel_mutation_allowed` false and
lists only candidate ids with an explicit recorded `approve` as authorized.
It also checks the temporary Task SOP lifecycle: an active round names an
existing SOP, while a completed round records that the SOP was removed after
its result was transferred to a durable acceptance, journal, or todo artifact.

Use this minimum manifest shape:

```json
{
  "schema_version": 1,
  "round_id": "source-item-and-date",
  "task_sop": {
    "path": "todo/2026-8-24/source-item-and-date.md",
    "status": "active"
  },
  "tracer": {
    "source_item": "the real theorem or problem",
    "example_path": "source-owned/example.lit",
    "before": "the exact earlier limitation",
    "after": "the verified source-facing result",
    "file_gate": {
      "command": "target/release/litex -compact -runner -f source-owned/example.lit",
      "exit_code": 0,
      "top_level_ok": true
    }
  },
  "journals": ["source-owned/proof_journals/item.json"],
  "findings": [
    {
      "id": "stable-id",
      "summary": "one observable finding",
      "route": "agent",
      "boundary": "nearest case where the rule must stop",
      "recommendation": "send to the miner",
      "agent_action": "mine",
      "evidence": [
        {
          "journal": "source-owned/proof_journals/item.json",
          "history": "B001",
          "attempt": "A2"
        }
      ],
      "review": {
        "decision": "not_required",
        "reason": "No permanent mutation is authorized by this one round."
      }
    }
  ]
}
```

For a kernel route, use review decisions `pending`, `approve`, `reject`,
`defer`, or `agent_only`. A deferred finding needs a source-owned `todo_path`.
An approved and completed finding needs `implementation.status = verified`,
the changed paths, and passing `positive_gate` and `negative_gate` objects.

For an agent route, use `agent_action = record_only`, `mine`, or `promote`.
`mine` must record a deterministic miner result and its report path before the
round closes; `insufficient_evidence` is an honest completed mining result.
`promote` is rejected at closure unless its promotion record says the curator
candidate is `ready_for_promotion_review`, held-out behavior passed, and the
review explicitly approves promotion. User approval of a nomination alone is
not cross-journal evidence.

Produce the mining record with the existing read-only tools, for example:

```bash
python3 scripts/proof_journal_miner.py . --format json \
  --output scripts/<Workspace>/experience/miner_reports/<round-id>.json
python3 scripts/proof_journal_agent.py nominate-all --root . --format json
```

The broad miner discovers recurring shapes; the curator constructs
evidence-gated candidate cards. Neither command changes a skill. Link the
source-owned miner report from the round finding and record either
`nominated` or `insufficient_evidence` before closure.

## Selecting the next tracer

Choose one source item, not a detached capability wishlist. Prefer, in order:

1. a mathematical direction not represented by recent verified examples;
2. a held-out item that can test a nominated agent rule;
3. an item adjacent to a deferred library or diagnostic gap;
4. only then, an item likely to distinguish a real kernel gap from an agent
   mistake.

Do not select the next tracer merely to justify a desired kernel feature. The
source mathematics must supply the question; the loop discovers which lane
owns the answer.
