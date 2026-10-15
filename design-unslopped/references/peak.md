# Peak: what separates the reference set from competent work

Competent UI is correct: hierarchy, palette, anatomy, spacing. The reference set is beyond that. Each
image was chosen because it stops the scroll, and the reasons are specific and learnable. Use this
file twice: before designing (to set the bar) and during the compare loop (as the rubric). Numbers
point to `design-notes.md` and `../assets/previews/NNN.jpg`; open the images, do not rely on the
descriptions.

## 1. Composition with tension

Peak screens are composed, not tiled. One region is given disproportionate space and the rest is
compressed around it. Look at:
- 046 Bankora: six cards of unequal weight on a strict grid, the dark calculator card as a counter-weight.
- 093 Portal: three numbers and one chart on an almost empty page; the emptiness is the design.
- 042 Kanto: a magazine headline occupying the top third, a floating insight card overlapping the grid.
- 069 Restro: four bare numbers on the page surface above cards; the row with no cards is the hero.
- 010 Formula 1: full-bleed photography with data placed only in the clear areas.
Test: cover the hero with your hand. If the rest of the screen looks the same as before, there was
no composition; the hero was just another card. Second test, for long screens: if every card below
the hero shares one anatomy (eyebrow, sentence title, rows) at one height and radius, the page is a
list of cards, not a composition. Vary it: one tall card, two compact ones, one with a different
device (portions, a grid, a chart), and cut what repeats what the hero already said.

## 2. Scale

The hero number or headline is bigger than feels safe: 56-84px on desktop, 36-44px on mobile, with
the unit, decimals or eyebrow at a fifth of that size. Contrast of scale is what makes it premium.
- 081 Vanta, 093 Portal, 049 Nueansa (digits with letter-spacing), 092 (+2.6% at ~64px with a two-line
  explanation beneath), 011 (£24,769 with the pence shrunk).
Test: the largest text on screen should be at least 4x the body size. If it is 2x, double it.

## 3. Atmosphere

Flat hex colours on white are correct and dead. The references have light and depth, in one place:
- A gradient with a visible light source (076, 083 red→orange; 017 deep blue; 020 violet).
- A glow anchored to one edge or corner (012, 025, 037, 050).
- A photo or render behind a dark scrim with data in the clear (010, 033, 024).
- Material: glass that reads as glass because something sits behind it (020 action tiles, 062, 076's
  card stack), or a 3D card render with a real reflection (027, 073).
- Grain or noise at 2-4% on a dark surface so black is not flat (033, 037).
Atmosphere is applied to the hero region only; everything else stays matte. Test: is there a single
place on the screen that looks lit? If not, add one; if there are three, remove two.

## 4. A bespoke element

Every peak screen has one thing that was invented for it, not pulled from a library:
- 023 treemap of contracts with icons in the tiles.
- 040 dot-matrix bar chart with a yellow selected column.
- 069 hexagon-dot customer heatmap; 030 cohort dot grid; 037 Sankey of assets.
- 046 cash-flow calculator with two inputs and a result on the dashboard.
- 013 nutrition score as a glass sphere; 014 calorie arc as discrete rounded portions.
- 001 scope rows with sparkline + value + "% of total" + delta, five facts per row.
- 017 payment lifecycle as a vertical timeline stepper with timestamps.
The bespoke element serves the one idea of the screen and is drawn by hand (SVG, CSS grid, custom
markup), never from a chart library's defaults. Test: name the element on your screen that a
competitor could not have. If none, you have not designed yet.

## 5. Typographic character

- Character comes first from how the body sans is set (weight contrast, tight tracking, scale), not
  from adding a second face. Where a second face appears it has exactly one role: a serif page title
  (017 "Transactions."), serif numerals in two references only (071, 081, both heavy), an italic
  word in a marketing headline (013, 074, 086), or condensed uppercase (007). See
  `typography.md` before choosing one; a thin display serif is now a generated-UI tell.
- Letter-spaced small-caps eyebrows above every big number (001, 046, 076).
- Mixed weight inside one line: bold greeting + regular question (021), bold value + light unit.
- Faded decimals, shrunk units, tabular figures everywhere.
Test: read the screen's type as a system: display / title / body / label / data. Five roles, two
faces at most, and the display role must be unmistakable.

## 6. Micro-detail density

Peak screens reward a second look. Within one card: a copy icon beside an ID, a relative time next to
an absolute one, a status dot that is actually a tiny ring, a hatch texture on the "other" segment, a
2px white ring on stacked avatars, a filled pill on the selected axis label, a privacy eye beside a
balance, a "vs last month" line in 12px grey, a ⌘K hint in the search field, a drag handle that
appears on hover. See 004, 017, 029, 036, 054, 068.
Test: zoom to 200% on any card. If nothing new appears, add two details that carry meaning.

## 7. Real-looking content

Peak screens read as a live product: plausible company names, mixed amounts with sensible
precision, one failed and one pending row, dates in sequence, a greeting that names a task,
insight sentences with a specific number, a disclaimer where one belongs. Lorem, "John Doe",
round numbers and uniform rows break the spell instantly (028, 041, 053 show the cost of typos).

## 8. Confidence

The screen commits. One stance, held everywhere; no hedging between light and dark; no "safe"
default blue; buttons are black or the accent, never grey-blue; the hero is not apologetic. 007 is
loud and 046 is silent and both are confident. Test: could this screen be the first image on the
product's website? If it needs a caption, it is not confident.

## The compare rubric

When the render is beside the three references, score each of the eight above as "matches /
weaker / missing" and fix the weakest first. A screen is ready when nothing is "missing" and at most
two are "weaker". Two rounds minimum; most screens need three.
