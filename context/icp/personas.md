# Paystack buyer personas

**Scope:** Nigerian mid-market and enterprise (see [icp.md](icp.md)).
**Sources:** files in `context/docs/research/`. Pains are quoted word for word from customers on Paystack's Wall of Love and Corporates pages [customers.md]. INFERRED = our reading of the cited evidence. Gaps are listed at the end.

**Speaker fit:** quotes from in-scope speakers (Tier 1 or 2 verticals, named enterprise or funded firms) are preferred. Where only a small-business speaker said it, the quote is tagged **(SMB speaker)**: the pain is real but unproven for this ICP.

---

## 1. Champion: technical lead

| | |
|---|---|
| **Job titles** (as quoted) | Chief Technology Officer, Chief Technical Officer (CTO), Developer, Lead Developer, Product Developer, Software Architect [customers.md] |
| **Example speakers** | Femi Jacob (CTO, GUO Transport), Yomi Osamiluyi (CTO, Printivo), Opeyemi Obembe (CTO, Reliance HMO), Arikawe Ayodeji (CTO, Thrive Agric), Nnamdi Okeke (CTO, FINT), Douglas Kendyson (Developer, Selar) [customers.md] |
| **Measured on** | INFERRED from what they praise: payment success rate, uptime, integration speed, reliable transaction notifications, conversion [customers.md] |

**Top three pains (their words):**
1. Lost payment notifications: "With webhooks, Paystack automatically notifies us of all successful transactions even when the customer's browser fails to send us a notification." (CTO, GUO Transport)
2. Hard integrations: "Integrating Paystack into our platform is the easiest we've ever had on any of our technology providers." (CEO, Aella Credit; a CEO, not a CTO, speaking about integration)
3. Customers dropping off at checkout: "our conversion rates increased because people no longer had to leave our website to pay." (CTO, Printivo)

**What makes them start looking:**
- A new product that needs recurring billing: "Paystack's recurring billing feature helped us do that effectively." (CTO, Reliance HMO) [customers.md]
- Payment failures with the current gateway: "Before Paystack, there were constant payments failures." (Marketing Manager, Garanntor Hosting) **(SMB speaker)** [customers.md]
- A marketplace that needs to split revenue (Selar) [customers.md]

**Objections:**
- Support responsiveness: Trustpilot reviews describe slow or no responses; Capterra rates support 3.9/5 [customers.md]
- "We already integrated another gateway": INFERRED from competitor presence [competitors.md]; customers who switched say it was easy ("No bogus paperwork, just a few lines of code") [customers.md]
- Data localisation: Nigerian payment data must be stored in Nigeria by 1 Jan 2027 [market.md]. Paystack's readiness: Not found

---

## 2. Economic buyer: finance lead

| | |
|---|---|
| **Job titles** (as quoted) | Senior Finance Officer, Director of Finance & Technology, Chief Risk Officer; CEO at founder-led firms [customers.md]. No CFO is quoted anywhere in the research; CFO as signer is a hypothesis |
| **Example speakers** | Oluwafemi Owoeye (Senior Finance Officer, Farmcrowdy), Adetokunbo Adetona (Director of Finance & Technology, Nairabox), Daniel Watts (Chief Risk Officer, Renmoney), Akin Alabi (CEO, Nairabet), Razaq Ahmed (CEO, Cowrywise) [customers.md] |
| **Measured on** | INFERRED from what they praise and what the corporate pitch stresses: reconciliation accuracy, settlement speed, chargeback losses, collections, cost per transaction [customers.md, voice.md] |

**Top three pains (their words):**
1. Reconciliation: "Before Paystack, reconciliation was a big issue and the process used to take weeks." (IT Consultant, St. Gregory's College) and "helps us easily reconcile the amounts customers pay us with what we actually have in the bank." (Senior Finance Officer, Farmcrowdy)
2. Chargebacks: "Before Paystack, we had so many chargeback issues." (Director of Finance & Technology, Nairabox)
3. Slow settlement: "unlike others where you have to call, send messages & wait for about a week to get paid." (Web Developer, AdNaira) **(SMB speaker)**. No in-scope speaker is quoted on settlement; the enterprise version is Paystack's own claim: "We settle all merchants before 10 AM, every morning" [voice.md]

**What makes them start looking:**
- Collections falling short: "we've seen a significant increase in our loan collections" (Chief Risk Officer, Renmoney) [customers.md]
- Fast growth straining the current setup: "At a 50% month on month growth rate in Q1 of 2018 alone, we wanted a payment platform that wouldn't break at scale" (Country Manager, Branch Nigeria) [customers.md]
- INFERRED: their current acquirer is hit by the CBN market-share caps (31 Dec 2026) [market.md]

**Objections:**
- Price: Nigeria local "1.5% + NGN 100", capped at NGN 2,000 [company.md]; answered by "Bulk volume discounts", "Zero integration fee", "Zero maintenance fee" [voice.md]. Competitor price comparison: Not found
- Payout delays: Trustpilot complaints about pending payouts [customers.md]
- Regulatory risk: Paystack is named among firms affected by the CBN caps [market.md]; Semafor raises capital-intensity questions about the MFB [company.md]
- "You're becoming our competitor" (Tier 1 fintech lenders): Paystack MFB plans working capital loans, merchant cash advances and embedded accounts for startups [company.md]. INFERRED objection; not tested

---

## 3. Influencer: digital, product or operations lead

| | |
|---|---|
| **Job titles** (as quoted) | Chief Digital Officer, Chief Transformation Officer, Growth Lead, Head of Audience Engagement, Operations Manager, Chief Operating Officer, Country Manager [customers.md] |
| **Example speakers** | Bayo Adesanya (Chief Digital Officer, AXA Mansard), Olubayo Adekanmbi (Chief Transformation Officer, MTN), Henry Uku (Growth Lead, Carbon), Nonso Onwuzulike (Operations Manager, Bolt), Yvette Dimiri (Head of Audience Engagement, BusinessDay) [customers.md] |
| **Measured on** | INFERRED from what they praise: payment options offered, fewer failed payments, subscriber and customer growth, vendor speed [customers.md] |

**Top three pains (their words):**
1. Payment failures and few options: "Since we started using Paystack, payment failures have reduced, and customers now have multiple payment options to choose from." (Chief Digital Officer, AXA Mansard)
2. Cash-only or offline operations: "Before Paystack, Taxify only accepted cash." (Operations Manager, Bolt)
3. A gateway that can't keep up with growth: "Paystack has grown with us, scaling perfectly to support our large transaction volumes." (Growth Lead, Carbon)

**What makes them start looking:**
- A digital or subscription launch: "over 10,000 subscribers already, and Paystack's recurring billing feature makes this possible" (Head of Audience Engagement, BusinessDay) [customers.md]
- Feature requests ignored by the current vendor: "When we make product feature requests, they take it seriously and move fast on it." (Country Manager, Branch Nigeria) [customers.md]
- Customer demand for a new payment method: "We added Paystack as one of our payment options without announcing to our customers, and within a month it shot up to the number one most used option." (CEO, Nairabet) [customers.md]

**Objections:**
- In-store needs: third parties say "Moniepoint owns in-store payments" [competitors.md]; Paystack sells a Physical Terminal in Nigeria (NGN 86,000) [company.md]
- Cross-border volume: third parties say Flutterwave "handles large cross-border volume transactions" [competitors.md]; Paystack supports USD pricing and settlement [voice.md]
- Vendor attention at scale: answered by the dedicated Relationship Manager [voice.md]

---

## Gaps (not in research)

- KPIs per role: all "Measured on" rows are INFERRED. Confirm with customers or sales.
- Who signs the contract in enterprise deals: Not found.
- Procurement steps for government and enterprise buyers: Not found.
- Most quotes are undated and likely years old (references to Taxify, Paylater, 2018) [customers.md]. Pains may have changed.
