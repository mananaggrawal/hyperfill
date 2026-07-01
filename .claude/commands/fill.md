Fill a form or annexure from the RFP using company data.

**Arguments:** `$ARGUMENTS` (format: `<slug> <annexure name or number>`)
Example: `/fill acme-bank-rfp-2026 annexure-3` or `/fill acme-bank-rfp-2026 "Company Profile Form"`

## Steps

1. Parse the arguments:
   - First word = slug
   - Remaining = annexure identifier
   - If annexure not specified, list all annexures found in `bids/<slug>/parsed/rfp.md` and ask which to fill.

2. Read `bids/<slug>/parsed/rfp.md` and find the specified annexure/form.
   - Extract every field, table, and instruction from it.
   - Note any instructions about format, signatures, stamps, or attachments.

3. Read company data:
   - `company/company-info.json`
   - `company/about/` (for narrative fields)
   - `company/experience/` (for project/reference tables)
   - `company/documents/` (to know what attachments are available)

4. Map each field to company data. For every field:
   - If data is available: fill it in
   - If data is missing: write `[MISSING — please add to company-info.json: <field name>]`
   - If field requires a document attachment: note `[ATTACH: <document name from company/documents/>]`

5. Generate the filled Word document using the toolkit:

```python
import sys
sys.path.insert(0, ".")
from toolkit import docx_builder as db, bidder_profile as bp, paths

profile = bp.load_profile()
bid = paths.bid_dir("<slug>")

# Build the document content based on the form structure found in the RFP
# Use db.heading(), db.paragraph(), db.table(), db.sign_block()
# Pull values from profile.* — never hardcode them

body = db.heading("[Annexure Title]")
# ... form content ...
body += db.sign_block(profile)

db.build_docx(body, bid / "outputs/docx/[AnnexureName].docx")
```

6. List any manual actions needed:
```
⚠ MANUAL ACTION REQUIRED:
- [Field X] requires a notarised declaration — this is a draft only
- [Field Y] requires the CA's signature with UDIN — send the format to your CA
- [Document Z] is not in company/documents/ — please upload it
```

7. Tell the user:
   "✓ [Annexure name] filled and saved to bids/<slug>/outputs/docx/[filename].docx

   Fields filled: [n]
   Fields missing: [n] — see MISSING markers in the document
   Manual actions: [n] — listed above"
