# Pattern library: index

Patterns are concrete anatomies: the slots, in order, that the best references use for a recurring
part of a screen, with the evidence numbers beside each heading. Open the file for the region you
are building, use the anatomy as a starting point, and fill it with this product's content. A
pattern is never the hero; the hero and the bespoke element come from `../ideation.md`.

When the design language fixes a component (a native sheet, a GOV.UK question page, a Carbon data
table), the language's version wins and the pattern only supplies the content and states. When an
existing design system has its own pattern for the region, use that first (`../languages/brand-systems.md`).

| File | Open when the screen has… |
|---|---|
| `finance-and-dashboards.md` | A hero balance or headline metric, KPI tiles, quick actions, transaction rows, data tables, status chips, breakdowns, chart cards, limits and goals, a transfer or payment form, a transaction lifecycle, cards and accounts, choice screens, sidebar and header chrome, a mobile home or tab bar, kanban or calendar |
| `applications-and-onboarding.md` | Sign-up or sign-in, first-run onboarding, identity / KYC checks, a multi-step application (account opening, loan, quote), document upload, consent and e-signature, approvals, and the form craft they all share |
| `app-chrome.md` | Search and results, a command palette, filters and saved views, settings, notifications and activity, modals / drawers / sheets / popovers, empty, loading, error and offline states, files and attachments, profile, team and roles |
| `commerce-and-marketing.md` | Pricing, product listing and detail, cart, checkout, subscription checkout, order confirmation and tracking, comparison tables, marketing sections and the landing-page hero |
| `content-social-ai.md` | Feeds, profiles, messaging, AI insight cards and assistants, AI chat, AI agents with human approval, media players, maps, news and long-form reading |

For analytics and tool dashboards (trends, funnels, retention, paths, experiments) use
`../tools-and-analytics.md` §5 instead.

Rules every pattern file shares:
- State consequences before the user commits (fees, totals, what happens next, what the AI will
  do), and status with time ("since", "expected by").
- Design one non-happy state per pattern: empty, failed, pending, refused, offline.
- One filled primary action per view.
- Copy is part of the anatomy: real names, plausible numbers, proofread labels.
