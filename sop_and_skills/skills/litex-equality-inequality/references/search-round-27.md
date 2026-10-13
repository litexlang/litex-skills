# Search round 27 — preimage definition equality and member consumers

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


28 independent strict files: 17 accepted, 11 rejected. Exact inverse_image
declaration and four original topology showcase theorem bodies were preserved
in isolated probes. Fresh release build succeeded; immutable executable and
source excerpt identity are retained. No registered topology-module gate.

## Existing support and source shortening

Carrier membership, subset and powerset membership pass directly. Literal
set-builder member introduction and condition extraction already pass; do not
duplicate those primitives. Preimage introduction needs only its definition
equality in the tested original interface. Preimage value extraction shortens
from three statements to two:

```litex
\inverse_image<X,Y,f,U> = {x X: f(x) $in U}
p $in \inverse_image<X,Y,f,U>
```

The final f(p) in U echo is removable. Definition equality alone, member echo
alone and the literal-member replacement all miss in independent cold files.
[Part 68](part-68-preimage-definition-members.md).

## Candidate and diagnosis boundary

Inspect goal-directed consumption of already known set equality and member
facts to instantiate a set-builder body, retaining actual citations, free
function identity and domain WD. Do not prescribe permanent membership replay
or modify Env state merely because this author route checks. Current probes
establish the consumer gap, not its precise storage/search implementation cause.

For an additional set alias E, introduction passes with one E=template=builder
chain; extracting the body additionally needs a member statement. Both the
E-member route and template-member route check. Direct alias targets miss.

## Controls and evidence

Changing f to unrelated g, dropping the original member condition and using a
point outside f's domain reject. The controls distinguish mathematical false
and invalid-domain targets from true shortcut misses. No premise or carrier
was weakened to obtain the positives.

[Receipt](evidence/round-27-2026-10-09.summary.json), complete `evidence/round-27-cases/`
and build log. Same-Session successes after original theorems are retained as
warm observations only; cold files determine capability. No canonical/kernel
edits, trust, global-minimality or runtime claim. Next: generic set-alias/body
consumer probes with literal predicates and held-out source interfaces.
