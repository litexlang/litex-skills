# IMO 1968, problem 4

Show that every nondegenerate tetrahedron has a vertex whose three incident
edge lengths can be the sides of a nondegenerate triangle.

Source: [official IMO 1968 problem sheet, problem 4](https://www.imo-official.org/problems/1968/eng.pdf).
The archived dataset calls this problem **16**. Its `problem` field matches
the source; its `statement` paraphrase adds six distinct edge lengths. This
experiment follows the original problem and allows equal edge lengths.

## Frozen mathematical task

Write `ab`, `ac`, `ad`, `bc`, `bd`, `cd` for the six positive edge lengths of
vertices A, B, C, D. Define `triangle_edges(x,y,z)` by all three strict triangle
inequalities. The four faces give:

| Face | Length triple |
| --- | --- |
| ABC | ab, ac, bc |
| ABD | ab, ad, bd |
| ACD | ac, ad, cd |
| BCD | bc, bd, cd |

Prove that at least one of these four **incident** triples is a triangle:

| Vertex | Length triple |
| --- | --- |
| A | ab, ac, ad |
| B | ab, bc, bd |
| C | ac, bc, cd |
| D | ad, bd, cd |

The literal definition and universal goal are in `prefix.lit` and `goal.lit`
in a prepared run. The checker composes the unchanged prefix, the agent's proof
and the unchanged goal. A passing file containing only a trivial identity cannot
satisfy that acceptance gate.

## Geometry boundary

Every ordinary nondegenerate Euclidean tetrahedron supplies positive lengths
and four nondegenerate triangular faces, so the length theorem applies. The
formal task proves the stronger implication for any six positive numbers
satisfying those four face conditions, without a distinctness premise.

The Euclidean distance construction, coordinate realizability and derivation
of face inequalities from 3D coordinates are explained here as the geometric
interpretation; they are not formalized in this example. Report a checked
edge-length formulation, not a separately checked 3D geometry library. The old
planar `library_final.lit` is retained in the archive and is not a dependency.
