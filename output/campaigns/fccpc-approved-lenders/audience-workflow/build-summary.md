# Week 2B: Audience segment + Workflow (W1 FCCPC approved lenders)

Built 19 Nov 2026 for the Week 2B brief (Sandra Uche, "Your Week 2B build", resource PDF page 10). Built from Claude Code with the Clay plugin and CLI, checked in Clay. Workspace: Valentine's Workspace.

## In one sentence (the audience criteria)

Companies on the FCCPC digital lender register (Nigeria, W1 batch S/N 1 to 45) that have a verified website domain and are not on the W1 exclusion list.

**Entity:** companies. **Exclusions:** Paystack competitors, named Paystack customers and Paystack-owned companies (the W1 exclusions list). In this batch that removes Branch International (a named Paystack customer, customers.md) and Allawee Technologies (owned by Paystack, company.md). Lenders with no confirmed domain are left out too, because the enrichment needs a domain to run.

## How it maps to SEA (Segment, Enrich, Act)

| Step | What we built | Where |
|---|---|---|
| Load | 45 lenders from the Week 2 Lenders table, written into the Companies audience by a small loader workflow | Workflow "W1 · Load FCCPC lenders to Audiences" |
| Segment | "W1 · Lenders to enrich": 24 of the 45 match | Audiences > Companies |
| Enrich | BuiltWith "Enrich website technologies" on each lender's domain (1 credit) | Workflow "W1 · Lender gateway check and routing" |
| Act | A routing rule writes W1 Route back to the lender's record. Three destination segments fill from it | Same workflow, plus 3 segments |

## The Audience

**Fields added to Companies** (inputs from the register and Week 2): FCCPC S/N, FCCPC Register Name, FCCPC App Names, FCCPC Entry Type, FCCPC Snapshot Month, W1 Source, W1 Excluded, W1 Exclusion Reason, W1 Website Confidence. The default fields Company name, Domain and Country are filled too.

**Fields the workflow writes back** (outputs): W1 Gateway Status, W1 Gateway Name, W1 Route, W1 Cell, W1 Route Reason, and Technographics (the list of technologies BuiltWith found).

**Identifier:** the Audiences record ID. The loader matched on External record ID (`fccpc-<S/N>`) and then domain. The enrichment workflow writes back by record ID, so results always land on the same lender. Clay also matched 45 of 45 to its own company records (LinkedIn page, logo).

**Segments (all dynamic filters, no fixed lists):**

| Segment | Filter | Records |
|---|---|---|
| W1 · FCCPC lenders (all loaded) | W1 Source = "W1 FCCPC register" | 45 |
| W1 · Lenders to enrich | W1 Source = "W1 FCCPC register" AND Country = Nigeria AND Domain is not empty AND W1 Excluded is false | 24 |
| W1 · Ready for review | W1 Source = "W1 FCCPC register" AND W1 Route = ready_for_review | 21 |
| W1 · Needs research | W1 Source = "W1 FCCPC register" AND W1 Route = needs_research | 1 |
| W1 · Drop: already on Paystack | W1 Source = "W1 FCCPC register" AND W1 Route = drop_paystack | 2 |

The 45 to 24 cut: 19 lenders have no confirmed domain, and 2 are excluded (Branch, Allawee).

## The Workflow

```
Segment: W1 · Lenders to enrich
  > BuiltWith: website technologies      (domain from the record)
  > Classify gateway and pick route      (code, no AI, no credits)
  > Route lender                          (rules)
      ready_for_review  > Write back: Ready for review
      drop_paystack     > Write back: Drop (on Paystack)
      anything else     > Write back: Needs research   (default route)
```

**Why this enrichment:** the payment gateway on a lender's website decides both whether we contact the lender and which angle it gets. That is the routing matrix in the workflow spec (section 5).

**The routing rule** (code saved as [classify-gateway-route.py](classify-gateway-route.py)):

1. BuiltWith returns nothing for the domain: `needs_research` (check the site by hand).
2. Paystack appears anywhere in the result: `drop_paystack` (spec exclusion X1).
3. Flutterwave, Monnify, Interswitch or Remita appears: `ready_for_review`, gateway = competitor. Cell A if the entry type is new, C if backlog.
4. Otherwise: `ready_for_review`, gateway = none_detected. Cell B if new, D if backlog.

The competitor list and Paystack check are the same as the Week 2 Gateway Status formula. One deliberate change: in Week 2 a BuiltWith "no data" result counted as none_detected (cell D). Here it goes to Needs research, because we cannot qualify a lender we know nothing about.

**Status:** published live (version 1, 19 Nov 2026). Any lender that newly enters "W1 · Lenders to enrich" runs through automatically, for example next month's FCCPC approvals once they are loaded. Publishing did not re-run the 24 lenders already done (checked: still 24 runs, no credits used).

## Test results

**Test 1, 10 lenders (draft):** 9 ready (Creditclan and CashRun: Flutterwave, cell C. Seven more in cell D), 1 dropped (Creditville: Paystack on site). 10 credits.

**Run 2, the other 14 lenders (draft, by record ID so nothing ran twice):** this exercised the Needs research branch (Instawave, secucash.vip: BuiltWith had no data, and the credit was refunded) and the second Paystack drop (Nextpayday).

**All 24:**

| S/N | Lender | Domain | Route | Gateway | Cell |
|---|---|---|---|---|---|
| 1 | Creditclan Tech | creditclan.com | Ready for review | Flutterwave | C |
| 20 | Flowood Lending (CashRun) | cashrunapp.com | Ready for review | Flutterwave | C |
| 32 | Provest | provesting.com | Ready for review | Flutterwave | C |
| 2, 3, 6, 9, 13, 14, 16, 18, 22, 25, 26, 28, 35, 37, 40, 41, 43, 44 | 18 lenders | | Ready for review | none detected | D |
| 24 | Instawave Internet Technology | secucash.vip | Needs research | no data | |
| 4 | Nextpayday | nextpayday.co | Drop | Paystack | |
| 38 | Creditville Microfinance Bank | creditville.ng | Drop | Paystack | |

**Check against Week 2:** the same 3 lenders in cell C, the same 2 Paystack drops, and the same lenders in D except secucash.vip (now Needs research, as explained above).

## Cost

| Step | Credits |
|---|---|
| Loader workflow, 45 writes to Audiences | 0 |
| One BuiltWith action test on secucash.vip (no data, refunded) | 0 |
| BuiltWith in the workflow, 24 lenders (23 charged, 1 refunded) | 23 |
| Code, rules and write-backs | 0 |
| **Total** | **23** (balance 30,147.9 to 30,124.9) |

Workflow runs used: loader 45, gateway check 24. Free and trial workspaces may cap each workflow at 100 runs in total.

## Links for the Build Log

- Workflow (enrich and route): https://app.clay.com/workspaces/1431348/terracotta/tc-workflows/wf_0torounJd78qewqch5K
- Workflow (loader): https://app.clay.com/workspaces/1431348/terracotta/tc-workflows/wf_0toroqcwzYkmJY7khRx
- Audience segments: open Audiences > Companies in Clay and copy each segment's link from the browser (the CLI does not return segment URLs). Segment IDs: Lenders to enrich `audseg_0torottZrA2CtCVMv6Y`, Ready for review `audseg_0torotvQvM4TtTb6VJ3`, Needs research `audseg_0torotyBNEUa5ZSjoks`, Drop `audseg_0torou0H2a4gcA7dZug`, all loaded `audseg_0torotrbvc8T3tPmCrP`.
- These links open only for members of the workspace. If faculty cannot open them, use screenshots plus the Loom (same fallback as Week 2).

## Build Log text (paste-ready)

> **Week 2B: Audience segment + Workflow.** Audience: companies on the FCCPC digital lender register (Nigeria) with a verified website, excluding Paystack competitors, customers and Paystack-owned companies. 45 lenders loaded, 24 in the segment "W1 · Lenders to enrich". Enrichment: BuiltWith website technologies, because the payment gateway on the site decides whether and how we approach the lender. Routing rule: Paystack on site = Drop; Flutterwave, Monnify, Interswitch or Remita = Ready for review (cell C); no gateway = Ready for review (cell D); no BuiltWith data = Needs research. Results are written back to each record, and three segments show the destinations. Test: 10 lenders first, then the other 14. Result: 21 Ready for review (3 C, 18 D), 1 Needs research, 2 Drop, matching the Week 2 table. Cost: 23 credits. Workflow published, so new lenders that join the segment are processed automatically. Built from Claude Code with the Clay CLI.
