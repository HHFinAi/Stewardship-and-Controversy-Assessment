---
name: stewardship-escalation
description: Escalation and stewardship accountability for institutional sustainable-finance research; return evidence-linked findings, assumptions, gaps and reviewable outputs.
license: MIT
metadata:
  author: HHFinAi
  version: "0.2.0"
---
# Escalation and stewardship accountability

Read `../../AGENTS.md` and `../../prompts/stages/escalation.md` relative to this skill directory. Obtain the current stage packet using the repository CLI. Do not create or claim unavailable source access.

## Task
Present evidence-based engagement, voting, collaborative action and holding-review options without automatically acting. Consider likely consequences for affected people and mandate restrictions. Draft only; require human approval to send, vote or publish. Report outcomes separately from meetings and letters.

## Deliverable
Return the fields in `../../schemas/artifact.schema.json`; use the current run ID and input digest. Required sections: engage_vote_escalate_options, policy_and_mandate_consistency, communications_review, outcomes_reporting. Include source IDs, scope, periods, methods and material gaps. Call only allowlisted calculations with explicit provenance; missing evidence means NEEDS_DATA, not invented values.

## Limit
No automatic votes, emails, allegations of illegality, divestment, trading or claim of causal engagement success. Human approval is required before any external communication; this package has no sending or execution connection.
