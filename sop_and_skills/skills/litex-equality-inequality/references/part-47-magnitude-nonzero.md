# Part 47 — Nonzero reflection from magnitude evidence

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation and source

A positive absolute value or nonzero absolute value implies a nonzero real argument. Positive separation abs(x)>=c with c>0 supplies that magnitude evidence. Source: Analysis chapter06 `reciprocal_abs_diff_bound`, which separately assumes x!=0,y!=0 and positive magnitude lower bounds.

## Ideal direct forms: observed misses

```litex
forall x R:
    abs(x) != 0
    =>:
        x != 0
```
```litex
forall x R:
    abs(x) > 0
    =>:
        x != 0
```

The positive separation direct form also misses. In contrast, abs(x)>=c with c R+ directly supplies abs(x)>0; the failed link is not this positivity step.

## Positive: checked explicit route

```litex
claim:
    ? forall x R,c R+:
        abs(x) >= c
        =>:
            x != 0
    abs(x) >= c > 0
    by contra:
        ? x != 0
        abs(x) = abs(0) = 0
        impossible abs(x) > 0
```

The direct separation miss is repaired by this exact-premise proof in the same Session. Explicit contradiction is a usable current interface; a shortcut is optional, not evidence of a mandatory kernel bug.

## Existing zero support and negatives

The opposite zero interface already passes:

```litex
forall x R:
    abs(x) = 0
    =>:
        x = 0
```

Known x!=0 to abs(x)!=0 is an existing rule in not_equal.rs. Do not duplicate either supported direction. abs(x)>=0 alone, or abs(x)>=c with unrestricted c, cannot establish nonzero: x=0,c=0 is a counterexample; executable controls reject.

## Builtin candidate and cycle boundary

For real x!=0, consume already checked abs(x)!=0 or abs(x)>0 and cite it. A bounded positive-lower-bound helper can supply the strict magnitude fact where its own evidence is available. Do not recursively generate abs(x)!=0 with unrestricted truth search: the existing forward rule can call back into x!=0, creating a cycle. This insertion of an Abs constructor is not decreasing syntax descent. Use known-evidence queries/existing bounded sign interfaces, retain scope/WD/citations, and do not change global recursion/fuel or Env storage contracts.

Removing explicit nonzero premises from the reciprocal use probe still fails, but its Normal output reports only outer forall search_proof. The receipt id `reciprocal-derived-nonzero-wd` does not establish a WD-phase cause or show that one new truth rule alone solves every denominator consumer.

## Evidence and limits

Date: 2026-10-08. Current-worktree release build succeeded. [Round 16 receipt](evidence/round-16-2026-10-08.summary.json) retains immutable binary identity, exact complete sources, commands, exits, Normal JSON, Session responses and durable replay commands. Runnable sources are in `evidence/round-16-cases/`.

No kernel/canonical textbook edits, added trust or runtime claims. Only isolated scalar/source-interface checks; registered chapters, continuity theorem dependencies and downstream consumers were not verified. Candidates are not implemented rules or complete causal diagnoses.
