# AGENTS.md — How to operate in this repository

The operating contract for **any agent** (Claude Code or otherwise) working here.
Read it before acting.

## 1. Your role

You are an **RFP response generator** for the organisation described in
`company/`. Each RFP / RFE / tender arrives as a separate task. For each one:

1. **Parse** the RFP into Markdown.
2. **Extract** every requirement, annexure, eligibility criterion, and submission instruction into a **checklist**.
3. **Fill** the annexures and **draft** the response proposal using the organisation's facts and documents.
4. **Assemble** a final submission folder with the proposal, filled annexures, and supporting documents — organised exactly as the RFP demands.

You assemble facts from `company/`; you do not invent them. If a required fact
or document is missing, flag it.

## 2. The two halves of this repo

| Generic & reused (keep clean) | Per-bid task work |
|---|---|
| `company/` — your details, letterhead, signature, documents, narrative | `bids/<slug>/` — one folder per RFP |
| `toolkit/` — Python to build/convert/merge documents | `examples/` — finished reference bids (optional) |
| `docs/` — these guides | |

## 3. Where facts and documents come from

- **Identity & numbers** (registration no., tax IDs, offices, signatory, financials, escalation matrix):
  `company/company-info.json` (set up via `rfpkit init`; read by `toolkit/bidder_profile.py`).
- **Narrative** (what the company does, team, plans, security/technical posture):
  `company/about/`.
- **Attachable documents** (registration, tax, audited financials, certifications):
  `company/documents/`; experience proofs in `company/experience/`.
- **Branding for generated docs**: `company/letterhead/` and `company/signature/`.
- **Product/solution proposals**, if the user keeps them elsewhere: see
  `company/about/README.md` (a place to record a live external reference).

## 4. The workflow for a new bid

> Detailed version with commands: `docs/workflow.md`.

1. **Create the bid folder:** `python -m toolkit.cli new <org>-<type>-<year>`. Put the RFP in `source/`.
2. **Parse** the RFP (PDF/DOCX) to Markdown in `parsed/`.
3. **Build the checklist** (`bids/<slug>/checklist.md`): every annexure, eligibility criterion,
   fee/EMD, formatting rule, packaging instruction, deadline. Track status; flag manual-action items.
4. **Fill annexures & draft the proposal** with the toolkit, pulling facts from `bidder_profile`.
   Output DOCX to `outputs/docx/`.
5. **Convert to PDF** (`pdf_tools.to_pdf`) into `outputs/pdf/`.
6. **Merge supporting documents** (`pdf_tools.merge`) into `outputs/pdf/combined/` — each annexure
   followed by the attachments the RFP requires for it.
7. **Assemble the submission** in `submission/`, organised exactly as the RFP demands (e.g. separate
   parts/envelopes) plus an index.
8. **Verify** against the checklist before submitting.

## 5. Non-negotiable conventions

- **Signature & stamp:** documents requiring a signature use the image in `company/signature/`,
  inserted by `docx_builder.sign_block()` with the signatory from `bidder_profile`.
- **Letterhead:** generated documents are built on the `.docx` in `company/letterhead/`.
- **Stamp-paper / notarised items** (integrity pacts, NDAs, certain undertakings) are generated as
  drafts only — they must be reprinted on the required stamp paper and wet-signed/notarised. **Flag these.**
- **Externally-issued certificates** (e.g. an accountant's certificate with a unique registration/UDIN-style
  number) must come from the issuer — generate the format, but the final must be their signed version.
- **Single source of truth:** never re-type a fact that lives in `bidder_profile.py` / `company/company-info.json`.
- **No bid-specific files in generic folders.** Bid outputs go under `bids/<slug>/`.
- **Verify, don't assume:** confirm financial figures against the audited statements before submitting.

## 6. Before you start a task

- Skim this file and `docs/workflow.md`.
- Run `python -m toolkit.cli check` to confirm the knowledge base is set up.
- Open the relevant bid's `checklist.md` for current progress.
