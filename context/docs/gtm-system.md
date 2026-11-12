# Paystack outbound GTM system

**Status:** design v1, 2026-11-12. Work in progress; validate with Paystack sales.
**Diagram:** [Paystack GTM System on Miro](https://miro.com/app/board/uXjVEOwCk1Y=/) (flowchart of the 12 steps below; spec in `diagrams/paystack-gtm-system.json`, rebuild with the miro-gtm-flowchart skill).
**Built from:** [icp.md](../icp/icp.md), [personas.md](../icp/personas.md), [signal-matrix.md](../icp/signal-matrix.md) and the kit playbooks in `knowledge-base/playbooks/` (workflow-anatomy, signal-matrix-framework, clay/iron-laws, copy-frameworks, linkedin-dm-frameworks).
**Scope:** Nigeria, mid-market and enterprise, Tier 1 and 2 verticals. Fintech is the primary segment, betting secondary [signal-matrix.md].
**Tool status:** tools named in CLAUDE.md are decided (Claude Code, GitHub, Clay from Week 2, HubSpot from Week 3, n8n from Week 4). Tools marked **DECISION PENDING** are kit examples, not choices yet.
**INFERRED** = design choice or assumption not backed by `context/docs/research/`.

---

## The flow at a glance

```
 [0] Context OS (GitHub) ──────────────────────────────────────────────┐
      icp.md · personas.md · signal-matrix.md · research                │
        │                                                               │
        ▼                                                               │
 [1] Buying signals ──► [2] Find companies ──► [3] Enrich accounts      │
     (registry diffs,       (signal-first;         (Clay, account       │
      jobs, funding)         domain match)          table)              │
                                                       │                │
                                                       ▼                │
                    [5] Route by segment ◄── [4] ICP fit check          │
                     (Matrix 1 cell,           pass / fail / unknown    │
                      product, displacement?)                           │
                            │                                           │
                            ▼                                           │
 [6] Find people ──► [7] Find + verify emails ──► [8] Sequence          │
     (persona per        (waterfall, verify,          (email +          │
      segment)            catch-all rule)              LinkedIn)        │
                                                         │              │
                                                         ▼              │
                         [10] CRM (HubSpot) ◄── [9] Reply handling      │
                                │                                       │
                                ▼                                       │
                     [11] Weekly feedback loop ─────────────────────────┘
                      (learnings → ICP, signals, copy)
```

---

## Step 0: Context OS

| | |
|---|---|
| **What happens** | Every downstream step reads its rules from this repo: who to target (icp.md), who to talk to (personas.md), which signals to run (signal-matrix.md), what is true (research). Nothing is targeted or written that these files do not support |
| **Tool** | GitHub (source of truth), Claude Code (maintains it), Notion (publishes finished docs) [CLAUDE.md] |

| Decision | Answer leads to |
|---|---|
| Is the claim in a research file with a source? | Yes: usable in targeting and copy. No: not used; add to open questions |
| Is it a number Paystack states inconsistently (200K vs 300K businesses; 50% vs 20% share)? | Yes: banned from copy until confirmed [icp.md open questions 6, 7]. No: usable with source |
| Do `context/messaging/` and `context/brand-kit/` exist? | Not yet: **gap**. Build an approved-facts list before any copy (step 8 depends on it) |

---

## Step 1: Buying signals

| | |
|---|---|
| **What happens** | Scheduled jobs detect the timing events from Matrix 2 and output company names with a signal date and signal type. The signal comes first, ICP filter second (signal-matrix-framework guardrail) |
| **Tool** | Clay (HTTP scrapes, Find Jobs, Find Organization, Company Headcount, BuiltWith). Schedules move to n8n in Week 4. Until then, runs are manual (INFERRED) |

Signals live in v1 (top 5 from [signal-matrix.md]):

| W # | Signal | Source | Run cadence |
|---|---|---|---|
| W1 | Newly approved on the FCCPC digital lenders register | fccpc.gov.ng, Clay HTTP, diff vs last snapshot | Monthly (INFERRED; real update cadence not found) |
| W2 | Nigerian companies hiring in GH, KE, ZA, CI | Clay Find Jobs, location filter | Weekly (workflow-anatomy periodicity: job posts) |
| W3 | Payments / finance-ops hiring naming a competitor | Clay Find Jobs, keyword filter | Weekly |
| W4 | New operator on NLRC or LSLGA licensed list | Clay HTTP, diff | Monthly (INFERRED) |
| W5 | Funded in last 90 days + competitor gateway | Crunchbase via Clay + BuiltWith | Bi-weekly (periodicity: funding) |

| Decision | Answer leads to |
|---|---|
| Is the signal new since the last run (diff)? | Yes: pass to step 2. No: drop (already processed) |
| Did the registry scrape return a parseable list? | Yes: continue. No (page changed or blocked): alert in Slack/email via n8n, pause that workflow, fix the scraper (INFERRED) |
| Is the signal older than its window (90 days funding; 30 days jobs)? | Yes: drop. No: continue |
| Is it a compound-only signal (BuiltWith)? | Yes: only enriches accounts already found by another signal; never starts a workflow [signal-matrix.md U4] |

---

## Step 2: Find companies

| | |
|---|---|
| **What happens** | Turn each signal row into one company record with a website domain and LinkedIn company URL. One table per source, then one consolidated accounts table (Clay iron laws 4, 5) |
| **Tool** | Clay: Find Company / Enrich Company; Claygent to find the website when the signal gives only a brand or app name |

| Decision | Answer leads to |
|---|---|
| Does the signal give a domain? | Yes: enrich directly. No: Claygent finds the website from name + "Nigeria" (one task per run, iron law 11) |
| Domain found with confidence? | Yes: continue. No: manual review queue (cap the queue; if it grows, the signal source is poor) |
| Already in the consolidated accounts table? | Yes: add the new signal to the existing record (signal stacking), do not duplicate (iron law 13). No: create record |
| Brand is an app owned by a different legal entity (common for loan apps, INFERRED)? | Yes: map app to parent company and domain before enrichment. No: continue |

---

## Step 3: Enrichment (accounts)

| | |
|---|---|
| **What happens** | Add the fields the fit check and routing need, on accounts first, contacts later (iron law 5): industry, headcount, HQ country, funding, website checkout and gateway (BuiltWith), app presence, job posts, Nigerian registration |
| **Tool** | Clay enrichments; BYOK keys before Clay credits (iron law 9); batches of 10 before full runs (iron law 7) |

| Decision | Answer leads to |
|---|---|
| Data already in another table? | Yes: lookup, do not re-enrich (iron law 10). No: run enrichment |
| Enrichment returns empty for a Nigerian firm (coverage risk, INFERRED)? | Fall back to Claygent website read for the missing field. Still empty: mark "unknown" (fit check handles it) |
| Cost per row above budget after the 10-row test? | Yes: drop or replace the enrichment, re-test. No: run on the full table. Check with /calculate-costs |

---

## Step 4: ICP fit check

| | |
|---|---|
| **What happens** | Apply icp.md 1a hard filters, 1b tiers, 1c size rule and the not-a-fit list. Every row ends as Pass, Fail (with reason) or Unknown |
| **Tool** | Clay formula columns and conditional runs (iron law 12); suppression list lookup |

| Gate (in order) | Pass | Fail | Unknown |
|---|---|---|---|
| Registered business in Nigeria [icp.md 1a] | Next gate | Disqualify: "not Nigeria" | Claygent check of website / CAC mention (INFERRED) |
| Not a current Paystack merchant [icp.md 1a] | Next gate | Disqualify; send to account management list (INFERRED) | **Blocked until the suppression list exists** [icp.md open question 10] |
| Not a competitor or acquirer [icp.md not-a-fit] | Next gate | Disqualify: "competitor" | Manual check |
| Takes payments digitally [icp.md 1a, Layer 2 row 1] | Next gate | Disqualify: "no digital payments" (Not yet tier) | Claygent: does the site or app show checkout? |
| Tier 1 or 2 vertical [icp.md 1b] | Next gate | Disqualify: "Tier 3" | Claygent classify vertical |
| Size working rule: named enterprise, venture-funded, or high-frequency digital payments [icp.md 1c] | **Pass** | Disqualify: "below size" | Keep if signal is W1 or W4 (licensed entities, INFERRED); else drop |

Every disqualify reason is stored, because the weekly loop reads it (step 11).

---

## Step 5: Routing by segment

| | |
|---|---|
| **What happens** | Each passing account gets: segment, the Matrix 1 angle row, lead product, displacement or greenfield path, and a readiness tier |
| **Tool** | Clay formula columns; routing matrix defined per workflow in `/build-workflow-spec` |

| Decision | Answer leads to |
|---|---|
| Which segment? | Fintech / Betting / Education / Corporates and government / Mobility: picks the angle row in Matrix 1 [signal-matrix.md 1a] |
| Segment = Corporates and government? | Yes: route out of signal-led outbound to an account-based list for Paystack sales [signal-matrix.md 1c]. No: continue |
| Segment = Betting? | Yes: hold for copy until betting regulation is researched [icp.md open question 13]. No: continue |
| Competitor gateway detected (U4)? | Yes: displacement copy path. No: greenfield path |
| Which product angle (icp.md Layer 2 rows 2 to 6)? | Recurring billing → Subscriptions; payouts → Transfers; split revenue → Subaccounts; KYC → Identity; per-customer transfers → Dedicated Virtual Accounts. None detected: lead with collections/checkout [signal-matrix.md 1b] |
| Readiness tier [icp.md Layer 5]? | Ready now: full sequence. Warm: lighter sequence or nurture (INFERRED). Not yet: no outreach |

---

## Step 6: Find people

| | |
|---|---|
| **What happens** | Find the personas for each account from personas.md: Champion (technical lead), Economic buyer (finance lead; CEO at founder-led firms), Influencer (digital, product, growth, ops) |
| **Tool** | Clay Find People (title filters per persona) on the contacts table, looked up from accounts (iron law 5) |

| Decision | Answer leads to |
|---|---|
| Company size / founder-led? | Founder-led (INFERRED from headcount): CEO as economic buyer. Larger: finance lead titles |
| Which persona leads? | Set per workflow (INFERRED default): W1 and W3 lead with Champion (technical build); W2 and W5 lead with Economic buyer (expansion, capital). Second persona added later, not in parallel |
| How many contacts per account? | Max 2 in sequence at once, staggered (iron law 14; exact cap INFERRED) |
| No person found for the lead persona? | Fall back to the next persona. None found: account to a "no contact" list, retry next month |
| Person already contacted in the suppression window? | Yes: skip. No: continue (workflow-anatomy deduplication) |

---

## Step 7: Find and verify emails

| | |
|---|---|
| **What happens** | Waterfall email finding, then verification, then a send/no-send decision per address. LinkedIn URL kept for the LinkedIn channel |
| **Tool** | Clay email waterfall. **DECISION PENDING:** providers (kit names Prospeo, LeadMagic, Findymail) and verifier (kit names Debounce, ZeroBounce, NeverBounce). Nigerian email coverage per provider is unknown: test on 50 rows and keep the best order (INFERRED) |

| Decision | Answer leads to |
|---|---|
| Email found by provider 1? | Yes: verify. No: provider 2, then 3. None: LinkedIn-only route |
| Verification result? | Valid: send. Catch-all: send only if the account is Ready now and volume per domain is low (INFERRED rule). Invalid or unknown: do not email; LinkedIn-only route |
| Personal email domain (e.g. Gmail)? | Do not email (INFERRED: B2B outreach to work addresses only); LinkedIn-only |
| Legal basis for cold email in Nigeria? | **Not researched.** Check the Nigeria data protection rules with legal before launch (open question) |

---

## Step 8: The sequence (email and LinkedIn)

| | |
|---|---|
| **What happens** | Copy is written per workflow with `/build-workflow-spec` then `/campaign-copy`, from approved facts only, with the Matrix 1 angle and a signal-specific first line. Email and LinkedIn run in one coordinated cadence |
| **Tool** | Email sequencer: **DECISION PENDING** (kit options: EmailBison, Instantly, Smartlead, PlusVibe). LinkedIn: **DECISION PENDING** (kit example: HeyReach). QA with /campaign-qa; deliverability with /inbox-placement-test (built on EmailBison + MailReach) |

Default cadence (INFERRED; set per workflow in its spec):

| Day | Channel | Content |
|---|---|---|
| 1 | Email 1 | Signal line + Matrix 1 angle + one proof point for the segment [icp.md Layer 5 proof table] |
| 2 | LinkedIn | Connection request, no pitch |
| 4 | Email 2 | Second angle (other product row or persona pain) |
| 6 | LinkedIn | DM if connected (linkedin-dm-frameworks) |
| 9 | Email 3 | Short close-the-loop |

| Decision | Answer leads to |
|---|---|
| Copy passes QA (facts gate, no em dashes, no banned claims, variables filled)? | Yes: load. No: back to /campaign-copy |
| Sender pool passes placement test? | KEEP: send. MARGINAL: reduce volume, re-test. KILL: rotate pool [/inbox-placement-test] |
| Reply received at any step? | Yes: stop all steps on both channels, go to step 9. No: continue |
| LinkedIn connection accepted? | Yes: DM on day 6. No: email only |
| Bounce? | Stop; mark email invalid in Clay and HubSpot; feed bounce rate to step 11 |

---

## Step 9: Reply handling

| | |
|---|---|
| **What happens** | Every reply is classified and acted on within one business day (INFERRED SLA) |
| **Tool** | Sequencer inbox → n8n webhook → AI classification (Claude, INFERRED) → HubSpot update + Slack alert to the owner. Before Week 4: manual classification |

| Reply class | Action |
|---|---|
| Interested / wants a call | Book meeting; HubSpot deal created; hand to Paystack sales owner with signal + angle context |
| Referral to another person | Add referred contact, restart at step 8 with "referred by" line |
| Not now / timing | Snooze; re-enter on next signal or after 90 days (INFERRED) |
| Already a Paystack customer | Remove from outbound; add to suppression list; flag gap in step 4 (suppression list missed them) |
| Using a competitor, happy | Log competitor; nurture; re-enter on a new signal |
| Not a fit | Log reason; feeds ICP review in step 11 |
| Unsubscribe / negative | Suppress permanently, all channels |
| Out of office | Pause, resume after return date |
| Objection (price, support, regulation, "you compete with us") | Log objection type [personas.md objections]; send matching answer or route to sales |

---

## Step 10: CRM

| | |
|---|---|
| **What happens** | HubSpot holds every contacted account and person, their signal, segment, persona, workflow, sequence status, reply class, deal and outcome. Clay pushes on load; n8n syncs replies |
| **Tool** | HubSpot (from Week 3) [CLAUDE.md] |

| Decision | Answer leads to |
|---|---|
| Account already in HubSpot? | Yes: update, do not duplicate; check owner before outreach. No: create |
| Account owned by a Paystack rep or is a customer? | Yes: do not sequence; notify owner. No: continue |
| Lifecycle stage (INFERRED design) | Prospect (in sequence) → Engaged (replied) → Meeting booked → Opportunity → Won / Lost, with Lost reason |
| Deal lost? | Store reason (price, competitor, timing, no fit); reason feeds step 11 |

Required properties: signal type, signal date, workflow W #, segment, Matrix 1 cell, persona, product angle, displacement flag, readiness tier, reply class, objection type, disqualify reason.

---

## Step 11: Weekly feedback loop

| | |
|---|---|
| **What happens** | Once a week, results are pulled into the Context OS and the rules are updated: what worked goes to `knowledge-base/learnings/`, changes to targeting go to icp.md and signal-matrix.md, all logged in the work log |
| **Tool** | HubSpot reports + sequencer stats → Claude Code session → GitHub commit; Notion publish when needed. Tracker: Matrix 3 in signal-matrix.md |

Weekly review questions and what each answer changes:

| Question | If yes | If no |
|---|---|---|
| Did a workflow's reply rate or meetings beat the others? | Raise its priority in Matrix 2; write the learning | Keep |
| Did a signal produce fewer accounts than its volume estimate? | Lower its Volume score; consider killing it | Keep |
| Did many rows fail one fit gate? | Fix the signal source or tighten the target definition | Keep |
| Did "already a customer" replies appear? | Fix the suppression list sync | Keep |
| Did one persona reply more in a segment? | Make it the lead persona for that segment | Keep |
| Did one objection repeat? | Add the answer to personas.md and copy | Keep |
| Did bounce or spam placement rise? | Run /inbox-placement-test; pause pool | Keep |
| Did a Tier 3 vertical produce meetings via referral or inbound? | Re-score it in icp.md 1b | Keep |
| Did an open question get answered by sales data? | Update icp.md and remove the question | Keep |

Outputs each week: updated Matrix 3 tracker, one learnings file, any icp.md / signal-matrix.md edits, work-log entry.

---

## Four-pillar check

| Pillar | How the design meets it | Gaps |
|---|---|---|
| **Clean data** | One table per source, accounts before contacts, dedupe at every load, suppression of customers, competitors and contacted people, stored disqualify reasons, email verification before send (steps 2 to 7) | **Suppression list of current Paystack merchants does not exist** (icp.md Q10): blocks launch. Nigerian enrichment and email coverage unmeasured. Domain matching for app brands |
| **Always-on signals** | Five scheduled signals with cadences from the periodicity matrix; registry diffs run unattended; signal date and window on every row (step 1) | Schedules are manual until n8n (Week 4). FCCPC and NLRC update cadences unknown. Scraper breakage needs alerts |
| **Composable workflows** | Same pipeline for every workflow; only step 1 inputs and step 5 routing change. One "Nigeria registry diff" build serves W1, W4 and later N2, N4; fintech and betting share 6 of 7 universal signal builds [signal-matrix.md 2b]. Saved as Clay templates (iron laws 17, 18) | Sequencer and LinkedIn tool not chosen, so the load step is not yet composable |
| **Tight feedback loops** | Reply classes, objection types and lost reasons are HubSpot properties; weekly review maps each result to a specific file change; all changes committed and logged | Weekly review is a manual session; no dashboard yet. Loop depends on HubSpot (Week 3) |

---

## Open decisions and blockers

| # | Item | Blocks |
|---|---|---|
| 1 | Suppression list of current Paystack merchants (from Paystack CRM) | Step 4, every launch |
| 2 | Email sequencer choice (EmailBison / Instantly / Smartlead / PlusVibe) | Step 8 |
| 3 | LinkedIn tool choice (e.g. HeyReach) | Step 8 |
| 4 | Email finding and verification providers; Nigerian coverage test | Step 7 |
| 5 | Approved-facts list in `context/messaging/` and tone in `context/brand-kit/` | Step 8 copy |
| 6 | Legal check on cold outreach under Nigerian data protection rules (not researched) | Step 7 and 8 |
| 7 | Betting regulation research | Betting workflows (W4) |
| 8 | Sales handoff: who at Paystack owns booked meetings | Step 9 |
