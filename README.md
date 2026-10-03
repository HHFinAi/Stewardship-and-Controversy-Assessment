# Stewardship and Controversy Assessment

**Investment research by HHFinAi: evidence, issuer questions, observable milestones and accountable follow-up.**

What is evidenced, what change is sought, how would progress be verified, and how could the result change the investment case?

## Start with the research

### Microsoft — responsible AI from disclosure to investor engagement

**Assessment: seek implementation evidence, not another principles statement.** This public-disclosure case connects environmental constraints, AI accountability, workforce, intellectual property and privacy to investment questions and six proposed milestones.

**Status:** proposed engagement programme, prepared **4 October 2026**. No issuer meeting, request, response or engagement outcome is claimed. The 2026 Microsoft HTML overview is a company disclosure, not independent assurance that every control works.

[Read the engagement case](examples/microsoft-ai/README.md) · [Inspect the proposed milestone ledger](examples/microsoft-ai/milestones.json) · [Review source boundaries](examples/microsoft-ai/SOURCES.md)

The companion [Microsoft cooling-economics case](https://github.com/HHFinAi/Sustainability-to-Financial-Materiality-Analysis/blob/main/examples/microsoft-ai/README.md) shows how a financial evidence gap becomes a specific research or engagement question. Its project inputs are illustrative assumptions, not Microsoft's reported site economics.

## What this research contributes

The case separates company statements, unverified implementation, original investment inferences and proposed engagement activity. Requests have observable evidence criteria and relative timeframes. A meeting or a policy announcement is not counted as an outcome, and absence of public disclosure is not proof that a control is absent.

Nuveen's transparency, accountability and impact framing is attributed in the case. The original HHFinAi implementation adds issuer-specific evidence gaps, financial transmission and a milestone ledger. The release was prepared with AI assistance under Ed's portfolio-development brief; independent human validation and workflow research approval are not recorded.

[Portfolio and research standards](https://github.com/HHFinAi/HHFinAi)

## Demonstrations are separate from issuer research

[Original synthetic worked example](examples/WORKED_EXAMPLE.md) demonstrates milestone-status arithmetic. [Synthetic workflow packet](examples/reports/synthetic-packet.md) demonstrates the engine. [Methodology-only source study](examples/reports/source-study-packet.md) deliberately remains `NEEDS_DATA`. None establishes an actual engagement or a completed issuer assessment.

## Workflow infrastructure

**Engine v0.2.0 · Python 3.10+ · 10 research stages · 3 named routes · Human review**

[Workflow](WORKFLOW.md) · [Host instructions](AGENTS.md) · [Skills](PROMPTS.md) · [Data contract](docs/DATA_CONTRACT.md) · [Evidence and audit](docs/AUDIT.md) · [Validation](docs/VALIDATION.md)

The local engine validates and records structured research. It does not retrieve documents or run an LLM. A human or separately authorized AI host performs the substantive work.

```bash
python -m unittest discover -s tests -v
python scripts/check_repository.py
python -m sf_agent routes
python -m sf_agent demo --out runs/demo-01
python -m sf_agent report --run runs/demo-01
python -m sf_agent export --run runs/demo-01 --out exports/demo-01
python -m sf_agent calc --operation milestone_status --arguments examples/calculation-arguments.json
```

Use a fresh output directory. The demo uses fictional inputs and pre-authored fixtures; it is not live research. The supplemental Microsoft milestone ledger is a research artifact, not an automatic engine submission or an approval record.

For actual research, replace all placeholders in `examples/research-request-template.json` and keep confidential material outside the public repository:

```bash
python -m sf_agent init --request your-request.json --out runs/research-01
python -m sf_agent next --run runs/research-01
python -m sf_agent submit --run runs/research-01 --stage mandate --artifact your-artifact.json --revision 0
python -m sf_agent status --run runs/research-01
```

Continue using the current revision. Material evidence gaps require `NEEDS_DATA` or an explicit blocking issue.

## Controls and limitations

No automatic votes, emails, allegations of illegality, divestment, trading or causal claims about engagement success. Human approval is required before external communication; this package has no sending or execution connection. Milestones alone do not establish investability, legal compliance or positive impact.

Inspectable local records are not tamper-proof or independently audited. Reviewer names and evidence-review flags are attestations, not authenticated identities. Tests establish selected software behavior, not source truth, investment alpha, causal impact or production security. [Claim-to-control map](docs/INSTITUTIONAL_QUALITY.md).

[Sources](references/SOURCES.md) · [FAQ](docs/FAQ.md) · [Notices](NOTICE.md) · [Repository metadata](repository-metadata.json) · [Discoverability](docs/GEO_SEO.md)

The original workflow core and source-study controls are preserved. Fetch and pull remote changes before editing an existing clone; preserve `.git` and review local changes. [GitHub Desktop guide](START_HERE_GITHUB_DESKTOP.md).
