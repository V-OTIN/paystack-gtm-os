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
| Not already a Paystack merchant | Exclude current customers from new-logo outbound. The named customers in 1b are **proof and lookalike seeds, not targets** | Named customers [customers.md]. The customer list to suppress needs Paystack's CRM (Open question 10) |

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
| 3 | Media and subscriptions | 1/4 | None | BusinessDay (1) [customers.md] | Recurring billing, "over 10,000 subscribers" [customers.md] | Not found |

Tier cutoffs: 3 to 4 points = Tier 1, 2 points = Tier 2, 1 point = Tier 3. AXA Mansard counts under both Corporates and Insurance. Global brands were removed: they fail hard filter 1 (see Not a fit).

**Rule for reps:** start with Tier 1. Work Tier 2 only with a live trigger from Layer 3. Tier 3 is outside the ICP (fails filter 1a) until win data moves a vertical up.

### 1c. Size

| What we know | Evidence |
|---|---|
| Paystack gives "Large volume merchants" a dedicated Relationship Manager and "Bulk volume discounts", but publishes no volume threshold | [voice.md] |
| Nigeria's tax authority defines medium taxpayers as N1bn to N5bn annual turnover and large as N5bn and above | [market.md] |
| No employee, revenue or volume cutoff for a Paystack outbound target appears anywhere in the research | Open question 1 |

**Working rule until sales data replaces it:** an account qualifies on size if it is (a) a named enterprise brand, or (b) venture-funded (funding data is observable [signals.md]), or (c) visibly running high-frequency digital payments (wallets, loans, subscriptions, bets). Using the N1bn tax tier as a size proxy is INFERRED and not directly observable in list data, so it is a reference point, not a filter.

## Layer 2: Technographic

Only row 1 is a filter. Rows 2 to 6 decide **which product and angle** to lead with, not whether the account qualifies. Row 8 decides displacement vs greenfield messaging.

| # | Criterion | Role | Product it routes to | Evidence | Detection method in research |
|---|---|---|---|---|---|
| 1 | Takes payments on its own website or app | Filter | Checkout and APIs | "Collect one-time and recurring payments from your app or website" [voice.md] | INFERRED: visible on the website; no tool named |
| 2 | Runs recurring billing or subscriptions | Angle | Subscriptions / recurring billing | Reliance HMO, Workstation, BusinessDay quotes [customers.md] | Not found |
| 3 | Pays out at volume (salaries, earnings, withdrawals, winnings) | Angle | Transfers | PiggyVest, Bolt, Bento, Arena FunBox quotes [customers.md]; transfer pricing [company.md] | Not found |
| 4 | Marketplace that splits revenue | Angle | Subaccounts / split payments | Selar, Weafricans quotes [customers.md] | Not found |
| 5 | Needs KYC at signup | Angle | BVN and account lookup | BuyCoins quote [customers.md]; identity pricing [company.md] | Not found |
| 6 | Bank-transfer collections per customer | Angle | Dedicated Virtual Accounts, "1% per transaction (capped at NGN 300)" | [company.md] | Not found |
| 7 | Built on Shopify, WooCommerce, or uses Xero | Angle (plugin path) | Plugins and integrations | [company.md] | INFERRED: BuiltWith-style lookup [signals.md] |
| 8 | Currently uses another gateway | Messaging | Displacement | BuiltWith can list sites by gateway [signals.md] | BuiltWith [signals.md]. INFERRED: compound only, pair with a Layer 3 signal |

Finding detection methods for rows 2 to 6 is a step 7 task.

## Layer 3: Intent signals

No signal in the research is proven to predict a Paystack purchase (Open question 4). Signals are split by whether the research names a way to detect them.

### 3a. Detectable today (data source named in research)

| Signal | Data source | Link to buying | Evidence |
|---|---|---|---|
| Recent funding round, Nigerian company | Funding trackers: Disrupt Africa, Briter, Africa: The Big Deal, monthly funded-startup lists | INFERRED | Nigeria led Q3 2026 funding with $624M (single source); fintech most active sector [signals.md, market.md] |
| Uses a competitor gateway on its website | BuiltWith | INFERRED; compound only | [signals.md] |
| Dated regulatory deadlines (timing, not account signals) | Calendar: CBN caps 31 Dec 2026; data localisation 1 Jan 2027 | INFERRED | [market.md] |

### 3b. Hypotheses for step 7 (no detection method in research)

| Signal | Why it might matter | Evidence |
|---|---|---|
| Launching subscriptions or recurring billing | Existing customers adopted Paystack for this | Recurring billing quotes [customers.md] |
| Pays out at volume / launching a wallet | Existing customers adopted Paystack for transfers | PiggyVest, Arena FunBox quotes [customers.md] |
| Expanding from Nigeria into GH, KE, ZA or CI | Paystack operates in all five | [company.md]; no source links expansion to buying [signals.md] |
| Opening physical locations in Nigeria | Physical Terminal exists, Nigeria only | [company.md] |
| Hiring payments, finance-ops or payment-engineering roles | None in research | [signals.md] |
| Current acquirer affected by CBN market-share caps | OPay and Moniepoint named; Paystack also named as affected | [market.md] |
| Public complaints about a competitor's payouts or failures | Not researched yet | [signals.md] |

Pains (failed payments, settlement, reconciliation, chargebacks) are not signals. They live in [personas.md](personas.md).

## Layer 4: Persona

Three buyer personas, detailed in [personas.md](personas.md):

| Role in deal | Who | Evidence of their voice |
|---|---|---|
| Champion | CTO / head of engineering | CTO quotes at GUO Transport, Printivo, Reliance HMO, Thrive Agric, FINT [customers.md] |
| Economic buyer | Finance lead (CEO at founder-led firms). No CFO is quoted in the research, so "CFO" is a hypothesis | Senior Finance Officer, Farmcrowdy; Director of Finance & Technology, Nairabox; Chief Risk Officer, Renmoney; CEO quotes at Nairabet, Cowrywise [customers.md] |
| Influencer | Digital, product, growth or operations lead | Chief Digital Officer, AXA Mansard; Chief Transformation Officer, MTN; Growth Lead, Carbon; Operations Manager, Bolt [customers.md] |

## Layer 5: Engagement readiness

| Tier | Observable criteria | Evidence |
|---|---|---|
| Ready now | Passes all 1a filters, Tier 1 vertical, **and** a 3a signal (funding in the last quarter, or a competitor gateway paired with funding) | Layers 1 and 3a |
| Warm | Passes 1a filters, Tier 1 or 2, uses a competitor gateway, no 3a timing signal | Displacement quotes: "After we left our previous payment gateway for Paystack..." [customers.md] |
| Not yet | Passes country filter only; no visible digital payments | INFERRED: the corporate offer (RM, volume discounts) assumes volume [voice.md] |

3b hypotheses do not move an account to "Ready now" until step 7 validates them.

**Proof for outreach, by fit to this ICP** (all customer quotes are undated and likely years old [customers.md]):

| Use for mid-market and enterprise | Do not lead with (small-business speakers) |
|---|---|
| Named logos: MTN, AXA Mansard, Bolt, Carbon, PiggyVest, Renmoney [customers.md] | "about 30% of all abandoned or failed transactions" recovered (Siscomedia Ltd) [customers.md] |
| "a significant increase in our loan collections" (Chief Risk Officer, Renmoney) [customers.md] | "prepaid orders on Bentigos.ng have grown by 15%" (Bentigos.ng) [customers.md] |
| "scaling perfectly to support our large transaction volumes" (Growth Lead, Carbon) [customers.md] | |
| Settlement "before 10 AM, every morning" (Paystack's claim) [voice.md] | |

---

## Not a fit (for outbound)

| Who | Why | Evidence |
|---|---|---|
| Existing Paystack merchants | Not new-logo targets. INFERRED: route to account management for upsell (e.g. Paystack MFB accounts, credit) | [customers.md, company.md] |
| Global brands without a Nigerian entity | Fail hard filter 1. Paystack markets to them ("Paystack for Global Brands" [voice.md]) but services are for businesses registered in NG, GH, ZA, KE [company.md]. Whether they need a local entity: Open question 11 | [voice.md, company.md] |
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
10. The list of current Paystack merchants to suppress from outbound: needs Paystack's CRM. Not in public research.
11. Can a global brand use Paystack without a Nigerian entity? The "Global Brands" page and the registration rule conflict [voice.md, company.md].
12. Do Tier 1 fintech lenders see Paystack as a competitor? Paystack MFB plans working capital loans and embedded accounts for startups [company.md]. INFERRED risk; not tested.
13. Betting regulation in Nigeria: not researched. Tier 1 betting carries unknown regulatory risk.
