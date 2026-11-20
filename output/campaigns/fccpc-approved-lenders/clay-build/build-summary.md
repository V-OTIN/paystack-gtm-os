# What we built in Clay, in plain English (W1 FCCPC approved lenders)

Built 18 to 19 Nov 2026 for the Week 2 brief. Workbook: "V1: Paystack · W1 FCCPC Approved Lenders" in the folder "WF 1- New Digital Lenders".

## The idea

Every digital lender in Nigeria needs FCCPC approval. A newly approved lender needs to collect repayments and pay out loans, which is exactly what Paystack does. So the FCCPC register is the list, and being on it is the signal.

## The three tables

| Table | What it holds | Why |
|---|---|---|
| Exclusions | 11 competitors, named Paystack customers, and Allawee (owned by Paystack) | So we never email a competitor or an existing customer |
| Lenders | The FCCPC register, 526 lenders | The list of companies |
| Contacts | 21 people found at the ready lenders | The people we would email |

## Step by step

1. **Exclusions table.** We built a CSV of companies to avoid and imported it. Each row gets a Register Key (a cleaned-up name and domain) so other tables can look it up.
2. **Imported the register.** The FCCPC page wouldn't paste cleanly into Google Sheets, so we turned it into a CSV with 526 rows and imported that. We didn't use a Clay search, because the register is the real source.
3. **Free formula columns.** These clean the company name, count each lender's apps, and pull a website from the app details where one is listed. Formulas cost nothing.
4. **A small batch.** In Batch? limits paid steps to rows 1 to 45. We started with 30 and widened it to 45 when 30 didn't give us 20 people.
5. **AI column (Claygent).** It finds each lender's website and says how confident it is. We tightened the prompt after it called a dead domain "high".
6. **Manual override.** Where the AI was wrong (parked domains, for-sale pages, the wrong company), we typed the right domain, or a dash to drop the row. Company Domain combines the override, the app domain and the AI result.
7. **Exclusions check.** A free lookup compares each domain to Exclusions. It caught Branch (a Paystack customer) and Allawee (owned by Paystack). Pass Company Gates? is true only if the lender has a domain and isn't excluded.
8. **Signal (BuiltWith).** Tech Stack shows which payment gateway is on the lender's website. Gateway Status turns that into "paystack", "competitor" or "none_detected".
9. **Routing.** Company Ready? drops lenders that already use Paystack (Nextpayday and Creditville). Cell sorts the rest: C if a competitor is on the site (3 lenders, all Flutterwave), D if no gateway was found (19 lenders). All are "Warm".
10. **Company enrichment.** Clay's Enrich company adds size and industry. It only charges when it finds a match.
11. **Finding people.** Find People searches each ready lender's domain for technical and finance or leadership titles. It found 21 people at 10 lenders.
12. **Choosing who to contact.** Persona labels each person as a champion (technical) or an economic buyer (CEO, CFO, founder and similar). Title Rank scores seniority. Champion Pick and Buyer Pick, in Lenders, choose the top person of each type, so there are at most 2 per lender. Chosen? marks those people.
13. **The contact gate.** Ready to Contact? is true only if the lender is ready, the person was chosen, and both persona and cell are filled in. 12 of the 21 passed.
14. **Emails.** The Work Email waterfall tries several providers in turn and validates each result. It ran only on the 12 ready contacts and found 10 emails. We had to turn on auto-run for the waterfall alone so its steps would chain.
15. **The final gate.** Email Domain OK? checks that the email matches the lender's real domain. Send Ready? is the last check: 8 are ready to send. Two were held for a domain mismatch, and two because no email was found.
16. **Views and tidy-up.** We set up three views in Contacts (Ready to send, Held and Dropped) and added a description to every formula column.

## Funnel

526 register rows, 45 in the batch, 24 passed the company gates, 22 ready lenders (3 in cell C, 19 in cell D), 10 lenders with people, 21 people, 12 ready to contact, 10 emails found, 8 ready to send.

## Cost

52.1 credits in total (30,200 down to 30,147.9):

- Claygent: 7.3
- BuiltWith: 23
- Enrich company: 7
- Email waterfall: 14.8

Formulas, lookups and searches were free.

## What we learned

- Prove every paid column on a few rows before running it on more.
- Never click "Run all empty rows" on a big table. One prompt here would have cost about 980 credits.
- AI columns need a strict rule for "high confidence", or they guess.
- In formulas, true and false may be stored as text, so we compare with `String(x) === "true"`.
- A waterfall needs its own auto-run turned on, or only the first provider runs.

## Deferred (optional)

Crunchbase funding (Part 7.2) and job posts (Part 8) only feed an optional line in Email 2, so we skipped them for Week 2.
