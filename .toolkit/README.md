# Toolkit

Reusable, config-driven Python for generating bid documents. **No absolute paths** live
in these scripts — everything resolves relative to the repo root via `paths.py`, and your
letterhead/signature are auto-detected from `company/`, so the kit works wherever it's cloned.

## Modules

| Module | Purpose |
|--------|---------|
| `paths.py` | Repo-relative path resolver. Finds your letterhead (`company/letterhead/*.docx`) and signature (`company/signature/*.png`). |
| `bidder_profile.py` | Loads `company/company-info.json` and exposes your details to the toolkit. Fill the JSON via `rfpkit init`. |
| `docx_builder.py` | Letterhead-based DOCX builder + helpers (`para`, `heading`, `table`, `tr`, `tc`, `sign_block`). |
| `pdf_tools.py` | `to_pdf()` (DOCX→PDF via LibreOffice) and `merge()` (ordered PDF concatenation). |
| `cli.py` | The `rfpkit` command (`init`, `check`, `new`, `list`, `build-pdf`). |

## How a document gets built

1. **Compose the body** from helpers. Text is bid-specific; the plumbing isn't.
2. **`build_docx(body, out_path)`** clones your letterhead, injects the body before
   `<w:sectPr>`, embeds your signature/stamp as `rId9`, and repacks the `.docx`.
3. **`to_pdf(docx)`** renders it to PDF.
4. **`merge([...], out)`** appends the supporting documents for that annexure.

## Minimal example

```python
import sys; sys.path.insert(0, "/path/to/repo")     # repo root
from toolkit import docx_builder as db, bidder_profile as p, pdf_tools, paths

body = (
    db.heading("Annexure-2")
    + db.heading("General Detail of the Bidder", size=24, after=200)
    + db.table([2500, 4000], [
        db.tr(db.tc(2500, "Name of Bidder", bold=True), db.tc(4000, p.COMPANY["legal_name"])),
        db.tr(db.tc(2500, "Registration No.", bold=True), db.tc(4000, p.COMPANY["registration_no"])),
        db.tr(db.tc(2500, "Tax ID", bold=True), db.tc(4000, p.COMPANY["tax_id"])),
    ])
    + db.sign_block()     # signature image + signatory pulled from bidder_profile
)

slug = "acme-bank-rfp-2026"
docx = db.build_docx(body, paths.bid_dir(slug) / "outputs/docx/Annexure2.docx")
pdf  = pdf_tools.to_pdf(docx)
pdf_tools.merge(
    [pdf, paths.company_doc("incorporation.pdf"), paths.company_doc("tax-id.pdf")],
    paths.bid_dir(slug) / "outputs/pdf/combined/Annexure2_Combined.pdf",
)
```

## Requirements

- Python 3.9+, `pypdf` (`pip install -e .` installs it).
- LibreOffice (`soffice`) on PATH for DOCX→PDF.

Run `rfpkit check` (or `python -m toolkit.cli check`) to confirm everything's in place.
