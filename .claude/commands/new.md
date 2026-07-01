Create a new bid folder for an RFP.

**Arguments:** `$ARGUMENTS` (the bid slug, e.g. `acme-bank-rfp-2026`)

## Steps

1. The slug is: `$ARGUMENTS`
   - If no slug was provided, ask: "What would you like to name this bid? Use lowercase with hyphens, e.g. `acme-bank-rfp-2026`."
   - A good slug is: buyer name + type + year, all lowercase, hyphens only.

2. Check that `bids/$ARGUMENTS/` does not already exist. If it does, say "A bid folder for '$ARGUMENTS' already exists."

3. Create this folder structure under `bids/$ARGUMENTS/`:
   - `source/` — user will drop the RFP PDF here
   - `parsed/` — /parse will populate this
   - `analysis/` — analysis commands populate this
   - `outputs/docx/` — generated Word documents
   - `outputs/pdf/` — generated PDFs
   - `submission/` — final package

4. Write `bids/$ARGUMENTS/README.md`:

```
# Bid: $ARGUMENTS

| Field | Value |
|---|---|
| Buyer / Issuer | _(fill in)_ |
| Reference number | _(fill in)_ |
| Submission deadline | _(fill in)_ |
| EMD / Bid fee | _(fill in)_ |
| Status | In progress |

## Notes
_(Add notes here)_
```

5. Write `bids/$ARGUMENTS/checklist.md`:

```
# Requirements Checklist — $ARGUMENTS

Run /parse then /synopsis to populate this checklist.

| # | Requirement | Status | Notes |
|---|---|---|---|
```

6. Confirm to the user:
   "✓ Bid folder created at bids/$ARGUMENTS/.

   Next step: Upload the RFP PDF into bids/$ARGUMENTS/source/, then run:
   /parse $ARGUMENTS"
