Analyse whether the company should bid on this RFP.

**Arguments:** `$ARGUMENTS` (the bid slug)

## Steps

1. Read `bids/$ARGUMENTS/parsed/rfp.md` in full.
2. Read `company/company-info.json`.
3. Read all files in `company/about/`.
4. Read all files in `company/experience/`.

## Analysis framework

Score each dimension on a 1–5 scale, then recommend GO / NO-GO / CONDITIONAL GO.

### 1. Eligibility (pass/fail — any fail = NO-GO unless waivable)
Check every eligibility criterion in the RFP against the company profile:
- Minimum turnover / revenue requirements
- Years in operation
- Prior experience requirements (sector, project size, number of similar projects)
- Geographic / registration requirements
- Certifications required (ISO, etc.)
- Any blacklist / debarment declarations

For each criterion: state whether the company MEETS / DOES NOT MEET / PARTIALLY MEETS it,
with the evidence from the company profile.

### 2. Technical fit (1–5)
- How well does the company's capability match the scope of work?
- Do we have relevant past projects?
- Do we have the required team / skills?

### 3. Commercial attractiveness (1–5)
- Estimated contract value vs. effort
- Payment terms (advance, milestone, retention, penalty for delay)
- Liquidated damages / penalty clauses — are they reasonable?

### 4. Risk level (1–5, where 5 = highest risk)
- Unreasonable timelines
- Vague scope that could expand
- Unfavourable IP / data clauses
- Onerous warranty / SLA requirements
- Single-point-of-failure dependencies

### 5. Strategic fit (1–5)
- Is this buyer / sector part of our target market?
- Will this reference be valuable?
- Do we want to win, or just participate?

## Output format

Write to `bids/$ARGUMENTS/analysis/go-nogo.md`:

```markdown
# Go / No-Go Analysis — [RFP name]
**Date:** [today]
**Recommendation:** GO / NO-GO / CONDITIONAL GO

## Eligibility Checklist
| Criterion | Requirement | Our Status | Evidence |
|---|---|---|---|

## Scoring
| Dimension | Score (1–5) | Notes |
|---|---|---|
| Technical fit | | |
| Commercial attractiveness | | |
| Risk level (lower is better) | | |
| Strategic fit | | |
| **Overall** | | |

## Key reasons for recommendation
[3–5 bullet points]

## Conditions / actions required before bidding
[If CONDITIONAL GO: what must be resolved]

## Risks to flag to management
[Top 3 risks]
```

Tell the user where the file was saved and summarise the recommendation in 2–3 sentences.
