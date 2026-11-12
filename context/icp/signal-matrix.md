# Paystack signal matrix (work in progress)

**Status:** draft v1, 2026-11-12. To be validated with Paystack sales and leadership. Not a final deliverable.
**Inputs:** [icp.md](icp.md), [personas.md](personas.md), `context/docs/research/` (cited as [file.md]). Method: `knowledge-base/playbooks/signal-matrix-framework.md` and `workflow-anatomy.md`.
**Scope:** Nigeria, mid-market and enterprise, Tier 1 and Tier 2 verticals from icp.md 1b. Existing Paystack merchants are excluded from every list (icp.md 1a).
**INFERRED** = our reading of cited evidence, not a stated fact. Scores are our judgement (see Matrix 2 scale).

---

## Matrix 1: Segments x personas

Personas (from personas.md): **Champion** = technical lead (CTO, lead developer). **Economic buyer** = finance lead (CEO at founder-led firms; CFO is a hypothesis). **Influencer** = digital, product, growth or operations lead.

### 1a. Angle per cell

| Segment | Champion: technical lead | Economic buyer: finance lead | Influencer: digital / product / ops |
|---|---|---|---|
| **Fintech** (lending, savings, investment, crypto) | One integration for collections, instant withdrawals and BVN checks. Proof: BuyCoins on "BVN & Bank Account Look-Up", PiggyVest on transfers [customers.md] | Collections and reconciliation. Proof: Renmoney "significant increase in our loan collections"; Farmcrowdy reconciles "with what we actually have in the bank" [customers.md] | Users trust you when withdrawals are instant. Proof: PiggyVest "customers can get their savings immediately"; Carbon "scaling perfectly" [customers.md] |
| **Betting and gaming** | Wallet funding plus real-time winnings payouts on one API. Proof: Arena FunBox "winnings transferred to them in real time" [customers.md] | Deposit success turns into revenue. Proof: Nairabet, Paystack "shot up to the number one most used option" [customers.md] | Players feel payouts as the product. Proof: Arena FunBox "to them, it's magic!" [customers.md] |
| **Education** (schools, universities) | Plugins and Payment Pages, no build needed. INFERRED: no education CTO quote; nearest is St. Gregory's IT Consultant [customers.md] | Fee reconciliation in days, not weeks, at schools pricing "0.7% capped at N1,500". Proof: St. Gregory's "used to take weeks" [customers.md, company.md] | Parents pay by card, transfer or USSD. INFERRED from channel list [voice.md]; no education quote |
| **Large corporates and government** | PCI-DSS, network-wide fraud protection, data export to internal tools [voice.md] | Settlement "before 10 AM, every morning", split settlement across accounts, daily automated reports, user permissions [voice.md] | A vendor that moves at your speed. Proof: MTN "speed of delivery, execution excellence"; AXA Mansard "payment failures have reduced" [customers.md] |
| **Mobility and transport** | Webhooks that confirm every payment. Proof: GUO Transport "even when the customer's browser fails" [customers.md] | Driver and partner payouts at transfer pricing (NGN 10 to 50 per transfer) [company.md] | Move riders off cash. Proof: Bolt "Before Paystack, Taxify only accepted cash" [customers.md] |

### 1b. Segment definitions, products, examples, priority

| Segment | Target definition (filterable) | Lead product | Upsell (hypothesis) | Example accounts | Priority |
|---|---|---|---|---|---|
| Fintech | Nigeria-registered; lending, savings, investment or crypto app; takes payments in app; on the FCCPC register (lenders) or funded; not a Paystack merchant; not a competitor (icp.md not-a-fit) | Collections: checkout, Dedicated Virtual Accounts, direct debit [company.md] | Transfers, identity verification [company.md]. Not Paystack MFB: may read as competing (INFERRED; icp.md open question 12) | 2026-funded, customer status unknown: Cardtonic, Stabyl, CreditChek, Trade Lenda [signals.md]. Lookalike seeds (customers, not targets): Renmoney, Carbon, FairMoney, PiggyVest, Cowrywise [customers.md] | **High** |
| Betting and gaming | Nigeria-licensed (NLRC or LSLGA list); online wallet product; not a Paystack merchant | Checkout for wallet funding | Transfers for winnings payouts | MSport (NLRC-cleared) [signals.md]. Rest: requires Clay research on NLRC and LSLGA lists, minus Nairabet, Fortunebets, Arena FunBox, Sportsbookcloud [customers.md] | **Medium**: strong fit, regulation not researched (icp.md open question 13) |
| Education | Nigerian private school or university; collects fees online or plans to | Payment Pages / schools pricing [company.md] | Dedicated Virtual Accounts per student (INFERRED) | Sani Bello University, Kontagora (new 2026 licence) [signals.md]. Rest: requires Clay research on NUC list of 168 private universities [signals.md] | **Low-Medium**: low signal volume |
| Large corporates and government | Named Nigerian enterprise or state revenue agency; high online collection volume | Corporate gateway with Relationship Manager [voice.md] | Terminal; Paystack MFB corporate account (INFERRED) [voice.md] | Requires Clay research: Nigerian enterprises by industry (airlines, insurance, telecoms), minus MTN, UPS, AXA Mansard [customers.md] | **Low** for outbound: no programmatic signal found (Matrix 2) |
| Mobility and transport | Nigerian ride-hailing, logistics, bus or ticketing firm taking digital payments | Checkout | Transfers for driver payouts | Requires Clay research: Nigerian transport and logistics, minus Bolt, Moove, GUO Transport [customers.md] | **Low-Medium**: universal signals only |

### 1c. Phase 2 scoring

| Segment | Signal density | Product fit | Penetrability | Pursue now? |
|---|---|---|---|---|
| Fintech | High: FCCPC register, funding trackers, jobs, BuiltWith | High: 11 named customers, 4/4 evidence (icp.md 1b) | High: digital-first firms, public registers | **Yes, primary** |
| Betting and gaming | Medium: NLRC and LSLGA lists | High: payouts plus deposits (icp.md 1b, 3/4) | Medium: contested regulator lists | **Yes, secondary** |
| Mobility and transport | Low: universal only | Medium | Medium | Later |
| Education | Low: NUC licences are few | Medium | Low (INFERRED: weak digital footprint) | Later |
| Large corporates and government | Low: no tender feed | Medium | Low | Account-based, not signal-led |

---

## Matrix 2: Buying signals

**Scale (our judgement):** each test scored 1 (weak) to 5 (strong). The four tests come from workflow-anatomy.md "Choosing a Mother Intent":
- **Reason** = clear buying reason now
- **Volume** = enough accounts to sustain a workflow
- **Data** = data you can actually get
- **Story** = natural opening line

**Status:** VERIFIED = data source confirmed to exist [signals.md]. COMPOUND = only works paired with another signal. PARTIAL = coverage or volume limits. KILLED = fails "Could I send this to a Clay operator right now with zero ambiguity?"

### 2a. Signals

| # | Type | Signal | Mother intent (catalog) | Segments | Data source | Tool / Clay action | Volume | Reason | Volume | Data | Story | Total /20 | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N1 | Niche | Newly approved (or moved from conditional to full) on the FCCPC digital lenders register | Regulatory changes / niche play | Fintech | fccpc.gov.ng register [signals.md] | Clay HTTP scrape of register, monthly diff | Register 400+ total; new per month Not found [signals.md] | 5 | 3 | 4 | 5 | **17** | VERIFIED (cadence to test). INFERRED: a newly approved lender needs disbursement and collections |
| U9 | Universal | Nigerian company hiring in Accra, Nairobi, Johannesburg, Cape Town or Abidjan | Hiring offshore | Fintech, betting, mobility | Job posts with location filter | Clay "Find Jobs at Company"; LinkedIn Jobs via Apify | Not found; measure in Clay | 4 | 2 | 3 | 5 | **14** | VERIFIED (tool). INFERRED: expansion triggers a provider review; Paystack is live in all five markets [company.md] |
| U2 | Universal | Job post for payments, payment-integration, reconciliation, settlement or treasury roles, especially naming Flutterwave, Monnify or Interswitch (and not Paystack) | Hiring specific roles + competitor customers | All | Job posts; Nigerian boards include MyJobMag [signals.md] | Clay "Find Jobs at Company" with keyword filter | Not found; measure in Clay | 3 | 3 | 3 | 4 | **13** | VERIFIED (tool). Nigerian job-data coverage INFERRED |
| N3 | Niche | New operator on the NLRC or LSLGA licensed list | Regulatory changes / niche play | Betting | nlrc-gov.ng; LSLGA licensed-operators page [signals.md] | Clay HTTP scrape, monthly diff | LSLGA 70+ entities (Sep 2025); new per month Not found [signals.md] | 4 | 2 | 3 | 4 | **13** | VERIFIED (PARTIAL): no dated 2026 list; regulators contest jurisdiction |
| U1 | Universal | Funding round in last 90 days, Nigerian company | Companies fundraising | Fintech, mobility | Crunchbase via Clay; Propel, african-startups.com, Nairametrics [signals.md] | Clay "Find Organization" (Crunchbase) + tracker scrape | Low: 15 disclosed Nigerian deals in Q1 2026 [signals.md] | 3 | 2 | 4 | 4 | **13** | VERIFIED (PARTIAL): low volume. INFERRED buying link |
| U5 | Universal | Headcount growth over 25% in 6 months | Hypergrowth (headcount) | Fintech, betting, mobility | Company headcount data | Clay "Company Headcount" enrichment | Not found | 3 | 3 | 3 | 4 | **13** | VERIFIED (tool). Echoes Branch "wouldn't break at scale" [customers.md] |
| U7 | Universal | New finance or wallet app published by a Nigerian company | New product launches | Fintech, betting | App store listings | Apify Google Play scraper via Clay HTTP (to verify) | Not found | 4 | 3 | 2 | 4 | **13** | INFERRED: data source not verified this session |
| U3 | Universal | New CTO, CFO, head of finance or head of payments in last 90 days | New leadership | All | People data with start date | Clay "Find People" + title + start date | Not found | 3 | 3 | 3 | 3 | **12** | VERIFIED (tool). INFERRED: research has no evidence new leaders switch gateways [signals.md] |
| U4 | Universal | Competitor gateway on website (Flutterwave, Monnify, Interswitch) | Companies using specific software / competitor customers | All | BuiltWith [signals.md] | Clay "Find Technology Stack" (BuiltWith) | INFERRED: high | 2 | 4 | 4 | 2 | **12** | VERIFIED (COMPOUND): pair with U1, U2 or U9. Detectability of each competitor script INFERRED |
| U6 | Universal | Lookalike of named Paystack customers | Lookalike of customers | Fintech, betting | Seed list from customers.md | Clay lookalike / company search | INFERRED: high | 2 | 4 | 4 | 4 | **14** | VERIFIED. Static, not timing: base list only, not a trigger |
| N2 | Niche | New or upgraded CBN licence (MFB, PSP) | Regulatory changes | Fintech | CBN press releases / licensed institutions pages [signals.md] | Clay HTTP scrape | Low; many holders are competitors [signals.md] | 3 | 1 | 3 | 4 | **11** | VERIFIED (PARTIAL) |
| N4 | Niche | New university provisional licence from NUC | Regulatory changes / niche play | Education | nuc.edu.ng news [signals.md] | Clay HTTP scrape of news page | 33 in 2025; 2 in July 2026 [signals.md] | 4 | 1 | 3 | 5 | **13** | VERIFIED. Volume too low for a workflow: one-off list |
| N5 | Niche | State revenue agency digitising collections | Niche play | Corporates and government | News only; no tender feed [signals.md] | None programmatic | Low | 3 | 1 | 1 | 3 | **8** | **KILLED**: manual research only |
| U8 | Universal | Merchant's acquirer hit by CBN caps (31 Dec 2026) or data localisation (1 Jan 2027) | Regulatory changes | All | No account-level source [market.md] | None | Not found | 2 | 1 | 1 | 3 | **7** | **KILLED** as a trigger; keep as narrative timing only |
| U10 | Universal | Medium taxpayer facing e-invoicing enforcement (Jan to Mar 2027) | Regulatory changes | All | Turnover not observable; Paystack support for e-invoicing Not found [market.md] | None | Not found | 2 | 1 | 1 | 2 | **6** | **KILLED** until icp.md open question 5 is answered |

Note: U6 scores 14 but is a base list, not a buying signal, so it is not ranked below.

### 2b. Universal vs niche-specific

- **Universal (one Clay build, swap keywords per segment):** U1, U2, U3, U4, U5, U7, U9, plus U6 as base list. That is 7 live signals plus the base list; U8 and U10 killed.
- **Niche-specific (new build per segment):** N1 (fintech), N3 (betting), N2 (fintech), N4 (education). N5 killed.
- **Compounding insight:** fintech and betting share 6 of 7 live universal builds. Only the registry scrape changes (FCCPC for fintech, NLRC/LSLGA for betting). One "Nigeria registry diff" pattern covers N1, N2, N3 and N4.

### 2c. Play and product per priority segment

| Signal | Fintech play | Fintech product | Betting play | Betting product |
|---|---|---|---|---|
| N1 FCCPC approval | Newly approved lender: disbursement and collections from day one | DVA + checkout + Transfers | n/a | n/a |
| N3 NLRC/LSLGA licence | n/a | n/a | New licensed operator: deposits and winnings payouts from launch | Checkout + Transfers |
| U9 Expansion hiring | Expanding to Ghana or Kenya: one provider across five markets | Checkout in new market | Same play | Checkout + Transfers |
| U2 Payments hiring | Building payments team, naming a competitor | Collections + Identity | Same, keywords "wallet", "payout" | Checkout + Transfers |
| U1 Funding | Fresh round, scaling collections | Collections | n/a (INFERRED: betting rarely VC-funded; not in research) | n/a |
| U5 Hypergrowth | Volume growth, "wouldn't break at scale" | Collections | Same | Checkout + Transfers |
| U4 Competitor on site (compound) | Displacement route for U1/U2/U9 | Same as primary | Same | Same |

---

## Build first: top 5 signals

| Rank | Signal | Why |
|---|---|---|
| 1 | **N1: FCCPC newly approved lenders** | Highest score (17). Primary segment. Public register, timely event, clean story ("you were just added to the FCCPC's approved lenders list"; no congratulations, banned in `context/messaging/facts.md`), and a product match on both sides of a lender's money flow. Few competitors likely watch it (INFERRED) |
| 2 | **U9: Nigerian companies hiring in GH, KE, ZA, CI** | Uses Paystack's clearest structural edge: live in all five markets [company.md]. Works across fintech, betting and mobility. Also matches Paystack's own South Africa push (5 of 15 open roles [signals.md]) |
| 3 | **U2: Payments and finance-ops hiring naming a competitor** | Highest-volume universal build. Same Clay build across segments with keyword swaps. Competitor names route displacement copy |
| 4 | **N3: New NLRC/LSLGA licensed betting operators** | Second Tier 1 segment. Reuses the N1 registry-diff pattern. Hold copy until betting regulation is researched (icp.md open question 13) |
| 5 | **U1 + U4: Funding plus competitor gateway (compound)** | Low volume alone (15 Nigerian deals in Q1 2026 [signals.md]), but cheap to build and a strong story. BuiltWith adds the displacement route |

Not chosen: U5 and U3 (no evidence linking them to gateway decisions), U7 (data source unverified), N4 (too few events), corporates and government (no programmatic signal; treat as account-based).

---

## Matrix 3: Workflow tracker

| W # | Status | Workflow name | Mother intent | Segment | Persona | Channel | Clay URL | Total leads |
|---|---|---|---|---|---|---|---|---|
| W1 | Planned | FCCPC newly approved lenders | Regulatory changes / niche play | Fintech | | | | |
| W2 | Planned | Nigerian companies hiring in GH, KE, ZA, CI | Hiring offshore | Fintech, betting, mobility | | | | |
| W3 | Planned | Payments and finance-ops hiring | Hiring specific roles | All | | | | |
| W4 | Planned | New licensed betting operators | Regulatory changes / niche play | Betting | | | | |
| W5 | Planned | Funded in last 90 days + competitor gateway | Companies fundraising | Fintech, mobility | | | | |
| W6 | Planned | Hypergrowth (headcount over 25%) | Hypergrowth | Fintech, betting, mobility | | | | |
| W7 | Planned | New finance or payments leader | New leadership | All | | | | |
| W8 | Planned | New finance or wallet app launch | New product launches | Fintech, betting | | | | |
| W9 | Planned | New or upgraded CBN licence | Regulatory changes | Fintech | | | | |
| W10 | Planned | New university licences (one-off list) | Regulatory changes | Education | | | | |

Other tracker columns (campaign name, launch date, enrichments, iterations, bounce) are filled as campaigns launch.

---

## Open items before building

1. Suppression list of current Paystack merchants (icp.md open question 10). Every workflow depends on it.
2. Confirm example accounts are not already Paystack customers.
3. Measure real volumes in Clay for every "Not found" volume.
4. Research Nigerian betting regulation before W4 copy.
5. Verify a Google Play data source before W8.
6. Validate scores and priorities with Paystack sales.
