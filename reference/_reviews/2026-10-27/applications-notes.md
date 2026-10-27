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
