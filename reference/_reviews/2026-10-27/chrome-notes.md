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
