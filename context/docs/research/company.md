# Paystack: company

Raw research. Facts only, each with a source and the date checked. Inferences are marked INFERRED.

**Method note (2026-11-12):** paystack.com (homepage, /pricing, /about, /careers, /docs, country pages) returned HTTP 403 to our automated fetch. Facts below come from support.paystack.com (fetch worked), press and third-party pages. Quotes from some third-party pages were truncated by the fetch tool to about 125 characters, marked "(truncated)".

## What they sell

- Self-description: "Paystack is a payment service provider that facilitates easy, fast and secure online and in-person payments" ... "for African businesses". Source: https://support.paystack.com/en/articles/2130562 (checked 2026-11-12)
- Offers "no-code, low-code and pro-code tools"; merchants can start accepting payments "within minutes". Features listed on the same page: recurring payments, invoicing, subscription billing, split payments. Source: https://support.paystack.com/en/articles/2130562 (checked 2026-11-12)
- Homepage title tag: "Paystack - Modern online and offline payments for Africa". Source: search result title for https://paystack.com/ (checked 2026-11-12)
- YC tagline: "Modern payments infrastructure for Africa". YC description: "We enable businesses to accept payments via credit card, debit card, money transfer, and mobile money" (truncated) "directly from their website or mobile app". Source: https://www.ycombinator.com/companies/paystack (checked 2026-11-12)

## Products (names seen in Paystack docs, support and changelog)

| Product | What the source says | Source (checked 2026-11-12) |
|---|---|---|
| Payments / checkout | Cards, bank transfer, USSD, mobile money, M-PESA, EFT, Apple Pay, Direct Debit (from pricing table) | https://support.paystack.com/en/articles/2130306 |
| Product Links, Payment Pages, Storefront | Sell one product with Product Links, or multiple via Payment Pages or Storefront; stock management and delivery fees | search snippet of support.paystack.com (not fetched directly) |
| Invoices | Listed as a no-code tool alongside Payment Links and Storefront | search snippet of website-v4.paystack.co (page now 404) |
| Subscriptions / recurring | "recurring charges with subscriptions or authorizations" | search snippet of https://paystack.com/docs/payments/ (403 on fetch) |
| Transfers (single and bulk) | Kenya merchants can send to any Kenyan bank or M-PESA account | search snippet of https://paystack-changelog.netlify.app/ |
| Dedicated Virtual Accounts | Unique account number per customer or order; Nigeria pricing "1% per transaction (capped at NGN 300)" | https://support.paystack.com/en/articles/2130306 |
| Virtual Terminal | "Only Registered Businesses in Côte d'Ivoire, Ghana, Kenya, Nigeria and South Africa can use Virtual Terminal." | https://support.paystack.com/en/articles/2131842 |
| Physical Terminal (POS) | "Only Registered Businesses in Nigeria currently have access to our Physical Terminals." Device: Live Morefun M960, NGN 86,000 | https://support.paystack.com/en/articles/2131842 |
| Identity verification | Account Number Resolve API (Nigeria, Ghana): Free. Account Validation API (South Africa): ZAR 3 per successful call | https://support.paystack.com/en/articles/2130818 |
| Zap | Consumer payments / money transfer app, launched March 2025 | https://www.semafor.com/article/01/20/2026/paystack-eyes-growth-beyond-payments-with-restructuring |
| Paystack Microfinance Bank | Former Ladder MFB, acquired January 2026. Planned: working capital loans, merchant cash advances, overdrafts using gateway transaction history | https://www.billionaires.africa/2026/01/19/shola-akinlade-paystack-targets-nigerias-32-billion-financing-gap-for-small-businesses/ |
| Card issuing (via Allawee) | Allawee was issuing cards for Piggyvest, Nomba and Carbon by May 2025; Allawee accounts close 1 Dec 2026 | https://www.billionaires.africa/2026/09/01/paystack-quietly-acquired-nigerian-fintech-allawee-and-is-now-shutting-it-down-to-build-something-bigger/ |

Partnerships (per Wikipedia): Shopify (2016), WooCommerce preferred payment partner (2021), Apple Pay (2021), Xero (2022). Source: https://en.wikipedia.org/wiki/Paystack (checked 2026-11-12)

## Pricing model

Per-transaction fees, no subscription. Fees "are deducted per transaction, and we settle the difference via your payouts." Source: https://support.paystack.com/en/articles/2130306 (checked 2026-11-12). The page shows no "last updated" date.

### Transactions (verbatim figures)

| Country | Local | International | Source |
|---|---|---|---|
| Nigeria | "1.5% + NGN 100 (all local channels, including Direct Debit)". "All local transaction fees are capped at NGN 2,000, while the NGN 100 fee is waived for transactions under NGN 2,500." | "3.9% + NGN 100 (via Mastercard, Visa, Verve cards)"; "4.5% (via American Express cards)" | https://support.paystack.com/en/articles/2130306 |
| Nigeria, schools | "0.7% capped at N1,500 for Local card payments. For all other payment methods, we charge a Flat fee of NGN300." | | same |
| Ghana | "1.95% (cards, mobile money, bank transfer)" | "1.95%" (column inferred by fetch tool) | same |
| Kenya | "2.9% (cards)"; "1.5% (M-PESA)" | "3.8% (via Mastercard, Visa, ApplePay and American Express cards)" | same |
| South Africa | "2.9% + R1.00 (VAT exclusive)"; "2% (via EFT)" | "3.1% + R1.00 (VAT exclusive)" | same |
| Côte d'Ivoire | "3.2% VAT excl (cards)"; "1.95% VAT excl. (mobile money via Wave, MTN Côte d'Ivoire and Orange Money)" | "3.8% VAT excl." | same |
| Egypt | "2.7% + EGP 2.5 (via Visa and Mastercard)"; "2.0% + EGP 2.5 (via Meeza)" | "3.5% + EGP 2.5" | same |

- Passing fees to customers: "Currently, only Nigerian businesses can enable this feature directly from the dashboard." Source: same page.
- Conflict: an older search snippet showed Nigeria local at 3.9% + NGN 100. The current support page shows 1.5% + NGN 100 for local and 3.9% + NGN 100 for international. Treat 1.5% local as current.

### Transfers (payouts)

- Nigeria: "NGN 10 per successful transfer" (NGN 5,000 and below); "NGN 25" (NGN 5,001 to 50,000); "NGN 50" (above NGN 50,000). "Stamp duty of NGN 50 apply for transfers of NGN 10,000 and above".
- Ghana: mobile money "GHS 1 per successful transfer"; bank "GHS 8 per successful transfer".
- Kenya M-Pesa: KES 20 / KES 40 / KES 60 by band (KES 10 to 1,500; 1,501 to 20,000; above 20,001).
- South Africa: "ZAR 3 per transfer (failed or successful)".
- Source: https://support.paystack.com/en/articles/2130370 (checked 2026-11-12)

### Terminal

- Physical Terminal card transactions: 0.5% capped at NGN 1,000. Transfers and USSD on terminal: 1.5% + NGN 100, capped at NGN 2,000. Virtual Terminal Nigeria transfer: 0.5% capped at NGN 500. Source: https://support.paystack.com/en/articles/2131842 (checked 2026-11-12)

## Markets

- "Our services are available only to businesses registered in" Nigeria, Ghana, South Africa and Kenya, "but we aim to serve merchants across Africa soon." Private beta: "We're currently running a private beta program in Côte d'Ivoire and Egypt." Source: https://support.paystack.com/en/articles/2130562 (checked 2026-11-12)
- January 2026 statement: licensed and operational in Côte d'Ivoire, Ghana, Kenya, Nigeria and South Africa; regulatory approvals underway in Egypt and Rwanda; together about 46% of Africa's GDP. Sources: https://techpoint.africa/news/paystack-creates-holding-company/ and https://techeconomy.ng/paystack-launches-holding-company-few-days-after-ladder-mfb-acquisition/ (both 2026-01-20, checked 2026-11-12)
- Conflict: the support page lists four markets plus a Côte d'Ivoire beta; the January 2026 statement lists Côte d'Ivoire as operational. INFERRED: the support page is older than the January statement.
- South Africa was the first market outside Nigeria (May 2021). Source: https://en.wikipedia.org/wiki/Paystack (checked 2026-11-12)
- Nov 2023: cut 33 staff in Europe and the UAE, reducing operations outside Africa. Sources: https://techpoint.africa/2023/11/16/paystack-slashes-its-headcount/ , https://www.bloomberg.com/news/articles/2023-11-17/stripe-backed-nigerian-fintech-paystack-cuts-overseas-staff (checked 2026-11-12)
- Offices listed by a third-party profile: Lagos (HQ), San Francisco, Cape Town, Accra, Nairobi. Source: https://altss.com/profile/paystack (checked 2026-11-12)

## Scale

- "Over 200,000 businesses across the continent — both registered and unregistered — use Paystack to process payments." Source: https://support.paystack.com/en/articles/2130562 (checked 2026-11-12)
- Akinlade: Paystack is used by 300,000 merchants. Source: https://www.semafor.com/article/01/20/2026/paystack-eyes-growth-beyond-payments-with-restructuring (2026-01-20, checked 2026-11-12)
- "more than 300,000 Nigerian merchants" (in context of Paystack MFB). Source: https://techpoint.africa/news/paystack-creates-holding-company/ (2026-01-20, checked 2026-11-12). Note: sources disagree on whether 300,000 is total or Nigeria only.
- Payment volume grew "more than twelvefold since the Stripe acquisition". No absolute TPV given. Source: https://businessday.ng/technology/article/a-decade-on-flutterwave-paystack-and-moniepoint-compete-for-africas-financial-plumbing/ (2026-03-03, checked 2026-11-12)
- About 60,000 merchants at acquisition (2020); BBC (Nov 2020) reported over 50% of Nigeria's web payments. Source: https://en.wikipedia.org/wiki/Paystack (checked 2026-11-12)
- BuiltWith tracks 11,321 live websites using Paystack. Source: search snippet of https://trends.builtwith.com/payment/Paystack (checked 2026-11-12)
- Absolute TPV, revenue, profit figures: **Not found.**

## Profitability

- Profitable across all markets for the first time in February 2025; seven profitable months in 2025 (per Akinlade). Source: https://www.semafor.com/article/01/20/2026/paystack-eyes-growth-beyond-payments-with-restructuring (checked 2026-11-12)
- "the group is profitable" (Paystack statement, no figures). Source: https://businessday.ng/technology/article/a-decade-on-flutterwave-paystack-and-moniepoint-compete-for-africas-financial-plumbing/ (checked 2026-11-12)

## Funding and ownership

| Date | Event | Source (checked 2026-11-12) |
|---|---|---|
| 2015 | Founded by Shola Akinlade and Ezra Olubi, Lagos | https://en.wikipedia.org/wiki/Paystack |
| Winter 2016 | Y Combinator W16 batch | https://www.ycombinator.com/companies/paystack |
| 2016 | Seed, $1.3M; investors include Tencent and Comcast Ventures | https://en.wikipedia.org/wiki/Paystack |
| 2018 | Series A, $8M, led by Stripe, with Visa and Tencent | https://en.wikipedia.org/wiki/Paystack |
| Oct 2020 | Acquired by Stripe for "over $200 million" (one reference cites €180m) | https://en.wikipedia.org/wiki/Paystack |
| 2024 | Paystack-led consortium rescued Brass; Brass absorbed into Paystack MFB June 2026 | https://www.billionaires.africa/2026/09/01/paystack-quietly-acquired-nigerian-fintech-allawee-and-is-now-shutting-it-down-to-build-something-bigger/ |
| 2025 | Undisclosed acquisition of Allawee (card issuing) | same |
| Oct 2025 | TSG shareholder agreements signed, pending regulatory approval | https://www.semafor.com/article/01/20/2026/paystack-eyes-growth-beyond-payments-with-restructuring |
| Jan 2026 | Acquired Ladder Microfinance Bank, renamed Paystack Microfinance Bank | https://www.billionaires.africa/2026/01/19/shola-akinlade-paystack-targets-nigerias-32-billion-financing-gap-for-small-businesses/ |
| Jan 2026 | Announced The Stack Group (TSG): Paystack, Zap, Paystack MFB, TSG Labs. Founding shareholders: Stripe, Akinlade, Paystack's employees | https://techpoint.africa/news/paystack-creates-holding-company/ |

- Wellfound lists $11.7M total raised (consistent with seed + Series A + earlier). Source: https://wellfound.com/company/paystack (search snippet, checked 2026-11-12)
- TSG regulatory approval status as of Nov 2026: **Not found.**

## Team size

- 209 employees (Semafor: TSG founding shareholders include "Paystack's 209 employees"). Source: https://www.semafor.com/article/01/20/2026/paystack-eyes-growth-beyond-payments-with-restructuring (2026-01-20, checked 2026-11-12)
- YC page: Team Size 115 (undated snapshot). Source: https://www.ycombinator.com/companies/paystack (checked 2026-11-12)
- Hiring: Greenhouse boards exist for Paystack and Paystack MFB. Sources: https://job-boards.greenhouse.io/paystack/jobs/8460184002 , https://job-boards.greenhouse.io/paystackmfb/jobs/8372213002 (search snippets, checked 2026-11-12)

## Leadership

| Name | Role | Source (checked 2026-11-12) |
|---|---|---|
| Shola Akinlade | Co-founder and CEO | https://www.semafor.com/article/01/20/2026/paystack-eyes-growth-beyond-payments-with-restructuring |
| Ezra Olubi | Co-founder, former CTO. YC: "Led the technology function at Paystack from 2015-2025". Fired November 2025 after allegations of inappropriate behaviour; not a TSG shareholder; has threatened legal action | https://www.ycombinator.com/companies/paystack , https://www.semafor.com/article/01/20/2026/paystack-eyes-growth-beyond-payments-with-restructuring |
| Amandine Lobelle | COO in a 2023 TechCabal interview; quoted on TSG in Jan 2026 per search snippet. Current title not confirmed | https://techcabal.com/2023/06/01/paystack-after-two-years-of-stripe-acquisition/ , https://techcabal.com/2026/01/20/paystack-restructure-tsg/ (search snippets; TechCabal blocks fetch) |

- Current CTO, country heads (Ghana, Kenya, South Africa, Côte d'Ivoire), head of sales, Paystack MFB CEO: **Not found.**

## 2026 strategy (as reported)

- Akinlade: "There are significant opportunities to support businesses beyond payments." Source: https://techpoint.africa/news/paystack-creates-holding-company/ (2026-01-20, checked 2026-11-12)
- Akinlade: "The launch of TSG signals a larger scope of ambition for us and sets the tone for the next decade of our company." Source: https://techeconomy.ng/paystack-launches-holding-company-few-days-after-ladder-mfb-acquisition/ (checked 2026-11-12)
- Moonshot, late Oct 2026: Akinlade said Paystack will look beyond payment acceptance to more of businesses' financial needs. Source: search summary of https://techcabal.com/2026/10/29/paystack-looks-beyond-payments/ (403 on fetch; not read directly)

## Update 2026-11-12: careers site

- Mission: "Paystack's mission is to power African ambition." Scale: "Over 300K businesses across Nigeria, South Africa, Ghana, and Kenya". Source: https://careers.paystack.com/jobs/8042968-qa-lead (checked 2026-11-12). Conflict remains: the live homepage (pasted 2026-11-12) still says "Trusted by over 200,000 businesses", while the careers page and the CEO (Jan 2026) say 300K. Do not use either number in copy until confirmed.
- Benefits mention "TSG Equity compensation" and a 13th month bonus. Source: same.
- Careers index shows 15 open jobs. Departments: Business, Creative Studio, Engineering, Paystack MFB, Product, Revenue. Countries: South Africa, Côte d'Ivoire, Ghana, Kenya, Nigeria, UAE. Source: https://careers.paystack.com/ (checked 2026-11-12). Full role list in signals.md.
- Paystack MFB has its own site, paystackmfb.com (footer link). Source: same.
- Corporates page claims "Paystack processes over 50% of all online transactions in Nigeria" and next-morning settlement "before 10 AM". Source: https://paystack.com/corporates (search snippet, possibly years old, checked 2026-11-12)

## Update 2026-11-12: Wall of Love footer (pasted by user from https://paystack.com/wall-of-love)

- "Paystack is a Stripe company"
- Offices: Lagos (126 Joel Ogunnaike Street, Ikeja GRA), San Francisco (2261 Market Street), Cape Town (51 Wale Street), Johannesburg (32A Jellicoe Avenue, Rosebank), Accra (VIVO Place, Cantonments), Dubai (Al Thuraya Tower 1, Dubai Internet City), Nairobi (The Pavilion, Westlands), Abidjan (AfricaWorks, Zone 4/C). Contact: hello@paystack.com.
- Segment pages in nav: Entrepreneurs, Corporates, International Companies, Startups, Fintechs, Agencies, Schools, Betting. Products in nav: Commerce, Terminal.

## About page (pasted by user from https://paystack.com/about, 2026-11-12)

### Milestones, in Paystack's words
| Date | Milestone (verbatim) |
|---|---|
| 2015 | "Paystack is founded by Shola Akinlade and Ezra Olubi, software developers and longtime friends" |
| Nov 2015 | "Paystack becomes the first Nigerian company to be accepted into the Y Combinator" |
| Jan 2016 | "Public launch" / "Paystack comes out of beta!" |
| Dec 2016 | "Paystack raises $1.3 million from local and international investors, including Tencent, Comcast Ventures, and Ventures Platform" |
| Jul 2017 | "Launch of Pay with Bank": "the ability for customers to pay with only a bank account number" |
| Jul 2017 | "For the first time, Paystack processes over 1 billion Naira (~$3 million) in a single month" |
| Feb 2018 | "Launch of Paystack Starter Businesses": "businesses who aren't yet formally registered are able to get started with online payments" |
| Aug 2018 | "Paystack raises $8 million Series A led by Stripe, together with Visa, and follow-on investment from Tencent and Y Combinator." |
| Oct 2018 | "For the first time, Paystack processes over 10 billion Naira (~$27.5 million) in a single month" |
| Oct 2020 | "Stripe acquires Paystack to accelerate commerce across Africa" |

Note: the timeline stops at 2020. It does not mention Zap, TSG, Paystack MFB or expansion markets.

### Team roster on the About page
- Shola Akinlade: "CEO, Co founder" (the only person with a title; everyone else is listed by function: Product, Engineering, Commercial, Growth, Business, Revenue, Design).
- Amandine Lobelle is listed under "Business" (no title shown). Ezra Olubi is not in the roster.
- Functions used: Engineering (largest group by eye, INFERRED), Business, Growth, Revenue, Product, Design, Commercial.
- Names include several South African and Kenyan staff (e.g. Revenue: Mechiel Couvaras, Hazel Stuart; Growth: Andrew Nduati, Jacqueline Mutero), and Ghana (Revenue: Felix Darko). Country of each person is INFERRED from name only and not reliable.
- Leadership titles beyond the CEO: still **Not found**. The About page does not give them.

## Homepage (pasted by user from https://paystack.com/, 2026-11-12)

- Payment channels listed: Card, Bank Account, Bank Transfer, USSD, POS, Apple Pay, Google Pay, Visa QR, Mobile Money.
- Claims (Paystack's own, unverified): "highest transaction success rates in the market" through automatic routing; "automated and manual fraud systems".
- Segments on homepage: Global Brands, Entrepreneurs, Large Organizations (Nigeria corporate and government).
- Top banner promotes registering a business and getting "a corporate bank account". INFERRED: this is the Paystack MFB product.
- Investors named in quotes: Stripe, Visa, Y Combinator.

## Corporates page (pasted by user from https://paystack.com/corporates, 2026-11-12)

- Corporate offer (Paystack's words, see voice.md): settlement within 24 hours, "before 10 AM, every morning"; split settlement to multiple bank accounts; USD pricing and USD settlement; dashboard chargeback management; PCI-DSS; network-wide fraud protection; user permissions; dedicated Relationship Manager for large-volume merchants; "Zero integration fee", "Zero maintenance fee", "Bulk volume discounts".
- Market share claims conflict on the same page: "over 50% of all online transactions in Nigeria" vs "nearly 20% of all online transactions". Current share: **Not found.**
