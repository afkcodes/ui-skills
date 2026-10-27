# Principles: what the good work has in common

Distilled from the 85 reference designs (see `design-notes.md` for the evidence behind each point).
These are the reasons a screen reads as considered rather than generated. Apply them as judgement,
not as a checklist to tick: a design can satisfy every line and still be dull, and the F1 concept
(010) or tubik's restaurant app (007) break several and are excellent because they break them
consistently.

## 1. One idea per screen, stated by the hierarchy

Every strong screen has a single thing it is "about", and you can tell what it is in under a second
because exactly one element is visually dominant. On a balance screen it is the balance (004, 011,
020, 022, 046). On a transaction detail it is the amount and status (017). On an analytics page it is
the hero KPI or the headline chart (030, 036, 081). Everything else is subordinate by size, weight,
or colour.

Test: squint. If two or more things compete, the hierarchy is unresolved. Fix it by demoting, not
by making the winner louder.

The screens that fail this (028) have four equally loud KPI tiles, a loud chart and a
loud table. Nothing leads.

## 2. Colour is a budget, and most of it goes unspent

Across the set, the designs that feel expensive use colour the same way:

- A neutral base (white, bone, warm grey, or a near-black like #141414 / #1c1c1e; never pure #000
 for surfaces, rarely pure #fff for cards on white).
- One brand accent, used for the primary action and the "selected" state and almost nothing else
 (003 terracotta, 029 acid lime, 037 red, 040 yellow, 045 lime, 072 yellow).
- Semantic green/red (and sometimes amber) reserved for meaning: positive/negative deltas,
 success/failed status, in/out money. Always as a tint or a small element, never as a card fill.
- Optionally a second or third categorical colour for data series, fixed across the whole product
 (030 orange + navy, 059 orange + violet + green, 069 one orange in three tints).

That is the whole palette. Six or seven values. Monochrome data palettes (one hue in three tints, as in
052, 069, 081) are the safest and still look rich because hatching, dots and weight do the second
encoding. When you want more categories than you have colours, use texture (hatching for
projected/inactive/other: 011, 059, 069), shape, or position before adding a hue.

The negative example is 028: rainbow gradients on every KPI tile, a different bright fill for every
chip, a three-colour donut. Structurally fine, visually meaningless because colour carries no
information.

Gradients are allowed, as one contained region: a header band (076), one hero card (083, 012), one
promo tile, a glow anchored to a single edge (012, 025). Never a page wash, never on
data.

## 3. Numbers are typography

Finance and analytics screens are mostly numbers, and the good ones treat digits as the display type:

- The hero figure is large; its unit, currency code or decimals are smaller and lighter
 (001 "17.0 tCO2e", 011 "£24,769.42", 015 "83 %", 076 "$12,680.42" with faded decimals, 010
 "1:12.171" with grey hundredths). The eye lands on the integer.
- Deltas sit beside the number as a small tinted chip or a tiny arrow and text, never as a second
 big number (every dashboard from 027 to 083).
- Context lines under the number say what it is compared to: "vs last month", "Since Last Week",
 "Prev: $210,450" (063 shows the previous value, which is clearer than a percentage for money),
 "Target: 70%" (075).
- Tabular figures in tables so columns align. Right-align amounts.
- A serif for headings or numerals is the recurring cue for "premium bank / wealth" (017, 027,
 081, 099). Sans for everything else. One flourish, used consistently.

## 4. Status is text first, colour second

Status chips appear in nearly every list. The ones that scan fastest carry a word and a glyph with a
tint behind them, not a coloured dot alone: "✓ Completed" teal, "✕ Failed" red, "⏱ Pending" amber
(068, 092). Where space is tight, a dot plus a word (045) is lighter than a chip and still
reads. Define the whole status vocabulary once (005 shows New / Active / Paused / Completed / Due
Soon / Overdue / Cancelled as a set) and reuse it everywhere. Use tints, not fills: filled status
chips (068) shout in a dense table.

The same goes for direction of money: a sign and colour (+$1,200.00 green / -$55.00 black or red)
plus a word where ambiguity is possible ("Received", "Withdrawn", "Refund").

## 5. Group, label, and give every row the same anatomy

Lists and tables are where generic designs fall apart. The references that work:

- Group by time with day headers and, when it helps, a day subtotal ("Today · 4 transactions ·
 −$100.01": 004, 017, 068).
- Each row has fixed slots: leading glyph or avatar → primary text + grey secondary line → middle
 metadata (method chip, masked card, category) → right-aligned amount → status → actions. Once the
 slots are fixed, 50 rows read as one object.
- Label-over-value cells (072) or a two-line "id / amount" cell let a list carry more columns
 without a header row.
- Tables have sortable headers (⇅), a toolbar (search, filter chips, export), and a footer with
 "Page 2 of 16", numbered pagination, and "7 / page". Row height 40-48px, hairline
 separators, no zebra striping.
- Key-value panels (017 breakdown, 004 card details) use label left in grey,
 value right in black, grouped by hairlines, with inline editable values where editing is allowed.

## 6. Forms tell you what will happen before you submit

The payment and transfer forms in the set are small and all do the same four things (040, 068): amount field with the currency, recipient or account with a way to change it, a helper line
with the available balance or limit ("Available to send: $62,690.67"), and a meta block before the
button: exchange rate, fee ("$0.00 (free transfer)"), balance after. Then one primary button.

Confirmation flows show a timeline (Sent → Processing → Cleared with timestamps: 017) rather than a
single status. Choice screens use radio cards with a title and a one-line description (072),
not bare radio buttons. Multi-step flows put the stepper in the toolbar (070) or as a thin
segmented progress bar (015), not as dots.

## 7. Actions: verbs, few, one primary

Quick actions are four to six verbs (Add, Send, Convert, Request, Pay Bills, Scan) as equal tiles or
a chip row, icon above or beside a short label (004, 011, 020, 022). One of them, or a separate
header button, is filled with the accent; the rest are outlined or ghost. The failure mode is three
filled primaries side by side.

Primary / secondary pairs are filled + outlined (023, 045, 091, 095). On a coloured surface the pair
is filled-white + ghost (003). Destructive or urgent actions get a reserved colour and position
(006 full-width red emergency bar).

AI entry points are a header button with a sparkle glyph (075) or a right-rail panel
(042, 054), never a floating bubble over the content.

## 8. Charts earn their place or they go

The honest charts in the set share habits:

- A selected point or bar is highlighted and labelled with a value callout; everything else is
 muted (007, 027, 054, 076). The chart answers "what is this number" on hover.
- Legends double as controls (checkbox legend in 036) or scorecards (accuracy stats in 033), or
 are replaced by direct labels at line ends.
- Axes are minimal: a few gridlines, labels at the edge, dual axes labelled both sides when there
 are two units (063).
- A one-sentence insight sits under or beside the chart ("Most expenses come from Activity and
 Meals": 054).
- Breakdown widgets are a segment bar plus legend rows with amounts and percentages (029,
 052, 081), not a donut, unless the donut is small and labelled externally (052).
- Area composition with more than four parts is a treemap (023), not a pie.
- Unusual forms (Sankey 037, activity grid 037, hexagon heatmap 069, cohort dots 030, capsule bars
 054/059, dot-matrix bars 040, diverging in/out bars 049) are used because the data has that
 shape, and each is used once.

Remove any chart that restates a number already on screen (the three-slice pie in 001). Keep
legends to five items or fewer; past that, split the chart or move encodings to a footnote. Never
draw a reading as a control (a slider handle for "7 s typical"): readings are dots, bars or figures.

## 9. Chrome is quiet so content isn't

Sidebars: grouped with small-caps section labels (MAIN MENU / TOOLS / ACCOUNT), the active item the
only filled element, counts as small grey numbers or a single tinted badge, a plan or promo card at
the bottom, user card last (027, 057). Icon rails (050, 054) when the
product has fewer than eight destinations. Top pill navs (045) for consumer-facing
products.

Headers carry: page title or greeting, a helper sentence, a period picker ("Last 30 days ▾"), a
date range, and one or two actions (Export, Create). Data freshness is stated in the chrome
("Last update: 3 min ago", "Last updated: Feb 28, 2024 ⟳": 036, 052). Workspace or account
switchers sit under the logo (030, 057, 063).

Cards: 1px borders in a slightly darker neutral or a very soft shadow, 12-16px radius, consistent
padding (16-24px), a title row with an optional kebab or period picker on the right. On dark
surfaces, cards are a lighter value, not a border (006, 009, 054, 060).

## 10. Decoration has a domain budget

Wellness (024), smart home (006), sport (010), food (014) and brand-led apps (007) can spend on
renders, illustration, photography and glass. Banking, payments, insurance and enterprise tools
(011, 017, 027, 036, 046, 057) spend almost nothing, and the result is trust. Mockups of hands,
tilted devices and ambient backgrounds are presentation, not product; never design for them.

When you do decorate: confine it to one region behind the data layer (033's fluid art behind a dark
card, 050's map), make it relevant to the domain (015's wireframe car, 005's logo
construction grid), and keep it off anything that carries a number.

## 11. Density is a choice, made once

The set spans very airy (093 wealth dashboard: no cards, three numbers, one chart) to very dense
(036 logistics, 057 payments inbox). Both work because the density is uniform across the screen and
matched to the user's task: monitoring and operations want dense; wealth and consumer banking want
airy. Mixed density (a sparse hero over a cramped table) feels unresolved. Pick a row height, a
type scale (usually 12/13/14 for data, 16-20 for titles, one display size for the hero) and a card
padding, and hold them.

## 12. Copy is part of the layout

Greeting + helper sentence is the standard header for a logged-in home ("Good morning, Oripio.
Stay on top of your tasks, monitor progress, and track status." 045; also 049, 063, 072).
Card titles can be benefit sentences ("Forecast your end-of-month balance in seconds": 046).
Empty states, insights and AI output are plain sentences with a specific number ("Your Transaction
Volume has increased by 5% since last month"; "You saved €26 this week": 025).
Section eyebrows are small caps. Microcopy under inputs says what the input accepts. Typos (016
"Fry") are the fastest way to look generated: proofread.

## 13. Consistency beats taste

The strongest signal that a design is considered is that the same thing looks the same everywhere:
every KPI tile has the same anatomy (016, 027, 063), every status uses the same chip, every
chart highlights the selection the same way, every card has the same corner radius and padding.
Theming tests (identical widgets in two brand accents) prove the system. When
tempted to make one card special, make its content special, not its styling.
