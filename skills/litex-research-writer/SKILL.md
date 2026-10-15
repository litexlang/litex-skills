---
name: litex-research-writer
description: Write evidence-based Litex explanations, module documentation, comparisons and research material. Use when communicating mathematical meaning, verifier behavior and verified scope.
---

# Litex research writer

Lead with a concrete user-visible behavior and its evidence. Distinguish
source mathematics, assumptions, checked source, historical results and
proposed capabilities. A small proof is not an untested general capability
or performance claim.

1. Identify the audience and the exact claim the artifact should communicate.
2. Anchor the real source, mathematical statement, command, executable and
   assumption boundary. Use [reference routing](../litex-reference/SKILL.md)
   for live docs and a relevant showcase.
3. For module documentation describe implemented interfaces in README and
   important mathematical design/dependencies in `math_collections.md`.
   Explain partial chapters, scalar models and remaining debt explicitly.
4. Show a complete small example with its actual result. For executable source
   use [the foundation](../litex-basics/SKILL.md) and
   [proof writing](../litex-proof-writer/SKILL.md); do not present an unrun
   excerpt as verified evidence.
5. Keep comparisons aligned on statement, assumptions and measured scope.
   Report unknowns and implementation boundaries honestly.
6. For public explanations or research packets, let source evidence support
   each capability claim. Drafting outreach does not authorize sending it.

Expanded mode-specific historical guides remain in the source edition.
Use [review](../litex-review/SKILL.md) when prose and the accepted mathematical
statement need an independent read-only consistency check.
