# Mandate and investable decision

## Decision context
What is evidenced, what change is sought, how will progress be verified, and what investment or engagement review is warranted?

## Assignment
Identify decision owner, objective, benchmark, time horizon, currency, jurisdiction, risk budget and instrument. Specify whether output supports equity, credit, portfolio constraints or a private contract. A research theme is not a security. Missing material instructions require NEEDS_DATA. Do not execute trades or communicate externally.

## Required output sections
- `decision_question`: substantive analysis linked to claim IDs.
- `instrument_boundary`: substantive analysis linked to claim IDs.
- `mandate_constraints`: substantive analysis linked to claim IDs.

## Evidence and methodology
Use the mandate and registered primary evidence with edition, applicability, date and limitations. Source references are in `references/standards.json` from the repository root.

## Return contract
Return the structured artifact in `schemas/artifact.schema.json`; copy run_id, input_digest, stage_id and revision from the current packet. Never recycle IDs from a demo. Source uncertainty is not resolved by lowering confidence alone: preserve a gap or issue.

## Domain boundary
No automatic votes, emails, allegations of illegality, divestment, trading or claim of causal engagement success. Human approval is required before any external communication; this package has no sending or execution connection.
