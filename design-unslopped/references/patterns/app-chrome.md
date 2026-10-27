# Patterns: app chrome

The parts every product needs and nobody screenshots. Numbers in brackets point to
`../design-notes.md` (255-272 are the chrome batch; 271 and 272 are negatives). Chrome is quiet: no
atmosphere, the accent only on selection and the one primary, 13-14px type on desktop; in tool mode
`../tools-and-analytics.md` governs density. Tables: `finance-and-dashboards.md` §5. Document upload
inside a flow: `applications-and-onboarding.md`.

## Contents
1. Global search and results
2. Command palette
3. Filters, active-filter summary and saved views
4. Settings
5. Notifications, inbox and activity
6. Overlays: modal, drawer, sheet, popover, inline
7. States library, toasts and banners
8. File manager and attachments
9. Profile, account, team and roles

Shared rules: targets at least 24×24 CSS px (WCAG 2.2 SC 2.5.8, AA), 44×44 pt on iOS (Apple HIG),
48×48 dp on Android (Material 3). Shortcuts show the platform modifier (⌘ on macOS and iPadOS, Ctrl
elsewhere). Status is word + glyph + tint, never colour alone (WCAG 1.4.1). Customer-facing
notification, error and confirmation copy in a regulated product goes to Compliance review.

---

## 1. Global search and results [255, 256, 257, 258, 259, 072, 075]
- Entry: a field in the top bar or sidebar with a keycap (⌘K: 075, 256, 258) and a placeholder that
  names what it searches ("PNR / Name / Ticket No / Booking Ref": 258; "Search anything or ask AI":
  072). Desktop opens an overlay or a dropdown under the field (255, 256); mobile opens a full-screen
  view, field focused, keyboard up, Cancel (iOS) or back (Android) to leave (257).
- Pre-query, never blank (257, 261): recent searches, 5 at most, with a clock icon and a ↖ control
  that copies the text into the field (distinct from tapping the row to run it), a "Clear" link and ×
  per row; then category or scope chips; then recent items and quick actions.
- Scope and sort (255, 256, 261): one row. Up to six fixed scopes as a segmented control with icons
  (255); user-toggled scopes as removable chips (256); connected sources as tabs above type chips
  (261). Scope narrows, sort orders: sort is its own control at the row end ("⇅ Most Relevant": 255).
- Result row: icon or avatar 32-40px · title with the match highlighted · one meta line (type ·
  location) · optional two-line snippet with the term highlighted again (255) · relative age right
  ("1d", "13d", "4mo"). Highlight is a tint behind the matched characters in the text colour (255
  lavender pill; 260 grey box per character), not bold plus colour, which reads as a link.
- Group by type with a counted heading ("Pages (6)": 255), 3-5 rows per group, then "Show all". The
  count must equal the rows (261 heads four rows "RECENT 3").
- Results page (255's expand icon, or Enter): the query stays editable at the top (258's Modify Search
  card); the count is a sentence with its scope ("102 Available Flights from 20 Airlines": 258); sort
  segmented (Cheapest / Fastest) apart from filter chips that overflow to "+3"; List / Table toggle
  for rows with many attributes. Totals must add up (259's do not).
- Zero results (255, 256): echo the query and scope, keep the scope bar, offer three exits: widen
  the scope, fix the query ("Did you mean…"), hand off (advanced search: 256; "Ask AI": 255).
- Keys and a11y: a combobox owning a listbox; focus stays in the input, `aria-activedescendant`
  follows ↑/↓, Enter opens, Esc closes and refocuses the trigger; "12 results" goes to `role="status"`.

Goes wrong: "Search…" with no scope, a blank panel before typing, one ungrouped list, the query lost
on the results page, "No results" as a dead end. Instead: scope, recents, true counts, three exits.
Sources: https://www.w3.org/WAI/ARIA/apg/patterns/combobox/ ·
https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html ·
https://developer.apple.com/design/human-interface-guidelines/search-fields

## 2. Command palette [260, 261, 255, 089, 075]
1. Input with the query at ~20px (the one large input in chrome); right: scope, an AI handoff, ×.
   First row pre-selected so Enter always acts (260's "Smart search ⌘M").
2. Optional scope row: source tabs and type chips (261).
3. Pre-query: Recent, then Quick actions with shortcuts ("Create new task ⌘T", "Add member ⌘M":
   261). Small-caps group labels with a count.
4. With a query: Actions first when the query matches a verb or object, composed from the match
   ("Assign to Simon Prusin": 260); then navigation groups named by content ("People", "Issues"),
   not "Keyword" (260).
5. Row: 16-20px icon · label · grey secondary · shortcut keycaps right-aligned.
6. Footer key contract: ↑↓ Navigate · ↵ Open · ⌘R Open in new tab · ⌘L Copy link · Esc Close
   (260, 261). Secondary verbs for the highlighted row live here.
- Actions are verb-first ("Create note"); an ellipsis means a second step (260 "Assign to…" pushes a
  people list; Backspace pops back). Navigation rows are nouns with an open-in arrow (261).
- The ⌘K hint: a 1px-bordered grey keycap in the search field (075, 256, 258) and beside "Search" in
  the sidebar (089). Keycaps inside the palette teach global shortcuts; they do not fire while the
  input has focus (260's single-letter [A] and [U] would eat typed letters).
- A11y: `role="dialog"`, `aria-modal="true"`; combobox + listbox with `role="group"` per section; focus
  returns on close. Mobile has no palette: the same index drives full-screen search with an Actions
  section and no keycaps; an iPad with a keyboard keeps ⌘K.

Goes wrong: a palette that only navigates (that is search); no footer, so nobody learns the keys;
eleven full-colour logos as the loudest row (261). Instead: actions first, footer always, logos grey.

## 3. Filters, active-filter summary and saved views [262, 263, 264, 258, 017, 029, 005, 095, 057]
| Situation | Form | Evidence |
|---|---|---|
| Up to 5 facets, few values, above a list | Dropdown chips; overflow "+3" or "More ▾" | 017, 029, 258 |
| 6+ facets, catalogue browsing | Faceted panel: left column desktop, sheet mobile | 262 |
| Dozens of values in one facet (IDs, sites) | Search in the facet, two rows, "Show 15 more" | 263 |
| AND / OR, operators, custom fields | Condition builder: field · operator · value | 264, 101 |

- Chip row: a set chip shows its value ("Status: Failed", "Class · 2") and is filled or tinted
  (017); unset chips outlined; "Clear all" as text at the row end, only when something is set.
- Faceted panel: one collapsible block per facet, control by type (262): exclusive → radios; many
  short values → wrap chips; boolean → one toggle; ordered sizes → checkboxes; numeric → range plus
  typed min/max ($500 / $900); colour → swatch plus its name ("Purple"). Each option shows a count;
  zero-count options stay visible and muted (005). Per-facet Reset only where something is set
  (263). A collapsed facet header shows its current value.
- Condition builder: "Where [Owner ▾] [is ▾] [Davon ▾]", drag handle, remove; an And / Or pill joins
  one nested group; Add condition, Clear all, Apply; flag incomplete rows (264 leaves "Select" blanks).
- Active-filter summary: with the panel closed, removable chips ("Brand: Apple ✕") + "Clear all"
  (095) + the result count. It is the only proof the list is filtered.
- Apply: instant for chip rows and fast desktop panels; explicit for modals, mobile sheets and slow
  queries, with the outcome on the button ("Show 128 results", not "Apply filters": 263).
- Saved views: tabs above the table, each a named filter + sort + columns with a count (057 Inbox /
  Needs Approval / Scheduled / Paid; 005). A changed view shows a dot and offers Save, Save as new,
  Reset; shared and personal views are labelled.
- Mobile: a "Filters · 3" button opens a full-height sheet; facets as an accordion; sticky footer
  "Clear all" (text) + "Show 128 results" (primary). Sort is a separate button, never a facet inside
  Filter (262's weakness). Desktop: chip row with a popover per chip, or the left panel.
- A11y: chips are toggle buttons (`aria-pressed`) or menu buttons; facet headers are disclosures with
  `aria-expanded`; count changes go to `role="status"`. Sliders and drag handles need a single-pointer
  alternative (typed values, Move up / down): WCAG 2.2 SC 2.5.7. Facets on protected characteristics
  (gender, age, nationality) in people search or credit need a stated lawful purpose: flag them.

Goes wrong: a modal for three facets; 20 IDs as checkbox tiles with no search; a chip reading "Class"
while two are set; "Select all" on every facet and placeholder values (263); Sort inside Filter
(262). Instead: the form that fits the count, values on chips, counts on options, one Clear all.
Sources: https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/ ·
https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html

## 4. Settings [265, 269, 270, 004]
- IA: desktop gets a sub-nav column beside the app nav, grouped under small-caps labels: Account
  (Profile, Security, Notifications) · Workspace (General, Members, Roles, Billing and plan,
  Integrations) · Advanced; a settings search once sections outgrow one screen; top tabs only when
  all sections fit on one line.
- Mobile is a hub: identity card, then two or three titled groups of rows (Account: Manage
  subscription, Restore purchases; Preferences: App settings, Privacy & Security, Notifications,
  Language: 270); each row pushes a page.

Section layout:
- Heading + one helper sentence, rows split by hairlines, forms at a readable measure.
- Toggle and select rows: label + one-line consequence left, control right ("Outside business
  hours · Route callers who dial outside hours": 265).
- Field rows: label column (~30%) left, control right on desktop (269); label above on mobile.
- State lives on the field: "✓ Verified 2 Jan 2025" under the email (269); a day switched off reads
  "Closed", not an empty grey input (265); prefixes as addons ("untitledui.com/": 269).
- Sub-flows open from their row ("Set Up": 265) into a page or modal, never inline.

Saving:
- Autosave independent, reversible controls (toggles, selects, a schedule: 265): commit on change,
  show "Saved" beside the control, revert and explain on failure (265 commits silently).
- Explicit save for fields edited as a set and for consequential changes (email, payout account,
  permissions): one save per section, enabled when dirty and valid, filled primary (269's dark-grey
  Save is not); on long pages a sticky bar appears when dirty ("Unsaved changes · Discard · Save
  changes") and must not cover the focused field (WCAG 2.2 SC 2.4.11). Leaving dirty asks first.
- Email or password change re-authenticates first; a new email stays "Pending verification" until
  confirmed; no "Confirm password" field with nothing to confirm (270).

Danger zone and billing:
- Danger zone: last section, red heading or 1px red border. Each row: action, consequence in numbers
  ("Deletes 14 projects and 2,310 files for 12 members"), outlined red button. The reversible option
  comes first (Archive beside it: 269; transfer ownership; export). Irreversible deletes confirm by
  typing the resource name (WCAG 3.3.4: reversible, checked or confirmed).
- Plan and billing: plan card (name, price with currency and period, renewal date, seats "8 of 10");
  usage as limit bars (`finance-and-dashboards.md` §9); card masked "•••• 4329" with expiry (004);
  invoices with status and download; "Change plan" states the price difference before confirming.
  iOS in-app subscriptions also offer "Restore purchases" (270; App Review Guideline 3.1.1).

Goes wrong: eight flat ungrouped rows; marketing bullets inside settings; a pencil per card opening a
modal per field; one Save covering three sections; Cancel as heavy as Save (270). Instead: grouped
sub-nav, consequence helpers, autosave or one save per section.
Sources: https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html ·
https://www.w3.org/WAI/WCAG22/Understanding/error-prevention-legal-financial-data.html ·
https://developer.apple.com/app-store/review/guidelines/

## 5. Notifications, inbox and activity [266, 267, 063, 089, 057]
- Entry: a bell with an unread badge (063), capped "9+". Desktop: a scrolling popover from the bell,
  footer "Mark all as read" + "View all" to the inbox page (266). Mobile: a full-screen page (267).
- Row (266): avatar 32-40px with a type badge · actor · verb · object, actor and object bold ·
  context and age right ("Workel · 15 min ago") · a bordered preview of the object (quoted comment,
  task card with due date, file path, event) · the one action it asks, inline (Decline / Accept).
- Copy names the object, amount and counterparty ("order #2458", "$450.00 from Upwork Inc.", "New
  login from Chrome on Windows 11 in Seattle, WA": 267). Security and money alerts carry their
  response ("This wasn't me"); account numbers stay masked.
- Group by day (TODAY / YESTERDAY / THIS WEEK: 267; 089) and by type tabs with counts (All ·
  Requests 14 · Mentions 2: 266). Collapse runs from one actor ("Yahya and 3 others…"); 266 lists
  four separate rows from one person.
- Unread is three cues together: tint fill + a thin leading accent bar + coloured time or dot (266, 267).
  Opening marks read; hover offers Mark as read / unread; the badge equals the unread rows (267
  shows 3 over two marked rows). "Clear all" gets an Undo toast, or archive instead.
- Inbox versus activity feed: an inbox is mine, actionable, and empties (057 Inbox / Needs
  Approval); a feed belongs to a record, is chronological and read-only, has no unread state, and
  doubles as the audit trail.
- Preferences: event types grouped by area as rows, channels (In-app, Email, Push, SMS) as toggle
  columns; "Mute" per thread from the row menu; quiet hours as day rows with a timezone (265's
  anatomy). Security and regulatory messages are marked as not mutable.
- A11y: the bell's name includes the count ("Notifications, 3 unread"); the popover is a non-modal
  dialog; new items announce through `role="status"`, never by moving focus.

Goes wrong: every row "15 min ago" (266); "A payment was failed" with no amount or action; icon
colour as the only grouping; nothing doable in place. Instead: true times, the object, the action.

## 6. Overlays: modal, drawer, sheet, popover, inline [011, 259, 101, 109, 264, 265, 266, 269, 271]
| Job | Desktop | Mobile | Evidence |
|---|---|---|---|
| Name one control | Tooltip on hover and focus, no actions | Inline helper text | — |
| Small choice tied to a trigger | Popover or menu, non-modal | Bottom sheet, medium detent | 264, 266 |
| Configure while watching data; inspect a row | Side panel, non-modal | Full-height sheet or page | 259, 101, 109 |
| Short blocking task or decision | Modal over a dimmed page | Sheet; system alert to confirm | 265, 269, 011 |
| Long, multi-step, or needs a URL | A page | A page | — |
| Feedback on what happened | Inline, toast or banner (§7) | Same | 271 (negative) |

- One modal at a time; a modal may open a popover, never another modal.
- Modal: header (title, optional icon tile, helper, ×), scrolling body, sticky footer with the
  primary rightmost and Cancel beside it (269). A modal with no button is a dead end (271).
- Side panel: title and ×, the page beside it still usable, no focus trap (259).
- Sheet: grabber, title, close (011); swipe-down is Cancel, so a dirty sheet asks first. Dim the
  page; blur only where the brand already uses glass (011).
- Popover: anchored to its trigger, closes on outside click and Esc, holds nothing irreversible.
- Focus (WAI-ARIA APG dialog): on open, focus moves inside (first field, or the least destructive
  button in a destructive confirmation); Tab and Shift+Tab cycle inside; the page behind is inert; Esc
  closes unless input would be lost, then asks; focus returns to the trigger. `role="dialog"` or
  `role="alertdialog"`, `aria-modal="true"`, labelled by the title.
- Destructive confirmation: the title names verb and object ("Delete 'Q3 payroll'?"); the body states
  the consequence in numbers and whether it can be undone; the button repeats the verb ("Delete
  payroll"), never "Continue", "OK" or "Yes"; red only on that button; Cancel takes initial focus.
  Reversible actions skip the dialog and offer Undo in a toast; irreversible, high-impact deletes ask
  for the name to be typed (WCAG 3.3.4).

Goes wrong: "Link Copied!" as a modal (271); a modal per settings field; a drawer for a two-field
form; "Are you sure?" with "Continue"; focus left behind the backdrop. Instead: the surface from the
table, the consequence in words, focus trapped and returned.
Sources: https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/ ·
https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog/ ·
https://developer.apple.com/design/human-interface-guidelines/sheets ·
https://developer.apple.com/design/human-interface-guidelines/alerts ·
https://m3.material.io/components/bottom-sheets · https://m3.material.io/components/side-sheets

## 7. States library, toasts and banners [268, 255, 256, 271, 037]
Design these for every list, panel and page; `../tools-and-analytics.md` §3 and §8 add stale,
sampled, read-only and long-running.

| State | Copy | Action | Evidence |
|---|---|---|---|
| First use | What will live here + ways to fill it, ranked | One recommended route, others grouped, manual last | 268, 037 |
| No results | Query and filters echoed | Clear filters · widen scope · hand off | 255, 256 |
| Cleared | The good state with time ("All caught up · last 2h ago") | Link to history, no create CTA | — |
| Loading | Skeleton in the final layout's shape | Cancel on long tasks | 271 (negative) |
| Error | What failed, why, when ("Bank feed timed out at 09:42") | Retry in place; input kept | — |
| Offline | "You're offline. Changes sync when you reconnect." + last sync | Queue writes; disable the rest | — |
| No permission | Who can grant it ("Only admins can change billing. Ask Priya Shah") | Request access; read-only stays | tools §8 |

- First use keeps the page frame (tabs, toolbar, disabled filters) and puts the add affordance where
  the data will appear (037's dashed "Add another currency" tile). Illustration optional, small,
  never the action (268 has none).
- Loading: skeleton rows at real height, text bars at varied widths, no layout shift when data
  lands; spinners only inside the button that started an action; long tasks show numbers
  ("Uploading 3 of 8 · 42 of 120 MB") and Cancel, never a modal "Please wait" (271).
- Errors stay in the region that failed while the rest of the page works; never "Something went
  wrong" without a reason or Retry.

Toasts versus banners:
- Toast: the result of the user's own action, one line plus optional Undo; bottom-centre or
  bottom-left on desktop, above the tab bar on mobile; one at a time; pauses on hover and focus;
  never an error that needs action; `role="status"`. An Undo must not vanish before it can be
  reached; offer the action elsewhere too (WCAG 2.2 SC 2.2.1).
- Banner: a persistent condition (offline, trial ends in 3 days, degraded service, read-only), full
  width at the top of its region; dismissible only when not critical.
- Inline message: tied to a field or region; the default for errors. A modal is never feedback (271).

Goes wrong: a 3D bell, a vague sentence and no button; every state as a buttonless modal (271); a
full-page spinner when one panel is slow. Instead: the copy formula, the surface by persistence.
Sources: https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html ·
https://design-system.service.gov.uk/components/notification-banner/ ·
https://m3.material.io/components/snackbar

## 8. File manager and attachments [261, 272, 259, 042, 089, 057]
- Toolbar: breadcrumb from the root, search, "Upload" as the primary (057 "Upload Bill"), New
  folder, sort, List / Grid. Grid only for images and media.
- Row: checkbox · type badge (PDF / CSV / DOC: 261) · name truncated in the middle so the extension
  stays · "Modified 2 hours ago by Sophia Jones" (261) · size right-aligned, tabular, upper-case
  consistent units (KB / MB / GB) · kebab. Folders first; default sort Modified, newest.
- Long folders scroll (virtualised) or "Load more", never 99 numbered pages (272).
- Storage meter: "141.2 GB of 200 GB" with a bar split by type; the parts add up to the total (272:
  Video and Audio alone are 176.6 GB of a 188 GB plan with "78% Space Left").
- Upload: limits stated first ("PDF or JPG, max 25 MB"); while dragging, the whole list is the drop
  target ("Drop to upload to Finance / Q3"); the Upload button is the non-drag alternative (WCAG 2.2
  SC 2.5.7). Per-file rows: name, size, %, cancel; failures inline with reason and Retry ("Too
  large · max 25 MB"); a "Checking file…" state where uploads are scanned.
- Selection swaps the toolbar for a bulk bar ("3 selected · Move · Download · Delete"); Shift-click
  selects a range.
- Preview: a side panel on desktop with metadata, versions and activity (259's pattern); a full-screen
  viewer with a share sheet on mobile.
- Delete moves to Trash with an Undo toast; permanent deletion only from Trash, confirmed (§6). Where
  records fall under retention rules, the dialog says so and routes deletion to the data owner.
- Attachments in a message or form: rows or chips with type icon, name, size, ×, progress (042's file
  bubble; 089's attach control under the input); images as thumbnails; limits beside the control.
- Mobile: rows 56-64px ("2.4 MB · Mon"); Upload opens a sheet (Camera, Photos, Files); long-press
  starts selection.

Goes wrong: folders as cards with no dates or owners, sizes that cannot be true, lower-case "gb", no
upload or drop target (272). Instead: the list, real metadata, honest totals.

## 9. Profile, account, team and roles [269, 270, 266, 261, 004, 057]
- Own profile: identity card (avatar, name, email, plan or role chip), form rows with verification
  state and date on the field (269); avatar change as its own step with crop, zoom − +, Reset,
  Confirm (270). Email and password changes follow §4.
- A record viewed by staff: facts strip first ("First seen 1 Mar 2025 · First purchase 4 Mar 2025 ·
  Revenue $118.00 · MRR $0.00": 269); the reversible action before the destructive one (Archive:
  269); PII masked with reveal and copy (004), every reveal logged. Dates on one record agree (269's
  email is "verified" before the customer was first seen).
- Team members table: member (avatar, name, email) · role (inline select for admins) · status
  (Active / Invited, expires in 6 days / Suspended) · last active (relative; absolute on hover) ·
  2FA · kebab (Resend invite, Change role, Remove). "Invite members" is the primary: emails as
  tokens, a role select with one sentence per role, the cost before sending ("Adds 2 seats · £24 a
  month from 1 Nov"). The invite arrives as an actionable notification (266) and the palette offers
  "Add member ⌘M" (261). Removing someone states what happens to their files and access.
- Roles are permission sets, not job titles ("Admin", "Approver", "Viewer", never "CEO"): 3-5
  built-in, each with a sentence and a member count; custom roles start as a copy. Matrix: rows are
  capabilities grouped by area, columns are roles, cells ✓ or —; consequential rows carry limits
  ("Approve payments up to £10,000"). Payments products show the approval chain (maker-checker:
  057's Needs Approval tab). The last Owner cannot be downgraded and the control says why. Every
  role change lands in the activity feed with who and when (§5).
- Mobile: members as rows with a role chip; role change in a sheet; the matrix becomes one page per
  role listing its capabilities.
- A11y: role selects are labelled with the member ("Role for Priya Shah"); the matrix is a real table
  with header cells; denied controls are disabled with a reason, not hidden (§7).

Goes wrong: job titles in a Role column; names truncated with space to spare; "Remove" with no
consequence; an invite with no seat cost. Instead: permission sets, consequences, a visible audit.
