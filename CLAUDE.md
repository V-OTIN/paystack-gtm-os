# Paystack GTM Context OS

## Company
Paystack (paystack.com). To be filled in after research (step 6).

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
- Clay: prospecting, enrichment, signals, Claygents (from Week 2)
- HubSpot: CRM, pipeline and lifecycle (from Week 3)
- n8n: automation layer (from Week 4)
- Helpers in tools/: rex (Clay API client), crawl4ai, agent-browser
