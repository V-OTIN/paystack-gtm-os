# Paystack GTM Context OS

## Company
Paystack (paystack.com), a Lagos-founded payments company owned by Stripe since October 2020. It helps businesses in Africa accept payments online and in person, pay out, bill recurrently and verify customers, with per-transaction pricing and no monthly fee. It is live in Nigeria, Ghana, Kenya, South Africa and Côte d'Ivoire, and since January 2026 it sits inside The Stack Group alongside Paystack Microfinance Bank and the Zap consumer app. Sources: [company.md](context/docs/research/company.md), [voice.md](context/docs/research/voice.md).

Outbound focus (decided 2026-11-12): Nigerian mid-market and enterprise.

## File index

### Context
- [context/icp/icp.md](context/icp/icp.md): five-layer ICP, not-a-fit list, open questions
- [context/icp/personas.md](context/icp/personas.md): champion, economic buyer and influencer personas
- [context/icp/signal-matrix.md](context/icp/signal-matrix.md): segments x personas angles, buying signals with scores, top 5 to build, workflow tracker
- [context/docs/gtm-system.md](context/docs/gtm-system.md): end-to-end outbound system, step by step, with decisions, tools and four-pillar check
- [diagrams/paystack-gtm-system.json](diagrams/paystack-gtm-system.json) and [.svg](diagrams/paystack-gtm-system.svg): flowchart spec and layout for the GTM system, drawn on the Miro board [Paystack GTM System](https://miro.com/app/board/uXjVEOwCk1Y=/)
- [context/docs/research/company.md](context/docs/research/company.md): products, pricing, markets, funding, team, leadership
- [context/docs/research/customers.md](context/docs/research/customers.md): named customers, industries, Wall of Love testimonials
- [context/docs/research/competitors.md](context/docs/research/competitors.md): competitors and how each positions itself
- [context/docs/research/market.md](context/docs/research/market.md): regulation and market changes by country
- [context/docs/research/signals.md](context/docs/research/signals.md): buying signals, hiring, and verified signal data sources (FCCPC, NLRC/LSLGA, NUC, CBN, funding)
- [context/docs/research/voice.md](context/docs/research/voice.md): how Paystack describes itself, verbatim
- [context/positioning/value-proposition.md](context/positioning/value-proposition.md): job, pain, gain and proof per persona
- [context/positioning/positioning.md](context/positioning/positioning.md): category, target, alternatives, unique value, proof, positioning statement
- [context/positioning/competitors.md](context/positioning/competitors.md): competitor table, where Paystack wins and loses, how to respond
- [context/messaging/messaging.md](context/messaging/messaging.md): core message, four pillars with proof, persona angles, words to use and avoid
- [context/brand-kit/brand.md](context/brand-kit/brand.md): tone of voice and verbatim key phrases from Paystack's copy
- [context/docs/case-studies.md](context/docs/case-studies.md): every customer story in the research (customer, size, industry, problem, result, quote, source)
- [context/messaging/facts.md](context/messaging/facts.md): authorized copy facts (sender, locked value prop, approved claims, Renmoney as the only proof name, bans, CTA ladder). Approved for the bootcamp, not by Paystack

### Campaigns
- [output/campaigns/campaign-strategy.md](output/campaigns/campaign-strategy.md): 18 ranked outbound campaign ideas with mother intent, segment, signal, angle, volume, difficulty and tier
- [output/campaigns/fccpc-approved-lenders/workflow-spec.md](output/campaigns/fccpc-approved-lenders/workflow-spec.md): W1 workflow spec (FCCPC newly approved lenders) with approved copy (3 emails + 2 LinkedIn DMs), COPY-APPROVED

### Knowledge base (from the GTM Starter Kit)
- [knowledge-base/playbooks/signal-matrix-framework.md](knowledge-base/playbooks/signal-matrix-framework.md): how to build the signal matrix
- [knowledge-base/playbooks/workflow-anatomy.md](knowledge-base/playbooks/workflow-anatomy.md): workflow layers and the Mother Intent Catalog
- [knowledge-base/playbooks/copy-frameworks.md](knowledge-base/playbooks/copy-frameworks.md), [copy-iron-laws.md](knowledge-base/playbooks/copy-iron-laws.md), [copy-bans.yaml](knowledge-base/playbooks/copy-bans.yaml), [linkedin-dm-frameworks.md](knowledge-base/playbooks/linkedin-dm-frameworks.md): copy rules and frameworks
- [knowledge-base/playbooks/clay/](knowledge-base/playbooks/clay/): iron-laws.md, expert.md, prompts.md, formulas.md, actions-data-credits.md
- [knowledge-base/playbooks/templates/facts-template.md](knowledge-base/playbooks/templates/facts-template.md): template for the approved facts file
- `knowledge-base/learnings/`: empty until campaigns run

### Operating files
- [weekly-priorities/2026-W45.md](weekly-priorities/2026-W45.md), [weekly-priorities/2026-W46.md](weekly-priorities/2026-W46.md): weekly goals
- [work-log/2026-W45.md](work-log/2026-W45.md), [work-log/2026-W46.md](work-log/2026-W46.md): change logs
- [README.md](README.md): repo overview
- [.claude/settings.json](.claude/settings.json): project settings (Miro plugin enabled)
- `meetings/`: empty

### Tools
- [tools/rex/](tools/rex/): Clay API client (start with README.md, GETTING_STARTED.md, clay-api-reference.md; table registry in registry/INDEX.md; ClayLens cost extension in claylens/)
- [tools/crawl4ai/README.md](tools/crawl4ai/README.md), [tools/agent-browser/README.md](tools/agent-browser/README.md): research helpers

## How this folder works
- `context/icp/`: ICP, personas and signal matrix. Read before any targeting, list building or copy.
- `context/positioning/`: value proposition, positioning and competitors. Read before writing any messaging.
- `context/messaging/`: core message, pillars and approved facts. Read before writing copy.
- `context/brand-kit/`: tone of voice and key phrases. Read before writing copy.
- `context/docs/research/`: raw facts about Paystack, each with a source. Read when you need evidence. Never put conclusions here.
- `context/docs/`: system architecture and other synthesised docs.
- `knowledge-base/playbooks/`: frameworks and methods. Read when a skill or task names one.
- `knowledge-base/learnings/`: what worked and what didn't. Read before planning a new campaign.
- `meetings/`: meeting notes. Read when a task refers to a past conversation.
- `output/campaigns/`: workflow specs and campaign outputs, one folder per campaign.
- `tools/`: tool notes and scripts. Read before using a tool.
- `weekly-priorities/`: this week's goals, one file per ISO week. Read at the start of every session.
- `work-log/`: a timestamped log of changes, one file per ISO week. Add to it after every change.
- `.claude/skills/`: reusable skills (slash commands).

## Rules
- Cite a source for every company fact.
- Never invent numbers.
- No em dashes in any copy.
- Ask before sending or publishing anything.
- Log every change in this week's work log.

## Skills (in .claude/skills, from the GTM Starter Kit)
- Strategy: /signal-matrix, /campaign-strategy, /build-workflow-spec, /campaign-copy, /prompt-builder
- Clay build: /campaign-contract, /design-clay-table-json, /import-clay-table, /build-clay, /save-clay-schema, /export-tables
- Clay cost and QA: /calculate-costs, /workspace-cost-audit, /campaign-qa
- Deliverability: /inbox-placement-test
- Research and diagrams: /crawl4ai, /agent-browser, /miro-gtm-flowchart

## Tools
- Claude Code (in VS Code): builds and maintains this Context OS
- GitHub (V-OTIN): version control, the source of truth
- Miro (plugin with MCP): diagrams and GTM flowcharts
- Notion (claude.ai connector): where we publish finished docs; GitHub stays the source of truth. Published copy: [Paystack GTM OS](https://app.notion.com/p/416ca87d1d13813a9634f2ab607eb29c) (private draft page; mirrors `context/` and `output/`, raw research not published; republish after changes)
- Clay: prospecting, enrichment, signals, Claygents (from Week 2)
- HubSpot: CRM, pipeline and lifecycle (from Week 3)
- n8n: automation layer (from Week 4)
- Helpers in tools/: rex (Clay API client), crawl4ai, agent-browser
