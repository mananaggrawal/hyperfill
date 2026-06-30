# Knowledge base guide

`company-knowledge/` holds everything reusable about your organisation. Pull from it;
don't re-type facts or re-create documents that already live here. It ships empty —
[`setup.md`](setup.md) walks through filling it.

## master-data.md

The human-readable single source of truth — corporate identity, signatory, offices,
escalation matrix, financials. Its machine twin is `toolkit/bidder_profile.py`. **Keep
them in sync.**

## profile/ — narrative & reference text

Material for writing the response **proposal** and descriptive annexures: company deck,
business plan, technical write-ups, security/ISMS posture. Add whatever describes what
your company does and why it's credible.

## submission-documents/ — the documents you attach

- **company-documents/** — registration/incorporation, tax registrations, audited
  financials, certifications (ISO/PCI/etc.), banking details, authorisations.
- **experience-proofs/** — client agreements, purchase orders, completion/satisfaction
  certificates proving past experience (include client name + contact where the RFP asks).

Reach them from code via `paths.company_doc("...")` and `paths.experience_proof("...")`.

## proposal-library.md — optional external reference

If you keep product/solution proposals in a separate folder, record its path here so agents
read the latest versions directly (a live reference, not a copy).

## Keeping it current

When a new certificate, audit report, or agreement arrives, add it to the right
`submission-documents/` subfolder, and update any fact it changes in `master-data.md` +
`bidder_profile.py`.
