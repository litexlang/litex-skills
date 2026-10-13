# Part 87 — Three-point least squares: retain one sign fact, remove repeats

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source mathematics and unchanged interfaces

The probability/statistics showcase defines a least-squares center by a
comparison against every real candidate, defines mean3=(a+b+c)/3, and gives
a bodyless checked polynomial decomposition. That identity is the mathematical
spine: SSE(candidate)=SSE(mean)+3*(candidate-mean)^2. This card preserves all
real domains, the named predicate and the polynomial identity. Namespace r47
only separates declarations from other Session work.

## Positive: five calculation statements to two, followed by the same fold

The original candidate claim separately states square nonnegativity, scaled
square nonnegativity, releases the decomposition theorem, repeats its identity,
and writes the calculation chain. The checked replacement retains only the
scaled-square sign fact and that chain. Its inline predicate fold is unchanged.
Thus five candidate-body statements become two; counting the final inline
by-def step gives six original proof steps versus three retained proof steps.

Exact retained sign fact:

```litex
0 <= 3 * (candidate - (a + b + c) / 3)^2
```

The retained chain is mathematically SSE(mean)=SSE(mean)+0<=SSE(mean)+
3*(candidate-mean)^2=SSE(candidate); SSE is explanatory notation here, not
an added Litex function or alias. [Complete runnable short proof](evidence/round-47-cases/formula-chain-nonnegative.lit)
contains the literal expanded chain and the original named predicate fold.
The decomposition theorem remains in the dependency prefix. Its separate
invocation and repeated equality are removed, not the interface itself.

## Actual mean constructor consumer: three statements to no proof body

With that accepted short formula theorem in the prefix, this theorem passes
independently without the source's value bridge, formula theorem call and
repeated predicate:

```litex
thm r47_mean3_is_least_squares_center:
    ? forall a, b, c R:
        $r47_is_least_squares_center(r47_mean3(a, b, c), a, b, c)
```

[Complete short dependency slice and bodyless consumer](evidence/round-47-cases/mean-bodyless-nonnegative-prefix.lit).
The original consumer, value-and-call and call-only variants also pass with
this prefix. Bodylessness here is a verified consumer result, not a universal
rule for named predicates. The formula theorem itself misses bodyless, and
its candidate claim with no calculation body also misses cold.

## Negative and unknown boundaries

The false claim that0 is a least-squares center for observations1,1,1 rejects;
candidate1 has zero error while center0 has error3. Changing the decomposition
coefficient3 to2 also rejects. These are executable mathematical negatives.

Deleting even the scaled-square sign fact later returned a normal failure in
the persistent Session. Its very large response was truncated, so the earliest
failing proof phase is not established. The one-shot cold file reached an
explicit20-second observation limit and was
terminated as an independent file probe. Four consumer files sharing that
chain-only prefix also reached the limit. Their status is unknown, not rejected;
those observations do not establish a downstream mean-consumer defect. No
speedup, nontermination cause, or permanent mandatory-sign rule is inferred.
The accepted two-statement route is the verified improvement available now.

## Evidence and journal limitation

[Round47 receipt](evidence/round-47-2026-10-09.summary.json):16 source files,7 accepted,
4 rejected and5 observation-limit unknown. All11 completed strict outcomes
were rechecked at promoted paths with the fixed current-source snapshot. The
unknown files retain their actual draft commands and separate promoted artifact
paths; no unrun promoted command is presented as evidence. Normal outcomes
require exit/envelope agreement and no session error.

The warm orchestration queue was stopped without stopping Session25852. Its
in-memory journal was not retained on termination; literal source and observed
acceptances are saved as an explicitly partial journal, not invented full
responses. The original source theorem passed warm before the chain-only candidate.
After that candidate returned failure, the same Session accepted the retained
nonnegative version; its returned source/response is saved. Cold completed
outputs own this card's acceptance. No canonical/kernel/trust,
AST/Env/Runtime, whole probability showcase or performance change.
The warm Session is available again. Five bounded cold observations remain
unknown; the verified short slice supports subsequent corpus work.
