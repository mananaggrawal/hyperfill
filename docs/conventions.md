# Conventions

Rules that keep every bid consistent and submittable.

## Signing & stamping

- The authorised signatory is defined in `bidder_profile.AUTHORISED_SIGNATORY`. Their
  signature + company stamp is the image in `assets/signature-stamp/`.
- Any generated document needing a signature uses `docx_builder.sign_block()`, which inserts
  the image and the signatory's name/designation from the profile.
- If a bid-opening representative signs/carries certain documents, use
  `bidder_profile.BID_OPENING_REP`.
- Before physical submission, every page of annexures and supporting documents is signed and
  stamped; supporting copies are self-attested where required.

## Letterhead

Generated documents are built on the `.docx` in `assets/letterhead/` (logo, header, footer).
The builder injects content before the section properties so the letterhead is preserved.

## Manual-action items (cannot be fully auto-generated)

Always flag these in the bid's `checklist.md`:

| Item | Why it's manual |
|------|-----------------|
| Integrity pacts, NDAs, certain undertakings | Must be printed on the required stamp paper and wet-signed / notarised. |
| Externally-issued certificates | Must come from the issuer (e.g. an accountant's certificate with a unique registration/UDIN-style number) on their letterhead. |
| Counter-signatures | Require the other party's (e.g. the buyer's) signature too. |
| Fees / EMD | External payment or a valid exemption certificate. |
| Witness signatures | Physical witnesses where the form demands them. |

Generate the **draft/format** so the human has something to print — never treat these as final.

## Single source of truth

- Identity numbers, addresses, signatory, financials, escalation matrix live **once** in
  `toolkit/bidder_profile.py` and `company-knowledge/master-data.md`. Keep them in sync.
- Don't hard-code these into individual scripts. Import from `bidder_profile`.
- Verify financial figures against the audited statements you attach before each submission.

## Files & folders

- Bid slug: `<org>-<type>-<year>`, lowercase, hyphenated.
- No spaces in new filenames; use underscores or hyphens.
- Per-bid work stays under `bids/<slug>/`. Generic folders stay clean.

## Measurements (WordprocessingML)

- Font `sz` is in half-points (`sz="22"` ≈ 11pt). Table widths use DXA (twips, 1/20 pt).
  The helpers handle the XML; you pass integers.
