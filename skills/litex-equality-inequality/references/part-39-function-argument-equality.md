# Part 39 — Consume equality inside function arguments

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation

Function application preserves equality of valid arguments. Distinguish consumption of an already established equality from discovery of a new arithmetic identity or extensional function equality.

## Existing positive support

Ordinary congruence and nested arithmetic congruence already pass:

```litex
forall x,y R,F fn(t R) R:
    x = y
    =>:
        F(x) = F(y)
```
```litex
forall x,y R,F fn(t R) R:
    x = y
    =>:
        F(x+1) = F(y+1)
```

Known equality of two named function arguments also passes under a higher-order function. Do not claim generic function congruence is missing.

## Already-proved anonymous function alias

This complete input misses only at the final equality; `h = fn(x R) ...` is accepted:

```litex
have F fn(h fn(t R) R) R
have g fn(t R) R
have h fn(t R) R = fn(y R) R {-1*g(y)}
h = fn(x R) R {-1*g(x)}
F(h) = F(fn(x R) R {-1*g(x)})
```

The same mathematical goal passes via an explicit checked generic equality theorem:

```litex
thm apply_equal_argument:
    ? forall X,Y set,F fn(t X) Y,a,b X:
        a = b
        =>:
            F(a) = F(b)
have F fn(h fn(t R) R) R
have g fn(t R) R
have h fn(t R) R = fn(y R) R {-1*g(y)}
h = fn(x R) R {-1*g(x)}
release thm apply_equal_argument(fn(t R) R,R,F,h,fn(x R) R {-1*g(x)})
F(h) = F(fn(x R) R {-1*g(x)})
```

A live Session with the theorem declared first preserves all declarations after the ordinary final-equality failure; releasing the theorem repairs that goal in the same process. A separate failed session attempt reused binder `F` after global `F` and hard-exited in parsing; this is an authoring error, not evidence against mathematical congruence.

## Arithmetic identity under a function argument

A true direct identity misses:

```litex
forall x R,F fn(t R) R:
    F((x+1)-1) = F(x)
```

Publishing the inner equality first passes:

```litex
forall x R,F fn(t R) R:
    (x+1)-1 = x
    F((x+1)-1) = F(x)
```

This does not establish that arbitrary identities or recursive function unfolding should be discovered automatically.

## Mathematical negatives

`F(x)=F(y)` does not imply `x=y` without injectivity. Different free captures in anonymous function arguments cannot be equated; `F` may evaluate the argument at zero, distinguishing `g1=0` and `g2=1`. A function on `R+` cannot silently replace one on `R`. All three executable controls reject in this round; see receipt and retained sources.

## Improvement candidates and ownership

1. Prioritize inspection of the existing corresponding-argument/equality-consumption route when one argument is a checked anonymous-function alias. Trigger same valid application head/arity; consume exact known argument equality (including sound binder-alpha identity), preserve free captures, domains, WD and citations. No extensional-function search or global normalization is implied. The observed miss does not yet identify its internal cause.
2. Separately consider bounded arithmetic equality checking at an argument leaf: same application head, smaller argument-equality obligations, existing guarded rational normalization only, fixed permissions/budget and certificates. Do not unfold an arbitrary user function or increase global search permissions to close this case.

Read-only source locator: `src/execute/execute_fact_stmt/verify_atomic_fact/verify_equality/search_equal_fact_proof_by_matching_one_arg_by_one.rs` and the corresponding-argument helper. These are investigation anchors, not a proven causal diagnosis or authorization for shared AST/Runtime changes.

## Evidence and scope

Date: 2026-10-08. Fresh current-worktree release build succeeded. Immutable binary identity, full commands, Normal JSON, cases and synchronized Session transcript: [round 12 receipt](evidence/round-12-2026-10-08.summary.json). Each case has a durable replay command. All positives require exit 0, Normal `kind: run`, `success: true`, `session_error: null`.

Earlier snapshot experiments and an unrelated failed source build are historical evidence only. This fresh build supersedes their source-correspondence limitation. No kernel or canonical geometry source was changed. No performance comparison or universal minimality claim.
