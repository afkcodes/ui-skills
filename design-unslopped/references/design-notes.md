# Design notes: 100 reviewed references

One entry per reference image in `../../reference/` (same numbering as `reference/INDEX.csv` order:
app-designs/dribbble, app-designs/behance, website-designs/dribbble-dashboards, website-designs/dribbble,
website-designs/behance, website-designs/awwwards). Each entry records what the design does, what it
teaches, and where it is weak. These are observations, not rules; the rules distilled from them live in
`principles.md`, `patterns.md`, `anti-slop.md` and `platforms.md`.

Numbers 001-025 are mobile apps. 026-085 are web-app dashboards (mostly banking, fintech, payments, SaaS).
086-100 are marketing sites and AI tool homes.

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
## 026 Team comms (Conceptzilla) — desktop, Slack-like
- Three-pane: icon rail → channel tree (nested with ↳) → thread → right info panel. Four columns and still calm because only text weight and 1px separators do the work.
- Right panel "Main info" as key-value rows with icons (Creator, Date, Status chip, Tags 13 ›, Tasks 4 ›); "Thread activity" as a tiny green heatmap strip; Members list with role chips tinted by department.
- Unread counts as small grey numbers right-aligned in the tree. Numbers, not red dots, for low-urgency counts.
- Message composer at the bottom with ghost "Discard" + solid black "Send".
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
## 031 FinSight (SpineEdge) — desktop, banking, sage green
- Monochrome sage palette; bars in two greens (income darker, expense lighter). Delta chips tinted green/red are the only non-green colours.
- Three KPI tiles with an icon in a tinted circle top-right and "Since Last Week" + chip. Card tile (My Card) is a pale green tile with chip icon, name, balance, EXP/CVV small.
- Four square action buttons under the card (Top Up / Transfer / Request / History), outlined.
- Daily Limit: "$2,500.00 spent of $20,000.00" + progress bar + 57%. Budget widget pattern.
- Transaction table has a "Note" column with 2-line grey descriptions and status chips (Failed red tint, Completed green tint). Sidebar groups with chevrons for Payments/Cards; Inbox has a count badge "21".
## 032 NeuroBank (Phenomenon) — desktop, dark navy + electric blue
- Sidebar has a profile card with date eyebrow ("MONDAY, MARCH 24") and greeting; nav below; promo card at the bottom. Sidebar as a mini-profile column.
- Top toolbar: "This Month" period chip left, "Manage Widgets" + solid blue "Add new Widget" right. Customisable dashboards expose widget management in the header.
- AI Insights card with a one-sentence insight ("Your Transaction Volume has increased by 5%") and dots pagination: insight cards are sentences, not charts.
- Balance Overview: number, delta chip, two meta chips (44 transactions, 12 categories), mini area chart with the current 3 days highlighted. Earnings: semicircle gauge with legend (Current / Month goal).
- Transactions table on dark: logo + merchant, masked card, date, amount; positive in green. Spending: category icons row + "+8".
## 033 Borea AI stock prediction (Ramotion) — desktop, dark, data viz
- Stat strip at top: four label/value pairs in one translucent bar (Market Cap 735.75B · Day's Range 284-289 ...). Horizontal key stats row.
- Chart card header: toggle "Prediction", Day/Week segmented, calendar icon; legend right: solid orange "Actual", dashed blue "Borea AI Prediction", two accuracy stats. Legend doubles as a scorecard.
- Confidence band (blue area) around the actual line, dashed projection after "today" marker. Tooltip shows Prediction vs Actual High/Low/Close with a score. Range selector row 1D…Max as text tabs.
- Y-axis labels right-aligned on the right edge; current value marker "142" in an orange tag. Financial-chart conventions respected.
- Fluid red/blue background art is contained BEHIND a dark card so the data layer stays flat. Decoration behind, data in front.
- Disclaimer copy bottom-left in small grey: legal text present but quiet.
## 034 Recruitment rounds (Olack-like) — desktop, HR SaaS, dusty rose
- Top bar as a row of soft grey chip-buttons (Search, Add person, Notifications, ⋯) + language + date picker + solid black "Create →". Toolbar actions as chips, one black primary.
- Breadcrumb above a big page title "Round"; filter chips right (All Departments ▾, Export, Filter).
- Round cards: metadata chips row (date range, 10 candidates, Completed/In progress with dot), title, avatars +5, black "View candidates →" button.
- Question list: numbered rows with edit/delete/drag handles; expanded item becomes an inline form (Prompt, Competencies ▾, Time, Level ▾, Guidelines textarea) with "Insert From Library" ghost + rose "Create New Prompt" filled. Inline edit-in-place pattern.
- Right rail: notifications list with icons, assigned interviewers avatars, draggable "Sections" list with duration/question counts. Department colours as small squares in the sidebar.
## 035 Payment dashboard widgets (Black Bulls) — dark violet, crypto
- Widget set on black: donut with hatched empty segment and a floating label chip; bar chart with hatched bars and a highlighted solid bar + tooltip; line chart card with Buy/Sell buttons; glass credit card; Exchange panel (two amount fields with currency selectors, swap button between, rate/fee rows, one violet CTA).
- Hatching used for "empty/other" everywhere — a texture, not a colour, for the inactive portion. Very good dark-mode trick.
- Exchange form: "Your Send / Your received" with Available balances right-aligned, swap icon on the seam. Standard but tidy.
- Weak: "Storage Statistic" in a finance set is filler.
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
## 038 Ollo Bank (Plainthing) — desktop, white, orange dot system
- Every card title has a small orange square bullet: a tiny repeated brand mark that unifies all cards.
- Sidebar: icon rail + text sidebar with section labels (HOME / FINANCE OVERVIEW / WEALTH STRATEGY) in small caps grey. Nested groups with chevrons.
- Balance card: number, black "Withdraw" button inline, delta chip, three currency pills with flags and %. Quick Actions as 4 bordered tiles with icon+label.
- Line chart with dual series and a dark tooltip (date, two values with coloured labels); range tabs 1D/1Week/1Month/1Year under the chart.
- Recent Activity rows: avatar, "To/From name", "Show Tracking ▾", amount, status chip (IN PROGRESS blue / COMPLETED green / CANCELED red) in uppercase micro text.
- Contract tiles with logos and "● Active"; "Create Contract" with three radio-card options (Fixed Rated / Pay As You Go / Milestone Based) each with a one-line description. Radio cards with descriptions > plain radios.
## 039 Borrower stats (Sogee?) — desktop, lending, heat gradients
- Arc gauge coloured by a red→green gradient with legend rows (state, dotted leader, amount). Dotted leaders between label and value keep rows aligned without a table.
- Choropleth heat map of Australia with a +/−/expand control stack and a 3-step legend (<60% / <40% / <20%). Map zoom controls as a vertical button stack.
- Funnel as a flowing gradient ribbon with % callouts above/below at three stages — a "stream" funnel. Pretty; legibility ok because labels are explicit.
- New Request Trend: three S-curves ending in coloured pills that name the series at the line end (Development / Investment / Build and Hold). Direct labelling at line ends beats a legend.
- KPI strip top-right: "120 req." with a small grey chip "$22.5 M" — count + money chip.
## 040 Personal banking (Nixtio) — desktop, mint + yellow
- Mint background, yellow balance card (the only saturated element), white everything else. The hero number gets the one loud colour.
- Balance card with currency conversion hint (1 USD = EUR 0.95 = GBP 0.79) and an eye-off icon; three text-buttons under it (Pay/Transfer/Receive) separated by hairlines.
- Currency tiles (Euro 0.97 / British Pound 0.82 / Swiss Franc 1.10) with coloured glyph circles.
- Dot-matrix bar chart ("Total Rate") with the selected column in yellow and a yellow callout — bars drawn as dot columns is a distinctive but readable texture.
- Right panel = a transfer flow: card selector pill, recipient row with "Change", big amount, meta rows (exchange rate, balance after transfer, fee $0.00 (free transfer)), note field, 3x4 numeric keypad, black "Send". Keypad on desktop is odd but the meta-rows are exemplary.
## 041 Payment widgets (Roohi) — dark + orange, crypto
- Same family as 035 but orange. "Premium Plan" gradient tile with white CTA, two small KPI tiles with chips, wallet card with currency dropdown, area chart, 4 tiny asset stats.
- Activity: Monthly/Yearly segmented + five day bars with % inside each bar. Portfolio tokens with chip filters and "Withers" buttons (typo). Exchange panel repeated.
- Lesson: a widget library should show the same component in two brand accents (035 violet, 041 orange) and otherwise be identical — that's a theming test.
## 042 Kanto client metrics (Gnyadek) — desktop, lavender, editorial
- Editorial header: small eyebrow "Unified Client Metrics" + huge display "All Client Data" left; a floating insight card right with a sentence in two weights ("This quarter, optimized workflows reduced manual checks by 27%"). Dashboard with a magazine headline.
- Date range as two date chips + "All Accounts ▾" right-aligned on the header row.
- Weekly stacked bars with a hover tooltip listing three categories with counts; "+31%" chip floating top-right of the chart.
- Three metric cards with a % and a status dot (green ✓, orange ✕), then a two-ended bar (Auto-cleared ↔ Under Review) with counts at both ends. Two-ended bar for a split.
- AI Assistant panel: chat with a file-upload bubble, model picker chips (GPT-5 / Docs AI / Finance AI), "+" and input with send. Assistant lives in the right column as a peer widget.
## 043 Shopeers e-commerce (Dipa) — desktop, blue, classic SaaS
- Header row: title left; date range chip, "Last 30 days ▾", "Add widget", solid blue "Export" right. The standard dashboard header formula.
- KPI tiles: title + icon top row, big number + delta chip, "vs. 14,653 last period" grey meta. Four identical.
- Total Profit card with a line chart and a nested "Customers" sub-card showing 3 segments with coloured underlines (blue/green/orange). Sub-card inside a card for breakdown.
- Most Day Active: 7 rounded bars with the max labelled above. Repeat Customer Rate: segmented semicircle gauge "68% On track for 80% target" + "Show details" button.
- Sidebar with collapsible "Finances" group (Invoices/Transactions/Reports indented with a vertical guide line) and a blue "Upgrade" promo card bottom. Orders badge "46" in green tint.
## 044 SugarCRM cases (RonDesignLab) — desktop, kanban, grey glass
- Kanban with 4 columns as outlined pill headers; cards = avatar + title + wait-time subline + a right-side icon (⋯ / clock / check) that changes by column. Column semantics expressed in the card's trailing icon.
- Pill tab filter (Pipelines / In Progress / Completed / Expired) with the active one black.
- Left icon rail with tooltipped icons; theme toggle (moon/sun) at the bottom of the rail.
- Bottom row: donut "Top Case Drivers" with legend %; three gauges "Case Metrics". Soft frosted-glass panels on a grey gradient — fashionable, slightly low contrast.
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
## 047 Fundora (Sujon Hossain) — desktop, blue, clean SaaS
- Sidebar with search (⌘K), grouped nav (MAIN MENU / FEATURES / GENERAL), active item black pill, badge count on Analytics, red "Log out", plan card at the bottom. Textbook sidebar.
- Earning/Spending overview cards with (i) info icons and "This Month ▾" period pickers per card. Spending Breakdown as a 3-segment bar with a legend of label + amount above.
- Cash Flow: filter chips (Income filled / Expense / Savings), bar chart with the hovered month highlighted and a tooltip "August 2025 : $8,689.20".
- Upcoming Bill & Payment: logo, name, date, chevron, amount, "Scheduled" chip; "View All" outlined. Tables use dot+word status chips tinted.
## 048 Salezy (Sajibur) — desktop, blue, e-commerce
- Nearly identical structure to 047 (same author family): KPI tiles with icon-in-circle + title + (i), number, delta chip + "From the Last month:". Shows the house template.
- Revenue Insights: Monthly/Yearly toggle (active black pill), hatched bars with the selected one solid blue + tooltip. Hatch = inactive months.
- Sales Overview: segmented arc gauge "70.8% Sales Growth", with Sales $ vs Target $ and a thin progress bar. Gauge + target row.
- Table toolbar: title left; search field, "All Category ▾", "Filter" right, inside a grey toolbar band. Status chips (Pending amber / Completed green).
- Tools section in sidebar lists integrations with logos (HubSpot, Zoho, Zendesk) + "Add New Tool".
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
## 051 Personal finance (Orbix) — desktop, periwinkle, playful
- Header: logo, search "Search or jump to ⌘K", right "Move Money ▾" + bell + avatar. Then greeting left and SIX action chips right (Send filled, Request, Transfer, Deposit, Pay Bill, Create Invoice). Actions as a chip row in the header, primary filled.
- Stacked cards widget: three coloured card edges peeking (Euro/Naira/Dollar with amounts) + "4 cards" chip + "+" button; wallet balance + delta. Card stack as a visual metaphor done compactly.
- Overview: two smooth lines (current/last year) with a dual-value tooltip; Monthly spending limit as a striped progress bar; Quick transfer avatars with the selected one ringed, amount + "Send".
- Transaction list as a plain 4-col text table without chips; Money movement bars with a date pill tooltip.
- Weak: pastel gradients + glow on the nav icon drift toward "pretty"; density is low for the screen size.
## 052 Alignify revenue analytics (Wolfpixel) — desktop, white + coral
- Five KPIs in one connected card divided by hairlines: icon, label, number; footer row with "↑ +3.5% vs last Year" in green/red. One card, five cells — stronger than five floating tiles.
- "Last updated: Feb 28, 2024 ⟳" chip in the header. Data freshness again.
- Cashflow line with a tooltip and a legend chip "■ Reimbursed $5,133"; "Time Interval: Monthly ▾".
- Revenue by Product Category: total, delta, a 3-segment bar, then legend rows (coloured pill, label, amount (%)). Segment bar + legend rows with amounts — the canonical breakdown widget.
- Donut with external leader-line labels; Sales Calendar with day tabs and meeting cards; horizontal bars with % right-aligned. Coral used in 3 tints (dark/mid/light) = monochrome data palette.
## 053 Payment widgets (Roohi 2) — dark + orange
- Billing & invoice rows: date, invoice id + amount stacked, client, status chip (Pending amber / Paid green), chevron. Stacked id/amount in one cell saves a column.
- Activity as a bubble matrix (size = volume) across M–S. Credit cards carousel with the centre card in focus.
- Same Exchange panel for the third time: the pattern is clearly a "house component". Weak typo "This Munt".
## 054 Financial analytics (Outcrowd) — desktop, DARK, blue accent, calendar
- Rounded-capsule bar chart: each month is a dark capsule track; the selected month filled blue with a "+12%" chip above and "$1048" inside. Capsule bars with in-bar value label.
- Period segmented (Weekly/Monthly/Yearly/Range) + a filter icon button. Calendar widget with today highlighted and a KPI "$1,434 ↑12.4%" beneath it.
- "How can I help you?" AI card: an "AI Summary" paragraph, two mini stat tiles with status chips (7 Stable, 25 Processed), and an "Ask me anything…" input. AI as summary + stats + prompt.
- Spending donut with legend; a one-sentence insight footer ("Most expenses come from Activity and Meals…"). Insight sentence under the chart = good practice.
- Invoices: "Payment Score" as a thin barcode-style meter with 76; rows with date + relative time ("in 1 week"), status chip, name, amount.
- Left icon rail with the active icon in a white rounded square. Dark grey (#1a1a1a) not pure black; borders are 1px lighter grey.
## 055 Payline transactions (Outcrowd) — desktop, white + lime
- Quick transfer widget: avatars, "From William Grace (You) 275.00 €▾", conversion line "1 € = 1.18 $", "To Anabel Smith 324.50 $▾", and a "Drag to continue sending" slider. Slide-to-confirm on desktop is odd but the from/to/rate layout is excellent.
- History table: sortable headers (Merchant ⇅ / Transaction Date ⇅ / Amount ⇅ / Status), merchant logo + name + category subline, full datetime, signed amount (red for negative failed), status chips with icons (✓ Completed teal / ✕ Failed red / ⏱ Pending amber), kebab. Chips with glyphs are faster to scan than colour alone.
- Payment volume: purple capsule bars with a tooltip. Lime used only for the active nav icon and "See All" link.
## 056 Finexa scheduled payments (Confidency) — desktop, white + violet
- Top nav as a pill group (active black); page title + two header actions: ghost "+ Create New Payment" and a gradient "✦ Ask Finexa" AI button. AI entry as a header button.
- Summary card: "Total Scheduled Amount −$3,089.99" with an eyebrow + helper line, then THREE nested mini-tiles (Upcoming This Month / Recurring 14 Active / Overdue 2 Payments) inside a grey well. Sub-tiles in a well, not floating.
- Donut with a dark tooltip (Subscriptions $2,325) and a legend of dots. Table toolbar: search + Export + Filter; status chips Complete/Pending; Actions ⋯. Monthly-subscription descriptions in the Type column.
## 057 Payments inbox (Orbix) — desktop, white, dense table
- Workspace switcher (Agency / Orbix Studio Team) at the top of the sidebar; nav groups with nested sub-items under Payments (Requests, Recipients, Wire Drawdowns, ACH Authorizations); "Workflows" section. IA for business payments.
- Page header: title + helper, right: ghost "Send Money" + black "Upload Bill". Tabs Inbox / Needs Approval / Scheduled / Paid; a forwarding email chip ("jamiesmith@gmail.com") and settings gear on the tab row.
- Table: due date, status chip (Completed green / Overdue red / Not due yet grey), recipient with a card icon, amount, invoice no, last update (date + time stacked). Rows 44px, hairline separators, zero decoration. The purest "work table" in the set.
- Promo card bottom-left (GlobalLink) with one black CTA.
## 058 Ficopay (Mohammad Ali) — desktop, lavender gradient tints
- Balance card with a soft gradient tint, delta chip top-left, eye-off toggle, Income/Expenses sub-tiles. "AI Insights" card: two plain-language sentences with a bulb icon each + "View More Insights" button. Insights as short sentences again.
- Quick actions as three tiles with a circular icon and label; Expense Breakdown donut with rainbow gradient (weak: gradient donut segments are hard to map to the legend).
- Sidebar has a "Recent Transaction" people list (avatars + names with presence dots) — contacts in the sidebar.
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
## 061 Payr rent payments (Outcrowd) — web + widget, light blue
- Tenancy widget: rows with a coloured header strip ("Rent Day: 24th — Due" pink / "Rent Day: 11th — Paid" blue / green Paid / amber Due), property name, amount + card dot, "Pay now" button. Row header strip coloured by status.
- Compact 2x2 variant with pagination "4 of 7 ‹ ›" and "Add a new tenancy +" footer. Widget designed in two densities.
- Dashboard: hero card "£2,050 · Rent Day: 11th · Pay now" with soft radial tint; points card "24.600"; Payments table with card logos and status chips (Processing / Failed / Succes[sic]).
- Tenancy filter at the card header: "Tenancy: ● Tenancy 2, ● Walker st, 3+ ▾" — multi-select summarised inline with coloured dots.
## 062 Payal payments (VALMAX) — desktop, DARK blue glass
- Hero band: huge "Total balance $375,928.00" with the decimals faded; four glass KPI tiles right (Net revenue, Revenue growth, Payment success rate 92.8%, Chargeback rate 0.72%). Payments KPIs that matter.
- Chargebacks bar chart with the selected bar in blue gradient + "1.0%" pill; Refunds gauge; Revenue area. Transactions: a segmented semicircle gauge coloured by outcome with a 4-item legend (Successful 90.6% / Hard declines / Soft declines / Disputed) — payments funnel as a gauge.
- Recent rows: card brand logo, masked number, date, signed amount. Three blue action buttons (Transfer ↗ / Request ↘ / Swap ⇄). Blue gradient background with light streaks is decorative but contained under the cards.
## 063 Buildly growth analytics (Delisas) — desktop, DARK, orange
- Workspace dropdown "Growth Team" at top of sidebar; nav with count badges (Data Sources 12, Alerts 3). Header: search, orange "+ Add Data", bell with badge.
- Five KPI tiles: icon square top-left, delta chip top-right, label, number, "Prev: $210,450" grey. Prev-value instead of a % is clearer for finance.
- Dual-axis line chart (Revenue $ left, Conversion % right) with a legend below and range pills (24H/7D/30D/90D). Dual axes labelled on both sides.
- "Strategy Simulator" card with three sliders (Price Change, Ad Budget, Traffic Increase) and live values — what-if controls on a dashboard. "AI Recommendations" as three cards with a confidence % chip and an "Impact" line in green/red.
## 064 FlowMail (Confidency) — desktop, white + violet
- KPI tiles with a kebab, number + delta chip inside a tinted pill (chip sits in a grey well). Header: ghost "New Campaign" + gradient "Create Automation"; "✦ Get AI Insight" button in the top bar.
- Campaign Performance: 3-series step/line chart with a dashed cursor and a tooltip listing three values; Campaign Types donut with a centre label callout; Top Automations as mini cards with % and a progress bar + two counts.
- Audience Growth bars with the selected one filled and a value pill; Recent Campaigns table with status chips (Active/Scheduled/Completed). AI Insights: two tip cards (icon, title, one-line) + "Open AI Assistant".
## 065 NadaPay payments table (Jubed) — desktop, white + lime
- Header: greeting + helper; right: avatar with "Business Account" role. Page title row with FOUR actions: outlined "Export" + three lime filled (Swap/FX, Payment Route, New Payment) — too many primaries; one should be filled.
- Tabs (All Payments active black / History / Payment Routes); search + "Add Filter" right.
- Table: checkbox, Payment ID (sortable), Customer (avatar+name), Amount in ₦ with negative shown with a minus, Payment Method as plain text, Date & Time, Status chip (Success / Failed / Pending / Unpaid in four tints), row actions (edit, print). Footer: "Page 2 of 16" left, numbered pagination centre, "7 / page ▾" right. Full pagination anatomy.
- Sidebar groups: MAIN MENU / CARDS & TREASURY / DEVELOPER (API Keys, SDKs, Support, Sandbox) — developer section in a payments product.
## 066 Elegostra (Outcrowd) — desktop + mobile companion, blue/orange
- Four KPIs in one connected card with drag handles (⋮⋮) on each cell — a hint that the dashboard is rearrangeable. Icon squares in brand colours on the right of each KPI.
- Balance Trend with a vertical highlight band on the selected month; Cash Flow as three mini stat rows (value + delta chip + label + "vs prev period"); Financial Growth as two labelled progress bars with a value pill on the bar ("72%").
- Spending Breakdown: bars with % above and amounts under, the top one filled blue with a label chip ("Food & Drink"). Orange "Insights" card with one sentence + ↗ button.
- Mobile companion panel shows the same data at phone width: Transaction history grouped "Today · 4 transactions", Cards Overview with card art + two mini stats + a spending-limit line + black "Manage Cards". Designing both widths from one system.
## 067 TalentOS (Orix) — desktop, lavender, recruitment
- Status bar top-right: credits "● 3,212", "● All systems operational", "Share Feedback", lavender "✦ Start a Search". System health in the header.
- Job cards: icon, title, 1-line description, then a small key-value table (Status chip / Candidates "87 Shortlisted" / Created by). Mini table inside a card.
- KPI tiles with a title, icon, huge number, one-line meaning ("Total pools created"). Sidebar "Collections" with coloured dot categories and a plan card with a usage bar ("3 days remaining").
- Recent Candidates: avatar + name in a pill + presence dot, role right, chevron. Pill-wrapped names as tags.
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
## 071 Novera (Nixtio) — tablet, lilac, serif headings
- Serif display for card titles (Total balance, Saving, My goal, Quick transfer, Budget) + sans for data. Chips for deltas are outlined, not tinted ("+ 12%", "77% completed").
- Total balance with a wavy area; Saving with chunky bars; My goal with a striped progress; Budget as stacked rounded bars in three pastel colours (Income/Expense/Saving).
- Card stack: three coloured tabs peeking above the lilac debit card (which carries a geometric pattern). Premium subscription card in pink with a black CTA. Pill tab nav, active black.
- Pastel but disciplined: three data colours + black. Shows "playful" can still be systematic.
## 072 Multipliiier (ElevenSpace) — desktop, white + yellow
- Sidebar: active item is a yellow filled pill (the only yellow besides the + button and reward icon). Light/Dark toggle at the bottom of the sidebar as a segmented control.
- Balance with currency chips (US Dollar / EURO) and an outlined "↗ Withdraw". Quick actions as three tall tiles with a tinted icon square top-left and a label bottom-left. Contracts as logo tiles; "Create contract" as three radio rows with title + one-line description + chevron.
- Cards: two card designs side by side (white / pale green) with "Account number ****9934", cardholder, valid thru — flat card designs, not 3D.
- Recent transactions: each row has THREE labelled columns ("To Miriad systems / LogicBox", "Request date / 09/09/2026", "Status / Pending") — label-over-value cells make a list readable without a header row.
- Rewards: referral card with "Copy link". Search placeholder "Search anything or ask AI ⌘S".
## 073 Fintech dashboard (Arounda) — desktop, warm beige + orange + black card
- Top nav as pills (Overview active) + search "⌘+F" + "Refresh data", black "Export", "Share". Left icon rail in a rounded column.
- "My cards" with a dark 3D card (card number, name, balance); "Application tokens" dark card with a big number (decimals faded), two deltas, an area chart and two footer buttons (Send / Invoice) that split the card's bottom edge. Footer-split buttons on a card.
- Total Expenses (red bars) / Total Income (blue bars) as two stacked mini cards with bar sparklines and deltas. Recent Contacts avatars + "Add new" black + "Manage contacts" ghost. "Add or Manage Widgets" dashed-style footer button. Promo tile "Powering Your Business Potential" with a 3D render — contained to one tile.
## 074 Voiceon AI voice (Oripio) — desktop, white, blue hero
- Greeting with italic serif name ("Welcome, Alex Carter 👋") — a single typographic flourish again. Helper sentence under it; black "+ Create Voice" right.
- Blue hero card with mixed-weight headline ("Turn Any Script Into *Natural Speech*") and a black pill CTA; Popular Services as three illustration tiles; Trending voices as rows (gradient orb avatar, name — tone, style, flag + language). Handpicked cards with 3D icons.
- Sidebar: workspace switcher, nav with "New" chip, Pinned section, "Invite team members" card. Low information density is appropriate for a creative tool home.
## 075 Enrolliq edtech (Filllo) — desktop, white, AI-heavy
- Header: search ⌘K, "AI Brain" pill with gradient icon, theme toggle, refresh. Page actions: "Courses: All Courses ▾" combined chip + blue "Analyze My Courses".
- KPI strip as ONE card with four cells: eyebrow in small caps (AVG. COMPLETION RATE), number + chip, and a third line (Target: 70% / 27 haven't logged in for 7+ days). Three-line KPI with target context.
- "Needing action today · 5" with a confidence banner ("96% CONFIDENT based on 1500 previous sessions"); two alert cards: severity chip (Needs Attention amber / Critical red) + timestamp, title, problem sentence, a tinted "AI Recommendation & Impact" block with a bulleted suggestion + "Estimated recovery 18 students · +$5400 revenue increase", and an action button (Fix Automatically / Review Lesson). The best AI-recommendation card anatomy in the set: severity → problem → suggestion → impact → action.
- "Improved this week" as a numbered list with before/after chips (65% → 83%) and "See details" buttons. Performance line chart with three series; Students At-risk with a count + delta + ranked list.
## 076 Banking dashboard (Nixtio) — desktop, red→orange gradient header
- Full-bleed warm gradient header (deep red → orange) holding the greeting, two white pill actions (Deposit/Withdraw) and a glassy card stack with "$12,680.42" (decimals faded). Everything below the header is white cards. Gradient as a header band, not a page wash.
- Overview: thin-bar histogram (hundreds of bars) with a selected cluster darker and a black tooltip "$1,548.24 ↗2.46% for April 2026". Category tiles 2x2: name + tiny icon, amount with faded decimals, delta with ↗/↘ and "from last month". Faded decimals = recurring Nixtio signature.
- Pill nav centred in the header with the active tab in a translucent pill. Investment Performance as mini bars with a "1.5%" black pill.
## 077 Fintech dashboard (Nabil) — desktop, white + orange, dashed cards
- Pill nav with the active one filled orange; Notifications pill with a red count. Left icon rail with the active icon as a black circle.
- KPI strip as one card, three cells with icon circles + delta chips. Segmented "Full Statistic / Result Summary".
- Three mid cards: dashed-border "Team Payments" (date chip + avatar stack +20), "Income Statistics" with four fat rounded bars in four colours, and an orange promo "Choose Best Plan" with "Upgrade Now". Dashed borders mark "configurable/placeholder" cards.
- Total Sales and Cost: two KPI tiles with ↗ circle buttons beside a step-area chart with a "$65.00" tooltip. Black "Submit Tax Information" alert card with a yellow warning icon — one dark card for the urgent task.
## 078 QNBpay (WLITZ) — desktop, Turkish payments, pink brand
- Bar chart in navy with the selected day in magenta; donut in green/red/grey/orange (semantic: success/refund/fail/dispute) with "Toplam İşlem 109" centre. Semantic colours for payment outcomes.
- Table with uppercase micro headers (SİPARİŞ ID / DURUM ⇅ / TARİH ⇅ / KART SAHİBİ / HAKEDİŞ / TUTAR), status chips (BAŞARILI green tint, BEKLEYEN İADE red filled, BAŞARISIZ grey), copy icons per row. Localised UI keeps the same anatomy.
- Shortcuts card as four icon+label rows; promo tile in brand gradient; announcements card. Brand ribbon decoration sits BEHIND the panel. Pastel pink page tint from the brand.
## 079 Jiron time tracker (Nixtio) — desktop, periwinkle, kanban + calendar
- Team cards in four saturated pastels (violet/blue/amber/pink) with avatar stacks, a title, a one-line description and a progress bar in a darker shade of the card colour. Colour per team.
- Kanban columns (Draft / In Progress / Editing / Done) with avatar initials chips (UI/PD/FD) per task, attachment/comment counts, a star, and green checks in Done. Week calendar with time rows, "now" line in blue, event blocks coloured by team with avatars + counts.
- Strong colour but systematic: 4 team colours, each used identically. Weak: pastel saturation + white text in events strains contrast.
## 080 Skymetrics (Maria M) — desktop, white, green/grey
- Sidebar grouped Analytics / Product / Customers / System with small-caps labels and a "Version 2.0" footer; "Invite team" tinted button. Header: "Last 14 days ▾", "All Brands ▾".
- KPI tiles: title + delta chip on the same line, number with a coloured dot, "vs previous 14 days". Revenue over time: two smooth lines (current green / previous grey) with a dual tooltip. Traffic by source: donut with external labels + counts and % via dotted leaders.
- Recent orders / Top products as compact tables with avatars/thumbnails. Everything 12–13px, one accent. A model of a quiet analytics dashboard.
## 081 Vanta business (Odama) — desktop, white, serif numerals, mountain backdrop
- Serif numerals for KPIs ("$284,892") with small 3D icons right; "Compared with Aug 01 – Aug 17, 2026" meta top-right. Serif numbers signal "finance/wealth".
- Revenue & Profit: three lines with a hover band and a 3-row tooltip; Cash Flow: barcode-style thin bars with the selected one black, Incoming green / Outgoing red, and a metric row beneath (Previous / Current). Revenue by Channel: labelled thin bars with amounts and %; Operating Expenses: stacked segment bar + legend rows + total footer.
- Customer Growth: number + delta + a "You're on track to hit your 70k customer goal" chip + weekly bars with Week 5 highlighted. Goal-tracking copy next to the number.
## 082 Paystay (Yscale) — desktop, soft pastel KPIs
- Four KPI tiles each on a different PASTEL tint (blue/lilac/peach/green) with an icon — category-coloured tiles; readable because tints are light and text is dark.
- Sidebar: greeting at the top ("Hello again, Emily Johnson! We're glad to see you back!"), nav with the active item as a black pill, "Current Account Balance $4,200.75" at the bottom. Balance in the sidebar footer is a nice persistent anchor.
- Transaction Log rows: icon, title + subtitle, status chip (Completed/Pending/Failed/Archived), amount + method. Quick Actions as four small outlined tiles. Activity Summary as a 4-colour segment bar with counts under. Launch banner with "Create a reminder".
## 083 Personal finance banking (Nixtio) — desktop, red→orange gradient CARDS
- Variant of 076: the gradient is on two hero cards (Overview, Credit Cards) rather than the header, page is cream. Overview chart = thin-bar histogram with a white tooltip. Credit Cards: amount, delta chip, "Credit Limit: $1000.00" chip, two white pill buttons (Deposit/Withdraw) with a swap icon between, glass card stack.
- Black "Create Report" button top-right; categories 2x2 tiles; Recent Transactions rows with status chip + masked card + signed amount. Shows how one system flexes: gradient-as-header vs gradient-as-cards.
## 084 Wallet dashboard (Ihor Ryzhak) — laptop, dark + green
- Total balance "569,324 USD" big; Credit limit / Internet limit as two green progress bars with "562$ / 1200$" ends. Limits as bars again.
- Filter chips (All / Incomes / Expenses) + date range chip + search + download icons on one row; bar chart of 9 days with the selected one green and a "↗ $200" chip.
- Transfer + Mobile top-up as two mini forms: input with a card icon and a green arrow button; helper text under each ("VISA/MasterCard Ukrainian or foreign banks", "Book of contacts"). Mini forms with helper lines. Digital Card tile with two 3D cards. Round icon buttons (≫, ⇄, +) top-right.
## 085 BorderFlow cross-border payments (Gurvinder) — desktop, white + indigo
- Sidebar with GENERAL / TOOLS / ACCOUNT groups (Exchange Rates, Verification, Security). Header: search with ⌘K, gift/bell/plus icons, avatar with role "Individual".
- KPI tiles: icon in a tinted circle, title + (i), big number, delta chip, "vs. last month". Transfers & Volume: paired bars (sent USD / received INR) with a dual axis + a line. Recent Transfers: flag avatar, name, "Country • Method", amount, status chip (Completed/In Progress/Failed), date/time, chevron. Country flags as avatars for cross-border.
- Sales Distribution donut with a country legend %; Transfer Methods as rows with % and counts; Quick Actions as three rows with icon, title, one-line description and chevron. Action rows with descriptions > icon grids when actions need explaining.
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
