# Brand systems: designing inside a design system that already exists

Most real work happens inside someone's system: a token file, a component library, a Figma library,
a brand book, or a public system themed for a brand (Material or Carbon with a client's colours).
The risk is the opposite of the blank-canvas risk. A blank canvas drifts to generic defaults; a
system drifts to a **component dump**: every section a default card, every page the default
template, nothing invented. This file is the method for getting peak work out of a system without
breaking it. Read it whenever the brief names a design system, a token file or a component library,
alongside `platform-native.md` or `systems.md` when the system is built on one of those.

## 1. Inventory the system before designing

Read the layers in this order and write the inventory into the design brief, so every later choice
can cite it. Never ask the user for what the repo or library already answers.

| Layer | What to find | Where it usually lives |
|---|---|---|
| Tokens | Colour roles (surface, content, accent, semantic, data), type scale, space scale, radius, elevation, motion | `tokens.json`, CSS custom properties, Tailwind config, Figma variables |
| Components | Every component you plan to use: API, variants, sizes, fixed behaviours (colours it hard-codes, padding it adds) | Type definitions, Storybook, the library's source |
| Templates | Page layouts and when each one applies ("not for…" lines matter) | Template docs or index |
| Patterns | How the system asks for things, shows things, helps | Pattern docs |
| House style | The written rules templates leave out: how screens look, density, imagery, tone | A `DESIGN.md`, brand book, content guide |
| Voice | Capitalisation, tense, words to avoid, how errors and amounts are written | Content style guide |
| Existing screens | What the product already looks like next to the screen you are changing | The running app, screenshots |

Inventory block for the brief, one line each: tokens used · components used · template · patterns
matched · house-style rules touched · gaps (what the system does not have).

## 2. Find the system's signature

Every system worth using has one or two things that make it *this* brand: a colour used with
restraint, a shape, a type treatment, an illustration style, a status vocabulary, a motion. Name it
in a sentence. 005 shows a system whose signature is rigour (a logo construction grid and a complete
status vocabulary); 046 is a system of black fills on white with one amber chip; 126 is the neutral
floor with no signature at all.

If the system is neutral (no signature you can name), the screen's character must come from content
and the bespoke element, not from styling. Do not import a stance the tokens cannot express.

## 3. Expression zones: where character may live

| Zone | Character allowed | Notes |
|---|---|---|
| The content area's hero | Yes: the number, the sentence, the bespoke element | Built from tokens (fills, strokes, radii, space) so it reads as native |
| Empty states, onboarding, success screens | Yes: illustration, voice, a larger type step | Only in the system's illustration style if it has one |
| Marketing and campaign surfaces | Yes, within the brand book | Product chrome stays untouched |
| Data visualisation | Yes, within the data palette | If there is no data palette, propose one (section 6) |
| Navigation, headers, sidebars, tab bars | No | Chrome is the system's job |
| Component internals (padding, states, focus, disabled) | No | Never restyle a component to make a layout work |
| Semantic colours, spacing scale, type scale | No | Use the roles; never a raw hex or a magic pixel |

## 4. How the skill's steps change inside a system

| Skill step | Inside a system |
|---|---|
| Stance (`stances.md`) | Take the stance the tokens already imply (one accent on neutrals → ink and bone or monochrome data; a gradient token → gradient band). Never a stance that needs colours, faces or radii the system lacks. |
| Type (`typography.md`) | The system's faces only. The voice still decides *how* they are set: weights, which scale steps, tracking within what the tokens allow. |
| Colour | Token roles only. Accent for the primary action and selection; semantic roles for meaning; data colours from the data palette. |
| Scale | The hero takes the largest display step. If that step is under 4x body, get contrast from weight and space, and propose a display token rather than inventing a size. |
| Atmosphere | Only if the system has a gradient, material or illustration token for it. Otherwise none, and say so. |
| Bespoke element | Still required. Draw it by hand with the system's tokens so it looks like it shipped with the library, and propose it as a component. |
| Patterns | The system's own pattern first. Use this skill's pattern files only where the system has none, and say so. |
| Compare loop | Score `peak.md` as usual, plus the system rubric in section 8. |

## 5. Departing from the system

Departures are allowed when the brief needs something the system cannot do, but never silently:
- State what departs, which rule or pattern it departs from, and why, in one line each.
- Keep it inside an expression zone and build it from tokens.
- Offer it back as a proposal (a token or component request) so the system can absorb it.
- List departures in the deliverable under "Departures from the system". Zero departures is fine;
  undeclared departures are not.

## 6. Proposing additions

When the inventory shows a gap, design the addition as the system would, and hand it over as a
proposal, not a fork:
- **A display type token** when the largest step cannot carry a hero (give size, weight, tracking,
  line-height, and which screens use it).
- **A data palette** when the system has only brand and semantic colours: 3-8 hues that hold
  against the system's surfaces, ordered, with dark variants (`tools-and-analytics.md` §6 shows the
  shape).
- **The bespoke element as a component**: its anatomy, states, tokens used and accessibility notes.
- **A missing pattern** (an approval queue, a check-your-answers page): anatomy and copy, citing the
  pattern file in this skill that it came from.

## 7. How a system design goes sloppy

| Tell | Why it reads as slop | Do instead |
|---|---|---|
| Every section is the default card, same padding, same title row | A component dump; nobody composed the page | Compose first (hero, supporting regions), then choose components for each region |
| The default template with placeholder copy | The template was the design | Templates are skeletons; fill them with the content inventory and a hero |
| Raw hex, magic pixels, a restyled component | Breaks theming, dark mode and the next release | Token roles only; if none fits, propose a token |
| An alert or notification badge used for a neutral count | Colour says "problem" when nothing is wrong | A neutral count in the trailing slot; reserve alert colours for alerts |
| A second accent "for variety" | The system's one accent stops meaning "act here" | One accent, as the system defines it |
| The system's illustration style replaced with stock or 3D | The brand loses its voice | Use the system's illustration or none |
| Copy that ignores the content guide (Title Case, "Oops!", vague errors) | Reads as a different product | Follow the voice layer; write errors that say what to do |
| A bespoke element in a foreign style (a library chart, a glass card) | Looks pasted in | Draw it with the system's tokens |

## 8. System review rubric (add to the compare loop)

1. **Token purity**: no raw colour, size or radius values outside proposed additions.
2. **Component fidelity**: components used as their API intends; no restyled internals.
3. **Pattern match**: every section maps to a template or pattern, or the gap is stated.
4. **Signature present**: the system's signature is visible and the screen still has a hero.
5. **Bespoke element native**: built from tokens, proposed as a component.
6. **Voice**: copy follows the content guide.
7. **Departures declared**: listed with reasons, or none.
Ready when all seven hold and the `peak.md` score meets its own bar.

## 9. Worked example: Alchemy (Allica Bank)

Alchemy is Allica Bank's web design system (`@allicabankltd/alchemy-web`). Its layers map directly
onto section 1: page templates in `docs/templates/index.json`, patterns in `docs/patterns/index.json`,
the house-style guide in `docs/DESIGN.md`, component APIs in `dist/components/<Name>/*.d.ts`, and
tokens as semantic classes. Read template → patterns → DESIGN.md, in that order, before sketching.
Component behaviours that bite (fixed colours, default padding, version differences) are listed in
the `alchemy-ui-change` skill's gotchas file; check it before using a component in a design.
Design here, then hand implementation, the before/after page and the PR to `alchemy-ui-change`.
Customer-facing banking screens may need Compliance or Legal review before publication.

Other systems: a themed Material or HIG product follows `platform-native.md` for the chrome and this
file for the brand layer; Carbon, Polaris, Atlassian and GOV.UK follow `systems.md`.
