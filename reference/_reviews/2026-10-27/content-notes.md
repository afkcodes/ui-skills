# Content, social and AI patterns (310-324)

Collected 2026-10-27 for the content area: feeds, profiles, messaging, AI chat, AI agents, media
players, maps and reading. Searches: social media app, feed app ui, profile page app, messaging app,
ai chat app, ai agent dashboard, music player app, map app ui. 31 candidates, 15 kept (13 references
+ 2 negatives, 317 and 319). No music or video player passed (tilted, hand-held, glass art or
skeleton content), so media players are evidenced from platform docs only. These entries are the
evidence for `patterns/content-social-ai.md`.

## 310 Feed redesign (Diana Larussa) — desktop, white + network blue, FEED (desktop)
- Three columns of about 300 / 660 / 380px: an identity card left (cover, avatar, "UI Designer for
  AI & SaaS Products", Profile viewers 145 ▲12%, Post impressions 204 ▲38%, then Saved items / Groups
  / Newsletters), the feed centre at reading width, "Top stories" and a network card right.
- Composer first ("Start a post…" with Video / Photo / Write an article), then a hairline with
  "Sort by: the newest ▾" right-aligned. Ranking is named and changeable, not implied.
- Post card: 40px avatar, name • "2h ago", role line, "+ Follow" or "Following" right; real
  multi-paragraph text with line breaks and three hashtags; a reaction stack of three glyphs + "Garry
  and 1,200 others" left, "86 comments • 14 reposts" right; hairline; four equal verbs Like /
  Comment / Repost / Send.
- Top stories: headline + one grey meta line "12 min ago · 11,071 readers". Lesson: recency and
  popularity belong in one quiet line under a headline, and the feed column stays narrow while the
  side columns carry identity and news.
- Weak: every post "2h ago" and both reaction lines start "Garry and…"; Follow vs Following differ
  only by a small + icon; the loudest element on the page is the filled "See who's hiring" ad.

## 311 Social app (Piqo Studio) — mobile, white + black + one yellow, FEED + CREATOR PROFILE
- Header "Following / For You" as text tabs with a yellow underline, yellow round search. Stories as
  tall ~3:4 photo cards instead of circles, each with a state chip (black "Live", yellow "Premiere")
  and a viewer count ("20.5K"), author avatar and name on a scrim at the bottom.
- Trending card: full-bleed photo, author name + handle on the image, three glass engagement pills
  on the image (♡ 120K, ↺ 96K, ➤ 36K). Counts sit on the media; nothing trails below the card.
- Creator profile: ~120pt avatar centred with "2.5M Followers" and "120 Following" flanking it;
  name, handle; segmented "Post 25 | Reels 34" with the counts in nested chips; a resurfacing row
  "24 videos in your drift · Take a look" with an avatar stack; 3-column 9:16 grid with ▷ play
  counts (20.5K, 45.9K, 534.4K).
- Lesson: one saturated accent carries only the active tab, the create button and the selected
  segment; counts are abbreviated one way everywhere (one decimal, K/M).
- Weak: posts carry no time at all; the profile has a back button and bell but no Follow or Message,
  so it is unclear whose profile it is; the third story is cut mid-name.

## 312 ConnectWorld (Kretya) — mobile, white + blue, FEED CARD + COMMENTS + SHARE SHEET
- Story rings (own story first, a 1px divider, then others), filter pills My Feed (filled) / LIVE /
  Friend / Explore. Post card: avatar, username + verified tick, location "San Francisco", ⋯ in a
  circle; photo with carousel dots on the image; "Liked by ryangildan and 22 others" with a two-avatar
  stack; outlined count pills ♡ 6,525 · comment 23 · share 23; bookmark alone at the right.
- Comments sheet: grabber, centred title, rows of avatar, bold username, comment, "Reply" link, heart
  + count at the right (the liked one filled red, "2"); six emoji quick reactions above "Add comment"
  with the viewer's avatar.
- Share sheet: grabber, search, 4-column grid of recent contacts with truncated handles, then a
  horizontal row of round targets (Add Story, Copy link, Facebook, Instagram, Threads).
- Lesson: engagement detail opens in sheets over a dimmed feed (comments, share), so the reader
  never loses their place.
- Weak: comment and share counts identical (23 / 23) reads as template data; the external row is
  cut at the edge with no scroll cue; default blue with no stance.

## 313 Social feed (Nodus Labs) — mobile, dark warm brown + orange, REELS + FEED + PROFILE
- Full-screen reel: tabs Feed / Following / Reels at the top (active bold + dot); a right rail of
  author avatar with a red +, ♡ 1.2k, comment 1k, share 1.1k, save 1k; bottom-left name + verified,
  hashtags, "♪ Dopamin so…" sound credit; a spinning disc thumbnail bottom right. The short-video
  anatomy: verbs on the thumb side, credit bottom-left, nothing over the face.
- Feed cards: rounded media with a glass author pill on the image ("@Krismosley (2h ago)"), ⋯ in a
  glass circle, the same vertical rail inside the card, caption bottom, segmented carousel progress.
- Profile: cover photo, avatar overlapping its edge, name + grey "Edit" chip, one-line bio, four
  stats split by hairlines (205k Followers / 110 Following / 90 post / 11.3k Likes), icon-only content
  tabs (photos, videos, private, liked, saved), 2-column masonry.
- Lesson: in video-first feeds the actions are a vertical rail with counts under each icon, and the
  same rail travels from full-screen to card.
- Weak: "90 post" (lowercase, singular) beside "Followers"; hashtag spam (#foryou #foryoupage) as
  caption; the orange gradient + competes with the photos; device frames.

## 314 Group chat (Cansaas) — mobile, dark warm gradient brown→rose, MESSAGING
- Group thread header: group avatar, "Visit Denpasar", members "Akbar, Fawzy, Khai, Kira, Musa,
  Smi…" truncated; video, call, ⋮. Runs from one sender: name in a tan accent on the first bubble
  only, avatar beside the last bubble only, one time label ("8:16PM") above each run.
- Outgoing bubbles black, right, no avatar; incoming dark translucent. A media message as a fanned
  stack of three photos with a "+2 photos" chip and reaction chips (🔥 3, ❤️ 2) hanging off the corner;
  "@Rohmad" mention in the accent.
- Chat list: large title "Chats"; square story thumbnails with count badges; filters All / Favorites
  / Work / Groups / Communities; previews with sender prefix ("Khai: Are they still open at sunday?"),
  "You:" + image glyph for media, blue double ticks for read, a pin, a red unread badge, an orange
  presence dot, relative times ("24 mins").
- Contact screen: three stat tiles (Message 12,145 / Group 94 / Spaces 48), "Media and photos" strip
  with "+42", rows Notification / Media visibility / Bookmarked / Lock Chat toggle.
- Lesson: group by sender and by time, not per message: name once, avatar once, time once per run.
- Weak: the composer floats over and blurs the newest message; "5mins" vs "2 mins", "8:16PM" with no
  space; the settings group repeats; the gradient sits behind every screen rather than one region.

## 315 Messages (Huge Binary) — Android / Material 3, sage + lime, MESSAGING (list states)
- Thread list: search field with the user's avatar inside it, filter chips All (lime) / Contacts /
  Finance / Unknown; two-line rows with avatar, name + red count badge (15, 2, 12, 99+), truncated
  preview, time right ("Now", "8:05 PM"); extended FAB "Start Chat".
- Selection mode: the long-pressed row tints, and the bottom bar becomes a contextual bar "✕ 1" with
  block / archive / delete. Count + bulk verbs replace navigation while selecting.
- Conversation: header is an avatar stack of other open chats with badges plus video / call / ⋮;
  date separators "Tuesday, Jan 12" and "Today"; outgoing lime bubbles; incoming grey with the avatar
  on the run; "10 min" under the run; smart-reply chips (Yay! / Congratulations! 👍 / Ok) above the
  composer; composer pill with SIM-slot glyph, emoji and +.
- Lesson: a thread list has three designed states (browse with filters and badges, select with a
  contextual bar, compose from the FAB); smart replies sit above the composer, never in the thread.
- Weak: previews repeat ("Some great new colours", "A new material?") and every time is "8:05 PM";
  the FAB covers the last row; delete has no undo shown.

## 316 Agento support inbox (Mohammad Saju) — desktop, white + slate, MESSAGING (desktop) + AI LABELS
- Four panes: nav (Inbox, Teams, Integrations, Knowledge, AI Center, Automations), inbox views (Open
  / Awaiting 5 / Snoozed 2 / Overdue SLA / Resolved 12) and channels with counts (Email 6, WhatsApp,
  Slack 16, Shopify 4, Stripe 2), the thread, and a right panel with Profile details / Tickets tabs.
- Conversation rows carry provenance chips: "AI gen." (the agent replied), "AI drafted" (waiting for
  a human), "Escalated" (red). AI involvement is a visible state before the thread is opened.
- Thread: both sides named with "22m ago"; a date separator "09 Sept, 2025"; customer in grey
  bubbles left, agent as plain text right with an initial avatar; an attachment card "Refund
  Processed #RF-23891" with a receipt thumbnail and a download button; composer "Type your reply…".
- Right panel: Assignee, email, Plan Premium ($29/mo), LTV $1,450, Joined Mar 2021, Priority High
  (red), Segment, Language; "Last payment $29 · Sep 8, 2025"; "AI Insights" block with a labelled
  "Summary: Double charge detected… Customer is frustrated but polite." and Status Resolved.
- Lesson: in team inboxes AI involvement is labelled per row in words, and the AI summary lives in
  the context panel, labelled, not inside the conversation.
- Weak: the three direct-message rows are the same customer and text; "John Ab" truncated in the
  header; a "Get 40% discount" promo in the nav; the customer's email shown in full.

## 317 Messages (Azmir Sheikh) — mobile, grey + black, MESSAGING · NEGATIVE
- Serif "Messages" title, search + filter, chips All / Contacts / Unknown / New, four rows each with
  an "8" badge; conversation with "Today,jun 14" and a time under every bubble.
- Kept as a NEGATIVE example: per-message timestamps with no run grouping, and out of order (12:43 PM,
  11:50 AM, 12:43 PM); typing shown as "Type...." in the list and "Type.." in the header instead of
  "typing…"; every unread badge is 8; previews repeat ("A place to slow down."); copy errors ("Hi! Im
  interested", "Can you meeting with tomorrow?").
- Lesson: the anatomy is right (presence in the header, attach / camera / mic in the composer) and
  the screen still reads as fake because the data is uniform and the states are mislabelled.

## 318 AI chat response flow (Keitoto) — mobile, white + periwinkle, AI CHAT
- Empty state: "Hi James, how can I help you today?" under an orb; intent chips Ask Anything / Create
  image / Code / Analyze / Brainstorm with coloured glyphs. Thread header is a breadcrumb "Text
  generate / Font recommendation" (mode / auto-title).
- Generating: a "··· Generating" pill where the answer will land, and the composer itself reads
  "Generating…" while the model works.
- Answer: labelled "Answer" with the model glyph; structured markdown (bold lead terms, a numbered
  option, bullets); an inline citation chip "1" at the end of the claim; a "Sources" block of cards
  below; copy and flag left, Rewrite and Share right.
- Composer: + attach, "Ask me anything…", mic and a black voice-mode button; model picker "✦ Lumina
  2.0 (beta) ▾" inside the composer; a dismissible "Upgrade to pro for unlimited usage" strip docked
  on top of it. A shared variant "James Workspace · 4 members".
- Lesson: an answer carries its own provenance (label, citation number, sources) and its own verbs
  (copy, flag, rewrite, share) directly beneath it.
- Weak: a rotated collage (study anatomy, not presentation); source cards show titles only, no
  domain, favicon or date, and the composer overlaps them; the orb repeats on every screen; the
  answer recommends Playfair Display, itself a generated-UI tell (`typography.md`).

## 319 Talkora AI tutor (Fireart Studio) — mobile, white + iridescent blue, AI CHAT · NEGATIVE
- Home with "Your Profesional AI Language Tutor", skill chips and four practice cards with % rings;
  a chat home dominated by an iridescent orb above "Let's Learn a New Language"; a speaking-practice
  thread with a play button on the AI reply, a "Suggestions" block of three follow-up questions, and
  a "Listening…" voice state with a waveform and ✕ cancel / ■ stop / ✓ done.
- Kept as a NEGATIVE example: the orb is the hero on two of three screens and says nothing about
  what the model can do; typos in the hero and in the suggestions ("Profesional", "Trevel the
  English", "treveling", "favorite trevel destinations", "player guitar"); three of four rings read
  92%; sparkles on the header button and the "In Progress" chip.
- Worth keeping: follow-up suggestions after an answer, a play control on spoken replies, an explicit
  three-control voice state.
- Lesson: AI slop is decoration where the evidence should be, and generated copy nobody proofread.

## 320 Agent control centre (Topnotch Studio) — desktop, white + one blue glow, AI AGENTS · APPROVAL
- Left column of agent cards: icon, "Scheduler Agent / Calendar Ops", status dot + word right
  (Pending Confirmation amber, Analyzing violet, Executing green). The pending one expands into an
  approval: "Confirm Meeting Schedule?", a two-line explanation ("Your Scheduler Agent has proposed…
  review the details and confirm to proceed"), the proposed object (Tue, Apr 16 · 10:00–10:45 AM ·
  +2 People · 3 Todo List · 60 Min) and Confirm / Decline.
- Running agents report progress in domain units: "Analyzing market trends · 124 data points
  processed", Confidence 92% with a sparkline; "Budget Used $120/$300" with the cap smaller and grey.
- Right: "Good Afternoon, Adom" + "3 agents active · 1 pending action" (state in the greeting line),
  date and time with zone; "AI is ready / Waiting for your instructions or voice command"; mode chips
  Fast / In Depth / Magic AI / Holistic / Canvas / Quizzes; composer with "Core Intelligence ▾",
  "Fast ▾" and mic.
- Lesson: agents are a list of runs with a status word each; an action with consequences becomes a
  card at the top that names the agent, the proposal with its values, and two verbs.
- Weak: "14:02 PM"; the proposal says 10:00–10:45 but "60 Min" and is dated a month before today
  (Tuesday, May 14); a "Starting" chip contradicts "Pending Confirmation"; two agents share one
  copy-pasted progress line; Confirm and Decline are near-equal; "John Doe"; the orb takes 40% of the
  screen to say "ready".

## 321 Molar AI (Korsa) — desktop, white + deep violet band, AI AGENTS · ACTIVITY LOG
- Header "Good morning, Dr. Bennett" + "Molar has handled 47 tasks this morning" (number in the
  accent) and an "All systems normal" pill right.
- Hero band, the one lit region: "AI AGENT · LIVE" chip with a waveform, "Molar is handling 4 tasks
  right now", task chips ("Calling 2 patients", "Drafting 2 claim"), three glass tiles (Tasks Today
  47 · 12 done · 12 to go; Time Saved 8.4h; Confirmed 98% · Awaiting Dr. Bennett).
- "AI Agent activity · Live · last 24 hours": one icon per verb, the verb bold first ("Confirmed
  Sophia M. via SMS for tomorrow 14:30.", "Drafted claim for Michael C. … ready for review.",
  "Rescheduled 1 patient from Tue 14:00 → Wed 10:30 (staff conflict).", "Follow-up sent to Olivia
  P. — day 7. Reply: …"), then "✦ AI agent · 2 min ago". Schedule rows say "AI reminder sent" or
  "Confirmed". The Ask panel uses an example placeholder ("e.g. 'Resched…'").
- Lesson: an agent log is past-tense verb + object + reason + actor + time, and work waiting on a
  human says so in the row ("ready for review", "Awaiting Dr. Bennett").
- Weak: progress bars on rates ("No-show rate 3.2% · Progress 3.2%"); "1 hours ago", "Drafting 2
  claim"; "Time Saved" captioned "AI reminders active"; "09.42" vs "9.43" in the Ask panel, which is
  cropped; patient names would need masking in production.

## 322 Avero agent builder (Repo Studio) — desktop, white + blue, AI AGENTS · LOGS
- Breadcrumb "Personal / My workflows / Customer support auto-responder ✎", "Export PDF ▾", filled
  Save. Tabs Editor / Executions / Evaluation: build, run history and evals as three views of one
  agent.
- Canvas: Chat trigger → AI Agent → four tools (OpenAI chat model, Session memory, Knowledge lookup,
  Code execution), each icon + title + type; floating toolbar ending in Hide Chat and a filled Execute.
- Bottom split: a test chat "Avero 2.1" whose last line fades out as it streams, beside a Logs table
  (Log level · Created at · Message) with Info blue, Error red, Warning yellow.
- Lesson: test the agent beside its log, and make every model or tool step a timestamped row.
  Compare 070 for the canvas and 103 for the event-log anatomy.
- Weak: nav cropped at the left; a component name leaked as a node subtitle ("AgentNodeCard");
  "Search anythings…"; log rows out of order (Apr 29, Apr 29, Apr 26) with no run ID, duration or cost;
  yellow "Warning" text fails contrast; the Error row describes a step, not what failed.

## 323 Hotel search map (Cuberto) — mobile, white + sky blue, MAPS
- Price pins ($92, $1,387, $2,999) as small filled capsules; the selected pin inverted to dark violet
  ($246); "120 hotels · Filters" at the foot of the map over a horizontal card carousel (photo, name,
  stars, "$246", "Booking.com $299" struck) that follows the selected pin.
- Filters: Clear top right, search, "Sort by $ > $$$", a two-handle price slider drawn over a
  histogram of prices with "$250–$300" and "Average price $298", star rows as checkboxes.
- Detail: "#7 BEST SPA" badge, date and guest chips (aug 2-4, 3 guests), "Expedia price $299 / night"
  struck against "Members price $150 / night" and "You're saving $149" in green; amenity icons in
  circles; address with a map snippet.
- Lesson: the pin carries the one number people compare, and the selected pin, the card under the
  thumb and the detail page are visibly the same object.
- Weak: an older collage, cropped at the edges and only 1600px; pins overlap with no clustering
  ($79 / $490 / $231); tab labels about 9px.

## 324 Trip planner (Farhan) — mobile, white + pastel map, MAPS · BOTTOM SHEET
- Map in the top half with place labels as white pills on a stem dot (Tabanan, Denpasar, Singaraja),
  floating round controls (layers, locate, photos, people, menu); a card sheet below: carousel of
  trip photos with the owner's avatar, "Trip to Bali ✓", "30 Aug . 06 Sep 2026 . 8 days", chips
  Planning / Expenses; an "8 days to plan" card.
- Long-press opens a menu over the dimmed map: Edit ›, Archive ›, Delete in red with a red bin.
- Stay detail: 1+3 photo mosaic with "08+", name + verified, "4.0 (8k reviews)", "Hotel · Ubud,
  Gianyar, Bali, Indonesia", Check-In 28 Aug — "6 Night" — 03 Sep Check-Out, "Directions · Navigate
  there ↗", black "Create Stay".
- Lesson: the map stays visible above a sheet that holds the list; destructive actions are split off
  by colour and position.
- Weak: the pins are place names, not the trip's own stops; "." as a date separator, "6 Night",
  "08+"; no grabber on the sheet, so it is unclear that it moves.
