# Workflow — RFP to submission

The end-to-end process for one RFP/RFE/tender. Everything for a bid lives in
`bids/<slug>/`.

## Step 0 — Create the bid folder

```bash
rfpkit new <org>-<type>-<year>      # e.g. acme-bank-rfp-2026
```

This copies `bids/_template/` and gives you:

```
bids/<slug>/
├── README.md          # bid name, reference no., deadlines, status
├── checklist.md       # the live requirements tracker
├── source/            # original RFP file(s)
├── parsed/            # RFP converted to Markdown
├── outputs/
│   ├── docx/          # generated/filled annexures + proposal (editable)
│   └── pdf/, pdf/combined/   # rendered PDFs, and annexure+attachments merged
└── submission/        # final, organised package ready to submit
```

## Step 1 — Parse the RFP

Put the original in `source/`. Convert to Markdown into `parsed/`:
- PDF → `pdfplumber` / `pdftotext` (keeps tables/structure).
- DOCX → read `word/document.xml` or a docx reader.

## Step 2 — Build the checklist

From the parsed RFP, capture **everything that must be submitted or done** in `checklist.md`:
eligibility criteria; every annexure/form and what it needs; fees/EMD and exemptions;
formatting & collation rules; packaging & submission steps; deadlines; and **manual-action
flags** (stamp paper and its value, notarisation, externally-issued certificates, counter-
signatures, payments). Track status per item.

## Step 3 — Fill annexures & draft the proposal

Use the toolkit; pull facts from `bidder_profile` (never re-type them).

```python
import sys; sys.path.insert(0, ".")            # repo root
from toolkit import docx_builder as db, bidder_profile as p, paths

body = db.heading("Annexure-5") + db.heading("Details of Offices", size=24, after=200)
rows = [db.tr(db.tc(500,"S.No",bold=True,fill="D9D9D9"),
              db.tc(3000,"Address",bold=True,fill="D9D9D9"),
              db.tc(2000,"Contact",bold=True,fill="D9D9D9"))]
for i, o in enumerate(p.OFFICES, 1):
    rows.append(db.tr(db.tc(500,str(i)), db.tc(3000,o["address"]),
                      db.tc(2000,f'{o["contact"]}\n{o.get("phone","")}')))
body += db.table([500,3000,2000], rows) + db.sign_block()

db.build_docx(body, paths.bid_dir("<slug>") / "outputs/docx/Annexure5.docx")
```

For the **response proposal** (narrative), draw from `company/about/` (and any
external proposal library you linked in `company/about/README.md`).

## Step 4 — Convert to PDF

```python
from toolkit import pdf_tools
pdf_tools.to_pdf(".../outputs/docx/Annexure5.docx", ".../outputs/pdf")
```

## Step 5 — Merge supporting documents

For each annexure that travels with attachments, merge in the order the RFP specifies:

```python
from toolkit import pdf_tools, paths
pdf_tools.merge(
    [ ".../outputs/pdf/Annexure2.pdf",
      paths.company_doc("<your-incorporation>.pdf"),
      paths.company_doc("<your-tax-id>.pdf") ],
    ".../outputs/pdf/combined/Annexure2_Combined.pdf",
)
```

Record which attachments belong with which annexure in the checklist.

## Step 6 — Assemble the submission

Build `submission/` exactly as the RFP requires — many tenders split into separate parts/
envelopes with precise super-scribing text; replicate it. Add an index and page numbering.

## Step 7 — Verify

Walk the checklist top to bottom: every required item present, on letterhead where required,
signed + stamped, attachments merged, and manual-action items flagged for the human
(stamp paper, notarisation, externally-issued certificates, counter-signatures, fees). Only
then is the bid ready to submit.
