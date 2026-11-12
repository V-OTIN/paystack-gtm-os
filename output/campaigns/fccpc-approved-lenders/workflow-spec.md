# W1: FCCPC newly approved digital lenders

**Status:** COPY-APPROVED 2026-11-12 (approved by Valentine for the bootcamp; facts not yet approved by Paystack)

**Workflow:** W1 in [signal-matrix.md](../../../context/icp/signal-matrix.md) (score 17/20). Segment: fintech lending, Tier 1, Nigeria.
**Built from:** [icp.md](../../../context/icp/icp.md), [personas.md](../../../context/icp/personas.md), [signal-matrix.md](../../../context/icp/signal-matrix.md), [gtm-system.md](../../../context/docs/gtm-system.md), [signals.md](../../../context/docs/research/signals.md). Method: `knowledge-base/playbooks/workflow-anatomy.md`.
**Facts:** `context/messaging/facts.md` does not exist yet. Every specific fact in copy stays a `{{placeholder}}` until it is approved there.
**Approvals:** Gate 1 (sections 1 to 3) and Gate 2 (section 4) approved 2026-11-12. Gate 3 (section 5) approved 2026-11-12. Sections 6 and 7 completed on approval of Gate 3; open to change. Section 7 amended 2026-11-12 (3 emails + 2 DMs, all cells).

---

## 1. Mother intent (trigger) [ENGINE]

**A Nigerian lending company appears on the FCCPC "Approvals of DMLs" register that was not on the previous monthly snapshot.**

- Catalog match: Regulatory changes, as a niche-specific play (workflow-anatomy.md).
- First run: all current register entries (526 rows on 2026-11-12 [signals.md]) form the **backlog**. Backlog is a lookalike play, not a timing play. Only names new since the last snapshot are the timing trigger.

## 2. Inclusion / exclusion [ICP]

### Include

| Layer | Rule | Source |
|---|---|---|
| Geography | Nigerian registered company (FCCPC register is Nigerian by definition) | icp.md 1a |
| Industry | Digital lending, Tier 1 fintech | icp.md 1b |
| Size | icp.md 1c working rule; for W1, being an FCCPC-approved lender counts as meeting it (INFERRED) | icp.md 1c; gtm-system.md step 4 |
| Trigger | Row in the "Approval" table; NAME OF COMPANY new vs the last snapshot (or in the backlog run) | signals.md |
| Recipient, first contact | Champion: CTO, Head of Engineering, Lead Developer | personas.md 1 |
| Recipient, second contact | Economic buyer: CEO (founder-led) or finance lead (Head of Finance, CFO, Chief Risk Officer). Staggered after the champion, never in parallel | personas.md 2; gtm-system.md step 6 |

### Exclude

| Who | Why |
|---|---|
| Current Paystack merchants | icp.md 1a. Blocked until the suppression list exists (icp.md Q10). X1 covers part of it |
| Competitors and acquirers with lending licences (e.g. OPay, Moniepoint, Kuda, PalmPay, Paga if listed) | icp.md not-a-fit |
| Named Paystack customers on the register (e.g. Renmoney, Carbon, FairMoney, Aella Credit, Branch if listed) | customers.md: proof, not targets |
| Entries also on the FCCPC watchlist or delisted sections | Regulatory risk (INFERRED). Needs a verbatim read of those sections before launch |
| Rows with no website found after matching | Can't enrich or contact (gtm-system.md step 2) |
| Contacts reached in the last 90 days | gtm-system.md step 6 dedupe window |

## 3. Sources [ENGINE]

| What | Source | Tool |
|---|---|---|
| Trigger | https://fccpc.gov.ng/registration-of-digital-money-lenders/approvals-of-dmls/ (HTML table: S/N, NAME OF COMPANY, NAME OF APP(S), REMARK) [signals.md] | Clay HTTP request + parse column, monthly. Snapshot stored in its own Clay table; new rows found by diff |
| Exclusion lists | Same page: watchlist and delisted sections | Same scrape, separate Clay table (iron law 4) |
| Company website | URL inside NAME OF APP(S) when present; otherwise Claygent: official website of {company} {app} Nigeria | Clay formula (URL regex) → Claygent fallback |
| Company enrichment | Domain → LinkedIn company page, headcount, founded year | Clay Enrich Company |
| Gateway on website | BuiltWith: Paystack, Flutterwave, Monnify, Interswitch, Remita scripts | Clay Find Technology Stack |
| Hiring | Open jobs at the company | Clay Find Jobs at Company |
| Funding | Crunchbase | Clay Find Organization |
| People | Champion and economic buyer titles | Clay Find People |
| Emails | Waterfall + verification | Clay; providers DECISION PENDING (gtm-system.md step 7) |
| Suppression | Paystack merchant list (pending); HubSpot contacted list | Clay lookup table |

App-store presence (signal-matrix U7) is not used: data source unverified.

## 4. Signals table [ENGINE]

| # | Signal | Role | How it's read | Output |
|---|---|---|---|---|
| S1 | Listed on the FCCPC "Approval" table | trigger | Boolean: NAME OF COMPANY present in the current scrape | `on_register` = true |
| S2 | New since last snapshot | router | Boolean: normalised NAME OF COMPANY (uppercase; "LIMITED", "LTD", "LIMIT" stripped) not in the previous month's snapshot | `entry_type` = `new` / `backlog` |
| S3 | Payment gateway on website | router | BuiltWith script match on `company_domain`. Enum: `paystack` if any Paystack script; else `competitor` if Flutterwave, Monnify, Interswitch or Remita; else `none_detected` | `gateway_status`, `competitor_name` |
| S4 | Number of apps listed | context-clause | Count of app names in NAME OF APP(S), split on "," and " AND ". Clusters: 1 = `single`; 2+ = `multi` | `app_count_cluster` |
| S5 | Hiring payments or engineering roles | context-clause | Count of open jobs with title keywords: payment, payments, backend, engineer, collections, recovery, finance. Clusters: 0 = `not_hiring`; 1+ = `hiring` | `hiring_cluster`, `role_title` (first match) |
| S6 | Funded in last 12 months | context-clause | Boolean: Crunchbase last round date within 365 days | `recently_funded`, `round_type` |

### Exclusion reads (remove the row; never route or reach copy)

| # | Read | Rule |
|---|---|---|
| X1 | S3 = `paystack` | Probable existing merchant. Exclude until the suppression list confirms (INFERRED) |
| X2 | On FCCPC watchlist or delisted sections | Exclude |
| X3 | On competitor list or Paystack named-customer list | Exclude |
| X4 | No `company_domain` after regex and Claygent | Exclude |

### Build fields (plumbing, not copy)
`company_domain` (URL regex on the app cell, else Claygent), `app_names_raw` (raw NAME OF APP(S) cell), `company_name_normalised` (for the diff).

### Why only two routers
S5 and S6 are colour, not routers: funding is rare (15 disclosed Nigerian deals in Q1 2026 [signals.md]) and hiring coverage for Nigerian lenders is unmeasured. S4 does not change what Paystack sells. S3 = `none_detected` is ambiguous: lenders are app-first and BuiltWith reads websites only, so it never means "no gateway".

## 5. Routing matrix with angles [ENGINE]

Axis 1, `entry_type`: 2 values (`new`, `backlog`). Axis 2, `gateway_status` after X1: 2 values (`competitor`, `none_detected`). Stacked: 2 x 2 = **4 cells**.

| Cell | Deterministic read | What it tells us (inferred situation) | The angle it earns |
|---|---|---|---|
| **A** | `entry_type` = new AND `gateway_status` = competitor | The lender has just been added to the FCCPC approved list and already takes web payments through `{{competitor_name}}`. It is operating, now on a formal footing with the regulator, and its payment stack was chosen before approval. INFERRED: approval is a moment when a lender reviews the vendors it will scale with | **Post-approval stack review.** A newly approved lender moves money both ways: repayments in, loans out. Paystack covers both on one integration (collections, a virtual account per borrower, direct debit, transfers for disbursement), next to what `{{competitor_name}}` does on the web today. The ask is a comparison, not a rip-and-replace |
| **B** | `entry_type` = new AND `gateway_status` = none_detected | Newly approved, no gateway visible on the website. A digital lender with nothing on its site most likely runs lending inside its app, so its stack is invisible to us. We do not know whether it has a gateway | **Repayments and disbursement inside the app, set up for scale after approval.** Lead with borrower-level collection (dedicated virtual account per borrower, direct debit) and instant disbursement, plus BVN and account lookup at onboarding. Framed as how approved lenders run the loan loop in-app, never as "you have no gateway" |
| **C** | `entry_type` = backlog AND `gateway_status` = competitor | An established, approved lender with `{{competitor_name}}` on its site. No timing event: it has operated under approval for a while with a settled gateway | **Collections performance, lender to lender.** Lead with what Nigerian lenders measure: loan collections and reconciling what borrowers paid against the bank. Proof from lenders already on Paystack via `{{proof_point}}`. Displacement through peer comparison, not a feature list |
| **D** | `entry_type` = backlog AND `gateway_status` = none_detected | An established, approved, app-first lender with an unknown stack and no timing event. The weakest cell: neither timing nor stack is known | **Peer pattern, low pressure.** How lenders like `{{proof_customer}}` run repayments and disbursement on Paystack, with KYC at onboarding as the second hook. Readiness: Warm (icp.md Layer 5), lighter sequence |

**Readiness by cell** (icp.md Layer 5): A and B = Ready now. C and D = Warm. (Sequence length is the same for all cells since the 2026-11-12 cadence amendment; readiness now affects send priority only.)

**Recipient lens** (not an axis): the champion gets the integration side of each angle (one API, webhooks, virtual accounts, BVN lookup). The economic buyer, staggered after, gets the money side (collections rate, reconciliation, disbursement speed).

**Niche-native check:** every angle depends on two things only this workflow has: being on the FCCPC lender register, and a lender's two-way money loop. A and B also depend on approval timing.

**Inference stops at what they are doing:** operating, newly approved, app-first, on a given gateway. No angle claims a pain they have not shown.

### Branch coverage

| Variable | A | B | C | D | Rule |
|---|---|---|---|---|---|
| `{{competitor_name}}` | yes | no | yes | no | Only where S3 = competitor |
| `{{company_name}}`, `{{app_name}}` | yes | yes | yes | yes | From the register row |
| `{{app_names}}` | if multi | if multi | if multi | if multi | Only when `app_count_cluster` = multi |
| `{{role_title}}` | if hiring | if hiring | if hiring | if hiring | Clause dropped when `hiring_cluster` = not_hiring |
| `{{round_type}}` | if funded | if funded | if funded | if funded | Clause dropped when `recently_funded` = false |
| `{{proof_point}}`, `{{proof_customer}}` | yes | yes | yes | yes | Placeholder until facts.md approves them. Candidates in research: Renmoney loan-collections quote, Farmcrowdy reconciliation quote [customers.md] |

## 6. Variables contract [ENGINE]

| Variable | Source field | Exists in branches |
|---|---|---|
| `{{first_name}}` | Clay Find People: first name | All |
| `{{persona}}` | Workflow assignment: `champion` / `economic_buyer` | All |
| `{{company_name}}` | Register NAME OF COMPANY, cleaned (title case; "Limited", "Ltd", "Limit" removed) | All |
| `{{app_name}}` | First app in NAME OF APP(S); falls back to `{{company_name}}` when the cell is empty | All |
| `{{app_names}}` | All apps in NAME OF APP(S), joined with "and" | All, only when `app_count_cluster` = multi |
| `{{entry_type}}` | S2 | All (routing only; copy references approval timing in A and B, never the word "backlog") |
| `{{competitor_name}}` | S3 BuiltWith match: Flutterwave / Monnify / Interswitch / Remita | A, C |
| `{{role_title}}` | S5 first matching job title | All, only when `hiring_cluster` = hiring |
| `{{round_type}}` | S6 Crunchbase last round type | All, only when `recently_funded` = true |
| `{{proof_point}}` | `context/messaging/facts.md` (to be created) | All |
| `{{proof_customer}}` | `context/messaging/facts.md` (to be created) | All |

Not available to copy: `company_domain`, `app_names_raw`, `company_name_normalised`, raw job counts, BuiltWith raw output.

## 7. Cadence and channel [ENGINE]

| | |
|---|---|
| **Periodicity** | Backlog: one-shot, run in batches (iron law 7: 10 rows first). New entries: monthly register diff (FCCPC update cadence not found [signals.md]; revisit after 3 runs) |
| **Channel** | Both: email + LinkedIn (gtm-system.md step 8). Sequencer and LinkedIn tool: DECISION PENDING |
| **All cells (A to D)** | Amended 2026-11-12 (approved by Valentine): 3 emails + 2 LinkedIn DMs for every cell. Day 1 email 1, day 2 LinkedIn connection request (no note), day 4 email 2, day 5 DM 1 if connected, day 9 email 3, day 10 DM 2 if connected (timings INFERRED) |
| **Signature** | `{{sender_name}}`, `{{sender_title}}`: sequencer built-ins, resolved per inbox [facts.md] |
| **Second persona** | Economic buyer enters 7 days after the champion's last step if no reply (INFERRED). Max 2 contacts per account (iron law 14) |
| **Stop rules** | Any reply stops both channels (gtm-system.md step 9). Bounce marks the email invalid |

---

## Definition of done

- [x] Mother intent: one sentence, signal-led, matched to the catalog
- [x] Inclusion: ICP box + trigger definition + recipient, tagged [ICP]
- [x] Exclusion: who's out and why
- [x] Sources: trigger + every enrichment
- [x] Signals table: every read deterministic, every role declared
- [x] Count clusters declared for counts (S4, S5; neither routes)
- [x] Routing matrix with the angle column complete
- [x] Branch coverage: every cell's angle survives on its own data
- [x] Variables contract: every variable mapped to its source field
- [x] Engine/ICP markers on every section
- [x] Cadence and channel declared

## Before launch (not blocking copy)

1. Suppression list of current Paystack merchants (icp.md Q10).
2. Verbatim read of the FCCPC watchlist and delisted sections (X2).
3. Approved facts in `context/messaging/facts.md` for `{{proof_point}}` and `{{proof_customer}}`.
4. Sequencer, LinkedIn tool and email providers chosen (gtm-system.md open decisions 2 to 4).
5. Legal check on cold outreach under Nigerian data protection rules (gtm-system.md open decision 6).

## Next

`/campaign-copy` reads this file (GATE 1 checks the status and checklist), reads the angles back, and writes copy per cell. Copy is appended here and the status line advances.

---

## Copy

Facts from `context/messaging/facts.md` only (approved by Valentine for the bootcamp, not by Paystack). Variables from section 6 only. Kit syntax: `{{variable}}`, `{spintax}`.

### Email 1 (approved 2026-11-12)

**Subject (same across the thread):** {repayments in, loans out|lender payments question|repayments and disbursement}

**Line map**

```
{{first_name}},

{{e1l1}}
{{e1l2}}

{{e1l3}}
Renmoney's Chief Risk Officer has said their loan collections went up significantly on Paystack.

{{e1cta}}

{Best|Thanks|Cheers},
{{sender_name}}
```

**{{e1l1}}: mother intent** (exhaustive by `entry_type`)
- + entry_type = new (cells A, B): {{app_name}} was recently added to the FCCPC's list of approved digital lenders, so I'm guessing lending is about to pick up.
- + entry_type = backlog (cells C, D): {{app_name}} is on the FCCPC's list of approved digital lenders, so I'm guessing a lot of money moves through it every day, in both directions.

**{{e1l2}}: their setup** (exhaustive by `gateway_status`)
- + gateway_status = competitor (A, C): Your website uses {{competitor_name}} for payments.
- + gateway_status = none_detected (B, D): I couldn't tell from your website who handles payments, so I'm guessing it all runs inside the app.

**{{e1l3}}: value prop** (locked lead-in; tail exhaustive by `persona`)
- + persona = champion: Paystack lets lenders collect repayments and send out loans on one integration, with webhooks confirming each payment.
- + persona = economic_buyer: Paystack lets lenders collect repayments and send out loans on one integration, and the money lands in your bank before 10 AM every morning.

**Proof (static):** Renmoney's Chief Risk Officer has said their loan collections went up significantly on Paystack.

**{{e1cta}}** (exhaustive by `gateway_status`)
- + gateway_status = competitor: Would a side-by-side with {{competitor_name}} help, or is that already sorted?
- + gateway_status = none_detected: Is that right, or do payments run somewhere else?

**Sample as received (cell A, champion):**

> Subject: repayments in, loans out
>
> {{first_name}},
>
> {{app_name}} was recently added to the FCCPC's list of approved digital lenders, so I'm guessing lending is about to pick up.
> Your website uses {{competitor_name}} for payments.
>
> Paystack lets lenders collect repayments and send out loans on one integration, with webhooks confirming each payment.
> Renmoney's Chief Risk Officer has said their loan collections went up significantly on Paystack.
>
> Would a side-by-side with {{competitor_name}} help, or is that already sorted?
>
> Best,
> {{sender_name}}

### Email 2 (approved 2026-11-12)

**Subject:** Re: (same thread, unchanged). Day 4.

**Line map**

```
{{first_name}},

{{e2l1}}

Each borrower can get a dedicated virtual account for repayments, direct debit covers scheduled ones, and loans go out by instant transfer.
Paystack also checks BVN and bank account details at signup, through the same integration.
Renmoney says it can onboard customers online much faster than before.

{Want me to map how that would work for {{app_name}}?|Should I sketch how that would run for {{app_name}}?}

{Best|Thanks|Cheers},
{{sender_name}}
```

**{{e2l1}}: context waterfall** (priority order, first match wins)
- + hiring_cluster = hiring: You're also hiring a {{role_title}}, so I'd guess the payments side of {{app_name}} is getting more attention.
- + app_count_cluster = multi: With {{app_names}} to run, my guess is there's more than one repayment flow to keep in step.
- + recently_funded = true: After your {{round_type}} round, I'd imagine loan volume is set to grow.
- FALLBACK: Matching every repayment to the right borrower is usually where lending gets fiddly.

**Sample as received (hiring route, cell A, champion):**

> Subject: Re: repayments in, loans out
>
> {{first_name}},
>
> You're also hiring a {{role_title}}, so I'd guess the payments side of {{app_name}} is getting more attention.
>
> Each borrower can get a dedicated virtual account for repayments, direct debit covers scheduled ones, and loans go out by instant transfer.
> Paystack also checks BVN and bank account details at signup, through the same integration.
> Renmoney says it can onboard customers online much faster than before.
>
> Want me to map how that would work for {{app_name}}?
>
> Best,
> {{sender_name}}

### Email 3 (approved 2026-11-12)

**Subject:** Re: (same thread, unchanged). Day 9. Static.

```
{{first_name}},

{Last note from me on this.|I'll leave it here after this one.}

{For context,|In case it helps,} Paystack is a Stripe company, live in Nigeria, Ghana, Kenya, South Africa and Côte d'Ivoire.

{If payments sit with someone else at {{company_name}}, who should I speak to?|Is someone else the right person for payments at {{company_name}}?}

{Best|Thanks|Cheers},
{{sender_name}}
```

**Sample as received:**

> Subject: Re: repayments in, loans out
>
> {{first_name}},
>
> Last note from me on this.
>
> For context, Paystack is a Stripe company, live in Nigeria, Ghana, Kenya, South Africa and Côte d'Ivoire.
>
> If payments sit with someone else at {{company_name}}, who should I speak to?
>
> Best,
> {{sender_name}}

### LinkedIn (approved 2026-11-12)

**Day 2: connection request:** empty, no note.

**Day 5: DM 1** (if connected; exhaustive by `entry_type`)

```
{{first_name}},
{{dm1}}
```

- + entry_type = new (cells A, B): any plans to scale lending now that {{app_name}} is on the FCCPC's approved list?
- + entry_type = backlog (cells C, D): are repayments at {{app_name}} mostly collected by bank transfer or by direct debit?

**Day 10: DM 2** (static)

```
{Asking because|Only asking since} Paystack runs both sides for lenders on one integration: virtual accounts and direct debit for repayments, instant transfers for loans.
{Happy to show how that would look for {{app_name}}.|Can send a short outline for {{app_name}} if useful.}
```

**Samples as received:**

> DM 1 (new): {{first_name}}, any plans to scale lending now that {{app_name}} is on the FCCPC's approved list?
>
> DM 2: Asking because Paystack runs both sides for lenders on one integration: virtual accounts and direct debit for repayments, instant transfers for loans.
> Happy to show how that would look for {{app_name}}.

### Before launch

Run a final manual read against `knowledge-base/playbooks/copy-iron-laws.md`, get Paystack to approve every fact in `context/messaging/facts.md`, and clear the five before-launch items above.
