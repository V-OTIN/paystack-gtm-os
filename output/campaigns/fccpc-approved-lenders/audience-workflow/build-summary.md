# What we built in Clay for Week 2B, in plain English (W1 FCCPC approved lenders)

Built 19 Nov 2026 for the Week 2B brief: one Audience segment connected to a Workflow that enriches and routes the records. Built from Claude Code with the Clay CLI, then checked in Clay. Workspace: Valentine's Workspace.

## The idea

In Week 2 we tested the play in a Clay table: FCCPC-approved digital lenders, checked for a website and a payment gateway. Tables are for testing. Week 2B moves the same play into Audiences, where it can run again and again: one record per lender, one segment that picks the right lenders, and one workflow that checks each lender and writes the answer back to its record.

Sandra's framework for this is SEA: **Segment** your audience, **Enrich** it, then **Act** on it.

## What's where in Clay

| Thing | Name in Clay | Where to find it |
|---|---|---|
| The audience | 45 lenders in Companies | Sidebar: building icon (Companies) |
| The segment the workflow runs on | **W1 · Lenders to enrich** (24 lenders) | Companies, segment list |
| The workflow | **W1 · Lender gateway check and routing** (published) | Sidebar: Workflows |
| The destinations | W1 · Ready for review (21), W1 · Needs research (1), W1 · Drop: already on Paystack (2) | Companies, segment list |
| Helpers | W1 · FCCPC lenders (all loaded) segment (45); W1 · Load FCCPC lenders to Audiences workflow | Companies; Workflows |

The segment and workflow in bold are the deliverable. The rest supports them.

## Step by step

1. **Added fields to Companies.** Audiences starts with basic fields (company name, domain, country). We added fields for what the FCCPC register tells us (S/N, register name, app names, entry type, snapshot month), what Week 2 found (website confidence, excluded or not, and why), and what the workflow will write back (gateway status, gateway name, route, cell, route reason).
2. **Loaded the lenders.** A small workflow, "W1 · Load FCCPC lenders to Audiences", took the 45 batch lenders from the Week 2 Lenders table as a CSV and wrote one Audiences record per lender. Each record is matched on its FCCPC number (`fccpc-<S/N>`), so loading again updates the same record instead of making a copy. Clay also matched all 45 to its own company data (LinkedIn page, logo). Cost: 0 credits.
3. **Made the segment.** "W1 · Lenders to enrich" is a saved filter: register lenders, in Nigeria, with a website domain, and not excluded. 24 of the 45 match. It drops Branch International (a Paystack customer) and Allawee (owned by Paystack), plus 19 lenders with no confirmed website, because the next step needs a website to check. Because it's a filter rather than a fixed list, any new lender that meets the rules joins on its own.
4. **Chose one enrichment.** BuiltWith reads the technologies on each lender's website. We chose it because the payment gateway decides two things at once: whether we contact the lender at all (not if it already uses Paystack), and which message it gets (the cells in the workflow spec's routing matrix). It costs 1 credit per lender.
5. **Built the workflow.** "W1 · Lender gateway check and routing" starts from the segment. For each lender:
   - **BuiltWith** reads the website's technologies, using the domain on the record.
   - **A code step** turns the list into a decision. No AI, no credits. It uses the same rules as the Week 2 Gateway Status column.
   - **A rules step** sends the lender down one of three branches.
   - **Each branch writes back** the gateway, route, cell and a one-line reason to the lender's own record (matched on its Audiences record ID, so it can't land on the wrong lender).
6. **The routing rule.**
   - Paystack on the site: **Drop** (spec exclusion X1).
   - Flutterwave, Monnify, Interswitch or Remita on the site: **Ready for review**, cell C (cell A for a newly approved lender).
   - No gateway visible: **Ready for review**, cell D (cell B if new).
   - BuiltWith has no data for the domain: **Needs research**. Someone checks the site by hand.
7. **Made the destinations visible.** Three more segments filter on the route field: Ready for review, Needs research, and Drop. They fill as the workflow writes back.
8. **Tested small first.** We ran the draft on 10 lenders (10 credits) and checked every result against Week 2. Then we ran it on the other 14, choosing them by record ID so nobody was charged twice.
9. **Published it.** The workflow is live. When next month's FCCPC approvals are loaded, any new lender that joins the segment is checked and routed automatically. Publishing didn't re-run the 24 already done.

## The result

| Route | Lenders | Who |
|---|---|---|
| Ready for review, cell C (competitor) | 3 | Creditclan, CashRun (Flowood Lending), Provest: all on Flutterwave |
| Ready for review, cell D (no gateway visible) | 18 | Acetech, Letshego, Kobogo, MyCashier (Fast Point), 9moni (OTP), Swiftkash (Altracred), MenaCred, CSENSE, Trivista, Nmoney (Finnew), Umba, Sycamore, Dot MFB, Oxymon, P2Vest, Yescredit, KKCash (Hollandale), Koins (Primera) |
| Needs research | 1 | Instawave (secucash.vip): BuiltWith had no data, and the credit was refunded |
| Drop: already on Paystack | 2 | Nextpayday, Creditville |

This matches the Week 2 table lender for lender. The one change is deliberate: in Week 2, a lender BuiltWith knew nothing about counted as "no gateway" (cell D). Now it goes to Needs research, because we can't qualify a lender we know nothing about.

## Funnel

45 lenders loaded, 24 in the segment, 24 enriched, 21 ready for review (3 in cell C, 18 in cell D), 1 needs research, 2 dropped.

## Cost

23 credits in total (balance 30,147.9 to 30,124.9): BuiltWith on 24 lenders, with 1 refunded. Loading, code, rules and write-backs were free. Workflow runs used: 45 for the loader and 24 for the gateway check. Free and trial workspaces may cap each workflow at 100 runs.

## Lessons

- **Tables test, Audiences run.** The logic came from Week 2's table unchanged. Audiences adds one record per lender that every workflow can write back to.
- **Write results back as fields, then segment on them.** The route field makes the destinations visible and reusable for the next step (HubSpot in Week 3, sending later).
- **Test 10, check, then run the rest by record ID.** Running the full segment again would have charged the first 10 twice.
- **A "no data" result needs its own branch.** Without it, a lender we know nothing about looks like one with no gateway.

## Links

- Workflow: https://app.clay.com/workspaces/1431348/terracotta/tc-workflows/wf_0torounJd78qewqch5K (opens for workspace members only)
- Routing code: [classify-gateway-route.py](classify-gateway-route.py)
- Loom script: [loom-script.md](loom-script.md)
