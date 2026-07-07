# Knowledge base guide

Two places hold everything reusable about your organisation. Pull from them;
don't re-type facts or re-create documents that already exist.

## company/ — the flat drop zone (user-visible)

Drop anything you'd attach to a bid here — letterhead, signature/stamp image,
registration/incorporation documents, tax registrations, audited financials,
certifications (ISO/PCI/etc.), banking details, client agreements, completion
certificates. No subfolders to sort into — Claude auto-detects file types by
content, not by which folder they're in.

Reach a specific file from code via `paths.company_doc("gst")` (matches by
filename fragment, case-insensitive).

## .rfp-kit/company-info.json — your details (hidden)

The single source of truth for corporate identity, signatory, offices,
escalation matrix, financials, banking details, and go/no-go preferences. You
never edit this file directly — tell Claude what's wrong or what's new and it
updates the JSON for you, keeping a backup of the previous version
(`.rfp-kit/company-info.backup.json`) so a bad extraction can always be
undone. The toolkit reads it via `.toolkit/bidder_profile.py`, so facts live
in **one place** and every generated document stays consistent.

## .rfp-kit/experience/ — proof of past work (hidden)

Short write-ups of client agreements, purchase orders, completion/satisfaction
certificates (include client name + contact where the RFP asks). Reach them
via `paths.experience_proof("client-name")`.

## .rfp-kit/about/ — narrative & reference text (hidden)

Material for writing the response **proposal** and descriptive annexures:
company deck, business plan, technical write-ups, security/ISMS posture.

## Keeping it current

When a new certificate, audit report, or agreement arrives, drop it in
`company/`, and tell Claude what fact it changes — it updates
`.rfp-kit/company-info.json` (with a backup) rather than you editing JSON by
hand.
