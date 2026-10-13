# Part 110 — Group homomorphism proofs: native theorem calls own their results

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Source mathematics and retained abstraction

The abstract-algebra showcase proves that a group homomorphism preserves
identity and inverses, using group_left_cancel and group_inverse_unique.
Keep its existing GroupSetting/GroupHomomorphismSetting predicates, generic
nonempty carriers, source group theorems and all original assumptions. Reuse
these mathematical interfaces rather than rebuilding group cancellation.

## Shortened identity proof

With the original theorem binder and homomorphism premise, retain:

```litex
mul_A(one_A,one_A)=one_A
mul_B(f(one_A),f(one_A))=f(mul_A(one_A,one_A))=f(one_A)=mul_B(f(one_A),one_B)
release thm group_left_cancel(B,mul_B,one_B,inv_B,f(one_A),f(one_A),one_B)
```

The source's following f(one_A)=one_B repetition is removable. The theorem
call stores the needed result; four body statements become three. Deleting
the first source multiplication fact instead fails in the subsequent chain.
That concrete value is a useful bridge inside f(...), unlike the final echo.

## Shortened inverse proof

Under the original homomorphism premise and with a in A, retain:

```litex
release thm homomorphism_maps_identity(A,mul_A,one_A,inv_A,B,mul_B,one_B,inv_B,f)
mul_A(inv_A(a),a)=one_A
mul_B(f(inv_A(a)),f(a))=f(mul_A(inv_A(a),a))=f(one_A)=one_B
release thm group_inverse_unique(B,mul_B,one_B,inv_B,f(a),f(inv_A(a)))
```

The source repeats f(one_A)=one_B after the first call and repeats
f(inv_A(a))=inv_B(f(a)) after the second. Both can be removed together:
six body statements become four. Deleting the source product fact instead
fails. An empty inverse theorem body misses; the retained theorem calls and
calculation remain meaningful mathematical proof moves.

[Full combined short source](evidence/round-71-cases/combined-short.lit)
contains exact binders, definitions and prerequisite theorems; the blocks
above are excerpts. Joint deletion of all three result echoes passes.

## Actual downstream consumer and negatives

The next source theorem kernel_is_normal_subgroup uses both homomorphism
theorems to prove closure under inverses and conjugation. The original source
through this theorem passes, and the same source with only the two shortened
homomorphism bodies also passes. This checks an actual downstream consumer,
not just the isolated shorter theorem declarations.
[Short source through normal kernel](evidence/round-71-cases/short-through-normal-kernel.lit).
Later struct-based APIs and the full showcase are outside this gate.

Wrong inverse conclusion f(inv_A(a))=f(a) rejects, as does removing the
homomorphism premise. These are distinct from the true empty-body or product-
fact deletion misses. No group-law, injectivity or scalar-sign assumption is
introduced to simplify the source proof.

## Fixture correction and evidence

An initial unanchored indentation substring accidentally deleted theorem
goals while removing body echoes. Three initial results are explicitly
excluded in the receipt. Exact-line deletions corrected the fixtures, asserted
the original goals remained, and reran them. Their old parse/proof failures
are author generation errors, not Litex capability observations.

[Receipt](evidence/round-71-2026-10-09.summary.json):12 corrected strict files,
7 accepted/5 Normal rejections, all promoted paths rerun on the fixed snapshot
after successful current-source release build. Source/binary hashes retained.
Session66922 stays on round68 and accepted source group theorem dependencies,
the existing homomorphism predicate and both shortened theorem statements;
cold round71 owns deletion and downstream evidence. No canonical source,
kernel, trust, protected owner, performance or whole-showcase claim.
