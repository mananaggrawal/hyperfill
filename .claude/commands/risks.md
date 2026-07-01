Find and flag risky clauses in the RFP.

**Arguments:** `$ARGUMENTS` (the bid slug)

## Steps

1. Read `bids/$ARGUMENTS/parsed/rfp.md` in full.
2. Scan every clause for the risk categories below.
3. Quote the exact clause text, not a paraphrase.

## Risk categories to scan for

### 🔴 HIGH — These can cause major financial or legal exposure
- **Liquidated damages / penalties:** any clause specifying penalties for delay or non-performance. Note the rate (e.g. 0.5% per week), cap, and trigger conditions.
- **Unlimited liability:** clauses that do not cap the bidder's total liability.
- **Termination for convenience:** buyer can cancel with no compensation to bidder.
- **IP ownership transfer:** buyer claims ownership of all IP created during the contract.
- **Unilateral variation:** buyer can change scope/price without bidder's consent.
- **Payment terms beyond 60 days:** delayed payment with no interest on late payment.

### 🟡 MEDIUM — Significant but manageable
- **Performance / uptime SLAs:** note the required % and penalty for breach.
- **Retention money:** amount withheld and release conditions.
- **Price escalation clause absent:** fixed price for long-duration contracts.
- **Data localisation / residency:** restrictions on where data is stored/processed.
- **Exclusivity clauses:** prohibiting work with competitors during/after the contract.
- **Warranty periods beyond 12 months:** extended defect liability.
- **Key personnel lock-in:** buyer can reject substitution of named personnel.

### 🟢 NOTE — Worth flagging but lower risk
- **Insurance requirements:** types and coverage amounts required.
- **Audit rights:** buyer's right to audit systems, financials, or subcontractors.
- **Governing law / dispute resolution:** jurisdiction, arbitration vs. litigation.
- **Subcontracting restrictions:** limitations on using subcontractors.
- **Force majeure definition:** what events are covered.

## Output

Write to `bids/$ARGUMENTS/analysis/risks.md`:

```markdown
# Risk Analysis — [RFP Name]
**Date:** [today]

## 🔴 High Risk Clauses
### [Risk type]
**Clause reference:** [Section X.X]
**Exact text:** "[quote]"
**Risk:** [Why this is problematic]
**Recommended action:** [What to do — negotiate, seek clarification, price in, or flag to management]

---

## 🟡 Medium Risk Clauses
[Same format]

## 🟢 Notes
[Same format]

## Summary
| Risk | Severity | Recommended action |
|---|---|---|
```

After saving, summarise the top 3 risks to the user in plain language.
