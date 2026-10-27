# Platform guidance: web, mobile, both

What changes when the brief is a website, a mobile app, or a product that spans both. Based on how
the references handle each (mobile 001-025, web app 027-083, marketing web 086-100, tools 101-144),
with 095 showing a paired web + mobile design.

This file covers layout per platform. What makes a screen feel *native* (Material 3, Apple HIG and
Liquid Glass, Fluent 2, visionOS) is in `languages/platform-native.md`; read it whenever the brief
is a native app.

## Mobile app (iOS / Android)

Layout
- Single column, 16px side gutters (20px on larger phones), 8px grid.
- Safe areas respected: status bar, notch, home indicator. Floating tab bars sit above the indicator.
- Vertical rhythm: greeting block → hero → actions → one alert row → lists. Lists scroll; the hero
  may pin or collapse.
- Cards are full-width or in a 2-column grid of equal squares; never 3 columns of text.

Type scale (typical in the references): 11-12 captions, 13-14 secondary, 15-16 body, 18-20 titles,
28-40 display for the hero number. Minimum tap target 44x44.

Navigation
- Bottom tab bar, 4-5 items; active item labelled, others icon-only is acceptable (003, 008).
- Centre raised action when the product has one dominant verb (014, 017, 022).
- Back and context actions top-left/top-right in 40px round buttons.
- Bottom sheets with a grabber for secondary flows (011 accounts sheet); background dimmed and
  blurred, not replaced.

Content
- Hero number is the screen's one idea; privacy toggle beside it on finance apps.
- Quick actions as 4 tiles; status rows with count badges and chevrons.
- Transactions with day headers; 56-64px rows; swipe actions implied by chevrons.
- Charts simplified: one series, 7-12 bars, selected bar labelled; no legends beyond two items.
- Forms one field per row; helper text under the field; primary button pinned near the bottom.

Dark mode
- Dark banking UIs (004, 006, 012, 020) use a dark header region for state and a lighter or white
  region for lists, or stay dark with cards one step lighter. One hue glow max.

## Web app (desktop, tablet)

Layout
- Shell: sidebar (240-260px) or icon rail (56-72px) + header (56-64px) + content with 24-32px
  padding. Max content width around 1440-1600; let the grid breathe beyond that.
- 12-column grid; cards span 3/4/6/8/12. Common dashboard rhythm: KPI strip (full width) →
  main chart (8) + side widget (4) → table (8) + two small cards (4).
- Right rail (300-360px) for secondary widgets, AI panel, quick transfer, cards overview.
- Tablet (768-1024): sidebar collapses to a rail; 2-column grids; tables drop secondary columns.

Type scale: 12 captions/table headers, 13-14 table body and secondary, 14-15 body, 16-18 card
titles, 24-32 KPI numbers, 32-48 hero numbers or page display.

Navigation
- Sidebar groups with small-caps labels; active item filled; counts muted. Workspace switcher
  under the logo. Pill top nav for consumer-facing dashboards (045, 076).
- Breadcrumb above the page title when depth > 1.
- Period and scope controls live in the header, right-aligned; per-card period pickers only when
  cards genuinely differ.

Content
- Tables get the full anatomy (toolbar, sortable headers, footer pagination). Row height 44-48.
- Charts get legends, gridlines, dual axes when needed, hover tooltips with multiple values.
- Forms may be two columns for short fields; labels above fields; helper text under; one primary
  button right-aligned in a footer bar.
- Inline edit-in-place for fields that are frequently edited (017's tax and accounting fields).
- Data freshness and "last updated" in the chrome.

## Marketing website

- Nav: logo, 4-6 items, outlined + filled CTA; sticky.
- Hero: headline (2-3 lines), subhead (1 paragraph), two buttons, real product visual or a
  functional element. Social proof above or below.
- Sections alternate rhythm (dark/light, text-left/visual-right then flipped), each with a small-caps
  eyebrow, a heading, one paragraph, and a visual that is a real screenshot or a diagram.
- Feature cards contain mini-UI, not icons alone (098).
- Closing section: coloured band with one CTA. Footer with sitemap, legal, and a disclaimer where the
  product is regulated (033 shows the disclaimer habit).
- Long-scroll landing pages still need a consistent accent and photography that carries trust (097).

## Desktop app (Windows / macOS) and spatial (visionOS)

- Desktop apps follow the platform's window chrome, menus, keyboard shortcuts and materials (Mica
  and Acrylic on Windows, the macOS toolbar and sidebar); the content area is laid out like a web app
  (12-column grid, 24-32px padding) inside it. Density sits between web app and tool mode.
- Spatial apps are windows of glass in a room: content first, controls in ornaments, no full-bleed
  backgrounds, generous targets for eye-and-pinch input.
- Details and numbers for both: `languages/platform-native.md`.

## Designing for both

When the brief covers web and mobile:
1. Design the data model and the component vocabulary first (status chips, KPI anatomy, row slots,
   palette). These are shared.
2. Design the desktop dashboard and the mobile home side by side (095) so the same card appears
   in both at different densities: e.g. a transaction row keeps leading glyph, name, amount, status on
   mobile and adds method, masked card, date on desktop.
3. Decide what is mobile-only (scan, biometrics, push-driven alerts) and desktop-only (bulk actions,
   export, multi-column tables, canvas editors like 070).
4. Navigation maps: sidebar groups ↔ tab bar items + "More"; header actions ↔ quick-action tiles.
5. Charts: desktop multi-series with legend; mobile single-series with a selected-bar callout. Same
   colours, same selection behaviour.
6. Keep one type family and one radius scale; adjust sizes per platform, not styles.

## Accessibility baseline (all platforms)

- Text contrast 4.5:1 for body, 3:1 for large text and UI glyphs. Check tinted chips and grey
  secondary text on tinted cards; they are the usual borderline cases.
- Never colour alone for status, direction, or series; add text, glyph, hatch or position.
- Tap/click targets 44px mobile, 32px desktop minimum; 8px between adjacent targets.
- Focus states visible on web; reduced-motion respected for animated charts and gradients.
- Numbers formatted for the locale (thousands separators, currency position, date order); the
  Russian-language landing page (097) shows the same anatomy surviving localisation.
