# Amazé Web

The amazeweb.shop website, built as static HTML/CSS from a Python generator —
a hand-coded replacement for the original Framer site.

## Layout

    build/content.py   all site copy, transcribed from the published site
    build/build.py     generates the 21 pages into the repo root
    assets/            css, fonts, images, js
    index.html         generated — do not edit by hand
    services/ templates/ support/ themes/   generated

## Build

    python3 build/build.py

Writes 21 pages: `/`, `/templates`, `/services` (+ `/setup`, `/custom`, `/tools`),
`/support`, and 14 `/themes/<slug>` pages. Everything outside `build/` and
`assets/` is generated output and is overwritten on every run.

## Design values

`assets/css/style.css` carries the measured geometry of the original site —
breakpoints (desktop ≥1200, tablet 810–1199, phone <810), the 1040px theme-page
column, section rhythm, and type scale. Comments mark the values that were
measured rather than derived; don't "tidy" those without re-measuring.
