# Design reference

High-resolution UI reference images, collected 2026-10-14, 2026-10-18 and 2026-10-27 for internal
inspiration only. Each image is the work of the credited designer, studio or organisation. Do not
reuse, republish or ship them; use them to study layout, type, colour and motion. `INDEX.csv` lists
every kept file with its designer and a link back to the original page.

Every image here was reviewed one by one and has substantial, readable interface (real
screens, components, tables, dashboards, flows). Anything that was mostly photo, 3D art, a
bare hero, a splash or title cover, or a tilted / hand-held mockup went to `_rejected/`
(same subfolder layout, with its own `INDEX.csv`). One documented exception: 318, a flat rotated
collage kept because it is the only reference for AI-chat generating, citation and sources states.

| Folder | What it is | Files |
|---|---|---|
| `website-designs/dribbble-dashboards/` | Web-app dashboards: banking, fintech, payments, business banking, SaaS (incl. 1 negative) | 27 |
| `website-designs/dribbble-analytics/` | Product/web/marketing analytics tools: funnels, cohorts, event feeds, experiments, web vitals (incl. 2 negatives) | 18 |
| `website-designs/dribbble/` | Top web shots of the year (marketing sites, enterprise SaaS) | 11 |
| `website-designs/behance/` | Top website / landing-page projects | 3 |
| `website-designs/awwwards/` | Sites of the Day (almost all art-directed heroes, so only 1 passed) | 1 |
| `app-designs/dribbble/` | Mobile app shots (top of the year, plus 2 mobile banking screens) | 17 |
| `app-designs/behance/` | Top mobile app UI projects | 8 |
| `languages/dribbble-platform-native/` | Material 3 / Expressive, iOS 26 Liquid Glass, visionOS (incl. 2 negatives) | 7 |
| `languages/official-platform-native/` | Example images from the Material 3 blog and Apple HIG (iOS, iPadOS, macOS, visionOS) | 5 |
| `languages/official-systems/` | Headless-Chrome captures of GOV.UK service pages and Design System examples, Carbon, Polaris, Atlassian in use, USWDS (incl. 1 negative) | 13 |
| `languages/dribbble-movements/` | Neo-brutalism, bento, tactile, retro / Y2K, terminal, collage, editorial (incl. 2 negatives) | 15 |
| `patterns/dribbble-applications/` | Sign-up, onboarding, KYC, loan and account applications, document upload (incl. 2 negatives) | 13 |
| `patterns/dribbble-app-chrome/` | Search, command palette, filters, settings, notifications, empty states, profile, files (incl. 2 negatives) | 18 |
| `patterns/dribbble-commerce/` | Pricing, listing, product pages, cart, checkout, subscription checkout (incl. 2 negatives) | 16 |
| `patterns/dribbble-content-ai/` | Feeds, profiles, messaging, AI chat and agents, maps (incl. 2 negatives) | 15 |

Resolution: original upload size where the source offers it (Dribbble 1600-3200px wide,
Behance 1600px or wider, Awwwards 1600x1200); captures at 1440px wide (390px for mobile views).

`_reviews/2026-10-27/` holds the review record for the third batch: the Dribbble candidate list and,
per area, every candidate's keep / reject decision with a reason, plus the notes as first written.

Most relevant for banking / fintech work:
- Banking and business-banking dashboards: `website-designs/dribbble-dashboards/*Bank*`,
  `*Fintech*`, `*Payment*`, `*Business-Banking*`, `*Finance*`
- Table-heavy screens (payments lists, transactions, scheduled payments): `*Payment-Dashboard*`,
  `*Finexa*`, `*payment-dashboard-web-ui-design*`
- Mobile banking: `app-designs/dribbble/*Fintech-Mobile-Banking*`, `*Digital-Wallet*`,
  `*Insurance*`, `*Payx-Mobile-Business-Banking*`, `*SME-Business-Banking*`,
  `app-designs/behance/*Fintech*`, `*Northpoint*`
- Applications, KYC and loans: `patterns/dribbble-applications/`; transactional services:
  `languages/official-systems/official-govuk-*`

## Using these with the design skill

`../design-unslopped/` is a Claude skill built from a one-by-one review of every image here. Its
`references/design-notes.md` has one entry per image, numbered; `assets/previews/map.txt` maps each
number to its file here, and `scripts/find_refs.py <keywords>` finds the entries and image paths that
match a brief.
