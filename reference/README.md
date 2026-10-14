# Design reference

High-resolution UI reference images, collected 2026-10-14 for internal inspiration only.
Each image is the work of the credited designer or studio. Do not reuse, republish or ship
them; use them to study layout, type, colour and motion. `INDEX.csv` lists every kept file
with its designer and a link back to the original page.

Every image here was reviewed one by one and has substantial, readable interface (real
screens, components, tables, dashboards, flows). Anything that was mostly photo, 3D art, a
bare hero, a splash or title cover, or a tilted / hand-held mockup went to `_rejected/`
(same subfolder layout, with its own `INDEX.csv`).

| Folder | What it is | Files |
|---|---|---|
| `website-designs/dribbble-dashboards/` | Web-app dashboards: banking, fintech, payments, business banking, SaaS, analytics | 60 |
| `website-designs/dribbble/` | Top web shots of the year (marketing sites, enterprise SaaS) | 11 |
| `website-designs/behance/` | Top website / landing-page projects | 3 |
| `website-designs/awwwards/` | Sites of the Day (almost all art-directed heroes, so only 1 passed) | 1 |
| `app-designs/dribbble/` | Mobile app shots (top of the year, plus 2 mobile banking screens) | 17 |
| `app-designs/behance/` | Top mobile app UI projects | 8 |

Resolution: original upload size where the source offers it (Dribbble 1600-3200px wide,
Behance 1600px or wider, Awwwards 1600x1200).

Most relevant for banking / fintech work:
- Banking and business-banking dashboards: `website-designs/dribbble-dashboards/*Bank*`,
  `*Fintech*`, `*Payment*`, `*Business-Banking*`, `*Finance*`
- Table-heavy screens (payments lists, transactions, scheduled payments): `*Payment-Dashboard*`,
  `*Finexa*`, `*payment-dashboard-web-ui-design*`
- Mobile banking: `app-designs/dribbble/*Fintech-Mobile-Banking*`, `*Digital-Wallet*`,
  `*Insurance*`, `*Payx-Mobile-Business-Banking*`, `*SME-Business-Banking*`,
  `app-designs/behance/*Fintech*`, `*Northpoint*`

## Using these with the design skill

`../design-unslopped/` is a Claude skill built from a one-by-one review of every image here. Its
`references/design-notes.md` has one entry per image (same order as this index), and
`scripts/find_refs.py <keywords>` finds the entries and image paths that match a brief.
