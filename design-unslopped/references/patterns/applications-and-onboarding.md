# Patterns: applications, onboarding and the forms inside them

Each pattern gives the slots, in order, that the best references use, then how it goes wrong.
Numbers in brackets point to `../design-notes.md` (230-242 are this area's batch; 241 and 242 are
negatives). Official guidance is cited by name and listed under "Sources" at the end of each
section; GOV.UK Design System and Apple HIG pages were read as published on 2026-10-27, Material
values come from the material-web token set v0_192.

Regulated flows: anything that asks for identity, offers credit or insurance, or tells someone the
outcome of an application carries legal content (APR and representative examples, decline reasons,
data use, cooling-off). The patterns below give the anatomy; Legal and Compliance own the words, the
prominence and the decision wording, and sign them off before anything customer-facing ships.

## Contents
1. Sign-up and sign-in
2. First-run onboarding
3. Identity verification (KYC)
4. Multi-step applications
5. Document upload
6. Consent, e-signature and declarations
7. Approvals: maker-checker, queue, audit trail
8. Form craft for all of the above

---

## 1. Sign-up and sign-in [230, 231, 232, 234, 241]
1. **Delay the account.** Let people use as much of the product as possible before asking (a quote,
 a calculator, browsing). When the account is needed, a heading plus one sentence names what it
 gives ("start connecting with millions of top designers": 230).
2. **Identifier first.** One field (email, or mobile number) and one filled primary, "Continue".
 Social or SSO buttons above it as outlined buttons, an "or" divider, the legal line under the
 primary in 12-14px grey with underlined links (230). The next screen picks the method for that
 identifier: a passkey prompt, a password field, or "we've sent you a link".
3. **Passkeys.** Default to a passkey where the platform supports it; the user gives only a user
 name. Name the method on the button ("Sign in with passkey", "Sign in with Face ID"), mention
 only methods this device has, and never call app authentication a "passcode" (234 does). Keep a
 fallback: password or a one-time code.
4. **Passwords.** Label "Create a password" on sign-up, "Password" on sign-in. State the rule
 before typing (231): at least 8 characters, no maximum, block common passwords. Show/hide toggle,
 paste allowed, `autocomplete="new-password"` / `"current-password"`, no confirm field (the
 toggle replaces it; 231 still has one).
5. **Magic link or emailed code.** A "Check your email" page that shows the address it went to,
 says what to do, offers "Resend", and states expiry. Links expire after one use, when a newer one
 is sent, or when the address changes.
6. **One-time code.** One input with `inputmode="numeric"` and `autocomplete="one-time-code"`, or
 separate boxes that accept a pasted code (231: six ~52pt boxes). Under the heading, where it went:
 in full at sign-up, masked at sign-in ("to ••9704": 234). "Not received a code?" on the same
 screen (231 "Send Again"); at sign-up it lets the user correct the number. GOV.UK sends 5 digits,
 valid 15 minutes, accepts spaces and hyphens.
7. **The other path.** "Already have an account? Sign in" is visibly separate from the sign-up
 task (230); two equal buttons side by side is not enough of a difference.
8. **Help** stays on screen for anything longer than one step: routes with response times and
 hours ("within 24 hours", "● Online": 232).

Errors: on a failed sign-in say "Email or password is incorrect" (never which one), clear the
password, allow 5-10 attempts before a lock or extra check. Field errors use the templates in §8.

Goes wrong: 241 has a premium brand panel over a broken form: "Sing Up Account", an error on a valid
email that says "Enter a valid Email", and "Buy BTC" as the sign-up button. Proofread the two
largest strings, write the error that names the fault ("Enter an email address in the correct
format, like name@example.com"), and label the button with the action ("Create account").

Sources: GOV.UK Create accounts, Passwords, Password input, Confirm a phone number, Confirm an email
address, Email addresses (design-system.service.gov.uk/patterns/); Apple HIG Managing accounts
(developer.apple.com/design/human-interface-guidelines/managing-accounts).

## 2. First-run onboarding [233, 242, 013, 015, 234]
1. **Value first.** The first screen after sign-up does the product's first task with the user's
 data (connect an account and see a real balance, set a goal and see the projection). Teach by
 doing; put tips next to the control they explain, at the moment it is used. Postpone setup that
 has a sensible default.
2. **Personalisation, one question per screen** (233): section chip ("Goals", "Profile"), a
 two-line question, one sub-line, the control, a full-width primary. Each answer shows what it buys
 straight away ("15 min" → "329 books per year": 233). If an answer changes nothing the user
 sees, cut the question.
3. **Choice controls.** Chips with a "+" glyph for multi-select, the selected chip inverted (233,
 013); a picker wheel or preset tiles for one value; radio cards with a one-line consequence for a
 short set of options (`finance-and-dashboards.md` §13).
4. **Progress.** A thin segmented bar, one segment per section, filling within the section (233,
 015). Not dots, not a percentage that jumps.
5. **Permission priming.** Ask when the feature that needs it is first used; at launch only if the
 product cannot work without it. A custom screen before the system alert has one button,
 "Continue", that opens the alert: never "Allow", never a close or "Not now" on that screen. The
 purpose string is an active sentence saying what is collected and why ("The app uses your
 location to find branches near you.").
6. **Skip.** "Skip" top right on every optional step (234); a skipped tour does not return on next
 launch but stays findable in Help or Settings.
7. **Type and the other path.** The onboarding headline may carry the product's one typographic
 flourish (an italic or serif word: 013); body copy stays plain. One primary CTA plus a text link
 for the other path ("I already have an account").

Goes wrong: 242, the carousel: a milky lilac gradient, an icon cloud, a centred title, dots, the
same "Get Started" on every slide, and a body that contradicts its heading. Nothing to try, no skip,
no sign-in. Replace it with 233's shape (questions whose answers change the next screen) or with
the first task itself.

Sources: Apple HIG Onboarding; Apple HIG Privacy, "Requesting permission" and "Pre-alert screens"
(developer.apple.com/design/human-interface-guidelines/onboarding, /privacy).

## 3. Identity verification (KYC) [234, 235, 017]
1. **Where it lives.** Mid-task checks (a limit raise, a first large payment) open as a sheet over
 the blurred app, one heading, one sub-line, one control, one button, ✕ top right; closing returns
 to the task (235). Account opening runs it as full-screen steps inside the application's progress.
2. **Before capture.** Why it is needed and how the data is used, as a link and one reassurance line
 (234 "How we use your data"). Country first when the accepted documents depend on it (234).
 Documents as a list, each with its requirement ("Ensure it's valid and not expired": 235); never a
 one-card carousel (235's weakness).
3. **Document capture.** Full-screen camera, a target frame (dashed rectangle 234, corner brackets
 235), a live status pill above the frame that changes with the problem ("Please hold still", too
 dark, glare, move closer), a fixed instruction below it ("Move your ID inside the rectangle."),
 a shutter of ~80pt (234). On web, offer file upload beside the camera.
4. **Review before submit.** The captured image large, the same quality checks the pill used as a
 ticked list (corners visible, no glare, text sharp), the fields read from it (name, date of birth,
 expiry) for the user to confirm, "Retake" outlined and "Use this photo" filled.
5. **Selfie or liveness.** Same anatomy: an oval frame, one instruction at a time, the status pill,
 no countdown the user cannot control.
6. **Processing.** A named step with a time ("Checking your documents · usually under 2 minutes")
 and what happens if they leave (234's "We are processing…" has no time).
7. **Retry.** Name the fault and the fix ("The photo is blurred. Hold your phone still and take it
 again"); after repeated failures offer a different document, an upload, or a manual route.
8. **Manual review.** A status with time and owner: "We're checking your documents by hand. We'll
 email you by Tuesday 3 November", a reference number, what they can do meanwhile. Show it as the
 current step of a lifecycle stepper (017) on the application's status page.

Regulated: the data-use statement, retention, and any use of face or fingerprint (biometric data
can be special category data under UK GDPR) need DPO and Compliance review; so do the wording of
"we couldn't verify you" and the routes offered after it.

Goes wrong: a capture screen with only "Take photo", a spinner with no time, and "Verification
failed" with no reason or next step. Every state above has a sentence and an action.

Sources: GOV.UK File upload (error wording), Confirmation pages ("what happens next and when"),
Question pages ("Using range sliders"); Apple HIG Privacy, "Requesting permission" (camera).

## 4. Multi-step applications [236, 237, 238, 239, 240, 015, 017, 070]
**4a. Linear stepper or task list.** Use a linear stepper when the order matters and the
application is done in one sitting: a desktop rail of 3-6 steps, each a title plus a one-line
description of what it asks (238), done steps with ✓, the current step distinct from done (238's
black disc reads as done); a "Step 1/6" eyebrow over the page heading (238); a thin segmented bar
on mobile (237, 015); in a builder or setup tool, the numbered stepper sits in the toolbar with Back
and the primary beside it (070). Use a task list when users need several sessions or can choose
the order (business account opening, a mortgage): tasks named with verbs ("Provide financial
evidence"), statuses as words (Completed in plain text, Incomplete or In progress highlighted,
Cannot start yet grey and unlinked, There is a problem red and only for errors), the whole row a
link, tasks grouped under step headings ("Check before you start"). Test without a progress
indicator first; if one is needed, "Question 3 of 9" beats a twelve-step bar. Goes wrong: steps
labelled "Step 1 / Step 2 / Final", which tell the user nothing about what is coming.

**4b. Eligibility up front.** Hard rules (age, residency, minimum turnover) on the start page and at
the input they apply to ("You must confirm you are 15+": 235). Complex eligibility is a short
question set ending in a results page: eligible or not, cost, how long. Ineligible is a page with
the reason and what to do instead, never a validation error. For credit, a soft-search result
before the hard application ("75% Chance of Approval": 236), worded and checked by Compliance.
Goes wrong: the user learns on step 5 that sole traders cannot apply.

**4c. Live terms beside the control.** Preset tiles for common amounts plus "£ Enter another amount"
with the allowed range under it (236); term tiles in years with months in brackets (236). A box
beside or under the controls recalculates as the user changes them: monthly payment, number of
payments, first payment date, total repayable (237). On the results page a rail restates the
inputs with ± steppers and "Update" (236). Sliders always get a typed alternative. Goes wrong:
237's box omits APR and total repayable, and 236's offer says 8.9% APR beside a representative
example at 9.9%; every number on a credit screen is computed from one source and checked.

**4d. Save and resume.** The start page offers "Start a new application" and "Continue your
application"; the resume entry shows the product, last saved time, progress ("3 of 6 sections
complete") and the date the draft expires. Answers save on every "Continue"; "Save and come back
later" is a secondary link that ends with a reference or a sign-in link sent by email. Carried-
forward answers show as completed rows with ✓ that reopen on tap (239). Goes wrong: a bare "Open
saved application" tile with no product, date or progress.

**4e. Check your answers.** Title says what to do ("Check your answers before sending your
application"). A summary list per section: label, answer, "Change" link with hidden text ("Change
date of birth"); skipped optional answers read "Not provided". "Change" returns to this page, not
through the rest of the flow. For credit, a block restating amount, term, monthly payment, APR,
total repayable and first payment date (237's "Credit information"). The button names the act:
"Accept and send", "Send application". Goes wrong: 237's final button says "Next" and its first
says "Submit".

**4f. Outcome screens.** One template, four outcomes, each with a reference number, "what happens
next" as a vertical lifecycle stepper with dates (Submitted ✓ → Checks → Decision → Funds: 017),
contact details, and a way to save a record (PDF, email).
- Approved: the offer restated (amount, rate, first payment), the next action as the primary
 ("Review and sign").
- Referred: "We need to look at your application" + the date they will hear by + what they may be
 asked for. Not "pending".
- Declined: plain language, the reason category where it may be given, what they can do next
 (other products, free debt advice where relevant, how to ask for a review), no red failure
 illustration. UK credit declines can carry required content (for example, naming the credit
 reference agency used); Legal and Compliance own that copy.
- Submitted, decision later: received + reference + date.
Goes wrong: 239's thumbs-up and "We will process it and reach out to you in a days": no date, no
reference, a typo on the one screen everyone reads.

Sources: GOV.UK Question pages, Complete multiple tasks, Task list, Check a service is suitable,
Start using a service, Check answers, Confirmation pages, Interruption pages, Validation
(design-system.service.gov.uk/patterns/, /components/task-list/).

## 5. Document upload [240, 239]
1. **Requirements first.** Before the first dropzone: the list of documents and why, the formats
 and the size limit ("PDF, JPG or PNG, up to 15MB each": 240). On a long application, the same
 list on a "What you'll need" page before step 1.
2. **One slot per requirement** (240), titled with the document and the period ("Business bank
 statements, last 3 months"); optional ones say "(optional)" in the title (239).
3. **Dropzone.** Always visible, dashed 1px border, drag and drop plus a "Choose file" button
 (239, 240); on mobile "Take photo" and "Choose file" instead of drag.
4. **Per-file row.** File glyph, name, size; then the state: uploading (thin progress bar, ✕ to
 cancel: 240), checking ("Checking for viruses…"), uploaded (✓, "Replace", "Remove" acting on
 that file only), failed (the error in the row, "Try again"). The slot's title row shows the count
 when several files are allowed ("2 files").
5. **Errors** from the templates: "Select a [document]", "The selected file must be a JPG, PNG or
 PDF", "The selected file must be smaller than 15MB", "The selected file is empty", "The selected
 file is password protected", "The selected file contains a virus", "The selected file could not
 be uploaded – try again".
6. **Reuse.** A file uploaded earlier in the journey (a driving licence for identity) is offered
 again where the same proof is needed.
Goes wrong: one generic "Upload documents" card and a list of filenames with "00%", leaving the
user to guess which file satisfies which requirement; 240 also shows no uploaded or failed state.

Sources: GOV.UK File upload (design-system.service.gov.uk/components/file-upload/), Start using a
service.

## 6. Consent, e-signature and declarations [230, 236, 237]
1. **Review the document.** Title, version and date; a summary of the terms that bind (amount,
 APR, term, fees, cancellation period) above the full text; the full text inline or as a PDF link
 with its size. Key figures match the check-your-answers page exactly.
2. **Declaration.** One plain statement directly above the final button ("By sending this
 application you confirm that the details you have given are correct to the best of your
 knowledge"), then "Accept and send". Separate consents get separate unticked checkboxes; never
 bundle accuracy, terms and marketing in one box (237 bundles two).
3. **Signature.** A typed name pre-filled from the application with date and time stamped, or a
 drawn pad with undo and clear; a drawn signature needs a non-drawing alternative (same reason
 GOV.UK gives for sliders, WCAG 2.5.1). Show who signs and in what capacity ("Signing as director
 of Harbour Joinery Ltd").
4. **Legal copy present but quiet.** Grey, 12-14px, under the primary (230); representative example
 in a grey band under every offer (236). Quiet means lower contrast, never below legible
 size and never behind a disclosure where the regulator expects prominence; Compliance signs off
 size and placement.
5. **Record.** After signing: the signed document to download, the time it was signed, a copy by
 email, the reference.
Goes wrong: a pre-ticked "I confirm that the accuracy of my personal data I agree with the terms of
service" checkbox (237's wording) beside a yellow "Next".

Sources: GOV.UK Check answers, Confirmation pages, Question pages ("Using range sliders").

## 7. Approvals: maker-checker, queue, audit trail [057, 017, 103, 005, 036]
1. **Queue.** Tabs by state with counts (Inbox / Needs Approval / Scheduled / Paid: 057). Row:
 item, requester, amount right-aligned, submitted time relative with absolute on hover, due or
 cut-off time, status chip word + glyph (005). Bulk approve only for items of one type, with the
 total shown before confirming.
2. **Detail.** What is being approved as label-value rows (payee, amount, from account, when it
 leaves, fee) with the consequence stated (`finance-and-dashboards.md` §10-11).
3. **Maker-checker.** "Created by Priya Shah · today 09:14" above the actions. A maker viewing their
 own item sees the approve action replaced by a line saying why ("You created this payment, so
 another approver must approve it"), not a silent grey button. Actions: "Approve" filled, "Reject"
 outlined with a required reason, "Return for changes" as a link. The control (who can approve,
 thresholds, two approvers above a limit) is set by Compliance; the UI states it.
4. **Approval chain.** A vertical stepper with names, roles and timestamps: Created ✓ → Approved by
 Tom Reid ✓ → Waiting for a second approver (017).
5. **Audit trail.** One row per event: timestamp, actor and role, action verb, before → after for
 changed fields, source (web, API, mobile); newest first; filter by actor and action; export. No
 edit or delete affordance on the log (103's event feed anatomy). State freshness in the header
 ("Updated 2 min ago": 036).
Goes wrong: an "Approve" button with no amount or payee on the same screen, and "Pending" with no
"since" and no name of who it is waiting for.

## 8. Form craft for all of the above [230, 231, 233, 236, 237, 238, 239, 241, 036]
**8a. One thing per page or a long form.** Start with one question per page: the label or legend is
the page heading, a caption above it names the section ("About you"), a back link at the top, the
button reads "Continue". Group related questions on one page under a statement heading when
research says so: expert or repeat users, fields that belong together (238's vehicle block, 236's
loan questions), desktop back-office tools. Mobile consumer flows stay one question per screen
(233). Goes wrong: twelve fields on one mobile screen with one button at the bottom.

**8b. Label, hint, error anatomy.** Order top to bottom: label, hint, error message, input. Hint is
one short sentence, no full stop, no links; longer explanation goes in body text above the label
or in a side column (238's why-we-ask column, 236's right-gutter notes). The error sits after the
hint in red, the input gets a red border, and screen readers hear "Error:" first. Mark optional
fields "(optional)"; never asterisks (239 does it right; Material's own examples use "*required",
which this rule overrides). Never use placeholder text as the label or the example: it vanishes on
typing and fails contrast (230 and 239 do this). Material's outlined field, if the language is
Material: input 16/24, supporting text 12/16 (body-large / body-small),
1px outline, 2px on focus, 4px corners; its error text replaces the supporting text, so keep the
hint's content in the error. Goes wrong: 241's red "Enter a valid Email" on a correct address.

**8c. Error summary.** On submit with any error, even one: a box at the top headed "There is a
problem", one link per error that moves focus to the field, wording identical to the inline
message, keyboard focus moved to the box, every entered value kept. Messages say what is wrong and
how to fix it, use the question's words ("Enter how many hours you work a week"), and avoid
"valid", "invalid", "please", "sorry", "oops" and "This field is required". On the web validate on
submit, not on blur. In native apps HIG validates as people go (email on leaving the field,
password before leaving it) and may withhold Continue until required data is in; if the button is
disabled, a line says what is missing (231's grey "Verify" says nothing). Goes wrong: errors only
in a toast that disappears.

**8d. Input types and masks.** `inputmode="numeric"` for whole numbers, `"decimal"` for amounts;
avoid `type="number"`; `type="email"` with spellcheck off. Set `autocomplete` (email, postal-code,
bday-day/-month/-year, one-time-code, new-password). Size fixed-width inputs to the answer
(postcode about 10 characters, day and month 2, year 4). Dates of birth as three fields with an
example ("For example, 27 3 2007"). Currency as a prefix ("£": 236) with the unit also in the
label, because screen readers skip prefixes. Accept spaces, hyphens and pasted characters in
codes, sort codes and postcodes and normalise them after; one input for a sort code. Prefill
from what you already know or can look up: one VIN fills brand, engine, model, year and colour
(238); a postcode lookup fills the address with "Enter address manually" beside it. Goes wrong: a
mask that types the hyphens for the user and then rejects a pasted sort code.

**8e. Autosave and submit.** Save on every "Continue"; on long single pages save in the background
and say so in the header ("Saved 09:42"), the same freshness cue as 036. Never let autosave submit.
Prevent double submission on the final button. The browser back button returns to the previous
page in the state the user left it; after submission it shows the outcome, not a second submit.
Goes wrong: "Your progress may be lost" on a page that never said it was saving.

**8f. Buttons.** One filled primary per page, labelled with its action ("Continue", "Send
application", "Verify code"), left-aligned under the last field on desktop, full width at the
bottom on mobile (233). Back as a link at the top, not a second button competing with the primary
(238 puts an outlined Back top left and the primary bottom right). Goes wrong: 237's "Submit" on
step 1 of 4.

Sources: GOV.UK Question pages, Validation, Error summary, Error message, Text input, Password
input, Dates, Email addresses, Bank details, Button (design-system.service.gov.uk); Apple HIG
Entering data, Text fields; Material Web text field docs and tokens v0_192
(github.com/material-components/material-web).
