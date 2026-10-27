# Patterns: commerce and marketing

The pages that sell: pricing, listing, product, cart, checkout, subscription, confirmation,
comparison, and the marketing sections around them. Numbers in brackets point to
`../design-notes.md` (285-300 are the commerce batch; 299 and 300 are negatives). Each slot ends
with how it goes wrong and what to do instead. Filter mechanics: `app-chrome.md` §3. Field craft:
`applications-and-onboarding.md` §8. Status chips, transfer form, lifecycle stepper:
`finance-and-dashboards.md` §6, §10, §11.

Money on these pages is copy with consequences. Prices, savings, "was" prices, "most popular",
countdowns, reviews, instalment lines, subscription and renewal terms, competitor claims and any
financial-product page (rates, fees, eligibility, representative examples) may need Legal or
Compliance review before publication. Say so in the deliverable; never present them as final copy.

## Contents
1. Pricing page
2. Product listing and collection pages
3. Product detail page
4. Cart
5. Checkout
6. Subscription checkout
7. Order confirmation and tracking
8. Comparison tables
9. Landing page hero
10. Marketing page sections
11. Money checks before showing

---

## 1. Pricing page [285, 286, 287, 288, 297]
1. **Header.** Eyebrow chip ("Our Pricing Plan": 287), one headline, a subhead that states the terms
   ("Try our basic plan risk free for 30 days. Switch plans or cancel any time.": 288). The headline
   may carry the scale move (285: ~140px, two tones). Goes wrong: an exclamation-mark title and a
   subhead about "the perfect fit". Instead: trial, commitment and exit in one line.
2. **Billing toggle.** Two-option segmented control above the cards, the saving as a chip inside the
   option ("Bill annually · 10% OFF": 286). With annual on, show the monthly equivalent and the
   billed total ("£9/month, billed £108 yearly"). Goes wrong: "/month" prices with no yearly figure
   (286); a saving that does not compute (297: 12 × $19.99 is $239.88, so $1,149.99/year cannot
   "save $200"). Instead: saving = 12 × monthly − annual, printed in money.
3. **Plan cards: 3, at most 4** (Stripe's pricing table stops at four products). Top to bottom:
   name; who it is for ("For growing teams that need smarter workflows": 286); price at display
   size with period and basis small beside it ("/user/month, billed annually"); one CTA; features.
   The price block may sit raised in a tray that holds the features (287). Goes wrong: a price with
   no period (285 "$60k"); one description pasted into every card (287).
4. **One recommended plan**, marked four ways: middle position, taller than its neighbours (286:
   ~30px), outline or glow, the only filled button, and a label in words above it ("Recommended for
   you": 286; "Most Popular!": 285). Goes wrong: three identical buttons and a small chip (285,
   288), or the only filled button on Enterprise. A "most popular" label needs data behind it.
5. **Cumulative feature lists.** "Everything in Starter, plus" in grey small caps, then only what the
   tier adds, 5-7 rows of outcomes with numbers ("1,000 free words": 287). Goes wrong: twelve rows per
   card repeating the tier below. Instead: the step up is the list; the full grid goes in §8.
6. **The CTA says what happens next**: "Start free trial" (288), "Download for Windows" with the
   platform mark (287), "Start with Pro", "Contact Sales" (286). Goes wrong: "Get started" three
   times. A free plan's button never implies payment.
7. **Enterprise / talk to us.** Last card; the price replaced by a word ("Custom"); the list leads
   with what only this tier has (SSO, dedicated manager: 286); outlined "Contact sales" with a
   response time ("Reply within 1 working day"). Stripe's table allows one such custom-CTA product.
   Goes wrong: "Let's talk!" as the only filled button on the page.
8. **Comparison table** (§8) under the cards, then an **FAQ** of 5-8 questions buyers ask at the
   price: free trial, changing plan, cancellation, invoice details, billing (288), refunds, VAT.
   Accordion, first open, answers of one to three sentences with a link. Goes wrong: questions
   blurred under a "Show more" fade (288); "Why choose us?".
9. **Reassurance line**: cancel any time, secure payment, support hours, under the cards or in the
   closing band (§10). Goes wrong: a wall of seals. Instead: three facts.
Sources: https://docs.stripe.com/payments/checkout/pricing-table

## 2. Product listing and collection pages [289, 300, 090, 095]
1. **Header.** Breadcrumb; H1 = the collection; result count ("214 products"); one optional line.
   Goes wrong: an announcement bar and four promo tiles before the first product (300). Instead:
   products in the first viewport; one promotion slot, inside the grid if anywhere.
2. **Filters.** The 3-5 attributes that decide the category as dropdown pills above the grid, the
   rest behind "More filters" (289: brand, price, size, type; 090: tabs, four dropdowns, "Clear
   filters"); a facet column when there are 6+ facets. Applied filters as removable chips with
   "Clear all" (095) and the count; 28% of sites show no applied-filter overview (Baymard, 2026).
   Mechanics, mobile sheet, a11y: `app-chrome.md` §3. Goes wrong: facet counts that do not add up.
3. **Sort** is its own control at the row end ("Sort: Recommended ▾"), 4-6 options named by effect
   ("Price: low to high", "Newest"). Goes wrong: sort hidden inside the filter sheet.
4. **Grid.** 4 columns at 1440 without a facet column, 3 with one, 2 on mobile; one image ratio on
   one neutral tile (289). Goes wrong: mixed ratios, cut-outs beside lifestyle shots. Instead: one
   ratio, one background, the lifestyle image on hover.
5. **Card**: image; save heart top right, filled when saved; name, two lines max; variant hint
   (colour dots, "+3"); rating with count ("★ 4.9 · 652 Items Sold": 289); now price bold, was price
   struck in grey; status in words ("Just in", "Sold out": 289). The card is the link; one quick-add
   at most. Goes wrong: one name and price on every card (300); two buttons per card; a sold-out
   card that still looks buyable (289). Instead: sold out greyed, with "Notify me".
6. **Loading more.** "Load more" with "Showing 48 of 214" beats pagination and endless scroll;
   batches of 100-150 for visual categories and 50-100 for spec-driven ones on desktop, 15-30 on
   mobile (Baymard, 2020). Back returns to the same place. Goes wrong: 12 per page, numbered pages.
7. **Zero results** name the filter that emptied the list and offer to remove it ("No size 46 in
   stock · Remove 'Size: 46'"). Goes wrong: "No products found" and a blank grid.
Sources: https://baymard.com/blog/how-to-design-applied-filters ·
https://baymard.com/blog/number-of-items-loaded-by-default

## 3. Product detail page [290, 291, 292, 293, 294]
1. **Context.** Breadcrumb; a "Ship to" country selector in the header when price or delivery
   depends on it (290). Goes wrong: currency and delivery decided silently, changed at checkout.
2. **Gallery**, half to two-thirds of the content width (292, 290): an in-scale and an on-model image
   where relevant (37% of sites lack in-scale: Baymard, 2026); thumbnails, a video marked with a
   play glyph (290); on mobile a swipe carousel with dots (294). Goes wrong: five near-identical
   angles. Instead: front, back, detail, in use, in scale.
   **When there is no photography** (a mockup before the shoot, or no image access): do not fake
   it with stock-like illustration that pretends to be a photo. Use labelled placeholders that say
   which shot goes there and why ("Front, on white · 4:5", "In a room, to scale · 4:5"), sized and
   cropped exactly as the real images will be, in a neutral tone from the palette; or a precise
   line drawing where the drawing is itself information (dimensions, a doorway check, a fabric
   swatch at true colour). Put the craft into the parts that do not need photos: the buy box,
   delivery dates, the bespoke element. Say in the presentation that imagery is a placeholder and
   the page must be judged again with the real photos.
3. **Buy box order**: eyebrow (brand or category: 291, 292) → name → rating and count linked to the
   reviews ("4.8 (1.2k)": 290) → price → variants → quantity → one primary → delivery, stock and
   returns lines → details. On a single-product brand page the name may be the hero (293: ~150px
   condensed caps). Goes wrong: decisions split across columns under a giant name.
4. **Variants as buttons**, not dropdowns (57% of sites use dropdowns: Baymard, 2026). When a
   variant changes the price, put the price on the tile ("256GB $999.99 / 512GB $1,119.99": 291);
   swatches show their name on selection (294 rings the chosen one); unavailable sizes stay visible,
   struck. Goes wrong: tiny unnamed swatches; an active tab marked by a scribble that reads as
   "crossed out" (293).
5. **Price**: the largest figure in the buy box; a was price struck only when it is genuine; unit
   price for packs and sizes (81% of sites omit it: Baymard, 2026); bundles show the bundle price,
   not only "Save 10%" (290). Instalment lines ("As low as $45/mo with…": 291) are credit
   promotions: Compliance. Goes wrong: $ on the variant tiles and AED on the price; a was price
   lower than the now price (both 291). Instead: one currency, every figure from one source.
6. **One primary**, full width of the buy column, one line of microcopy under it ("Instant setup ·
   No technical skills needed": 290); save and share secondary. Goes wrong: "Add to cart" and "Buy
   now" at equal width and weight (292).
7. **Delivery promise between price and button**: a date, not a speed, with the postcode and
   "Change" ("Arrives by Fri, Feb 20": 291); fulfilment as tiles with their own state ("Shipping ·
   Free · Arrives Feb 20" / "Pickup · Not available": 291); stock ("15 in stock": 290); returns in a
   line with a link ("Free 30-day returns · Details": 291). 67% of sites do not show the total order
   cost and 44% do not link the returns policy from the main content (Baymard, 2026). Goes wrong:
   "Free shipping" with no date (290); all of it folded into an accordion (292).
8. **Details**: 4-6 key specs as tiles (291); the full spec table grouped under headings with dual
   units ("84 CM (33.1 IN)": 292); care and materials as numbered accordions (292). Goes wrong: a
   paragraph of adjectives where the dimensions should be.
9. **Reviews**: average, count, a 5-bar distribution; filters (rating, with photos, variant); each
   review with stars, date, "verified purchase" and the variant bought; replies to negative reviews
   (89% of sites never reply: Baymard, 2026). Goes wrong: three curated quotes with no rating, count
   or date (292); those are testimonials. Fake or selectively shown reviews are a Legal issue.
10. **Cross-sell** after the buy box: "Frequently bought together" with ticks and a live total, then
   similar items (291); related products with name, material and price (292). Goes wrong: a
   "Now total" that ignores the second ticked item (291). Instead: recompute on every tick.
11. **Mobile**: a sticky bottom bar, quantity stepper beside "Add to Cart" at ~60% width (294),
   targets at least 44px (`../platforms.md`). Goes wrong: the button scrolls away under the copy.
Sources: https://baymard.com/research-articles/current-state-ecommerce-product-page-ux

## 4. Cart [295, 294, 296]
1. **Header**: "Cart" and a count that matches the units; in a flow, a three-step progress (Menu ✓ →
   Cart → Checkout: 295). Goes wrong: "Your Cart (7)" over four units (296).
2. **Context row** when delivery depends on the seller: merchant, ETA, distance ("Arrives in 25–35
   min · 1.2 km": 295). Goes wrong: the ETA first shown after payment.
3. **Line item**: thumb, name, variant or modifier line ("Extra garlic sauce": 295), price, a
   stepper with − and + buttons (97% of sites lack buttons: Baymard, 2025), remove as × or trash;
   line total when quantity > 1. Goes wrong: + before −; quantity as a dropdown.
4. **Removal is undoable**: a toast "Baklava removed · Total updated · UNDO" and the total updates
   in place (295). Goes wrong: a confirm dialog for one item; the old total struck beside the new
   one, which reads as a discount (295).
5. **Free-delivery threshold** as a progress bar with the amount left ("£12 away from free
   delivery"), full and green once met (294). Goes wrong: the threshold first revealed at checkout.
6. **Add-ons** below the items, one row of three ("Popular with your order": 295). Goes wrong:
   cross-sells above the items, or a carousel of twelve.
7. **Promo code** behind a "Have a code?" link (Baymard: hide the field, apply known discounts
   automatically); an applied code becomes a chip with × and a negative line. Goes wrong: an open
   field that sends people off to hunt for codes.
8. **Summary**: Subtotal · Delivery ("From £3.95, chosen at checkout") · Discount · VAT · Total,
   the total labelled exactly ("Total incl. VAT"). 40% abandon over extra costs and 12% because they
   could not see the total up front (Baymard, 2025). Goes wrong: "Total incl. fees" that never names
   the fees (295); a list-price subtotal minus a discount the rows already applied (294).
9. **Mobile footer**, sticky: total label over the amount (~28px) and one CTA, "Go to checkout"
   (295). Goes wrong: the total only at the top of a long list.
10. **Empty state**: one sentence, one action ("Browse restaurants"), recently ordered or viewed
   (295). Goes wrong: an illustration and nothing to do.
Sources: https://baymard.com/lists/cart-abandonment-rate ·
https://baymard.com/blog/current-state-of-checkout-ux

## 5. Checkout [296, 297, 040, 068, 072]
1. **Guest first.** "Continue as guest" as the most prominent option, a button at the top; account
   creation offered on the confirmation page. 62% of sites do not make guest the most prominent; 18%
   of US shoppers abandoned rather than create an account (Baymard, 2025). Goes wrong: a sign-in wall.
2. **Structure.** One page (Shopify's default) with sections Contact → Delivery → Payment, or named
   steps whose numbers run without gaps (296 skips step 2). On mobile the order summary collapses
   behind "Show order summary" with the discount field above it (Shopify); keep the total on the
   collapsed bar. Goes wrong: five steps for a one-item order.
3. **Fields**: about 8 are enough; the average checkout in 2024 had 11.3 (Baymard). One "Full name",
   "Address line 2" behind a link, postcode lookup, billing = delivery ticked by default, required
   and optional both marked (61% of sites mark only one: Baymard, 2025), a reason under phone ("For
   the courier only"). Goes wrong: company, two phone fields and a required free-text box.
4. **Delivery options** as radio cards: name, price right, a date range ("Thu 6 – Mon 10 Mar"), not
   "3-5 days" (48% of sites use speed: Baymard, 2025); cheapest first; a cutoff countdown only when
   real ("Order within 2 h 10 min for Thursday"). Goes wrong: two cards that both look selected.
5. **Payment** as radio cards (072; `finance-and-dashboards.md` §13): the chosen method expands in
   place (296, 297); number, expiry and CVC as one grouped, bordered block with brand marks and a
   lock glyph, styled unlike the other fields (Baymard: it raises perceived security; 19% abandoned
   over trust); a (?) on CVC (296); "save my details" unticked by default (296, 297). State what the
   method costs and when it is charged, as the transfer form does (040, 068). Goes wrong: card
   fields styled like the address fields, on a separate step from the method choice.
6. **Order summary**: right column, sticky on desktop; thumbs with quantity badges; "Edit cart"; the
   totals of §4 (296). Goes wrong: a summary that disagrees with the button (299).
7. **The button carries verb and amount**: "Pay $107.02" (296; Stripe's submit text works the same
   way, "Donate US$5.00"). While processing: spinner, disabled, "Don't close this page". Goes wrong:
   "Pay now" with no amount; "Continue" on the step that charges.
8. **Trust beside the button**, not in the footer: returns in a line, support contact, Terms and
   Privacy, a terms tick box only when the terms require one (297; Stripe Checkout's policy
   settings). Goes wrong: six seals and a padlock in the header.
9. **Error recovery.** Validate a field when the user leaves it, fixed-length fields (postcode, card
   number) once complete, never mid-typing; clear the error on the keystroke that fixes it; confirm
   valid fields; still validate on submit (Baymard, 2024). Messages name the problem and the fix
   ("Postcode should look like SW1A 1AA"); 94% of sites use generic ones (Baymard, 2025). A declined
   card keeps every other field, says what happened and offers another method. Goes wrong: a reload
   that empties the form; "Something went wrong".
10. **Review step** (multi-step only): each block with a "Change" link; nothing new asked. Goes
   wrong: terms or upsells first introduced on the review page.
Sources: https://baymard.com/blog/current-state-of-checkout-ux ·
https://baymard.com/blog/checkout-flow-average-form-fields · https://baymard.com/blog/inline-form-validation ·
https://baymard.com/blog/perceived-security-of-payment-form ·
https://help.shopify.com/en/manual/checkout-settings/checkout-style ·
https://docs.stripe.com/payments/checkout/custom-components

## 6. Subscription checkout [297, 298, 299, 286, 068]
1. **Layout**: summary on a dark or tinted half, payment on white (297); or the choice left and a
   dark summary card right as the one inverted element (298; as 092, 046). Goes wrong: the summary
   below the card form, out of sight when the button is pressed.
2. **Plan row**: name, cadence in words ("Billed monthly"), price; the annual switch attached to the
   row with the saving in money (297). Goes wrong: the cadence only as a grey "/mo".
3. **Two numbers, today and then**: "Due today $58", "Then $38 every 8 weeks" (298). With a trial:
   "£0.00 due today · £19.99 on 12 March unless you cancel". Label the total "Total due today"
   (297). Goes wrong: one total that hides whether it repeats.
4. **Offer terms**: the intro price, the date it ends and the price after, as large as the intro
   price. Goes wrong: "20% Off for 12 month" in a chip, the renewal price in the small print (299).
5. **Mandate under the button**: amount incl. VAT, cadence, start date, when the offer ends, refund
   cutoff, how to cancel, links to terms (299's order is right; its numbers are not). In
   subscription mode Stripe Checkout shows a payment-method reuse agreement; custom text (up to
   1,200 characters) can link the subscription terms, customer portal and cancellation route, and
   Stripe says to consult legal before changing it. Goes wrong: "You agree to our terms" and a link.
6. **The exit beside the commitment**: "Skip, pause or change the schedule any time. No minimum."
   (298). Goes wrong: cancellation explained only in an FAQ.
7. **Button**: "Subscribe" (297) or "Start this plan" (298), with the amount when one is due today.
   Goes wrong: "Continue" on the step that starts the charge.
8. **After**: a manage page with next billing date, amount and method; pause and cancel at the same
   depth as upgrade; recurring items with frequency chips (068). Goes wrong: cancel behind a call.
299 is the negative: "$200.50 → $100.00" sold as 20% off, and $90 + $10 charged as $112 in the
total, the button and the legal text. Per-day framings ("about $0.68 a day": 298), offer and renewal
terms are Legal/Compliance copy; UK consumer law has specific rules for subscriptions: flag the flow.
Sources: https://docs.stripe.com/payments/checkout/custom-components

## 7. Order confirmation and tracking [017, 054, 068, 005]
Confirmation page, top to bottom:
1. A headline that confirms in words ("Order placed"), the order number with a copy icon, the email
   address the receipt went to. Goes wrong: "Thank you!" over a confetti illustration.
2. The delivery date promised at checkout, the address, the method. Goes wrong: a new, later date
   appearing here for the first time.
3. Items and totals exactly as charged; payment method masked ("Visa •••• 4329"). Goes wrong: a
   recalculated total that differs by the delivery fee.
4. Next steps: track; change or cancel, with the deadline; for guests "Save your details: add a
   password" (Baymard: offer the account here, not before). Goes wrong: a full sign-up form.
5. Nothing promotional above the confirmation. Goes wrong: a discount banner that pushes the order
   number below the fold.
Tracking: the six details Baymard tested (33% of sites gave all six): expected delivery date first
(25% failed to give it), a status progress bar that starts before dispatch, carrier name, tracking
number linked to the carrier, the full event history, what is in this parcel. Draw the stages as the
lifecycle stepper (017; `finance-and-dashboards.md` §11): check and timestamp per stage, the current
stage as a ring, future stages grey; status as chip words (005); absolute and relative time together
("Thu 6 Mar · in 2 days": 054). Several parcels: one card each, grouped by date (as 068's days).
Failed delivery: what happened, where the parcel is, the two choices, by when. Goes wrong: "In
transit" with no date and a carrier link as the only detail.
Sources: https://baymard.com/blog/integrate-tracking-info

## 8. Comparison tables [285, 288, 291]
1. **Columns**: 2-4 plans or up to 5 products; the item being viewed is the first column (291 leaves
   it out); the header sticky with name, thumbnail and price (Baymard). Goes wrong: six columns of
   near-identical items.
2. **Row labels left**, sentence case, a (?) tooltip only where the term needs one (288); rows
   grouped under headings in the order buyers decide ("Reporting and analytics": 288). Goes wrong:
   forty ungrouped rows in alphabetical order.
3. **Cells say the value**: numbers and words ("10 / 20 / Unlimited", "Basic / Advanced": 288) beat
   ticks; a tick for yes, a dash for no (285, 288), never a red ✕ for what a cheaper plan lacks;
   specs as large value + small unit ("6.8 in", "200 MP": 291). Goes wrong: a "Basic features ✓ ✓ ✓"
   row that says nothing.
4. **Colour as the column key** when plans have colours: each tier's ticks in its own hue (285); the
   recommended column tinted. Goes wrong: the recommended plan invisible in the table.
5. **"Show only differences"** (Baymard: hiding identical rows beats highlighting them); hairlines
   or light zebra so rows can be traced across. Goes wrong: a highlight that appears only on hover.
6. **Mobile**: two columns at a time with a selector per column, row labels as full-width captions
   above each pair. Goes wrong: a five-column table shrunk until unreadable.
7. **Competitor tables** make claims about other companies' products: dated, sourced, Legal review.
   Goes wrong: a column of ✕ under every rival.
Sources: https://baymard.com/blog/user-friendly-comparison-tools

## 9. Landing page hero [086, 087, 088, 091, 095, 096, 098, 099]
- Nav: logo, 4-6 items (dropdowns ok), one outlined + one filled CTA.
- Optional social proof line above the headline ("4.6 Google · 4.9 Trustpilot").
- Headline 2-3 lines, 48-72px; one flourish allowed (italic word, second line in the accent, serif).
- One-paragraph subhead, two buttons (filled + outlined).
- Hero visual: real product UI (screenshot, floating fragments, a diagram) rather than stock photo;
 a functional element (search box: 087) when the product is search-led.
- Logo strip "Trusted by…" below. Dark hero → light body → coloured closing CTA is a reliable rhythm.

## 10. Marketing page sections [288, 292, 096, 098, 091, 086, 088, 087, 046, 033]
Start from the hero (§9). Rhythm: dark hero → light body → coloured close (098); each section has a
small-caps eyebrow, a heading, one paragraph and a real visual.
1. **Logo strip**: "Trusted by 200,000+ users" or "You're in good company" + 6-10 greyscale logos at
   one optical height, one row, faded edges if it scrolls (288, 096; in a rounded panel: 091). Goes
   wrong: logos of companies that are not customers. Instead: customers, with permission.
2. **Feature rows**: alternate text-left / visual-right; eyebrow; a benefit sentence as the heading
   (as 046's card titles); one paragraph; 2-3 checks; a link. The visual is real UI or a cropped
   fragment of it (098, 086). Goes wrong: rows of icon + title + blurb tiles.
3. **Proof numbers** with their source ("4.6 Google · 4.9 Trustpilot": 096), counts and dates. Goes
   wrong: "10x faster" with no basis. Instead: the number, the base, the date.
4. **Testimonial**: a large quote (288: three lines at ~28px), avatar, name, role and company (288),
   the company logo, a link to the case study. One strong quote beats a carousel of five. Goes
   wrong: five stars and a first name. Invented or edited testimonials are a Legal issue.
5. **Section tabs** for long product pages (088); a functional element where the product is a tool:
   a search (087) or a calculator (046). A calculator on a financial-product page shows its
   assumptions and a representative example: Compliance. Goes wrong: tabs on a three-section page.
6. **FAQ** as in §1.8; on a product page, the objections that block the sale. Goes wrong: questions
   nobody asks.
7. **Closing CTA band**: one coloured band or a panel over a photo (292), the offer restated in a
   line, one filled and one outlined button. Goes wrong: a newsletter form as the final call.
8. **Footer**: logo and one line, 3-5 link columns under small grey labels (288), newsletter field,
   social icons, legal row (© · Terms · Privacy · Cookies), and the regulatory statement where the
   product is regulated, quiet but legible (033). A full-width wordmark may close the page (292).
   Goes wrong: legal text missing on a regulated product, or set too small and pale to read.

## 11. Money checks before showing [299, 297, 291, 294, 300]
- Every figure that appears twice is identical: plan card, summary, button, legal text (299 fails
  all four).
- The sums hold: subtotal + delivery + VAT − discount = total; annual saving = 12 × monthly − annual
  (297 fails). Do the arithmetic in the mock, not by eye.
- One currency per page (291 mixes two), one format ("£1,290.00" or "£1,290", not both).
- A discount is shown once, in the rows or as a line, not both (294).
- No placeholder products, prices or names (300); no brand switching mid-flow (297, 299).
- "Was", "most popular", countdowns, stars, "save" and "free" are claims: true, dated, and flagged
  for Legal/Compliance with the rest of the pricing and promotional copy.
