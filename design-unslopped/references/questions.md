# Intake questions

Ask these before designing. The aim is to remove the decisions that make output generic: who it is
for, what the one idea is, what the constraints are. Ask in at most two rounds; batch related
questions; skip anything already answered in the brief or discoverable from the codebase, Figma
file, or existing screens. If the user says "just go", pick sensible defaults, state them in one
line each, and proceed.

## Round 1: always (new design or update)

1. **Platform.** Website (marketing), web app (logged-in), mobile app (iOS / Android / both), or
   web + mobile? If web app or mobile: which breakpoints or devices matter most?
2. **The one idea.** What should the user see or do first on this screen? (The hero: a balance, a
   list to act on, a chart to read, a form to complete.) If they can't say, ask what the user comes
   here to do most often.
3. **Who.** Who uses it and in what state: a consumer checking money on a train, an ops analyst at
   a desk all day, a prospect evaluating a product? This sets density and decoration budget.
4. **Domain and tone.** Banking / payments / insurance / SaaS tool / consumer / brand-led? And two or
   three adjectives (e.g. "calm, precise, trustworthy" vs "bold, energetic").
5. **Scope.** One screen, a flow (how many steps), or a system (dashboard + detail + forms)?

## Round 1 additions for an update / redesign

6. **What exists.** Link, screenshot, Figma, or path to the current screen. What is wrong with it in
   the user's words, and what must not change (brand, information architecture, specific
   components)?
7. **Design system.** Is there one (tokens, component library, e.g. Alchemy)? If yes, work inside it
   and do not invent components that exist. If no, should this become the start of one?

## Round 2: only if not already clear

8. **Brand constraints.** Colours, type, logo, existing accent; light / dark / both.
9. **Data reality.** What are the real values, ranges, and edge cases? (Negative balances, failed
   payments, 0 items, 10,000 rows, long names, multiple currencies, locales.) Designs are judged
   on edge cases.
10. **Must-have components.** Tables with sort/filter? Charts (which questions must they answer)?
    Forms (which fields are required, what helper text)? AI features (what exactly does the AI do)?
11. **Accessibility and compliance.** WCAG level; regulatory copy (disclaimers, FCA-style warnings);
    PII handling on screen (masking, privacy toggles).
12. **Deliverable.** Figma, HTML prototype, React components in a repo, before/after page,
    annotated mockup? How will it be reviewed and by whom?
13. **References.** Anything they like or hate (and why). Offer 2-3 items from
    `../../reference/` that match the brief so they can react to something concrete.

## How to ask

- Lead with the two or three questions whose answers change the design most (usually platform, the
  one idea, and what exists). Put the rest in a short list they can skip.
- Offer defaults inline: "Platform: I'll assume web app, desktop-first, with a mobile home screen
  unless you say otherwise."
- Never ask for things you can look up: existing components, current colours, repo structure.
- Reflect the answers back in one paragraph (the design brief) before you start, so a wrong
  assumption is caught early.
