# Worked example — Stewardship and Controversy Assessment Agent

**SYNTHETIC / RESEARCH_ONLY. All company, portfolio, instrument and outcome values are fictional. No capital should be deployed from this example.**

## Investment-relevant observation
As of 25 September 2026, milestone M1, due 1 September with no completion date, is **overdue**. M2, due 20 September and completed with a verified-outcome declaration on 18 September, is classified as a **verified outcome**.

## Reproduce the arithmetic
From the repository root:
```bash
python -m sf_agent calc --operation milestone_status --arguments examples/calculation-arguments.json
```

### Inputs
```json
{
  "milestones": [
    {
      "id": "M1",
      "due_on": "2026-09-01",
      "completed_on": null,
      "outcome_verified": false
    },
    {
      "id": "M2",
      "due_on": "2026-09-20",
      "completed_on": "2026-09-18",
      "outcome_verified": true
    }
  ],
  "as_of": "2026-09-25"
}
```

### Recomputed result
```json
{
  "milestones": [
    {
      "id": "M1",
      "status": "OVERDUE",
      "days_overdue": 24,
      "completion_was_late": null
    },
    {
      "id": "M2",
      "status": "VERIFIED_OUTCOME",
      "days_overdue": 0,
      "completion_was_late": false
    }
  ],
  "counts": {
    "VERIFIED_OUTCOME": 1,
    "COMPLETED_UNVERIFIED": 0,
    "OVERDUE": 1,
    "PENDING": 0
  },
  "verified_outcome_fraction": 0.5,
  "causal_engagement_success_established": false
}
```

## What the result does not establish
The package validates the status record, not the underlying evidence or investor causality. A late milestone prompts a human thesis/engagement review, not automatic divestment, a vote or external communication. Meetings and letters are activity, not outcomes.

## Diligence handoff
Fictional engagement: an overdue material milestone triggers a human review; a meeting or letter is activity, not evidence of an achieved outcome.

Register source-backed inputs, contrary evidence, material data gaps and the investment constraints before replacing this illustrative result with actual research. Unit, boundary, timing, attribution and legal judgments are not supplied by arithmetic alone. No human research approval is recorded for this example.
