Produce a one-page RFP summary for internal stakeholders.

**Arguments:** `$ARGUMENTS` (the bid slug)

## Steps

1. Read `bids/$ARGUMENTS/parsed/rfp.md`.
2. Extract the following information precisely — do not guess or fill in placeholders if information is not present; write "Not stated in RFP" instead.

## Output

Write to `bids/$ARGUMENTS/analysis/synopsis.md`:

```markdown
# Tender Synopsis — [RFP/Tender Name]

| Field | Detail |
|---|---|
| Issuing authority | |
| Tender / RFP reference no. | |
| Tender type | (Open / Limited / Single-source) |
| Scope of work | (2–3 sentence summary) |
| Estimated contract value | |
| Contract duration | |
| Submission deadline | |
| Pre-bid meeting / query deadline | |
| EMD / Bid security | Amount + form (DD / BG / online) |
| Performance security | Amount + timeline |
| Eligibility snapshot | (key criteria in one line each) |
| Evaluation method | (L1 / QCBS / marks-based — summarise weightage) |
| Submission method | (online portal / physical / email) |
| Key annexures / forms required | (bullet list) |
| Key contacts | Name, email, phone |

## Scope summary
[One paragraph describing exactly what the buyer wants delivered]

## Commercial highlights
[Payment terms, milestone structure, penalties, price validity]

## Our fit in one line
[Single sentence: why we are / are not a strong fit]

## Immediate actions required
| Action | Owner | By when |
|---|---|---|
| Upload RFP source documents | Bid manager | Immediately |
| Go/No-Go decision | Management | [date] |
| Pre-bid query submission | Bid team | [date from RFP] |
| Bid submission | Bid team | [deadline] |
```

Tell the user the file has been saved to `bids/$ARGUMENTS/analysis/synopsis.md`.
