# Intake: the full interview

Run the whole interview for every new design and every redesign. Do not pick "the two that matter
most" and skip the rest: the questions below are the decisions that make output specific to this
product, and every one you guess instead of ask is a place where a default creeps in. Skip a
question only when the conversation, the repo, a Figma file or a screenshot already answers it (say
so: "Palette: taken from your tokens, navy #0b1f4d + amber"), or when the user says "just go" (then
state every default you chose, one line each, before designing).

Use `AskUserQuestion` when it is available: four questions per call, options with a recommended
default first, "Other" always possible. Five calls cover the interview (group B takes two). Where it is not available,
ask the same groups in prose with the defaults shown inline. Reflect the answers back as the design
brief before designing.

## Group A: the product (always)

1. **Platform.** Website (marketing) · Web app (logged in) · Mobile app (iOS / Android / both) ·
   Web + mobile · Desktop app (Windows / macOS) · Spatial (visionOS). Follow-up if web app or
   mobile: which breakpoints or devices matter most?
2. **The one idea of this screen.** What should the user see or do first? (A balance to check, a list
   to act on, a chart to read, a form to complete, a decision to make.) If they can't say, ask what
   they come here to do most often.
3. **Who, and in what state.** Consumer on a phone in a hurry · professional at a desk all day ·
   prospect evaluating · internal ops / admin. Age range, expertise, and anything about mood (anxious
   about money, rushed, exploring).
4. **Scope.** One screen · a flow (how many steps) · a system (dashboard + detail + forms) · a
   component.

## Group B: look and feel (always)

5. **Design language.** Native to the platform (Material 3, iOS / Liquid Glass, Windows Fluent) · an
   existing design system (name it: a company library, Carbon, Polaris, Atlassian, GOV.UK) · an
   aesthetic direction (editorial, Swiss, neo-brutalist, bento, tactile, retro / Y2K, terminal,
   maximalist, spatial) · "you choose from the references" (recommended when nothing exists). This
   decides which file in `languages/` applies; see `languages/README.md`.
6. **Colours.** Do you have brand colours (give hex or a link)? If not: warm neutrals · cool neutrals ·
   dark · a specific hue you want as the accent · colours to avoid. Also: light, dark, or both.
7. **Mood in three words.** e.g. "calm, precise, trustworthy" / "bold, energetic, young" / "quiet
   luxury" / "playful but serious about money". Offer six example triplets as options.
8. **Type preference.** Grotesk / clean (Inter-like) · geometric / friendly · editorial serif + sans ·
   condensed / loud · mono / technical · "you choose from the references". Any fonts already in use
   or forbidden.
9. **Density.** Airy (few numbers, lots of space) · balanced · dense (tables, many figures per
   screen). Explain that this follows from who uses it, and recommend one.
10. **Creative appetite.** Evolutionary (keep the structure, improve the craft) · Confident (new
    structure, one bold idea; recommended) · Radical (the category has not seen this; expect two
    rounds).
11. **References.** Anything they like or hate (links, screenshots, product names), and why. Offer to
    show three from `../assets/previews/` that match the brief so they can react to something real.
12. **Things to avoid.** Patterns, colours, words, competitors' looks, "AI-looking" traits they have
    seen and disliked.

## Group C: content and constraints (always)

13. **Data reality.** Real value ranges and edge cases: negative balances, failed or pending states,
    zero items, thousands of rows, long names, several currencies, locales; for commerce, out of
    stock, many variants, long product names, discounts; for content and AI, posts with no media,
    very long threads, a response that fails or is refused. Ask for one real (or realistic) example
    per screen.
14. **Must-have components and actions.** Tables (sort, filter, export)? Charts (which question must
    each answer)? Forms (required fields, helper text)? AI features (what exactly does the AI do, and
    what may it do without asking)? The single primary action.
15. **Design system and codebase.** Is there one (tokens, component library, e.g. Alchemy)? Work
    inside it if so (`languages/brand-systems.md`); otherwise, should this become the start of one?
    Any existing screens to stay consistent with?
16. **Compliance and accessibility.** WCAG level; regulatory copy (disclaimers, FCA-style warnings);
    PII on screen (masking, privacy toggle); anything that needs Legal or Compliance review before it
    is shown to customers.

## Group D: delivery (always)

17. **Deliverable.** HTML prototype (artifact) · Figma · annotated mockup page · React components in a
    repo · before/after page. Light and dark both? Mobile and desktop both?
18. **Review.** Who sees it next and how (a stakeholder deck, a PR, a design crit)? Deadline or
    time box?

## For a redesign, add

19. **What exists.** Link, screenshot, Figma or path to the current screen. What is wrong with it in
    the user's words; what must not change (brand, information architecture, specific components).
20. **What has been tried.** Earlier attempts and why they were rejected.

## How to ask

- Ask everything above the first time, in five batched calls (A, B in two parts, C, D), with a
  recommended default first in each option list. It takes the user two minutes and removes most
  guessing.
- Never ask for what you can look up (existing tokens, components, repo structure, colours in a
  screenshot); say what you found instead and ask only to confirm.
- If the user answers only some, ask the rest once in a short follow-up; after that, choose defaults
  and state them.
- Reflect everything back in one design brief (8-12 lines) before step 2 of the workflow. A wrong
  assumption is cheapest to fix here.
