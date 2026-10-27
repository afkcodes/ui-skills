# Design languages: choosing the rules the screen obeys

A design language is the set of rules a screen must obey before any stance or signature move: the
platform's, a public or enterprise system's, a company's own, or an aesthetic movement's. The
reference set's peak screens are mostly custom products with no language to obey; most real briefs
have one. Choose it right after the interview, write it into the brief, and read the file it points
to before step 3.

## 1. Decide in this order

1. **Does a design system already exist for this product** (tokens, a component library, a Figma
   library, a brand book)? → `brand-systems.md`, plus the file for whatever it is built on. Never
   design past an existing system.
2. **Is it a native app** where users expect the platform (Android, iOS / iPadOS, macOS, Windows,
   visionOS)? → `platform-native.md`. A brand system then sits on top of it.
3. **Is it built on, or required to follow, a public or enterprise system** (GOV.UK, Carbon,
   Polaris, Atlassian), or is it a **form-heavy transactional service** (apply, register, claim,
   renew)? → `systems.md`; transactional services run in its **service mode**.
4. **Otherwise it is a custom product.** Choose a stance from `../stances.md`. If the mood words or
   the user's references point to an aesthetic movement (neo-brutalist, bento, tactile, retro / Y2K,
   terminal, maximalist / collage, spatial, Swiss, editorial), read `movements.md`; the movement is
   then the stance.

Tools (analytics, admin, ops, dev tools) also read `../tools-and-analytics.md` whatever their
language; admin, access, approval and agent screens use its workflow variant (§11).

## 2. How the layers stack

| Layer | What it decides | One per | Where it comes from |
|---|---|---|---|
| Language | Chrome, components, tokens, materials, motion, what may never be overridden | Product | This folder |
| Brand layer | Colour, type, illustration and voice inside what the language allows | Product | `brand-systems.md` (the company's system) |
| Stance | The visual direction within what the language and brand allow | Product | `../stances.md`, or the movement |
| Signature move | The one bold thing a screen does | Screen | `../stances.md` |
| Bespoke element | The thing invented for this screen, drawn in the language's materials | Screen | `../ideation.md` |

Allowed stacks: native + brand (a themed Material or iOS app); system + brand (a Polaris app with a
merchant's brand; Carbon for an IBM partner); custom + movement. Not allowed: two languages on one
screen, or a movement worn over native chrome.

A mode (tool, service) is not a language: it sits beside the stack and decides the screen's
structure and rubric, while the language decides the look. The combined cases:

| Brief | Language (the look) | Mode (structure and rubric) | Score |
|---|---|---|---|
| Identity check or application inside a native app | Platform-native (+ brand) | Service mode: one thing per screen, check answers, errors, every ending | Service rubric, with the platform's adjustments in §3 |
| Shop: product page, basket, checkout | Custom + stance (or a movement) | Consumer for product and basket; service mode for checkout and payment | Peak eight for the first two; service rubric for checkout |
| Admin, team access or settings inside Carbon, Polaris or Atlassian | The system | Tool mode, workflow variant (`../tools-and-analytics.md` §11) | Workflow rubric, plus the system's sloppy-version checks (`systems.md` §8) |
| AI agent console, approvals, ops queue | Custom (or the company's system) | Tool mode, workflow variant | Workflow rubric |
| Analytics inside an enterprise system | The system | Tool mode, analytics | §10 of the tools file, plus the system checks |
| Marketing site for a developer tool | Custom + movement | Marketing (not tool mode, whatever the product is) | Peak eight, with the movement's rules |
| Public service not hosted on GOV.UK (council, NHS trust, a company) | The organisation's own brand on GOV.UK patterns, no crown or GDS Transport | Service mode | Service rubric |

Where the language and the mode still collide (the platform asks for atmosphere on chrome, service
mode asks for none), the language wins on how things look and the mode wins on what is on the
screen and in what order. Every rubric has the same pass bar: nothing missing, at most one weaker.

## 3. What each family changes in the peak rubric

The eight qualities in `../peak.md` were read off custom products. Each family adjusts them; the
detail is in its file.

| Quality | Custom (+ movement) | Platform-native | Public / enterprise system | Service mode |
|---|---|---|---|---|
| Composition | As `peak.md` | Inside the platform's layout regions | Inside the system's grid and templates | One thing per page; the question is the composition |
| Scale | Largest text ≥ 4x body | The platform's largest type role | The system's largest heading | The question as the h1; nothing larger |
| Atmosphere | One lit place | The platform's material on chrome (glass, Mica, tonal surfaces); content stays matte | Usually none | None |
| Bespoke element | Required | Required, in the content area | Required where the system allows (data, summaries), drawn with its tokens | Rarely; clarity is the flourish |
| Typographic character | From the voice | From the platform's scale, set well | From the system's scale, set well | Plain and large |
| Micro-detail | Four or five per screen | Native details (haptics, context menus, swipe actions) count | The system's details, applied consistently | Hints, error messages, change links |
| Real content | Always | Always | Always | Always, in plain English |
| Confidence | One stance held | The platform held, the brand clear | The system held | The service says what will happen and when |

## 4. Files

| File | Covers |
|---|---|
| `platform-native.md` | Material 3 and M3 Expressive, Apple HIG and Liquid Glass, visionOS, Fluent 2; one product across iOS and Android |
| `systems.md` | GOV.UK, IBM Carbon, Shopify Polaris, Atlassian; service mode and its rubric |
| `movements.md` | Neo-brutalism, bento, tactile / skeuomorphic, retro / Y2K, terminal / mono, maximalist / collage, spatial / 3D, and what is new for Swiss and editorial |
| `brand-systems.md` | Designing inside an existing system: inventory, signature, expression zones, departures, proposals, the system rubric, Alchemy as the worked example |

Reference numbers for each language are in its file and in `../design-notes.md`; search with
`../../scripts/find_refs.py <language> <pattern>`.
