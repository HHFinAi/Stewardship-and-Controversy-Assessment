# Evidence and controversy chronology

## Decision context
What is evidenced, what change is sought, how will progress be verified, and what investment or engagement review is warranted?

## Assignment
Separate incident date, first public report and retrieval date. Deduplicate repeated reporting; a copied story is not independent corroboration. Attribute allegations and company responses. Do not decide criminal liability or omit material conflicting evidence.

## Required output sections
- `event_vs_publication_dates`: substantive analysis linked to claim IDs.
- `allegations_responses_findings`: substantive analysis linked to claim IDs.
- `affected_groups`: substantive analysis linked to claim IDs.
- `materiality_and_confidence`: substantive analysis linked to claim IDs.

## Evidence and methodology
Use UNGP, IFRS-S1 with edition, applicability, date and limitations. Source references are in `references/standards.json` from the repository root.

## Return contract
Return the structured artifact in `schemas/artifact.schema.json`; copy run_id, input_digest, stage_id and revision from the current packet. Never recycle IDs from a demo. Source uncertainty is not resolved by lowering confidence alone: preserve a gap or issue.

## Domain boundary
No automatic votes, emails, allegations of illegality, divestment, trading or claim of causal engagement success. Human approval is required before any external communication; this package has no sending or execution connection.
