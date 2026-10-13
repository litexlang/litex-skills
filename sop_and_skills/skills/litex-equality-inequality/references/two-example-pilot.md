# Two Pilot Cases: Recognize Support Before Proposing a Builtin

> Imported reference snapshot (2026-10-13). Use [the hub execution contract](../../litex-reference/references/execution.md). Repository conventions apply to the source project; dated examples remain historical until replayed.
> Receipt links contain summaries, not full verifier output. Original hashes, commands, and recorded outcomes remain available; see [evidence packaging](evidence-packaging.md).

These cases use the same layout: mathematical situation, concise positive,
verbose comparison, negative, current support, and improvement candidate.
Results come from the existing 2026-10-08 record; editing this page did not
rerun cases or modify the kernel. The linked Parts retain complete sources and
binary identity; those results do not establish later-version behavior.

## Part A: A numeric inequality after an established equality

The preceding Newton proof establishes the second-step residual as `1/144`.
The remaining goal is to bound it by `1/64`.

**Concise positive, historically accepted.** Excerpt with the same prefix:

```litex
square_root_two_residual(newton_sqrt_two_step(3 / 2)) = 1 / 144 <= 1 / 64
```

**Verbose comparison, historically accepted.**

```litex
80 / 9216 > 0
1 / 144 + 80 / 9216 > 1 / 144
1 / 64 = 1 / 144 + 80 / 9216
1 / 64 > 1 / 144
1 / 144 < 1 / 64
1 / 144 <= 1 / 64
square_root_two_residual(newton_sqrt_two_step(3 / 2)) = 1 / 144 <= 1 / 64
```

**Mathematical negative, historically rejected.** Same prefix:

```litex
square_root_two_residual(newton_sqrt_two_step(3 / 2)) = 1 / 144 <= 1 / 256
```

Since `1/144 > 1/256`, rejection is correct. Existing support suffices to remove
six helper statements; no new numeric-comparison builtin is justified. Earlier
residual computation and execution-time measurements are outside this change.
See [Part 1 and its evidence](part-01-numeric-endpoint.md).

## Part B: Subtraction transports both bounds

For real `a,b,c,d`, assume `a <= b` and `c <= d`; prove `a-d <= b-c`.

**Concise positive, historically accepted.**

```litex
claim:
    ? forall a, b, c, d R:
        a <= b
        c <= d
        =>:
            a-d <= b-c
    a-d <= b-d <= b-c
```

**Verbose comparison, illustrative and not independently checked.**

```litex
a-d <= b-d
b-d <= b-c
a-d <= b-c
```

**Ideal direct form: true, but missed in the original search record.**

```litex
forall a, b, c, d R:
    a <= b
    c <= d
    =>:
        a-d <= b-c
```

**Mathematical negatives, historically rejected.** The weak premises do not
justify either endpoint:

```litex
# Wrong direction: a=b=0, c=0, d=1 gives 0 <= -1.
a-c <= b-d

# False strictness: four zero inputs give 0 < 0.
a-d < b-c
```

These are target excerpts; Part 2 retains the complete negatives and a control
omitting `c <= d`.

**Builtin candidate at that checkpoint, not yet implemented then.** For a real
`L1-L2 <= R1-R2` goal, check:

```text
L1 <= R1
R2 <= L2
```

The second operand reverses direction. Accept the original goal only after
both subgoals and expression WD pass. This sufficient subtraction-order rule
needs no intermediate `b-d`. Failure of its conditions can defer to other
routes; it does not establish a false goal. Weak bounds do not imply strict
bounds. See [Part 2 and its evidence](part-02-subtraction-order.md) for later status.

## Writing later cases

Show checkable premises and source, then distinguish existing concise support,
true-but-undiscovered targets, and mathematically invalid controls. Only the
second category nominates a bounded kernel improvement. Verbosity is not a
mathematical error, and a current bridge is not a permanent authoring rule.
