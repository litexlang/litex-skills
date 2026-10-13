# Historical Litex Problem-Solving Navigation

This file routes readers within the archived package. Its single workflow is
`litex_problem_solving_workflow.md`, which owns the six stages, logging lifecycle,
whole-problem acceptance, and post-task experience updates. Specialized documents
do not define another ordering. Current work uses the shared hub entrypoints.

## Entry documents

- Main workflow: `litex_problem_solving_workflow.md`.
- Problem extraction: `extract_problem.py`.
- Full-dialogue capture: `start_full_logging.py`.
- Error parser: `parse_litex_error.py`.

Start with the workflow, then read a specialist document when its stage or
problem requires it; this index is not a requirement to read every document.

## Stages and supporting material

| Stage | Supporting material |
| --- | --- |
| 0: start logging | start_full_logging.py |
| 1: extract the problem | extract_problem.py |
| 2: formalize | Syntax reference and builtin appendix, translation specification and exact theorem matching, geometry pitfalls and reserved names, cross-file references and path lookup |
| 3: prove | litex_proof_guide.md, including core mechanisms and decisions |
| 4: verify | parse_litex_error.py |
| 5: stop capture and archive | Main workflow |
| 6: review the log and record reusable experience | Update the relevant existing topic document; no problem-specific SOP |

## Specialist topics

Read only when needed:

- Coordinate geometry: `litex_coordinate_solving_sop.md`.
- Incremental debugging: the historical references
  `litex_session_verification_sop.md` and `litex-repl-try-workflow.md`.
  Not every source referenced by this old index is included in the archive.

## Original document-maintenance rules

1. The main workflow owns ordering; specialist notes are conditional references,
   not separate mandatory prereading lists.
2. Consult the relevant note at the actual stage or error rather than loading
   the entire index.
3. In stage 6, review agent_session.log and promote only reusable lessons
   supported by both the log and tool evidence into existing topic documents.
4. Do not create a lessons/SOP file for one problem. Historical problem IDs,
   retry counts, and temporary bridge theorems do not belong in general guidance.

Original update: 2026-09-23. Maintain the workflow and index together when
adding or removing documents in this archived package.
