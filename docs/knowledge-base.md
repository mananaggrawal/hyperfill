# Knowledge base guide

The single `company/` folder holds everything reusable about your organisation. Pull
from it; don't re-type facts or re-create documents that already live here. It ships
empty — [`setup.md`](setup.md) walks through filling it.

## company-info.json — your details

The single source of truth for corporate identity, signatory, offices, escalation matrix,
and financials. Fill it with `rfpkit init` (a guided wizard) or by editing the file
directly — it's plain JSON. The toolkit reads it via `toolkit/bidder_profile.py`, so you
maintain facts in **one place** and regenerate.

## letterhead/ and signature/

- **letterhead/** — your letterhead `.docx`. Generated documents are built on it.
- **signature/** — the authorised signatory's signature + company stamp image, inserted
  automatically wherever a signature is required.

Both are auto-detected — just drop the file in; no filename to configure.

## documents/ — the documents you attach

Registration/incorporation, tax registrations, audited financials, certifications
(ISO/PCI/etc.), banking details, authorisations. Reach them from code via
`paths.company_doc("...")`.

## experience/ — proof of past work

Client agreements, purchase orders, completion/satisfaction certificates (include client
name + contact where the RFP asks). Reach them via `paths.experience_proof("...")`.

## about/ — narrative & reference text

Material for writing the response **proposal** and descriptive annexures: company deck,
business plan, technical write-ups, security/ISMS posture. If you keep product proposals
in a separate folder, note its path at the top of `company/about/README.md` and have the
agent read the latest versions from there.

## Keeping it current

When a new certificate, audit report, or agreement arrives, drop it in the right `company/`
subfolder, and update any fact it changes by re-running `rfpkit init` (or editing
`company/company-info.json`).
