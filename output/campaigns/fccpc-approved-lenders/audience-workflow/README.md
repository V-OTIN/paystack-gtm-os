# W1 FCCPC approved lenders: Audience segment + Workflow (Week 2B)

Clay workspace: Valentine's Workspace. Audience: Companies (45 W1 lenders). Deliverable: the segment **W1 · Lenders to enrich** connected to the published workflow **W1 · Lender gateway check and routing**.

**Links:** the workflow and segments open only for members of the Clay workspace (free plan, no sharing), so the build is shown through the Loom and screenshots in the Build Log.

## Files

- [build-summary.md](build-summary.md): every step in plain English, plus the result, funnel, cost and lessons
- [loom-script.md](loom-script.md): the 4-minute walkthrough script
- [classify-gateway-route.py](classify-gateway-route.py): the workflow's code step (gateway, route and cell)

## Audience criteria, in one sentence

Companies on the FCCPC digital lender register (Nigeria) with a verified website domain that are not on the W1 exclusion list (competitors, Paystack customers, Paystack-owned).

## Enrichment and routing rule

BuiltWith website technologies (1 credit), then: Paystack on site = Drop; Flutterwave, Monnify, Interswitch or Remita = Ready for review (cell C, or A if new); no gateway = Ready for review (cell D, or B if new); no BuiltWith data = Needs research. Results are written back to each record, and three segments show the destinations.

## Result

45 loaded, 24 in the segment, 21 Ready for review (3 C, 18 D), 1 Needs research, 2 Drop. Matches the Week 2 table. 23 credits.
