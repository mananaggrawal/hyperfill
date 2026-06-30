# Setup — make the kit yours

Do this once. After it, every bid reuses what you entered here.

## 1. Install

```bash
pip install -e .          # installs the `rfpkit` command and pypdf
```

Install **LibreOffice** too (provides `soffice` for DOCX→PDF). Python 3.9+ required.

## 2. Fill in your organisation

- **`toolkit/bidder_profile.py`** — the machine-readable single source of truth.
  Fill `COMPANY`, `AUTHORISED_SIGNATORY`, `OFFICES`, `ESCALATION_MATRIX`, `FINANCIALS`,
  and (if needed) `BID_OPENING_REP`. Use the field names that match your country
  (registration number, tax IDs, etc.).
- **`company-knowledge/master-data.md`** — the human-readable copy of the same facts.
  Keep it in sync with `bidder_profile.py`.

## 3. Add your assets

- **`assets/letterhead/`** — drop your letterhead as a `.docx`. Generated documents are
  built on top of it (logo, header, footer preserved). The toolkit auto-detects the file.
- **`assets/signature-stamp/`** — drop the authorised signatory's signature + company
  stamp as a single image (PNG/JPG). It's inserted wherever a signature is needed.

## 4. Add your documents

- **`company-knowledge/submission-documents/company-documents/`** — registration/incorporation,
  tax registrations, audited financials, certifications (ISO/PCI/etc.), and any standing proof
  you attach to bids.
- **`company-knowledge/submission-documents/experience-proofs/`** — client agreements,
  purchase orders, completion/satisfaction certificates that prove past experience.
- **`company-knowledge/profile/`** — narrative material (company deck, business plan,
  technical/security write-ups) used to draft the response proposal.

## 5. (Optional) Link an external proposal library

If you keep product/solution proposals in another folder, record its location in
`company-knowledge/proposal-library.md` so agents read the latest versions directly.

## 6. Verify

```bash
rfpkit check
```

Resolve any ⚠️ items. Once it reports ready, scaffold your first bid with
`rfpkit new <slug>` and follow [`workflow.md`](workflow.md).
