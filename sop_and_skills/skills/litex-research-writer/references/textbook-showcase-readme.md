# Litex textbook and showcase READMEs

> Imported reference snapshot (2026-10-13). For execution use [the hub contract](../../litex-reference/references/execution.md). Repository paths and author preferences are scoped to the source project; dated examples are historical until replayed.


Use this maintainer-approved writing pattern for Litex textbook and showcase
READMEs unless the user requests a different form. The reference example is
`textbooks/The-Mechanics-of-Litex-Proof/README.md` in the Litex repository.
Treat it as an editorial model; choose claims and examples from the actual
artifact being documented.

The aim is to connect the direction of the whole artifact with the details of
its code: **positioning → mathematical progression → real examples → coverage
and navigation map**.

## Six characteristics to preserve

1. **Clear positioning.** Explain what the artifact is, its source or mathematical
   setting, who it serves, and why it exists. For a textbook adaptation, credit
   the original author and book. Mention Lean or another source system when it
   is actually part of that source, and explain the comparison's purpose.
2. **A mathematical thread.** Show how the reader progresses through ideas.
   Mechanics moves from calculation to definitions and constructions, then to
   functions, sets and relations. Another book or showcase should have its own
   mathematical learning or reasoning path.
3. **Small examples revealing larger mechanisms.** Use a few short examples
   drawn from checked source. Explain the mathematical statement, the key code
   and the Litex mechanism it makes observable. Mechanics uses an
   assumption-to-conclusion fact, an oddness definition with a witness, and a
   function whose domain condition is in its declaration. Select examples that
   reveal the current artifact's actual design choices; no fixed count or
   identical trio is required.
4. **Accurate conceptual layers.** Distinguish mathematical objects such as
   numbers, sets, functions and tuples; facts such as equality, membership and
   quantified properties; and definition/proof commands used to construct
   objects, establish facts and reuse results. This distinction should emerge
   naturally from the examples.
5. **A view of the whole after the details.** Follow the examples with a compact
   coverage map of demonstrated objects, concepts and proof tools. For books,
   map them to chapters; for showcases, map them to examples or modules. A
   table is usually useful. Include only demonstrated capabilities, with
   locations readers can actually find.
6. **Deliberate selection.** Retain purpose, source, useful examples, coverage,
   navigation and supplied maintainer credit. Keep paragraphs short and give
   each one a distinct job. The README should explain the artifact's
   mathematical content and what it reveals about Litex.

## Applying the pattern

Start with a brief introduction, then let concrete examples make the main
Litex characteristics visible. Explain syntax only as far as needed to
understand the mathematical move. Follow with the coverage map and useful
contents or example links. Headings and section count may vary with scope.

A short source attribution or comparison purpose may appear in the opening.
Support substantive Lean/Litex comparisons with the examples that follow;
preserve the same mathematics and avoid unsupported claims of superiority.
A focused showcase may need only one mathematical thread and a small map.
Do not inflate it into a textbook or a research manifesto.

Keep migration notes, update history, debugging, failed attempts and internal
verification receipts in their working records. Omit local installation,
build and run recipes by default. If the user requests usage guidance, refer
to official Litex installation and CLI documentation and use its conventions.
Keep relevant mathematical conditions and capability boundaries visible when
they affect the reader's understanding.

Preserve supplied attribution and maintenance credit. The Mechanics README
uses `Maintained by Jiachen Shen.`; do not infer authorship or maintenance for
another artifact without evidence.

## Completion check

Read the introduction, examples, transitions and coverage map together. Can
the reader understand why the artifact exists, follow its mathematics, see a
Litex characteristic in actual code, and find the relevant chapter or example?
Check source attribution, local links and every claimed capability against the
artifact. Verify runnable snippets in the required Litex context under the
applicable proof workflow; keep excerpts short without changing their meaning
or hiding necessary conditions.
