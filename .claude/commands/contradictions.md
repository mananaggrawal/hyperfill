Find contradictions and inconsistencies within the RFP.

**Arguments:** `$ARGUMENTS` (the bid slug)

## Steps

1. Read `bids/$ARGUMENTS/parsed/rfp.md` in full — do not skim.

2. Do multiple passes looking for each type of contradiction below.

## What to look for

### Scope contradictions
- Scope of work described differently in different sections (e.g. Section 2 says X but Annexure A says Y)
- Technical specifications that conflict with the functional requirements
- Deliverables listed in one place but not another

### Timeline contradictions
- Conflicting deadlines (e.g. submission date in the notice vs. in the terms)
- Implementation timeline in scope that is incompatible with the contract duration
- Pre-bid query deadline after the submission date

### Eligibility contradictions
- Eligibility criteria stated differently in different sections
- Qualification requirements that contradict each other (e.g. must be an MSME and must have turnover > ₹500 Cr)

### Commercial contradictions
- EMD / bid security amount stated differently in different places
- Payment terms described inconsistently
- Price basis (inclusive/exclusive of tax) stated differently

### Technical contradictions
- Conflicting technical specifications (e.g. uptime of 99.9% in one place and 99.5% in another)
- Contradictory data requirements
- Conflicting compliance standards referenced

### Format / submission contradictions
- Number of copies required stated differently
- Submission address or portal stated differently
- Document format requirements that conflict

## Output

Write to `bids/$ARGUMENTS/analysis/contradictions.md`:

```markdown
# Contradictions Found — [RFP Name]
**Date:** [today]
**Total contradictions found:** [n]

---

## Contradiction 1 — [Type]
**Statement A:** Section [X.X] says: "[exact quote]"
**Statement B:** Section [Y.Y] says: "[exact quote]"
**Impact:** [What this means for the bidder — which version to follow?]
**Recommended action:** Raise as a pre-bid query (see /prebid)

---

[Repeat for each contradiction]

---

## Summary table
| # | Type | Sections | Impact | Action |
|---|---|---|---|---|
```

If no contradictions are found, say so clearly: "No contradictions found. The RFP appears internally consistent."

Tell the user how many were found and suggest running `/prebid $ARGUMENTS` to generate clarification questions.
