# Ideation: how to think of the idea, not just execute one

Everything else in this skill makes execution match the references. This file is about the step
before: finding the idea that makes a screen *this product's* and nobody else's. The references
have one each, and in every case it came from a question, a metaphor or a constraint, not from a
component library. Run this method in full for a new design; for an update, run the parts marked ◆.

## 1. Reframe before you sketch ◆

Answer in one line each. The answers often contain the idea.
- What is the user *feeling* when this screen opens? (anxious about money; proud; rushed; curious)
- What question are they really asking? ("can I afford this?" not "what is my balance")
- What would they do with the answer in the next ten seconds?
- What is the data's natural shape? (a composition → area; a sequence → timeline; a flow → Sankey;
 a count → units; a position → map; a limit → gauge; a comparison → paired bars)
- What physical object from this domain already solves this? (pay packet, till receipt, passbook,
 cheque stub, ledger, meter, boarding pass, timetable, dial, ticket, seed tray, lap counter)
- What is the one sentence this screen should say if it could talk? (046: "Forecast your end-of-
 month balance in seconds." 025: "Nice work! You saved €26 this week.")
- What is everyone else's version of this screen, and what do they all get wrong?

## 2. Diverge: six directions, fast

Write six directions. Each is three lines: the idea in a sentence, what the hero is, what the
bespoke element is. Force variety by taking each direction through a different lens below; do not
write six variants of one idea. This takes ten minutes and is the most valuable ten minutes in the
workflow.

Lenses (pick six that fit; the reference beside each shows the lens working):
1. **Lead with the change, not the state.** The hero is the delta or the insight; the balance is
 secondary. (092 "+2.6%" at 64px with a two-line explanation beneath)
2. **Make the data a countable thing.** Units, squares, dots, portions, coins. (040 dot-matrix;
 014 calorie portions; 046 barcode bars; 030 cohort dots)
3. **Composition as area.** Treemap, mosaic, stacked blocks. (023 treemap of contracts; 069 order
 status as three wide blocks)
4. **Map it onto its real shape.** A circuit, a floor plan, a body, a country, a calendar grid.
 (010 drivers on the track; 024 body silhouette; 016 avatars on dates)
5. **The screen answers a question.** A calculator, a simulator, a slider with live result. (046
 cash-flow calculator; 063 strategy sliders; 040 keypad transfer)
6. **Time as the spine.** Timeline, stepper, lifecycle, "now" line. (017 payment lifecycle;
 054 relative times)
7. **One object, big.** The product, the card, the car, the device, rendered and centred; data
 around it. (015 car; 006 lamp dial; 025 Cubee device)
8. **Sentences instead of widgets.** Card titles that say what they do; insights as prose with the
 number inside. (046; 060 "Improve 32% in morning engagement…")
9. **Invert one surface.** One dark card on a light page or one light card on dark, and it is the
 action. (092 exchange panel; 046 calculator)
10. **Texture as encoding.** Hatching, dots, stripes for projected / pending / other instead of a
 colour. (011 hatched bars; 059 hatched potential; 046 hatched vs solid expense bars)
11. **Steal a print idea.** Ledger rules, small-caps eyebrows, a ticket stub, a receipt tear-off, a
 stamped status, a numbered index. (046 Swiss ledger; 023 boxed grid; 017 "Transactions." as a
 magazine title)
12. **Strip it to numbers on the page.** No cards; hairlines; the numbers are the layout. (093; 069)
13. **A single saturated colour on nothing.** Everything grey except the one thing that matters.
 (029 lime; 040 yellow card; 072 yellow nav)
14. **The brand is a character.** Illustration, voice, a mascot, loud type. (007 tubik)
15. **Split the screen by meaning.** State above (dark), activity below (light); summary left,
 action right. (004; 040; 024)
16. **Make the status physical.** Coloured header strips, stamps, rings, progress you can read from
 across the room. (023 "B+" grade; 068 limits as bars)
17. **Give it a voice.** Notifications and empty states that sound like a person with a number.
 (025 "You saved €26 this week"; 075 recommendation cards)
18. **Borrow from another domain.** A bank statement as a boarding pass; a budget as a seed tray;
 savings as a thermometer; approvals as a kanban. (014 scan as AR labels)
19. **Remove the obvious component.** No tab bar, no donut, no KPI row; what replaces it? (093 has
 no cards; 069 has no KPI tiles)
20. **Make the empty state the hero.** Design for zero first; the full state inherits its idea.

Random stimulus, when stuck: pick a reference number at random that is *outside* the brief's domain
(e.g. 010 Formula 1 for a payments brief), open it, and ask what its idea would look like here.

## 3. Converge: choose one ◆

Score each direction 1-3 on four things and sum:
- **Serves the one idea** (does the hero answer the user's real question?)
- **Honest** (does the form follow the data's shape; would the numbers still make sense?)
- **Not already in the set** (would a competitor, or this reference library, have done it?)
- **Executable at peak** (can it be drawn by hand at the craft level, in the time available?)

Take the top one. If two tie, take the bolder. Write the winner as one sentence the user can react
to: "The home screen is a pay packet: this month's pay as 100 squares that fill with where the
money went; the number left is the hero." Present the top two to the user when the brief allows
(step 7 of the workflow), recommend one, and say in one line why the other lost.

## 4. Push, then protect ◆

- **Push 20%.** Whatever the winning idea is, make it bigger, bolder or more literal than feels
 comfortable: the hero number one size up, the bespoke element taking the full card, the colour
 fully saturated. The references all sit slightly past comfortable (076's full-bleed gradient; 092's
 64px delta; 023's edge-to-edge treemap).
- **Protect the idea.** Everything that is not the idea gets quieter to make room: fewer colours,
 plain tables, standard chips. One idea per screen; the second-best idea goes to the next screen or
 the bin.
- **Keep it honest.** Novelty that makes the data harder to read is decoration. If the treemap
 needs a legend to be understood, it is the wrong lens. Test: can a first-time user say what the
 bespoke element means without being told?

## 5. Creative appetite (from the brief) ◆

Ask it in Round 1 of `questions.md` and design to it:
- **Evolutionary**: keep the current structure and system; one signature move; craft fixes.
- **Confident** (default): new structure, one stance, one bespoke element, pushed 20%.
- **Radical**: run all 20 lenses, present three directions, allow the hero to be something the
 category has not done; expect a second round.
State the appetite you designed to in the brief so the user can move the dial.

## 6. Signs the thinking was skipped

- The hero is a balance in a card with four quick actions under it, and nothing else was considered.
- The bespoke element is a chart type chosen from a library.
- All six directions share the same hero.
- The winning direction could be described by naming components ("KPI strip, chart, table").
- The design could be re-skinned for a different product without changing anything but the logo.
