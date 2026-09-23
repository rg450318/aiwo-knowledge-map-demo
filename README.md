# AiWo knowledge map — interactive demo

Pick a manual, type a word, and the page draws the local knowledge map around
the matching section of a heavy-machinery operator manual. Click any dot to open
the map behind it.

Open `index.html`, or visit the hosted page. One self-contained file: no server,
no build step, no network access, works offline. Add `#h7`, `#c50` or `#engine`
to the URL to open straight onto one manual.

## What it shows

Research prototype from **Task 2.4** of the AiWo project (Business Finland),
University of Helsinki, Faculty of Educational Sciences.

An AI manual answers the question you asked. It cannot show you the question you
did not know to ask. After each answer, the map shows what else in the manual
bears on the task — the hazards that govern it, its sister procedures, the
sections that discuss the same thing — so the next question can be picked rather
than invented.

The map is derived automatically from each manual's own text. There is no
ontology and no hand curation.

| Manual | Pages | Sections | Hazard types | Typed links |
| --- | --- | --- | --- | --- |
| H7 harvester head | 346 | 135 | 11 | 183 |
| C50 crane | 120 | 79 | 7 | 57 |
| Scorpion King 8W engine | 91 | 47 | 6 | 63 |

Links are typed — hierarchy, cross-reference, warns, shared hazard, semantic
similarity — so when two things are linked the reason is always recoverable.

## How hazards are found

Every safety callout in these manuals is drawn the same way, a pale-yellow box
with a signal icon in the margin, but manuals differ in what goes inside. The
pipeline first detects which convention a manual uses, then extracts
accordingly:

| Convention | Manuals | How the hazard is named |
| --- | --- | --- |
| Titled callouts | H7, C50 | The box opens with an all-caps title such as `CHAIN SHOT HAZARD`; the title is the hazard. |
| Untitled callouts | Scorpion King engine | The box holds only the instruction; the hazard type is read from its wording, using the same hazard names as the titled manuals. |

The boxes and icons are read from the PDF's vector drawings, because plain text
extraction loses them. A callout becomes a hazard only if its text names one.

## Source material

Structure derived from Ponsse operator manuals, used within the AiWo research
consortium. **The manuals themselves are not included and not redistributed.**
This page carries only section titles, the typed links between them, and
per-section term lists for the search box. No prose from any manual appears in
this repository.

## Using it

| | |
| --- | --- |
| Manual pills | Switch manual; map, search, legend and panel all follow. |
| Search | Two letters or more; matches titles, section numbers and section vocabulary. "Also in" shows strong matches in the other manuals and switches to them in one click. |
| Click a dot | Opens that node's two-hop neighbourhood. |
| Legend | Click an edge type to filter it from map and panel. |
| Breadcrumbs | Retrace your path; `Back` steps up one. |
| Drag / scroll | Move a node, pan the background, zoom, `Fit` to reframe. |

## Layout

Fruchterman–Reingold forces (repulsion `k²/d`, attraction `d²/k`), integrated as
damped velocity under a cooling heat that reaches a full stop, with positions
confined to a circular frame. The clicked node is not pushed by forces; it glides
to the centre and everything else arranges around it. Hand-written, no
dependency.

## Rebuilding

`graphs/*.json` hold one graph per manual. `_template.html` is the page with a
`/*__MANUALS__*/` placeholder; `python3 build.py` inlines the graphs into
`index.html`. To add a manual, add one line to the list in `build.py`.
