# Design systems: working inside GOV.UK, Carbon, Polaris and Atlassian

Read this when the brief names a design system, when the repo already ships one (`govuk-frontend`,
`@carbon/react`, Polaris web components, `@atlaskit/*`, an in-house system such as Alchemy), or
when the product is a form-heavy transactional service. Read it right after `peak.md`. Inside a
system the stance is inherited, not chosen, and for services §2 replaces the peak targets the way
`tools-and-analytics.md` §1 does for tools. Evidence: 170-182 (captured 2026-10-27 from public
pages; 182 is the negative), plus 017, 028, 036, 052, 057, 068, 070, 142 where they show the point.
Values below come from the named package versions; re-check them when the repo pins another.

## 1. Working inside a system

The system is the stance. The work moves from inventing a look to making four things excellent:
the content, the data, the order of the flow, and one element inside the content area.

| Never override | Where character may live |
|---|---|
| Header, shell, logo, navigation (170, 181) | The words: questions, hints, error messages, button verbs (171, 173, 174) |
| Type family and type scale | Real data with edge cases: "Not provided" (174), relative-then-ISO dates (181) |
| Colour tokens and their roles; the one primary colour | The flow: what is asked, in what order, what is cut |
| Focus state, field anatomy, button hierarchy | Composition inside the content column: main versus aside (180) |
| Spacing scale, radius, elevation, motion tokens | One bespoke element in the content area, drawn with the system's tokens |
| Status vocabulary (tags, badges, lozenges) | Illustration only where the system allows it (Polaris empty states, 179) |

1. Read the system and version from `package.json`; load its tokens. Write tokens, not hex copies
   (GOV.UK: `govuk-functional-colour("brand")`, never `#1d70b8`), so a palette update reaches you.
2. Map the visual-system block (SKILL step 4) onto named tokens. Where the brief wants something
   the system lacks, say so and use the nearest token; do not invent a value.
3. Start from the system's own templates and patterns (question page, details template, data
   table), then add the bespoke element: a cost breakdown before a start button, an eligibility
   result, a "what happens next" timeline (017 drawn in system type and colour), a chart in tool
   mode.
4. Compare renders against the keepers here and the system's own examples, not the lit
   references (076, 083). The question is "does this belong in the system and say more?".

Sloppy: re-skinning (a new accent, softer radii, a gradient hero) breaks the trust and the
accessibility testing the system bought; the opposite failure is the default component dump with
demo data left in (182, 028). Do instead: tokens untouched, content and data made specific.

## 2. Service mode: form-heavy transactional services

Use for anything a person completes once or rarely: apply, register, claim, open an account,
report, pay, renew. Add **service** to the step 1 classification beside consumer app, marketing
site and tool. GOV.UK's patterns (170-176) are the bar whatever the brand.

Service mode decides the structure and the rubric; it does not replace the design language. Inside
a native app (an identity check or application in a banking app), the platform's chrome and
components replace GOV.UK's: a large title as the question, native text fields, pickers and the
camera sheet, the platform's buttons, and the content stays matte. Score this rubric with the
platform's adjustments from `README.md` §3. Inside a shop, only the checkout and payment steps run
in service mode; the product pages and basket stay consumer screens. Ask in the interview whether
the service will be hosted on GOV.UK (`../questions.md` 1b): that decides the crown, GDS Transport
and the header (§3).

| Rule elsewhere in the skill | In service mode |
|---|---|
| One hero taking 35-45% of the screen | The hero is the question. One question per page, the h1 is its label or legend (171); nothing competes. Only the start page (170) and the confirmation panel (175) get a hero moment |
| Largest text ≥ 4x body; hero 56-84px | h1 32-48px over 19px body (about 2-2.5x). Scale contrast comes from the empty page, not a giant figure. Body never under 16px |
| Atmosphere in one place | None. White page, dark text, the brand bar. The confirmation panel is the only coloured block (175) |
| Composition with tension | A two-thirds column, left-aligned, about 75 characters per line; the empty third is intended (171) |
| A bespoke element on every screen | Optional and inside the content only: a cost or eligibility summary before start, a timeline on confirmation (017), a calculator that answers the question. Never decorative |
| Stance and signature move | Inherited. The "move" is plain English and the order of questions |
| Micro-detail | Hints with an example, inputs sized to the answer (172), "(optional)" on labels, Change links with hidden context (174), the reference number (175) |
| Scroll-stop test | **Completion test**: can a first-time user on a phone answer this page without help, in one go, recover from the error state, and say what happens next? |

Page types, in journey order:
- **Start page (170)**: h1 is the task ("Register to vote"); what you can do in 2-4 bullets; how
  long it takes ("about 5 minutes"); what you need ("Before you start"); one start button
  ("Start now ›", larger than Continue); other routes as links. Cost and timescales here, before
  commitment. Sloppy: a marketing hero with a photo and three feature cards (182).
- **Question page (171, 172)**: back link, h1 as label or legend, hint as one short sentence
  without a full stop, the input, Continue. One thing per page means one question or one tightly
  bound group (a date, an address). A section name goes in a caption above the h1. Optional
  fields say "(optional)"; never mark mandatory fields with asterisks. A progress indicator only
  if research shows it helps. Sloppy: twelve fields in a card under a six-dot stepper with a
  "Next" button disabled until valid. Even inside a product shell, a wizard stepper in the
  toolbar (070) carries Back and Next; the step's content still asks one thing.
- **Error summary (173)**: on submit, at the top of main, titled "There is a problem", one link per
  error to its field, focus moved to it, the same words inline above the field with a 5px red
  rule on the group, entered values kept, "Error: " prefixed to the page title. Messages say what
  to do: "Enter your date of birth", "Passport issue date must include a year". Sloppy: a toast
  saying "Something went wrong", a cleared form, a submit button greyed until everything is valid.
- **Check answers (174)**: a summary list per section (key, value, "Change"); skipped optional
  answers show "Not provided"; close with an h2 ("Now send your application"), the declaration in
  one sentence, and a button that names the commitment ("Accept and send"). This is where fees,
  consents and the balance-after line belong (068, 040 show the meta-row habit). Sloppy: the form
  re-rendered read-only, a "Submit" button.
- **Confirmation (175)**: a panel with the outcome and the reference; "We have sent you a
  confirmation email"; "What happens next" saying who acts and by when; a feedback link. Sloppy:
  "Success!" with a tick, confetti, no reference, no timescale.
- **Task list (176)**: only for long services done over several sessions in any order. Tasks
  grouped under h2s, the whole row is the link, statuses in sentence case: "Completed" as plain
  text, "Incomplete" or "In progress" as a tinted tag, "Cannot start yet" in grey; the final
  action available only when all are complete. Sloppy: uppercase coloured pills on every row and
  a green tick on the finished ones, so the unfinished rows are the ones that disappear.
- **Plain English**: sentence case; front-load the point; check any sentence over 25 words; no
  jargon (GOV.UK's A-Z bans "agenda", "collaborate"); address the user as "you"; buttons are
  verbs that say what happens. Atlassian targets reading ages 12-14 and Shopify US grade 7; use
  the stricter of the brand's own target and these.
- **Regulated services** (banking, insurance, lending at Allica): declarations, fees, consents and
  eligibility copy go through Compliance or Legal before publication; say so in the brief.
- **Test with users, and the Service Manual**: a mockup is a hypothesis, not a finished service.
  For any public-sector service (central government, councils, the NHS) say in the brief and the
  presentation that it must follow the GOV.UK Service Manual and meet the Service Standard: research
  with real users, including people with access needs and low digital confidence, before and during
  build, and a service assessment before it goes live (https://www.gov.uk/service-manual,
  https://www.gov.uk/service-manual/service-standard). For any other service, recommend testing the
  flow with five or more users before launch and name the questions most likely to fail.
- **Failure endings**: design the screens for declined, referred to a person, more documents
  needed and timed out, each with what happens next, by when and how to get help, not only the
  success confirmation.

Service-mode review rubric (replaces the eight peak qualities in step 6):
1. **One thing per page**: every page has one question or one bound group.
2. **The question is the heading**: label or legend as h1, a caption for the section, no repeated
   h1s.
3. **Inputs fit answers**: widths sized, hints by example, "(optional)" marked, no asterisks.
4. **Errors designed**: summary + inline + message copy exist for every page that validates.
5. **Review before commit**: check answers with Change links and a button that names the act.
6. **Ending**: confirmation with reference, next step, who and when.
7. **Plain English**: proofread, sentence case, no jargon, no sentence over 25 words unchecked.
8. **Access**: WCAG 2.2 AA contrast, visible focus, works at 320px wide and at 400% zoom.
Ready when nothing is missing and at most one is weaker (the bar for every rubric). Item 6 covers
every ending: success and the failure endings above.

## 3. GOV.UK Design System (govuk-frontend 6.6.0)

- **Principles**: the 11 Government Design Principles, chiefly start with user needs, do less, do
  the hard work to make it simple, this is for everyone, be consistent not uniform.
- **Layout**: design for small screens first. Width container 960px (`$govuk-page-width`; content
  measured x 240-1200 at 1440), gutter 30px, columns full, three-quarters, two-thirds, one-half,
  one-third, one-quarter; two-thirds for most pages. Breakpoints 320 / 641 / 769. Responsive
  spacing units 0-9 on large screens: 0, 5, 10, 15, 20, 25, 30, 40, 50, 60 (small screens 4-9:
  15, 15, 20, 25, 30, 40). Every line height is a multiple of 5px.
- **Type**: GDS Transport. Services on service.gov.uk must use it; a service not on GOV.UK must
  not (nor the crown, the GOV.UK logotype or the brand colours). Off GOV.UK keep the patterns, set
  `$govuk-font-family` to your organisation's brand font (the coded fallback is `arial,
  sans-serif`) and use the generic header. Scale, large / small screens: 48/32 heading-xl,
  36/27 heading-l, 24/21 heading-m and body-l, 19/19 heading-s and body, 16/16 body-s; 80 and 27
  are for exceptional use. Headings bold; tabular figures via `govuk-font($tabular: true)`.
- **Colour (functional, v6)**: text #0b0c0c, secondary #484949, link #1a65a6 (hover #0f385c,
  visited #54319f), border #cecece, input border #0b0c0c, template background #f4f8fb, focus
  #ffdd00 with #0b0c0c text, error #ca3535, success #0f7a52, brand #1d70b8. Primary button green
  with a 2px darker shadow and 0 radius; secondary grey; warning red. Brand blue is the header and
  footer rule, not the button.
- **Density**: low by design: 19px body, 40px radios and inputs, 2px black field borders (171).
- **Components to reach for**: back link, button (start variant), radios, checkboxes, text input
  with width classes, date input, error summary and message, summary list and card, panel, task
  list, tag, notification banner, cookie banner, service navigation.
- **Accessibility**: WCAG 2.2 AA is a must; focus is a yellow fill with a black underline and is
  never restyled; labels and legends double as headings.
- **Content**: the GOV.UK style guide is part of the system; plain English is mandatory.
- **Inside it**: character is the quality of the questions, their order, and one bespoke block in
  the main column built from GOV.UK type and colour. Never restyle the header, buttons, focus,
  radios or error colours. Sloppy: rounded blue buttons, Inter, each question in a shadowed card
  with progress dots; or the crown and GDS Transport on a non-government domain.

Sources: design-system.service.gov.uk/styles/ (layout, spacing, type-scale, typeface, colour);
/patterns/question-pages, check-answers, confirmation-pages, start-using-a-service;
/components/error-summary, task-list;
gov.uk/service-manual/design/making-your-service-look-like-govuk;
gov.uk/guidance/government-design-principles; gov.uk/guidance/style-guide/a-to-z; govuk-frontend
6.6.0 source (`settings/_measurements.scss`, `_media-queries.scss`, `_typography-font.scss`).

## 4. IBM Carbon (v11)

- **Principles**: open, inclusive, modular and flexible, builds consistency; built on the IBM
  Design Language. It is a product system first: productive type, square shapes, layers.
- **Grid (2x Grid)**: 8px mini unit. Breakpoints sm 320 (4 columns, margin 0), md 672 (8, 16px),
  lg 1056 (16, 16px), xlg 1312 (16, 16px), max 1584 (16, 24px); box padding 16px; total gutter
  32px, or gutterless for closely related content. Spacing tokens 01-13: 2, 4, 8, 12, 16, 24, 32,
  40, 48, 64, 80, 96, 160.
- **Type**: IBM Plex Sans and Plex Mono (open source, SIL OFL; usable on any product).
  Productive tokens: label-01 and helper-text-01 12/16 +0.32px; body-compact-01 14/18 and
  body-01 14/20 +0.16px; body-02 16/24; heading-01 14/20 semibold; heading-02 16/24 semibold;
  heading-03 20/28; heading-04 28/36; heading-05 32/40; heading-06 42/50 light; heading-07 54/64
  light. Big type goes lighter, not bolder; that inversion is Carbon's own scale move.
- **Colour (White / Gray 100 themes; also Gray 10, Gray 90)**: background #ffffff / #161616;
  layer-01 and field-01 #f4f4f4 / #262626; text-primary #161616 / #f4f4f4; text-secondary #525252 /
  #c6c6c6; border-strong-01 #8d8d8d; interactive and focus #0f62fe (G100: #4589ff, focus #ffffff);
  support error #da1e28, success #24a148, warning #f1c21b, info #0043ce. Depth comes from layer
  colours, not shadows.
- **Density and shape**: table rows 24 / 32 / 40 / 48 / 64 with a 48px toolbar for the large
  sizes (177); buttons 24 / 32 / 40 / 48; fields 40px filled with a bottom rule (178); UI shell
  header 48px, side nav 256px. Core controls are square (177, 178). Motion: 70, 110, 150, 240,
  400, 700ms (fast-01 to slow-02).
- **Components**: UI shell, data table (toolbar, batch actions, expansion, AI label), text input,
  select, date picker, number input, tile, inline and toast notifications, progress indicator,
  and the IBM Products patterns (create flows, tearsheet, side panel).
- **Accessibility**: the IBM Accessibility Checklist (WCAG AA, Section 508, European standards);
  themes aim at WCAG 2.1 AA contrast. Status needs an icon or tag, not blue text alone (177).
- **Content**: concise, actionable, sentence case (177, 178).
- **Inside it**: character lives in the data and in tool-mode precision (`tools-and-analytics.md`;
  036 and 057 show the same restraint off-system); a heading-04 or -05 value (28-32px) over 14px
  body is the north-star row in Carbon's own scale. The only gradient is the AI aura
  (`ai-aura-start` rgba(69,137,255,0.1)) and it marks AI-generated content only. Sloppy: Carbon
  with decorative gradients, rounded shadowed tiles and a second accent; do instead: layers for
  depth, square controls, one blue (§8).

Sources: carbondesignsystem.com/all-about-carbon/what-is-carbon, /elements/2x-grid/overview,
/components/data-table/style, /components/button/style, /components/UI-shell-header/style,
/components/UI-shell-left-panel/style, /guidelines/accessibility/overview; @carbon/layout 11.62.0,
@carbon/type 11.70.0, @carbon/themes 11.84.0, @carbon/motion tokens.

## 5. Shopify Polaris (App Home web components)

- **Principles** (App Design Guidelines): match the Shopify admin; put merchant needs ahead of
  being different; design for mobile first; build accessibly; express the brand with a light
  touch, through imagery and illustration.
- **Layout**: the page component sets width: `base` (default, shows the aside slot), `large` for
  resource indexes and dashboards, `small` for settings. Homepage single column (179); details two
  columns, main plus aside (180); settings as annotated sections. A 4px spacing grid. Content lives
  in containers; no paragraphs on the background; one density per page.
- **Type**: Inter, then the system stack. Sizes 11, 12, 13, 14, 16, 20, 24, 30, 32, 36px
  (font-size-275 to -900); weights 550 medium, 650 semibold, 700 bold; 13px body (179, 180). The
  page title is the largest heading on the page.
- **Colour**: page #f1f1f1, surface #ffffff, text #303030, secondary #616161, border #e3e3e3,
  link #005bd3; the primary fill is near-black #303030, not green. Fills: success #047b5d,
  critical #c70a24, warning #ffb800, caution #ffe600. Roles: green positive or done, yellow paused
  or incomplete, orange in progress or pending, red blocked or error only. Text contrast ≥ 4.5:1.
- **Shape**: radius 4, 6, 8, 12, 16, 20 (border-radius-100 to -500); cards 12px, fields 8px (180).
- **Components**: page (breadcrumb, title, primary and secondary actions), section (heading,
  subheading, supplemental, accessory), banner, badge, index table, resource list, empty state,
  setup guide, metrics card (179; 052's hairline KPI card), callout, modal, save bar, toast.
- **Rules**: one primary action per card; no primary buttons in table rows (tertiary, icon or a
  menu); destructive actions use the critical tone, not a red fill (180); the save bar guards
  unsaved changes.
- **Accessibility and content**: never colour alone for status, contrast ≥ 4.5:1; Shopify's
  voice, plain language at US grade 7, CTAs open with a verb, active voice, and no page title
  repeated under the title bar.
- **Inside it**: character lives in illustration (empty states, callouts), real merchant data and
  one well-made section; never custom chrome, a custom primary colour, or a hero in the app frame.
  Check badge semantics: a falling return rate is good news, so not red (179). Sloppy: the app
  arrives with its own gradient header and fonts and a primary on every row; do instead: admin
  chrome untouched, brand in imagery, row actions as a menu.

Sources: shopify.dev/docs/apps/design, /design/layout, /design/visual-design, /design/content;
shopify.dev/docs/api/app-home/latest/patterns (homepage, details, settings, resource-index);
@shopify/polaris-tokens 9.4.2 (the last published token set; values match what 179-180 render).

## 6. Atlassian Design System (@atlaskit/tokens 20.8.0)

- **Principles**: familiar and consistent (build from system components; the same pattern for the
  same job), keep experiences and language simple, make no assumptions about people's abilities.
- **Layout**: the navigation system: top bar, side nav, main, optional aside and panel. On 181 the
  side nav is 320px, the top bar 56px, the page title 24px, default buttons 32px, table rows 48px.
  Spacing tokens space.025 to space.1000: 2, 4, 6, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80.
- **Type**: Atlassian Sans and Atlassian Mono for app UI; Charlie Sans is the brand face for
  marketing only. Outside Atlassian products use the token's fallback stack (`ui-sans-serif,
  -apple-system, "Segoe UI", …`). Tokens: body 14/20, body.small 12/16, body.large 16/24; headings
  at weight 653 from xxsmall 12/16 to xxlarge 32/36; metric 16/20, 24/28, 28/32.
- **Colour (light)**: text #292a2e, subtle #505258, subtlest #6b6e76; link and brand bold
  #1868db; selected background #e9f2fe; border #0b120e at 14% alpha; input border #8c8f97; focus
  border #4688ec; danger #c9372c (text #ae2e24); success bold #5b7f24; warning bold #fbc828;
  surface #ffffff, sunken #f8f8f8.
- **Shape and elevation**: radius xsmall 2, small 4, medium 6, large 8, xlarge 12, xxlarge 16,
  full. Surfaces sunken, default, raised, overlay; raised and overlay pair with shadows, and in
  dark mode higher surfaces get lighter.
- **Accessibility and content**: components ship keyboard support and ARIA, but patterns, content
  and interactions still need review; plain language for reading ages 12-14.
- **Components**: navigation system, page header, dynamic table, lozenge for status, badge, flag,
  section message, inline edit, modal dialog, form (header, sections, footer; a "Required fields
  are marked with an asterisk" legend; GOV.UK forbids asterisks, so never mix the two), empty
  state.
- **Inside it**: character lives in the data and its micro-details (181: relative dates that turn
  ISO after a week, folder glyphs in tinted tiles); brand blue stays on links, icons, selection and
  the one primary. Sloppy: a hand-built coloured sidebar, brand blue on every button, legacy hex
  values pasted instead of tokens, so light and dark themes drift apart.

Sources: atlassian.design/foundations/typography, /foundations/elevation,
/foundations/accessibility, /components/navigation-system/examples, /components/form/examples;
@atlaskit/tokens 20.8.0 themes (atlassian-light, -spacing, -shape, -typography).

## 7. Relatives: NHS.UK and USWDS

- **NHS.UK frontend 10.6.1** ships the same service building blocks as GOV.UK (error summary,
  summary list, task list, panel, date input), so §2 applies unchanged. Frutiger W01 is loaded
  from NHS's own font host with an `arial, sans-serif` fallback; outside an NHS service use the
  fallback. Colours: blue #005eb8, text #212b32, secondary #4c6272, page grey #f0f4f5, red
  #d5281b, focus yellow #ffeb3b.
- **USWDS**: Public Sans by default (Source Sans Pro, Merriweather, Roboto Mono also shipped).
  Colour grades run 0 (white) to 100 (black); the grade difference ("magic number") predicts
  contrast: 40+ AA large text, 50+ AA, 70+ AAA (WCAG 2.0). Its page templates are scaffolding;
  182 is what they look like shipped unedited.

Sources: nhsuk-frontend 10.6.1 `core/settings` (`_typography.scss`, `_colours-palette.scss`);
designsystem.digital.gov/design-tokens/typesetting/font-family, /design-tokens/color/overview,
/templates/landing-page.

## 8. The sloppy version of each system

| System | The sloppy version | Why it reads as slop | Do instead |
|---|---|---|---|
| Any | Template or storybook shipped as-is: "<Project title>", "Option 1", "Load Balancer 1-6", placeholder circles (182) | Nobody designed the content; the system did all the work and the page says nothing | Real questions, real data, every placeholder replaced, empty sections deleted |
| Any | Default component dump: every component the library has on one page, all at equal weight (028 off-system) | No decision about what the user is here to do | One task per page (services) or one north-star row (tools) |
| GOV.UK | Rounded blue buttons, Inter, each question in a card, a six-dot stepper, asterisks | Loses the tested patterns and the trust of the GOV.UK look | Stock components; character in the questions and their order |
| GOV.UK | Crown, GDS Transport or GOV.UK colours on a non-gov domain | Misleads users about who runs the service | Generic header, own brand font and colours, same patterns |
| Carbon | Decorative gradients, 12px radii and drop shadows on tiles, a second accent on buttons, Plex swapped for Inter | Fights layers, square geometry and the one-blue rule; looks like a different product | Layers for depth, square controls, #0f62fe only; gradient only as the AI aura |
| Carbon | Status as blue or grey text, tiles in rainbow fills (142 off-system) | Colour-only status; colour stops meaning anything | Status icons or tags; colour from support tokens only |
| Polaris | Own gradient header, own fonts and a hero inside the app frame | Shopify's own words: over-branding "sets it apart from Shopify" | Brand in illustration and imagery only |
| Polaris | A primary button on every row; red badges for good news (179's return rate) | Primaries lose meaning; signs read backwards | Tertiary row actions or a menu; badge tone follows the meaning |
| Atlassian | Hand-built nav, hard-coded legacy hex, brand blue on every button | Breaks theming and the shared shell users rely on | Navigation system and tokens; blue for links, selection, one primary |
