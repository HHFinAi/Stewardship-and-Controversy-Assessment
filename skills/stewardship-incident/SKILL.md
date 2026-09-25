---
name: stewardship-incident
description: Evidence and controversy chronology for institutional sustainable-finance research; return evidence-linked findings, assumptions, gaps and reviewable outputs.
license: MIT
metadata:
  author: HHFinAi
  version: "0.2.0"
---
# Evidence and controversy chronology

Read `../../AGENTS.md` and `../../prompts/stages/incident.md` relative to this skill directory. Obtain the current stage packet using the repository CLI. Do not create or claim unavailable source access.

## Task
Separate incident date, first public report and retrieval date. Deduplicate repeated reporting; a copied story is not independent corroboration. Attribute allegations and company responses. Do not decide criminal liability or omit material conflicting evidence.

## Deliverable
Return the fields in `../../schemas/artifact.schema.json`; use the current run ID and input digest. Required sections: event_vs_publication_dates, allegations_responses_findings, affected_groups, materiality_and_confidence. Include source IDs, scope, periods, methods and material gaps. Call only allowlisted calculations with explicit provenance; missing evidence means NEEDS_DATA, not invented values.

## Limit
No automatic votes, emails, allegations of illegality, divestment, trading or claim of causal engagement success. Human approval is required before any external communication; this package has no sending or execution connection.
