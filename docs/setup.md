# Setup — make the kit yours

Do this once. After it, every bid reuses what you entered here.

## 1. Install

```bash
pip install -e .          # installs the `rfpkit` command and pypdf
```

Install **LibreOffice** too (provides `soffice` for DOCX→PDF). Python 3.9+ required.

## 2. Fill in your organisation

Run the guided wizard — it asks questions and writes the file for you (no code editing):

```bash
rfpkit init
```

It fills **`company/company-info.json`** with your identity, signatory, offices, and
financials. Prefer to type it yourself? Just open that JSON file and fill the blanks.
You can re-run `rfpkit init` any time to update — it pre-fills your current values.

## 3. Add your assets

- **`company/letterhead/`** — drop your letterhead as a `.docx`. Generated documents are
  built on top of it (logo, header, footer preserved). The toolkit auto-detects the file.
- **`company/signature/`** — drop the authorised signatory's signature + company
  stamp as a single image (PNG/JPG). It's inserted wherever a signature is needed.

## 4. Add your documents

- **`company/documents/`** — registration/incorporation,
  tax registrations, audited financials, certifications (ISO/PCI/etc.), and any standing proof
  you attach to bids.
- **`company/experience/`** — client agreements,
  purchase orders, completion/satisfaction certificates that prove past experience.
- **`company/about/`** — narrative material (company deck, business plan,
  technical/security write-ups) used to draft the response proposal.

## 5. (Optional) Link an external proposal library

If you keep product/solution proposals in another folder, record its location in
`company/about/README.md` so agents read the latest versions directly.

## 6. Verify

```bash
rfpkit check
```

Resolve any ⚠️ items. Once it reports ready, scaffold your first bid with
`rfpkit new <slug>` and follow [`workflow.md`](workflow.md).
