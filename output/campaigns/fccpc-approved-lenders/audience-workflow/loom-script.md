# Loom script: Week 2B Audience + Workflow (W1 FCCPC approved lenders)

About 4 minutes, one take. Words in **[brackets]** are what to show on screen. Read the rest out loud.

---

## 1. Intro (20 seconds)

**[Clay, Audiences > Companies, segment "W1 · FCCPC lenders (all loaded)"]**

Hi, I'm Valentine. This is my Week 2B build for Paystack: one Audience segment connected to a Workflow that enriches and routes the records.

It builds on my Week 2 table. The list is the FCCPC register of approved digital lenders in Nigeria, and the approval is the signal.

## 2. The audience (40 seconds)

**[Scroll the 45 lenders. Open one record, e.g. Creditclan Tech, and show the FCCPC and W1 fields]**

I loaded 45 lenders from my Week 2 Lenders table into the Companies audience. Each record carries its FCCPC register details, its verified website, and whether it is on my exclusion list.

Tables were for testing. Audiences is where the play runs over and over, on a single record per company that every workflow writes back to.

## 3. The segment (40 seconds)

**[Open "W1 · Lenders to enrich" and show its filter]**

My segment, in one sentence: FCCPC lenders in Nigeria with a verified website domain that are not excluded.

The exclusion list is competitors, Paystack customers and companies Paystack owns. It drops two lenders here: Branch, which is a Paystack customer, and Allawee, which Paystack owns. Nineteen more have no website yet. That leaves 24 lenders.

It's a dynamic filter, so any new lender that meets these rules joins the segment on its own.

## 4. The workflow (60 seconds)

**[Open the workflow "W1 · Lender gateway check and routing" on the canvas]**

The trigger is the segment. For each lender it does three things.

**[Point at BuiltWith]** First, one enrichment. BuiltWith reads the technologies on the lender's website. I chose it because the payment gateway decides both whether we contact the lender and which message it gets. It costs one credit.

**[Point at the code step]** Second, a code step turns that into a gateway status. Paystack on the site means drop. Flutterwave, Monnify, Interswitch or Remita means a competitor, cell C. No gateway means cell D. No data at all means needs research. This step uses no AI and costs nothing.

**[Point at Route lender and the three write-backs]** Third, a rules step sends the lender down one of three branches, and each branch writes the result back to the lender's record in Audiences.

## 5. The result (50 seconds)

**[Open "W1 · Ready for review", then "Needs research", then "Drop: already on Paystack"]**

The destinations are three more segments that read the route field.

I tested 10 lenders first, checked them, then ran the other 14. Ready for review has 21: three on Flutterwave and 18 with no gateway visible. Needs research has one, Secucash, where BuiltWith had no data. Drop has two, Nextpayday and Creditville, which already use Paystack.

**[Open Creditclan's record and show W1 Route, W1 Cell, W1 Route Reason]**

That matches my Week 2 table, lender for lender. The whole run cost 23 credits.

## 6. Close (20 seconds)

**[Back to the workflow, show it is published]**

The workflow is published. When I load next month's FCCPC approvals, any that join the segment get checked and routed automatically. I built all of this from Claude Code using the Clay CLI, then checked it here in Clay. Thanks.
