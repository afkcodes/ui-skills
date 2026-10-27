# Platform batch: platform-native design languages (145-156)

Material 3 and M3 Expressive (145-148), Apple iOS/iPadOS 26 with Liquid Glass (149-153), macOS 26
window chrome (154), visionOS (155-156). Dribbble was thin for native work, so five keepers are
official examples from m3.material.io and the Apple HIG (147, 152-155). No Fluent 2 / Windows 11
candidate passed: the Dribbble ones were a web magazine, 3D art and an ad poster, and the Fluent 2
site illustrates materials with placeholder windows ("Text" menus). The Fluent section of
`platform-native.md` rests on the official docs only. Two negatives: 148 (M3 by default) and 156
(an opaque white slab in visionOS).

## 145 Music player, M3 Expressive (Tom) — Android, black + per-cover accent, EXPRESSIVE SHAPES
- Four now-playing screens, each themed from its cover: coral (Måneskin "Supermodel"), lime
  ("NUEVAYoL", Bad Bunny), periwinkle ("The Greatest", Billie Eilish), pink (Olivia Dean). The
  cover fills the top ~60%, a dark scrim carries the title in a wide extended display face and a
  thin artist line, then a black control deck.
- Controls form an M3 Expressive button group with shape by role: play/pause a ~195dp circle (half
  the width), skip back/forward two tall pills (~70 x 135dp), shuffle in a scalloped "cookie" shape
  from the shape library, queue in a circle. Hierarchy is carried by size and shape; all four
  share one tone.
- Progress is the Expressive wavy indicator: the played part is a sine wave, the rest flat, with a
  vertical stop mark. Lesson: Expressive ships sanctioned bespoke parts (wavy progress, the
  35-shape library, morphing button groups); spend them on the one interaction that matters and
  keep everything else baseline.
- Lesson: dynamic colour from content is the atmosphere. One seed per cover, spent only on the
  controls; the deck stays black.
- Weak: no elapsed/remaining time on the progress; the selected shuffle reads as disabled (muted
  tint on the scallop); the board repeats and mirrors screens for presentation.

## 146 Reservations concept, M3 Expressive (Dan) — Android, sage + butter yellow, DYNAMIC COLOUR
- Map-first café booking: tonal circular POI markers (McDonalds, Country Bread, Zino Ristorante) on
  a pale map; a large sage container card holding "Kara Kedi Coffee Shop", "Open · Closes at 7 pm",
  a photo with its own smaller inner radius, an address row with "A little busy now", a yellow
  directions button, and "Availability for Today" time chips (9:00 am / 9:15 am / 9:30 am / →).
- Colour from one seed: sage primary-container surfaces, butter-yellow tertiary containers for the
  bookable times and the directions action. Tertiary is used where M3 says it belongs (contrasting
  accents that need attention), so the eye goes to the times first.
- M3 navigation bar untouched: 4 destinations (Explore / Search / Reservations / Account), active
  icon in a pill indicator, labels on every item. Lesson: the brand lives in the card and the map;
  the bar is the platform's.
- Lesson: the photo's radius is smaller than the card's, i.e. optical roundness (outer − padding).
- Weak: shown in an iPhone frame with the Dynamic Island and iOS status bar, the "which platform?"
  error in miniature. A dark sibling (search sheet, filter chips) exists; this light one is stronger.

## 147 Payments list, M3 Expressive (Material Design, official) — Android, baseline lilac, CONTAINMENT
- From "Start building with Material 3 Expressive" (m3.material.io blog, May 2025): the lower half
  of a payments home. "Cards & passes" tonal chip with a "3" badge; Favorites row of circular
  containers (Deposit / Goals / Credit score) and avatars (Pia, Marty); a "Payments" sheet with
  rows "Alejandro Ortega · Internet · 1 day ago · +$75", "Carmen Villanueva · Nephew's gift · 2 days
  ago · $24.50", "Ana Russo · Lunch · 4 days ago · $19"; a 3-item nav bar (Dashboard / Offers /
  Rewards) with a pill indicator.
- The post pairs it with a baseline version of the same content (flat rows, bare icons, no
  containers). The Expressive one groups rows into tinted containers with small gaps and rounder
  outer corners, puts icons in circular containers and fills the chip with primary container.
  Lesson: Expressive hierarchy comes from containment and tone, not from shadows or more hues.
- Lesson for banking: an official transaction row with person, purpose, relative time and amount;
  the incoming amount signed and set in the tertiary tone.
- Weak: still the baseline lilac seed (right for a spec, wrong for a product; see 148); mixed
  precision ("$19" beside "$24.50").

## 148 MaterialMe products dashboard (Setproduct) — tablet/web, default M3 lilac, NEGATIVE
- A "MaterialMe" kit page: black navigation drawer with an outlined active item and a "New"
  badge; underline tabs (All products / Digital goods / Books / Files / Music); four equal KPI cards
  ($128,109.38 / 1292 / 102 / $12,134.15) each with an (i); a stacked bar chart in three lilac
  tints with a tooltip; a product table.
- Kept as a NEGATIVE example: M3 by default. Nobody chose the seed (lilac container on the one
  button, lilac bars, lilac badge); the button carries a black outline M3 does not use; the drawer
  is black instead of a surface container with a pill indicator; four identical tiles and no hero.
- Small tells: "$10.038" in the tooltip (wrong separator), "1292" with no separator beside
  "$128,109.38".
- Lesson: start from a brand seed or content-derived dynamic colour and the five surface
  containers. If the screen could be any page of the M3 docs, it is unbranded, not native.

## 149 Pine Peak Cabin detail, iOS 26 (Mari Chubina) — iPhone, stone + espresso, GLASS OVER CONTENT
- Listing detail: a full-bleed photo hero (~45% of the screen) with a "1 of 32" counter; back,
  share and heart as circular glass buttons floating on the photo; meta chips (2 guests / 24-26
  Sept / 48 m² / 1 beds); "Pine Peak Cabin, Karelia, Russia"; three stat tiles (4,99 Average rating
  / 587 Reviews / Superhost); a floating espresso CTA "Book for $140" over "$0 today · Free
  cancellation".
- Second screen: "4.97" at ~68pt between laurel glyphs (4x the 17pt body), "Guests' choice", a
  review card, "Show all 100 reviews".
- Lesson: glass is only on controls, and it has something to refract (the photo). The hero is
  content: a photo and a giant rating, both inside the content layer.
- Lesson: the photo's lower corners take a large radius that echoes the device corner; the CTA
  carries its consequence line.
- Weak: "4,99" on one screen and "4.97" on the next; "1 beds"; the CTA clips the stat tiles; an
  Airbnb pastiche.

## 150 Pine Peak results, iOS 26 (Mari Chubina) — iPhone, stone + espresso, FLOATING TAB BAR
- Search results: a glass back button and a search capsule ("Karelia, Russia", "24-26 Sept · 2
  guests") in the nav area; filter chips (filter icon, "On map" filled espresso, Popular ▾,
  Price ▾); a photo mosaic (one large, two stacked) for the first listing; "24-26 Sept · $140 for 2
  nights · ★ 4,99"; a carousel of smaller cards.
- The tab bar is the iOS 26 one: a capsule inset from the screen edges, floating over the
  carousel with the photos blurred through it, the selected tab (Search) in a lighter inner
  capsule, filled glyphs with single-word labels (Search / Favourites / Booking / Chat / Profile).
- Lesson: let content run under the bar; that is what makes the material read. No solid footer.
- Weak: same product as 149 (kept because it is the only clear floating tab bar in the batch);
  photos repeat across screens; the content face is a geometric sans, fine in content only if it
  scales with Dynamic Type.

## 151 GitHub profile with contributions, iOS 26 (Max Burnside) — iPhone, near-black + green, CONTENT HERO
- Current vs Revised. Current: avatar, name, "Set your status", a list of links, then inset-grouped
  rows (Repositories 13 › / Starred 3 › / Organizations 0 ›). Revised: links condensed to one line,
  achievements beside the name, and a contributions grid as the hero: "3,542 contributions in the
  last year", 7 x 16 rounded tiles in five greens, "+1,928 more than 9/17/24" and "449 day streak".
- Lesson: the bespoke element goes in the content area, between the header and the native list;
  the list below keeps the system anatomy (icon tile, label, count, chevron) with the larger iOS 26
  section radius.
- The number sits inside the sentence in the accent (the 060 move), three times.
- Weak: 16 weeks shown for "the last year"; US-only date; tiles are bevelled like glass (opaque,
  so acceptable, but do not make content tiles translucent).

## 152 Notes with format sheet, iOS 26 (Apple HIG, official) — iPhone, white + Notes yellow, SHEETS
- From the HIG Sheets page: a note "Monday Morning Meeting" with a selection; glass controls at the
  top (back; undo; share and ••• grouped in one capsule) and a yellow prominent ✓ that is the only
  coloured control; a nonmodal "Format" sheet inset from the screen edges with a large radius
  following the device, a close button, a style row (Title / Heading / Subheading / Body, Body
  selected in yellow) and segmented groups (B I U S; lists; indent).
- Lesson: the Liquid Glass colour rule in one screen: monochrome glass, accent on the background of
  the single primary action.
- Lesson: a part-height sheet floats inset with content visible around it; segments inside it use
  concentric inner radii.
- Weak: a system app with no brand; use it for chrome anatomy only.

## 153 Landmarks with background extension, iPadOS 26 (Apple HIG, official) — iPad, photo hero, SIDEBAR
- From the HIG Layout page: a floating glass sidebar (Landmarks / Map / Collections) with its toggle;
  a Mount Fuji photo filling the top of the content area and mirrored, blurred, beneath the sidebar
  (background extension effect); back, share, a grouped favourite + collection capsule and info as
  glass buttons on the photo; "Mount Fuji" and three paragraphs below.
- Lesson: this is the platform-native hero. Full-bleed imagery in the content layer, glass controls
  on top, the image extended under the sidebar so chrome sits on content, not on a grey panel.
- Lesson: toolbar items grouped by function in shared capsules; icons, not text.
- Weak: the text block has no hierarchy beyond the title; the busy crop behind the buttons is
  where a scroll edge effect earns its place.

## 154 Notes window, macOS 26 (Apple HIG, official) — Mac, white, WINDOW CHROME
- From the HIG Toolbars page: traffic lights; sidebar toggle and back as round glass buttons; the
  title "Notes" with "103 notes" inline in the toolbar; grouped glass capsules (compose; Aa,
  checklist, table, attachment, collaboration; lock; share; •••; search); the ••• menu open (Pin
  Note highlighted, Lock Note, Find in Note, Move to ›, Recent Notes ›, Math Results ›, Attachment
  Viewer ›, Delete Note).
- Lesson: Mac chrome is one toolbar integrated with the title bar; items have no individual
  bezel, they sit in glass groups, and ••• holds the overflow. Each item must also exist in the
  menu bar.
- Lesson: the window's large corners and the toolbar capsules are concentric.
- Weak: a system app; shows chrome, not density.

## 155 Music window, visionOS (Apple HIG, official) — visionOS, glass over passthrough, ORNAMENTS
- From the HIG Sidebars page: a Music window on default glass in a room; a vertical tab bar
  ornament floating off the window's leading edge (six glyphs, Library selected in a lighter
  circle); inside, a sidebar "Library / All Music" (Recently Added, Artists, Albums, Songs, Made For
  You) and a "Playlists" section with "All Playlists" selected as a lighter rounded rectangle; the
  content pane "Playlists / All 254 Playlists", a search field and a grid of large rounded tiles.
- Lesson: the tab bar is vertical and outside the window as an ornament; the sidebar is a second
  glass; selection is a lighter fill, never a hue.
- Lesson: rows are tall and widely spaced for eye targeting; text is bold white with vibrancy.
- Weak: placeholder tiles; the crop hides the window bar and the toolbar ornament.

## 156 Reader, visionOS explorations (Paperpillar) — visionOS, beige room + coral, NEGATIVE
- Three windows angled around the viewer: a timer and checklist, a reader with a glass sidebar
  (Home / Just For You / Reading List / Draft / Collaboration / Your Stats) and an opaque off-white
  article pane "The Cultural Significance of Greenhouses" in a thin serif, and a chat window. A
  custom bar floats above the reader: back, history, list, search, share and a close ×.
- Kept as a NEGATIVE example: the article is an opaque white slab in passthrough, which the HIG says
  blocks the surroundings and feels heavy; a thin serif at 12-14pt in space; the custom top bar
  duplicates the system close and window controls instead of a bottom toolbar ornament; lorem
  ipsum in the side windows; "Jean Doe".
- What is right: the sidebar glass and a separate floating bar show the ornament idea. Lesson:
  keep the window glass; put the brand in imagery and content, not in the window material.
