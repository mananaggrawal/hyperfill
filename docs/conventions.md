# Conventions

Rules that keep every bid consistent and submittable.

## Signing & stamping

- The authorised signatory is defined in `.rfp-kit/company-info.json`, read via
  `bidder_profile.AUTHORISED_SIGNATORY`. Their signature + company stamp is
  the image auto-detected from `company/`.
- Any generated document needing a signature uses `docx_builder.sign_block()`,
  which inserts the image and the signatory's name/designation from the
  profile, under a relationship ID that's guaranteed free in that specific
  letterhead (never a hardcoded ID, to avoid colliding with an existing logo).
- If a bid-opening representative signs/carries certain documents, use
  `bidder_profile.BID_OPENING_REP`.
- Before physical submission, every page of annexures and supporting documents
  is signed and stamped; supporting copies are self-attested where required.

## Letterhead

Generated documents are built on the first `.docx` found in `company/` (logo,
header, footer). The builder injects content before the section properties so
the letterhead is preserved exactly.

## Manual-action items (cannot be fully auto-generated)

Always flag these in the bid's hidden `checklist.md`:

| Item | Why it's manual |
|------|-----------------|
| Integrity pacts, NDAs, certain undertakings | Must be printed on the required stamp paper and wet-signed / notarised. |
| Externally-issued certificates | Must come from the issuer (e.g. an accountant's certificate with a unique registration/UDIN-style number) on their letterhead. |
| Counter-signatures | Require the other party's (e.g. the buyer's) signature too. |
| Fees / EMD | External payment or a valid exemption certificate. |
| Witness signatures | Physical witnesses where the form demands them. |

Generate the **draft/format** so the human has something to print — never
treat these as final.

## Single source of truth

- Identity numbers, addresses, signatory, financials, escalation matrix live
  **once** in `.rfp-kit/company-info.json` (read by `.toolkit/bidder_profile.py`).
  Update there and regenerate — always through `bidder_profile.save()`, which
  keeps a backup of the previous version.
- Don't hard-code these into individual documents. Read from `bidder_profile`.
- Verify financial figures against the audited statements you attach before
  each submission.

## Addenda & corrigenda

RFPs frequently get amended after publication. When one arrives:
- Parse it separately — don't overwrite the original `parsed/rfp.md`.
- Reconcile it clause-by-clause against the original extract and against
  `checklist.md`, and call out exactly what changed (new deadline, revised
  scope, etc.) rather than silently updating anything.

## Files & folders

- Bid slug: `<org>-<type>-<year>`, lowercase, hyphenated.
- No spaces in new filenames; use underscores or hyphens.
- Per-bid working files stay under `.rfp-kit/bids/<slug>/` (hidden); per-bid
  deliverables stay under `bids/<slug>/outputs/` (user-visible). Generic
  folders (`company/`, `.toolkit/`) stay clean of bid-specific content.

## Measurements (WordprocessingML)

- Font `sz` is in half-points (`sz="22"` ≈ 11pt). Table widths use DXA (twips,
  1/20 pt). The helpers handle the XML; you pass integers.
