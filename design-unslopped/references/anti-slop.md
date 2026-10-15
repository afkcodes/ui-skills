# Anti-slop: the tells, and what to do instead

"Slop" is the generic default: output that could be any product, made by nobody, for no one in
particular. These tells come from comparing the 100 kept references against the 77 rejected ones
and against template work like 028. Scan a design against this list before showing it.

## Tells that a design was generated rather than designed

| Tell | Why it reads as slop | Do instead |
|---|---|---|
| Rainbow KPI tiles, every card a different gradient (028) | Colour carries no meaning, so nothing stands out | Neutral tiles; one accent; green/red only for deltas |
| Three or more filled primary buttons in one row (065) | No decision about what the user should do | One filled primary; others outlined/ghost |
| Donut chart with 5+ slices and a floating legend | Proportions unreadable; legend hunting | Segment bar + legend rows with amounts; treemap for 4+ |
| Chart that restates a number already visible (001's pie) | Double-encoding wastes attention | Delete it or replace with the breakdown list |
| Pure #000 background with pure #fff cards | Harsh, flat, no depth | #141414-#1c1c1e base, cards one step lighter, 1px borders |
| Glassmorphism everywhere, blur on every card (044) | Low contrast, trendy, dates fast | Blur for one overlay (modal, sheet); solid cards otherwise |
| Gradient page background with gradient cards on top | Nothing is a surface; data floats | Gradient confined to one band or one hero card |
| Hand-holding-phone, tilted device, ambient 3D scene | Presentation, not product | Flat, full-frame screens; the UI is the hero |
| Generic greeting with no helper line ("Welcome back!") | Filler; says nothing | Greeting + one sentence that states what the page is for |
| Lorem ipsum, "Lorem" in production copy (094) | Unfinished | Write the real sentence; if unknown, write a plausible specific one |
| Typos in labels ("Fry", "Withers", "This Munt", "Succes") | Nobody proofread | Proofread every label; spell-check the export |
| Icons from three different sets, mixed stroke widths | No system | One icon family, one stroke weight, one optical size |
| Mixed corner radii (4px buttons, 24px cards, 12px inputs) | Inconsistency reads as carelessness | One radius scale: e.g. 8 / 12 / 16, applied by element class |
| Status shown by colour only (a red dot) | Colour-blind users and scanners lose it | Word + glyph + tint |
| Numbers with inconsistent decimals ("$5,200" next to "$3,750.90") | Looks unedited | Same precision per context; faded decimals if you keep them |
| Every card the same height regardless of content, with empty space | Layout imposed, not fitted | Let cards size to content; align tops, not bottoms |
| "AI" badge or sparkle on something that isn't AI | Trend-chasing | Label AI output honestly; otherwise don't badge it |
| Dashboard with 8+ widgets and no primary | No hierarchy | Choose one hero (balance, headline chart); demote the rest |
| Sidebar with 20 flat items (028) | No grouping, no priority | Groups with small-caps labels; promote 5-7, collapse the rest |
| Mobile screen that is one big illustration and a button | Empty UI; the design is the illustration | Put the product's real first task on screen |
| Centered everything on desktop | Reads as a slide, not a tool | Left-align content; centre only hero headlines on marketing pages |
| Placeholder avatars and "John Doe" in every row | Unconvincing | Varied, plausible names and real-looking merchants/logos |

## The generated-UI typographic signature

Thin display serif (Instrument Serif, Playfair) at 60px+; a greyed currency symbol; an italic word in
a product headline; Plus Jakarta paired with a serif; lilac/mint/peach pastels; four equal display
numbers in a row; pill radii on everything; a bento grid with icons; glass on every card. The full
list with the evidence is in `typography.md`. Any of these is allowed only when two of the three
references chosen for the brief do it, cited by number.

## Structural tells (harder to see, more damaging)

- **No empty, loading, or error state considered.** A design that only shows the happy path with
  perfect data has not been thought through. Sketch at least: empty list, zero balance, failed
  payment, no network.
- **Actions without consequences stated.** A "Send" button with no fee, rate, or balance-after
  line. See `patterns.md` §10.
- **Status without time.** "Pending" with no "since" or "expected by". Add a timestamp or a
  relative time ("in 1 week": 054).
- **Tables without sort, filter, or pagination.** A static list of 8 rows pretends to be a table.
  Either make it a list card with "View all", or give it the full toolbar + footer.
- **Numbers without comparison.** A KPI with no delta, previous value, or target is a label, not a
  metric.
- **Identical structure for different content.** Every card is title + number + chart even when the
  content is a list, a form, or a sentence. Let the content choose the component.
- **Density mismatch.** Hero at 10% density, table at 90%. Choose one and hold it.
- **Same card six times.** Below the hero, every card has the same anatomy and height, and a trick
  that worked once (a sentence title, a sparkline) is repeated until it is wallpaper. Vary height,
  device and density; compress the third and fourth cards.
- **Saying it twice.** An alert card that repeats a row further down ("Gym+ renews tomorrow" as a
  banner and again in the subscriptions list). One of them goes.
- **Quick-action tiles next to a FAB.** If a floating + already owns the primary verb, four identical
  outlined tiles underneath the hero are filler. Keep the one or two verbs that matter as a chip row,
  or drop them.
- **A reading drawn as a control.** A slider handle, a toggle, a knob used to *show* a value implies
  the user can change it. Readings are dots on a track, bars, or figures; controls are for input.
- **Legend over five items.** The chart is carrying too many encodings to be read at a glance. Keep
  the two or three the eye needs; explain the rest in a footnote ("Faded = in progress") or the
  methodology block, or split the chart.
- **Secondary chart squeezed under the primary.** When two charts share an axis, the second is often
  left 60-80px tall and its slices unreadable. Give it at least 40% of the height, or simplify its
  encoding to what fits.
- **Unbalanced short numbers.** "7 s typical" at display size next to "10.5 min": a one-digit figure
  with a trailing unit and word looks broken. Set number + unit together at display size, the
  qualifier on the line below, same anatomy as its neighbours.
- **A headline that promises what the hero doesn't deliver.** A two-sentence headline whose second
  sentence is answered only below the fold needs a link or a second beat; otherwise cut it.
- **Signs that read backwards.** "↑ $4/day vs plan" (up = good or bad?); "You owe −$38" (the label
  already carries the sign). Write the comparison in words and let the label carry the sign.

## What "unslopped" does NOT mean

- It does not mean minimal. tubik's restaurant app (007) is loud, saturated and illustrated, and it
  is excellent because every element follows the same loud rules.
- It does not mean no decoration. Decoration is fine in one region, behind the data, relevant to
  the domain, within the domain's budget (`principles.md` §10).
- It does not mean no trends. Serif numerals, capsule bars, pill navs are all current and all appear
  in good work. The problem is adopting a trend without deciding why.
- It does not mean no colour. It means colour spent on meaning.

The underlying test is intent: for every visible choice, could you say in one sentence why it is
that way and not another? If the answer is "it's the default" or "it looked nice", change it or
own it.
