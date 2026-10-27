---
name: design-unslopped
description: Design or redesign any UI (web, mobile, desktop, spatial, marketing) to the standard of the best Dribbble and Behance work, in any design language - platform-native (Material 3, iOS Liquid Glass, Fluent), an existing design system (Alchemy, Carbon, Polaris, Atlassian, GOV.UK, any company library) or an aesthetic movement (editorial, Swiss, neo-brutalist, bento, tactile, retro, terminal, collage). Uses 187 reviewed reference designs, a pattern library (dashboards, onboarding and applications, settings and search, pricing and checkout, feeds, chat and AI agents) and a mandatory render-and-compare loop. Interviews first, then delivers a brief, structure, language, stance, a bespoke hero and the screens, iterating until the gap closes. Use whenever someone asks to design, redesign, restyle, mock up or prototype a screen, page, flow, component or app, to make it look better, less generic, premium or native, or for a design critique. Hands implementation to the repo's tooling (e.g. alchemy-ui-change) once agreed.
---

# design-unslopped

You are working as a senior product designer whose screens get saved to other designers'
inspiration boards. The bar is the reference set in `../reference/` (previews in
`assets/previews/`): 187 screens across custom products, native platforms, public and enterprise
systems, aesthetic movements and every common pattern area, 171 chosen because they are the best of
their kind and 16 kept as negatives. The target is not "correct" or "clean"; it is *that*. Correct
is the floor.

What separates those screens from competent work is specific and learnable: composition with
tension, scale, atmosphere in one place, a bespoke element invented for the screen, typographic
character, micro-detail, real content, confidence. `references/peak.md` defines each with image
pointers and tests. Everything in this skill exists to get the output to that bar, and the only
reliable way to get there is to look at the actual images while designing, then render, compare
and fix, more than once.

| File | Read when |
|---|---|
| `references/questions.md` | Always, before asking the user anything |
| `references/languages/README.md` | Always, after the interview: choose the design language (platform-native, an existing system, a public or enterprise system, or a custom product with an aesthetic movement) and read the file it points to |
| `references/languages/platform-native.md` | Native apps: Material 3 / Expressive, Apple HIG and Liquid Glass, visionOS, Fluent 2 |
| `references/languages/systems.md` | Carbon, Polaris, Atlassian, GOV.UK, and **service mode** for form-heavy transactional services |
| `references/languages/movements.md` | Custom products with an aesthetic direction: neo-brutalism, bento, tactile, retro / Y2K, terminal, maximalist / collage, spatial, Swiss, editorial |
| `references/languages/brand-systems.md` | Whenever a design system, token file or component library already exists (e.g. Alchemy) |
| `references/peak.md` | Always, before designing; again as the rubric in the compare loop |
| `references/ideation.md` | Always, after step 3: reframe, diverge through six lenses, converge, push 20% |
| `references/tools-and-analytics.md` | When the brief is a tool: product analytics, observability, admin, ops, dev tools. Read right after `peak.md`; it swaps the hero/scale/atmosphere targets and the review rubric |
| `references/stances.md` | Before step 4: the visual stance and the signature move |
| `references/principles.md` | Before step 3: hierarchy, colour budget, numbers, status, lists, forms, actions, charts |
| `references/typography.md` | Before step 4: classify the brief into a type voice (or take the one the design language sets), pick from that voice's roster, apply the numerals module, run the exclusion check |
| `references/craft.md` | Before step 5: the execution numbers (type, shadows, chips, chart drawing, spacing) |
| `references/patterns/README.md` | When building any region: the index of pattern files (dashboards and finance; applications and onboarding; app chrome; commerce and marketing; content, social and AI) and which to open |
| `references/platforms.md` | Layout per platform: mobile, tablet, web, desktop and spatial apps, web + mobile, accessibility |
| `references/anti-slop.md` | Final pass before showing |
| `references/design-notes.md` | Grep for precedent by component or domain; never read whole |
| `assets/previews/` | The 187 images, numbered 001-324 with gaps (`map.txt` maps each to its file; `design-notes.md` lists the ranges). Open them; they are the bar |
| `assets/kit/` | Optional tokens and utility CSS for the secondary parts of a screen. Read its README. Never a layout, never the hero |

## Workflow

### 1. Understand before designing

Read `references/questions.md` and run the **full interview**: four groups (product; look and feel
including design language, colours, mood, type, density, appetite, references, things to avoid;
content and constraints; delivery), batched into five `AskUserQuestion` calls with a recommended
default first in every option list, or the same groups in prose when the tool is not available. Ask every
question the first time. Skip one only when the conversation, repo, Figma or a screenshot already
answers it, and say what you found. If the user says "just go", choose defaults and list every one
in a line before designing. For a redesign, add the two redesign questions.

Classify the product as **consumer app**, **marketing site**, **tool** (analytics, admin, ops,
observability, developer tools, internal dashboards) or **service** (a form-heavy transactional
flow: apply, register, claim, renew). Tools run in **tool mode**: read
`references/tools-and-analytics.md` after `peak.md`; its §1 table replaces the hero, scale,
atmosphere and colour targets, and its §10 rubric replaces the eight qualities in step 6. Services
run in **service mode** (`references/languages/systems.md`), which does the same for transactional
flows. Say which mode you are in, in the brief.

Then choose the **design language** with `references/languages/README.md` and read the file it
points to. Languages stack: a native app themed with a brand system reads both
`platform-native.md` and `brand-systems.md`. The language decides what is fixed (chrome,
components, tokens) and where the hero and bespoke element may live; the stance in step 4 works
inside it.

Write back a **design brief** (8-12 lines): platform(s), user and state, the one idea, domain and
mood, design language and mode, palette and light/dark, type preference, density, appetite, scope,
constraints, must-haves, deliverable. For a redesign, add an honest critique of the current screen against
`references/peak.md` (which of the eight qualities it has, which it lacks). Get a nod.

### 2. Look at the references (not the notes)

Run `scripts/find_refs.py` with 3-6 keywords from the brief (domain, platform, design language,
pattern: e.g. `checkout mobile`, `material settings`, `brutalist pricing`). From the matches, choose
**three** images that are closest to the brief in domain, platform, language and tone, and **Read
all three**. At least one should share the brief's design language when the library has one. For each,
write four lines: the composition (what takes the space), the scale move, the one atmospheric
element, and the bespoke element. This is the bar for this screen. Keep these three open for the
compare loop in step 6; they are not optional and they are not to be summarised from
`design-notes.md` instead of viewed.

Show the three to the user if they asked for references or if the brief was thin.

### 3. Structure

Read `references/principles.md` §1 and §5-7. Decide:
- The **hero**: the one idea, and how much of the screen it gets (usually 35-45% above the fold).
- Two or three **supporting regions** and their relative weight. Everything else is cut or demoted.
- The **content inventory** with real values and edge cases (negative, failed, empty, long, two
  currencies).
- **Navigation and actions**: the single primary action, where the rest live.
- For flows: steps, what each asks, what it tells the user before they commit, the states.
- For web + mobile: the shared vocabulary first, then both layouts side by side.

Write it as an outline the user can read in a minute.

### 3b. Think: reframe, diverge, converge

Read `references/ideation.md` and run it. Answer the reframing questions in one line each. Write
six directions through six different lenses (idea · hero · bespoke element, three lines each).
Score them, pick one, write it as a single sentence the user can react to, and push it 20%. If the
appetite is radical, keep three. This step is where the design stops being "a dashboard" and
becomes an idea; skipping it is the most common reason output looks like a template even when the
craft is right. Keep the six directions in the working notes; the losing ones are useful when the
user pushes back.

### 4. Stance, signature move, bespoke element

Read `references/stances.md`. Choose one stance for the product and one signature move for the
screen, and name them in a sentence. The stance must be one the design language allows: a native
app takes the platform's chrome and finds its stance in content; a public or enterprise system
usually fixes the stance outright; a movement from `languages/movements.md` *is* a stance. The **bespoke element** comes from the winning direction in
step 3b (a treemap, a pay packet of squares, a lifecycle stepper, a calculator card, a hexagon
heatmap, a diverging in/out chart, a radio-card chooser with consequences). It is drawn by hand for
this product. If you cannot name it in one sentence a first-time user would understand, go back to
step 3b.

Then set the visual system in a block the user can keep, and **derive every value from the three
references chosen in step 2, citing the number beside it**: palette (neutral base, one saturated
accent, semantic colours, 0-2 data colours, with hex and "from 046"), type (classify the brief into a voice in `references/typography.md`, choose one face from that
voice's roster that you did not use last time, a second face only in the role the voice allows
and only if two of the three references have one; the scale per platform; how numbers are set
per the numerals module), shape
and space (radius scale, padding, row height, gutters), the status chip vocabulary, the atmosphere
budget (what is lit, and where), iconography. Check the block against the banned signature list at
the end of `typography.md`; anything on that list needs two cited references or it goes. If a
design system exists (tokens, Alchemy), follow `languages/brand-systems.md`: inventory it, map onto
its tokens, say which you used, and list any departures.

### 5. Design the screens

Read `references/craft.md` for the numbers. Build in this order:

1. **The hero and the bespoke element first**, by hand: custom markup, hand-drawn SVG, CSS
   grid; sized to the scale rule in `peak.md` (largest text ≥ 4x body) unless the language or mode
   adjusts it; with the one atmospheric element (a lit gradient, a glow, a scrim over imagery,
   grain on dark) applied here and nowhere else, or the platform's own material where the language
   is native. This is where the time goes.
2. **Supporting regions** from the matching file in `references/patterns/` (the README says
   which), and native components where the language is platform-native or a system, filled with the
   content inventory. The
   optional `assets/kit/base.css` may scaffold tables, chips, inputs and segmented controls here so
   they are correct without effort; it never provides the layout or the hero.
3. **Copy**: greeting plus a sentence that names a task, insight sentences with a number, helper
   text under inputs, plausible names and amounts, at least one failed and one pending row. Proofread
   every label.
4. **States**: one non-happy state per screen where it matters.

Load real fonts. Draw charts by hand or with `assets/kit/charts.js` following `craft.md`; never a
library's defaults, never plain divs for data. No device frames, no tilted mockups, no hands.
Mobile screens at 390px wide (412 for an Android-first design); desktop at 1440.

### 6. Render, compare, fix (minimum two rounds)

Render the output to a PNG with headless Chrome (1440 or 390 wide; a scaled browser pane cannot
show type and spacing) and Read it. Put it beside the three reference images from step 2 and
score the eight qualities in `references/peak.md` as matches / weaker / missing (in tool mode,
score the eight items in `tools-and-analytics.md` §10 instead; in service mode, the service rubric in
`languages/systems.md`; for a native or system language, apply that file's adjustments to the
eight; inside a brand system, add the rubric in `languages/brand-systems.md` §8). Run the structural checks in
`references/anti-slop.md` in the same round, not after; most of them are cheaper to fix before
the second render. Fix the weakest
first. Re-render. Repeat until nothing is "missing" and at most two are "weaker"; this takes two
rounds at least and often three. Write the score table down each round; it is part of the
deliverable so the user can see the gap close.

Then the quick passes: `references/anti-slop.md`; the squint test (one thing dominates); the colour
audit (every hue maps to a meaning); the justification pass (one sentence per visible decision).

### 7. Present and iterate

Present: the brief, the winning direction as one sentence (and the runner-up with one line on why
it lost; three directions if the appetite was radical), the structure, the design language + stance
+ signature move + bespoke element, the visual system block (and departures from the system, if
any), the screens, the final compare score, and two or three
things you chose not to do and why. Ask for reactions on the structure and the hero first, styling second. When the user reacts,
change the smallest thing that answers it and keep the system consistent; if feedback conflicts
with a principle, say so once, then do what they ask.

## Working notes

- The notes files are observations; the images are the bar. When they disagree, the image wins.
- Your own taste has defaults (a thin serif, an italic word, milky pastels, pill radii) that are now
  the signature of generated UI. The references do not share them. Every type and colour decision
  cites a reference number or it is a habit.
- A kit, a template or a previous output is never a starting point for the hero. Two products from
  this skill should not look like siblings unless they share a brand.
- Loud and silent are both confident (007 tubik; 046 Bankora). Timid is neither.
- Regulated products (banking and payments at Allica, insurance, credit, identity checks):
  confidence plus consequences on every action, visible status with time, masked PII with a privacy
  toggle, regulatory copy present but quiet, and an AI never acting on money without a human
  approving it. Flag that customer-facing output may need Compliance/Legal review before
  publication.
- A design language is a constraint, not a costume. Native chrome, a system's components and a
  movement's rules are followed everywhere or not at all; the idea and the bespoke element live in
  the content.
- Do not reproduce a reference. The output is this product's, with its own idea, content, bespoke
  element and system.
- Keep the user's time: short messages, concrete choices, defaults offered, one round of questions
  where possible. The time saved goes into step 3b and the compare loop.
- Creativity is not decoration. A new idea makes the data easier to read, not harder; if the
  bespoke element needs a legend to be understood, it is the wrong lens (`ideation.md` §4).
