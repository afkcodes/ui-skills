# Stances: the bold move that makes a screen stop the scroll

Every reference that stays in the memory commits to one visual stance and one signature move, then
executes everything else quietly around it. Generic output has no stance: white cards, one blue
accent, same radius, a donut. Before designing, choose from this menu (or invent one of equal
confidence) and name it in the design brief. Numbers point to `design-notes.md`.

Rule: one stance per product, one signature move per screen, held consistently. Two stances on one
screen is noise; zero is slop.

## Stances (whole-product direction)

| Stance | What it looks like | Best for | References |
|---|---|---|---|
| **Gradient band** | A deep two-tone gradient (red→orange, navy→blue, violet) as a header band or one hero card; everything below is bone-white cards with faded decimals | Consumer banking, wallets | 076, 083, 017, 020, 012 |
| **Ink and bone** | Near-black and warm white only; one tiny accent chip; benefit sentences as card titles; black filled primaries | Business banking, B2B tools that sell precision | 046, 023, 089, 090 |
| **Dark with one acid** | #141416 surfaces, cards one step lighter, a single acid accent (lime, electric blue, orange, violet) on selection and the primary only; capsule bars; hatching for inactive | Fintech, analytics, crypto, ops | 029, 037, 054, 059, 060, 092 |
| **Pastel block colour** | Three or four *saturated* pastels (lilac, cyan, hot pink, acid yellow) as whole-card fills by category, black type and black buttons on top; or pastel on four small tiles only. Never the milky lilac/mint/peach set | Consumer finance, neobanks, playful SaaS | 092 |
| **Serif wealth** | A heavy, high-contrast serif for the page title or (rarely) numerals at 32-44px, sans for everything else; generous white; hairlines instead of cards; numbers on the page surface. 093 achieves it with no serif at all | Wealth, investing, premium accounts | 081, 027, 017, 093 |
| **Editorial** | Magazine headline (small eyebrow + huge display), a floating insight card, asymmetric grid, big type as the hero | Reporting dashboards, insights products, marketing | 042, 049, 069, 009, 117, 209 |
| **Monochrome data** | One hue in three tints for all data; hatch, dot and weight as the second encoding; everything else grey | Any dense dashboard where legibility wins | 052, 069, 011 |
| **Swiss boxes** | Square corners, 1px rules, flat primaries, a treemap or grid as the hero, uppercase micro labels | Insurance, contracts, admin | 023, 046, 036, 197, 199 |
| **Brand-loud** | Saturated brand colours, illustration, condensed uppercase type, chunky outlines; everything follows the same loud rules | Hospitality, consumer brands, campaigns | 007, 010, 014 |
| **Analyst's grid** | White or near-white page, hairline cards on a 12-column grid, a north-star metric row, a categorical palette that holds at eight series, 12-13px type, borders not shadows; the flourish is a chart type drawn precisely (retention triangle, funnel). The default for product analytics, admin and ops tools; see `tools-and-analytics.md` | Analytics, observability, admin, dev tools | 036, 052, 063, 060 (dark) |
| **Soft glass on gradient** | One ambient gradient page, frosted cards, soft shadows; use sparingly and keep text dark | Wellness, lifestyle, onboarding | 024 |
| **Neo-brutalist** | Black 1.5-3px outlines, flat fills, a hard offset shadow (4-6px, no blur) on what can be pressed, one loud colour on the action region; square corners for tools. Raw variant: no colour, the grid drawn as rules, mono facts | Consumer, education, community, dev-tool marketing; quiet variant for small B2B tools | 195, 196, 197, 007 |
| **Bento** | 5-7 unequal tiles, one hero at least 1.5x the next, each tile a real product fragment or one magnified control; neutral tiles plus one accent tile | Feature sections, launch heroes; dashboards as unequal cards | 198, 199, 200, 046; negative 201 |
| **Tactile object** | Flat screen with one lit physical control (knob, dial, roller) the user operates, its value repeated as a flat number in the accent | Device, home, media and camera control | 202, 200, 006 |
| **Retro source** | One period medium (printed menu, 90s desktop) shapes the grid or the IA; one ink and one spot colour; period display for headlines only; texture on the ground | Hospitality, music, culture, campaigns, youth commerce | 203, 204 |
| **Terminal** | Mono, #0A0A0A ground, one phosphor accent, `key : value` facts, scales under bars, logs with timestamps, a wireframe of the real object | Dev tools, ops, security, infra, crypto, hardware | 205, 206, 122, 015; negative 133 |
| **Collage** | Palette sampled from the product, one condensed display face, four or five collage devices repeated, loud and quiet bands alternating, plain chrome | Food and drink, fashion, music, D2C brands | 207, 007; negative 208 |
| **Spatial object** | One rendered object (the product or the reading) behind flat, frontal UI; motion on interaction only; static fallback | Hardware, automotive, launches; one render on a home screen | 013, 015, 027, 091, 100 |

The last seven rows are aesthetic movements; their tokens, domain limits and sloppy versions are in
`languages/movements.md`, which must be read before choosing one. When the design language is
platform-native or a public / enterprise system (`languages/README.md`), the stance works inside it:
most of this table is then out of bounds for chrome and applies only to the content area.

## Signature moves (one per screen)

- A hero number set at 48-56px in the body sans at 600 with faded decimals (076, 083, 093); or in a heavy serif at 36-44px (081).
- A treemap for composition instead of a pie (023).
- A dot-matrix or barcode bar chart (040, 046, 081).
- Capsule bars with the selected one filled and labelled inside (054, 059, 092).
- A dark card on a light page as the single primary action (092 exchange panel; 046 calculator).
- A card title that is a benefit sentence ("Forecast your end-of-month balance in seconds": 046).
- A full-bleed gradient header holding only the greeting, actions and the balance (076).
- Day-grouped list with a subtotal per day (068).
- A timeline stepper for a payment's lifecycle (017).
- An insight sentence with the number highlighted inside it (060).
- Icon-only nav where the active item expands to icon + label (003, 008, 069).
- A Sankey or cohort grid for flow or retention (037, 030).
- A segmented, discrete gauge (portions, not a smooth %) (014).
- Status row strips coloured by state on a widget.
- A diverging in/out bar chart around a zero line (049).

## How to pick

1. Read the brief's tone words and domain. Map to one stance (two candidates at most).
2. Check the brand constraints: an existing accent usually decides between Gradient band, Dark
 with one acid, and Monochrome data.
3. Choose the signature move that serves the screen's one idea (a composition → treemap; a
 lifecycle → stepper; a balance → hero numeral; a trend → capsule bars).
4. Write the stance and move into the design brief as a sentence: "Ink-and-bone business banking;
 the hero is a 56px serif balance over a dark cash-flow calculator card."
5. Everything else on the screen is executed to `craft.md` and stays quiet.

## The scroll-stop test (run before showing)

Imagine the screen as a thumbnail in a feed of a hundred dashboards. Would it be the one you tap?
If the honest answer is "it looks like a nice template", the stance is missing or diluted:
either the signature move is too small, the colour has crept back to default blue-on-white, or the
hero number is not big enough. Fix the one thing, not everything.
