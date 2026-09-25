---
name: stewardship-valuation
description: Progress and investment read-through for institutional sustainable-finance research; return evidence-linked findings, assumptions, gaps and reviewable outputs.
license: MIT
metadata:
  author: HHFinAi
  version: "0.2.0"
---
# Progress and investment read-through

Read `../../AGENTS.md` and `../../prompts/stages/valuation.md` relative to this skill directory. Obtain the current stage packet using the repository CLI. Do not create or claim unavailable source access.

## Task
Calculate overdue/unverified milestones and a simple benchmark-relative return only as descriptive context. Neither abnormal return nor management action establishes causal engagement impact. Update the investment thesis with evidence, downside and alternative explanations.

## Deliverable
Return the fields in `../../schemas/artifact.schema.json`; use the current run ID and input digest. Required sections: milestone_status, event_return_context, financial_thesis_update, outcome_attribution. Include source IDs, scope, periods, methods and material gaps. Call only allowlisted calculations with explicit provenance; missing evidence means NEEDS_DATA, not invented values.

## Limit
No automatic votes, emails, allegations of illegality, divestment, trading or claim of causal engagement success. Human approval is required before any external communication; this package has no sending or execution connection.
