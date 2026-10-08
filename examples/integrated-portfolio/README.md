# Stewardship handoff: illustrative five-issuer portfolio

Read the [dated investment committee memo](https://github.com/hhfinai/Portfolio-Carbon-Accounting-and-Attribution/blob/main/examples/integrated-portfolio/MEMO.md) and [proposed handoff packet](https://github.com/hhfinai/Portfolio-Carbon-Accounting-and-Attribution/blob/main/examples/integrated-portfolio/handoffs.json). They connect separate carbon scopes, Meta site water evidence and financially relevant evidence requests. Portfolio weights are hypothetical; shareholder authority is unverified.

The proposed milestones are 7 November 2026 for public site/permit verification, 6 January 2027 for a reviewed draft evidence request, and 6 April 2027 for scenario and gap review. Owners remain unassigned. A new stewardship research run must register evidence and open issues under the repository's normal contract. Any contact requires separate authorization; no issuer communication, proxy vote or trade has occurred.

The owning carbon repository maintains the reproducible calculation and tests:

```sh
python3 examples/integrated-portfolio/model.py --check
python3 -m unittest discover -s tests -p 'test_integrated_portfolio.py' -v
```

These commands run from the carbon repository root. This packet remains `NEEDS_DATA`, with independent review unrecorded and research approval not granted.
