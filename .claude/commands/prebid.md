Draft pre-bid clarification questions to submit to the buyer.

**Arguments:** `$ARGUMENTS` (the bid slug)

## Steps

1. Read `bids/$ARGUMENTS/parsed/rfp.md` in full.
2. Read `bids/$ARGUMENTS/analysis/contradictions.md` if it exists.
3. Read `bids/$ARGUMENTS/analysis/risks.md` if it exists.
4. Read `company/company-info.json` and `company/about/` to understand our position.

## What to look for

Generate questions from four sources:

### A. Contradictions (from contradictions.md or found while reading)
Each contradiction that affects the bid should become a question asking for the correct version.

### B. Vague or ambiguous scope
- Phrases like "as required", "best efforts", "industry standard", "adequate" without definition
- Scope items that could be interpreted broadly or narrowly
- Deliverables without clear acceptance criteria

### C. Missing information
- Technical specifications not defined (e.g. load, volume, concurrency)
- Integration requirements not specified
- Pricing basis unclear (per unit, fixed, time-and-material)
- SLA measurement methodology not defined

### D. Risky clauses worth challenging
- Unreasonable penalty rates
- Unlimited liability clauses
- IP transfer clauses that are too broad
- Timelines that appear infeasible

## Output

Write to `bids/$ARGUMENTS/analysis/prebid-questions.md`:

```markdown
# Pre-Bid Clarification Questions — [RFP Name]
**RFP Reference:** [reference number from RFP]
**Submitted by:** [company legal name from company-info.json]
**Date:** [today]

---

| Q# | Section Reference | Our Question | Reason for asking |
|---|---|---|---|

---

## Questions in full

### Q1 — [Topic]
**Section:** [X.X]
**Question:** [Precise, professional question]
**Context:** [1 sentence on why we are asking — optional, include only if it adds clarity]

---

[Repeat for each question]

---

## Submission note
These questions should be submitted via [submission method from RFP] before [pre-bid query deadline from RFP].
⚠ Confirm the submission deadline and method from the RFP before sending.
```

Aim for 8–20 questions. Fewer is better — every question should be genuinely necessary.
Questions should be professional, factual, and non-adversarial in tone.

Tell the user the file was saved and remind them to check the pre-bid query deadline.
