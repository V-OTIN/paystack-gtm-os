# W1 FCCPC approved lenders: Clay build (Week 2)

Clay workbook: "V1: Paystack · W1 FCCPC Approved Lenders" (folder "WF 1- New Digital Lenders", Valentine's Workspace). Tables: Exclusions, Lenders, Contacts. Auto-run off on all three.

**Table link:** Clay sharing is not available on the free plan (the trial ended during the build), so the table is shown through screenshots and a Loom, both linked in the Build Log. They are kept out of this repo because they show contact names and emails.

## Files

- [fccpc-approved-lenders-clay-build-guide.md](fccpc-approved-lenders-clay-build-guide.md): the build plan, with the flow diagram ([.png](fccpc-approved-lenders-clay-flow.png))
- [build-summary.md](build-summary.md): every step in plain English, plus the funnel, costs and lessons
- [loom-script.md](loom-script.md): the 5-minute walkthrough script
- [exclusions.csv](exclusions.csv): the Exclusions import (competitors, named Paystack customers, Paystack-owned)

## Funnel

526 FCCPC register rows imported, 45 in the test batch, 24 pass the company gates, 22 ready lenders (cell C: 3, cell D: 19), 21 people found at 10 lenders, 12 Ready to Contact, 10 emails found (2 not found), 8 Send Ready (2 held for a domain mismatch).

## Cost

52.1 Clay credits in total: Claygent 7.3, BuiltWith 23, Enrich company 7, Work Email waterfall 14.8. Formulas, lookups and searches were free.

## Notes

- The list is an import of the FCCPC register, not a Clay search: the register is the signal's source of truth.
- The email waterfall ran only on the 12 contacts that passed Ready to Contact?, as the brief asks.
- Crunchbase (guide Part 7.2) and job posts (Part 8) were deferred: they only feed an optional line in Email 2.
