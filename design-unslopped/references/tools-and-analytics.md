# Tool mode: analytics, admin, ops and developer dashboards

Product analytics (PostHog, Mixpanel, Amplitude, Firebase, Matomo, GA4), observability, admin
consoles, ops and dev tools are a different kind of object from the reference set's hero-led
dashboards. People work inside them for hours, build their own views, and read eight series at
once. The bar is clarity at density, and the peak examples in the set are the quiet ones: 
Skymetrics, 036 Sypher, 052 Alignify, Shopeers, 060 Insighta (dark), 063 Buildly, 081 Vanta,
and in the analytics batch 101 Vectra, 103 Trace, 108 RevenuePulse, 114 cohorts, 117 LeonAnd, 122
privacy analytics, 125 web vitals, 126 Untitled UI, 129 Beast. 028, 133 and 142 are the negatives. When the brief is a tool, read this file after `peak.md` and apply the
adjustments in §1 before anything else.

## 1. What changes in tool mode

| Rule elsewhere in the skill | In tool mode |
|---|---|
| One hero taking 35-45% of the screen | A **north-star row** (2-4 metric cards) or one **primary insight at 2x width**; the rest is a grid of equal-weight insights. The user's saved layout is the composition. |
| Largest text ≥ 4x body; hero number 56-104px | Metric cards 28-36px; body 13px; table 12-13px. Nothing above 40px. Scale contrast comes from the north-star row vs the grid, not from one giant figure. |
| Atmosphere in one place (glow, gradient, grain) | None, or a 2% tint on the north-star row. Flat surfaces, hairlines, white or near-white page. Dark only if the product is dark by brand (060, 063). |
| 0-2 data colours | A **categorical palette of 8-10** (§6) for breakdowns, plus semantic green/red for deltas; hover isolates one series and greys the rest. |
| Signature move per screen | The signature is a **chart type rendered precisely**: a retention triangle, a funnel with drop-off, a path diagram. Precision is the flourish. |
| Scroll-stop test | **Live-in test**: after an hour, does anything on the screen get tiring, ambiguous, or need re-reading? |
| Sentence card titles | Insight titles are the **query**: "Signups by platform · weekly · last 90d". A sentence may sit under the north-star row as the one insight line. |
| Decoration budget by domain | Zero. Icons 16px, one stroke. No illustration, no renders. |

Everything else holds: one accent for selection and the primary action, status as text + glyph, tabular
numerals, real content, consistent anatomy, proofread copy.

## 2. Information architecture

- **Left nav (220-240px)**: project / environment switcher at the top (with a coloured dot for
 prod/staging), search ⌘K, then product areas as groups: Dashboards · Insights (Trends, Funnels,
 Retention, Paths, Lifecycle, Stickiness) · Users / Cohorts · Session replay · Feature flags ·
 Experiments · Surveys · Data (Events, Properties, Sources, Destinations) · Settings. Collapsible
 groups, pinned items, recently viewed. Active item filled with a tint.
- **Top bar**: breadcrumb (Project › Dashboards › Growth), dashboard title editable inline, right:
 **date range picker** ("Last 30 days ▾") with a **Compare to previous period** toggle, global
 filters as pills, "Share", "Add insight" (the one primary), refresh / last-computed timestamp
 ("Computed 3 min ago · auto-refresh 5m"), kebab.
- **Filter pills**: `property = value ×` chips in a row under the title; "+ Add filter". Breakdown as a
 pill with a different icon. Active pill count badge when collapsed.
- **Query builder** (insight edit view): left panel of stacked rows — Series A/B/C each with event
 picker, math (Total · Unique users · Sum of…), per-series filters; then Filters, Breakdown by,
 Formula; right side the chart with chart-type tabs (Trend · Number · Table · Pie · Bar · World map).
 Each series letter colour-matched to its line.

## 3. Insight card anatomy (the grid unit)

Header (36-40px): title (13px 500, truncates) · subtitle in grey (query summary: "Unique users ·
weekly · breakdown: platform") · right: time-range override chip if it differs from the dashboard,
"⋯" menu (edit, duplicate, move, delete, export), drag handle on hover.
Body: the chart, minimum 180px tall at 1x, 240px at 2x; padding 12-16px; chart fills the width.
Footer (optional, 24px): legend chips or a one-line note ("Excludes internal users").
Sizes: 1x1, 2x1, 3x1 (full), 2x2 for tables. The grid is 12 columns, 16px gutter, row 320px.
States: loading skeleton (grey blocks in the chart's shape), empty ("No events matched · Edit
filters"), error ("Query timed out · Retry"), stale (clock icon + "Last computed 2h ago").

## 4. The north-star row

2-4 metric cards across the top, 1x1 each or one connected strip with hairlines. Anatomy: label
(13px grey) · value (28-36px 600, tabular) · delta chip vs the compared period (+12.4% green / −3.1%
red) with "vs previous 30d" in 12px grey · 32px sparkline for the period · optional target line on
the sparkline. One insight sentence may run under the row: "Signups up 12% on last month; retention
flat." Nothing else on the page is bigger than these values.

## 5. Chart types and how to draw them

Evidence in `design-notes.md` (previews `assets/previews/`): query builder 101; funnels 108 (complete
page), 109 (builder + step settings), 110 (dark), 112 (stream), 144 (capsules); cohort triangle 114,
stacked retention units 115; live event feed 103; experiments table 143; web vitals 125; treemap of
pages + anomaly heatmap 122; editorial report-as-dashboard 117; monochrome dark 129; goal lines under
KPIs 139; the neutral floor 126; negatives 133 (HUD chrome), 142 (rainbow tiles).

**Trends (line/bar, many series)**: 1.5-2px lines, no dots except on hover; up to 8 series in the
categorical palette, "Other" in grey; legend as a row of chips under the chart with the current
value, clickable to toggle, hover isolates (others to 25% opacity); compared period as the same
colour dashed at 60%; 3-5 horizontal gridlines; x labels every 2-7 ticks; tooltip lists all series
sorted by value with coloured squares; annotations as small flags on the x-axis (release, incident).

**Number (big value)**: as north-star card. If it has a breakdown, a compact table beneath.

**Funnel**: horizontal steps as columns; each step a bar whose height is its count, with the
conversion % from the previous step above the gap and the overall % at the top; drop-off shown as
a lighter or hatched remainder; step labels under each bar with the event name and count; median
time between steps as a small grey label on the gap; optional breakdown as stacked segments per
step. Vertical variant for mobile. Never a 3D or tapering "funnel" shape.

**Retention (cohort triangle)**: rows = cohort start week, columns = Week 0…N; cells coloured on a
single-hue sequential scale by %, value in the cell (12px, tabular), Week 0 always 100% and muted;
the right-hand triangle empty (future); row header shows cohort date and size ("w/c 1 Sep · 1,240");
a summary line chart above or below of mean retention by week. Hover a cell: cohort size and count.

**Paths / Sankey**: nodes as rounded rectangles with event name and count, left-to-right by step;
links as curved bands with width ∝ users, 25% opacity in the categorical colour of the source;
drop-off as a grey stub leaving each node; max 5 nodes per step with "+n more".

**Lifecycle / stickiness**: stacked bars (new, returning, resurrecting, dormant) around a zero line
with dormant below zero; stickiness as a histogram of "days active".

**Distribution / histogram**: bars with a median and p90 marker; log scale option labelled.

**World map**: choropleth with a 5-step single-hue scale and a legend; countries hoverable; a ranked
table beside it.

**Live events / event explorer**: a dense table, 36px rows, monospaced event names, relative time
("12s ago"), property chips, a live indicator dot; pause/resume control; expand row for JSON.

**Session recordings list**: rows with user, duration, pages, errors count, a thin activity strip
(click/scroll/error ticks), and a play affordance.

**Feature flags / experiments**: table with key (mono), rollout % as a mini bar, status chip
(Active / Disabled / Scheduled), variants as small coloured squares with %, a result card with
probability of being best and a confidence interval drawn as a horizontal bar with a centre tick.

## 6. Palette for many series

Base: page #ffffff or #fafafa; cards #ffffff with 1px #e5e7eb; text #111827 / #6b7280 / #9ca3af.
One accent (brand) for selection, links and the primary button.
Categorical (ordered, 8-10, perceptually distinct, holds on white):
`#2563eb` blue · `#f97316` orange · `#16a34a` green · `#9333ea` purple · `#dc2626` red ·
`#0891b2` cyan · `#ca8a04` yellow · `#db2777` pink · `#6b7280` grey (Other) · `#a16207` brown.
Dark variants: raise lightness one step. Sequential (retention, maps): one hue from 8% to 90% in
5-7 steps; never rainbow. Semantic: green/red for deltas only; never reuse them as series colours
unless the series *is* success/failure (then say so in the legend).

## 7. Density, type, spacing

- Type: a neutral or tight grotesk (Inter, Geist, IBM Plex Sans, Public Sans) at 13px body, 12px
 table and axis, 11px eyebrows, 14-15px titles, 28-36px metric values. Tabular numerals everywhere.
 Mono (JetBrains Mono, IBM Plex Mono) for event names, keys, IDs.
- Rows 36-40px in tables; 8px gutters inside cards; 16px between cards; page padding 24px.
- Borders over shadows; radius 6-8px on cards, 4-6px on chips; no shadows except on menus.
- Everything aligned to the grid; charts share y-axis widths across a row where possible.

## 8. States that matter more here

- First-run / no data: an onboarding card with the SDK snippet, "Waiting for events…" with a live
 dot, and sample dashboards offered.
- Sampling / approximation: a small chip "Sampled 10%" or "≈" on the value, with a tooltip.
- Permissions: read-only badge on the dashboard title; disabled "Edit".
- Long-running queries: progress with "Computing… 12s" and a cancel.

## 9. Ideation lenses that work for tools

From `ideation.md`, the lenses that produce good tool ideas: *the screen answers a question* (a
query bar as the hero), *time as the spine* (annotations, compare period), *texture as encoding*
(hatched sampled data), *remove the obvious component* (no north-star row; the saved grid is the
page), *sentences instead of widgets* (one insight line under the metrics), *make the empty state
the hero* (first-run). The lenses to avoid here: one object big, brand as character, invert one
surface, strip to numbers (analysts need the charts).

## 10. Tool-mode review rubric

Score these instead of the eight peak qualities:
1. **Grid discipline**: consistent card anatomy, aligned axes, deliberate 1x/2x sizing.
2. **Legibility at eight series**: palette holds, hover isolates, legend is chips with values.
3. **Chart correctness**: funnel/retention/paths drawn to §5; axes labelled; compare period dashed.
4. **Query transparency**: every insight's title says what it measures and over what period.
5. **Density without fatigue**: 12-13px, tabular, 36-40px rows, borders not shadows, white space
 between cards only.
6. **States**: loading, empty, error, stale, sampled, read-only all designed.
7. **Real data**: plausible event names, counts that add up, a cohort triangle that is actually
 triangular, dates in sequence.
8. **One accent, one primary**: "Add insight" or "Save" is the only filled button; selection uses the
 accent tint.
Ready when nothing is missing and at most one is weaker.
