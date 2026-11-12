# Paystack ICP (outbound)

**Scope (decided by Valentine, 2026-11-12):** Nigeria first. Mid-market and enterprise. SMBs are out of scope for outbound because they can self-serve ("Start accepting payments in just 30 minutes" [voice.md]).

**Sources:** every row cites a file in `context/docs/research/`. INFERRED = our reading of the cited evidence, not a stated fact. Items with no support are under Open questions.

---

## Layer 1: Firmographic

### 1a. Hard filters (all must be true)

| Criterion | Rule | Evidence |
|---|---|---|
| Country | Registered business in Nigeria | Services "available only to businesses registered in" NG, GH, ZA, KE [company.md]; Nigeria is the core market [company.md] |
| Takes payments digitally | Own website or app with checkout, or a digital product that bills users | The corporate offer (settlement, reconciliation, chargebacks, RM) assumes online volume [voice.md]; see Layer 2 |
| In a Tier 1 or Tier 2 vertical | See 1b | [customers.md, company.md, voice.md] |

### 1b. Vertical priority, ranked by strength of evidence

Scoring: one point each for (1) a dedicated Paystack page or pricing for the vertical, (2) three or more named Nigerian customers, (3) a customer quote tying a Paystack product to a core workflow, (4) a market fact showing activity in 2026. This ranks **how well the research backs each vertical**, not market size or win rate (see Open questions).

| Tier | Vertical | Score | Page / pricing | Named Nigerian customers | Core workflow quote | 2026 market fact |
|---|---|---|---|---|---|---|
| 1 | Fintech: lending, savings, investment, crypto | 4/4 | "For Fintechs" page [company.md] | Renmoney, Carbon, FairMoney, Aella Credit, Branch, PiggyVest, Cowrywise, Farmcrowdy, BuyCoins, FINT, Bento (11) [customers.md] | Payouts (PiggyVest), KYC (BuyCoins), loan collections (Renmoney) [customers.md] | Fintech was the most active sector in Q3 2026: 47 deals, $230.2M [market.md] |
| 1 | Betting and gaming | 3/4 | "For Betting" page [company.md] | Nairabet, Fortunebets, Arena FunBox, Sportsbookcloud (4) [customers.md] | Wallet funding and winnings payouts (Arena FunBox) [customers.md] | Not found |
| 2 | Education: schools and universities | 2/4 | "For Schools" page; schools pricing "0.7% capped at N1,500" [company.md]; universities on corporates page [voice.md] | St. Gregory's College (1) [customers.md] | Reconciliation "used to take weeks" (St. Gregory's) [customers.md] | Not found |
| 2 | Large corporates and government | 2/4 | Corporates page, Relationship Manager, "Bulk volume discounts" [voice.md] | MTN, UPS, AXA Mansard (3) [customers.md] | Not found (quotes are general praise, not one workflow) | Not found |
| 2 | Mobility and transport | 2/4 | None | Bolt, Moove, GUO Transport (3) [customers.md] | Driver payouts (Bolt), webhooks (GUO) [customers.md] | Not found |
| 3 | Insurance and health | 1/4 | None | AXA Mansard, Reliance HMO (2) [customers.md] | Recurring billing for health plans (Reliance HMO) [customers.md] | Not found |
| 3 | Global brands selling into Nigeria | 1/4 | "Paystack for Global Brands" [voice.md] | Not Nigerian; Qatar Airways, Crocs, Under Armour, Burger King named [customers.md] | Not found | Not found |
| 3 | Media and subscriptions | 1/4 | None | BusinessDay (1) [customers.md] | Recurring billing, "over 10,000 subscribers" [customers.md] | Not found |

Tier cutoffs: 3 to 4 points = Tier 1, 2 points = Tier 2, 1 point = Tier 3. AXA Mansard counts under both Corporates and Insurance. Global brands are not Nigerian, so they score on their page only.

**Rule for reps:** start with Tier 1. Work Tier 2 only with a live trigger from Layer 3. Treat Tier 3 as opportunistic until win data says otherwise.

### 1c. Size

| What we know | Evidence |
|---|---|
| Paystack gives "Large volume merchants" a dedicated Relationship Manager and "Bulk volume discounts", but publishes no volume threshold | [voice.md] |
| Nigeria's tax authority defines medium taxpayers as N1bn to N5bn annual turnover and large as N5bn and above | [market.md] |
| No employee, revenue or volume cutoff for a Paystack outbound target appears anywhere in the research | Open question 1 |

**Working rule until sales data replaces it:** an account qualifies on size if it is (a) a named enterprise brand, or (b) venture-funded (funding data is observable [signals.md]), or (c) visibly running high-frequency digital payments (wallets, loans, subscriptions, bets). Using the N1bn tax tier as a size proxy is INFERRED and not directly observable in list data, so it is a reference point, not a filter.

## Layer 2: Technographic

| Criterion | Why it matters | Evidence |
|---|---|---|
| Takes payments on its own website or app | Core product is online checkout and APIs | "Collect one-time and recurring payments from your app or website" [voice.md] |
| Runs recurring billing or subscriptions | Repeated customer use case | Reliance HMO, Workstation, BusinessDay quotes [customers.md] |
| Pays out at volume (salaries, earnings, withdrawals, winnings) | Transfers product | PiggyVest, Bolt, Bento, Arena FunBox quotes [customers.md]; transfer pricing [company.md] |
| Marketplace that splits revenue | Subaccounts / split payments | Selar, Weafricans quotes [customers.md] |
| Needs KYC at signup | BVN and account lookup | BuyCoins quote [customers.md]; identity pricing [company.md] |
| Bank-transfer collections per customer | Dedicated Virtual Accounts, "1% per transaction (capped at NGN 300)" | [company.md] |
| Built on Shopify, WooCommerce, or uses Xero | Paystack partnerships | [company.md] |
| Currently uses another gateway (detectable on the website) | Displacement target | BuiltWith can list sites by gateway [signals.md]. INFERRED: only a compound signal |

## Layer 3: Intent signals

| Signal | Status | Evidence |
|---|---|---|
| Recent funding round (Nigeria) | Supported as a market fact; link to buying is INFERRED | Nigeria led Q3 2026 funding with $624M (single source); fintech most active sector [signals.md, market.md] |
| Launching subscriptions or recurring billing | Supported | Recurring billing quotes [customers.md] |
| Expanding from Nigeria into GH, KE, ZA or CI | INFERRED | Paystack operates in all five markets [company.md]; no source says expansion triggers a purchase [signals.md] |
| Opening physical locations in Nigeria | Supported (product exists) | Physical Terminal for registered Nigerian businesses only [company.md] |
| Hiring payments, finance-ops or payment-engineering roles | INFERRED | No evidence that hiring predicts a Paystack sale [signals.md] |
| Current acquirer affected by CBN market-share caps (deadline 31 Dec 2026) | INFERRED | Caps on card issuing and merchant acquiring; OPay and Moniepoint named; Paystack also named as affected [market.md] |
| Public complaints about a competitor's payouts or failures | INFERRED | Not researched yet [signals.md] |
| Pains: failed payments, slow settlement, reconciliation, chargebacks | Supported as pains; detection method not found | Wall of Love quotes [customers.md] |

## Layer 4: Persona

Three buyer personas, detailed in [personas.md](personas.md):

| Role in deal | Who | Evidence of their voice |
|---|---|---|
| Champion | CTO / head of engineering | CTO quotes at GUO Transport, Printivo, Reliance HMO, Thrive Agric, FINT [customers.md] |
| Economic buyer | CFO / finance director (CEO at founder-led firms) | Senior Finance Officer, Farmcrowdy; Director of Finance & Technology, Nairabox; Chief Risk Officer, Renmoney; CEO quotes at Nairabet, Cowrywise [customers.md] |
| Influencer | Digital, product, growth or operations lead | Chief Digital Officer, AXA Mansard; Chief Transformation Officer, MTN; Growth Lead, Carbon; Operations Manager, Bolt [customers.md] |

## Layer 5: Engagement readiness

| Tier | Observable criteria | Evidence |
|---|---|---|
| Ready now | Nigerian mid-market or enterprise firm in a named vertical **and** a live trigger (funding, new recurring product, expansion, acquirer affected by the caps) | Layers 1 and 3 |
| Warm | Fits Layer 1 and 2, uses a competitor gateway, no trigger yet | Displacement quotes: "After we left our previous payment gateway for Paystack..." [customers.md] |
| Not yet | Fits Layer 1 only; no online payments or volume | INFERRED: the corporate offer (RM, volume discounts) assumes volume [voice.md] |

Proof available for outreach: named enterprise logos [customers.md]; customer-stated results (about 30% of failed transactions recovered, prepaid orders up 15%) [customers.md]; next-morning settlement "before 10 AM" [voice.md].

---

## Not a fit (for outbound)

| Who | Why | Evidence |
|---|---|---|
| SMBs and sole traders | Self-serve in 30 minutes; outbound cost not justified | [voice.md]; scope decision |
| Unregistered businesses | Below mid-market by definition. Terminal products require registration; "Starter Businesses" lets unregistered firms self-serve online payments | [company.md] |
| Businesses outside Nigeria | Out of scope for now. GH, KE, ZA, CI are later phases | Scope decision |
| Competitors and acquirers (Flutterwave, Moniepoint, OPay, Interswitch, Nomba, Kora, Squad, PalmPay) | They sell the same product | [competitors.md] |
| In-store-first, POS-heavy retail | Lower fit, not excluded: third parties say "Moniepoint owns in-store payments. Paystack owns the online checkout." | [competitors.md] |
| Bank-transfer-only collectors | Lower fit, not excluded: Monnify is often recommended for bank-transfer-heavy businesses | [competitors.md] |

---

## Open questions (research does not answer)

1. Size thresholds: no employee count, revenue or volume cutoff for "mid-market" or "large volume merchant" appears in the research. The 1c working rule stands in until Paystack sales or volume data replaces it. Also missing: which verticals Paystack actually wins most. The 1b tiers rank research evidence, not revenue.
2. Win and loss data against Flutterwave, Moniepoint and Interswitch: Not found [competitors.md].
3. Which job titles actually sign Paystack contracts: Not found [signals.md].
4. Whether funding, hiring or new leaders predict a Paystack purchase: Not found [signals.md].
5. Does Paystack's invoicing support Nigeria's e-invoicing rules (IRN, QR)? Not found [market.md]. If yes, it is a trigger for medium taxpayers (enforcement January to March 2027).
6. Current Nigeria market share: Paystack's own pages say both "over 50%" and "nearly 20%" [company.md].
7. Business count: 200,000 (homepage) vs 300K (careers, CEO) [company.md]. Do not use either in copy until confirmed.
8. Does the CBN cap force any Paystack customer or competitor customer to move? Not confirmed [market.md].
9. Is the Paystack MFB corporate account the lead product for some segments? The homepage banner suggests it (INFERRED) [voice.md].
