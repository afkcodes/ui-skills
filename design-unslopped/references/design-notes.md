# Design notes: 187 reviewed references

One entry per reference image in `../../reference/`. Numbers are fixed: where a reference was later cut,
its number is a gap and its file is in `reference/_rejected/`. `../assets/previews/map.txt` maps each
number to its file. Each entry records what the design does, what it teaches, and where it is weak.
These are observations, not rules; the rules distilled from them live in `principles.md`, `patterns/`,
`languages/`, `anti-slop.md`, `platforms.md` and `tools-and-analytics.md`.

Numbers 001-025 are mobile apps. 027-083 are web-app dashboards (mostly banking, fintech, payments, SaaS).
086-100 are marketing sites and AI tool homes. 101-144 are analytics and tool dashboards (tool mode).
The design-language and pattern batch (collected 2026-10-27) follows in ranges, each with its own
section header: 145-156 platform-native, 170-182 public and enterprise systems, 195-209 aesthetic
movements, 230-242 applications and onboarding, 255-272 app chrome, 285-300 commerce and marketing,
310-324 content, social and AI. Negatives are marked "Kept as a NEGATIVE example" in their entry:
028, 133, 142, 148, 156, 182, 201, 208, 241, 242, 271, 272, 299, 300, 317, 319. The review record
for the batch (every candidate and why it was kept or rejected) is in `reference/_reviews/2026-10-27/`.

How to use this file: when a brief resembles one of these (a payments table, a balance card, a kanban, a
landing hero, a checkout, a settings page, an AI chat) read the matching entries for concrete anatomy
before designing. Search by keyword (e.g. "status chip", "treemap", "stepper", "helper text",
"Liquid Glass", "brutalism", "check your answers", "command palette").

## 001 Upstream GHG mobile (Ramotion) — mobile, sustainability data
- Hero number "17.0 tCO2e" set large, unit in lighter weight: number dominates, unit whispers. Same pattern in the side card: value bold, unit regular grey.
- Three-scope list uses a coloured dot + name + description + big value + "x% of total" + delta chip. Each row carries 5 data points but reads clean because hierarchy is strict (bold value, grey meta, tiny chip).
- Delta chips: pale green/red tint with tiny arrow; never saturated. Lesson: status colour as tint, not fill.
- Segmented control (Company / Globally / Supply chain) as pill tabs above the number: context switch lives above the data it changes.
- Weak: pie chart with 3 slices adds nothing the list doesn't already say. Lesson: don't double-encode.
## 002 Insurance app (Paperpillar) — mobile, insurance
- Home card uses warm gradient ONLY for the greeting/hero block; everything below is near-white. Gradient = one accent, not a wash.
- "You have 2 claims in progress" row with a numbered badge: unresolved items get a count badge + chevron, placed directly under the greeting. Status-first home.
- Services as a horizontally scrolling row of icon+label chips (Payment, Statement Download, Top-up...). Chips are small, same-weight, no colour: utilities shouldn't compete with status.
- Neumorphic soft shadows on cards and the floating FAB: subtle elevation, no hard borders. Feels tactile but risks low contrast; works here because background is almost white.
- Hospital list: thumbnail + category tag + name + distance. Category tag coloured by domain (primary care warm, dental pink, mental green). Semantic category colours are muted.
- Weak: e-Card gradient tile with a policy number set huge is decorative; policy numbers aren't scannable data.
## 003 AI fitness app (Paperpillar) — mobile, health
- One accent (terracotta) used for exactly: the coaching card, the ring, the progress icon. Everything else grey/white. Accent budget is tiny and therefore reads.
- Coaching card has two actions: ghost "Dismiss" and solid white "Set Routine" on the coloured card. Primary/secondary distinction on a coloured surface = filled-white vs outlined.
- Stat tiles: label small grey, number large, then a mini-visual (sparkline bars / route squiggle) below. Each tile is label → number → glyph, consistent.
- Activity ring is cropped off the edge of its card; intentional crop adds motion. Risky but works at this scale.
- Pill tab bar at bottom with the active tab expanded to show a label (Progress) while others are icons only. Smart: label only where needed.
- Large display headline "Let's start strong!" centred: emotional headline is allowed on a home screen when the data below is calm.
## 004 Fintech banking app (Conceptzilla) — mobile, banking
- Dark header region for balance + currency tabs (USD/EUR/AUD with flags), light region for transactions. Dark-to-light split = "account state" vs "activity log". Strong mental model.
- Currency tabs show both code and balance; active one underlined. Multi-currency as tabs, not a dropdown.
- Four quick actions (Add, Send, Convert, More) as equal square tiles with icon above label. Verbs, not nouns.
- Transactions grouped by day headers ("Today", "Yesterday"), each row: avatar/logo, title, subtitle (category), right-aligned amount + method. Currency conversion row shows result in green under amount. Secondary info below primary, always.
- Card screen: 3D card art, then balance, then a plain key-value list (Card number with copy icon, CVC, Expiry). Sensitive fields as plain monospaced-ish values with a copy affordance.
- Weak: tilted device mockup hides edges; shot is marketing. The UI itself is solid.
## 005 Upstream UI kit (Ramotion) — components, sustainability platform
- Status chip system shown explicitly: New (blue), Active (green), Paused (purple), Completed (green outline), Due Soon (amber), Overdue (red), Cancelled (grey). Each is tint background + dot/icon + label. Lesson: define the whole status vocabulary once, tinted not filled.
- Task card: title (2 lines max), status chip, assignee avatars, date range in a grey box on the right, comment count. Cards carry metadata in corners, body is text.
- Filter row: segmented control (two big options) above pill counts (Ongoing 16 / Inactive 0 ...). Counts in the pill, muted when zero.
- Logo construction grid shown: brand built on a geometric grid. Signals rigour.
- Scope emissions row: icon + label + sparkline + value + "% of total". Three identical cards side by side = instant comparison.
- Sunset illustration tile is pure mood; harmless in a kit, not in a product screen.
## 006 Sentry smart-home IoT (Phenomenon) — mobile, dark
- Dark UI where cards are slightly lighter charcoal, not borders. Elevation by value, not line.
- Room chips (Doorbell, Living room, Kitchen, Backyard) as scrolling pills; active one filled.
- Live camera tile with "● Live" badge top-right and controls (mic, expand) bottom-right inside the image. Overlays sit in corners.
- Emergency call is a full-width red-tinted bar with icon + label + chevrons: the one destructive/urgent action has a reserved colour and position.
- Device tiles: name, toggle (green when on), then 1-2 status lines with tiny icons (battery %, temperature). Toggle top-right is the control; the rest is state.
- Thermostat tile uses a tiny rainbow arc gauge — colour gradient encodes temperature, acceptable because it mirrors physical thermostats.
- Big dial with a lamp render: skeuomorphic hero on a secondary screen, fine for one "delight" moment. Floating pill nav with 3 icons, centre one raised.
## 007 Restaurant ops app (tubik) — mobile, bold/illustrated
- Deliberately loud: black device frames, saturated coral/yellow/periwinkle blocks, hand illustrations, uppercase condensed headings. This is a brand-led style; everything is consistent with it (chunky corners, 2px outlines, monospace-ish labels).
- Alert card "STABILIZING LABOR COST" with a countdown "Shift ends in 2:59:12": time-boxed alerts carry a live timer.
- Venue capacity: 7 circular day badges with % inside, then an area chart below with legend of locations. Days as circles is a compact weekly heatmap.
- Integrations as tilted "cards" (Quickbooks unconnected in red, Xero connected in yellow with check): connection state = colour + check.
- Revenue screen: two KPI cards stacked (gross revenue, AOV) each with delta chip, then bar chart with the selected bar highlighted and a value callout. Selected-bar callout pattern recurs across the set.
- Lesson: "unslopped" doesn't mean minimal. A strong, committed, consistent visual language is the opposite of slop. Slop is the generic default; this is a choice.
## 008 DocSpot doctor booking (Phenomenon) — mobile, healthcare
- Greeting + location picker (Paris, France ▾) top-left; location is a first-class control on a booking app.
- Specialty grid: 3x2 tiles with a small 3D organ icon + label. Icons are small (~24px) inside big tiles; tile is the tap target, icon is just a glyph.
- Appointment card: avatar + name + specialty + "Confirmed" green check, then date/time as two labelled key-values with icons. Confirmation state is explicit text + icon, not just colour.
- Calendar tile (Monday 21 Jan) in green next to a map thumbnail with doctor pins and ratings: the "next thing" gets the only coloured tile.
- Doctor profile: stat chips (2k patients, 7 years, 4.8 rating) as small cards; tabs (Services/Reviews/Education/Rewards) underlined; black full-width "Book Appointment" CTA pinned near the bottom.
- Pill tab bar: active item shows icon+label in a white pill, others icons only (same pattern as 003).
## 009 Hager smart control (Ramotion) — mobile, dark, industrial brand
- Near-monochrome dark UI; colour is reserved for device-type icons (orange shutter, yellow light, blue electricity, green %). Icon colour = category, nothing else is coloured.
- Home status as a single dropdown row ("Night mode" with moon icon). Global state at top, in one control.
- Device grid 2-col: name bold, room in grey small, icon bottom-right in a circle. Three pieces of info per tile, strict positions.
- Tabs "Favorite Actions | Kitchen | Living Room" with the active one in white and others in grey: no underline needed when contrast carries it.
- Presentation board uses lots of white space with sparse labels (Automation / Energy, Efficiency / Comfort) — editorial layout for a brand that sells precision.
## 010 Formula 1 concept (Nixtio) — mobile, dark, sport
- Full-bleed photography with a dark gradient scrim; text sits in the clear areas. Large display type "Formula 1" with thin weight = premium sport.
- Track map with driver position markers (P1..P5) placed on the circuit, red segments showing sector. Data mapped to a real shape, not a generic chart.
- Lap time "1:12.171" in a tabular/mono display with the hundredths in grey: digits are the hero, precision is secondary.
- Points screen: "11 PTS" huge with "PTS" in grey, then a tiny two-row table (Sprint / Race with P6 +3 PTC). Big-number + mini-breakdown pattern.
- Buttons are flat grey rectangles with white text — restraint inside a cinematic frame.
## 011 SME business banking home (Okanlawon) — mobile, banking, GBP
- Account selector pill ("Operational Account ▾") above the balance: switch context before you read the number.
- Balance "£24,769.42" with pence smaller: the classic big-integer/small-decimal.
- Four outlined square quick actions (Deposit, Send, Request, Get paid): icons in 1px-bordered squares, labels below. Monochrome, equal weight.
- Account Summary: paired bars per day (money in hatched, money out solid), legend below with totals and a "Net flow" figure. Hatching as a second encoding on a one-colour palette = accessible without a second hue.
- Accounts bottom sheet: icon + name + masked number + balance per account, "+ Add Account" at the end. Sheet has a grabber, an icon header and a close button.
- Blurred background screen behind the sheet keeps context. Lesson: modal = dim + blur, not opaque.
## 012 Digital wallet (Nixtio) — mobile, dark/orange
- Dark card with a burnt-orange glow at the bottom edge, matching the brand orange of the page. One gradient, anchored to one edge.
- "Spent €3,480.00" centred large, Mastercard logo + masked number under it. Card identity below the number.
- Shared-card avatars (+6) between "+" and edit buttons: who-has-access as an avatar stack.
- Transaction rows tinted by direction (red-brown for withdrawn, green for received), with a small status word + icon. Direction colour applied to the whole row tint, not just the number — bold but legible on dark.
- Pagination dots under the card carousel. Five-item bottom nav with labels.
## 013 DailyMe nutrition (Phenomenon) — mobile, onboarding + home
- Onboarding headline mixes weights/italic ("your days" in italic serif): one typographic flourish, then plain copy. Dashed-outline chips float as a word cloud.
- Home: single large circular score (83) inside a glassy sphere with a one-line prompt above ("Eat More Nutritional Food"). Score as a sphere = gamified feel.
- Weekday strip (M T W T F S S) as small circles, today filled.
- Day card: meals as rows (Breakfast (+2) with items list and a check; Lunch empty with +). Timeline tick (09:01) on the right.
- "Select a Method" screen: 4 outlined pill buttons stacked on a gradient background with a single round Cancel at the bottom. Choice screens can be nearly empty.
- Goal projection chart with "You are here" marker and a green wedge to "Your goal": motivational chart with annotations instead of axes.
## 014 Food tracking with AI scan (Nixtio) — mobile, warm neutral
- Calorie arc built from discrete rounded segments (filled peach / empty grey) rather than a smooth gauge — reads as "portions", more honest than a smooth %.
- Meal cards: thumbnail, name, time, big kcal number with "% of goal" in orange under it, then a 3-col macro table (Protein/Carbs/Fat with grams). Edit pencil bottom-right.
- Scan screen: callout pills with a leader line to the food item ("170 kkal") — AR-style labels.
- Category chips with small photo thumbnails inside rounded squares + label below. Photo-chips for food categories.
- Dark pill tab bar with the centre "scan" action as a filled orange circle: the primary action gets the only colour in the nav.
- Palette: cream background, dark charcoal for nav/CTA, one orange. Three colours total.
## 015 EvoCare car maintenance (Phenomenon) — mobile, automotive
- Vehicle header: brand logo + model name, "● Updated" green status right-aligned. Status words are tiny and green, never a banner.
- Big product render centred with pagination dots — the object you own is the hero image.
- Stat tiles 2-col: icon + label, large number with unit smaller ("83 %", "248 mi", "24.2 °C"); battery tile adds a segmented bar (green bars) with 0%/100% ends. Units are always attached but visually subordinate.
- Dark onboarding screen uses a wireframe car line-drawing as background texture: technical drawing as decoration fits the domain.
- Thin top progress bar segmented in three: onboarding step indicator as a progress bar, not dots.
## 016 Productivity calendar (Nixtio) — mobile + widgets
- Month grid with avatars on dates that have meetings; today in solid black circle. Avatars-on-dates is a dense but readable way to show "who" without opening the day.
- Today list: app logo + title + attendees + a solid black time pill on the right. Time as a pill makes scanning the column trivial.
- Widget cards: title, huge number, delta chip (green/red), a sub-line (+12 Meetings), and a thin gradient progress bar with a % on the right. Same anatomy on all four = a system.
- Performance chart: vertical thin bars under a smooth curve, coloured by band (green/amber/red legend "<500 ≈1k >2k"). Band colouring explained by a legend of thresholds — good.
- Weak: "Fry" typo; gradient bar charts in rainbow can become decorative. Keep.
## 017 Fintech transactions + detail (Designfuzz) — mobile, payments, serif accent
- Header on a deep-blue gradient with a serif display title "Transactions." (with full stop) and "47 transactions" as a small eyebrow above. Serif for headings + sans for data = editorial fintech.
- Four KPI tiles (Inflow +8,420 green, Outflow -3,710 red, Net flow, Pending) in translucent cards on the gradient: KPIs sit in the coloured header, lists live below in white.
- Filter chips row: "Last 30 days ▾ | All status ▾ | All methods ▾" — filters as dropdown-chips, first one filled to show it's active.
- Transaction row: icon (arrow direction), name, date + method tag (ACH/BTC/Swap as tiny grey chips), right: signed amount in green/black + status word in grey/blue. Method as a chip is a great pattern for payments.
- Detail screen: status pill "● Completed" + "Cleared Jun 4 · 09:42 AM EST" then big "+$1,200.00" then from-line. Three equal action buttons (Receipt filled black, Share, Report outlined).
- Timeline card: three steps with green checks and a connecting line (Sent / Processing / Cleared), each with timestamp and a one-line description. Payment lifecycle as a vertical stepper.
- Breakdown screen: label-value rows grouped (Gross, Fee, Net received bold green), then Method details, Tax & Accounting with inline editable fields (Service revenue ▾, + Add note). Related payments at the bottom. A full transaction detail IA worth copying for banking.
- FAB "+" in the centre of the tab bar, raised.
## 018 Niva AI family assistant (Behance) — mobile, AI chat
- Assistant home: eyebrow "HELLO JUAN!" + headline question, then suggestion chips, then a large text input with a mic button. Suggestions ABOVE the input, not below.
- One warm gradient blob behind the input; everything else bone-white. Decoration is confined to one region.
- Upcoming activities as cards with category tags (CHILDREN blue, PARENTS yellow): people-group tags coloured.
- Lesson: AI UIs should look like forms with suggestions, not chat bubbles, on the home screen.
## 019 Softphone (Behance) — mobile, VoIP analytics
- Semi-circular gauge with the total in the middle ("2,835 total min") and three small stat columns below with mini progress bars (inbound/outbound/unanswered). Gauge + legend-as-stats.
- Tabs as pills: active filled blue "Overview", others text. Section header "This month ▾" is itself a dropdown.
- Blue gradient lower panel for "Recent activities" with white cards: bottom sheet colour inversion to separate summary from list.
- Weak: tilted hero mockup; the UI is fine but the presentation hides it. Kept for the gauge+stats pattern.
## 020 Fintech AI wallet (Behance) — mobile, dark/violet
- Violet gradient header block with greeting, "Available Balance" eyebrow, big balance with eye-off toggle (hide balance) — the privacy toggle sits beside the number.
- Four frosted-glass quick-action tiles on the gradient (Add/Send/Request/Scan), icon above label.
- "People" row of circular avatars + a violet "More" circle; Recent transactions with converted amount shown under the primary amount (e.g., +€240.00 / €8,240.90 EUR running balance). Running balance after each transaction is useful and rare.
- Floating pill tab bar with 5 round icon buttons, centre one filled violet (AI). Dark UI with one hue.
## 021 MediFlow (Arounda) — mobile, healthcare, warm grey
- Greeting as a two-tone headline (bold "Hi There!" + regular "How Are You Feeling Today?"): weight contrast inside one sentence.
- Next appointment card: title, duration chip in pale green ("45 min"), doctor avatar + name + role, time right-aligned. One card = one upcoming thing.
- Doctor cards with portrait photos, name/specialty, and a small lime-green arrow button on the active one. Lime as the single accent on a warm-grey base.
- Pill tab bar, 4 icons, active with a soft white pill. Very restrained; almost no colour.
## 022 Payno finance (Orbix) — mobile, banking, navy
- Balance card: eyebrow with icon ("Available Balance"), big navy number with eye toggle, then a small pill "Available Limit • $3,600 Left ›" — a secondary limit shown as a chip under the balance.
- Quick actions as round icon buttons with labels, "See All" link at the row end.
- Transactions: avatar + name + relative time ("Today, 5:32 PM"), amount right. Tab bar with a raised navy "+" FAB.
- Palette: navy + soft blue-grey, white cards. Calm banking.
## 023 Northpoint insurance (Behance) — mobile, treemap
- Coverage shown as a TREEMAP (Vehicle 42% blue, Protection 28% green, Healthcare 16% yellow, House 10% tan) with icons in tile corners. Proportional area for portfolio composition — far better than a donut for 4+ categories.
- Counter "17 Contracts / 4 Categories" with the small number as a subscript. Tabs (Contracts/Capital/Family) underlined, square corners everywhere, 1px borders: a deliberately Swiss, boxy system with no rounded corners.
- Dark green "Optimization score" card with a letter grade in a circle ("B+") and "You're close to A- just 1 things left" + "Missing: Vehicle". Gamified score with a concrete next step.
- Two side-by-side buttons: filled dark "Add Contract" + outlined "My Contracts". Primary/secondary pair.
- Lesson: squares and flat colour can be as premium as rounded glass; consistency matters more than style.
## 024 Luma wellness dashboard (Behance) — desktop, wellness, dark/light split
- Light top panel with a figure illustration and stat cards, dark bottom "Program" panel. Half-light/half-dark layout = overview vs. actions.
- Stat cards: label small, number big with unit smaller (23 min, 84/100, 86%, 58 bpm), each with a different micro-visual (bars, wave line, ring, watch image). Varied glyphs, identical card anatomy.
- Date strip with a stress reading callout ("Stress 78% 14:30") positioned over the day: annotation over a timeline.
- Pink "Inner Flow 34%" body-silhouette card and olive program cards with 2/5 progress: strongly art-directed, borderline decorative — fine for wellness, wrong for banking. Lesson: domain sets the decoration budget.
## 025 Cubee home energy (Behance) — mobile, dark green
- Headline metric "Saved this month €75" with a 3D device render below; stat tiles: ring gauge "82% powered by your solar today", "Producing 12.4 kW", "Saved today €2.50". Money + energy both as big-number tiles.
- Notification cards floating outside the phone show the system's voice: "Nice work! You saved €26 this week." Friendly, specific, numeric.
- Monochrome green palette (one hue, many shades) — a strong example of one-hue dark UI.
## 027 Bankio banking dashboard (Catalystco) — desktop, banking, forest green
- Classic 3-zone layout: sidebar (Main menu / Others groups, active item filled dark green) · main · right rail. Active nav item is the only filled element in the sidebar.
- Card Overview: physical card render + 4 stat tiles (Main Balance, Net Worth, Investment with a mini donut + legend). Each tile: eyebrow, big number, delta chip "from last month".
- Total Income / Total Expenses as two stacked tiles with ↑/↓ arrows, delta chips, and "Last Month" meta — identical anatomy, inverse semantics.
- Transfer table: Date & Time / Description (avatar + 2-line) / Account (masked) / Amount / ⋯. Row footer links "Repeat Transfer" and "View Full Transaction History ↗".
- Quick Transfer: 4 icon buttons (Bankio, Top Up, Pay Bills, Others) + recent avatars + one small black CTA. Spending Overview bar chart with the selected month in dark green and a value callout.
- Serif used only for section headings (Card Overview, Recent Transfer Activity): serif headings + sans body is a recurring "premium bank" cue.
## 028 Lector admin template (Rasel) — desktop, 2017-style template
- This is what slop looks like: rainbow gradients on four KPI tiles, saturated pink/purple/blue/orange, every status chip a different bright fill, donut with three loud colours, no grouping in a 20-item sidebar.
- Kept as a NEGATIVE example: nothing is wrong structurally (sidebar/table/charts) but colour is used as decoration not meaning, so nothing stands out. Lesson: if everything is accented, nothing is.
## 029 Qiespend fintech (Vektora) — desktop, dark + acid lime
- Dark charcoal with ONE acid accent (lime) for: selected bar, spending-limit segments, logo, upgrade badge. Rest is white/grey text.
- KPI tiles with a footer strip "⏱ Vs Last month" in a darker band — meta in a footer band, not inline.
- Spending limits as a segmented horizontal bar with a 4-item legend (Shopping 27%, Subscriptions 35%...): stacked bar + legend for category split.
- Transactions table: checkbox, Payment ID (mono-ish), amount with currency code, To (avatar + name), period, Payment Method as a filled grey chip, date. Column header row has subtle vertical dividers.
- Toolbar: search + two filter chips with icons + "More ▾" + export icon. Toolbars are flat chip rows.
## 030 MoonRow ticket analytics (One Week Wonders) — desktop, orange/navy
- Two-colour data palette (orange + navy + grey) across gauge, progress bars, area chart, cohort grid. Everything comparable because the palette is fixed.
- Gauge card "Today's Increase 571" with three product tiles under it (icon, name, count, coloured underline). 
- "Target Sales Breakdown": big number + three labelled progress bars (35.1% · 64.640 ticket) + area chart with a dark tooltip containing a mini stacked bar. Tooltip carries its own mini-chart.
- Country table with flags; retention cohort as a dot-matrix grid with a right-side % axis. Dense but all in one type size.
- Workspace switcher (Global Connect · 37 Members) under the logo: tenant context near the brand.
## 033 Borea AI stock prediction (Ramotion) — desktop, dark, data viz
- Stat strip at top: four label/value pairs in one translucent bar (Market Cap 735.75B · Day's Range 284-289 ...). Horizontal key stats row.
- Chart card header: toggle "Prediction", Day/Week segmented, calendar icon; legend right: solid orange "Actual", dashed blue "Borea AI Prediction", two accuracy stats. Legend doubles as a scorecard.
- Confidence band (blue area) around the actual line, dashed projection after "today" marker. Tooltip shows Prediction vs Actual High/Low/Close with a score. Range selector row 1D…Max as text tabs.
- Y-axis labels right-aligned on the right edge; current value marker "142" in an orange tag. Financial-chart conventions respected.
- Fluid red/blue background art is contained BEHIND a dark card so the data layer stays flat. Decoration behind, data in front.
- Disclaimer copy bottom-left in small grey: legal text present but quiet.
## 036 Sypher logistics ERP (Conceptzilla) — desktop, white, green/red/black data
- Horizontal top nav with the active tab underlined; a thin meta strip under it ("Changes: Last month ▾ · Last update: 3 min ago" / "Manage layout"). Data freshness stated in the chrome.
- KPI micro-visuals: fleet utilization as a bar strip, on-time rate as a gradient segmented bar, deliveries as a sparkline. Three KPIs, three different glyphs, one row.
- Revenue and costs multi-line (green revenue, red costs, black profit) with checkbox legend (toggle series) and a "Vs. previous period" switch. Legend items are controls.
- Invoices panel: 3 KPIs with % and a stacked progress bar; tabs All/Unpaid/Resent request/Paid; table with company logo, issue date (sortable), contact email, value; footer "Show by 10 ▾ · 1/4 ›". Compact, no chips, all text — density done right.
- Costs by category: stacked bar + legend with amounts and %. Text sizes stay small and uniform throughout — the restraint IS the design.
## 037 Vaulto (Orbix) — desktop, black + red
- Pure black with a soft radial light top-left; cards are #141414-ish. Red is the one accent (Add Funds button, highlighted bar, line tooltip). Everything else greyscale.
- Balance block with cash/crypto split, three outlined action pills (Add Funds filled red, Send, Convert).
- Asset tiles ETH/EURO/YEN with sparkline + delta; a dashed-border "Add another currency" tile as the 4th. Dashed empty-state tile = add affordance.
- Sankey (Total assets → currencies) and a GitHub-style activity grid for Net Cashflow; a 21-day number strip under the line chart. Unusual charts used appropriately.
- Vertical bars drawn as rounded capsule tracks with a filled portion — bar-as-progress.
## 040 Personal banking (Nixtio) — desktop, mint + yellow
- Mint background, yellow balance card (the only saturated element), white everything else. The hero number gets the one loud colour.
- Balance card with currency conversion hint (1 USD = EUR 0.95 = GBP 0.79) and an eye-off icon; three text-buttons under it (Pay/Transfer/Receive) separated by hairlines.
- Currency tiles (Euro 0.97 / British Pound 0.82 / Swiss Franc 1.10) with coloured glyph circles.
- Dot-matrix bar chart ("Total Rate") with the selected column in yellow and a yellow callout — bars drawn as dot columns is a distinctive but readable texture.
- Right panel = a transfer flow: card selector pill, recipient row with "Change", big amount, meta rows (exchange rate, balance after transfer, fee $0.00 (free transfer)), note field, 3x4 numeric keypad, black "Send". Keypad on desktop is odd but the meta-rows are exemplary.
## 042 Kanto client metrics (Gnyadek) — desktop, lavender, editorial
- Editorial header: small eyebrow "Unified Client Metrics" + huge display "All Client Data" left; a floating insight card right with a sentence in two weights ("This quarter, optimized workflows reduced manual checks by 27%"). Dashboard with a magazine headline.
- Date range as two date chips + "All Accounts ▾" right-aligned on the header row.
- Weekly stacked bars with a hover tooltip listing three categories with counts; "+31%" chip floating top-right of the chart.
- Three metric cards with a % and a status dot (green ✓, orange ✕), then a two-ended bar (Auto-cleared ↔ Under Review) with counts at both ends. Two-ended bar for a split.
- AI Assistant panel: chat with a file-upload bubble, model picker chips (GPT-5 / Docs AI / Finance AI), "+" and input with send. Assistant lives in the right column as a peer widget.
## 045 Finexy (Oripio) — desktop, white + lime green
- Greeting + one-line helper text ("Stay on top of your tasks, monitor progress, and track status.") under the title.
- Total Balance card: currency dropdown top-right (USD ▾ with flag), number, delta, two buttons (lime filled "Transfer", outlined "Request"), then a Wallets sub-section with 3 currency mini-cards (flag, code, amount, limit line, Active/Inactive status).
- 2x2 KPI tiles where ONE (Total Earnings) is filled green and the other three white — highlighting the primary KPI by inverting one tile.
- Profit and Loss as paired bars (lime vs black). Monthly spending limit progress. My Cards as two dark card renders with Active chips.
- Table: checkbox, Order ID, Activity (icon + name), Price, Status (coloured dot + word, no chip), Date, ⋯. Selected row has a tinted background. Status as dot+word is lighter than a chip and still scannable.
## 046 Bankora business banking (Lypovska) — desktop, black/white, Swiss
- Pure black-and-white with ONE amber chip ("3 days left"). Cards use small-caps eyebrows ("QUICK ACTIONS", "MAIN ACCOUNT BALANCE") and a sentence as the card title ("Manage your daily tasks in one click", "Remind, review, and get paid faster", "Forecast your end-of-month balance in seconds"). Card titles as benefit sentences — rare and good.
- Balance tile with a tall thin-bar histogram, expenses trend with hatched vs solid bars, outgoing payments as a segmented bar with a 3-row legend of % values.
- Black "Cash flow calculator" panel with two inputs (Weekly spending, Scheduled payments) and a "Calculate →" button: a calculator widget on the dashboard.
- Icon-only centre nav in the header (5 icons, active one black). Lesson: monochrome forces hierarchy through size, weight and black fills — and it works for banking.
## 049 Nueansa (Sogee) — desktop, warm white + orange, serif-ish numerals
- Greeting with date line; "Total Revenue $210,550" set extra large with digit spacing (", " spaced) — numerals as typography.
- Three KPI cards share one row: label, big number, "Growth Rate ↑ 4.1%" footer row. Footer-row for the delta (consistent with 029).
- Monthly Cash Flow as floating range bars (inflow above zero in orange, outflow below in black) with a dashed zero line and a tooltip listing both. Diverging bars for in/out.
- Financial card: "AI Finance Insight" header with a chat icon; ring gauge split orange/black with Available Balance centred; two mini stats under it with coloured left bars.
- Transaction History table: category as grey chips (Subscription / Revenue), amounts signed. My Card with "Primary Business Account" label. Export is the only filled orange button.
## 050 Quantix procurement (VALMAX) — desktop, grey + red + dark cards
- Mixed surfaces: light grey page, light-grey KPI cards, DARK cards for data-heavy tables/charts. Dark surfaces used to frame the dense parts.
- Overview tile: three numbers in a row with small deltas and labels beneath (13.7K Total orders / 98.6K Quantity / 312% ROI). Horizontal KPI triplet.
- Map with pin clusters and callouts ("217 Suppliers Germany"); Key Suppliers as four mini bars with % above and country below (Others hatched).
- Spend by Category table on dark: sortable headers (CATEGORY ⇅ SPEND ⇅…), a "proc. cycle" column with a tiny line + marker + "11 days" — micro-visual in a table cell.
- Chart-type toggle icons (bar / table) next to period tabs. Red "Upgrade" banner with a radial glow — promo kept to one strip.
- Round icon rail left with a round search button at top. Pill primary nav with the active tab filled red.
## 052 Alignify revenue analytics (Wolfpixel) — desktop, white + coral
- Five KPIs in one connected card divided by hairlines: icon, label, number; footer row with "↑ +3.5% vs last Year" in green/red. One card, five cells — stronger than five floating tiles.
- "Last updated: Feb 28, 2024 ⟳" chip in the header. Data freshness again.
- Cashflow line with a tooltip and a legend chip "■ Reimbursed $5,133"; "Time Interval: Monthly ▾".
- Revenue by Product Category: total, delta, a 3-segment bar, then legend rows (coloured pill, label, amount (%)). Segment bar + legend rows with amounts — the canonical breakdown widget.
- Donut with external leader-line labels; Sales Calendar with day tabs and meeting cards; horizontal bars with % right-aligned. Coral used in 3 tints (dark/mid/light) = monochrome data palette.
## 054 Financial analytics (Outcrowd) — desktop, DARK, blue accent, calendar
- Rounded-capsule bar chart: each month is a dark capsule track; the selected month filled blue with a "+12%" chip above and "$1048" inside. Capsule bars with in-bar value label.
- Period segmented (Weekly/Monthly/Yearly/Range) + a filter icon button. Calendar widget with today highlighted and a KPI "$1,434 ↑12.4%" beneath it.
- "How can I help you?" AI card: an "AI Summary" paragraph, two mini stat tiles with status chips (7 Stable, 25 Processed), and an "Ask me anything…" input. AI as summary + stats + prompt.
- Spending donut with legend; a one-sentence insight footer ("Most expenses come from Activity and Meals…"). Insight sentence under the chart = good practice.
- Invoices: "Payment Score" as a thin barcode-style meter with 76; rows with date + relative time ("in 1 week"), status chip, name, amount.
- Left icon rail with the active icon in a white rounded square. Dark grey (#1a1a1a) not pure black; borders are 1px lighter grey.
## 057 Payments inbox (Orbix) — desktop, white, dense table
- Workspace switcher (Agency / Orbix Studio Team) at the top of the sidebar; nav groups with nested sub-items under Payments (Requests, Recipients, Wire Drawdowns, ACH Authorizations); "Workflows" section. IA for business payments.
- Page header: title + helper, right: ghost "Send Money" + black "Upload Bill". Tabs Inbox / Needs Approval / Scheduled / Paid; a forwarding email chip ("jamiesmith@gmail.com") and settings gear on the tab row.
- Table: due date, status chip (Completed green / Overdue red / Not due yet grey), recipient with a card icon, amount, invoice no, last update (date + time stacked). Rows 44px, hairline separators, zero decoration. The purest "work table" in the set.
- Promo card bottom-left (GlobalLink) with one black CTA.
## 059 Leads overview (Outcrowd) — desktop, DARK, orange+violet+green
- Three-colour categorical palette (orange/violet/green) used consistently across capsule bars, donut, chips, and mini stat tiles. Capsules stacked = multi-series bars.
- Conversion card: three KPIs in a row with tiny ▲▼ triangles only (no chips), then an area chart with month pills under it (active month filled). Month selector as pills under the chart.
- Leads bars with hatched "potential" above solid "actual" (hatch for projection). Right card: donut with external % pills, three mini tiles with coloured left dots.
- Date chip "Jun. 6, 2026" repeated per card; platform picker "Meta ▾" top-right. Serif-ish condensed numerals set with letter spacing ("$ 33, 846") — stylised but legible.
## 060 Insighta analytics (Outcrowd) — desktop, DARK, violet
- Top nav as pills with icons (Overview active white). KPI tiles: icon + label, ↗ button, number, delta chip (green/red). Heatmap (hours × days) with a 3-step legend and a 3-segment "Day/Morning/Evening" bar beneath with %s.
- "AI-derived Comparison" card: two numbers (82 Engagement / 41 Satisfaction) with stacked bar glyphs (green vs orange) and a "Warning:" sentence. "AI forecast:" sentence under the heatmap. Every AI output is a labelled sentence.
- Line chart with a vertical highlight band and a value pill (101k) on the selected day; day numbers as the x-axis with the selected one in a pill.
- Violet "Insights" callout card with a highlighted figure inside the sentence ("Improve 32% in…") and a progress dots row. Donut with dotted leader legend; segmented arc "Quality Score 64%".
- Dark UI done right: #1c1c1e surfaces, 1px lighter borders, one hue + semantic green/red only.
## 063 Buildly growth analytics (Delisas) — desktop, DARK, orange
- Workspace dropdown "Growth Team" at top of sidebar; nav with count badges (Data Sources 12, Alerts 3). Header: search, orange "+ Add Data", bell with badge.
- Five KPI tiles: icon square top-left, delta chip top-right, label, number, "Prev: $210,450" grey. Prev-value instead of a % is clearer for finance.
- Dual-axis line chart (Revenue $ left, Conversion % right) with a legend below and range pills (24H/7D/30D/90D). Dual axes labelled on both sides.
- "Strategy Simulator" card with three sliders (Price Change, Ad Budget, Traffic Increase) and live values — what-if controls on a dashboard. "AI Recommendations" as three cards with a confidence % chip and an "Impact" line in green/red.
## 068 Cascade transactions (Outcrowd) — desktop widgets, white, blue/orange
- Quick Transfer widget: recipient avatars (selected name in blue), card selector dropdown, amount input with the recipient avatar inside the field and an "Available to send: $62,690.67" helper line, black "Transfer", text link "Make scheduled 📅". Form helper text under the amount is essential for payments.
- Recurring transactions: a 5x6 grid of checkboxes-as-calendar with a count "12 Recurring" and a list of subscriptions with date squares and frequency chips (Monthly/Yearly).
- Limits card: two horizontal progress bars (Credit limit 72% orange / Online limit 23% blue) with "$7,189 / $10,000" labels and card chips top-right. Limits as progress against a cap.
- Transaction history grouped by day with a day total ("- $100.01 · 2 transactions"), each row: logo, merchant + time, card brand + masked number, category chip, signed amount, status chip (Success green filled / Failed orange filled), expand chevron. Grouped lists with day subtotals.
## 069 Restro restaurant analytics (Sujon) — desktop, white + burnt orange
- Horizontal icon-only nav with the active one expanded to icon+label (same pattern as mobile pill bars). Date/time stamp top-right.
- Hero KPI row without cards: four big numbers with a small chip beside each ("$12,368 · 20 Closed", "45 · ☆ 4.8"). Numbers on the page surface, no tiles — airy.
- Reports: hatched area band chart (range) with dots and a two-row tooltip; Order Status as three wide rounded blocks (dark/mid/light orange) with a legend row of values. Customers as a hexagon-dot heatmap with a 3-tone legend. Occupation: hatched bars with the max solid + "80%" pill. Weekly Summary: solid line vs dashed line.
- Monochrome orange data palette with hatching as the second encoding. Very cohesive.
## 070 Synthex workflow builder (Nixtio) — desktop, white, node canvas
- Stepper in the header (① Build — ② Add Sender Profiles — ③ Add Contacts — ④ Launch) with "← Back" and black "Next step →". Wizard progress in the toolbar.
- Canvas toolbar: undo/redo, zoom "− 100% +", layout icons, "View Logs". Floating bottom tool palette (select, hand, settings, link, grid) with the active tool black.
- Nodes: icon + title + subtitle, "Draft" chip, a footer of tiny counters (⎘ 11 · ⬡ 27 · ♥ 41 · ⚡ 72). Edges labelled with pill labels on the line ("Initialize Data", "Execute Triggered"). Coloured edges by path.
- Right inspector: Real-time Metrics (two sparklines), Model Status, Environment dropdown, collapsible sections (+/−), read-only code block with copy, a slider with min/max, Dependency Tree with a mapping diagram, violet "Apply Normalization" CTA. Inspector = stack of collapsible labelled sections.
## 072 Multipliiier (ElevenSpace) — desktop, white + yellow
- Sidebar: active item is a yellow filled pill (the only yellow besides the + button and reward icon). Light/Dark toggle at the bottom of the sidebar as a segmented control.
- Balance with currency chips (US Dollar / EURO) and an outlined "↗ Withdraw". Quick actions as three tall tiles with a tinted icon square top-left and a label bottom-left. Contracts as logo tiles; "Create contract" as three radio rows with title + one-line description + chevron.
- Cards: two card designs side by side (white / pale green) with "Account number ****9934", cardholder, valid thru — flat card designs, not 3D.
- Recent transactions: each row has THREE labelled columns ("To Miriad systems / LogicBox", "Request date / 09/09/2026", "Status / Pending") — label-over-value cells make a list readable without a header row.
- Rewards: referral card with "Copy link". Search placeholder "Search anything or ask AI ⌘S".
## 075 Enrolliq edtech (Filllo) — desktop, white, AI-heavy
- Header: search ⌘K, "AI Brain" pill with gradient icon, theme toggle, refresh. Page actions: "Courses: All Courses ▾" combined chip + blue "Analyze My Courses".
- KPI strip as ONE card with four cells: eyebrow in small caps (AVG. COMPLETION RATE), number + chip, and a third line (Target: 70% / 27 haven't logged in for 7+ days). Three-line KPI with target context.
- "Needing action today · 5" with a confidence banner ("96% CONFIDENT based on 1500 previous sessions"); two alert cards: severity chip (Needs Attention amber / Critical red) + timestamp, title, problem sentence, a tinted "AI Recommendation & Impact" block with a bulleted suggestion + "Estimated recovery 18 students · +$5400 revenue increase", and an action button (Fix Automatically / Review Lesson). The best AI-recommendation card anatomy in the set: severity → problem → suggestion → impact → action.
- "Improved this week" as a numbered list with before/after chips (65% → 83%) and "See details" buttons. Performance line chart with three series; Students At-risk with a count + delta + ranked list.
## 076 Banking dashboard (Nixtio) — desktop, red→orange gradient header
- Full-bleed warm gradient header (deep red → orange) holding the greeting, two white pill actions (Deposit/Withdraw) and a glassy card stack with "$12,680.42" (decimals faded). Everything below the header is white cards. Gradient as a header band, not a page wash.
- Overview: thin-bar histogram (hundreds of bars) with a selected cluster darker and a black tooltip "$1,548.24 ↗2.46% for April 2026". Category tiles 2x2: name + tiny icon, amount with faded decimals, delta with ↗/↘ and "from last month". Faded decimals = recurring Nixtio signature.
- Pill nav centred in the header with the active tab in a translucent pill. Investment Performance as mini bars with a "1.5%" black pill.
## 081 Vanta business (Odama) — desktop, white, serif numerals, mountain backdrop
- Serif numerals for KPIs ("$284,892") with small 3D icons right; "Compared with Aug 01 – Aug 17, 2026" meta top-right. Serif numbers signal "finance/wealth".
- Revenue & Profit: three lines with a hover band and a 3-row tooltip; Cash Flow: barcode-style thin bars with the selected one black, Incoming green / Outgoing red, and a metric row beneath (Previous / Current). Revenue by Channel: labelled thin bars with amounts and %; Operating Expenses: stacked segment bar + legend rows + total footer.
- Customer Growth: number + delta + a "You're on track to hit your 70k customer goal" chip + weekly bars with Week 5 highlighted. Goal-tracking copy next to the number.
## 083 Personal finance banking (Nixtio) — desktop, red→orange gradient CARDS
- Variant of 076: the gradient is on two hero cards (Overview, Credit Cards) rather than the header, page is cream. Overview chart = thin-bar histogram with a white tooltip. Credit Cards: amount, delta chip, "Credit Limit: $1000.00" chip, two white pill buttons (Deposit/Withdraw) with a swap icon between, glass card stack.
- Black "Create Report" button top-right; categories 2x2 tiles; Recent Transactions rows with status chip + masked card + signed amount. Shows how one system flexes: gradient-as-header vs gradient-as-cards.
## 086 Sensia landing (One Week Wonders) — web, dark + acid lime, serif
- Landing page: hero with a cut-out athlete, serif headline with an italic word ("Move With *Meaning*"), a chat-style input with suggestion chips (Energize/Recover/Focus/Calm/Reset), partner logos row, acid-lime section, then dark sections with photo trios and product cards. Serif+italic headline, one acid accent, dark/lime alternation.
- Phone mock embedded mid-page shows a real app screen (score gauge 75, stats). Marketing pages should show real UI, not abstractions.
## 087 Borea AI landing (Ramotion) — web, dark, red→blue gradient frame
- Hero: three-line bold headline with a ghosted giant word behind, one-line subhead, a search field "Search stocks" + "Popular Stocks:" links. Search as the hero CTA for a data product.
- "Top Traded Stocks" as four logo tiles with ticker chips; the hovered tile fills blue. Single orange "Sign In/Up" button. Functional hero: the first thing you can DO is search.
## 088 Quantexa enterprise (Ramotion) — web, purple, B2B
- Header: logo, 5 dropdown nav items, search icon, lavender "Book a Demo". Hero: two-line headline, one paragraph, teal CTA; right: a product-UI illustration (table with masked rows, chips, icons) with connecting lines above it. Enterprise hero = abstracted screenshot, not a stock photo.
- Section tab bar under the hero (challenge / How We Solve It / Impact / Why Quantexa / Where we help / Contact) with an underline — in-page anchors as tabs.
## 089 Noera AI chat (Shakuro) — desktop app, white, minimal
- Empty-state chat: logo, two-line headline in two weights ("Built to think. / Designed to assist."), three suggestion chips with icons, then a wide input with "Type / for command", mic, blue send; secondary tools (attach, Tools, Search) under the input; disclaimer line. Chat home = headline + 3 suggestions + input + tools row + disclaimer.
- Sidebar: Chats 14, New chat (⌘N), Search in chats (⌘K), Discover; Today/Yesterday/Earlier groups; Settings / Help center 3; user card. Shortcuts shown inline in grey.
## 090 Horizon Estate (Shakuro) — web, white, real estate
- Hero: giant two-line headline left, a short paragraph right, small black "Book a call"; a full-width house render below. Then "We help you find…" + a search panel: tabs (Buy / Rent / New developments / Commercial) + four dropdowns + "More options", "Clear filters", black "Show properties". Search panel as tabs + dropdown row + two actions.
- Property cards: photo, name + price, location, four spec chips (400 m², 2 floors, 6 beds, 2 baths). Agent cards with portrait. Typography: one grotesk, two sizes, black buttons — very restrained.
## 091 Nexori fintech landing (Outcrowd) — web, white, globe hero
- Centred two-line headline, one-line subhead, two buttons (black filled "Begin building" + outlined "Contact a team"). Floating UI fragments (notification list, KPI card, mini chart) orbiting a globe render — product-UI as hero imagery; partner logo strip in a rounded panel. Clean B2B fintech landing formula.
## 092 Crypto income (Odama-like) — desktop, DARK, lilac + yellow
- Three KPI tiles each with a category chip top-right (Cashout / Fees / Activity) on three different fills (lilac / yellow / grey). Tile fill = category; chip repeats the category in words.
- Weekday bars drawn as thin stems with a dot, the selected day as a thick gradient capsule + value pill; day letters as circles, selected one yellow. "+2.6%" set huge with a 2-line explanation ("This week's income is higher than last week's"). Big delta + plain-English meaning.
- Watchlist rows expandable (BTC expanded shows volume/cap/dominance); trading table with status chips (outlined ✓ Completed / outlined ⏱ Pending). Exchange panel in a white card on the dark page — the one inverted card = the primary action.
## 093 Portal crypto tax (Phenomenon) — laptop, white + green
- Very sparse dashboard: title, segmented Portfolio/NFT, three headline numbers in a row (Total Value / Cost Basic / Unrealized Gain with deltas), a tall green area chart, then a "KPI" row of four numbers with icons. No cards at all — hairline dividers only. Numbers on the page surface for a wealth product.
- Deltas as tiny green/red text next to numbers, no chips. Pastel gradient area fill. Minimal chrome, maximum quiet.
## 094 Next World VR (Outcrowd) — web, white + orange, B2B
- Hero: photo with a dark gradient scrim, two-line headline, 3-line description, two small buttons (orange filled / grey). Nav as grey pill groups. "I Want To:" section with tab-like links and a 01/05 carousel of cards. Giant "Subscription Plans" display heading. Card tiles with product renders and small charts. Section eyebrows in small caps (SOLUTIONS / SERVICES).
## 095 ZeBeyond engineering SaaS (Phenomenon) — web, DARK green, tablet + phone
- Hero: two-line headline with the second line in mint, subhead, mint filled "Contact us" + outlined "View demo". Right: an isometric process diagram (Market study → Concept exploration → System spec → Component spec) with the active step highlighted mint. Diagram-as-hero for a technical product.
- Six industry tiles with isometric icons (Automotive, Off-Highway, Defense…). Phone view: Case studies with filter chips ("Automotive ✕", "CV ✕", "Clear all") and case cards with category chips. Responsive pairing shown.
## 096 Deflexai (Orix) — web, white, SaaS landing
- Social proof above the headline ("4.6 Google · 4.9 Trustpilot"), two-line headline, two-line subhead, black "Get started free" + outlined "Talk to sales team". Floating notification cards (activity feed) as the hero visual; integration logos on concentric orbits; "Trusted by 200,000+ users" + logo row. The modern SaaS landing template — competent, low on surprise.
## 097 Landscaping landing (Behance, RU) — web, cream + green
- Long-scroll landing: hero photo card with an overlaid headline + green CTA, team photo sections, four service tiles with photos, a services price list with chip filters. Consistent green accent, serif-free, generous photo use. Lesson: local-market landing pages still follow the same structure; photography carries trust.
## 098 Lyra AI (Behance) — web, DARK indigo → white sections
- Dark hero with a chip eyebrow ("Next Generation AI Platform"), two-line headline with the second line in lavender, subhead, two buttons, three feature columns with icons, then a product screenshot in a browser frame. Light sections below with feature cards (each containing a mini-UI), "Get Started in Just Three Simple Steps" with three screenshot cards, then a blue gradient closing section. Dark hero → light body → coloured footer CTA.
## 099 HomeVision underwriting (Behance) — web, serif headline, meadow backdrop
- Huge serif two-line headline ("One platform for all your underwriting needs"), two-line subhead, dark "Request a demo" + light "Learn more" (both with a tiny dot prefix), then a product screenshot (Workflows canvas with nodes). Serif display + sans body + real product UI = credible fintech B2B.
## 100 Butter (Awwwards) — web, grey, product hero
- Minimal: nav pill left, Login/"Try for free" pill right, a floating timeline UI component with 3D app icons tumbling out of it, giant ghosted script logo behind, one caption "A whole new timeline". The product component IS the hero; no headline needed. Only passes because the timeline component is real UI.

# Analytics and tool dashboards (101-144)

Collected 2026-10-18 for tool mode. Searches: product analytics, funnel, retention cohort, web
analytics, dark analytics, data dashboard, marketing analytics. 73 candidates, 44 kept on a first pass, then cut to 18 on a second pass against the tool-mode rubric (16 references + 2 negatives). Rejected numbers are gaps in the sequence; their files are in `reference/_rejected/`. These are the
evidence for `tools-and-analytics.md`; the chart-type entries (funnel, cohort, events, experiments) are
flagged.

## 101 Vectra product analytics (Cansaas) — light, insight builder
- Three-column: nav · main · a right **Insight Builder** panel with tabs (Metrics / Compare / Filters /
  Display), lettered series rows ("A · Active Users · Total unique users"), "+ Add event", a property
  filter row ("Country is Singapore or United States"), and "Run Analysis" as the one filled primary.
  Textbook query-builder anatomy.
- Activity timeline as hourly columns with a 4-step legend "Less active → More active" and tiny
  summary bars under each hour. Feature engagement table: feature (icon + name + description),
  platform, user group chip, avg engagement as a mini bar + ratio, delta chip. Date-range picker as
  a chip row (Today / Yesterday / 7D / 30D / 3M / 6M / 12M).
## 103 Trace AI observability (Odama) — light, dark sidebar · LIVE EVENTS
- Four KPI tiles with sparkline/ring; a stepped multi-line chart (requests / input / output tokens)
  with a 3-row tooltip; a donut of model usage with a legend table; **Live Event Feed**: timestamp
  (ms), event-type chip (LLM_CALL / GUARDRAIL / TOOL_USE / ANOMALY / COMPLETED), latency + tokens, a
  one-line description. Prompts table with success-rate bars and sparklines. The best event-log
  anatomy in the set.
## 108 RevenuePulse funnels (Insoftex) — light, lavender · FUNNEL
- Funnel page IA: five KPIs (Overall conversion, Completions, Users, Avg time to convert,
  Abandonment) each with a sparkline; filter chips (All Funnels / Daily / All Devices / All Segments)
  + a Compare toggle + view-type icons; the funnel as **stepped columns with a sloping drop-off
  area** between them, step name + count + % per step, and a footer strip (Overall rate · Total
  drop-offs · Biggest drop-off in red · Improvement opportunity). Funnel Performance table with
  sparkline trends; Funnel Trend as four lines with a legend; AI insights as three cards; drop-off
  reasons as bars from survey data. The most complete funnel screen in the set.
## 109 Lead magnet funnel (Alamgir) — light, violet · FUNNEL + STEP SETTINGS
- Funnel builder: step cards across the top (Landing Page 100% / Thank You 45% / Order Form 100%)
  with URL chips; "Funnel Drop-off" as five columns with step label, %, count, and a bar coloured on
  a violet→green scale; right panel **Step Settings** form (Page type, Step name, URL match, Goal
  type, Form, Goal conversion rate as a slider with a recommendation line). Builder + preview in one
  view.
## 110 RevenuePulse funnels, dark variant (Insoftex) · FUNNEL
- Same anatomy as 108 on near-black; drop-off area as a gradient wedge. Shows the tool-mode dark
  recipe: surfaces one step lighter, categorical palette lifted, text at 85-90% white.
## 112 Sales funnel (Octet) — light, teal · FUNNEL (stream)
- Funnel drawn as a flowing stream: width ∝ users, with step labels and counts above each
  transition. Devices donut and audience as stacked segment bars by age with %. A legible stream
  funnel because every step is labelled with its number.
## 114 Retention cohorts (Mohammadi) · COHORT TRIANGLE
- The classic: rows = cohort first day with user count; columns Day 0+ … 7+; a header row with the
  column average %; cells show % bold and count small, coloured on a single blue sequential scale;
  Day 0 column fully saturated; the lower-right triangle empty. Simple / Revenue / Advance view
  toggle. This is the anatomy tool-mode §5 describes.
## 115 Retention widget (Shift Studio) — light, orange/navy · COHORT (stacked)
- Retention as **stacked unit bars**: each month a column of hatched blocks, first-time buyers
  (orange) above zero and loyal (navy) below, with a 100…0…100 axis on the right; "40% after 8
  months" as the headline. Countries table with flags. A compact, countable retention device.
## 117 LeonAnd revenue intelligence (Paperpillar) — light, editorial
- "The week in revenue." as a 48px headline with an issue line ("VOL. IV · ISSUE 117 · MON, APR 27
  2026"), one insight paragraph with inline bold numbers, four KPI cells with sparklines and a
  footnote each, then "SECTION 01 · TOP-LINE" with a sentence headline and a single area chart with
  a quarterly-target dashed line. A report-as-dashboard; the editorial lens applied to a tool and it
  works because the data is weekly, not live.
## 122 Privacy-first web analytics (Sokhovich-Kanarovskiy) — light, lime/cyan/red · TREEMAP
- Browser-chrome framing; four KPIs on a hairline strip; **Activity** as a GitHub-style yearly
  heatmap with red cells for anomalies; **Top Pages as a treemap** (lime /home, cyan /how-it-works,
  red-outlined /changelog) with monospaced paths and counts in the corners; Geography and Privacy
  Compliance sections below. Distinctive and honest; mono for paths is the right call.
## 125 Core Web Vitals (Nuvelabs) — light, violet/blue · WEB VITALS
- Cloudflare-style nav (Analytics & logs › Web Analytics); KPI tiles with "from last month"; a
  **Core Web Vitals** tile with a 92.7 score and a 3×4 block matrix for LCP / INP / CLS; Performance
  Overview as grouped bars (Good / Needs improvement / Poor) with a 3-row tooltip; Key Performance as
  a radar (this vs previous period); a pages table with per-column deltas and row actions. A real
  developer-analytics page.
## 126 Reporting overview (Untitled UI) — light, black line
- Three KPI cards (icon, label, value, delta); website traffic as a black line over a hatched area
  with a dotted previous period and range tabs (12m / 30d / 7d / 24h / Custom); a customers table
  with status chips, progress bars and star ratings. The neutral-grotesk floor for tool mode.
## 129 Beast insights (Anna Z.) — near-black, white
- Monochrome dark: four KPI tiles; a sales table with inline progress bars; a cashflow key-value
  panel with a bold total; an overview with three selectable KPIs above a single area chart (the
  selected KPI is the one drawn). Zero colour; hierarchy by weight alone. A strong tool-mode dark
  reference.
## 133 OTT analytics (Sunil) — dark sci-fi
- HUD-styled: angled card corners, cyan outlines, gradient bars, a pie, a map with % bubbles, an
  "evaluation" strip. Kept as a **negative** for tool mode: the chrome shouts and the data whispers;
  every chart uses a different palette.
## 139 Zolatto (Dipa) — light, violet/mint
- Toolbar with "Edit Widget" and "All Channels"; KPI tiles with "40% of 20K goal met" lines; average
  sales as **dot-and-stem bars** with a selected month filled and an insight sentence beneath;
  total transactions as a semicircle gauge with a hatched remainder; AI recommendations as rows with
  category chips. The goal-progress line under every KPI is good practice.
## 142 eye (Rasel) — light, rainbow KPI tiles
- Eight KPI tiles in eight gradient fills, three-colour area chart, coloured world map, multiple
  donuts. Kept as the **tool-mode negative** alongside 028: every tile a different colour means the
  deltas (the only thing that matters) are invisible.
## 143 KLO experiments (Tvardovska) — light, yellow brand · EXPERIMENTS
- Experiments table: name + segment, status chip (Active / Completed), **Lift, ROI, P-value with a ✓
  or ✕ for significance**, period; completed experiments with budget; segments lists (AI-generated
  vs manual) with churn-risk chips; trends with a tab per metric; anomalies and notifications as
  rows with a probable cause. Ukrainian UI; the anatomy is the point.
## 144 MetricFlow (Korobova) — light, blue/coral
- Tilted but legible: KPIs with deltas; two-line performance with a tooltip; **funnel conversion
  breakdown as capsule columns with drop-off % chips** on each step; spend by channel as horizontal
  bars with platform icons; campaign performance as a semicircle gauge with three buckets. The
  capsule funnel is a clean variant.

# Platform batch: platform-native design languages (145-156)

Material 3 and M3 Expressive (145-148), Apple iOS/iPadOS 26 with Liquid Glass (149-153), macOS 26
window chrome (154), visionOS (155-156). Dribbble was thin for native work, so five keepers are
official examples from m3.material.io and the Apple HIG (147, 152-155). No Fluent 2 / Windows 11
candidate passed: the Dribbble ones were a web magazine, 3D art and an ad poster, and the Fluent 2
site illustrates materials with placeholder windows ("Text" menus). The Fluent section of
`platform-native.md` rests on the official docs only. Two negatives: 148 (M3 by default) and 156
(an opaque white slab in visionOS).

## 145 Music player, M3 Expressive (Tom) — Android, black + per-cover accent, EXPRESSIVE SHAPES
- Four now-playing screens, each themed from its cover: coral (Måneskin "Supermodel"), lime
  ("NUEVAYoL", Bad Bunny), periwinkle ("The Greatest", Billie Eilish), pink (Olivia Dean). The
  cover fills the top ~60%, a dark scrim carries the title in a wide extended display face and a
  thin artist line, then a black control deck.
- Controls form an M3 Expressive button group with shape by role: play/pause a ~195dp circle (half
  the width), skip back/forward two tall pills (~70 x 135dp), shuffle in a scalloped "cookie" shape
  from the shape library, queue in a circle. Hierarchy is carried by size and shape; all four
  share one tone.
- Progress is the Expressive wavy indicator: the played part is a sine wave, the rest flat, with a
  vertical stop mark. Lesson: Expressive ships sanctioned bespoke parts (wavy progress, the
  35-shape library, morphing button groups); spend them on the one interaction that matters and
  keep everything else baseline.
- Lesson: dynamic colour from content is the atmosphere. One seed per cover, spent only on the
  controls; the deck stays black.
- Weak: no elapsed/remaining time on the progress; the selected shuffle reads as disabled (muted
  tint on the scallop); the board repeats and mirrors screens for presentation.

## 146 Reservations concept, M3 Expressive (Dan) — Android, sage + butter yellow, DYNAMIC COLOUR
- Map-first café booking: tonal circular POI markers (McDonalds, Country Bread, Zino Ristorante) on
  a pale map; a large sage container card holding "Kara Kedi Coffee Shop", "Open · Closes at 7 pm",
  a photo with its own smaller inner radius, an address row with "A little busy now", a yellow
  directions button, and "Availability for Today" time chips (9:00 am / 9:15 am / 9:30 am / →).
- Colour from one seed: sage primary-container surfaces, butter-yellow tertiary containers for the
  bookable times and the directions action. Tertiary is used where M3 says it belongs (contrasting
  accents that need attention), so the eye goes to the times first.
- M3 navigation bar untouched: 4 destinations (Explore / Search / Reservations / Account), active
  icon in a pill indicator, labels on every item. Lesson: the brand lives in the card and the map;
  the bar is the platform's.
- Lesson: the photo's radius is smaller than the card's, i.e. optical roundness (outer − padding).
- Weak: shown in an iPhone frame with the Dynamic Island and iOS status bar, the "which platform?"
  error in miniature. A dark sibling (search sheet, filter chips) exists; this light one is stronger.

## 147 Payments list, M3 Expressive (Material Design, official) — Android, baseline lilac, CONTAINMENT
- From "Start building with Material 3 Expressive" (m3.material.io blog, May 2025): the lower half
  of a payments home. "Cards & passes" tonal chip with a "3" badge; Favorites row of circular
  containers (Deposit / Goals / Credit score) and avatars (Pia, Marty); a "Payments" sheet with
  rows "Alejandro Ortega · Internet · 1 day ago · +$75", "Carmen Villanueva · Nephew's gift · 2 days
  ago · $24.50", "Ana Russo · Lunch · 4 days ago · $19"; a 3-item nav bar (Dashboard / Offers /
  Rewards) with a pill indicator.
- The post pairs it with a baseline version of the same content (flat rows, bare icons, no
  containers). The Expressive one groups rows into tinted containers with small gaps and rounder
  outer corners, puts icons in circular containers and fills the chip with primary container.
  Lesson: Expressive hierarchy comes from containment and tone, not from shadows or more hues.
- Lesson for banking: an official transaction row with person, purpose, relative time and amount;
  the incoming amount signed and set in the tertiary tone.
- Weak: still the baseline lilac seed (right for a spec, wrong for a product; see 148); mixed
  precision ("$19" beside "$24.50").

## 148 MaterialMe products dashboard (Setproduct) — tablet/web, default M3 lilac, NEGATIVE
- A "MaterialMe" kit page: black navigation drawer with an outlined active item and a "New"
  badge; underline tabs (All products / Digital goods / Books / Files / Music); four equal KPI cards
  ($128,109.38 / 1292 / 102 / $12,134.15) each with an (i); a stacked bar chart in three lilac
  tints with a tooltip; a product table.
- Kept as a NEGATIVE example: M3 by default. Nobody chose the seed (lilac container on the one
  button, lilac bars, lilac badge); the button carries a black outline M3 does not use; the drawer
  is black instead of a surface container with a pill indicator; four identical tiles and no hero.
- Small tells: "$10.038" in the tooltip (wrong separator), "1292" with no separator beside
  "$128,109.38".
- Lesson: start from a brand seed or content-derived dynamic colour and the five surface
  containers. If the screen could be any page of the M3 docs, it is unbranded, not native.

## 149 Pine Peak Cabin detail, iOS 26 (Mari Chubina) — iPhone, stone + espresso, GLASS OVER CONTENT
- Listing detail: a full-bleed photo hero (~45% of the screen) with a "1 of 32" counter; back,
  share and heart as circular glass buttons floating on the photo; meta chips (2 guests / 24-26
  Sept / 48 m² / 1 beds); "Pine Peak Cabin, Karelia, Russia"; three stat tiles (4,99 Average rating
  / 587 Reviews / Superhost); a floating espresso CTA "Book for $140" over "$0 today · Free
  cancellation".
- Second screen: "4.97" at ~68pt between laurel glyphs (4x the 17pt body), "Guests' choice", a
  review card, "Show all 100 reviews".
- Lesson: glass is only on controls, and it has something to refract (the photo). The hero is
  content: a photo and a giant rating, both inside the content layer.
- Lesson: the photo's lower corners take a large radius that echoes the device corner; the CTA
  carries its consequence line.
- Weak: "4,99" on one screen and "4.97" on the next; "1 beds"; the CTA clips the stat tiles; an
  Airbnb pastiche.

## 150 Pine Peak results, iOS 26 (Mari Chubina) — iPhone, stone + espresso, FLOATING TAB BAR
- Search results: a glass back button and a search capsule ("Karelia, Russia", "24-26 Sept · 2
  guests") in the nav area; filter chips (filter icon, "On map" filled espresso, Popular ▾,
  Price ▾); a photo mosaic (one large, two stacked) for the first listing; "24-26 Sept · $140 for 2
  nights · ★ 4,99"; a carousel of smaller cards.
- The tab bar is the iOS 26 one: a capsule inset from the screen edges, floating over the
  carousel with the photos blurred through it, the selected tab (Search) in a lighter inner
  capsule, filled glyphs with single-word labels (Search / Favourites / Booking / Chat / Profile).
- Lesson: let content run under the bar; that is what makes the material read. No solid footer.
- Weak: same product as 149 (kept because it is the only clear floating tab bar in the batch);
  photos repeat across screens; the content face is a geometric sans, fine in content only if it
  scales with Dynamic Type.

## 151 GitHub profile with contributions, iOS 26 (Max Burnside) — iPhone, near-black + green, CONTENT HERO
- Current vs Revised. Current: avatar, name, "Set your status", a list of links, then inset-grouped
  rows (Repositories 13 › / Starred 3 › / Organizations 0 ›). Revised: links condensed to one line,
  achievements beside the name, and a contributions grid as the hero: "3,542 contributions in the
  last year", 7 x 16 rounded tiles in five greens, "+1,928 more than 9/17/24" and "449 day streak".
- Lesson: the bespoke element goes in the content area, between the header and the native list;
  the list below keeps the system anatomy (icon tile, label, count, chevron) with the larger iOS 26
  section radius.
- The number sits inside the sentence in the accent (the 060 move), three times.
- Weak: 16 weeks shown for "the last year"; US-only date; tiles are bevelled like glass (opaque,
  so acceptable, but do not make content tiles translucent).

## 152 Notes with format sheet, iOS 26 (Apple HIG, official) — iPhone, white + Notes yellow, SHEETS
- From the HIG Sheets page: a note "Monday Morning Meeting" with a selection; glass controls at the
  top (back; undo; share and ••• grouped in one capsule) and a yellow prominent ✓ that is the only
  coloured control; a nonmodal "Format" sheet inset from the screen edges with a large radius
  following the device, a close button, a style row (Title / Heading / Subheading / Body, Body
  selected in yellow) and segmented groups (B I U S; lists; indent).
- Lesson: the Liquid Glass colour rule in one screen: monochrome glass, accent on the background of
  the single primary action.
- Lesson: a part-height sheet floats inset with content visible around it; segments inside it use
  concentric inner radii.
- Weak: a system app with no brand; use it for chrome anatomy only.

## 153 Landmarks with background extension, iPadOS 26 (Apple HIG, official) — iPad, photo hero, SIDEBAR
- From the HIG Layout page: a floating glass sidebar (Landmarks / Map / Collections) with its toggle;
  a Mount Fuji photo filling the top of the content area and mirrored, blurred, beneath the sidebar
  (background extension effect); back, share, a grouped favourite + collection capsule and info as
  glass buttons on the photo; "Mount Fuji" and three paragraphs below.
- Lesson: this is the platform-native hero. Full-bleed imagery in the content layer, glass controls
  on top, the image extended under the sidebar so chrome sits on content, not on a grey panel.
- Lesson: toolbar items grouped by function in shared capsules; icons, not text.
- Weak: the text block has no hierarchy beyond the title; the busy crop behind the buttons is
  where a scroll edge effect earns its place.

## 154 Notes window, macOS 26 (Apple HIG, official) — Mac, white, WINDOW CHROME
- From the HIG Toolbars page: traffic lights; sidebar toggle and back as round glass buttons; the
  title "Notes" with "103 notes" inline in the toolbar; grouped glass capsules (compose; Aa,
  checklist, table, attachment, collaboration; lock; share; •••; search); the ••• menu open (Pin
  Note highlighted, Lock Note, Find in Note, Move to ›, Recent Notes ›, Math Results ›, Attachment
  Viewer ›, Delete Note).
- Lesson: Mac chrome is one toolbar integrated with the title bar; items have no individual
  bezel, they sit in glass groups, and ••• holds the overflow. Each item must also exist in the
  menu bar.
- Lesson: the window's large corners and the toolbar capsules are concentric.
- Weak: a system app; shows chrome, not density.

## 155 Music window, visionOS (Apple HIG, official) — visionOS, glass over passthrough, ORNAMENTS
- From the HIG Sidebars page: a Music window on default glass in a room; a vertical tab bar
  ornament floating off the window's leading edge (six glyphs, Library selected in a lighter
  circle); inside, a sidebar "Library / All Music" (Recently Added, Artists, Albums, Songs, Made For
  You) and a "Playlists" section with "All Playlists" selected as a lighter rounded rectangle; the
  content pane "Playlists / All 254 Playlists", a search field and a grid of large rounded tiles.
- Lesson: the tab bar is vertical and outside the window as an ornament; the sidebar is a second
  glass; selection is a lighter fill, never a hue.
- Lesson: rows are tall and widely spaced for eye targeting; text is bold white with vibrancy.
- Weak: placeholder tiles; the crop hides the window bar and the toolbar ornament.

## 156 Reader, visionOS explorations (Paperpillar) — visionOS, beige room + coral, NEGATIVE
- Three windows angled around the viewer: a timer and checklist, a reader with a glass sidebar
  (Home / Just For You / Reading List / Draft / Collaboration / Your Stats) and an opaque off-white
  article pane "The Cultural Significance of Greenhouses" in a thin serif, and a chat window. A
  custom bar floats above the reader: back, history, list, search, share and a close ×.
- Kept as a NEGATIVE example: the article is an opaque white slab in passthrough, which the HIG says
  blocks the surroundings and feels heavy; a thin serif at 12-14pt in space; the custom top bar
  duplicates the system close and window controls instead of a bottom toolbar ornament; lorem
  ipsum in the side windows; "Jean Doe".
- What is right: the sidebar glass and a separate floating bar show the ornament idea. Lesson:
  keep the window glass; put the brand in imagery and content, not in the window material.

# Systems batch: enterprise and public design systems (170-182)

Captured 2026-10-27 with headless Chrome from public pages only (no sign-in): GOV.UK Design System
examples and gov.uk (govuk-frontend 6.6.0, the 2025 brand: blue header, GOV•UK logotype with a
turquoise dot, pale-blue footer), IBM Carbon storybook (v11), Shopify Polaris App Home page-pattern
previews on shopify.dev (cropped from the docs page), Atlassian Bitbucket Cloud, and the USWDS
storybook. Sizes are read off the 1440px captures (390px for 172). Source URLs are in `review.tsv`.
These are system screens, so the bar is clarity and consistency, not the scroll-stop qualities;
170-176 are the bar for **service mode**.

## 170 Register to vote start page (GOV.UK) — web, white + GOV.UK blue, START PAGE
- A real start page inside a multipart guide. Blue header 61px (logotype, "Menu", search); a grey
  "Part of Vote in UK elections" box; h1 "Register to vote" at 48px bold; a two-thirds column with
  "You can use this service to:" and three plain bullets; inset text for the Welsh version;
  "Register online" h2, "It usually takes about 5 minutes."; a green "Start now ›" button set at
  24px, larger than the 19px Continue used inside the service; "Before you start" naming the one
  document needed (National Insurance number) and that you can still register without it.
- Right one-third: step-by-step navigation, numbered circles 1-5 on a vertical connector, the
  current step filled black, alternatives marked "or", each step with Show/Hide.
- Lesson: the start page is the only hero a service gets, and its job is to set expectations
  before commitment: what you can do, how long it takes, what you need, then one start button.
- Cookie banner (two equal green buttons, "Accept"/"Reject additional cookies") pushes the h1 to
  y≈550 at 1100px tall. The step-by-step aside is for journeys spanning several services; do not
  add one to a single form.

## 171 Where do you live? question page (GOV.UK Design System) — web, white, QUESTION PAGE
- Content in a 960px column (x 240-1200 at 1440). Back link (chevron + underlined "Back", 16px);
  the legend is the h1, "Where do you live?" at 36px bold; four radios with 40px circles and 19px
  labels; green "Continue", 40px including its 2px darker shadow, square corners. Then the footer:
  10px blue top rule, #f4f8fb ground, OGL and crown copyright.
- Lesson: one thing per page. The question is the heading and the only thing on the page; no card,
  no progress dots, no sidebar, about 70% of the viewport empty. The emptiness is the design.
- Rejected sibling (gov.uk/check-uk-visa) adds the section as a grey caption above the h1 ("Check
  if you need a UK visa") and a select; the caption carries the section, never a repeated h1.
- Not a layout to "fill": the right half stays empty on purpose at desktop widths.

## 172 Date of birth question, mobile (GOV.UK Design System) — mobile 390, white, QUESTION PAGE
- h1 "What is your date of birth?" (27px on small screens), grey hint "For example, 31 3 1980"
  with no full stop, then Day and Month inputs about 52px wide and Year about 86px, all 40px tall
  with 2px black borders; "Continue" goes full width on mobile.
- Lesson: input width tells the user the length of the answer (width-2, width-4 classes); the hint
  shows the format by example rather than "DD/MM/YYYY"; body stays 19px on phones in v6.
- Weak: the footer licence line is clipped at the capture's right edge; check footers at 390.

## 173 Error summary on a question page (GOV.UK Design System) — web, white + red, ERROR STATE
- Error summary first in main: a 5px red border box, "There is a problem" at 24px bold, one red
  underlined link per error ("Passport issue date must include a year"). Below, the question
  "When was your passport issued?" with a 5px red rule down the left of the form group, the same
  message inline in red bold above the inputs, and a red border on the Year field only; Day (5) and
  Month (12) keep what the user typed.
- Lesson: errors at two levels that say the same words: the summary (focus moves to it, each item
  links to its field) and the inline message at the field; the message says what to do, and
  entered values survive. The page title also gets an "Error: " prefix.
- Do not borrow the red for anything that is not an error.

## 174 Check your answers (GOV.UK Design System) — web, white, CHECK ANSWERS
- h1 "Check your answers before sending your application" (36px, two lines); two summary lists
  under 24px h2s ("Personal details", "Application details"); each row a bold 19px key, the value
  (multi-line addresses kept as lines), and a right-aligned "Change" link; 1px grey rules; a
  skipped optional answer shows "Not provided". Closes with h2 "Now send your application", one
  declaration sentence and a green "Accept and send".
- Lesson: review is a summary list, not the form re-rendered read-only; every answer is one click
  from its question; the button names the commitment, not "Submit".
- Change links carry visually hidden context ("Change name"); copy that, or ten identical "Change"
  links read as noise to a screen reader.

## 175 Confirmation page (GOV.UK Design System) — web, white + green panel, CONFIRMATION
- A green panel (#0f7a52, 630x240) with "Application complete" at 48px bold white, "Your reference
  number" at 36px regular and "HDJ2123F" at 36px bold; then "We have sent you a confirmation
  email."; h2 "What happens next" naming the office that has the application and what it will do;
  a feedback link with "(takes 30 seconds)".
- Lesson: the only large coloured block in a GOV.UK service is the end. The confirmation carries
  outcome, reference, next step and who acts; no illustration, no confetti.
- Weak: no timescale ("They will contact you" has no "within 10 working days"); add one when known.

## 176 Task list (GOV.UK Design System) — web, white, TASK LIST
- h1 (placeholder "Service name"), two groups under 24px h2s ("Check before you start", "Prepare
  application"), rows about 46px with the task name as a link and the status right-aligned:
  "Completed" as plain black text, "Incomplete" as a light-blue tag. A green "Apply" at the end.
- Lesson: completed tasks go quiet so the remaining ones stand out; statuses are sentence case
  words, and the whole row is the link. The inverse of a list of green ticks.
- Weak: placeholder h1, and no count line; add "You have completed 3 of 7 sections" above the
  groups when the list is long.

## 177 Data table with batch actions (IBM Carbon) — web, White theme, DATA TABLE
- Title "DataTable" 20px with a 14px #525252 description on a gray-10 (#f4f4f4) layer; a 48px
  toolbar with search and settings icons and a blue (#0f62fe) "Add new" primary 136x48, square,
  flush to the right edge; header row #e0e0e0 with 14px semibold labels; 48px rows with 1px
  rules, a checkbox column, 14px IBM Plex Sans; status as coloured text ("Starting", "Active" in
  blue, "Disabled" in light grey).
- Lesson: Carbon density: no cards and no shadows, a layer colour instead of a container, square
  corners, row heights from a fixed set (24/32/40/48/64), one blue for action and selection.
- Rejected sibling (AI full table): the same table with a 1px #4589ff border, an "AI" label and a
  pale blue aura gradient over the rows. The one gradient Carbon sanctions is for AI output.
- Weak: status by colour alone and grey "Disabled" below contrast; use Carbon's status icons or
  tags. Demo data ("Load Balancer 1-6", "Kevin's VM Groups") is not content.

## 178 Form (IBM Carbon) — web, White theme, FORM FIELDS
- A 600px form: search field, then 12px #525252 labels over 40px fields filled #f4f4f4 with a
  1px bottom rule and no other border; 12px helper text under each ("Lowercase letters, numbers,
  hyphens only."); paired short fields in two columns; date fields with a calendar glyph; a number
  input with − and + steppers; inline radios with consequence labels ("Private – only invited
  members"); checkboxes; textarea.
- Lesson: the Carbon field is a filled box with a bottom rule, and every field gets a helper line.
  Spacing between groups is tight (16-24px); the form reads as a list, not a set of cards.
- Weak: placeholders left in ("Option 1", "Option 2", "Select members"); never ship demo values.

## 179 App homepage template (Shopify Polaris) — web, white cards, near-black primary, HOMEPAGE
- Page actions top right: two secondary ("Browse templates", "Import image", white with a 1px
  border) and one near-black primary ("Create puzzle"). A light-cyan info banner ("3 of 5 puzzles
  created. Upgrade…"); a setup guide with title and description outside the card, "0 of 3 steps
  completed" and a dismiss ×, three checkbox rows with chevrons; a metrics card of three cells
  split by hairlines ("Total Designs 156" + green "↑ 12%", "Units Sold 2,847" + orange "0%",
  "Return Rate 3.2%" + red "↓ 0.8%"); a callout card with an illustration; three template tiles;
  news rows with dates; featured app tiles. 12px card radius, 13px Inter body.
- Lesson: Polaris sections put the heading and description outside the white card; one primary
  per page; illustration lives in empty states and callouts only; the connected metrics strip is
  052's hairline KPI card in system form.
- Weak: "Return Rate ↓ 0.8%" is red although a falling return rate is good (the sign reads
  backwards); six stacked sections of equal weight give no dominant element.

## 180 Resource details template (Shopify Polaris) — web, white cards, DETAILS
- Breadcrumb "Puzzles", title "Mountain view" about 24px, page actions "Duplicate" and "Delete"
  (red text, not a red fill). Main column about two-thirds: "Puzzle information" card with 32px
  text fields (8px radius, 1px grey border) and a helper line under each; "Puzzle templates" with
  a count badge "2", a secondary "Browse templates" and a table inside the card (search, Preview
  link, ×); "Production settings" with a description; selects, a stepper field and a toggle.
  Aside one-third: "Puzzle summary" with a green "Active" badge and three facts; "Notes" with a
  pencil.
- Lesson: edit on the left, state on the right. Status and summary sit in the aside, destructive
  actions change tone rather than weight, and a card holding a table drops its padding so the
  table reaches the card edges.
- Weak: placeholder URL "https://example.com/image.jpg"; the aside is sparse at 1440.

## 181 Repository source view (Atlassian, Bitbucket Cloud) — web, white, NAVIGATION SYSTEM
- ADS in production. Side nav 320px (product tile, "For you", "Recent ›", "Customize sidebar");
  top bar 56px with a wide search field; breadcrumb "Atlassian / Project: Atlassian /"; title
  "atlassian-frontend-mirror" at 24px in Atlassian Sans heavy; default buttons "Pull requests",
  "Clone", "⋯" at 32px; a description line; branch picker and a "Files ▾ Filter files" combobox;
  a table (Name, Size, Last commit, Message) with 48px rows, folder icons in 32px blue-tint tiles,
  and dates relative up to a week ("18 hours ago", "4 days ago") then ISO ("2026-10-01").
- Lesson: ADS neutrals (#292a2e text, subtle greys) carry the page; brand blue appears on icons,
  links and the primary only. The relative-then-absolute date is a micro-detail worth copying.
- Weak: the message column clips mid-word with no ellipsis ("UTC 202"); the lilac cookie banner
  takes 104px. Rejected sibling (commits) adds mono hashes and a commit-graph rail.

## 182 Landing page template (USWDS) — web, navy + cyan + stock photo, TEMPLATE AS-IS
- The USWDS landing-page template exactly as shipped: the official-site banner, a header reading
  "<Project title>", a full-bleed stock photo with a navy callout "Hero callout: Bring attention to
  a project priority" in Merriweather (second line cyan) and a "Call to action" button; a
  "tagline" section; a navy band of four 120px solid blue circles standing in for images beside
  cyan headings ("Graphic headings can vary.").
- Kept as a NEGATIVE example: the sloppy version of any public or enterprise system is its
  template shipped unedited. Every element is valid USWDS and the page still says nothing: no
  task, no service, placeholder copy, decorative circles where content should be.
- Lesson: templates are scaffolding. Replace every placeholder, delete sections with nothing to
  say, and lead a service with the task and its start button (170), not a photograph.

# Aesthetic movements (195-209)

Collected 2026-10-27 for `languages/movements.md`. Searches: neubrutalism website, neo brutalism app,
bento grid website, skeuomorphic app ui, tactile ui, y2k website, retro ui website, terminal ui,
maximalist website, editorial website, collage website design, spatial ui, swiss style website, dark
mode website brutal. 42 Dribbble candidates plus 4 live-site captures (Awwwards / Land-book listings);
13 kept and 2 negatives. Spatial / 3D (non-platform) and Swiss have no new keeper: the Vision Pro
shots belong to the platform batch, and the live captures failed or were mostly photo (see
`review.tsv`). Hex values are sampled from the images; sizes are approximate, read at full size.

## 195 PawPal pet adoption (Md Nahid Hossain) — mobile, yellow + black, NEO-BRUTALISM
- Three screens (log in, home, pet detail). Yellow #FFD43B fills the whole log-in screen, the home
  header band and the primary CTA; everything else is #FFFFFF or the warm page. Every card, input,
  chip, segment and button has a ~3pt black outline and a hard black offset shadow (~5pt down-right,
  no blur); radius ~12pt on cards, full pill on chips.
- Heavy grotesk headings ("Find a New Best Friend", "Biscuit" ~30pt); chip row All (black fill) /
  Dogs / Cats / Rabbits (outlined); segmented controls with the active half filled black (Log In,
  Info). Detail: four stat tiles (2 yrs Age, Male Gender, 28 kg Weight, Dog Type), status chips
  "Vaccinated" green #4ADE80 / "New" / "1.2 km", a coral #FF5A5F "Urgent Adoptions" banner with
  "3 pets need homes today", and a sticky "Apply to Adopt Biscuit".
- Lesson: neo-brutalism is one rule applied without exception: outline + flat fill + hard shadow on
  everything interactive, and the loud colour spent on the one action region of each screen.
- Weak: the shadow also sits on non-interactive cards ("About Biscuit"), so it stops meaning
  "pressable"; emoji inside labels (a dog face after "Log In") and greyed emoji as tab icons mix icon systems;
  the blue "$150 adoption fee" is a fifth hue with no role.

## 196 Neo-brutalist task dashboard + help centre (WhiteUI.Store) — mobile, off-white, NEO-BRUTALISM (quiet)
- "Dashboard" (eyebrow "Content overview", ~36pt bold title): "Upcoming Events" row card with an
  icon square; progress card "Mobile app design 48%" with a two-tone bar, outlined date chip
  "04 Oct 2022" and a five-avatar stack; segmented All Tasks (black fill) / Pending / Done; one
  bordered list holding an add-task input with a black "Set date", a dotted rule under it, then rows
  of check + title + outlined date chip.
- "Help Center": violet eyebrow "Articles and instructions", a search field with a violet #A67CF7
  square button, "For example How to create an account", product rows (Wallet / Online Trading /
  Card) each with an outlined icon square, and an article card with an outlined "Taxes and Fees" tag.
- Tokens: page #FAF4F0, 1.5pt black lines, radius 0, and the hard offset shadow (~5pt) on exactly
  two elements: the Upcoming Events card and the search field.
- Lesson: the product version of neo-brutalism. Outline everything, square the corners, let black
  fills carry selection, and reserve the hard shadow for the one or two things that invite action.
- Weak: dates in two formats ("04 Aug 22", "19 Aug 2022"); the article dek talks about cancelling
  a reservation under a tax headline; violet eyebrow + violet button + green checks are three accents.

## 197 Axis Collective architecture studio (Diana Advokatova) — web, greyscale, BRUTALISM / EXPOSED GRID
- Hero on a mid-grey page: #202020 panels on a four-column grid whose 1px rules run past the panels
  like crop marks. Left: brand and a five-link nav in ~24px regular grotesk (active white, rest
  grey). Centre: grainy black-and-white architecture photo. Right: "BRUTALISM" set vertically in a
  heavy condensed grotesk ~300px tall over a translucent "01", and a second photo panel.
- Facts: three stat tiles with line icons and mono numerals (Active Projects 14, Total Gross Area
  120,000 m², Under Construction 5); "Axis" drawn with construction guide lines through the
  letters; "MUMBAI, IN → ARCHITECTURE AT SCALE" in small caps; text-link CTAs in the bottom row.
- Lesson: raw brutalism is not neo-brutalism. No colour, no offset shadow: the grid is drawn as
  rules, type is set as architecture, numbers are facts in mono, and grain lives on photos only.
- Weak: the brand is "Aethel Collective" in the nav and "Axis Collective" in the copy; the small
  paragraph is garbled placeholder text; "©2024" appears twice; glassy stat tiles contradict the
  raw stance.

## 198 Domo electrification features (Zenork) — web, five tints, BENTO
- Feature section of five tiles: top row split 2:3, bottom row three equal. Each tile shows a
  cropped live product fragment in its top ~60%, faded into the tile at the lower edge, then a
  ~24px title and a two-line sentence ("Compare timelines", "Share roadmap with others").
- Fragments are real UI: a roadmap card ("Ria's Home 1", address, avatars, "Upcoming Project: March
  2022"); a "Cumulative Cost" three-line chart 2022-2031 with a tooltip (Reactive $5210 / Proactive
  $4535 / My Custom $4805); a timeline menu (Actual / Alternate); a notification ("Choose an HVAC
  contractor"); a share modal with "Generate Invite" and roles.
- Lesson: a bento tile shows the feature itself, not an icon for it, and its width follows the
  fragment: the chart gets the 3/5 tile.
- Weak: the milky tint set (#FFF1E6 peach, #FDE2E4 pink, #DFE7FD periwinkle, #E2ECE9 sage,
  #EAE4E9 mauve), one per tile with no meaning; the template token "{projectName}" leaked into the
  copy twice; the equal bottom row is the uniform-tile tell creeping back.

## 199 Coordy calendar hero (Ann Kyrk) — web (tablet frame), dark + muted blocks, BENTO HERO
- Left half #131313 with an uppercase tight grotesk headline "OUTSOURCE YOURSELF. TO YOURSELF."
  (~40px, full stops), a three-line subhead and a red #E83A2A pill "Double Your Focus".
- Right half: a two-column masonry of widget tiles that bleed off the top and bottom of the frame,
  each drawn in one ink on its fill: olive #C0C1A5 menu (Meetings / Business Trips / Family, "BACK
  TO DASHBOARD"), green #154D40 "GROWTH" line on a grid, taupe #C5BBB9 "AVAILABILITY" 7×3 dot grid
  (empty / red / black), mauve #E3C3DD month calendar with today ringed, "Progress Tracker" ring
  "25% more productive this week", red "Scheduling Efficiency June – July 2025" thin-bar chart.
- Lesson: a hero bento of product micro-visualisations. Unequal tile heights in offset columns,
  cropped by the frame so the product seems to continue; one ink per tile keeps six fills calm.
- Weak: the calendar has "27" twice; the orphan "BACK TO DASHBOARD" shows tiles from different
  states; the tablet frame is presentation.

## 200 Drone flight app showcase (Dmazing) — web, charcoal + orange, BENTO + TACTILE
- Still from a motion piece: six tiles on #101010, radius ~28px, ~16px gutters. A matte drone
  render cropped tight with thin orange arcs; a landscape phone shot of the flight camera UI (timer
  "01:39", ISO scale, record button); a solid orange #E75324 tile "Tap. Fly. Control. / Film like a
  pro." (~80px); "Your Joystick to the world above." with "Joystick" in orange beside a macro crop of
  the on-screen joystick; a compass dial macro (0°, 30°, 330°, orange needle); a tall ISO roller
  (200 / 400 / 600 / 800, 600 selected in orange inside a glossy pill).
- Lesson: a marketing bento where each tile magnifies one control 3-4x, so the product's tactile
  vocabulary (dial, roller, joystick) becomes the layout; one accent runs through every tile.
- Weak: the phone screenshot is too small to read; no feature names or specs anywhere; the render
  tile is pure art.

## 201 Bento layout trend (Dmitry Sergushkin) — web, six tints, BENTO NEGATIVE
- A 3×2 grid of equal tiles, each with its own tint (mint #E6F6E5, lilac #FAF5FF, black #121213,
  grey #F6F7F9, blue #E8F4FF, cream #FFF9E5), a ~28px two-line title ("Understanding client
  needs", "Effective communication"), a three-line platitude and a generative line-segment glyph on
  a faint dash grid; repeated at a larger size on the right.
- Kept as a NEGATIVE example: the uniform-tile bento banned in `typography.md` §5. Equal size, one
  tint and one icon per tile, interchangeable copy; any tile could swap places with any other.
- Lesson: the glyphs are well drawn, and that is the point: craft does not rescue a grid with no
  hierarchy. The black tile is the only emphasis and it is not the most important claim.

## 202 Light control knob (Mik Skuza) — mobile, slate + orange, TACTILE
- Two variants side by side ("Modern Bulb Style", "Modern Knob Style") on #1E272F. Panel slate
  #445762 darkening downward; header "Main Settings / Group One →"; a 2×2 grid: "Brightness 72%" in
  orange #EB7500 at ~64px, "239", "R: 80 G: 60 B: 30" (grey labels, white values), "S-Curve".
- The hero is one physical control ~360px wide: A is a glossy sphere lit from the top with an orange
  glow arc tracing 72%; B is a matte dial with a single orange tick. − and + sit at the arc ends;
  menu and power icons in the footer. Variant B drops the tile borders for hairline dividers and
  loses nothing.
- Lesson: tactile done well is one object per screen, and it is an input the user turns, with its
  value repeated as a flat number; everything else stays flat.
- Weak: "239" has no label or unit; grey labels on slate look below 3:1; no on/off state.

## 203 Ellis "Recollection Prospective" (SUPERGLOW) — web, iridescent + pale pink, RETRO / Y2K OS
- The site is a late-90s desktop: white menu bar (logo, Spotify and YouTube glyphs, fullscreen,
  clock "14:17"), an iridescent pink/cyan/magenta wallpaper with scan lines, desktop icons (Spotify,
  Socials, About, Remix, Video, Sign Up, Artwork, Trash) and overlapping windows: a Spotify player
  with a track list, "Sign Up · Ellis Updates" with email, consent checkbox, legal paragraph and
  "Subscribe", "Video" with .mp4 file icons, "About" as a two-column credits grid, "Socials".
- Window chrome: 1px dark border, ~22px grey title bar with a centred letter-spaced title and a
  logo glyph, pale pink #F6DBE2 body, a hard grey offset shadow (~3-4px, no blur), bitmap-style UI
  type.
- Lesson: retro as information architecture. The OS metaphor is the navigation (window = section,
  icon = link), so the nostalgia does work; the colour is spent on the wallpaper and the windows stay
  pale and readable.
- Weak: windows hide half the consent copy; text ~10px; social icons from mixed sets; no single
  first action.

## 204 Retro Food diner (Jesse Showalter) — web, paper + yellow, RETRO / PRINTED MENU
- A menu site as a printed bill of fare: paper ground #F9F8F2 with grain; every region a cell in a
  grid of 1px black rules (mascot / title / mascot header row; a nav row of five equal cells HOME,
  MENU, LOCATION, CRAFT BEER, CONTACT); 8px hatched bands as section dividers.
- "RETRO FOOD" in a chunky display with a yellow #FDC74B extruded shadow; "PIZZA BY THE SLICE"
  ~56px; rubber-hose cartoon mascots in black line; price cells "$4.99 / $7.99 / $10.99 / $12.99"
  each ending in a yellow arrow square; "950 CALORIES" micro labels; black-and-white restaurant
  photos with clipped corners.
- Lesson: retro by one period source held everywhere: a print grid, one ink plus one spot colour,
  period illustration, a period display face. The price cell is a real commerce component in
  costume.
- Weak: the body paragraph repeats a clause ("and self-rising crusts") as filler; every item says
  "950 CALORIES"; long body set in the alternate-heavy display face reads slowly.

## 205 Satellite panel (Hananda) — desktop, black + mint, TERMINAL / INSTRUMENT
- #0B0B0D ground, 1px dark panel borders, one phosphor accent mint #73F7D6; mono throughout, labels
  uppercase. Hero: an isometric wireframe of the station on a faint grid with leader-line readings
  ("HG-ANTENNA 72%", "SOLAR-06 89%", "WING-02 90%") and a "SCANNING..." tag with a segmented meter.
- Right column: TRANSMISSION bars with their scale printed under each (Packet upload 65%, 125 /
  210 GB; Bandwidth quota 80%, 4.1 / 5 TB; Contact window 32%, 2:00 / 8:00 MIN); ORBITAL LOCATION
  (LAT +34.05°, LONG −118.25°, ALT 508.6 km (LEO), globe with a 27,540 km/h callout); BATTERY "90%"
  ~40px with an "ON CHARGE" chip; NETWORK SPEED boxed line chart (1.6 / 1.2 GBps). Bottom: "SAT-0043X
  ● IN ORBIT" with a `key : value` grid, a discrete 20-segment bar "SOLAR PANEL 03 32%", and LOGS
  with "2025-07-22 08:32:10 Power_Reroute" and a one-sentence event.
- Lesson: terminal language for a live instrument: one accent, `key : value` facts, scales printed
  under bars, a wireframe of the real object as the hero with readings on leaders (cf. 015), the
  latest log line as the newest fact.
- Weak: "Ø" substituted for "O" in labels hurts reading and screen readers; an unexplained number
  column ("4. 23 87867"); "LAUNCH DATE" used for two different fields; the battery curve is smoothed
  into decoration.

## 206 Mission control interface (Rayyan Anugerah) — desktop, black + orange tick, TERMINAL / TOOL
- Mono throughout on #0A0A0A; panels framed by 1px rules with corner-bracket marks; a 2px orange
  #FF6600 tick before every section title. Header: a red-tinted "[CLASSIFIED ACCESS]" chip, grey
  Admin / Access chips, "Last Sync: 2025-11-11 10:42:16 GMT+8", green-tinted ONLINE / ACTIVE chips.
- Metrics 37 Active / 129 Completed / 12 On Hold in bracketed boxes; bar-glyph meters "|||||||| 84/112".
  Mission table with one expanded row: objective, agents, region, risk, then an Activity Log of
  "> [17:48:12] …" lines with keywords coloured (red "Firewall breach detected", green "68%
  retrieved"). Status = dot + word; priority = coloured word.
- Approval panel: key-value grid (ID, region, risk as a two-segment bar + MEDIUM, 48HRS, PENDING
  APPROVAL), "AI Assessment:" as "> " lines (82% probability, a recommendation), then CANCEL
  (outlined) and APPROVE (white fill) under the facts. An assistant panel with "Ask anything...".
- Lesson: terminal for a dense tool: the log is content, AI output is plain prefixed lines inside the
  decision it informs, and the two actions sit directly under the facts that justify them.
- Weak, and not to copy: a real agency's seal and name and a face-identification camera tile (the
  theme, not the language); "MISSON NAME" typo; two identical "MIT 200777" rows; two colour systems
  per row (status dot and priority word); the blue dropdowns are the only blue on screen.

## 207 Ghia about page (LAIN) — web, oxblood + cream + olive, MAXIMALIST / COLLAGE
- Palette lifted from the cans: oxblood #370E0C, cream #FEF9F3, olive #6A8767, mustard #DABD96,
  brick #AA4922, wine #641B31. One condensed flared display face in uppercase for headlines and the
  manifesto paragraph; nav, footer lists and inputs in a plain sans.
- A fixed kit of collage devices, repeated: product renders wrapped in circular text paths; single
  words boxed as stickers ("SPIRIT FOR THOSE" in brick, "RITUAL" in mustard tilted ~3°); small photo
  pills inlined in the manifesto ("GHIA WAS BORN FROM [photo] A SIMPLE IDEA"); a wavy edge between
  the dark hero and the cream body; ghosted line drawings at ~8% behind text; five fanned recipe
  cards each with an outline sticker icon and a bullet list ("Craft Journey", "Botanical Craft");
  a giant script logotype closing the footer.
- Lesson: maximalism with a system: one display face, a palette taken from the product, four or five
  devices repeated; the noise is in the decoration layer while chrome and controls stay plain.
- Weak: the text paths are unreadable; the fanned cards crop their own titles ("Flavor Sto");
  inline photos break a four-line paragraph; "Fax" in the help menu.

## 208 INNO studio (Md Shakil) — web, purple + neon, MAXIMALIST NEGATIVE
- #331441 ground with diagonal stripes; "WE BUILD AI-POWERED DIGITAL PRODUCTS." in heavy uppercase
  with a cyan offset; a dashed-border pill "Top Rated on Fiverr · 4.9 (565 reviews)"; a pink→cyan
  gradient button with a yellow offset and a dashed secondary; a portrait in a magenta frame on a
  yellow block; sparkles, squares, rings and dots in five colours; stats "4.9 / 500+ / 9+ / 1hr" each
  in a different colour (#FF3AF2, #00F5D4, #FFD11E, #FF6B35).
- Kept as a NEGATIVE example: maximalism with no system. Every element has a different border
  (solid, dashed, gradient, offset), every number its own colour (142's rainbow tiles moved to
  marketing), confetti that means nothing.
- Note: the copy is honest (stats cite "per the Fiverr profile"); the failure is purely visual.

## 209 Founder Connects blog (Dima Strizhak) — web, warm dark + yellow, EDITORIAL / ZINE
- Warm near-black #232320; nav as small dark mono chips (MEETUPS, SQUAD, BECOME A HOST ▾,
  RESIDENTS, BLOG) and a white "Join WhatsApp Group"; "THE BLOG" in a heavy condensed grotesk ~90px
  over a two-line mono subhead.
- Featured post as a cream card: photo, chips "Building & Growth" and "Dec 20, 2025", condensed
  headline "HOW TO GET UNSTUCK WITHOUT HIRING ANOTHER ADVISOR", mono dek, full-width yellow #E0BF07
  "Read more". Handwritten yellow marginalia either side ("No SEO bait. No hot takes for clicks.",
  "Written by founders, not copywriters.").
- Category filter row in mono over a dotted rule; a three-up grid (chips, condensed headline, mono
  dek, film-graded photo) with the non-focused headlines dimmed grey.
- Lesson: a zine voice for a community: condensed display + mono body; the brand's stance said in
  handwriting, twice only; dimming the unfocused cards turns a grid into a sequence.
- Weak: three faces, one over the two-face rule (it survives because the script is two asides);
  dates out of order (Feb 2026 between Dec 2025 posts); mono body at ~13px tires beyond a dek.

# Applications and onboarding (230-242)

Collected 2026-10-27 for the applications and onboarding pattern area. Searches: onboarding app, KYC
verification app, identity verification UI, sign up flow, loan application form, multi step form,
document upload UI, account opening app. 28 candidates, reviewed one by one: 11 kept, 2 kept as
negatives, 15 rejected (tilted or rendered mockups, mostly-photo heroes, generic carousels, typos,
thumbnails too small to read). Unused numbers 243-254 are free. These are the evidence for
`references/patterns/applications-and-onboarding.md`; the form-craft and regulated-copy entries are
flagged.

## 230 Dribbble sign-up (Dribbble) — web, white + illustration panel, SIGN-UP
- Shipped product, not a concept. Split 2:1: a white form column and a full-height illustration panel
  (grainy pink/blue creatures) that carries the only colour on the page. Form column centred:
  logo mark, "Welcome to Dribbble" in bold, a two-line value sentence naming the benefit
  ("connecting with millions of top designers").
- Identifier-first: one outlined pill "Continue with Google", an "or" divider, ONE
  email field, a black filled pill "Continue with email". No password, no name, no confirm field on
  the first screen. Lesson: ask for the identifier only, decide the method (password, passkey,
  magic link, SSO) on the next screen.
- Legal line under the button in small grey type with two underlined links ("Terms", "Privacy Policy");
  "Already have an account? Sign in" sits well below it. Lesson: consent and the
  other path are present but quiet; neither competes with the primary.
- Weak: the email field has placeholder text and no visible label; no error state shown; the social
  button is visually heavier than it needs to be next to the primary.

## 231 Zevoa password reset (Orbix Studio LLC) — mobile, near-white + black, OTP / RECOVERY
- Three screens: "Forgot Password?" with a six-box code input, the destination number in bold under
  the heading ("(303) 555-0105"), the system numeric keypad; the same screen filled (9 4 9 6 9 |)
  with the black pill "Verify" now enabled; "Reset password" with the rule stated ABOVE the fields
  ("minimum of 6 characters with a mix of…"), New / Confirm fields with eye toggles.
- Code boxes ~52pt square on a 390pt screen, 6 across with ~8pt gaps; the active box white with a
  green caret, the rest outlined. "Didn't receive the code? Send Again" sits under the button, bold
  verb.
- Lesson: show where the code went, give the resend path on the same screen, state the password
  rule before the user types, offer show/hide on every password field.
- Weak: buttons stay grey and disabled until the input is complete (no reason shown, poor contrast);
  no resend countdown or expiry; a confirm-password field the show toggle already makes redundant;
  a 6-character minimum is below the 8 GOV.UK sets; no "wrong number? change it" route.

## 232 Untitled UI intake step (Jordan Hughes) — web, white + black, SIGN-UP / SUPPORT RAIL
- Two-panel card: a grey left rail (~30%) of support routes, each a title + one-line promise + a
  contact with a copy icon: "Chat to sales", "Email support" ("within 24 hours"), "Chat support"
  with a green "● Online" chip, "Call us" with hours and a UTC offset. Social icons at the foot.
- Right: logo, "What do you need help with?" (~28px), one grey sub-line, then a 2x3 grid of choice
  cards (icon in a 40px rounded square, title, first-person one-liner: "I need a website built.",
  "I want to understand users."), and "Something else" as the escape option. "Go back" outlined pill
  left, black "Continue" pill right.
- Lesson: on an intake or application step, help is a permanent column with response times and
  opening hours, not a "Need help?" link buried in the footer. First-person option copy reads as
  the user's own words.
- Weak: two cards are selected but both show filled RADIO dots; multi-select needs checkboxes. No
  progress indicator; the rainbow frame is presentation only.

## 233 Book summary personalisation (Tonmoy Das) — mobile, white + black, ONBOARDING
- Three onboarding questions, each: a segmented progress bar of four sections where the current
  section fills partially (position within section), a pill chip naming the section ("Goals",
  "Profile"), a two-line question (~28pt), one grey sub-line, the control, a full-width black
  "Continue".
- Minutes picker: a wheel with 13-17 min, "15 min" set at ~36pt in a grey selection band, then a
  live consequence below it: ▲ "329" in a tile, "Books per year". Lesson: a personalisation answer
  shows what it buys immediately; the number is the reason to answer.
- Book swipe: a card fan with No ✕ (grey) / Yes ✓ (black) as two half-width buttons; topic chips
  with "+" glyphs, the selected chip inverted to black ("Time-Management").
- Weak: screen 2 reuses screen 1's sub-line verbatim ("Choose a time that fits your daily
  routine"); the "Like time" chip is unclear; 15 minutes a day for 329 books a year is not credible;
  Title Case questions; no skip on any screen.

## 234 Blockfy KYC set (finterface) — mobile, dark navy + electric blue, KYC / CAPTURE
- Grid of dark screens (several cropped at the frame edge): country list with flags and radio
  circles (Germany selected with a blue fill), "Select Your Preferred Identification Type" as three
  chevron rows (Passport / Driving License / National ID Card), a "How we use your data" link and a
  key glyph over "Your data is completely secure…".
- Capture screen: live camera over the card, a dashed rounded rectangle as the target, a "⏱ Please
  hold still" status pill above it, "Move your ID inside the rectangle." below, a white ~80pt shutter.
  Lesson: capture guidance is two layers, a live status pill that changes (hold still, too dark,
  glare) and a fixed instruction.
- "Biometric Setup" with a large fingerprint glyph, "Scan Fingerprint" + "Skip This Step"; a Face ID
  opt-in "Yes, Use FaceID" / "No, Maybe Later"; a processing screen ("We are processing your plus
  membership trial…"); thin segmented progress with "Skip" top right.
- Weak: "Mexiso" typo in the country list; a "Passcode" screen (HIG says avoid that word for app
  authentication); the processing screen has no time estimate; near-duplicate 25108727 (same author,
  same ID chooser) rejected in favour of this one.

## 235 Airzon identity sheets (Airzon Agency) — mobile, near-black + silver, KYC / IN-CONTEXT
- Three dark bottom sheets (~20pt radius, round ✕ top right) over the app, which stays visible
  behind a heavy blur. Lesson: verification as a sheet keeps the user's place; closing it returns
  them to the task that triggered it.
- "Select your age": "16" at ~60pt over a ruler with ticks and a ▲ marker, eligibility stated under
  it ("You must confirm you are 15+"). "Verify your identity / Pick a document to confirm." with a
  document card that carries its requirement ("Ensure it's valid and not expired").
- "Submit Proof / Upload a clear photo of your ID." with a sample licence in corner brackets and a
  scan line; silver gradient pill "Finish verification". One heading, one sub-line, one control,
  one button per sheet.
- Weak: document choice is a one-card carousel with 4 dots (a list shows all options at once); age
  by slider is self-declared and needs a non-drag alternative (GOV.UK, WCAG 2.5.1); no capture
  quality checks or processing state shown.

## 236 Freedom Finance loan comparison (Emma McGrath) — web, white + navy/cyan, APPLICATION / REGULATED
- Application: a vertical stepper rail (Your Loan ✓ / Income 2 / About You 3 / Address 4), "Your
  Loan" with a one-line reason for asking. Each question is a bold line with a green ✓ once answered;
  purpose as a 2-col grid of radio cards; amount as six preset tiles (£1,000-£25,000, selected filled
  navy) plus "£ Enter another amount" and a range line; term as tiles with months in brackets
  ("2 years (24 months)"). Help sits in the right gutter beside each question, not under it.
- Results: navy left rail restating the inputs ("£5,000 over 5 Years") with ± steppers and "Update";
  "Good news Jane, you have 4 offers…"; sort chips (Lowest Repayments, Lowest APR, Chance of
  Approval); each offer a row of cells: lender + Trustpilot, Interest £1,297.23, Total Repayable
  £6,297.23, Representative APR (the one tinted cell), £188.30 per month + green "Continue", and a
  "75% Chance of Approval" tab.
- Lesson: a UK credit quote shows APR, total repayable and a representative example on every offer,
  the example in a quiet grey band under the row, never hidden behind a link.
- Weak: the figures disagree (8.9% APR in the cell vs 9.9% in the example; £188.30 a month vs
  £104.95); placeholder "£XXX and £XXXX" in the range hint; "infomation" typo. In a regulated quote
  these are compliance failures, not polish.

## 237 Loan application, mobile (Yuri Ternytsky) — mobile, white + yellow, APPLICATION / LIVE TERMS
- Step 1 of 4 (four short yellow bars): question left, answer right at ~36pt ("$5000", "6 mos."),
  min/max under each slider ("from $1000 / to $10000"), a calendar glyph with the end date ("till 21
  Dec 19"). A bordered "Loan information" box recalculates as you drag: amount, "6 × $833.3",
  next payment date, "View payment schedule".
- Step 4 "Confirm loan": check-your-answers as editable underlined fields (name, address, a
  same-address checkbox), a bordered "Credit information" block with amount, term dropdown,
  payments, monthly payment, next payment, purpose; a declaration checkbox bundled with terms.
- Lesson: the cost of the choice updates live beside the control; the final step restates every
  number the user will be held to.
- Weak: the step-1 button says "Submit" and the final one says "Next" (backwards); "currenly" typo;
  "$833.3" with one decimal; no APR, total repayable or fees (a regulated credit screen needs them);
  intro promises a credit card on a loan form; sliders for money need a typed alternative.

## 238 Ziemann multi-step booking (Kristina Broceta) — web, white + black, APPLICATION / STEPPER
- Left rail (~30%, tinted grey) with a vertical stepper of six steps, each a title + one-line
  description (Vehicle Info / Retailer / Services / Date & Time / Personal Details / Confirm); current
  step a filled black disc, the rest outlined.
- Main: "← Back" outlined button, "Step 1/6" eyebrow, "Vehicle Info" at ~36px, sub-line; a two-column
  section: left a heading + why-we-ask paragraph + "How to scan VIN Number?" link, right the fields.
  "VIN Number" (filled, clear ✕) OR "Registration Number" side by side; brand, engine, model, year,
  colour as prefilled dropdowns ("LC9X (Deep Black Pearl)"). Black "Next" bottom right; outlined
  "Scan VIN Number" top right.
- Lesson: one identifier fills five fields; the explanation column says why the data is needed; the
  stepper's descriptions tell the user what each later step will ask.
- Weak: the black disc on step 1 is indistinguishable from a "done" state (no ✓ style shown); ~40%
  of the main panel is empty; primary bottom right while Back is top left.

## 239 BuildStream job application (tonik) — web, white + violet/yellow, SHORT APPLICATION
- Square-cornered panels; a three-step horizontal stepper (numbered violet disc for current, yellow
  ✓ for done, grey numbers ahead) repeated on each panel. Inline-label fields ("Location: city,
  area…") with a pin or search glyph at the end; "SUGGESTIONS" as letter-spaced micro-label over
  outlined chips (Manchester, Liverpool, Leeds…).
- Roles as 2x2 radio cards: title, two-line description, a grey chip with a money glyph
  ("from £30 per hour"). Step 3 shows earlier answers as filled rows with a violet ✓ ("Roles: 360
  Operator, Steel Fixer"), then the new fields; "Certification (optional)" over a dashed dropzone
  ("Click to upload or drag and drop").
- Lesson: mark the optional field, not the required ones; carry answers forward as completed rows
  the user can reopen; a pay chip on each option answers the question before it is asked.
- Weak: examples live in placeholders ("e. g. John Smith"); the outcome screen is a thumbs-up and
  "reach out to you in a days" (typo, no date, no reference); radio dots on a multi-select step.

## 240 Newable business finance documents (STX Next) — web, white + navy/cyan, DOCUMENT UPLOAD
- Presentation collage (laptop frame cropped, stepper zoomed), but the UI is flat and readable. Six-
  step stepper: Loan details ✓, Business details ✓, Applicant's details (3, active, white card with a
  notch), Property details, "Step Five (Optional) Your plans for the business", Required documents.
- Documents page under the product name ("Property Backed Business Finance (Interest Only)"):
  formats and size limit stated first ("size limit 15mb per file") as three icon groups (images /
  documents / spreadsheets); then ONE dropzone per named requirement ("Business bank statements of
  the last 3 months", "Most recent statutory and management accounts"), each "Drag and drop file
  here or UPLOAD FILE".
- File row: file glyph, name, "Uploading…", a thin progress bar, ✕ to cancel. Lesson: a slot per
  document the underwriter needs, with requirements first, beats one generic dropzone and a list.
- Weak: "John Smith"; "15mb" should be "15MB"; uppercase outlined buttons; no uploaded, failed or
  replace state shown; the collage crops the right edge.

## 241 Paytech sign-up (Nixtio) — web, black + red, SIGN-UP / FORM CRAFT
- Kept as a NEGATIVE example: the visual is strong (red brand panel with barcode bars, white/orange
  lines, a "Reward BTC +0.289047 · Pending" card, a 3-line ~56px headline) and the form craft
  under it is broken. Peak styling does not rescue a form.
- Heading "Sing Up Account" and sub-line "Enter your personal date" (two typos in the two largest
  lines); the email field is red with "Enter a valid Email" while it holds a valid address; the
  error uses "valid" (GOV.UK bans it) and does not say what is wrong.
- The primary on a sign-up form says "Buy BTC"; the password has a hint ("Must be at least 8
  characters") but the email has none; no terms line. Lesson: proofread the two largest strings,
  write errors that name the fault, label the button with the action it performs.

## 242 Cashio onboarding carousel (SK RADWOAN) — mobile, milky lilac gradient, ONBOARDING
- Kept as a NEGATIVE example of first-run onboarding: three carousel slides, each a lilac gradient
  top, a cloud of category icons or invite rows as the picture, a centred title + two-line body,
  pagination dots, and the same full-width "Get Started" on every slide.
- Copy and picture disagree: "Invite Other People" over a body about connecting bank accounts. No
  skip, no sign-in path, nothing the user can try; the value is described, never shown.
- Milky lilac/violet with a purple pill is the generated-UI palette (`anti-slop.md`). Lesson: replace
  the slides with one screen that does the first task (connect an account, see a real number) or
  with personalisation questions that change what the user sees next (233).

# App chrome (255-272)

Collected 2026-10-27 for the chrome pattern file (`patterns/app-chrome.md`). Searches: settings page,
command palette, search results, filter UI, notifications, empty state, modal dialog, inbox, file
manager, user profile settings, data table filters. 35 candidates reviewed one by one: 16 kept, 2 kept
as negatives (271, 272), 17 rejected (`review.tsv`). Numbers 255-261 are search and the palette,
262-264 filters, 265 settings, 266-267 notifications, 268 empty state, 269-270 profile and account,
271-272 negatives. Unused numbers 273-284 are gaps.

## 255 Global search, two states (Shift Studio) — desktop overlay, white + lavender, SEARCH RESULTS
- One overlay shown twice: zero results and results. Input row: search glyph, query, then "Clear" (empty
  state) or an outlined "✦ Ask ai "Climate"" button (results state), an expand-to-full-page icon and
  a close ×. Under it a segmented scope bar (All · Horizon · Knowledge · Actions · Reports, each with
  an icon) and a separate "⇅ Most Relevant" sort button on the right.
- Results grouped with a count in the heading ("Pages in Horzion (6)"); each row: doc icon in an
  outlined square, title with the match on a lavender tint pill, a two-line snippet that also
  highlights the term and truncates with an ellipsis, relative age right ("1d", "13d", "4mo").
- Footer key hints: ↑ ↓ "To navigate", ↵ "To select", esc "To close". Zero state: icon tile, "No
  results found for "Derivatives"", one grey line.
- Lesson: highlight the match in title and snippet, put scope and sort on one row as two different
  controls, and offer a handoff (AI, full page) inside the input row rather than below the fold.
- Weak: typos ("Horzion", "Try adjusting you search"); the zero state shows the placeholder "Type
  here" while naming the query, and offers no way out (clear scope, check spelling, ask AI).

## 256 Search Something (Farrel Putra) — desktop dropdown, white, SCOPE CHIPS + FALLBACK
- Pill input with "Edo" typed and ×; dropdown below: scope chips (Employee ✕ and Company ✕ outlined
  in black = on; Software, Files grey = off), then results grouped under letter-spaced caps
  (EMPLOYEE, COMPANY). Rows: large avatar or logo, name, email in grey, right-aligned counts
  with glyphs (comments 3, members 1, lists 5), a "Pro" tint chip on the company.
- Last block, inside the dropdown: "Not finding what you're looking for? Try our advanced search."
  with a "Try Advanced Search" button. Idle state on the right: "Search anything…" with a ⌘K keycap.
- Lesson: scopes as removable chips above the results, and the escape route to advanced search as a
  standing last row, not only on zero results.
- Weak: the scope chips sit under a heading "ACTIONS" (they are filters, not actions); no match
  highlighting on "Edo"; the oversized avatars waste a dropdown's height.

## 257 sandow search, pre-query (strangehelix) — mobile, white on orange, ZERO-QUERY STATE
- Full-screen search on a phone: back glyph, outlined search field "Search for a workout…", filter
  icon right. Below, before any typing: "Recent Search" as five rows (clock icon, "25 Minute Cardio
  Pilates", "10 Minute HIIT Beginner"…, a ↖ arrow at the right edge, hairline separators), then
  "Top Categories" as six outlined icon chips (Yoga, Strength, Endurance, Pilates, Speed, HIIT), then
  "Browse All" photo tiles.
- Lesson: the empty search screen is a menu, recents first; the ↖ arrow means "copy into the field to
  refine", a different action from tapping the row to run it.
- Weak: cropped presentation shot; no "Clear" for recents and no per-row ×; the photo tiles are stock
  and repeat the category chips.

## 258 Flytkt flight results (Fixoria Studio) — desktop, black chrome + white, RESULTS PAGE
- Black top bar with a wide global search whose placeholder names the keys it accepts ("ex.
  PNR/Name/Ticket No/Booking Ref…") and a ⌘K keycap. Page: "← Flight Results", then the query kept
  editable as a card (One Way / Round Trip / Multi City radios, From ⇆ To with a swap button, dates,
  "2 Passenger, Economy", black "Modify Search").
- Under it an airline price strip (logo + "USD 980.00" ×7 with ‹ ›), a sort segmented "Cheapest"
  (black) / "Fastest", filter dropdown chips ("Direct / Connecting ▾", "Airline ▾", "+3 ▾"), and
  List View / Table View. Count as a sentence: "102 Available Flights from 20 Airlines".
- Result card: airline + flight numbers, depart 16:50 / "1 Stop DXB" on a dotted arc / arrive 20:50,
  fare stack right (Total Fare $1,080 · Commission $80 · Agent Fare $1,000), condition tags
  (Refundable green, Non-Refundable orange, Book & Hold, Partial Payment), "Flight Details ▾" + black
  "Book Now".
- Lesson: on a results page the query stays visible and editable, sort is separate from filter, the
  filter row overflows to "+3", and the count is a sentence with its scope.
- Weak: every fare is USD 980.00 and every flight 16:50-20:50; results dated 20 Dec for a 25 Nov
  search; typos ("Qater", "Transections"). The anatomy is right, the content is placeholder.

## 259 Results table with pivot panel (Never Before Seen) — desktop, white, SIDE PANEL
- Two states. Header "Results 7" with a count chip; toolbar: wide search, "Columns" and "Pivot"
  buttons. Column headers carry both ⇅ sort and a filter glyph. Country cells with round flags,
  numbers right-aligned and tabular, a bold "Total" row.
- Right side panel (about 30% width), not a modal: "Pivot Mode" toggle and ×, field search, a field
  list with + per field, then three accordions Rows / Columns / Values with dashed "Drag here to
  create rows" drop zones. Pivot on: rows collapse to Europe / North America / Asia / Others with
  chevrons; the panel shows "Rows 3" and a checked "Region".
- Lesson: configuration whose effect the user needs to watch (columns, pivot, grouping) goes in a
  non-modal side panel beside the data, never a modal over it.
- Weak: "Results 7" over 11 rows, and the totals do not add up (shipments sum to 4,430, shown as
  4,230; Asia pivots to 50 for three countries of 50). Check sums in any results mock.

## 260 Smart search palette (Brandby) — desktop overlay, warm grey, COMMAND PALETTE
- Palette about 60% of the frame width, soft shadow on a warm grey ground. Query "Si" set large with
  a caret; filter and × icons right. First row, pre-selected on a grey fill: "✦ Smart search" with a
  "⌘M" keycap.
- Group "Actions" first: "Assign to Simon Prusin" (avatar, built from the match), "Assign to…" [A],
  "Un-assign" [U]. Group "Keyword" below: person + email, "Sign up flow · Notion Page", "Sign up flow
  Design · MSP-10" with a status glyph. Matched characters sit on a grey box, per character (S, i).
- Footer: ↑ ↓ "Navigate", ↵ "Confirm", esc "Close" as keycaps on grey.
- Lesson: actions above navigation, an action composed from the match ("Assign to <match>"), single
  -letter accelerators shown right, and the keyboard contract printed in the footer.
- Weak: "Keyword" says nothing about the group; every issue has the same green check whatever its
  state; single-letter keys need a stated rule for when they fire (list focused, not input).

## 261 Command palette, light (Dmitry Sergushkin) — desktop overlay, white, PALETTE + SOURCES
- Input "Start typing here…" with a ⌘A keycap and an AI sparkle. Two scope levels: source tabs (All,
  then about 11 connected-app logos and a +) and type chips (People, Task, Pages, Files, Docs,
  Messages, Images fading out at the edge), plus filter and sort icon buttons.
- Groups with counts: RECENT (people: avatar, name • email, comment count right), FILES 4 (PDF / CSV
  / DOC type badges, title • category, "2.4 MB • Modified 2 hours ago by Sophia Jones", an
  open-in arrow right), QUICK ACTIONS (Create new task ⌘T, Create note ⌘N, Add member ⌘M).
- Footer: ⇅ Select, ↵ Open, ⌘R Open in new tab, ⌘L Copy Link, ESC Close, settings gear.
- Lesson: a pre-query palette is recents + files + quick actions, each group counted; the footer
  lists secondary verbs on the highlighted row, not only navigation.
- Weak: "RECENT 3" heads four rows; example.com addresses; eleven full-colour logos make the scope
  row the loudest thing in the overlay.

## 262 Filter panel, light and dark (Rabbani Rasha Alvy) — side panel, white / near-black, FACETS
- A narrow panel, "Filter" with funnel icon and ×, a search field, then collapsible facets each in
  its own rounded block: Category as radios (All / Laptops / Smartphones ● / Accessories), Brand
  as 12 wrap chips (Apple ✓ and Google ✓ filled violet), Availability as one toggle ("In stock
  only"), Storage as checkboxes (512 GB ✓), Price Range as an 8-stop slider with $500 / $900 value
  pills, Color as five swatches with the selected ringed and its name in text ("Purple"), Sort by ▾.
- Same panel in dark with identical anatomy; the violet holds on both.
- Lesson: the control follows the facet: exclusive → radio, many short values → chips, boolean →
  toggle, ordered sizes → checkboxes, numeric → range + typed values, colour → swatch plus its name.
- Weak: no result counts per option, no Apply / Clear all, no summary of what is active when facets
  collapse; Sort does not belong inside Filter.

## 263 Faceted filter modal (Volodymyr Lazariev) — desktop modal, white + green, HIGH CARDINALITY
- Modal over an energy dashboard. Top strip: Date (08/08/2023) and Time available (Shoulder / Off
  -peak / Peak). Then four facets as white blocks: label left, a per-facet search field, "Select
  all" tint button, kebab, collapse caret. Options are bordered checkbox tiles, eight per row;
  checked tiles turn pale green with a green tick.
- High-cardinality facets cap at two rows and end in "Show 7 more" / "Show 15 more"; Tags adds "# Add
  tag". "Reset" appears only on the two facets that have selections (Entity, Site). Footer: text
  "Cancel" + green "Apply filters".
- Lesson: for facets with dozens of values (site IDs), search inside the facet, cap visible rows,
  show the remainder count, and show per-facet Reset only where something is set.
- Weak: placeholder data ("Customer1", "Underfined", "Power Plant 1" twice, "green_net" twice); no
  running total of matches on "Apply filters"; "Select all" on every facet is noise.

## 264 Condition builder (Foyez Ahmed Kawsar) — desktop popover, white + orange, ADVANCED FILTER
- Under a view bar (View List · Filters active · Project Status · Tags): rows "Where: ⋮⋮ [Owner ▾]
  [Is ▾] [Davon ▾]" and a bin icon. An "And" pill with a bracket line joins a nested group card "Any of the
  following are true:" holding "Order Is Confirmed" (value as a green status chip) and an empty
  "Select / Select / Select" row, with "+ Add another" and "Clear owner's all".
- Footer: "Add another condition ▾" left, "Clear all" text and orange "Apply filter" right.
- Lesson: when filters need AND/OR, write them as sentences (field · operator · value) with drag
  handles and one visible nesting level; values keep their own chip styling.
- Weak: "Clear owner's all" is garbled; the empty row is not flagged as incomplete; one nesting level
  is the useful limit and the design does not say so.

## 265 Business hours settings (Dmitry Sergushkin) — desktop modal, white + black, AUTOSAVE ROWS
- Modal header: clock in an outlined square tile, "Business hours", helper "Control how this phone
  number works at different times of day", ×. Rows separated by hairlines: label + grey helper left,
  control right. Master "Enable" toggle (black when on); "Timezone (UTC-08:00) Pacific Time ▾".
- Seven day rows: toggle + day + From / To fields (09:00 AM - 5:30 PM). Saturday and Sunday off:
  toggle grey, day label grey, fields read "Closed" with a moon icon. Two sub-flows as rows with outlined "Set Up"
  buttons: "Outside business hours — Route callers who dial outside hours", "Create whitelist".
- No Save button: each control commits on change.
- Lesson: settings row = label + one-line consequence + control; the off state is written as content
  ("Closed"), not just a greyed input; sub-flows open from a row, they do not inline.
- Weak: "09:00 AM" beside "5:30 PM" (two time formats); no "Copy Monday to all"; autosave with no
  "Saved" acknowledgement anywhere; "whitelist" (prefer "allow list").

## 266 Workel notification centre (chakir) — desktop popover, white + blue, ACTIONABLE INBOX
- Popover over a blurred, dimmed workspace. Tabs with counts: All 2 · Request 14 · Mentions 2 ·
  Urgent. Row: avatar with a type badge (comment, invite, task, folder, event), a sentence with
  actor and object in bold ("Yahya Commented on Fix this front end"), context and age right
  ("Workel / 15min ago").
- Each row embeds its object: a quoted comment with a reply glyph; an invite with Cancel and black
  Accept inline; a task card (checkbox, title, assignee, "2 days"); a folder path "./Project/
  Folder-Name ›"; an event card with time and stacked avatars "4+".
- Unread: grey tint, a thin blue left bar, blue dot on the avatar. Footer: "Mark all as read" left,
  "View all" right.
- Lesson: a notification is actor · verb · object + a preview of the object + the one action it asks
  for, done in place.
- Weak: typos ("Resuest", "10::00", "Alexendar"), placeholders ("Project name", "Folder-Name"),
  every row "15min ago" and four of five from the same person.

## 267 Notifications, mobile (Mateen Haider) — mobile, pale grey + blue, READ / UNREAD
- Title "Notifications" with a blue count 3 and a "Clear All" link. Day groups in caps: TODAY,
  YESTERDAY, THIS WEEK. Cards: tinted icon circle or avatar, bold title, two-line body, time
  right.
- Unread cards: pale blue fill, a blue left bar, time in blue ("2m ago", "1h ago"); read cards
  white, time grey ("4h ago", "Yesterday", "Mon"). Specific copy: "order #2458", "New login detected
  from a Chrome browser on Windows 11 in Seattle, WA.", "$450.00 from Upwork Inc."
- Lesson: unread is three cues together (fill, bar, coloured time), never colour alone; group by day;
  write the specific object and amount into the body.
- Weak: count 3 but two cards marked unread; the security alert has no "This wasn't me" and the
  invite has no Accept; "Clear All" with no undo.

## 268 Coinstax empty portfolio (Rizki Mulyawan) — desktop card, near-black + lime, FIRST-USE
- One centred card on #0b0b0b with dashed layout guides. "Your portfolio is empty" + "Let's get
  started with your first portfolio". Primary route as a card with a lime-to-green gradient border
  and gradient wallet icon: "Connect your wallet", one sentence, "Supported Networks ▾".
- Secondary routes grouped in one bordered card: "Connect Binance account", "Connect OKX account",
  each "Securely sync assets from your … account". Last resort as a white pill: "+ Add transactions
  manually".
- Lesson: a first-use empty state is the list of ways to get data in, ranked (one recommended, the
  rest grouped, manual last), with no illustration.
- Weak: rows have no chevron, so clickability rests on the border; "Simply" is filler.

## 269 Customer profile modal (Untitled UI, Jordan Hughes) — desktop modal, near-black, RECORD + FORM
- Cover strip, a large avatar overlapping it with a verified badge, outlined "Archive" and "View orders"
  top right. Name + "● Subscribed" chip, email under it.
- Stat strip, four cells split by hairlines: First seen 1 Mar, 2025 · First purchase 4 Mar, 2025 ·
  Revenue $118.00 · MRR $0.00.
- Form rows, label column left (~30%), control right: Name as two fields; Email with a mail icon and
  "✓ VERIFIED 2 JAN, 2025" under it; Country with flag ▾; Username with an "untitledui.com/" prefix
  addon and a verified tick. Footer: Cancel / Save changes.
- Lesson: a profile is facts first (stat strip), then editable fields with their verification state
  and date attached to the field, not in a separate panel.
- Weak: "Save changes" is a dark grey, not the primary; email verified on 2 Jan before "First seen" on
  1 Mar; the cloud photo is decoration.

## 270 Account and edit profile (Safayet Hossain) — mobile, black + acid yellow, ACCOUNT HUB
- Three screens on a black base with a blurred pink-blue glow at the top. Account: profile card
  (avatar with camera badge, name, email, "PRO" gradient chip, full-width yellow "Edit Profile"),
  then grouped lists with headings: Account (Manage subscription, Restore purchases) and Preferences
  (App settings, Privacy & Security, Notifications, Language), rows with icons in circles.
- Avatar step: circular crop over the photo, a "− + Reset" zoom pill, "Select Another Photo" outlined
  and yellow "Confirm".
- Lesson: the mobile account hub is identity card + two or three titled groups; "Restore purchases"
  belongs beside the subscription; cropping is its own step with zoom and reset.
- Weak: Edit Profile shows Email empty and a "Confirm Password" field with nothing to confirm; Cancel
  is as heavy as Save (black filled); → arrows where iOS uses chevrons.

## 271 Mobile modal "system" (Orbix Studio) — mobile overlays, white + yellow isometric, NEGATIVE
- Kept as a NEGATIVE example. Nine centred modal cards, each an isometric yellow illustration, a
  title and one grey line, and not one button: "Video Uploading…", "No Messages", "New Followers",
  "Unblock Wade Warren", "No Wishlist Items Yet!", "No Transactions Yet", "Mentor approval Done",
  "Link Copied!", "Blocked wade warren".
- Five different jobs (progress, empty state, confirmation, success, toast) forced into one modal
  shape. An empty list does not need a modal; "Link Copied!" is a toast; "Unblock" is a confirmation
  with no confirm.
- Copy pasted between cards: "Blocked wade warren" carries the body of "No Transactions Yet" ("Keep
  track of your purchases, refunds and exchanges here"); lower-case name in one title, title case in
  the other.
- Lesson: choose the surface by the job (inline, toast, banner, dialog) before styling it; a modal
  with no action is a dead end the user must dismiss.

## 272 slothUI file manager grid (Samuel Oktavianus) — desktop, white + violet frame, NEGATIVE
- Kept as a NEGATIVE example. Greeting header ("Good Morning, Azunyan!", "188 gb · Pro Member · 78%
  Space Left", Share + violet "Go Pro"); five category tiles (Video 77.8 gb, Audio 98.8 gb, Documents
  100.2 mb…); twelve folder cards (icon, name, "118 files · 2.8 gb"); "Newest First ▾", "Grid View ▾";
  pagination 1-5 … 99.
- The numbers cannot be true: Video and Audio alone are 176.6 GB of a 188 GB plan with "78% Space
  Left"; "Cheat_Codes 8.8 tb", "Images & Gallery 998 tb", "Projects 77,4487". Units lower-case.
- Missing what a file manager is for: no breadcrumb, no search, no upload or drop target, no list
  view with modified date, owner or type; folders paginated to 99 pages.
- Lesson: in a file manager, sizes must add up to the quota, and the list (name, owner, modified,
  size) is the product; cards and pagination are for browsing, not managing.

# Commerce and marketing (285-300)

Collected 2026-10-27 for `references/patterns/commerce-and-marketing.md`. Searches: pricing page,
checkout page, subscription checkout, ecommerce product page, ecommerce website, shopping app, cart
ui, comparison table ui, saas landing page. 33 candidates, 16 kept (14 references + 2 negatives).
Numbers 301-309 are unused. Several keepers are kept for their anatomy despite arithmetic or copy
errors; the errors are listed in each entry because checking money is part of the lesson.

## 285 Threekit pricing (Brass Hands) — web, dark forest + three pastel tier blocks, PRICING + COMPARISON TABLE
- Dark green page, nav with one outlined "Get in touch". Headline "Simple pricing" in two tones
  (white, then grey) at ~140px, about 10x the body. A three-line product statement ("Your Visual
  Commerce Toolkit") holds the left column; three plan cards sit to its right in terracotta, slate
  blue and sage: name, one "Best for…" line, price ($60k / $112k / $160k), black pill "Get started".
- "Most Popular!" white chip hangs off the top edge of the middle card. "Key Features" table below:
  bold row labels left, one column per tier, check discs filled in each tier's own hue, an en dash
  for not included, hairlines between generous rows, an asterisk footnote on the first row.
- Lesson: the tier colour is the column key. Carry it from the card into the table so the eye never
  re-reads the header. Pastel block colour (`stances.md`) done with saturated fills and black type,
  not the milky set.
- Weak: prices carry no period or billing basis (per year? one-off?); three identical "Get started"
  buttons, so the popular plan is marked only by a small chip; "Most Popular" is a claim that needs
  data behind it in a real product.

## 286 Upgrade plan (Dipa Inhouse) — web, white + pale blue glow, RECOMMENDED PLAN
- Centred "Choose Your Plan" + one-line subhead; segmented billing toggle "Bill annually [10% OFF] |
  Bill monthly" with the saving as a blue chip inside the annual option. Three cards: Basic $10 /
  Pro $25 / Enterprise $50 "/month", an audience line ("For growing teams that need smarter
  workflows."), "What's included:" with 5-6 check rows.
- Pro is marked four ways at once: a "Recommended for you" tab fixed to the top of the card, the
  card ~30px taller than its neighbours, a blue outline with a soft glow, and the only filled button
  (navy "Start with Pro"). Basic and Enterprise get grey tonal buttons; Enterprise says "Contact Sales".
- Faint line drawings in each card's top-right corner and a + grid on the page; the glow behind Pro
  is the one lit place.
- Lesson: one recommended plan, marked by position, height, outline and the single filled CTA, plus
  a label in words.
- Weak: with annual selected the prices still read "$10/month" and no yearly total is given; "10%
  OFF" does not say off what. Write "$108 billed yearly, save $12".

## 287 AI writing tool pricing (Alamin Hossen) — web, grey + black, CUMULATIVE TIERS
- Eyebrow chip "Our Pricing Plan", headline "Get started for free" (~64px). Each plan is two layers:
  a raised white card with name, description, price and CTA, set inside a grey tray that holds the
  feature list. Starter "Free Plan" / Pro "$8.00 /Month" / Team "$12.00 /Month".
- Lists are cumulative and say so in grey small caps: "GET STARTED WITH", "EVERYTHING IN STARTER",
  "EVERYTHING IN PRO"; each list then carries only what the tier adds (5-6 rows), checks as black
  discs.
- The CTA verb matches the plan: "Download for Windows" with the Windows mark on the free tier, black
  "Go Pro Plan" with a drop shadow on the recommended tier, tonal "Get Started →" on Team.
- Lesson: "Everything in X, plus" keeps each list short and makes the step up legible; the button
  says what actually happens next.
- Weak: the same description pasted on all three cards, with "monthly free" for "fee"; no billing
  toggle; the recommended plan is marked only by its button.

## 288 Pricing sections (Jordan Hughes, Untitled UI) — web, dark grey, COMPARISON TABLE + FAQ + PROOF + FOOTER
- Five browser-framed sections in one system. Pricing: announcement chip ("We've just partnered with
  Coinbase · Read →"), "Pricing plans" + "Try our basic plan risk free for 30 days. Switch plans or
  cancel any time."; cards $24 / $48 / $96 "per month" with white "Start free trial" / "Get started".
- Comparison table: header "Features · Basic plan · Business plan · Enterprise plan"; each row label
  has a (?) tooltip; cells are green check rings, an em dash, or words and numbers ("10 / 20 /
  Unlimited", "20GB / 40GB", "Basic / Advanced"); rows grouped under section headings ("Reporting and
  analytics"); ~44px rows, no zebra.
- FAQ: centred title + scope line ("…about Untitled UI and billing"); questions with a 40px outlined
  icon square each, first one open; they are the questions asked at the price (free trial, change
  plan later, cancellation policy, invoice details, billing). The list fades under a blur into a
  "Show more" pill.
- Testimonial: five stars, a three-line quote at ~28px, 32px avatar, name, role and company. Logo
  strip "You're in good company" with faded edges. Footer: logo, one-line description, six social
  icons, four link columns under small grey labels.
- Lesson: the full set of below-the-fold pricing sections held in one quiet system; the comparison
  table uses words and numbers where ticks would hide the difference.
- Weak: no recommended plan; the blurred questions are unreadable to everyone, including screen
  readers; the testimonial has no logo or link that would let anyone verify it.

## 289 FootWear marketplace (Nija Works) — web, white + orange, PRODUCT CARD + FILTER BAR
- Utility bar (Start Selling / Help Center / Download FootWear App / English), search pill with a
  real example as placeholder ('try "Nike Air Jordan"'), cart chip "2 Items", user. Two promo cards,
  then "Today Best Deals!" with an orange countdown chip "Ends in: 12 : 10 : 09".
- Card: 1:1 grey image tile, round heart top-right (orange when saved), name truncated to one line,
  "★ 4.9 · 652 Items Sold", was-price struck in grey, now-price ~20px bold; "Rp 819,000" formatting
  held across 20+ cards; corner labels "Just in" / "Sold out" as orange text, not chips.
- Filter bar above the grid: brand (with its mark) ▾ · Price ▾ · Size ▾ · Type ▾ | "More Filter":
  the four attributes that decide a shoe inline, everything else behind one button.
- Lesson: a card is image, save, name, rating + sold count, was/now price, and nothing else.
- Weak: every rating is 4.9; the sold-out card still looks buyable; copy errors ("Shop Now, Goodlook
  Later"); two promo banners and a deals carousel come before the filterable listing.

## 290 Zerolock camera PDP (Sayeed Ahmad) — web, white + navy, BUY BOX
- "Ship to: USA ▾" in the header (country sets price and delivery before anything else); breadcrumb
  Home › Accessories › Camera; gallery ~840px wide with arrows and five thumbnails, the last a video
  with a play glyph.
- Buy box: condensed display name at ~44px over two lines, ★★★★★ "4.8 (1.2k)" linked to reviews, a
  two-line pitch with "Read more ▾", $89.00 with $115.00 struck, then three icon lines: "Free
  shipping", "30-day money-back guarantee", "15 in stock".
- "Choose Your Package" radios with the saving after a dash in grey italic ("2-Pack Bundle – Save
  10%"), quantity stepper, full-width navy "ADD TO CART", and under it "Instant setup · No technical
  skills needed". A six-feature icon strip on a grey band follows.
- Lesson: cost, stock and the way back sit between price and button as three short lines, not
  inside accordions.
- Weak: quantity "5" beside a package radio is ambiguous (five cameras or five packs?); "Free
  shipping" with no date; bundle savings without the bundle price.

## 291 emox marketplace PDP (Musemind) — web, white + royal blue, DELIVERY PROMISE + COMPARE + BUNDLES
- Dense marketplace PDP: brand eyebrow "SAMSUNG", three-line title, "★ 4.9 (2.6k) · Compare";
  capacity as two price-bearing tiles (256GB $999.99 selected / 512GB $1,119.99), colour as named dot
  chips; "From 999.99 AED"; instalment line "As low as $45/mo with tabby tamara Learn how"; full-width
  blue "Add to cart".
- "Add Protection Plan" (2-year / 3-year). "How you'll get this item": two tiles, Shipping "Free ·
  Arrives Feb 20" (selected) and Pickup "Not available"; then "Sacramento, 96898 Change · Arrives by
  Fri, Feb 20 · More option", "Sold and shipped by Samsung" with seller stars, free shipping and
  "Free 30-day returns" each with a Details link.
- Below: six spec tiles (Screen Size 6.8 in, Weight 218g…); "Compare with similar products", five
  product columns with attribute rows set large ("6.8 in", "200 MP", unit small); "Frequently bought
  together" with tick boxes, "Now total" and "Add 2 item cart"; similar items.
- Lesson: fulfilment as tiles, each with its own date, and a postcode the user can change, is the
  strongest delivery promise in the batch.
- Weak, and the reason to read it closely: currencies mix ($ on the variant tiles, AED on the
  price); a US postcode under a UAE flag; checkboxes for an either/or plan ("Only one option can be
  chosen at a time"); the bundle "Now total" ignores the second ticked item; one struck was-price is
  lower than its now-price; the product being viewed is missing from its own comparison.

## 292 Cira furniture PDP (LAIN) — web, warm bone + espresso, EDITORIAL PDP + SPEC TABLE
- Bone (#f3ede6) page, espresso type, centred monogram logo, four uppercase nav items pushed to the
  edges. Gallery ~580px square + four thumbnails; buy column: grey eyebrow "Lounge Chair", uppercase
  grotesk "OSLO LOUNGE CHAIR", $2,000 struck / $1,290, two paragraphs, quantity, espresso "ADD TO
  CART" + outlined "BUY NOW", numbered accordions "01 Details / 02 Care / 03 Shipping & Returns".
- "CRAFTED —— MATERIALS" split display heading (~64px, a rule between the words); spec table in
  groups (PRODUCT, DIMENSIONS, CONSTRUCTION), grey label left, value right, hairlines, dual units
  "84 CM (33.1 IN)".
- Three text reviews with name and role/city; related products with name, material line
  ("Seating · Oak & Woven Linen") and price, one card taller than the others; closing panel over a
  photo ("FIND THE PIECE THAT FEELS AT HOME.") with two buttons; footer with newsletter, three link
  columns and a full-width "CIRA PRO" wordmark.
- Lesson: an editorial stance carries a PDP when the facts are set as a table; the split heading and
  the giant wordmark are the bespoke moves, the spec table is the substance.
- Weak: no fabric or colour choice, no stock, no delivery estimate; reviews without a rating, count
  or date read as testimonials; ADD TO CART and BUY NOW compete at equal width.

## 293 Camping gear PDP (tubik) — web, sage + black, BRAND-LOUD PDP
- Split 50/50. Left, a sage panel: "TWO TONE DYEING SWEAT SHIRT" in condensed black caps at ~150px
  over two lines (about 12x the body), a one-line description, tabs MATERIAL / DETAIL / SIZE CHART,
  a composition table ("SHELL [1] COTTON 100%"), S / M / L squares with M outlined, "$90" at ~48px,
  full-width black "ADD TO CART" in the same condensed face. Right, a full-bleed editorial photo.
- Nav is three words: CAMPING GEAR, MENU, CART [0]. Orange grain gradient outside the page.
- Lesson: on a single-product brand page the product name can be the hero, as long as every decision
  (size, price, button) still sits in one column under it. Same studio and same loud rules as 007.
- Weak: the active tab is marked by an orange scribble through it, which reads as "crossed out"; no
  stock, delivery, returns or reviews; sizes have no availability state.

## 294 Fashion store app (Peno Lab) — mobile, white + black, MOBILE PDP + CART THRESHOLD
- Three 390pt screens: home (greeting + "Discover products you'll love", search + scan, promo,
  category circles, "Deals of the Day" with a 08 : 45 : 32 timer), PDP, cart.
- PDP: carousel with dots, name + "25% OFF" chip, $59.99 with $89.99 struck, "★ 4.9 (200 review)",
  four colour swatches with the selected one ringed, description + "Read more", three feature checks,
  then a bottom bar: quantity stepper (− 1 +) beside a black "Add to Cart" taking ~60% of the width.
- Cart: green banner "You've unlocked free shipping!" with a full progress bar and the "$40"
  threshold; three items with a variant line, trash icon and stepper; promo field; Subtotal $269.97,
  Discount −$90.00 in green, Shipping "Free", Total $179.97; black "Proceed to Checkout".
- Lesson: the free-delivery threshold drawn as a progress bar turns a hidden cost into a goal; on the
  PDP, quantity and add-to-cart share one bottom bar within thumb reach.
- Weak: "Minimal Backpack" is pictured as a clutch purse; rows show sale prices while the subtotal
  is at list price and the discount is subtracted again below, so the saving appears twice.

## 295 Saffra cart (Sayeed Ahmad) — mobile, cream + orange, CART STATES
- Three states of one cart. Header: back, "Cart", trash; a three-step progress (Menu ✓ → Cart 2 →
  Checkout 3) as discs on a line. Merchant row "Zayt & Za'atar · Arrives in 25–35 min · 1.2 km ›".
- Items as cards: photo, name, modifier line ("Extra garlic sauce"), €8.90, stepper in a pill;
  "+ Add more items"; "Popular with your order" as three add-on tiles with a + disc each.
- Sticky footer: "Total incl. fees" over €24.60 at ~28px, orange "Go to checkout". Empty state: icon,
  "Your cart is empty", one sentence, "Browse restaurants", "Recently ordered from" + three thumbs.
- Removal: dark toast "Baklava removed · Total updated · UNDO"; the footer shows €24.60 with the old
  €29.10 struck. The sums hold (€8.90 + €11.20 + €4.50 fees = €24.60; with the €4.50 baklava, €29.10).
- Lesson: design the cart's three states (filled, empty, just changed) and make a change reversible
  and visible in the total.
- Weak: "incl. fees" without naming the fees; the struck old total after a removal reads as a
  discount.

## 296 Infinite UI checkout (Ekaterina Motyleva) — web, light grey + blue, PAYMENT STEP
- Breadcrumb stepper "✓ Shipping Details › 3 Payment Method › 4 Confirmation"; ~700px form card left,
  ~550px summary stack right.
- Payment as radio cards: PayPal, Credit Card (selected and expanded in place: Visa / Mastercard /
  Amex + "+4", card number with a card glyph, MM / YYYY, CVV/CVC with a (?) tooltip, cardholder
  name), Buy Now Pay Later, Cash on Delivery; each method's mark on the right. Tick box "Save my
  information for a faster checkout with a Shop account". Full-width "Pay | $107.02".
- Summary: "Your Cart (7)" rows with × remove, stepper and price; gift-card/promo field + Apply;
  Subtotal $77.60 / Tax $15.52 / Delivery $13.90 / Total $107.02. The sums are right and the button
  repeats the total.
- Lesson: the chosen payment method expands where it was chosen; the pay button carries the exact
  amount; the order stays editable beside the payment step.
- Weak: step 2 is missing from the stepper; "(7)" items against 4 units; "Promo Code of Gift Card";
  default blue; no delivery date, returns or trust line near the button.

## 297 Dolens subscription checkout (Luxera Agency) — web, forest green split + white, SUBSCRIPTION CHECKOUT
- Stripe-Checkout anatomy. Left half dark green with a 45° hairline hatch: back arrow + logo,
  "Subscribe to Gorgo standard", "US$ 19.99" at ~80px with "Per month" stacked small beside it, the
  allowance line ("Unlimited contacts, 500 Messages per month").
- Plan row "Dolens Standard · Billed monthly · US$ 19.99" with an attached sub-row: switch + green
  chip "Save $200" + "with annual billing" + "US$ 1,149.99/year". Then Subtotal, "Add promotion code"
  link, Tax (i) US$ 0.00, "Total due today US$ 19.99"; footer © · Terms · Privacy.
- Right, "Pay With Card": Email, Name on card, one grouped card field (number with brand marks /
  MM/YY / CVC), billing country (flag) and address as one grouped field, a bordered opt-in "Securely
  save my information for 1-click checkout", dark green "Subscribe", and a three-line mandate under it
  ("…charge your card for this and future payments… You can always cancel your subscription").
- Lesson: "Total due today" is the right label for a subscription total; the annual switch sits on
  the plan row with the saving stated in money.
- Weak, and worth checking every time: 12 × $19.99 = $239.88, so $1,149.99/year cannot "save $200";
  the brand changes from Dolens to "Gorgo" in the first line.

## 298 Tare refill plan (Luke Pyrzynski) — desktop (front-on monitor mockup), cream + near-black + lime, SUBSCRIPTION SUMMARY
- Left: eyebrow "REFILL PLAN", headline "Set It Once, / change it whenever" (serif, second line
  italic green), "Pick your formula" as radio rows: 40px product thumb, name, size + one-line use
  ("250ml. For a barrier that reacts to everything"), price right; the selected row has a 2px black
  border.
- Right: near-black card "YOUR PLAN · Barrier Repair Cream"; rows "Glass jar, one time $20" and
  "Refill, every 8 weeks $38"; rule; "Due today" with "$58" in serif at ~40px; "Then $38 every 8
  weeks, which works out to about $0.68 a day."; lime pill "Start this plan ↗"; "Skip, pause or
  change the schedule any time. No minimum."; a "WHAT THIS AVOIDS" note with grams of glass saved.
- The maths holds: $20 + $38 = $58; $38 over 56 days = $0.68.
- Lesson: a recurring charge is two numbers, today and then, with the cadence in words and the way
  out stated beside the button. The dark summary card is the one inverted element (as 092, 046).
- Weak: shot inside a monitor mockup; a serif headline with an italic second line is on the
  generated-UI signature list (`typography.md` §5); a per-day framing of a price needs Compliance
  review in a financial product.

## 299 Skipa subscription checkout (Krevix) — web, white + purple — NEGATIVE
- Kept as a NEGATIVE example: the anatomy is right (payment radio cards with the card form expanded
  in place, "Pay $112.00" in the button, a plan card with an offer chip, a renewal paragraph that
  names the charge, the end of the offer term and the refund cutoff) and the numbers are wrong.
- "20% Off for 12 month" turns "$200.50 / mo" into "$100.00 / mo" (a 50% cut); Sub Total $90.00 +
  Vat/Tax (10%) $10.00 = $100.00, but the bold line, labelled "Sub Total" again, says $112.00, and so
  do the button and the legal text. The header email reads "Info@johndoe@gmail.com"; the card mandate
  names "Domestikar Inc.", not Skipa.
- Lesson: every figure in a checkout appears three or four times (plan card, breakdown, button,
  terms). Generate them from one source and check them by sum. A wrong total inside the legal
  paragraph is a misstatement, not a typo.
- Worth keeping: the renewal paragraph's order (amount incl. VAT, cadence, when the offer ends, the
  refund cutoff date, how to cancel, two links).

## 300 PioMart marketplace template (ThemeTags) — web, cream + teal + orange — NEGATIVE
- Kept as a NEGATIVE example of listing slop: every card, whether a watch, a phone, a chair or a pet
  product, is titled "Wilson Ultra Power XL 112 Tennis Racket" at "$1,899.00 $1,994.05"; "Supper Sale
  50%" twice; an announcement bar and four promo tiles before the first product, and more between rows; a
  countdown in four red boxes; filter chips
  "Up to 90% off / Under $1 / Almost Sold out".
- Lesson: a listing with placeholder names and one repeated price cannot be judged at all (as 028:
  uniform rows break the spell). Urgency devices stacked without a real deadline read as pressure.
- Do instead: real names and varied prices, one promotion slot above the grid, filters before
  banners.

# Content, social and AI patterns (310-324)

Collected 2026-10-27 for the content area: feeds, profiles, messaging, AI chat, AI agents, media
players, maps and reading. Searches: social media app, feed app ui, profile page app, messaging app,
ai chat app, ai agent dashboard, music player app, map app ui. 31 candidates, 15 kept (13 references
+ 2 negatives, 317 and 319). No music or video player passed (tilted, hand-held, glass art or
skeleton content), so media players are evidenced from platform docs only. These entries are the
evidence for `patterns/content-social-ai.md`.

## 310 Feed redesign (Diana Larussa) — desktop, white + network blue, FEED (desktop)
- Three columns of about 300 / 660 / 380px: an identity card left (cover, avatar, "UI Designer for
  AI & SaaS Products", Profile viewers 145 ▲12%, Post impressions 204 ▲38%, then Saved items / Groups
  / Newsletters), the feed centre at reading width, "Top stories" and a network card right.
- Composer first ("Start a post…" with Video / Photo / Write an article), then a hairline with
  "Sort by: the newest ▾" right-aligned. Ranking is named and changeable, not implied.
- Post card: 40px avatar, name • "2h ago", role line, "+ Follow" or "Following" right; real
  multi-paragraph text with line breaks and three hashtags; a reaction stack of three glyphs + "Garry
  and 1,200 others" left, "86 comments • 14 reposts" right; hairline; four equal verbs Like /
  Comment / Repost / Send.
- Top stories: headline + one grey meta line "12 min ago · 11,071 readers". Lesson: recency and
  popularity belong in one quiet line under a headline, and the feed column stays narrow while the
  side columns carry identity and news.
- Weak: every post "2h ago" and both reaction lines start "Garry and…"; Follow vs Following differ
  only by a small + icon; the loudest element on the page is the filled "See who's hiring" ad.

## 311 Social app (Piqo Studio) — mobile, white + black + one yellow, FEED + CREATOR PROFILE
- Header "Following / For You" as text tabs with a yellow underline, yellow round search. Stories as
  tall ~3:4 photo cards instead of circles, each with a state chip (black "Live", yellow "Premiere")
  and a viewer count ("20.5K"), author avatar and name on a scrim at the bottom.
- Trending card: full-bleed photo, author name + handle on the image, three glass engagement pills
  on the image (♡ 120K, ↺ 96K, ➤ 36K). Counts sit on the media; nothing trails below the card.
- Creator profile: ~120pt avatar centred with "2.5M Followers" and "120 Following" flanking it;
  name, handle; segmented "Post 25 | Reels 34" with the counts in nested chips; a resurfacing row
  "24 videos in your drift · Take a look" with an avatar stack; 3-column 9:16 grid with ▷ play
  counts (20.5K, 45.9K, 534.4K).
- Lesson: one saturated accent carries only the active tab, the create button and the selected
  segment; counts are abbreviated one way everywhere (one decimal, K/M).
- Weak: posts carry no time at all; the profile has a back button and bell but no Follow or Message,
  so it is unclear whose profile it is; the third story is cut mid-name.

## 312 ConnectWorld (Kretya) — mobile, white + blue, FEED CARD + COMMENTS + SHARE SHEET
- Story rings (own story first, a 1px divider, then others), filter pills My Feed (filled) / LIVE /
  Friend / Explore. Post card: avatar, username + verified tick, location "San Francisco", ⋯ in a
  circle; photo with carousel dots on the image; "Liked by ryangildan and 22 others" with a two-avatar
  stack; outlined count pills ♡ 6,525 · comment 23 · share 23; bookmark alone at the right.
- Comments sheet: grabber, centred title, rows of avatar, bold username, comment, "Reply" link, heart
  + count at the right (the liked one filled red, "2"); six emoji quick reactions above "Add comment"
  with the viewer's avatar.
- Share sheet: grabber, search, 4-column grid of recent contacts with truncated handles, then a
  horizontal row of round targets (Add Story, Copy link, Facebook, Instagram, Threads).
- Lesson: engagement detail opens in sheets over a dimmed feed (comments, share), so the reader
  never loses their place.
- Weak: comment and share counts identical (23 / 23) reads as template data; the external row is
  cut at the edge with no scroll cue; default blue with no stance.

## 313 Social feed (Nodus Labs) — mobile, dark warm brown + orange, REELS + FEED + PROFILE
- Full-screen reel: tabs Feed / Following / Reels at the top (active bold + dot); a right rail of
  author avatar with a red +, ♡ 1.2k, comment 1k, share 1.1k, save 1k; bottom-left name + verified,
  hashtags, "♪ Dopamin so…" sound credit; a spinning disc thumbnail bottom right. The short-video
  anatomy: verbs on the thumb side, credit bottom-left, nothing over the face.
- Feed cards: rounded media with a glass author pill on the image ("@Krismosley (2h ago)"), ⋯ in a
  glass circle, the same vertical rail inside the card, caption bottom, segmented carousel progress.
- Profile: cover photo, avatar overlapping its edge, name + grey "Edit" chip, one-line bio, four
  stats split by hairlines (205k Followers / 110 Following / 90 post / 11.3k Likes), icon-only content
  tabs (photos, videos, private, liked, saved), 2-column masonry.
- Lesson: in video-first feeds the actions are a vertical rail with counts under each icon, and the
  same rail travels from full-screen to card.
- Weak: "90 post" (lowercase, singular) beside "Followers"; hashtag spam (#foryou #foryoupage) as
  caption; the orange gradient + competes with the photos; device frames.

## 314 Group chat (Cansaas) — mobile, dark warm gradient brown→rose, MESSAGING
- Group thread header: group avatar, "Visit Denpasar", members "Akbar, Fawzy, Khai, Kira, Musa,
  Smi…" truncated; video, call, ⋮. Runs from one sender: name in a tan accent on the first bubble
  only, avatar beside the last bubble only, one time label ("8:16PM") above each run.
- Outgoing bubbles black, right, no avatar; incoming dark translucent. A media message as a fanned
  stack of three photos with a "+2 photos" chip and reaction chips (🔥 3, ❤️ 2) hanging off the corner;
  "@Rohmad" mention in the accent.
- Chat list: large title "Chats"; square story thumbnails with count badges; filters All / Favorites
  / Work / Groups / Communities; previews with sender prefix ("Khai: Are they still open at sunday?"),
  "You:" + image glyph for media, blue double ticks for read, a pin, a red unread badge, an orange
  presence dot, relative times ("24 mins").
- Contact screen: three stat tiles (Message 12,145 / Group 94 / Spaces 48), "Media and photos" strip
  with "+42", rows Notification / Media visibility / Bookmarked / Lock Chat toggle.
- Lesson: group by sender and by time, not per message: name once, avatar once, time once per run.
- Weak: the composer floats over and blurs the newest message; "5mins" vs "2 mins", "8:16PM" with no
  space; the settings group repeats; the gradient sits behind every screen rather than one region.

## 315 Messages (Huge Binary) — Android / Material 3, sage + lime, MESSAGING (list states)
- Thread list: search field with the user's avatar inside it, filter chips All (lime) / Contacts /
  Finance / Unknown; two-line rows with avatar, name + red count badge (15, 2, 12, 99+), truncated
  preview, time right ("Now", "8:05 PM"); extended FAB "Start Chat".
- Selection mode: the long-pressed row tints, and the bottom bar becomes a contextual bar "✕ 1" with
  block / archive / delete. Count + bulk verbs replace navigation while selecting.
- Conversation: header is an avatar stack of other open chats with badges plus video / call / ⋮;
  date separators "Tuesday, Jan 12" and "Today"; outgoing lime bubbles; incoming grey with the avatar
  on the run; "10 min" under the run; smart-reply chips (Yay! / Congratulations! 👍 / Ok) above the
  composer; composer pill with SIM-slot glyph, emoji and +.
- Lesson: a thread list has three designed states (browse with filters and badges, select with a
  contextual bar, compose from the FAB); smart replies sit above the composer, never in the thread.
- Weak: previews repeat ("Some great new colours", "A new material?") and every time is "8:05 PM";
  the FAB covers the last row; delete has no undo shown.

## 316 Agento support inbox (Mohammad Saju) — desktop, white + slate, MESSAGING (desktop) + AI LABELS
- Four panes: nav (Inbox, Teams, Integrations, Knowledge, AI Center, Automations), inbox views (Open
  / Awaiting 5 / Snoozed 2 / Overdue SLA / Resolved 12) and channels with counts (Email 6, WhatsApp,
  Slack 16, Shopify 4, Stripe 2), the thread, and a right panel with Profile details / Tickets tabs.
- Conversation rows carry provenance chips: "AI gen." (the agent replied), "AI drafted" (waiting for
  a human), "Escalated" (red). AI involvement is a visible state before the thread is opened.
- Thread: both sides named with "22m ago"; a date separator "09 Sept, 2025"; customer in grey
  bubbles left, agent as plain text right with an initial avatar; an attachment card "Refund
  Processed #RF-23891" with a receipt thumbnail and a download button; composer "Type your reply…".
- Right panel: Assignee, email, Plan Premium ($29/mo), LTV $1,450, Joined Mar 2021, Priority High
  (red), Segment, Language; "Last payment $29 · Sep 8, 2025"; "AI Insights" block with a labelled
  "Summary: Double charge detected… Customer is frustrated but polite." and Status Resolved.
- Lesson: in team inboxes AI involvement is labelled per row in words, and the AI summary lives in
  the context panel, labelled, not inside the conversation.
- Weak: the three direct-message rows are the same customer and text; "John Ab" truncated in the
  header; a "Get 40% discount" promo in the nav; the customer's email shown in full.

## 317 Messages (Azmir Sheikh) — mobile, grey + black, MESSAGING · NEGATIVE
- Serif "Messages" title, search + filter, chips All / Contacts / Unknown / New, four rows each with
  an "8" badge; conversation with "Today,jun 14" and a time under every bubble.
- Kept as a NEGATIVE example: per-message timestamps with no run grouping, and out of order (12:43 PM,
  11:50 AM, 12:43 PM); typing shown as "Type...." in the list and "Type.." in the header instead of
  "typing…"; every unread badge is 8; previews repeat ("A place to slow down."); copy errors ("Hi! Im
  interested", "Can you meeting with tomorrow?").
- Lesson: the anatomy is right (presence in the header, attach / camera / mic in the composer) and
  the screen still reads as fake because the data is uniform and the states are mislabelled.

## 318 AI chat response flow (Keitoto) — mobile, white + periwinkle, AI CHAT
- Empty state: "Hi James, how can I help you today?" under an orb; intent chips Ask Anything / Create
  image / Code / Analyze / Brainstorm with coloured glyphs. Thread header is a breadcrumb "Text
  generate / Font recommendation" (mode / auto-title).
- Generating: a "··· Generating" pill where the answer will land, and the composer itself reads
  "Generating…" while the model works.
- Answer: labelled "Answer" with the model glyph; structured markdown (bold lead terms, a numbered
  option, bullets); an inline citation chip "1" at the end of the claim; a "Sources" block of cards
  below; copy and flag left, Rewrite and Share right.
- Composer: + attach, "Ask me anything…", mic and a black voice-mode button; model picker "✦ Lumina
  2.0 (beta) ▾" inside the composer; a dismissible "Upgrade to pro for unlimited usage" strip docked
  on top of it. A shared variant "James Workspace · 4 members".
- Lesson: an answer carries its own provenance (label, citation number, sources) and its own verbs
  (copy, flag, rewrite, share) directly beneath it.
- Weak: a rotated collage (study anatomy, not presentation); source cards show titles only, no
  domain, favicon or date, and the composer overlaps them; the orb repeats on every screen; the
  answer recommends Playfair Display, itself a generated-UI tell (`typography.md`).

## 319 Talkora AI tutor (Fireart Studio) — mobile, white + iridescent blue, AI CHAT · NEGATIVE
- Home with "Your Profesional AI Language Tutor", skill chips and four practice cards with % rings;
  a chat home dominated by an iridescent orb above "Let's Learn a New Language"; a speaking-practice
  thread with a play button on the AI reply, a "Suggestions" block of three follow-up questions, and
  a "Listening…" voice state with a waveform and ✕ cancel / ■ stop / ✓ done.
- Kept as a NEGATIVE example: the orb is the hero on two of three screens and says nothing about
  what the model can do; typos in the hero and in the suggestions ("Profesional", "Trevel the
  English", "treveling", "favorite trevel destinations", "player guitar"); three of four rings read
  92%; sparkles on the header button and the "In Progress" chip.
- Worth keeping: follow-up suggestions after an answer, a play control on spoken replies, an explicit
  three-control voice state.
- Lesson: AI slop is decoration where the evidence should be, and generated copy nobody proofread.

## 320 Agent control centre (Topnotch Studio) — desktop, white + one blue glow, AI AGENTS · APPROVAL
- Left column of agent cards: icon, "Scheduler Agent / Calendar Ops", status dot + word right
  (Pending Confirmation amber, Analyzing violet, Executing green). The pending one expands into an
  approval: "Confirm Meeting Schedule?", a two-line explanation ("Your Scheduler Agent has proposed…
  review the details and confirm to proceed"), the proposed object (Tue, Apr 16 · 10:00–10:45 AM ·
  +2 People · 3 Todo List · 60 Min) and Confirm / Decline.
- Running agents report progress in domain units: "Analyzing market trends · 124 data points
  processed", Confidence 92% with a sparkline; "Budget Used $120/$300" with the cap smaller and grey.
- Right: "Good Afternoon, Adom" + "3 agents active · 1 pending action" (state in the greeting line),
  date and time with zone; "AI is ready / Waiting for your instructions or voice command"; mode chips
  Fast / In Depth / Magic AI / Holistic / Canvas / Quizzes; composer with "Core Intelligence ▾",
  "Fast ▾" and mic.
- Lesson: agents are a list of runs with a status word each; an action with consequences becomes a
  card at the top that names the agent, the proposal with its values, and two verbs.
- Weak: "14:02 PM"; the proposal says 10:00–10:45 but "60 Min" and is dated a month before today
  (Tuesday, May 14); a "Starting" chip contradicts "Pending Confirmation"; two agents share one
  copy-pasted progress line; Confirm and Decline are near-equal; "John Doe"; the orb takes 40% of the
  screen to say "ready".

## 321 Molar AI (Korsa) — desktop, white + deep violet band, AI AGENTS · ACTIVITY LOG
- Header "Good morning, Dr. Bennett" + "Molar has handled 47 tasks this morning" (number in the
  accent) and an "All systems normal" pill right.
- Hero band, the one lit region: "AI AGENT · LIVE" chip with a waveform, "Molar is handling 4 tasks
  right now", task chips ("Calling 2 patients", "Drafting 2 claim"), three glass tiles (Tasks Today
  47 · 12 done · 12 to go; Time Saved 8.4h; Confirmed 98% · Awaiting Dr. Bennett).
- "AI Agent activity · Live · last 24 hours": one icon per verb, the verb bold first ("Confirmed
  Sophia M. via SMS for tomorrow 14:30.", "Drafted claim for Michael C. … ready for review.",
  "Rescheduled 1 patient from Tue 14:00 → Wed 10:30 (staff conflict).", "Follow-up sent to Olivia
  P. — day 7. Reply: …"), then "✦ AI agent · 2 min ago". Schedule rows say "AI reminder sent" or
  "Confirmed". The Ask panel uses an example placeholder ("e.g. 'Resched…'").
- Lesson: an agent log is past-tense verb + object + reason + actor + time, and work waiting on a
  human says so in the row ("ready for review", "Awaiting Dr. Bennett").
- Weak: progress bars on rates ("No-show rate 3.2% · Progress 3.2%"); "1 hours ago", "Drafting 2
  claim"; "Time Saved" captioned "AI reminders active"; "09.42" vs "9.43" in the Ask panel, which is
  cropped; patient names would need masking in production.

## 322 Avero agent builder (Repo Studio) — desktop, white + blue, AI AGENTS · LOGS
- Breadcrumb "Personal / My workflows / Customer support auto-responder ✎", "Export PDF ▾", filled
  Save. Tabs Editor / Executions / Evaluation: build, run history and evals as three views of one
  agent.
- Canvas: Chat trigger → AI Agent → four tools (OpenAI chat model, Session memory, Knowledge lookup,
  Code execution), each icon + title + type; floating toolbar ending in Hide Chat and a filled Execute.
- Bottom split: a test chat "Avero 2.1" whose last line fades out as it streams, beside a Logs table
  (Log level · Created at · Message) with Info blue, Error red, Warning yellow.
- Lesson: test the agent beside its log, and make every model or tool step a timestamped row.
  Compare 070 for the canvas and 103 for the event-log anatomy.
- Weak: nav cropped at the left; a component name leaked as a node subtitle ("AgentNodeCard");
  "Search anythings…"; log rows out of order (Apr 29, Apr 29, Apr 26) with no run ID, duration or cost;
  yellow "Warning" text fails contrast; the Error row describes a step, not what failed.

## 323 Hotel search map (Cuberto) — mobile, white + sky blue, MAPS
- Price pins ($92, $1,387, $2,999) as small filled capsules; the selected pin inverted to dark violet
  ($246); "120 hotels · Filters" at the foot of the map over a horizontal card carousel (photo, name,
  stars, "$246", "Booking.com $299" struck) that follows the selected pin.
- Filters: Clear top right, search, "Sort by $ > $$$", a two-handle price slider drawn over a
  histogram of prices with "$250–$300" and "Average price $298", star rows as checkboxes.
- Detail: "#7 BEST SPA" badge, date and guest chips (aug 2-4, 3 guests), "Expedia price $299 / night"
  struck against "Members price $150 / night" and "You're saving $149" in green; amenity icons in
  circles; address with a map snippet.
- Lesson: the pin carries the one number people compare, and the selected pin, the card under the
  thumb and the detail page are visibly the same object.
- Weak: an older collage, cropped at the edges and only 1600px; pins overlap with no clustering
  ($79 / $490 / $231); tab labels about 9px.

## 324 Trip planner (Farhan) — mobile, white + pastel map, MAPS · BOTTOM SHEET
- Map in the top half with place labels as white pills on a stem dot (Tabanan, Denpasar, Singaraja),
  floating round controls (layers, locate, photos, people, menu); a card sheet below: carousel of
  trip photos with the owner's avatar, "Trip to Bali ✓", "30 Aug . 06 Sep 2026 . 8 days", chips
  Planning / Expenses; an "8 days to plan" card.
- Long-press opens a menu over the dimmed map: Edit ›, Archive ›, Delete in red with a red bin.
- Stay detail: 1+3 photo mosaic with "08+", name + verified, "4.0 (8k reviews)", "Hotel · Ubud,
  Gianyar, Bali, Indonesia", Check-In 28 Aug — "6 Night" — 03 Sep Check-Out, "Directions · Navigate
  there ↗", black "Create Stay".
- Lesson: the map stays visible above a sheet that holds the list; destructive actions are split off
  by colour and position.
- Weak: the pins are place names, not the trip's own stops; "." as a date separator, "6 Night",
  "08+"; no grabber on the sheet, so it is unclear that it moves.
