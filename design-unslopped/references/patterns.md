# Pattern library: concrete anatomies

Each pattern gives the slots, in order, that the best references use. Numbers in brackets point to
`design-notes.md` entries with the evidence. Use these as starting anatomies, then adapt; do not
copy pixel values.

## Contents
1. Hero balance / headline metric
2. KPI tile and KPI strip
3. Quick actions
4. Transaction / activity row and grouped list
5. Data table (toolbar, header, row, footer)
6. Status chip vocabulary
7. Breakdown widget (segment bar + legend)
8. Chart card with selection callout
9. Limit / budget / goal progress
10. Transfer / payment form
11. Transaction detail and lifecycle timeline
12. Cards & accounts widgets
13. Choice screens (radio cards, method pickers)
14. Sidebar and header chrome
15. AI insight, recommendation and assistant surfaces
16. Mobile home screen
17. Mobile tab bar
18. Onboarding and steppers
19. Kanban and calendar
20. Landing page hero

---

## 1. Hero balance / headline metric  [004, 011, 020, 022, 046, 076, 093]
- Context control ABOVE the number: account selector pill ("Operational Account ▾"), currency tabs
  with flags, or a period picker. Switch first, then read.
- Eyebrow label in small grey: "Available Balance", "Total balance".
- The number: display size (32-56px desktop, 28-40px mobile), semibold. Decimals/pence smaller
  and lighter, or faded. Currency symbol same size as digits or slightly smaller.
- Privacy toggle (eye-off) inline right of the number on consumer banking.
- One delta chip + context ("↑ 10% from yesterday") or a secondary chip ("Available Limit •
  $3,600 Left ›").
- Optionally a thin histogram/sparkline under it; selected bar darker with a value callout.

## 2. KPI tile and KPI strip  [016, 027, 043, 052, 063, 066, 075, 085]
Single tile anatomy, top to bottom:
1. Title row: icon in a tinted circle or square (left or right), label, optional (i) or kebab.
2. Number (24-32px) with delta chip beside it (tinted green/red, tiny arrow, "+12%").
3. Context line in grey: "vs. 14,653 last period" / "Prev: $210,450" / "Target: 70%".
4. Optional micro-visual: sparkline, segmented bar, mini progress.

Strip variants:
- One connected card with 4-5 cells separated by hairlines (052, 075, 077) reads stronger than
  floating tiles.
- Highlight ONE tile by inverting it to the accent (045 Total Earnings) when there is a primary KPI.
- Pastel category tints per tile (082) only when tiles represent different categories and text
  stays dark.
- Numbers directly on the page surface, no cards, for airy wealth products (069, 093).

## 3. Quick actions  [004, 011, 020, 022, 038, 051, 085]
- 4-6 verbs: Add/Deposit, Send/Transfer, Request, Pay Bills, Convert, Scan/QR, Create Invoice.
- Mobile: equal square tiles or round icon buttons with the label below; monochrome icons.
- Desktop: a chip row in the header with the primary filled (051), or four bordered tiles in a card.
- When actions need explaining, use rows: icon, title, one-line description, chevron (085).
- "See All" link at the row end if there are more.

## 4. Transaction / activity row and grouped list  [004, 012, 017, 047, 055, 066, 068]
Row slots left to right:
1. Leading: merchant logo, avatar, or direction glyph (↙ in / ↗ out) in a 36-40px circle.
2. Primary: merchant/person name. Secondary (grey, 12px): category • time, or "Transfer to…".
3. Middle metadata (desktop only): method chip (ACH / Card / Swap), masked card "•••• 4329",
   category chip.
4. Amount right-aligned, signed, tabular; positive green, negative default or red for failed.
   Converted amount or running balance under it in grey (020).
5. Status chip (word + glyph, tinted) and/or kebab / chevron.

List rules: day headers ("Today", "Yesterday", "Mar 4") optionally with a count and subtotal; 56-64px
rows mobile, 44-52px desktop; hairline separators; "View all" link in the card header.

## 5. Data table  [029, 036, 048, 055, 057, 065]
- Toolbar: title left; search field, filter chips with icons ("Processed Date", "All Category ▾"),
  "Filter", "Export" (outlined) right. Tabs above the table for state (All / Unpaid / Paid).
- Header: 12px grey, sortable columns show ⇅, subtle vertical dividers optional, checkbox column
  when bulk actions exist.
- Row: 44-48px, hairline separators, no zebra. Text 13-14px. ID columns in a mono-ish or tabular
  style. Date + time stacked in one cell when both matter.
- Row actions: kebab or two icons (edit, print) at the far right, muted until hover.
- Footer: "Showing 1 to 20 of 20 entries" or "Page 2 of 16" left; numbered pagination with « ‹ › »
  centre; "7 / page ▾" right.
- Selected row: tinted background (045).

## 6. Status chip vocabulary  [005, 045, 055, 068, 092]
Define once, reuse everywhere. Tint background (10-15% of the hue), coloured text, optional glyph:
- Completed / Success / Paid / Active: green, ✓
- Pending / Processing / In progress / Scheduled: amber or blue, ⏱ or ●
- Failed / Overdue / Cancelled / Declined: red, ✕
- Not due yet / Draft / Archived / Inactive: grey
- New: blue; Paused: purple; Due soon: amber
Lighter alternative for dense tables: coloured dot + word, no background (045, 085).
Never a filled saturated chip in a table row; reserve fills for a single urgent banner.

## 7. Breakdown widget  [029, 047, 052, 056, 081]
1. Title + optional period picker.
2. Total (24-28px) with a delta chip.
3. One horizontal segment bar, segments in the data palette (one hue in tints is fine).
4. Legend rows: coloured dot or pill, label, amount right-aligned, "(24%)" in grey.
5. Optional total footer row ("Total Expenses $128.4K").
Use a treemap instead when there are 4+ categories and proportion matters (023). Use a small donut
only with external labels and counts (052, 080).

## 8. Chart card with selection callout  [027, 033, 047, 048, 054, 063, 076]
- Header: title, optional (i); right: period segmented (Weekly / Monthly / Yearly) or "This Month ▾",
  and chart-type toggles if offered.
- Legend: dots + labels; make items toggleable when there are 2+ series (036).
- Body: 3-5 gridlines, y labels left (right for finance price charts), x labels under.
- Selection: the hovered/selected bar or point is the only saturated element; others muted or
  hatched. Callout pill or dark tooltip with date, value(s), delta.
- Dual series: current solid, previous grey or dashed (080, 081). Projection: dashed or hatched.
- Footer: optional one-sentence insight.

## 9. Limit / budget / goal progress  [031, 051, 068, 084]
- Label ("Credit limit", "Monthly spending limit", "Daily Limit").
- Bar: track grey, fill accent; value pill on the fill when space allows ("72%").
- Ends: "$7,189 / $10,000" or "$2,500.00 spent of $20,000.00", percent right.
- Optional date range under it ("From Sep 20 to Oct 2026").
Goal copy next to the number is encouraged: "You're on track to hit your 70k customer goal" (081),
"You're close to A- just 1 thing left" (023).

## 10. Transfer / payment form  [040, 055, 068, 084]
1. Recipient: avatar row of recents (selected ringed) or a recipient row with "Change".
2. Source: card/account selector dropdown showing brand + masked number.
3. Amount: large input, currency selector inline; helper line "Available to send: $62,690.67".
4. Meta block (label left grey, value right): exchange rate, fee ("$0.00 (free transfer)"),
   balance after transfer. Note field optional.
5. One primary button ("Send", "Transfer"), secondary text link ("Make scheduled").
Currency exchange variant: two stacked fields "You send / You receive" with available balances
right-aligned and a swap button on the seam; rate and fee rows; one CTA (035, 041, 092).

## 11. Transaction detail and lifecycle  [017]
- Header card: status pill ("● Completed") + "Cleared Jun 4 · 09:42 AM EST"; big signed amount;
  from/to line.
- Three equal actions: Receipt (filled), Share, Report (outlined).
- Timeline: vertical stepper with green checks and a connecting line: Sent → Processing → Cleared,
  each with timestamp and one-line description.
- Breakdown: Gross / Fee / Net (bold, green) rows; Method details (method, originating bank,
  reference, transaction ID with copy); Tax & accounting with inline-editable fields; Related
  payments list.

## 12. Cards & accounts widgets  [004, 027, 031, 051, 072, 073, 083]
- Card art: flat (072) or a restrained 3D render (027, 073); never tilted. Shows brand, masked
  number, holder, expiry; an "Active" chip if multiple.
- Below the card: 3-4 square outlined actions (Top Up / Transfer / Request / History).
- Card stack: coloured edges peeking above the active card with a "4 cards" chip (051, 071).
- Accounts sheet / list: icon, name, masked number, balance; "+ Add Account" last (011).
- Sensitive details as a key-value list with copy icons; CVV hidden by default (004).

## 13. Choice screens  [013, 038, 072]
- Radio cards: icon, title, one-line description, chevron or radio; stacked full-width.
- Method pickers on mobile: stacked outlined pill buttons on an otherwise empty screen with one
  Cancel (013).
- Segmented controls for 2-4 mutually exclusive views; pill tabs for 4-7.

## 14. Sidebar and header chrome  [027, 047, 057, 063, 080, 085]
Sidebar (240-260px): logo + workspace switcher; search with ⌘K; groups with small-caps labels; items
28-36px with icon + label; active item filled (black, accent, or tint); counts as small grey numbers
or one tinted badge; nested items indented with a guide line; promo/plan card; user card.
Icon rail (56-72px) when destinations ≤ 8: round or square icons, active one filled, tooltips.
Header: title or greeting + helper sentence left; period/date range chips, "Add widget", one
outlined + one filled action right; bell with dot, avatar with role. Data freshness chip when data
is not live.

## 15. AI surfaces  [032, 042, 054, 058, 060, 063, 075, 089]
- Entry: header button with ✦ ("Ask Finexa", "Get AI Insight") or a right-rail panel.
- Insight card: one sentence with a specific number; optional dots pagination; optional ↗.
- Recommendation card (best anatomy, 075): severity chip + timestamp → title → problem sentence →
  tinted "Recommendation & Impact" block with bullets and quantified impact → one action button.
  Confidence shown as a % chip or a banner.
- Assistant panel: short AI summary paragraph, 2-3 mini stat tiles with status chips, an input
  with placeholder and send; model picker chips if relevant.
- Chat home: logo, two-line headline (two weights), 3 suggestion chips with icons, wide input with
  "/ for commands", tools row, disclaimer line (089, 018).
- Label every AI output ("AI Summary", "AI forecast:", "Warning:") so users know its source.

## 16. Mobile home screen  [002, 003, 004, 011, 012, 020, 022]
Top to bottom: avatar + greeting (or account selector) + bell; hero balance block (dark or tinted
region on banking apps); 4 quick actions; one status/alert row if anything needs attention ("2 claims
in progress ›"); recent list with day headers; tab bar. The dark-header/light-list split (004) is a
strong banking mental model: state above, activity below.

## 17. Mobile tab bar  [003, 008, 014, 017, 020, 022]
- 4-5 items. Floating pill bar or flush bar.
- Active item: icon + label in a pill or a filled circle; inactive: icon only (003, 008) or
  icon + small label (012, 020).
- Centre primary action (scan, +, AI) as a raised filled circle when the product has one dominant
  action (014, 017, 022).

## 18. Onboarding and steppers  [013, 015, 070]
- Progress as a thin segmented bar (015) or a numbered stepper in the toolbar with Back / Next (070).
- Onboarding headline may carry one typographic flourish (italic word); body copy plain.
- Chips as a word cloud for interests; one primary CTA + a text link ("I already have an account").

## 19. Kanban and calendar  [044, 079]
- Columns with pill headers; cards = avatar/initials chip, title, one meta line, a trailing icon that
  changes by column (⋯ / clock / check).
- Calendar: time rows left, day columns, "now" line, events coloured by team/category with avatars
  and counts; month grids show avatars on dates (016).

## 20. Landing page hero  [086, 087, 088, 091, 095, 096, 098, 099]
- Nav: logo, 4-6 items (dropdowns ok), one outlined + one filled CTA.
- Optional social proof line above the headline ("4.6 Google · 4.9 Trustpilot").
- Headline 2-3 lines, 48-72px; one flourish allowed (italic word, second line in the accent, serif).
- One-paragraph subhead, two buttons (filled + outlined).
- Hero visual: real product UI (screenshot, floating fragments, a diagram) rather than stock photo;
  a functional element (search box: 087) when the product is search-led.
- Logo strip "Trusted by…" below. Dark hero → light body → coloured closing CTA is a reliable rhythm.
