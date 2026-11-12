# Campaign strategy: Paystack outbound

**Date:** 2026-11-12 · v1, work in progress
**Built with:** /campaign-strategy, from `CLAUDE.md`, `context/` (icp, personas, signal-matrix, positioning, messaging, brand-kit, case-studies, research) and `knowledge-base/playbooks/workflow-anatomy.md`.
**Scope:** Nigeria, mid-market and enterprise, Tier 1 and 2 verticals (`context/icp/icp.md`). Two ideas are deliberately outside the ICP (Creative non-ICP).
**Rules:** volumes use numbers from the research where they exist; otherwise "Not found" with an INFERRED band (Low under 20 a month, Medium 20 to 100, High over 100). Customer names may only appear in copy once approved in `context/messaging/facts.md` (not yet created), so copy uses `{{proof_customer}}`.

**Target audience:** Nigerian businesses taking digital payments at volume, led by fintech lending and savings, then betting, education, corporates and mobility [icp.md].
**Core value proposition:** get paid by anyone, anywhere, and see every naira land: one integration for money in and money out [messaging.md].
**Key differentiators:** one integration across nine payment channels; next-morning settlement "before 10 AM"; reconciliation and chargeback tools; live in five African markets; a Stripe company [positioning.md].

---

## Customer discovery analysis

From `context/docs/case-studies.md` (58 stories, mostly undated).

| Company | Industry | Size | Key result | Problem solved |
|---|---|---|---|---|
| Renmoney | Lending | Not found | "significant increase in our loan collections" | Collections, online onboarding |
| Carbon | Lending | Not found | "scaling perfectly to support our large transaction volumes" | Scale |
| PiggyVest | Savings | "Over 2 Million Nigerians" | More usage from instant withdrawals | Payouts |
| Branch | Lending | "50% month on month growth rate in Q1 of 2018" | Chose Paystack to not "break at scale" | Scale |
| BuyCoins | Crypto | Not found | KYC via BVN and account lookup | Identity checks |
| Farmcrowdy | Agri-investment | Not found | Reconciles against the bank | Reconciliation |
| Nairabet | Betting | Not found | Top payment option within a month | Payment adoption |
| AXA Mansard | Insurance | Not found | Fewer payment failures | Failures, options |
| Bolt | Mobility | Not found | Off cash, driver payouts | Cash only |
| BusinessDay | Media | "over 10,000 subscribers" | Recurring billing at scale | Subscriptions |
| St. Gregory's College | Education | Not found | Reconciliation no longer takes weeks | Reconciliation |
| Selar | Creator marketplace | Not found | Revenue splits via Subaccounts | Split payments |

**Patterns**
- Most common industries: lending, savings and investment (9 stories), then betting and gaming (3), plus many small e-commerce and services firms [case-studies.md].
- Sizes: from small sellers to MTN and AXA Mansard; size rarely stated.
- Roles quoted: CTOs and developers, CEOs and founders, finance and risk leads, digital and operations leads [case-studies.md].
- Common problems: payment failures, reconciliation, payouts, recurring billing, integration effort, settlement speed.

**Targeting challenge:** the case studies show a group outside the ICP that recurs: **web developers and agencies who integrate Paystack for their clients** (customers.md notes web developers and agencies who integrate Paystack for clients "appear repeatedly": Naira.Host, ECGD Services, Sanetech, DHELC, Kynox, MrTeey Investments; Mobiapp Nigeria: "I manage multiple Paystack accounts for my clients") [customers.md]. Paystack also has a "For Agencies" page and a "Service Partner Directory" [company.md]. This is a channel the ICP ignores, so it is used for the Creative (non-ICP) ideas below.

**Best customers for lookalike:** Renmoney, Carbon, PiggyVest, Cowrywise, BuyCoins (fintech); Nairabet (betting); AXA Mansard (insurance) [case-studies.md]. All are seeds, never targets.

---

## Campaign ideas, ranked

**Ranking:** Signal strength (1 to 5) + Data ease (1 to 5), highest first. Ties broken by volume. Scores are our judgement.
**Tier:** when to build (skill rubric: signal, data, volume, build time, differentiation).
**Value:** Money = make money, Time = save time, Cost = save money, Risk = mitigate risk.

| Rank | Campaign | Level | Mother intent | Segment / persona | Signal + data source | Angle | Volume / month | Difficulty | Signal | Data | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **FCCPC newly approved lenders** (W1, specced) | Niche | Regulatory changes (niche play) | Fintech lending / Champion, then Economic buyer | New name on FCCPC "Approvals of DMLs" table vs last snapshot; fccpc.gov.ng via Clay HTTP [signals.md] | Post-approval: repayments in and loans out on one integration | Backlog 526 once [signals.md]; new per month Not found (INFERRED Low) | Medium | 5 | 4 | **Tier 1**: unique public register, spec approved |
| 2 | **Payments hiring naming a competitor** (W3) | Focused | Hiring specific roles + competitor customers | All Tier 1-2 / Champion | Job posts for payments, integration, reconciliation, treasury roles mentioning Flutterwave, Monnify or Interswitch; Clay Find Jobs, MyJobMag [signals.md] | You're building payments now: compare before you scale on `{{competitor_name}}` | Not found (INFERRED Medium) | Low | 4 | 4 | **Tier 1**: abundant job data, one build for all segments |
| 3 | **New university licences** | Niche | Regulatory changes (niche play) | Education / Economic buyer (bursar or finance) | New NUC provisional licence; nuc.edu.ng news via Clay HTTP [signals.md] | A new university sets up fee collection once: do it at schools pricing "0.7% capped at N1,500" [company.md] | 33 approvals in 2025; 2 in July 2026 [signals.md] (about 2 a month, derived) | Low | 4 | 4 | **Tier 3**: strong signal, too few events |
| 4 | **Lookalike of fintech customers** (required: Lookalike) | Broad | Lookalike of customers | Fintech / Economic buyer | Companies similar to the seed list above; Clay lookalike + Tracxn (1,103 fintech startups listed in Lagos) [signals.md] | How lenders and savings apps like `{{proof_customer}}` run collections and payouts | Stock: up to 1,103 Lagos fintechs before exclusions [signals.md]; not monthly | Low | 2 | 5 | **Tier 1**: highest volume, fast build, proof-led |
| 5 | **New finance leader** (required: New Hire) | Focused | New leadership (past 90 days) | Fintech, betting / Economic buyer | CFO, Head of Finance, Financial Controller, Chief Risk Officer started under 90 days; Clay Find People + start date | First 90 days: settlement, reconciliation and collections are the stack you inherited; here's a benchmark from `{{proof_customer}}` | Not found (INFERRED Low to Medium) | Low | 3 | 4 | **Tier 2**: reliable data, but no evidence new leaders switch gateways [signals.md] |
| 6 | **New technical leader** (New Hire variant) | Focused | New leadership (past 90 days) | Fintech, betting, mobility / Champion | CTO, Head of Engineering, Head of Payments started under 90 days; Clay Find People | New CTO reviewing the payments integration: one API for collections, transfers and identity | Not found (INFERRED Low to Medium) | Low | 3 | 4 | **Tier 2**: same build as rank 5 |
| 7 | **Nigerian companies hiring abroad** (W2) | Focused | Hiring offshore | Fintech, betting, mobility / Economic buyer | Nigerian-HQ companies posting jobs in Accra, Nairobi, Johannesburg, Cape Town, Abidjan; Clay Find Jobs location filter | Expanding into Ghana or Kenya: keep one payments provider across all five markets [company.md] | Not found (INFERRED Low) | Medium | 4 | 3 | **Tier 2**: best story, unknown volume and HQ matching |
| 8 | **Newly licensed betting operators** (W4) | Niche | Regulatory changes (niche play) | Betting / Champion | New operator on NLRC or LSLGA licensed list; Clay HTTP diff [signals.md] | Launching under licence: deposits and real-time winnings payouts from day one | Stock: LSLGA 70+ entities, NLRC cleared 19 [signals.md]; new per month Not found | Medium | 4 | 3 | **Tier 2**: reuses W1 build; betting regulation not yet researched [icp.md Q13] |
| 9 | **FCCPC airtime and data lenders** | Niche | Regulatory changes (niche play) | Fintech lending / Champion | Separate FCCPC airtime/data lenders approval list [signals.md] | Same loop as W1 for micro-lenders: high-frequency, small-ticket repayments | Not found (list not read) | Low (clone of W1) | 4 | 3 | **Tier 2**: near-zero build cost, unknown size |
| 10 | **Funded in last 90 days + competitor gateway** (W5) | Niche | Companies fundraising + companies using specific software | Fintech, mobility / Economic buyer | Crunchbase round under 90 days, plus BuiltWith competitor script [signals.md] | Fresh round, scaling collections: compare `{{competitor_name}}` before volume locks you in | 15 disclosed Nigerian deals in Q1 2026, all sectors [signals.md] (about 5 a month, derived); fewer after filters | Low | 3 | 4 | **Tier 2**: cheap, strong story, low volume |
| 11 | **Golden ICP stack** | Niche | Regulatory changes + hiring specific roles | Fintech lending / Champion | FCCPC-approved lender AND hiring payments or engineering roles AND competitor gateway on site | What a rep would send after 10 minutes: you're approved, hiring `{{role_title}}`, and on `{{competitor_name}}` | INFERRED Low (single digits) | Medium | 5 | 2 | **Tier 2**: highest relevance, starved volume |
| 12 | **Creative Ideas** (required: Creative Ideas) | Broad | Niche-specific play | Tier 1-2 base list / Champion | None: base list. AI reads the prospect's website and app pages | "I had an idea for `{{company_name}}`": 3 specific uses (e.g. a virtual account per customer, split payments, instant withdrawals) | High (base list) | Low | 1 | 5 | **Tier 1**: no signal needed, fast build, shows research |
| 13 | **Subscription businesses** | Focused | Website content mentions | Media, insurance, edtech, SaaS / Influencer | Pricing page shows monthly or annual plans; Claygent reads pricing page (enum: recurring / one-off / none) | Recurring billing that runs without reminders [case-studies.md: BusinessDay, Reliance HMO, Workstation] | Not found (INFERRED Medium) | Medium | 3 | 3 | **Tier 2**: clear product match, AI classification needed |
| 14 | **Marketplaces with seller pages** (Creative stretch) | Focused | Website content mentions | Marketplaces, logistics, mobility / Champion | Website has "sell on", "become a vendor", "drivers" or "partners" signup pages; Claygent enum | Split revenue and pay sellers automatically next day (Subaccounts) [case-studies.md: Selar, Weafricans] | Not found (INFERRED Medium) | Medium | 3 | 3 | **Tier 2**: distinct angle, AI classification needed |
| 15 | **Hypergrowth** | Focused | Hypergrowth (headcount) | Fintech, betting, mobility / Influencer | Headcount up over 25% in 6 months; Clay Company Headcount | Growth that won't break the payment stack [case-studies.md: Branch, Carbon] | Not found (INFERRED Low to Medium) | Low | 3 | 3 | **Tier 2**: weak link to gateway decisions |
| 16 | **Web agencies and developers** (required: Creative non-ICP) | Broad | Niche-specific play (partner channel) | Nigerian web, app and Shopify/WooCommerce agencies / Founder | Agencies with Nigerian client portfolios; Clay company search + Google Maps (web design agency Lagos, Abuja), minus Paystack's Service Partner Directory | Your clients need payments that work on day one: plugins, multiple client accounts in a few clicks [case-studies.md: Mobiapp Nigeria] | Not found (INFERRED High stock) | Low | 2 | 4 | **Tier 2**: untouched channel, referral not direct revenue |
| 17 | **Diaspora sellers** (Creative stretch) | Focused | Website content mentions | Nigerian e-commerce brands / Founder or Influencer | Site ships internationally or shows USD prices; Claygent enum | Stop cancelling orders from customers abroad: foreign cards and USD settlement [voice.md; case-studies.md: WaraCake] | Not found (INFERRED Medium) | Medium | 2 | 3 | **Tier 3**: often below mid-market size |
| 18 | **Finance and payroll software partners** (Creative non-ICP) | Niche | Niche-specific play (partner channel) | Accounting, payroll and ERP vendors serving Nigerian businesses / Head of Partnerships | Vendors with Nigerian customers; Clay company search, partner pages | Embed collections and payouts for your users; Paystack partners with Xero [company.md]; payroll proof from Bento [case-studies.md] | Not found (INFERRED Low) | High | 2 | 3 | **Tier 3**: partnership cycle, not cold outbound |

**Required types present:** Lookalike (4), New Hire (5, 6), Creative Ideas (12), Creative non-ICP (16, 18). **Creative stretch:** 11, 14, 17. **Golden ICP:** 11.

---

## Campaign overviews (copywriter handoff)

1. **FCCPC newly approved lenders.** Full structure in `output/campaigns/fccpc-approved-lenders/workflow-spec.md` (4 cells: new or backlog × competitor or none detected). Hook: their FCCPC approval. Proof: `{{proof_point}}` on loan collections. CTA: a short comparison call. Unlike 4, it is timed to an event.
2. **Payments hiring naming a competitor.** Hook: the open role (`{{role_title}}`) and the competitor named in the job post. Personalised: role, competitor, segment angle from signal-matrix Matrix 1. CTA: "worth a side-by-side before the new hire builds on `{{competitor_name}}`?" Unlike 10, the trigger is team-building, not capital.
3. **New university licences.** Hook: the NUC licence. Content: schools pricing, Payment Pages, reconciliation for fee collection (St. Gregory's proof once approved). CTA: set up fee collection before first intake. Run as a one-off list each month.
4. **Lookalike of fintech customers.** Hook: a peer, not a signal. Personalised: AI picks the closest seed by product type (lending, savings, crypto) and names the matching proof. CTA: "want to see how `{{proof_customer}}` set it up?" Broadest Tier 1 list.
5. **New finance leader.** Hook: their new role and start date. Personalised: previous company, segment. Angle: what they inherited (settlement, reconciliation, collections), never "it's broken". CTA: a benchmark conversation.
6. **New technical leader.** Same build as 5, champion side: one API, webhooks, identity. CTA: technical walkthrough.
7. **Nigerian companies hiring abroad.** Hook: the job post in Accra or Nairobi. Angle: one provider across the five live markets. CTA: "planning payments for the `{{market}}` launch yet?"
8. **Newly licensed betting operators.** Hook: the licence. Angle: wallet funding and real-time winnings payouts (Arena FunBox, Nairabet proof once approved). Hold copy until betting regulation is researched.
9. **FCCPC airtime and data lenders.** Clone of W1 on the second FCCPC list. Read the list first to confirm size and fields.
10. **Funded + competitor gateway.** Hook: the round (`{{round_type}}`). Secondary: competitor on site. CTA: compare before scaling. Low volume, so run bi-weekly.
11. **Golden ICP stack.** Three facts in the first line: approval, the role they're hiring, their current gateway. Highest relevance; expect very few rows.
12. **Creative Ideas.** "I had an idea for `{{company_name}}`" + 3 bullets generated from their site (e.g. a virtual account per customer for repayments, Subaccounts for agents, instant withdrawals). Proof: one approved case. CTA: "would any of these be useful?" Broadest message; runs on the base list of the ICP.
13. **Subscription businesses.** Hook: their plans page. Angle: recurring billing without reminders. Proof: BusinessDay, Reliance HMO (once approved).
14. **Marketplaces with seller pages.** Hook: their seller or driver signup page. Angle: split revenue and pay out next day automatically. Proof: Selar.
15. **Hypergrowth.** Hook: team growth. Angle: a payment stack that keeps up. Proof: Branch, Carbon.
16. **Web agencies and developers.** Hook: their client work. Angle: plugins, managing many client accounts, payments that work on launch day. Ask: become a referral or Service Partner. Measured in referred merchants, not meetings.
17. **Diaspora sellers.** Hook: they ship abroad or price in USD. Angle: accept foreign cards and settle in USD. Check size before sending.
18. **Finance and payroll software partners.** Hook: their Nigerian user base. Angle: embed collections and payouts. A partnership motion handed to Paystack's partnerships team (owner Not found).

---

## No-AI campaigns

**Newly approved lender: plain note** (variant of 1)
- Why it works without AI: the FCCPC approval is the whole hook; the list itself carries the relevance.
- Core message: note the new FCCPC listing (no congratulations: banned in `context/messaging/facts.md`), one line on money in and money out on one integration, one proof point, a yes/no question.

**Agencies: referral offer** (variant of 16)
- Why it works without AI: every agency in the list builds client sites; the offer is the same for all.
- Core message: you build sites, your clients need payments, here is how Paystack plugins and multi-account management help, want to be listed as a partner?

---

## Front-end offers

1. **Payments setup review for newly approved lenders** (INFERRED offer, not stated by Paystack): a 20-minute review of their repayment and disbursement flow against Paystack's products (virtual accounts, direct debit, transfers). Lower ask than a demo; fits ranks 1, 9, 11.
2. **Try the live checkout** (Paystack offers a demo checkout and "Start accepting payments in just 30 minutes" [company.md, voice.md]): send the demo link so the champion sees the checkout before any call. Fits ranks 2, 6, 12.
3. **Agency partner listing** (Paystack has a "Service Partner Directory" [company.md]): offer agencies a path to be listed. Fits rank 16.

---

## Next

Rank 1 is already specced (`output/campaigns/fccpc-approved-lenders/workflow-spec.md`, STRUCTURE-APPROVED). Next to spec: rank 2 (payments hiring naming a competitor) or rank 4 (lookalike) with `/build-workflow-spec`. Before any copy: create `context/messaging/facts.md` so proof customers can be named.
