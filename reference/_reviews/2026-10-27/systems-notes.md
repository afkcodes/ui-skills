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
