Fill a form or annexure from the RFP using company data, on company letterhead with signature.

**Arguments:** `$ARGUMENTS` (format: `<slug> <annexure name or number>`)

## What you do

1. **Parse the arguments:**
   - First word = slug
   - Rest = annexure identifier
   - If no annexure given: read `bids/<slug>/parsed/rfp.md`, list all annexures found, and ask which to fill.

2. **Read the annexure** from `bids/<slug>/parsed/rfp.md`. Extract every field, table row, instruction, and note about required attachments or signatures.

3. **Read company data:**
   - `company/company-info.json` — identity, registration, financials, signatory
   - `company/about/*.md` — narrative fields
   - `company/experience/*.md` — if the form has a project/reference table
   - List files in `company/documents/` — to know what attachments exist

4. **Map every field** to company data:
   - Data available → fill it
   - Data missing → write `[MISSING — add to company-info.json: <field name>]`
   - Needs an attachment → note `[ATTACH: <document from company/documents/>]`
   - Needs stamp paper / notarisation → mark `⚠ MANUAL ACTION REQUIRED`

5. **Generate the Word document** using the toolkit:

```python
import sys, subprocess
# Ensure dependency
subprocess.run(["pip", "install", "python-docx", "--break-system-packages", "-q"], capture_output=True)

sys.path.insert(0, ".")
from toolkit import docx_builder as db, bidder_profile as bp, paths

profile = bp.load_profile()
bid = paths.bid_dir("<slug>")

body = db.heading("[Annexure Title from RFP]")
# Build each field/table based on what the RFP form requires
# Use profile.legal_name, profile.registration_no, profile.signatory_name, etc.
# For tables: db.table([col_widths], [db.tr(db.tc(...), ...), ...])
body += db.sign_block()

db.build_docx(body, bid / "outputs/docx/[AnnexureName].docx")
```

6. **Tell the user:**
   "Done. I've filled [Annexure name] and saved it to `bids/<slug>/outputs/docx/[filename].docx`.

   Fields filled: [n]
   Fields I couldn't fill: [list them — user needs to add to company-info.json]
   ⚠ Manual actions needed: [list any stamp paper / CA certificate / wet signature items]"
