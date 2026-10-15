# Part127 — Actual divisibility witnesses: thirteen proof actions become eight

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.
> Receipt links in this edition contain summaries, not full verifier output. Original hashes, commands and recorded outcomes are retained; see [evidence packaging](evidence-packaging.md).


## Mathematical situation

The number-theory showcase defines an integer witness predicate:

```litex
prop divides_by(d,n Z):
    exist k Z st {n=d*k}
```

This includes zero dividing zero. Preserve it and the exact premises/goals of
transitivity and common-divisor linear combination. Do not replace witnesses
by quotients or add a nonzero/positive divisor requirement.

## Transitivity: six actions become four

Under a,b,c in Z, divides_by(a,b) and divides_by(b,c), retain:

```litex
obtain k from $divides_by(a,b)
obtain m from $divides_by(b,c)
c=b*m=(a*k)*m=a*(k*m)
witness $divides_by(a,c) from k*m
```

The original repeated `b=a*k` after obtain and repeated `c=a*(k*m)` inside a
witness proof body can be omitted jointly. The witness itself checks its body
condition from the preserved calculation. Only obtains plus witness rejects;
the witness body equality fails search_proof. Shortening the calculation to
`c=b*m=a*(k*m)` or its bare endpoint rejects in the tested source.

## Linear combination: seven actions become four

Under d,a,b,x,y in Z and both divisibility premises, retain:

```litex
obtain p from $divides_by(d,a)
obtain q from $divides_by(d,b)
a*x+b*y=(d*p)*x+(d*q)*y=d*(p*x+q*y)
witness $divides_by(d,a*x+b*y) from p*x+q*y
```

The original a=d*p and b=d*q echoes plus nested witness body equation can be
removed jointly. The expanded factorization chain remains: deleting it or
using only its direct endpoint rejects. This is a checked short route, not a
claim of a globally shortest proof or automatic divisibility tactic.
[Complete preferred slice](evidence/round-99-cases/joint-short.lit).

## Positive consumers and negatives

Zero-divisor and signed-coefficient consumers pass. The shortened theorem is
called at d=0,a=b=0,x=-3,y=5 without stronger assumptions, and at d=-2,a=6,
b=-4,x=-1,y=3. The existing concrete transitivity example also remains passing.
The source's gcd certificate for 84 and 30 consumes the shortened linear-combination
theorem successfully. Original and shortened full standalone source both pass
through the later Diophantine and congruence proofs.
[Complete short draft](evidence/round-99-cases/short-full-standalone.lit).

Wrong transitivity witness k+m and wrong linear-combination witness p*x+q*y+1
reject. Removing the second common-divisor premise rejects. The latter changes
the mathematical statement; it differs from calculation deletion/direct-endpoint
misses for a true statement. No extra witnesses, trust or new division guards.

## Evidence

[Receipt](evidence/round-99-2026-10-10.summary.json):15 strict files,
7 accepted/8 Normal rejections, all promoted paths rerun with matching exits,
Normal envelopes and null session errors. Math source/binary identities recorded;
fixed snapshot from successful round88 build reused. New number-theory source
family; Part28's builtin modulo/gcd coverage is distinct from these witness proofs.
No permanent general-rule promotion from this one source.

Session99399 uses the accepted divides_by prefix. The failed first witness route
and successful calculation repairs stay in that Session; renamed theorem calls
are discovery evidence only, cold files own deletion gates.
[Session journal](evidence/round-99-session.summary.json) explicitly marks the truncated
first tool response; the receipt owns full cold failure outputs. The first
non-PTY startup reached normal EOF, then PTY startup retained the live Session;
no ordinary statement failure triggered a restart.
No canonical/kernel edits, new bt, performance, whole-module or moving-kernel
acceptance claim.
