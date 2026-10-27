# Movements: aesthetic design languages

A movement is a stance with a history: tokens, details and habits people recognise by name. Read
this file when the mood words or references name one (`README.md` §1). The movement then **is** the
stance: it replaces a row of `../stances.md`, and each screen still needs its own signature move and
bespoke element. Numbers point to `../design-notes.md`; 195-209 are the movements batch.

Rules that hold for every movement:
- One movement per product. A movement's tokens dress the chrome and components; the content still
  obeys `../principles.md` (one primary, status as text, numbers as type, real copy).
- The sloppy version of every movement is the **costume**: its surface tokens on a layout with no idea.
- The accessibility floor does not move: text 4.5:1 (3:1 at 24px+ or 18.66px bold), component
  boundaries and states 3:1, no meaning by colour alone, targets at least 24×24 CSS px (WCAG 2.2).
- Movements spend decoration. They obey the domain budget in `../principles.md` §10:

| Movement | Spend freely | Restrained use only | Never |
|---|---|---|---|
| Neo-brutalism | Consumer, education, community, dev-tool marketing | B2B tools and settings (196) | Payment confirmation, money errors, consent, regulated disclosures |
| Raw brutalism | Studios, architecture, culture, portfolios | Marketing for B2B | Any form or product flow |
| Bento | Feature sections, launch pages, product heroes | Dashboards (as unequal cards, 046) | Lists of equal items; anything that is really a table |
| Tactile | One control in a device, media or home app | One delight moment on a secondary screen (006) | Dense tools; money inputs |
| Retro / Y2K | Hospitality, music, culture, campaigns, youth commerce | Brand campaign pages for a bank | Product flows in banking, health, government |
| Terminal | Dev tools, ops, security, infra, crypto, hardware control | Analytics for technical users | Consumer onboarding; long reading; non-technical audiences |
| Maximalist / collage | Food and drink, fashion, music, D2C brands, campaigns | An about or story page for a calm brand | Tools, forms, money flows |
| Spatial / 3D | Hardware, automotive, launches | One render on a home screen (013, 027) | Dense tools; text on a tilted plane |

For banking at Allica: movements belong to marketing and campaign surfaces; product money screens use
the quiet stances in `../stances.md`. Customer-facing output may need Compliance or Legal review.

Sources (WCAG 2.2): https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html ·
https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html ·
https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html

## 1. Neo-brutalism (and raw brutalism)

**Definition.** Outline, flat fill and a hard shadow applied as one rule to every interactive
surface, with one loud colour spent on the action region.

**Tokens.**
- Type: brand-loud or a heavy grotesk at 700-900 for titles, a plain sans for body (`../typography.md`
  §2). Faces: Archivo Black, Archivo 800, Rubik 800, Space Grotesk 700, Familjen Grotesk 700; the
  quiet product variant uses a neutral grotesk at 700 (196).
- Colour: warm off-white page (#FAF4F0, 196), black ink, one loud fill (yellow #FFD43B, 195), at most
  one semantic set (green for done, coral for urgent: 195).
- Borders: 1.5-3px solid black on cards, inputs, chips, segments and buttons (196, 195, 007's 2px).
- Shadow: `box-shadow: 4px 4px 0 0 #000`, offset 4-6px, **zero blur** (195, 196). No soft shadow
  anywhere on the screen.
- Radius: 0 for the product variant (196); 12px cards with pill chips for consumer (195). One choice.
- Grid: full-width stacked blocks; one bordered container per list, rows split by 1px or dotted rules.
- Imagery: flat line illustration or photos clipped inside outlined frames (195).

**Signature details.** Segmented control with the active half filled black (195, 196); outlined date
and tag chips (196); icon in an outlined square (196); the loud colour as a full band behind the
header or the whole screen of a single-purpose step (195 log in); sticky primary with the shadow.

**Raw brutalism** is a different movement with the same name: no colour and no offset shadow. The
grid is drawn as 1px rules that run past the panels, type is set as architecture (a word vertical at
column height), facts are mono numerals, grain sits on photographs only (197).

**Sloppy → do instead.**
- Shadow on every element, including static text cards (195's weak point) → shadow only on what can
  be pressed; on a tool, on one or two elements per screen (196).
- Lime button with an offset shadow on an otherwise default template, sparkle stars, stock cut-outs
  → the rule must reach every component, or choose another stance.
- Emoji in labels and as tab icons (195) → one outlined icon set at one stroke.
- Raw brutalism with glass stat tiles or garbled placeholder text (197's weak points) → solid panels
  and written copy; the rawness is in the grid, not in unfinished content.

**Evidence.** 195, 196, 197; 007 for the loud, outlined tone held consistently.

## 2. Bento grids

**Definition.** A composed grid of unequal tiles, each showing one fragment of the product, one of
them clearly the hero. The uniform version (equal tiles, an icon each) is banned in `../typography.md` §5.

**Tokens.**
- Type: the product's own voice; tile titles 20-24px with one sentence below (198); the hero tile
  may carry the page headline at display size (200's ~80px "Film like a pro.").
- Colour: neutral tiles plus **one** accent tile (200's orange); or muted fills from one family with
  every tile drawn in a single ink (199). Never a different tint per tile for its own sake.
- Radius 24-28px with gutters ~16px (200); square tiles are equally valid with a Swiss stance.
- Grid: 5-7 tiles. Widths follow content (198 splits a row 2:3 so the chart gets 3/5); heights vary,
  in offset columns (199). The hero tile is at least 1.5x the next largest (198).
- Imagery: cropped live UI fragments faded at one edge (198), product micro-visualisations (199),
  one control magnified 3-4x (200). Renders only in one tile.

**Signature details.** Tiles cropped by the frame or viewport so the product seems to continue
(199); a fragment that keeps its real values (198's tooltip with $5210 / $4535 / $4805); one tile
that is pure type on the accent (200); in a product dashboard, one dark card as counterweight among
light ones (046). On mobile the bento becomes one column ordered by importance.

**Sloppy → do instead.**
- 3×2 equal tiles, a tint and an icon each, platitude copy (201) → unequal spans, one hero, a real
  fragment per tile.
- Covering the hero tile leaves the grid looking the same (`../peak.md` §1) → enlarge it, cut tiles.
- Rainbow photo tiles inside a perspective laptop → flat, full-frame tiles of the product.
- Milky pastel per tile (198's weak point) → neutral tiles and one accent, or one-ink fills from one
  family (199).
- Template tokens in tile copy ("{projectName}", 198) → proofread the fragments; they are content.

**Evidence.** 198, 199, 200; negative 201; 046 for bento logic inside a dashboard.

## 3. Tactile / skeuomorphic (neumorphism as the caution)

**Definition.** One physical-looking object on an otherwise flat screen, and the object is a control
the user operates, with its value repeated as a flat number.

**Tokens.**
- Type: a technical grotesk (Space Grotesk, Sora, Geist); the value at display size (202's "72%" at
  ~64px) in the accent; labels small and flat.
- Colour: dark slate ground (#1E272F with panels #445762, 202) or charcoal (#101010, 200); one warm
  accent for the active value and the arc (#EB7500, 202; #E75324, 200).
- Light: one source, from above; specular highlight and glow only on the object and its active arc.
- Shadow: soft and directional under the object only; every other surface flat.
- Shape and grid: the object is round or follows the real device and takes ~40% of the screen height
  (202); readings sit in a 2×2 grid above it.

**Signature details.** − and + at the ends of the arc (202); a roller with the selected value in a
lit pill (200's ISO 600); a dial with real degree marks (200); a dial with a lamp render (006).

**Neumorphism, the cautionary case.** Same-colour surfaces extruded with paired light and dark soft
shadows. A raised field's boundary and the raised / pressed difference are carried by shadow alone,
so they rarely reach WCAG's 3:1 non-text contrast. 202's variant B removes the tile borders entirely
and loses nothing: the knob is the only object that needed depth.

**Sloppy → do instead.**
- Glow on every slider, button and knob → one object; the rest flat.
- A reading drawn as a knob (`../anti-slop.md`) → knobs for input only; readings as numbers, arcs
  or dots (013's sphere is a reading and is not grabbable).
- Neumorphic fields with no border → 1px border or a value step of at least 3:1, focus ring visible.
- Unlabelled numbers ("239", 202) → every value gets a label and unit.

**Evidence.** 202, 200; 006, 013. Sources:
https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html

## 4. Retro / Y2K

**Definition.** One period source medium (a printed menu, a 90s desktop, a 70s poster) whose
structure becomes the layout, held in one ink and one spot colour.

**Tokens.**
- Type: a period display face for headlines only; a plain sans for body (204 sets body in the
  display face and it reads slowly). Faces: Bungee, Shrikhand, Righteous, Fraunces with its soft axis
  for the 70s; Silkscreen or VT323 for pixel UI labels only.
- Colour: ink + one spot on paper (black + #FDC74B on #F9F8F2, 204); or pale windows (#F6DBE2) over
  one loud iridescent wallpaper (203). The loud colour lives in one layer.
- Borders: 1px rules forming cells (204); 1px window borders with a ~22px title bar (203).
- Shadow: hard grey offset 3-4px under windows, no blur (203); an extruded headline shadow (204).
- Radius: 0, or the period's own (clipped photo corners, 204).
- Texture: grain on the paper ground; scan lines on the wallpaper; never over text or data.
- Imagery: period illustration (rubber-hose mascots, 204), black-and-white photography.

**Signature details.** The metaphor carries the navigation: windows as sections and desktop icons as
links (203); a nav row of equal ruled cells and price cells ending in a spot-colour arrow square
(204); hatched dividers (204); a menu-bar clock and status glyphs (203).

**Sloppy → do instead.**
- Grain + sparkle stars + offset shadow + "Y2K" chrome type on a standard template → choose a source
  medium and let it set the grid or the IA (203, 204).
- One paragraph repeated as filler, "950 CALORIES" on every item (204) → write real, varied content.
- 10px text in overlapping windows hiding consent copy (203) → body ≥ 14px; windows may overlap
  decoration, never a form or legal text.
- Glitch, flicker or strobing → no more than three flashes in any second (WCAG 2.3.1).

**Evidence.** 203, 204. Sources:
https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html

## 5. Terminal / mono

**Definition.** A live instrument rendered as a console: mono type, one phosphor accent, facts as
`key : value`, and the log as content.

**Tokens.**
- Type: mono throughout (205, 206) or mono for data with a tight grotesk for headings. Faces:
  JetBrains Mono, IBM Plex Mono, Geist Mono, Martian Mono, DM Mono. Uppercase small labels; the
  largest figure ~40px (205's "90%"); no paragraph longer than two lines in mono.
- Colour: ground #0A0A0A-#0B0B0D; one accent (mint #73F7D6, 205); semantic red / green only in logs
  and status (206); a 2px accent tick before section titles (206's #FF6600).
- Borders: 1px panel frames; corner-bracket marks instead of full boxes (206). Radius 0.
- Shadow: none. Atmosphere at most a faint grid behind the hero drawing (205).
- Grid: dense; aligned colons in `key : value` blocks (205, 206).
- Imagery: a wireframe line drawing of the real object with readings on leader lines (205; 015's
  wireframe car); dot-matrix maps (206).

**Signature details.** The scale printed under every bar ("125 GB … 210 GB", 205); discrete segmented
bars (205); bar-glyph meters "|||||||| 84/112" (206); log lines with timestamps and coloured keywords
(206); AI output as `>`-prefixed lines inside the panel it informs, with approve / cancel directly
below (206); "Last sync" with seconds and time zone (206); mono for paths, IDs and times (122, 010).

**Mode.** Most terminal products are tools: run tool mode (`../tools-and-analytics.md`) with
terminal as its stance.

**Sloppy → do instead.**
- HUD chrome: angled corners, glowing cyan outlines, every chart a different palette (133) → plain
  frames, one accent, the data loud and the chrome quiet.
- "Ø" for "O", fake hex dumps, unexplained number columns (205's weak points) → real characters, real
  values, every number labelled.
- Two colour systems per table row (status dot plus coloured priority word, 206) → one carries
  colour; the other is a word in the default ink.
- Borrowed menace (agency seals, surveillance tiles, "CLASSIFIED" chips, 206) → the product's own,
  honest context.

**Evidence.** 205, 206; 007, 010, 015, 122; negative 133.

## 6. Maximalist / collage

**Definition.** Density and noise as the brand, held together by a palette taken from the product, a
single display face and a small kit of collage devices repeated everywhere.

**Tokens.**
- Type: one condensed display face in uppercase for headlines and the manifesto (207); chrome (nav,
  footer lists, inputs, buttons) in a plain sans. Faces: Anton, Big Shoulders Display, Bebas Neue,
  Archivo ExtraCondensed.
- Colour: 4-6 colours, all sampled from the product or its packaging (207: oxblood #370E0C, cream
  #FEF9F3, olive #6A8767, mustard #DABD96, brick #AA4922, wine #641B31).
- Devices (choose four or five, repeat them): a word boxed as a tilted sticker; photo pills inline in
  display text; text set on a circular path around the product; fanned, tilted cards; a wavy section
  edge; line drawings ghosted at ~8% behind text (all 207).
- Borders and shadow: sticker outlines and a soft paper shadow under stickers and cards only.
- Composition: alternate a loud band with a quiet one (207's dark hero, then a cream manifesto).

**Signature details.** The manifesto set as display type with photos in the line and a giant
logotype closing the footer (207); in a product, every element following the same loud rules (007).

**Sloppy → do instead.**
- Every border a different kind, every number a different colour, confetti shapes (208) → one
  border style, one ink for figures, devices with a reason.
- Text on circular paths carrying real information, cards that crop their own titles (207's weak
  points) → paths and fans for decoration; information stays horizontal and whole.
- Maximal chrome → nav, buttons and forms stay plain so the user can still act.

**Evidence.** 207; negative 208; 007. See also Brand-loud in `../stances.md`.

## 7. Spatial / 3D (non-platform)

**Definition.** Depth used as a material on a web or app screen outside visionOS (that platform is
in `platform-native.md`): one rendered object, with flat UI in front of it.

No keeper in this batch; the rules come from the existing set. A WebGL Awwwards site of the day,
captured headless for this section, rendered only its "WebGL2 is not supported" line.

**Tokens.**
- Type: a tight grotesk (Inter Tight, Geist); text always on a flat, front-facing plane.
- Colour: a neutral ground, with the render supplying the colour and light.
- Depth: one object, and it is the product or the reading (015's car, 027's card, 013's score as a
  sphere); in a bento, one tile (200).
- Motion: depth moves on interaction only and stops for `prefers-reduced-motion`.
- Imagery: the object; UI fragments may float around it only when they are real UI (091's fragments
  around a globe; 100's icons tumbling out of a real timeline component).

**Sloppy → do instead.**
- Tilted devices, glass cards floating in an ambient room, text on a perspective plane
  (`../anti-slop.md`) → the UI flat and frontal; depth behind it.
- A WebGL-only page → a static image and full HTML content that render without WebGL.
- Motion on scroll with no off switch → honour reduced motion (WCAG 2.3.3).

**Evidence.** 013, 015, 027, 091, 100, 200. Sources:
https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion ·
https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html

## 8. Swiss / International: what is new

`../stances.md` already has **Swiss boxes** (square corners, 1px rules, flat primaries, uppercase
micro labels; 023, 046, 036). New from this batch:
- **Draw the grid.** 1px rules that run past the panels and through the page make the alignment
  visible (197); a printed-menu grid of ruled cells does the same in a retro voice (204).
- **Headline as statement.** Uppercase tight grotesk, flush left, with full stops ("OUTSOURCE
  YOURSELF. TO YOURSELF.", 199); one flat accent shared by the CTA and one tile (199's red).
- **Type as structure.** One word set vertically at column height (197); facts as mono numerals with
  units (197's 120,000 m²).
- Sloppy → do instead: "Swiss" as Helvetica, red and white space with everything centred and no
  grid → flush left on a visible grid, ragged right, one accent.

## 9. Editorial: what is new

`../stances.md` already has **Editorial** (magazine headline, floating insight card, asymmetric
grid; 042, 049, 069, 009) and 117 shows the report-as-dashboard. New from this batch:
- **The zine variant.** A heavy condensed grotesk for display with mono for deks and metadata (209);
  category and date as small chips above each headline (209).
- **Marginalia.** The brand's stance in handwriting, twice per page at most, in the accent (209). It
  is the third face, so it is allowed only as an aside.
- **Sequence by dimming.** In a three-up grid, unfocused headlines dim to grey so the eye reads one
  at a time (209); the full-width accent "Read more" belongs to the featured post only.
- **Manifesto as display.** A short brand paragraph set in the display face with photo pills inline
  (207), once per page.
- Sloppy → do instead: a thin display serif at 60px+ with an italic word (`../typography.md` §5) →
  a heavy condensed grotesk or a heavy serif; mono body beyond two lines → plain sans body.

## 10. How each movement changes the peak rubric

Score a movement screen on the eight qualities in `../peak.md` as usual, with these targets. Bold
marks the quality the movement lives or dies on.

| Quality | Neo-brutalism | Bento | Tactile | Retro / Y2K | Terminal | Collage | Spatial |
|---|---|---|---|---|---|---|---|
| Composition | As `peak.md` | **The movement: one hero tile** | Object ~40% of height | Set by the source medium | Tool grid (tool mode) | Loud and quiet bands | Object behind flat UI |
| Scale | Heavy titles | Hero tile at display size | Value ~64px | Period display | Nothing over ~40px | Display caps | As `peak.md` |
| Atmosphere | Replaced by the hard shadow | One tile | **The object's light only** | On the ground (paper, wallpaper) | None; a faint grid at most | Decoration layer, never a control | **The render, nothing else lit** |
| Bespoke element | Drawn in the rule | Inside a tile | The control | **The metaphor** | Object drawing or the log | The device kit | The object |
| Typographic character | Weight, not a second face | The product's voice | The value numeral | Period face, headlines only | Mono | One display face | As `peak.md` |
| Micro-detail | Risk: one outline flattens hierarchy | Real values in fragments | Labels and units | Period details | **Strength: scales, timestamps** | The devices | Labels on the UI plane |
| Real content | As `peak.md` | Fragments are content | Risk: one value, no states | Risk: filler | Logs and scales | Risk: decoration over copy | As `peak.md` |
| Confidence | **Strength** | One hero | One object | Strength | Strength | **The whole game** | One object |

## 11. In the stances menu

Each movement above has a one-row summary in `../stances.md` (Neo-brutalist, Bento, Tactile
object, Retro source, Terminal, Collage, Spatial object), and the Swiss boxes and Editorial rows there
cite 197, 199, 117 and 209. This file stays the source for tokens, limits and sloppy versions.
