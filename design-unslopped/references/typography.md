# Typography: choosing type for the design in front of you

Type is chosen from the brief, the way the references vary it: a restaurant-ops app (007) and a
wealth dashboard (081) share nothing typographically, and both are right. This file gives the method
and the evidence. It replaces any single default; if two products from this skill share a type
system without sharing a brand, the method was skipped.

Order of operations: 1) classify the brief into a voice; 2) take the voice's roster and rules;
3) check the three references chosen in step 2 of the workflow and cite them beside each choice;
4) apply the numerals module if the screen carries numbers; 5) run the exclusion check.

## 1. Classify the brief into a voice

| Brief traits (domain · tone · platform · stance) | Voice | Evidence |
|---|---|---|
| Banking, payments, insurance, ops, logistics, admin · precise, trustworthy · web app or mobile · ink-and-bone, monochrome, gradient band | **Neutral grotesk** | 011, 027, 031, 036, 046, 057, 080, 085, 088 |
| Analytics, crypto, dev tools, AI products · sharp, technical · dark UI | **Tight modern grotesk** | 029, 054, 060, 063, 092, 037 |
| Consumer apps: neobank, health, food, travel, family · friendly, light · mobile · pastel block or soft | **Friendly geometric** | 008, 013, 014, 020, 072, 082, 018, 022 |
| Healthcare, therapy, insurance for consumers · calm, human | **Humanist sans** | 021, 002, 023 (Swiss variant), 075 |
| Wellness, meditation, lifestyle · airy, soft · glass or gradient | **Light rounded geometric** | 024, 003, 025 |
| Wealth, investing, premium accounts, hospitality · quiet luxury | **Editorial: heavy serif + sans** | 081, 071, 017 (title only), 027 (headings only), 093 (achieves it with no serif) |
| Marketing landing pages, campaigns, portfolios · persuasive, cinematic | **Display serif or display sans headline + sans body** | 086, 099, 091, 096, 098, 087 |
| Hospitality, sport, food & drink brands, youth · loud, illustrated | **Condensed / uppercase brand-loud** | 007, 010 |

If a brief sits between two rows, pick by the tone adjectives the user gave; if they gave none, pick
by the platform (mobile consumer → friendly geometric; desktop tool → neutral grotesk) and say so.

## 2. Voices: roster, settings, what the references do, what to avoid

Each roster lists faces that read like the reference, available on Google Fonts or Fontshare.
Choose one per product and avoid the one you used last time; the roster is long on purpose.

### Neutral grotesk
- Roster: Inter, Geist, Schibsted Grotesk, Hanken Grotesk, Public Sans, IBM Plex Sans, Instrument
  Sans, Onest, Figtree, Albert Sans, Be Vietnam Pro, Mona Sans.
- Settings: titles 600 at 16-18, body 400 at 14, labels 500 at 12, eyebrows 11-12 uppercase +0.06em.
  Hero numbers 600, −0.02 to −0.035em. Line-height 1.5 body, 1.1 numbers.
- Seen: 046 sets everything in one grotesk and gets character from benefit-sentence titles and black
  fills; 011 from weight and the pence; 057 from nothing but discipline.
- Avoid: adding a serif "for warmth"; pairing with a rounded geometric; weight 700 on numbers.

### Tight modern grotesk
- Roster: Geist, Söhne-alikes (Inter Tight, Instrument Sans), Space Grotesk (sparingly), Manrope at
  600+, Archivo, Familjen Grotesk, Bricolage Grotesque (display only), Host Grotesk.
- Settings: as neutral grotesk but tracking tighter (−0.03 to −0.045em on display), KPI numbers
  28-36, uppercase micro-labels at 10-11px. On dark, primary text #f5f5f5, weights one step lighter
  than on white (600 → 500) because light-on-dark looks bolder.
- Seen: 060 Insighta (tight grotesk, violet accent, 11px heatmap labels); 092 "+2.6%" at ~64px;
  029 lime on charcoal.
- Avoid: thin weights on dark; serif anything; letter-spaced body text.

### Friendly geometric
- Roster: Plus Jakarta Sans, Outfit, Urbanist, Sora, DM Sans, General Sans, Satoshi, Lexend,
  Nunito Sans (not Nunito), Wix Madefor Display, Gabarito, Red Hat Display.
- Settings: titles 600-700 at 18-22, body 400-500 at 14-15, generous line-height 1.5-1.6; buttons
  600; chips 500; hero numbers 600 at 32-40 on mobile with same-size decimals (004, 012, 020).
- Seen: 013 DailyMe pairs a geometric sans with a serif *italic* on the onboarding headline only and
  serif labels on the method chooser; the home screen is all sans. 072 Multipliiier: a geometric at
  500 with wide tracking in small caps for labels. 082: geometric with pastel tiles.
- Allowed flourish: one italic or serif word on an onboarding or empty-state headline (013), never
  on the money screen.
- Avoid: pairing with Instrument Serif or Playfair on product screens; 24px+ radii on every card; the
  milky pastel trio (use 071's saturated pastels or 082's four small tiles).

### Humanist sans
- Roster: Inter (humanist cut), Source Sans 3, Noto Sans, Fira Sans, PT Sans, Lato, Atkinson
  Hyperlegible, Open Sans (only at 600+ for titles), Merriweather Sans, Cabin.
- Settings: weight contrast inside a sentence (021: bold "Hi There!" + regular question), titles 600
  at 18-22, body 400 at 15-16 (larger for health), line-height 1.55.
- Seen: 021 MediFlow is almost monochrome; the two-weight headline carries the tone. 023 Northpoint
  uses a Swiss grotesk at small sizes with square corners.
- Avoid: display sizes above 32 on mobile; decorative faces; low-contrast grey on tinted cards.

### Light rounded geometric
- Roster: Poppins at 300-500, Outfit 300-500, Quicksand 500-600, Nunito 500-600, Comfortaa (display
  only), Varela Round, M PLUS Rounded 1c, Fredoka (display only).
- Settings: light weights at large sizes (024 "Dashboard" ~32px at 300), stats 500, generous
  tracking 0 to +0.01em, line-height 1.3 on titles.
- Seen: 024 Luma; 003 (terracotta ring, light headline "Let's start strong!"); 025 Cubee.
- Avoid: light weights below 16px; light weight on dark without raising to 400; mixing with a serif.

### Editorial: heavy serif + sans
- Roster (serif, for numerals or titles): Fraunces (opsz 72-144, weight 500-700), Newsreader 600,
  Source Serif 4 600, Libre Caslon Display, Gelasio 600, Young Serif, Instrument Serif only for
  titles on marketing pages (see next voice), DM Serif Display sparingly.
- Pair with a neutral grotesk for data (Inter, Hanken, Public Sans).
- Settings: serif numerals 32-44 at 500-600 (081 Vanta ~36px, 071 Novera ~40px); serif page or
  card titles 20-28 at 400-500 (027 "Card Overview", 071 "Transaction history"); everything else
  sans 400-500 at 13-14. Hairlines, not cards (093).
- Seen: 081 serif KPI numerals with sans labels; 071 serif titles + serif numerals with saturated
  pastels; 017 serif page title "Transactions." over a sans data UI; 093 reaches the same quietness
  with a sans only.
- Avoid: thin serif at 60px+; serif for table figures or chips; italic words on a product screen;
  serif + rounded geometric.

### Marketing: display headline + sans body
- Roster (display): Instrument Serif and Fraunces italic for editorial/wellness/fashion (086, 099);
  Bricolage Grotesque, Syne, Unbounded, Clash Display, Cabinet Grotesk, Manrope 800 for tech/SaaS
  (087, 096, 098); Archivo Black, Anton for campaigns.
- Settings: headline 48-72 at 2-3 lines; one italic or alternate-weight word allowed (086 "Move With
  *Meaning*"); subhead 16-18 regular; body 15-16; eyebrow chips 12 uppercase. Buttons 500-600.
- Seen: 099 "One platform for all your underwriting needs" in a serif with a sans body and a real
  product screenshot; 088 Quantexa all-sans enterprise; 091 Nexori geometric sans.
- Avoid: carrying the marketing serif into the product screenshot; more than one flourish per page.

### Condensed / uppercase brand-loud
- Roster: Roboto Condensed 700, Barlow Condensed 600-700, Archivo Narrow, Oswald, Bebas Neue
  (display only), Anton, Druk-alikes (Archivo Black), with a mono for labels (JetBrains Mono, Space
  Mono, IBM Plex Mono).
- Settings: titles uppercase 700 at 18-24 with +0.02em; labels in mono 10-11px; body a plain sans
  at 13-14; thick 2px outlines, chunky chips.
- Seen: 007 tubik (condensed uppercase titles, mono timers "2:59:12", monospace tags) and 010
  (thin wide display "Formula 1" over photography, mono-ish lap times).
- Avoid: using this voice for anything regulated; lowercase condensed body text; mixing two display
  faces.

## 3. Numerals module (applies inside every voice)

- Hero amount: 32-56 desktop, 28-40 mobile; exactly one per screen; the voice's display or body
  face at 500-600 (serif only in the editorial voice); tracking −0.02 to −0.04em (serif: 0 to
  −0.01em); `font-variant-numeric: tabular-nums`.
- Currency symbol: same face, size, weight and colour as the digits in 24 of 25 money references.
  Fade the decimals (55-65% size, 40-50% opacity) if you want a secondary element; never the symbol.
- Secondary amounts (KPI tiles 24-32, legend and rows 14-16) in the body face at 500-600; never a row
  of equal display-size numbers.
- Deltas as 11-13px chips or arrow + text beside the number; previous value or target in 12px grey
  under it.
- Negative with a true minus; signed positives only when direction matters; tabular figures in every
  list and table; locale-correct separators.
- Times and IDs may use the mono from the voice's roster at 12-13px (007, 010, 046).

## 4. Pairing and system rules (every voice)

- At most two faces: one body, one display in one role. Never two display faces.
- Five roles only: display, title, body, label/eyebrow, data. Each role has one size per platform.
- Weight range: pick three weights (e.g. 400/500/600) and never use a fourth.
- Tracking: tighten as size grows; never letter-space lowercase body text.
- Load the fonts (Google Fonts / Fontshare) with `display=swap`; never ship system-ui for a presented
  design; native iOS/Android implementations may use SF/Roboto, and the design should still name
  the web-loaded equivalent.
- Dark mode: drop one weight step and raise contrast; light mode: never pure black text.

## 5. The generated-UI signature (exclusions, applied per voice)

These are the type habits that mark output as generated. Each is allowed only where this file's
evidence shows it, and then only when at least two of the three references chosen for the brief do
it, cited by number.

- Instrument Serif or Playfair as a product-screen face (allowed: marketing headline, 086/099).
- A thin serif number above 60px (not in the set at all).
- A greyed or shrunk currency symbol (not in the set).
- An italic word on a product-screen headline (allowed: onboarding 013; marketing 086).
- Plus Jakarta Sans paired with any display serif (not in the set).
- The milky lilac/mint/peach/pale-blue set across a screen (allowed: 071's saturated pastels; 082's
  four small tiles).
- Four or more equal display-size numbers in a row (not in the set).
- 24px+ radii on every card and 999px on every button (allowed: pill tab bars and chips).
- A bento grid of uniform tiles with an icon or emoji in each (not in the set).
- Glass blur on every card (allowed: one overlay or one hero region, 020/062).
- Centred everything on a desktop tool (allowed: marketing heroes).
- The same face as your last product when the brands differ.

## 6. Worked choices from the set (to calibrate)

- Business banking web app, "precise, trustworthy", ink-and-bone → Neutral grotesk: Hanken Grotesk
  400/500/600; hero 44px 600 −0.03em; eyebrows 11px uppercase; no second face. (046, 011, 057)
- Consumer money app, "light, encouraging", mobile, pastel block → Friendly geometric: Outfit
  400/500/600; hero 36px 600; saturated pastels with black type; one serif-italic word allowed on
  onboarding only. (013, 071, 082)
- Crypto/analytics, "sharp", dark → Tight modern grotesk: Geist 400/500/600; KPI 32px; 11px
  uppercase micro-labels; lime or violet accent. (060, 092, 029)
- Wealth dashboard, "quiet luxury" → Editorial: Fraunces 500 for the hero numeral at 40px and card
  titles at 22px; Inter 400/500 for data; hairlines, no cards. (081, 071, 093)
- SaaS landing page, "confident, modern" → Marketing: Bricolage Grotesque 700 headline 64px;
  Inter body; one accent; product screenshot as the hero visual. (096, 098, 087)
- Restaurant ops app, "bold, fun" → Brand-loud: Barlow Condensed 700 uppercase titles; JetBrains
  Mono labels; saturated blocks; illustration. (007)
