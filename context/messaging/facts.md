# Paystack: authorized copy facts

> The ONLY source of names, numbers and claims for prospect-facing copy (`/campaign-copy` FACTS GATE). Anything not listed here renders as `{{placeholder}}` in copy. Built from `knowledge-base/playbooks/templates/facts-template.md`.

**Last updated:** 2026-11-12 by Valentine (with Claude Code)
**Approval status:** approved by Valentine for the bootcamp build. **Not approved by Paystack.** Before any live send, Paystack must approve every name and claim below.

---

## Sender identity

| Field | Value |
|---|---|
| Sender name(s) | `{{sender_name}}`, resolved per inbox by the sequencer |
| Title | `{{sender_title}}`, resolved per inbox |
| Signature format | `{{sender_name}}` / `{{sender_title}}` / Paystack |
| Sender persona notes | First person singular. Peer to a technical or finance lead at a lender. Plain, direct, warm [brand.md] |

## What we do (locked value prop)

The lead-in is verbatim; the tail may adapt per route.

- **Variant A (lenders, money both ways):** "Paystack lets lenders collect repayments and send out loans on one integration: a dedicated virtual account per borrower, direct debit, and instant transfers."
- **Variant B (onboarding):** "Paystack also checks BVN and bank account details at signup, through the same integration."

Product one-liner (context, not copy): payments platform for businesses in Africa; online and in-person collections, transfers, recurring billing and identity checks; per-transaction pricing [company.md, voice.md].

## Approved claims (use these exact phrasings)

| Claim | Approved phrasing | Source | Approved by / date |
|---|---|---|---|
| Ownership | "Paystack is a Stripe company" | Homepage footer [voice.md] | Valentine, 2026-11-12 |
| Products for lenders | "dedicated virtual accounts", "direct debit", "transfers" (single and bulk) | Support pricing pages, docs [company.md] | Valentine, 2026-11-12 |
| Identity checks | "BVN and bank account lookup" | Wall of Love (BuyCoins) [customers.md]; identity pricing [company.md] | Valentine, 2026-11-12 |
| Payment notifications | "webhooks that confirm every successful payment" | Wall of Love (GUO Transport) [customers.md] | Valentine, 2026-11-12 |
| Settlement | "settled before 10 AM every morning" | Corporates page, live 2026-11-12 [voice.md]. Caveat: corporates-page claim; confirm it applies to lenders | Valentine, 2026-11-12 |
| Markets | "live in Nigeria, Ghana, Kenya, South Africa and Côte d'Ivoire" | Paystack statement Jan 2026 [company.md] | Valentine, 2026-11-12 |

**Formatting rules:** write "Paystack" and "Renmoney" as plain words, no domains. No currency figures in copy.

## Numbers to keep fuzzy (never quote)

- Number of businesses on Paystack (200,000 on the homepage vs 300K on careers) [company.md]
- Nigeria market share ("over 50%" vs "nearly 20%") [company.md]
- Payment volume growth, profitability, headcount
- Any count from the FCCPC register (526 entries) in prospect copy

## Authorized social-proof names

| Name | What it proves | Matches | Caveat |
|---|---|---|---|
| Renmoney | "a significant increase in our loan collections and we can onboard customers online much faster" (Chief Risk Officer) [customers.md] | Nigerian digital lender | Undated testimonial, likely years old. No numbers approved. Paraphrase allowed: "Renmoney saw loan collections go up and online onboarding get faster on Paystack" |

Everyone else (Carbon, Branch, Aella Credit, PiggyVest, MTN and all other logos) stays out of copy until added here.

## Proof caveats

- Renmoney proves collections and onboarding speed for a lender. It does not prove disbursement speed, settlement time or cost; don't imply it does.
- No customer result has a number approved. Never attach a percentage to Renmoney.

## Banned

### Banned angles
- Price or discount framing (no fees, caps or "cheaper")
- Superlatives Paystack can't prove: "the only gateway", "highest success rates" [voice.md]
- Anything implying the lender's current gateway or team is failing (iron law 14, insult test)
- Congratulating on FCCPC approval (global ban on "congrats"; and approval may be routine compliance, not a launch)
- Regulatory scare framing (CBN caps, data localisation) [market.md]: not proven to affect lenders

### Banned words and phrasing (company-specific)
- "loan app" when describing the prospect (can read as dismissive; say "lender" or their app's name)
- "FCCPC-approved" as a badge of trust in our own claims (we don't speak for the regulator)
- "seamless" (global ban; appears often in customer quotes, never reuse)

### Never in copy
- The suppression or exclusion lists, competitor customer counts, anything from the FCCPC watchlist or delisted sections

## Voice notes

- Register: plain, direct, peer to peer [brand.md]
- Hedges about the prospect: "my guess is", "could be off", "not sure if", "probably"
- Subjects: lowercase, 3 to 5 words, no variables, same subject across the thread

## CTA ladder

- **Primary (E1):** a relevance question, e.g. "Is that how you're set up today?" / "Worth comparing?"
- **Secondary (E2):** offer the specifics, e.g. "Want me to send how Renmoney set it up?"
- **Final (E3):** referral, e.g. "Is someone else the right person for payments?"
- Never: calendar links, "book a call", "free"

## Internal only (never in prospect copy)

- Pricing, merchant counts, register counts, signal scores, routing cells, reply rates
