Create a new bid folder for an RFP.

**Arguments:** `$ARGUMENTS` (the bid slug, e.g. `acme-bank-rfp-2026`)

## What you do

1. **Get the slug.** It is: `$ARGUMENTS`
   - If blank, ask: "What would you like to name this bid? I'll use it as a folder name — something like `acme-bank-2026` works well."
   - Good format: buyer name + year, lowercase, hyphens only. Keep it short.

2. **Check it doesn't already exist.** If `bids/$ARGUMENTS/` exists, say: "A folder for '$ARGUMENTS' already exists. Want to continue working in it, or use a different name?"

3. **Create the folder structure:**
   ```
   bids/$ARGUMENTS/
   ├── source/       ← user will upload RFP here
   ├── parsed/       ← /parse will create rfp.md here
   ├── analysis/     ← analysis outputs go here
   ├── outputs/
   │   ├── docx/     ← generated Word documents
   │   └── pdf/      ← PDF versions
   └── submission/   ← final package
   ```

4. **Write `bids/$ARGUMENTS/README.md`:**
   ```markdown
   # Bid: $ARGUMENTS

   | Field | Value |
   |---|---|
   | Buyer / Issuer | _(fill in)_ |
   | Reference number | _(fill in)_ |
   | Submission deadline | _(fill in)_ |
   | EMD / Bid fee | _(fill in)_ |
   | Status | In progress |
   ```

5. **Write `bids/$ARGUMENTS/checklist.md`:**
   ```markdown
   # Checklist — $ARGUMENTS

   Run `/parse $ARGUMENTS` to populate this list automatically.

   | # | Item | Status | Notes |
   |---|---|---|---|
   ```

6. **Confirm to the user:**
   "Done! Folder `bids/$ARGUMENTS/` is ready.

   **Next:** Upload the RFP PDF into `bids/$ARGUMENTS/source/`, then come back and run:
   `/parse $ARGUMENTS`"
