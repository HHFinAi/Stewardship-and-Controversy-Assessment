# Market context and implementation evidence

## Decision context
What is evidenced, what change is sought, how will progress be verified, and what investment or engagement review is warranted?

## Assignment
For public instruments obtain a timestamped scoped quote, price convention, liquidity, currency and funding/borrow evidence where relevant. For private structures obtain reviewed contracts and eligibility. Portfolio accounting and compliance assessments may remain RESEARCH_ONLY. No invented price or automatic hedge.

## Required output sections
- `market_or_contract_evidence`: substantive analysis linked to claim IDs.
- `liquidity_funding_access`: substantive analysis linked to claim IDs.
- `portfolio_context`: substantive analysis linked to claim IDs.

## Evidence and methodology
Use the mandate and registered primary evidence with edition, applicability, date and limitations. Source references are in `references/standards.json` from the repository root.

## Return contract
Return the structured artifact in `schemas/artifact.schema.json`; copy run_id, input_digest, stage_id and revision from the current packet. Never recycle IDs from a demo. Source uncertainty is not resolved by lowering confidence alone: preserve a gap or issue.

## Domain boundary
No automatic votes, emails, allegations of illegality, divestment, trading or claim of causal engagement success. Human approval is required before any external communication; this package has no sending or execution connection.
