# Design notes: 85 reviewed references

One entry per reference image in `../../reference/`. Numbers are fixed: where a reference was later cut,
its number is a gap and its file is in `reference/_rejected/`. `../assets/previews/map.txt` maps each
number to its file. Each entry records what the design does, what it teaches, and where it is weak.
These are observations, not rules; the rules distilled from them live in `principles.md`, `patterns.md`,
`anti-slop.md`, `platforms.md` and `tools-and-analytics.md`.

Numbers 001-025 are mobile apps. 027-083 are web-app dashboards (mostly banking, fintech, payments, SaaS).
086-100 are marketing sites and AI tool homes. 101-144 are analytics and tool dashboards (tool mode).

How to use this file: when a brief resembles one of these (a payments table, a balance card, a kanban, a
landing hero) read the matching entries for concrete anatomy before designing. Search by keyword
(e.g. "status chip", "treemap", "exchange", "stepper", "helper text").

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
