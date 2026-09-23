# AiWo knowledge map — interactive demo

Type a word and the page draws the local knowledge map around the matching
section of a heavy-machinery operator manual. Click any dot to open the map
behind it.

Open `index.html`, or visit the hosted page. One self-contained file: no
server, no build step, no network access, works offline.

## What it shows

Research prototype from **Task 2.4** of the AiWo project (Business Finland),
University of Helsinki, Faculty of Educational Sciences.

The premise is that an AI manual answers the question you asked, but shows you
nothing of the structure the answer sits inside. This layer adds that
structure: the hazards governing a procedure, its sister procedures, and the
sections that discuss the same thing, all surfaced without a follow-up query.

The map is derived automatically from the manual's own text. There is no
ontology and no hand curation.

| | |
| --- | --- |
| Nodes | 146 — 135 manual sections plus 11 hazard types |
| Edges | 183 typed links |
| By type | hierarchy 69 · LSA similarity 41 · cross-reference 25 · shared hazard 24 · warns 24 |

Every edge is typed, so when two things are linked the reason is always
recoverable: structural edges trace back to specific text, semantic edges to a
cosine value.

## Source material

Structure derived from a Ponsse H7 harvester-head operator manual, used within
the AiWo research consortium. **The manual itself is not included and not
redistributed.** This page carries only section titles, the typed links between
them, and per-section term frequencies for the search box. No prose from the
manual appears anywhere in this repository.

## Using it

| | |
| --- | --- |
| Search | Two letters or more; matches titles, section numbers and section vocabulary. Enter picks the top hit. |
| Click a dot | Opens that node's two-hop neighbourhood. |
| Legend | Click an edge type to filter it from both map and panel. |
| Breadcrumbs | Retrace your path; `Back` steps up one. |
| Drag / scroll | Move a node, pan the background, zoom, `Fit` to reframe. |

## Layout

Fruchterman–Reingold, hand-written, no dependency. Repulsion `k²/d`, attraction
`d²/k`, per-tick displacement capped by a cooling temperature, positions
confined to a circular frame. The frame is load-bearing: the graph is sparse,
so most node pairs only repel, and total repulsion grows with node count while
centre gravity is only linear. Without it the layout drifts apart indefinitely.

## Rebuilding

`_template.html` is `index.html` with a `/*__DATA__*/` placeholder in place of
the data. Edit the template, then substitute `graph.json` back in.
