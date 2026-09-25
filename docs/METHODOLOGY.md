# Methodology and model boundaries

No automatic votes, emails, allegations of illegality, divestment, trading or claim of causal engagement success. Human approval is required before any external communication; this package has no sending or execution connection.

## Analytical outputs
- Dated incident/allegation/response chronology
- SMART objectives and outcome milestones
- Escalation, voting and investment-review options
- Activities-versus-outcomes stewardship report

## Calculation library
The implementation is in `sf_agent/analytics.py`; generic helpers are in `sf_agent/maths.py`. Every exposed operation has argument-unit and result-unit metadata and is callable with `python -m sf_agent calc`. Arguments are not sourced automatically. See the operation inventory below, the worked example and domain regression tests.

### Stewardship calculations
`milestone_status` uses an explicit as-of date and mutually exclusive categories: verified outcome, completed but unverified, overdue and pending. Completion evidence must not be future-dated and verified outcomes require completion. It reports overdue and verified fractions separately, retains late completion, and yields null fractions for an empty plan. Milestone completion is an analyst-attested status; the software does not verify the outcome or causal investor contribution.

`benchmark_relative_return` compounds aligned periodic investment and benchmark returns, calculates arithmetic cumulative excess and, where the benchmark wealth remains positive, relative wealth return. It is descriptive market context only—not a risk-adjusted event study, alpha estimate, engagement impact or causal attribution. Voting, email, divestment, collaborative engagement and public controversy claims are never executed automatically.


## Evidence status
Causal and legal interpretations remain human judgments. The software is not a complete implementation or certification of the referenced standards. Read the exact applicable original documents; the dated source register gives the verification scope. Proposed changes and future validation dates must not be applied retrospectively or represented as current law.
