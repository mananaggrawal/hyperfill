# Changelog

## Unreleased — rename to Hyperfill + pre-release audit

- **Renamed the project to Hyperfill** across README, CLAUDE.md, AGENTS.md, docs, and
  package metadata.
- **Fixed a real import bug:** the documented pattern for loading the toolkit
  (`sys.path.insert(...)` + `from toolkit import ...`) can never work, because the
  package directory is `.toolkit/` — a leading dot, which standard Python import
  resolution cannot match against the name `toolkit`. Every doc referencing this
  pattern (`.toolkit/README.md`, `CLAUDE.md`, `AGENTS.md`) now documents the correct
  `importlib.util.spec_from_file_location(...)` bootstrap, verified working end-to-end
  against the real toolkit modules.
- Renamed the internal generated-image filename prefix (`claude_rfp_kit_image*.png` →
  `hyperfill_image*.png`) for consistency with the rename.
- Minor formatting fixes in `docs/repo-structure.md`'s folder tree.

## Unreleased — FOSS release readiness

- **Fixed `.gitignore`:** `docs/` and `examples/` were being ignored entirely, so
  none of the user-facing guides were ever actually published to GitHub despite
  being referenced from `README.md`. Also added `onboarding-guides/` and
  `.claude/` to the ignore list — internal/company material and local editor
  settings that must never be committed.
- **Removed hardcoded company examples:** `CLAUDE.md` and `xlsx_builder.py`
  referenced a real company name in example text; replaced with a generic
  placeholder so the kit reads as a template for any user.
- **LICENSE:** filled in the copyright holder.
- **README.md:** added badges, a "who this is for" section, and links to the
  new CONTRIBUTING.md and CODE_OF_CONDUCT.md.
- **Added CONTRIBUTING.md and CODE_OF_CONDUCT.md** for external contributors.

## Unreleased — consistency & reliability pass

Fixed a split-brain in the kit where AGENTS.md, `docs/`, and `.toolkit/cli.py`
described an older, different folder model than CLAUDE.md and `paths.py`
actually implement. Standardised everything on the hidden-`.rfp-kit/` model.

- **Structure:** Migrated in-progress bid working files (parsed RFP, analysis,
  checklist) into `.rfp-kit/bids/<slug>/`, and submission packages into
  `bids/<slug>/outputs/submission/`, so every bid folder now matches the
  documented two-folder model (`source/`, `outputs/`).
- **AGENTS.md:** Rewritten to match CLAUDE.md — removed slash commands and the
  old visible `company/letterhead/`, `company/documents/` subfolder model.
- **Removed `.toolkit/cli.py` and `setup.sh`:** the `rfpkit` CLI contradicted
  the "no scripts to run" model, referenced path helpers that no longer exist
  (`DOCUMENTS_DIR`, `BID_TEMPLATE`), and described a `company/` subfolder
  structure that never matched `paths.py`. Claude now calls the toolkit
  modules directly.
- **`docx_builder.py`:** Fixed a bug where the signature image was always
  embedded under a hardcoded `rId9` — if a letterhead already used that
  relationship ID for its own logo, the signature would silently bind to the
  wrong image. Now scans the letterhead's actual relationships and picks a
  genuinely free ID and media filename every time.
- **`bidder_profile.py`:** Schema expanded to match the fields actually in use
  (CIN, TAN, certifications, industry sector, banking details, go/no-go
  preferences). Added `save()`, which backs up the previous
  `company-info.json` before writing a new one. Completed the `_Profile`
  dot-access wrapper, which was missing several fields.
- **`paths.py`:** Added `company_doc()` and `experience_proof()` — referenced
  by the docs but never implemented.
- **New `xlsx_builder.py`:** many commercial RFPs need Excel annexures (BOQs,
  pricing sheets, pre-bid query formats), not just Word documents. Supports
  both filling an RFP-supplied template and building a new sheet from scratch.
- **CLAUDE.md:** added guidance for handling addenda/corrigenda without
  clobbering the original parsed RFP, a note on scanned/OCR-only PDFs, and
  wired `pdf_tools.merge()`/`to_pdf()` into the submission-assembly step for
  RFPs that require a single combined PDF.
- **README.md:** corrected the privacy claim — data is still sent to
  Anthropic's API as part of any Claude conversation; what the kit guarantees
  is that nothing is committed to git or uploaded elsewhere.
