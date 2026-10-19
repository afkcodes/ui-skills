# Craft: the execution details that separate the references from generated UI

The principles say what goes on screen. This file says how it is drawn. Every number below is read
off the reference set; where references disagree, the range is given and the most common value is
first. Apply these by default; deviate on purpose.

## Type

Read `typography.md` first; it has the counts. Summary:
- Classify the brief into one of the eight voices in `typography.md` (neutral grotesk, tight modern
 grotesk, friendly geometric, humanist, light rounded, editorial serif + sans, marketing display,
 condensed brand-loud) and choose from that voice's roster, avoiding the face you used last time.
 Load it. Never system-ui, never a face the three chosen references would not use.
- Money and every number: the body sans at 500-600, `letter-spacing` −0.02 to −0.04em,
 `font-variant-numeric: tabular-nums`, line-height 1.0-1.1. Currency symbol same size, weight and
 colour as the digits. Decimals optionally at 55-65% size and 40-50% opacity.
- Hero number 32-56px desktop, 28-40px mobile. Exactly one per screen. KPI numbers 24-32px,
 legend and row amounts 14-16px, all the same sans.
- Titles 16-18px 600; body 14px 400 line-height 1.5; secondary 12-13px grey; eyebrows 11-12px
 500-600 uppercase +0.06em in grey, above every hero number.
- Display serif only when two of the three references use one, and then heavy and high-contrast
 (Fraunces, Newsreader 600+, Source Serif 4 600+) at 32-44px for numerals or 28-40px for a page
 title. Italic words only on marketing pages.
- Greys for text on white: primary #0f1115-#1a1a1a; secondary #6b7280-#737373; tertiary #9ca3af.
 On dark: #f5f5f5 / rgba(255,255,255,.6) / rgba(255,255,255,.4).

## Surfaces, borders, shadows

- Light page background: #f6f6f7, #f5f5f4 (warm), #f7f8fa (cool), or #fafafa. Cards #ffffff.
 Sidebar either the page grey or white with a 1px right border.
- Card border: 1px solid #e9e9eb (cool) / #ebe9e6 (warm). Or no border and a shadow:
 `0 1px 2px rgba(16,24,40,.04), 0 1px 3px rgba(16,24,40,.06)`. Elevated/floating:
 `0 8px 24px rgba(16,24,40,.08)`. Never both a hard border and a big shadow.
- Nested wells (tiles inside a card): background #f6f6f7, no border, radius one step smaller.
- Dark page: #0f0f10-#141416. Cards #1a1a1d-#1e1e22. Borders rgba(255,255,255,.08). Hover
 rgba(255,255,255,.04). One radial glow max, 20-30% opacity, anchored to a corner or edge.
- Radius scale: 6 (chips, small inputs), 10 (buttons, inputs), 14-16 (cards), 20-24 (hero cards,
 sheets), 999 (pills, avatars). Mobile cards 16-20.
- Padding: cards 20-24px desktop, 16px mobile. Card title row to content 16px. Section gap 24px
 desktop (16 mobile). Grid gutter 16-24px.

## Colour recipes

- Accent: one hue, used at full strength for the primary button, the active nav item, the selected
 bar/point, and links. Accent-tint = same hue at 10-12% for selected rows, hover, and chip
 backgrounds.
- Semantic: green #16a34a / tint #dcfce7; red #dc2626 / tint #fee2e2; amber #d97706 / tint
 #fef3c7; blue #2563eb / tint #dbeafe; neutral chip #f3f4f6 with #6b7280 text. On dark, tints
 become the hue at 15-18% opacity with the hue at 80% lightness for text.
- Chip: 11-12px, weight 500, padding 2-3px 8px, radius 6 or 999, tint background, hue text,
 optional 12px glyph before the word with 4px gap.
- Delta chip: same as chip, with ↑/↓ or ▲/▼ glyph; "+12%" green, "−4%" red.
- Data series: accent for the primary series; a second hue only if two series must coexist;
 previous period in #d4d4d8 or dashed. Categorical palettes stay at 3 hues, chosen so no two are
 adjacent on the wheel (orange / violet / green; navy / orange; coral in three tints).
- Hatching for inactive / projected / "other": `repeating-linear-gradient(135deg, #e5e7eb 0 2px,
 transparent 2px 6px)` on light; rgba(255,255,255,.12) stripes on dark.
- Icon in a tinted square or circle (KPI tiles): 32-36px box, radius 8-10 or 999, background
 accent-tint or category tint, icon 16-18px in the hue.

## Buttons and inputs

- Primary: accent or #111 fill, white text, 36-40px tall desktop (44-48 mobile), padding 0 14-16px,
 radius 10, weight 500, 14px. Secondary: white fill, 1px #e5e7eb border, dark text. Ghost: no
 border, grey text, hover tint. Icon buttons 36px square or round.
- Inputs: 40px tall, 1px #e5e7eb, radius 10, 14px, padding 0 12px, placeholder #9ca3af; focus
 ring 2px accent-tint outside a 1px accent border. Label above (12-13px, weight 500), helper
 below (12px grey). Prefix/suffix (currency, ⌘K) in grey inside the field.
- Segmented control: 32-36px, container #f3f4f6 radius 10, active segment white with the small
 shadow, 13px weight 500.
- Pill tabs: 32-36px, active fill #111 or accent with white text, inactive transparent grey text.

## Icons and avatars

- One family, 1.5px stroke (Lucide, Phosphor Regular, Tabler). 16px inline, 18-20px in nav,
 24px in quick-action tiles. Never mix filled and outlined in one view except the active nav
 item.
- Avatars 32-36px round in lists, 24px stacked with a 2px white ring and −8px overlap, "+6"
 overflow chip in grey. Merchant logos: 36px rounded square with the brand mark, or coloured
 initials on a tint when no mark exists.

## Charts (SVG, drawn by hand or helper)

- Line: 2px stroke, round joins, slight smoothing; area fill = series colour fading to
 transparent (linear gradient, 18% → 0). Previous period 1.5px dashed grey.
- Bars: radius 4-6 on top (or full capsule on dark), 60-70% of the slot width; unselected bars
 #e5e7eb (light) or rgba(255,255,255,.08) (dark); the selected bar in the accent with a callout
 pill above (value) and the x label below in a filled pill.
- Gridlines: 1px #f0f0f1 (light) / rgba(255,255,255,.06) (dark), horizontal only, 3-5 of them;
 no vertical gridlines; axes have no lines, labels only (11-12px grey).
- Tooltip: dark #111 pill, white 12px, radius 8, small shadow, shows the x label and each series'
 value with a coloured dot; a 1px dashed vertical cursor line.
- Segment bar: 8-10px tall, radius 999, segments with 2px gaps; legend rows below with dot, label,
 amount right, "(24%)" grey.
- Gauge / ring: 8-12px stroke, round caps, track #e5e7eb, value in the centre at display size with
 the unit smaller.
- Sparkline: 1.5px, no axes, 24-32px tall, inside KPI tiles.

## Data that looks real

- Mixed, plausible names and merchants (Nordic Brand Co., Acme Studios, Sirius Tech Ltd, Netflix,
 Uber); mixed amounts with sensible precision (£1,200.00, −£55.00, +£18,450.00); dates in the
 product's locale; times with minutes; at least one negative, one pending, one failed in any list.
- Numbers agree with each other: totals sum, percentages add to 100, deltas match the two periods.
- Balances in the thousands to tens of thousands for consumer, hundreds of thousands for business;
 not round numbers.

## Spacing rhythm (the thing most generated UI gets wrong)

- 8px base grid. Inside a card: title row (20-24px tall) → 12-16px → content → 16px → footer.
- KPI tile: 20px padding; label → 8px → number → 6px → context line.
- List row: 12-14px vertical padding, 12px gap between glyph and text, 8px between primary and
 secondary line (line-height does most of it).
- Table cell padding: 12px 16px. Header cell 10px 16px.
- Between cards: 16-24px. Page padding: 24-32px desktop, 16px mobile.
- Align numbers right and text left; align icon centres to the first text line, not the block.

## The 1% details that read as "designed"

- Faded decimals on money; tabular numerals; a thin hairline between list rows instead of card
 separation; a 2px white ring on stacked avatars; a ⌘K hint inside the search field; a small
 grey "vs last month" line; a tiny dot before a live status word; a filled pill on the selected
 x-axis label; hatched projection bars; a copy icon beside IDs; a privacy eye beside a balance;
 a greeting with a helper sentence; a relative time ("in 1 week") next to an absolute date.
- Pick four or five of these per screen, consistently, instead of trying all of them.
