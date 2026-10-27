# Platform-native: Material 3, Apple (iOS, iPadOS, macOS, visionOS), Fluent 2

Read this when the brief is a native app, or a web app that must feel at home on one platform
(`README.md` §1). The platform owns the chrome; the product owns the content. Microsoft states the
split as a number: reuse native components and patterns 80% of the time and spend the energy on
signature experiences (Fluent 2 design principles). Numbers point to `../design-notes.md`; 145-156
are the platform batch (147 and 152-155 are official examples). Versions: M3 with the Expressive
update (May 2025), Apple's 26 releases with Liquid Glass, Windows 11 with Fluent 2.

## 1. The split, and how the peak rules change

Two layers on every platform. The **chrome layer** (navigation, top bars, toolbars, tab bars, sheets,
menus, pickers, switches, text fields, system materials, back behaviour) stays native: system
components, system type in chrome, system targets. The **content layer** is where the brand speaks.
Expression zones, in order of weight:
1. **The hero inside the content area**: under the title or bar, never in it. A photo (149, 153), a
   giant figure (149's "4.97"), a bespoke graphic (151's contribution grid).
2. **Colour inside the platform's colour model**: an M3 scheme from a brand seed or content (145,
   146); one iOS accent on the prominent action (152); the Windows accent, sparingly.
3. **Imagery and illustration** in content, and the app icon.
4. **The sanctioned bespoke parts** the system offers: M3 Expressive shapes and wavy progress (145),
   visionOS volumes and immersive spaces.

| Rule elsewhere in the skill | Platform-native mode |
|---|---|
| Hero takes 35-45% above the fold | Same share, measured inside the content area below the system bar. The bar never hosts the hero |
| Largest text ≥ 4x body | Hold it in content: 149 sets "4.97" at ~68pt over a 17pt body. M3 Display Large is 57sp; go larger only in content |
| One atmospheric place | The platform material is the chrome's atmosphere (Liquid Glass, Mica, M3 tonal surfaces). Add one lit place in content, ideally beneath the glass so it has something to refract (149, 150, 153) |
| Bespoke element by hand | Draw it in the content layer with system type and the system radius logic (151); never re-skin a system control |
| One stance, held | The stance lives in content colour, imagery and the hero; chrome stays the platform's. A movement worn over native chrome is not allowed (`README.md` §2) |
| Compare rubric | Score the eight qualities on the content; add a ninth check: would a platform user find anything foreign in the chrome? |

The sloppy versions: brand chrome that fights the system (a custom tab bar, a bespoke back button, a
coloured nav bar on iOS 26); or 100% defaults with no brand at all (148). Native and branded are not
in tension; the chrome is native, the content is branded.

## 2. Material 3 and M3 Expressive (Android, Material web)

**Colour by role, from a seed you chose.** Roles: primary, secondary, tertiary, each with a
container and "on" pair; error (static even under dynamic colour); surface, on-surface, on-surface
variant; five surface containers (lowest, low, default, high, highest) for nesting; inverse roles.
Containers are fills for buttons and chips, never for text. Pairs guarantee 3:1 minimum; apply them
only as pairs. Dynamic colour derives a scheme from the wallpaper or in-app content: 145 takes one
seed per album cover, 146 a sage scheme with butter-yellow tertiary containers on the bookable
times. Map body to surface and navigation to surface container at every breakpoint.
Sloppy: the baseline scheme (primary #6750A4, lilac containers) left unchanged (148; even 147 is a
spec, not a product); a container colour used for text; roles picked by look. Instead: a brand seed
or content-derived scheme, roles by meaning, tertiary only for the one contrasting accent.

**Type scale** (sp, size/line height): Display 57/64, 45/52, 36/44 · Headline 32/40, 28/36, 24/32 ·
Title 22/28, 16/24, 14/20 · Body 16/24, 14/20, 12/16 · Label 14/20, 12/16, 11/16. Fifteen baseline
and fifteen emphasized styles (heavier, for selection, primary actions, headlines, unread). A
**brand** face may take Display and Headline and a **plain** face Body and Label; Roboto is the
default for both, Roboto Flex or the brand face can replace it.
Sloppy: Roboto Regular everywhere when the brand owns a face; emphasized on every label so nothing
is emphasized. Instead: brand face on Display/Headline, emphasized only where state or the primary
action lives (145's wide display title over plain body).

**Shape.** Ten steps: 0, 4, 8, 12, 16, 20, 28, 32, 48dp and full. Buttons map to full; FAB to 16,
medium FAB to 20, large FAB to 28. Nested shapes use optical roundness: inner radius = outer −
padding (48 − 14 = 34; 146's photo inside its card). Expressive adds a 35-shape library for
decorative elements (avatars, image crops, a hero control) and shape morph in button groups and
the loading indicator, driven by the expressive motion scheme. 145 gives each control a shape by
role: a circle for play, pills for skip, a scallop for shuffle.
Sloppy: one radius on everything, nested at the same value; library shapes behind text-heavy cards;
large or full radii on dense cards. Instead: radius by component, shapes for one visual moment.

**Elevation and surfaces.** Levels 0-5 are 0, 1, 3, 6, 8, 12dp. Elevation positions a component; it
has no shadow of its own by default, and surface tint is deprecated. Hierarchy comes from surface
containers (147 groups rows into tinted containers with small gaps). App bars sit at level 0 and
rise to level 2 when content scrolls under them.
Sloppy: web drop shadows on every card. Instead: tone for hierarchy, shadow only on the FAB,
menus and dialogs.

**Motion: springs.** Two schemes: expressive (overshoots; most products, hero moments) and standard
(minimal bounce; utilitarian products). Spatial springs move position, size, rotation and corners;
effects springs animate colour and opacity with no overshoot. Three speeds: fast (small components),
default (partial-screen, e.g. bottom sheet), slow (full screen). Expressive fast spatial damping is
0.6, standard 0.9. Web equivalents: expressive spatial 350/500/650ms with `cubic-bezier(0.42, 1.67,
0.21, 0.90)` for fast; effects 150/200/300ms.
Sloppy: 300ms ease-in-out on everything; bounce on a fade. Instead: spatial springs for movement,
effects springs for colour, one scheme per product.

**Navigation by breakpoint** (previously window size classes): compact < 600dp, medium 600-839,
expanded 840-1199, large 1200-1599, extra-large 1600+. Panes: 1; 1 (2 if low density); 2; 2; up to
3. Compact and medium: the **flexible navigation bar** (64dp, replaces the 80dp baseline bar; vertical
items in compact, horizontal in medium; pill indicator 56 x 32dp; 3-5 destinations) or
a modal expanded rail. Expanded and up: the **navigation rail**, collapsed 96dp (narrow 80) or
expanded 220-360dp; in Expressive the expanded rail replaces the navigation drawer.
Sloppy: a hamburger drawer for four destinations on a phone; a bottom bar on a 1200dp window; a
black drawer with an outlined item (148); an iOS-style floating tab bar on Android. Instead: bar →
rail → expanded rail as the window grows, same destinations and order.

**FAB and app bars.** FAB 56dp, medium 80 (the most recommended), large 96; the 40dp small FAB is no
longer recommended. Primary container by default. One per screen and not on every screen, for the
most important positive action (create, share, start), never a minor, overflow or destructive one.
Aligned left, centre or right, above the navigation bar or nested in it; lower right is usually best
in compact and medium windows. App bars: small 64dp (title leading by default, centred optional),
medium flexible 112dp (136dp with subtitle), large flexible 120dp (152dp with subtitle), search app
bar 56dp; they may carry an image or logo.
Sloppy: a raised centre "+" in a hand-drawn tab bar (017, 022) instead of the M3 bar with a nested
FAB; two FABs; a FAB for delete; a centred title by habit. Instead: one FAB with the nav bar, or a
primary button in content.

**Targets**: 48 x 48dp (about 9mm) with 8dp between targets.

Sources: https://m3.material.io/styles/color/roles · https://m3.material.io/styles/typography/type-scale-tokens ·
https://m3.material.io/styles/shape/corner-radius-scale · https://m3.material.io/styles/shape/shape-morph ·
https://m3.material.io/styles/elevation/tokens · https://m3.material.io/styles/motion/overview/how-it-works ·
https://m3.material.io/styles/motion/overview/specs · https://m3.material.io/foundations/layout/breakpoints/overview ·
https://m3.material.io/components/navigation-bar/specs · https://m3.material.io/components/navigation-rail/specs ·
https://m3.material.io/components/floating-action-button/specs · https://m3.material.io/components/floating-action-button/guidelines ·
https://m3.material.io/components/app-bars/specs · https://m3.material.io/foundations/designing/structure ·
https://m3.material.io/blog/building-with-m3-expressive

## 3. Apple iOS and iPadOS 26: Liquid Glass

**Glass is the control layer only.** Liquid Glass is a functional layer for controls and navigation
(tab bars, toolbars, sidebars, sheets) floating above content; content scrolls and peeks through.
Do not use it in the content layer (the exception: a slider or toggle knob while it is being
dragged). The content layer uses the standard materials (ultra-thin, thin, regular, thick). Two
variants: regular (blurs and adjusts luminosity; most system parts, anything with text) and clear
(only over rich media; add a 35% dark dimming layer when the media is bright). Instead of a solid
bar background, rely on the scroll edge effect; extend full-screen imagery under bars, and under
sidebars with the background extension effect (153). 149 floats back, share and heart over the photo.
Sloppy: glass on content cards (the anti-slop "glass on every card"); custom fills behind tab bars
and toolbars; glass on glass. Instead: system bars, solid or standard-material content, one photo
or gradient beneath the glass.

**Tab bar.** Floats above content at the bottom on glass (150); can minimise on scroll, moving an
accessory such as a mini player inline; a search tab may sit at the trailing end. It navigates, it
never acts; tabs are never hidden or disabled; labels are single words with filled SF Symbols. On
iPad it sits near the top and can convert to a sidebar.
Sloppy: a bespoke pill tab bar (003, 008, 021 were good custom bars before 26; on iOS 26 they
duplicate the system and lose its behaviour); a raised centre action in the bar (014, 017, 022).
Instead: the system tab bar; put the dominant verb in a toolbar or as a prominent button in content.

**Colour on glass.** Glass has no colour of its own. Tint sparingly: the accent goes on the
**background** of the primary action (prominent style), one or two per view (152's yellow ✓ is the
only colour in its chrome). Over colourful content keep bars monochrome. In mostly monochrome apps
the brand colour as app accent is the right lever.
Sloppy: brand-coloured tab icons over brand-coloured photos; several tinted buttons. Instead:
monochrome chrome, one tinted action, brand colour in content.

**Concentric shapes.** Hardware curvature sets the curvature of controls, sheets, popovers and
windows; nested shapes are concentric with their container (`ConcentricRectangle`), and standard
toolbar items are concentric with bar corners. Sheets have a larger radius; part-height sheets are
inset from the display edge. List sections have a larger radius and row height, and section headers
use title case. 149's photo corners and 152's sheet follow the device.
Sloppy: one 12px radius everywhere; capsules jammed into square corners; uppercase section headers.

**Type: SF Pro and Dynamic Type.** Defaults at the Large setting (pt, size/leading): Large Title
34/41, Title 1 28/34, Title 2 22/28, Title 3 20/25, Headline 17/22 semibold, Body 17/22, Callout
16/21, Subhead 15/20, Footnote 13/18, Caption 1 12/16, Caption 2 11/13. Default 17pt, minimum 11pt;
support at least 200% enlargement. A large title collapses to a standard title on scroll. A brand
face may set content (149, 150) if it scales with Dynamic Type; chrome stays SF.
Sloppy: fixed px sizes; a brand face in the tab bar; text truncated at accessibility sizes.

**Targets**: 44 x 44pt default, 28 x 28pt minimum; about 12pt around bezelled controls, 24pt around
bezel-less ones.

**Sheets and detents.** Two system detents: large (full height) and medium (about half). Add medium
for progressive disclosure; include a grabber when resizable. A half sheet floats inset on glass and
turns more opaque at full height (152). Action sheets now originate from their source control.
Sloppy: a full-screen sheet for a three-field task; a custom drawer that ignores detents.

**Navigation patterns.** Tab bar for top-level sections; push navigation with back at top leading
and an edge swipe; sheets for self-contained tasks; toolbars for actions, grouped by function in
shared glass, icons not text, never mixed within a group (153). On iPad, the tab bar adapts to a
sidebar.

Sources: https://developer.apple.com/design/human-interface-guidelines/materials · https://developer.apple.com/design/human-interface-guidelines/tab-bars ·
https://developer.apple.com/design/human-interface-guidelines/color · https://developer.apple.com/design/human-interface-guidelines/toolbars ·
https://developer.apple.com/design/human-interface-guidelines/typography · https://developer.apple.com/design/human-interface-guidelines/accessibility ·
https://developer.apple.com/design/human-interface-guidelines/sheets · https://developer.apple.com/design/human-interface-guidelines/layout ·
https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass

## 4. macOS 26 window chrome

A window is a frame and a body. The toolbar lives in the frame, integrated with the title bar; the
title sits inline with the controls (154: "Notes" over its note count). Toolbar items have no bezel
of their own and sit in glass groups; overflow goes to •••; every toolbar item also exists as a menu
bar command. The sidebar floats in the glass layer with content extended beneath. Key windows show
coloured traffic lights; inactive windows go grey and drop materials. No critical information in a
bottom bar. Type: SF Pro, no Dynamic Type; body 13pt (minimum 10); text styles Large Title 26/32,
Title 1 22/26, Title 2 17/22, Title 3 15/20, Headline 13/16 bold, Body 13/16, Callout 12/15,
Subheadline 11/14, Footnote 10/13. Controls 28 x 28pt default, 20 x 20pt minimum.
Sloppy: a web app in a fake traffic-light frame; iPhone-sized 17pt controls on a Mac; a hamburger
menu instead of a menu bar; actions only in the toolbar. Instead: denser 13pt layouts, a source-list
sidebar, a unified toolbar, menus for everything.

Sources: https://developer.apple.com/design/human-interface-guidelines/windows · https://developer.apple.com/design/human-interface-guidelines/toolbars ·
https://developer.apple.com/design/human-interface-guidelines/sidebars

## 5. visionOS: windows, ornaments, glass and depth

**Windows.** A default window is an upright plane on the system glass, with a close button, window
bar and resize controls supplied by the system. Keep the glass: removing it hurts legibility, and an
opaque background blocks the surroundings and feels heavy (156 is the slab to avoid). Default size
1280 x 720pt, opened about 2m away; size it to its content, set minimum and maximum sizes. Keep 3D
depth inside a window shallow; bounded 3D goes in a **volume**.
**Ornaments** float in a parallel plane slightly in front of the window and move with it. The system
makes toolbars (bottom edge) and tab bars (always vertical, leading side, expanding on gaze) into
ornaments (155). Keep an ornament no wider than its window, use borderless buttons on its glass,
keep it visible, keep the count low; supplemental content goes in a second window, not an ornament.
**Glass and depth.** No Dark Mode: glass adapts to what is behind it. Materials: thin for interactive
elements, regular to separate sections (a sidebar), thick for a dark element on regular. Vibrancy
levels label, secondary and tertiary carry hierarchy, not hue (155 selects with a lighter fill). Use
depth for hierarchy (a sheet comes forward, the window recedes), never on text, and sparingly:
every depth change makes eyes refocus.
**Targets and type.** 60 x 60pt default; centres at least 60pt apart or 16pt around each item;
rounder shapes are easier to hold with the eyes. Icon-only buttons are circles, text buttons rounded
rectangles or capsules, icon + text capsules. SF Pro, bolder body and titles, Extra Large Title 1
and 2 for editorial layouts; body 17pt, minimum 12pt.
**Expression zones**: content inside the window, a volume for the hero object, an immersive space
for the moment that earns it.
Sloppy: an opaque white window; a thin serif at 12-14pt; a custom top bar with its own close (156);
a vertical toolbar beside the vertical tab bar; content anchored to the head. Instead: glass windows,
system ornaments, brand in imagery and 3D content.

Sources: https://developer.apple.com/design/human-interface-guidelines/windows · https://developer.apple.com/design/human-interface-guidelines/ornaments ·
https://developer.apple.com/design/human-interface-guidelines/materials · https://developer.apple.com/design/human-interface-guidelines/spatial-layout ·
https://developer.apple.com/design/human-interface-guidelines/eyes · https://developer.apple.com/design/human-interface-guidelines/buttons

## 6. Fluent 2 on Windows 11

No reference in the library shows native Windows 11 well; these rules rest on the official docs.

**Materials.** Mica is opaque, tinted once from the desktop wallpaper, and paints the base layer
of long-lived windows; it turns neutral when the window is inactive, so it signals focus. Extend it
into the title bar. Mica Alt tints more strongly, for tabbed title bars. On top sits one content
layer (`LayerFillColorDefaultBrush`), as a contiguous standard pattern or a card pattern. Acrylic
(frosted) is only for transient, light-dismiss surfaces: flyouts, context menus, menus, and panes
that overlay content (NavigationView in Compact or Minimal). Smoke dims the UI under a modal dialog.
Sloppy: Acrylic everywhere, stacked or edge to edge (it seams); acrylic behind a docked pane; accent-
coloured text or links on acrylic. Instead: Mica base, solid content layer, Acrylic for what
light-dismisses, an opaque docked pane.

**Type: Segoe UI Variable**, optical size automatic. Ramp (px, size/line height): Caption 12/16,
Body 14/20, Body Strong 14/20 semibold, Body Large 18/24, Subtitle 20/28, Title 28/36, Large Title
40/52, Display 68/92. Minimum 14px semibold or 12px regular; one font across the app.

**Grid and corners.** Sizes, margins and positions in multiples of 4 epx; the Fluent spacing ramp
is 2, 4, 6, 8, 10, 12, 16, 20, 24, 28, 32, 36, 40, 48, 52, 56. Corner radius 8px for top-level
containers (windows, flyouts, dialogs), 4px for in-page controls (Button, TextBox, ListView) and
bars (ProgressBar, Slider), 0 where straight edges meet and when a window is snapped or maximised.
Touch targets 40 x 40 epx (7.5mm).
Sloppy: iOS radii (16-28px) on Windows controls; 13px body; spacing off the 4 grid.

**NavigationView and CommandBar.** Top navigation for five or fewer equal categories, left for five
to ten. In Auto mode the pane goes LeftMinimal (≤ 640 epx) → LeftCompact, icons only (641-1007) →
Left, expanded (≥ 1008); back button at the top of the pane, Settings as an optional entry. The
CommandBar right-aligns primary commands as icon buttons whose labels show when opened, with a
"see more" […] overflow that also takes primary commands when space runs out; on large screens put
it near the top. Sloppy: a web hamburger header in a Windows app; a toolbar of text buttons. Instead:
NavigationView, CommandBar, the accent on the one primary button and the selection indicator.

**Expression zones**: the content layer (cards, the page header hero, illustration), the accent
colour on the primary action and selection; chrome stays Mica and system controls.

Sources: https://fluent2.microsoft.design/design-principles · https://fluent2.microsoft.design/material ·
https://fluent2.microsoft.design/typography · https://fluent2.microsoft.design/layout ·
https://fluent2.microsoft.design/shapes · https://learn.microsoft.com/en-us/windows/apps/design/style/mica ·
https://learn.microsoft.com/en-us/windows/apps/design/style/acrylic ·
https://learn.microsoft.com/en-us/windows/apps/design/style/rounded-corner ·
https://learn.microsoft.com/en-us/windows/apps/design/style/typography ·
https://learn.microsoft.com/en-us/windows/apps/design/layout/screen-sizes-and-breakpoints-for-responsive-design ·
https://learn.microsoft.com/en-us/windows/apps/design/controls/navigationview ·
https://learn.microsoft.com/en-us/windows/apps/design/controls/command-bar ·
https://learn.microsoft.com/en-us/windows/apps/design/input/guidelines-for-targeting

## 7. Placing the hero and the bespoke element without breaking the platform

- The hero is the first thing **under** the system bar: a photo running edge to edge beneath the
  glass (149, 153), a figure at display size, a bespoke graphic (151). It may scroll under the bar;
  the bar never changes colour to match it.
- The bespoke element is drawn in content with platform type and radius logic: 151's grid uses
  the iOS section radius and sits above an untouched inset-grouped list; 145's shapes come from
  the M3 library.
- One lit place, in content. The chrome's material already supplies depth; a second gradient in
  the bar is two atmospheres.
- Real content and states still apply: 147's rows carry purpose and time, 149's CTA its consequence.
- Test: cover the content area. If the chrome left over looks like the platform's own apps, it is
  native. Uncover it: if the content could be any app, it is unbranded.

## 8. One product on iOS and Android

**Share** (design once): the data model and content hierarchy; the hero and the bespoke element;
copy, photography, illustration; the brand seed (the M3 scheme on Android, the app accent on iOS);
the destinations and their order; motion intent; the status vocabulary and number formats.

**Differ** (design twice):

| | Android (M3) | iOS 26 |
|---|---|---|
| Top-level navigation | Flexible nav bar, 64dp, pill indicator, 3-5 items; rail when wider | Floating glass tab bar, may minimise on scroll; sidebar on iPad |
| Back | System back gesture with predictive back preview | Back at top leading, edge swipe |
| Primary action | One FAB (medium recommended), lower right or nested in the nav bar | Prominent tinted button in a toolbar or in content |
| Top bar | App bar 64dp, title leading; medium/large flexible with subtitle | Large title collapsing to inline; glass toolbar buttons |
| Sheets | M3 bottom sheet, tonal surface | Detents (medium, large), inset glass, grabber |
| Type and units | Brand face on Display/Headline, M3 scale in sp | SF Pro in chrome, Dynamic Type styles in pt |
| Icons | Material Symbols | SF Symbols, filled in tab bars |
| Surfaces | Tonal surface containers, elevation as tone | Standard materials in content, glass for controls |
| Targets | 48 x 48dp | 44 x 44pt |
| Edges | Edge-to-edge enforced when targeting SDK 35 on Android 15; transparent system bars | Safe areas; content runs under bars |

Pickers, switches, date and time selection, menus, share sheets and haptics are always the
platform's own.
Sloppy: an iOS tab bar and SF-style chevrons shipped on Android; a FAB on iOS; one set of mockups
in an iPhone frame labelled "Android" (146's frame is the warning); identical screenshots for both
stores. Instead: render the same content in both chromes side by side and check the table row by row.

Sources: https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture ·
https://developer.android.com/develop/ui/views/layout/edge-to-edge · and the M3 and Apple links above.
