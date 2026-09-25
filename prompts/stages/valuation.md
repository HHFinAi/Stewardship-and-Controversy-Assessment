# Progress and investment read-through

## Decision context
What is evidenced, what change is sought, how will progress be verified, and what investment or engagement review is warranted?

## Assignment
Calculate overdue/unverified milestones and a simple benchmark-relative return only as descriptive context. Neither abnormal return nor management action establishes causal engagement impact. Update the investment thesis with evidence, downside and alternative explanations.

## Required output sections
- `milestone_status`: substantive analysis linked to claim IDs.
- `event_return_context`: substantive analysis linked to claim IDs.
- `financial_thesis_update`: substantive analysis linked to claim IDs.
- `outcome_attribution`: substantive analysis linked to claim IDs.

## Evidence and methodology
Use FRC-2026, IFRS-S1 with edition, applicability, date and limitations. Source references are in `references/standards.json` from the repository root.

## Return contract
Return the structured artifact in `schemas/artifact.schema.json`; copy run_id, input_digest, stage_id and revision from the current packet. Never recycle IDs from a demo. Source uncertainty is not resolved by lowering confidence alone: preserve a gap or issue.

## Domain boundary
No automatic votes, emails, allegations of illegality, divestment, trading or claim of causal engagement success. Human approval is required before any external communication; this package has no sending or execution connection.

A domain calculation must pass recomputation. The minimal runnable illustration is `milestone_status`; other needed specialist models must remain explicitly external and independently reviewed.
