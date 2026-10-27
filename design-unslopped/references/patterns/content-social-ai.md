# Patterns: content, social and AI

Each pattern gives the slots, in order, that the best references use. Numbers in brackets point to
`../design-notes.md` entries (310-324 are this area's batch; 317 and 319 are negatives). Each pattern
ends with how it goes wrong. Account settings, generic sheets, notifications, search and file
handling are in `app-chrome.md`; AI onboarding is in `applications-and-onboarding.md`.

## Contents
1. Feed: card anatomy, media, ranking, end of feed
2. Engagement: actions, counts, comments, share
3. Profiles: personal, creator, business
4. Messaging: thread list
5. Messaging: conversation
6. Team and support inbox
7. AI insight, recommendation and assistant surfaces
8. AI chat: empty state and composer
9. AI chat: the response
10. AI chat: model picker and honest labelling
11. AI agents: runs, approvals, logs, limits, failure
12. Media players
13. Maps
14. News, community and long-form reading

---

## 1. Feed: card anatomy, media, ranking, end of feed [310, 311, 312, 313]
- Feed switch at the top: text tabs ("Following / For You", 311; "Feed / Following / Reels", 313) or
 filter pills (312). Name the ranking where it can change ("Sort by: the newest ▾", 310); an
 algorithmic tab always has a chronological neighbour.
- Stories or live row: rings with own story first and a divider (312), or tall ~3:4 cards with a
 state chip and viewer count ("Live 20.5K", "Premiere", 311).
- Card, top to bottom: header (32-40px avatar, name + verified, one meta line of role / location /
 time, Follow state, ⋯) → content (text first when the post is text, real line breaks, 310; media
 edge to edge of the card) → social proof ("Liked by ryangildan and 22 others" with two avatars,
 312; reaction glyphs + "Garry and 1,200 others" left, "86 comments • 14 reposts" right, 310) →
 action row (§2).
- Media keeps its type's ratio: 1:1 or 4:5 photo, 9:16 video, 16:9 link preview. Carousel position
 on the image (dots, 312; segmented progress, 313). Text on media only over a scrim (311, 313).
- Recency on every item: relative under a day ("2h ago"), a date after, the exact time on hover or
 long-press; news-like items add one popularity fact ("12 min ago · 11,071 readers", 310).
- New items arrive as a "↑ 12 new posts" pill, never by shifting what is being read (WCAG 2.2 SC
 2.2.2). The end is said ("You're all caught up · posts from the last 3 days"), then older items
 under a labelled divider or "Load more", so the footer stays reachable; a resurfacing row names
 its count ("24 videos in your drift · Take a look", 311).
- Desktop: three columns, the feed at reading width (about 660px in 310), identity left, news right.
 Markup: `role="feed"` of `article`s with `aria-posinset` / `aria-setsize`, `aria-busy` loading.
- Goes wrong: every post "2h ago" with matching counts (310, 312); a hashtag run as the caption
 (313); the ad as the loudest element (310's "See who's hiring"). Instead: a real spread of ages and
 counts, real text with one or two tags, sponsored items in the post card marked "Sponsored".
Sources: https://www.w3.org/WAI/ARIA/apg/patterns/feed/ · https://www.w3.org/TR/WCAG22/

## 2. Engagement: actions, counts, comments, share [310, 311, 312, 313, 314]
- Verbs: three or four (Like, Comment, Repost or Share, Send) as icon + count, Save alone at the far
 right (312), or four equal labelled verbs on desktop (310); a zero count shows the icon only. Under
 the media (310, 312), on it as glass pills (311), or a vertical rail on the thumb side for
 full-screen video, avatar with + on top, credit bottom-left (313).
- Counts: exact under 1,000, then one decimal and one suffix style everywhere (20.5K, 534.4K, 2.5M,
 311). Acting changes the icon (filled, coloured) and the count together; roll back on failure.
- Comments and share open as sheets over the dimmed feed (312). Comments: grabber, title with
 count, rows of avatar, bold name, text, time, "Reply", heart + count right; replies one level deep
 behind "View 4 replies"; quick reactions above "Add comment". Share: search, a 4-column grid of
 recent people, then external targets with Copy link first. On messages, reactions hang off the
 bubble corner as count chips (314).
- Targets 44x44pt (Apple) / 48x48dp (Material); the count belongs to its button.
- Goes wrong: one pill style for every verb so liked and unliked look alike (312); "1.2k" here and
 "120K" there (313 vs 311); comments as a new screen that loses the scroll position. Instead: a
 state change on the icon, one formatter, a sheet with a close button as well as drag-to-dismiss
 (WCAG 2.2 SC 2.5.7).
Sources: https://developer.apple.com/design/human-interface-guidelines/accessibility ·
https://m3.material.io/foundations/accessible-design/overview

## 3. Profiles: personal, creator, business [008, 310, 311, 313, 314, 316, 324]
- Personal: cover photo with the avatar overlapping its edge (313), or a centred avatar with two
 stats flanking it (311); name, handle, one-line bio; 3-4 stats split by hairlines (313); the action
 pair, which says whose profile it is (Follow filled + Message outlined for others, "Edit profile"
 for self, never neither: 311); content tabs with counts ("Post 25 | Reels 34", 311); a 3-column
 grid with play counts on video tiles (311) or 2-column masonry (313).
- Creator: owner-only insight (profile viewers 145 ▲12%, post impressions 204 ▲38%, 310) labelled
 "Only you can see this", pinned work above the grid. Business or place: category, rating with its
 count ("4.0 (8k reviews)", 324), location, hours, stat chips and one pinned verb (008 "Book
 Appointment").
- Inside other products: a messaging contact (314) gets stat tiles, a shared-media strip with "+42"
 and chat settings; a customer in a tool (316) gets key-values (Assignee, Plan, LTV, Joined,
 Priority), last payment and a labelled AI summary.
- Goes wrong: "90 post" beside "Followers" (313); full email and phone in a side panel (316).
 Instead: plural nouns, one case, one formatter; contact details masked with a reveal, always in
 finance.

## 4. Messaging: thread list [089, 314, 315, 316, 317]
- Header: large title ("Chats", 314; iOS Large Title is 34pt), search, compose; filter chips All /
 Unread / Groups / Work (314, 315).
- Row (a Material two-line list item is 72dp): avatar with presence dot; name, semibold when unread,
 time right; one-line preview with a sender prefix in groups ("Khai: Are they still open…"), "You:"
 plus read ticks on own messages, glyph + noun for media ("📷 Photo"); trailing unread count (99+),
 pin, mute. Pinned first, then by last activity. Typing replaces the preview with "typing…" in the
 accent (317 writes "Type....").
- Three designed states: browse (filters, badges), select (the bottom bar becomes "✕ 1" + archive /
 mute / delete, 315), compose (FAB or header action); plus empty and search results. Desktop: list,
 thread and an optional context panel side by side (316); history grouped by day (089).
- Goes wrong: every badge "8", every time "8:05 PM" (317, 315); unread by colour alone; delete as
 the only bulk verb. Instead: most rows without a badge, times spread over days; bold name + badge
 (WCAG 2.2 SC 1.4.1); archive first, delete confirmed or undoable.
Sources: https://developer.apple.com/design/human-interface-guidelines/typography ·
https://m3.material.io/components/lists/specs

## 5. Messaging: conversation [314, 315, 316, 317]
- Header: back, avatar, name, one sub-line ("Online", "last seen 14:02", the member list truncated
 for groups, or "typing…"), call / video / ⋮. Bubbles: own right in the accent or black (314),
 others left in a neutral, never full width; the corner nearest the sender squares off in a run.
- Runs: consecutive messages from one sender. Name on the first bubble (groups only, one colour per
 person, 314), avatar on the last, a tight gap inside a run and a clearly larger one between runs.
- Time: a centred day separator ("Today", "Tuesday, Jan 12", 315) and one time per run (above, 314;
 below, 315); the exact time on tap or hover. Never a time under every bubble (317).
- Delivery on the newest own message only: sending (clock) → sent ✓ → delivered ✓✓ → read ✓✓ in the
 accent (314) or "Read 14:02"; failed: red "!" and "Not delivered · Tap to retry". Typing: a
 three-dot bubble in the incoming position, "Kira is typing…" in a group header, cleared when the
 sender stops.
- Long-press: reactions + Reply, Copy, Forward, Delete; a reply quotes the original (name, one line,
 bar) and the quote scrolls to it; mentions in the accent (314).
- Attachments: photos as a stack or grid with "+2 photos" (314); files as a card with type, name,
 size and download (316 "Refund Processed #RF-23891"); voice notes as waveform + duration; links as
 a card with title and domain; upload progress on the bubble with cancel.
- Composer: + (camera, photos, file, location), field with emoji, mic when empty swapping to send;
 smart replies as chips above it (315). The thread's bottom inset equals composer plus keyboard, so
 the newest message is never underneath (314 gets this wrong). Scrolled up when messages arrive: a
 "↓ 3 new messages" pill and a "New messages" divider. The transcript is `role="log"`; typing and
 send failures are status messages (WCAG 2.2 SC 4.1.3).
- Goes wrong: times out of order and "Today,jun 14" (317); a gradient wallpaper behind every screen
 (314). Instead: monotonic, proofread times; one surface tone, atmosphere in one place
 (`../peak.md` §3).
Sources: https://www.w3.org/TR/wai-aria-1.2/#log · https://www.w3.org/TR/WCAG22/

## 6. Team and support inbox [089, 316, 321]
- Panes: nav · views with counts (Open / Awaiting 5 / Snoozed 2 / Overdue SLA / Resolved 12) and
 channels with counts · thread list · thread · context panel (316); agent actions in a log (321).
- Row: customer, channel glyph, preview, SLA in words and time ("Due in 2h" amber, "Overdue 35m"
 red), assignee, and an AI provenance chip: "AI gen." (sent by the agent), "AI drafted" (waiting
 for a human), "Escalated" (316).
- Thread: internal notes tinted and labelled "Internal · only your team sees this"; an AI draft lands
 in the composer as "AI draft · review before sending". Context panel: customer key-values, orders
 or payments, the AI summary with its label and time (316); saved replies through "/" (089).
- Goes wrong: three rows of one customer and text (316); AI replies styled like human ones. Instead:
 varied channels, ages, states; "Sent by AI agent" on the message, the chip on the row (316, 321).

## 7. AI insight, recommendation and assistant surfaces [042, 054, 060, 063, 075, 089]
- Entry: header button with ✦ ("Ask Finexa", "Get AI Insight") or a right-rail panel.
- Insight card: one sentence with a specific number; optional dots pagination; optional ↗.
- Recommendation card (best anatomy, 075): severity chip + timestamp → title → problem sentence →
 tinted "Recommendation & Impact" block with bullets and quantified impact → one action button.
 Confidence shown as a % chip or a banner.
- Assistant panel: short AI summary paragraph, 2-3 mini stat tiles with status chips, an input
 with placeholder and send; model picker chips if relevant.
- Chat home: logo, two-line headline (two weights), 3 suggestion chips with icons, wide input with
 "/ for commands", tools row, disclaimer line (089, 018).
- Label every AI output ("AI Summary", "AI forecast:", "Warning:") so users know its source.

## 8. AI chat: empty state and composer [018, 042, 089, 318, 319, 320, 321]
- Empty state: greeting + one line of what the assistant can do with this user's data; 3-4
 suggestions that are tasks on real objects ("Summarise the 3 claims awaiting review"), not
 categories. Above the input on mobile (018), under the headline on desktop (089). Five intent
 chips (318) or six modes (320) is a menu, not a suggestion.
- Composer, in order: + attach (files, photos, connectors) · multi-line field that grows, then
 scrolls · placeholder with an example ("e.g. 'Reschedule…'", 321) · tool toggles as chips under
 the field (attach, Tools, Search, 089) · model picker (§10) · mic or voice mode · send, filled,
 disabled when empty. Desktop: Enter sends, Shift+Enter breaks a line, "/" for commands, ⌘K
 search, ⌘N new chat (089). One grey disclaimer line underneath saying what it can get wrong (089).
 Attachments as chips above the text (name, type, size, progress, ✕); limits stated before upload.
- History by day with auto-titles (318's "Text generate / Font recommendation"); shared workspaces
 show members ("James Workspace · 4 members", 318). Voice mode: Listening / Thinking / Speaking as
 explicit states, the transcript on screen, cancel, stop and done as three controls (319).
- Goes wrong: an orb as the hero (318, 319, 320); an upsell strip docked on the composer (318);
 typos in suggestions and headline (319 "Profesional", "Trevel"). Instead: the space goes to
 suggestions with real objects or recent work; a quiet usage counter ("12 of 40 messages left
 today") whose menu offers the upgrade; suggestions proofread like any other copy.

## 9. AI chat: the response [017, 042, 070, 103, 318, 319, 322]
- Order: label row (model glyph + "Answer", 318) · step summary, collapsed · body · inline
 citations · sources · actions · 2-3 follow-up suggestions specific to the answer (319).
- Streaming: a "Generating" placeholder where the answer will land (318); text streams in place,
 only the newest line fading in (322); Send becomes Stop; the view follows the stream only if the
 reader is at the bottom, otherwise a "↓ New" pill; announce completion, not each token (WCAG 2.2
 SC 4.1.3). A stopped answer stays, labelled "Stopped", with Continue.
- Tool calls and steps: one collapsed line above the body ("Searched 6 sources · Read 3 files ·
 14 s ▸"); expanded, a vertical list with a glyph per step type, status (✓ / spinner / ✕), the input
 in mono (query, file name), duration, and the error in words on a failed step. Evidence: event
 types LLM_CALL / TOOL_USE / GUARDRAIL (103), the timestamped stepper (017), node and log views
 (070, 322).
- Citations: a numbered chip right after the claim (318 "1"); hover or tap opens a card with title,
 domain + favicon, date and the quoted passage; the Sources list follows citation order and shows
 the domain on every item (318 shows titles only).
- Artifacts: a document, table, chart or code opens in a panel beside the thread, thread narrow and
 artifact wide, with its own header (title, v1 / v2, copy, download, share); the message keeps a
 chip that reopens it. The assistant as a peer of the work: 042, 322.
- Actions under every answer: copy, regenerate (versions kept behind a "2 / 3" pager), thumbs up /
 down (down asks why: Inaccurate / Didn't follow instructions / Harmful, plus free text), share,
 flag (318). User messages are editable; an edit forks the thread and the old branch stays. A
 failure reads "Couldn't finish · connection lost" with Retry in the message; the partial answer
 stays.
- Goes wrong: a wordless spinner for twenty seconds; regenerate that overwrites; sources under the
 composer (318). Instead: a step line saying what it is doing; a version pager (HAX G9, efficient
 correction; G15, granular feedback); a bottom inset that keeps sources visible.
Sources: https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/ · https://www.w3.org/TR/WCAG22/

## 10. AI chat: model picker and honest labelling [042, 054, 060, 075, 089, 316, 318-321]
- Picker in the composer ("✦ Lumina 2.0 (beta) ▾", 318; "Core Intelligence ▾", 320) or as chips
 for 2-3 models (042). Rows: name, one-line trade-off ("Fastest, short answers" / "Best for long
 documents, slower"), cost or quota if metered, "Beta" chip, a check on the current one. One
 picker: if speed is a property of the model, a separate "Fast ▾" (320) is noise.
- Label every AI output in words where it appears: "Answer" (318), "AI Summary" (054), "AI
 forecast:" (060), "AI gen." / "AI drafted" (316), "✦ AI agent · 2 min ago" (321). Generated,
 drafted-awaiting-a-human and human-sent are three states and look different. ✦ marks AI output
 and AI entry points only (319 puts it on chrome; `../anti-slop.md`).
- Limits next to the output: the data used ("Based on your last 90 days of transactions"), how sure
 and why ("96% confident, based on 1,500 previous sessions", 075), what it cannot do (089's
 disclaimer). HAX G1-G2 (make clear what the system can do, and how well); Apple HIG Machine
 learning (confidence, attribution, limitations).
- Disclosure can be a legal requirement: the EU AI Act (Art. 50) sets transparency duties for
 systems that interact with people and for generated content. AI statements about money,
 eligibility or advice go to Compliance and Legal review before customers see them.
- Goes wrong: "Confidence 92%" with no basis (320); praise of the assistant the user cannot check.
 Instead: basis and scope in the same line (075); counts of work done that open the work (321's
 "47 tasks" leads to the log).
Sources: https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/ ·
https://developer.apple.com/design/human-interface-guidelines/machine-learning ·
https://pair.withgoogle.com/guidebook/ · https://eur-lex.europa.eu/eli/reg/2024/1689/oj

## 11. AI agents: runs, approvals, logs, limits, failure [017, 070, 075, 103, 320, 321, 322]
- Run list: a card or row per agent or run with name and purpose ("Scheduler Agent · Calendar
 Ops"), status as dot + word (Queued / Running / Waiting for you / Done / Failed / Stopped), the
 current step in domain units ("Analyzing market trends · 124 data points processed"), start time,
 spend against cap (320). Order: waiting for you, failed, running, done. A summary in the header
 ("3 agents active · 1 pending action", 320; "Molar is handling 4 tasks right now", 321); "LIVE"
 only when it is (321). Step progress: a vertical stepper per run (017) with step, tool, status and
 time; the current step open with live output; planned steps greyed.
- Approval before anything consequential (send, pay, book, delete, publish, spend past a cap): a
 card at the top naming the agent, the action as verb + object, every value that matters (who,
 what, when, how much, from which account), the consequence ("Sends invites to 3 people"), why it
 is proposed, and when the request expires. The primary button names the action ("Send 3
 invites"), then Edit and Decline; 320's equal Confirm / Decline is the weak form. "Fix
 automatically" (075) only after a preview of the change. Payments keep the product's own
 confirmation and authentication; an agent never skips them.
- Activity log for people (321): past-tense verb first, object, reason, actor, time ("Rescheduled 1
 patient from Tue 14:00 → Wed 10:30 (staff conflict) · AI agent"); rows awaiting a human say so.
 Debug log for builders (103, 322): time to the second (ms for latency), level as word + glyph,
 step, a message that says what failed, duration, tokens or cost, run ID with copy, one stated sort
 order, `role="log"`; Editor / Executions / Evaluation with a test chat beside the log (322).
- Limits: spend against cap per run and per period ("Budget Used $120/$300", 320) and what happens
 at the cap ("Pauses and asks you at $300"). Failure: the step marked in place with the error in
 words, earlier output kept; Retry step / Edit and retry / Skip / Stop run; what a retry will not
 repeat ("2 emails already sent will not be resent").
- Goes wrong: details that contradict (320: 10:00-10:45 vs "60 Min", "Starting" on a pending item);
 progress bars on rates ("No-show rate 3.2% · Progress 3.2%", 321); logs out of order, no run ID,
 yellow text on white (322). Instead: one status per object, numbers that add up; bars only toward
 a count or cap; sorted rows with IDs and durations at 4.5:1 contrast (WCAG 2.2 SC 1.4.3).

## 12. Media players [311, 313; platform docs]
No player in the library passed review; this follows platform guidance and the video evidence in 313.
- Now playing: artwork 1:1 as the largest element; title + artist (artist links), like / add;
 scrubber with elapsed left and remaining right in tabular figures; transport previous · play/pause
 (largest, centred) · next, shuffle and repeat at the ends (repeat shows off / all / one); a row for
 output device (AirPlay, Cast), lyrics, queue; a background tinted from the artwork as the one
 atmospheric move. Mini player docked above the tab bar on every tab: thumb, "title · artist",
 play/pause, next, a progress hairline; tap or swipe up expands it.
- Queue: now playing pinned, "Next in queue" (added by the user) above "Next from: <playlist>", drag
 handles, swipe to remove, Clear. Spoken audio: skip back shorter than forward (Apple Podcasts
 defaults to 15 s back, 30 s forward), speed, sleep timer, chapters.
- Video: overlay controls that hide after inactivity and return on tap or pointer move; scrubber
 with chapter ticks; captions toggle on the bar, not in a menu; speed and quality in settings;
 picture-in-picture; fullscreen. Keyboard as users know it: Space or K play/pause, J / L ±10 s,
 ← / → ±5 s, F fullscreen, M mute, C captions (YouTube shortcuts).
- Short video (313): full-bleed 9:16, action rail on the thumb side, credit and sound bottom-left,
 progress hairline. Live: "LIVE" chip with viewer count (311), no scrubber, "Back to live".
- Publish metadata and actions to the lock screen and notification (Android MediaSession, iOS Now
 Playing) to match the in-app controls. WCAG 2.2: no sound autoplay over 3 s without pause or
 volume (SC 1.4.2); autoplay and auto-advancing stories pausable (SC 2.2.2); captions (SC 1.2.2).
- Goes wrong: a glass player over a 3D blob with a skeleton queue; a scrubber without times;
 play/pause the size of shuffle. Instead: a real queue with titles, durations and its source; times
 at both ends; one dominant control.
Sources: https://developer.apple.com/design/human-interface-guidelines/playing-audio ·
https://developer.apple.com/design/human-interface-guidelines/playing-video ·
https://developer.android.com/media/implement/surfaces/mobile ·
https://support.google.com/youtube/answer/7631406

## 13. Maps [008, 010, 011, 050, 090, 323, 324]
- Mobile: map with a bottom sheet at three heights: peek (count + filters, "120 hotels · Filters",
 323), half (cards), full (list only, the map collapses to a header). Grabber always visible (011;
 324 omits it). iOS sheets use medium and large detents; Material 3 bottom sheets a 32x4dp drag
 handle and 28dp top corners. Desktop: list and map side by side as one selection, hovering a card
 raises its pin (323's carousel is the mobile form); results refresh on "Search this area".
- Pins carry the comparison value: price (323), rating (008), count ("217 Suppliers Germany", 050).
 The selected pin inverts and rises and its card scrolls into view (323); visited pins mute; pins
 hold 3:1 against the map (WCAG 2.2 SC 1.4.11). Overlapping pins cluster into a counted circle that
 zooms to its bounds on tap (MapKit, Google Maps clustering).
- Data on the real shape beats a generic chart (010); a route in the accent, stops numbered in
 order, the list below in the same order with times. Floating controls (locate, layers, compass;
 zoom on desktop) in corners clear of the sheet and the attribution (324), at 44pt / 48dp.
- Filters: 3-4 chips on the map plus "Filters" with an active count; the sheet holds sort, a price
 range over a histogram with the average (323), ratings, amenities, Clear, and an apply button
 with the live count ("Show 84 hotels"). Desktop: tabs + dropdowns (090). Long-press menu:
 destructive item last, red, with its glyph (324).
- States: nothing in this area ("No hotels here · Zoom out"), location denied (explain, offer
 manual search), offline tiles. Every drag (pan, sheet, slider) has a single-pointer alternative:
 list view, buttons, inputs (WCAG 2.2 SC 2.5.7).
- Goes wrong: pins that overlap (323) or that are place names, not results (324); a sheet that
 hides the map and its attribution. Instead: clusters; pins are the results; a sliver of map and
 the attribution stay visible (OpenStreetMap and Google both require it).
Sources: https://developer.apple.com/design/human-interface-guidelines/sheets ·
https://m3.material.io/components/bottom-sheets/specs ·
https://developer.apple.com/documentation/mapkit/mkclusterannotation ·
https://developers.google.com/maps/documentation/javascript/marker-clustering ·
https://www.openstreetmap.org/copyright

## 14. News, community and long-form reading [042, 117, 310, 312]
- News list: headline (2-3 lines at most), one meta line of source · time · readers or comments
 ("12 min ago · 11,071 readers", 310), thumbnail right on mobile, a label where true (Live,
 Opinion, Sponsored, "Updated 14:20").
- Article: eyebrow, headline, standfirst (one paragraph), byline with published and updated dates,
 read time from word count, hero image with caption and credit; body at a measure of 45-75
 characters (Bringhurst, The Elements of Typographic Style §2.1.2; WCAG 1.4.8 (AAA) caps it at 80, 40
 for CJK), no smaller than iOS's 17pt Body, in a layout that survives 1.5 line height and 2x
 paragraph spacing (WCAG 2.2 SC 1.4.12); section heads, pull quotes, a thin progress bar; related
 items, comments and share at the end. Digests borrow the issue line and a sentence headline ("The
 week in revenue." with "VOL. IV · ISSUE 117", 117; 042's magazine header).
- Community thread: original post, sort (Top / Newest, 310), replies nested one or two levels with
 a guide line and "View 4 more replies"; each comment has avatar, name, role or flair, time, text,
 like + count, Reply (312); an author badge on the poster's own replies; report in ⋯; a removed
 comment leaves "Removed by a moderator" so the thread still reads.
- Goes wrong: full-width paragraphs at 1440; headlines without a time. Instead: the measure, with
 the side columns used for notes or contents; every item time-stamped, "Updated" when it changed.
Sources: https://www.w3.org/TR/WCAG22/
