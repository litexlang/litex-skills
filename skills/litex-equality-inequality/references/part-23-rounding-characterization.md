# Part 23 — Determine a rounded value from its integer cell

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Situation and idea

For integer n, n<=x<n+1 characterizes floor(x)=n; n-1<x<=n characterizes
ceil(x)=n. Integer adjacency makes the candidate unique.
Anchor: Concrete Mathematics Chapter 3 equations 3.5a/3.5c.

## Positive

```litex
claim:
    ? forall x R,n Z:
        n <= x
        x < n+1
        =>:
            floor(x) = n
    floor(x) $in Z
    floor(x) <= x < n+1
    floor(x) <= n
    n <= x < floor(x)+1
    n <= floor(x)
```
Passes. The corresponding ceiling proof also passes; full source in the
receipt. Direct floor/ceil universal targets with the same premises miss.
Shorter floor/ceil candidates dropping the explicit integer/weak-bound bridges
also miss. Do not declare these bridges removable from mathematical redundancy
alone, or treat the full tested bodies as proven global minima.

## Negatives

Changing n's domain to R makes either characterization false; both probes
reject. For floor, x=0.8,n=0.2 is a counterexample; for ceiling,
x=0.2,n=0.5 is a counterexample.
Closing the wrong endpoint also fails: x=n+1 invalidates floor(x)=n,
and x=n-1 invalidates ceil(x)=n. Both variants reject.

## Candidate

A fixed cell-characterization equality leaf checks integer candidate and
the exact two inequalities. Preserve integer and half-open endpoint evidence;
do not approximate numeric cells or infer an integer candidate from a real
width-one interval. Candidate n is supplied by the equality goal, so no
search for a rounded value is needed. Existing native rounding definitions
provide its mathematical justification; no arbitrary logical unfolding.

## Evidence

[Round 7 receipt](evidence/round-07-2026-10-08.summary.json), `floor-characterization-*`,
`ceil-characterization-*`. Current working-tree release built on 2026-10-08;
independent strict files, no canonical chapter changes.
