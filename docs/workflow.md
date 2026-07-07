# Workflow — RFP to submission

The full sequence from receiving an RFP to a ready-to-submit package. Everything
here happens conversationally in plain English — there are no slash commands and
no CLI. Tell Claude what you want (or pick a lettered option from its menu) and
it does the rest.

**Multiple RFPs at once?** No problem — each bid has its own folder under
`bids/`. Mention the buyer's name (or the slug) and Claude keeps them isolated.

---

## Step 1 — Start a new bid

Tell Claude the buyer's name: *"I have a new RFP from Acme Bank."*

Claude creates `bids/acme-bank-rfp-2026/source/` and `outputs/submission/`
(and the hidden `.rfp-kit/bids/acme-bank-rfp-2026/` working folder), opens the
source folder, and asks you to drop the RFP PDF in.

---

## Step 2 — Parse the RFP

Say the PDF is in, and Claude reads it natively and writes a structured
extract to the hidden `.rfp-kit/bids/<slug>/parsed/rfp.md`, plus an initial
`checklist.md` of every requirement found.

If a corrigendum or addendum arrives later, drop it in `source/` too and tell
Claude — it parses it separately and reconciles it against the original
extract and checklist, flagging exactly what changed rather than silently
overwriting anything.

---

## Step 3 — Go / No-Go decision

Ask *"should we bid on this?"* Claude checks your eligibility against every
criterion in the RFP and scores technical fit, commercial attractiveness, and
risk. Share the result with management before investing further effort.

---

## Step 4 — Tender synopsis

Ask for a one-page summary: buyer, deadline, value, scope, evaluation method,
key contacts. Good for briefing the team.

---

## Step 5 — Risk analysis

Ask Claude to flag risky clauses. It scans every clause for penalty rates, IP
transfer, unlimited liability, unreasonable SLAs, and other red flags — each
quoted exactly and rated High / Medium / Note.

---

## Step 6 — Find contradictions

Ask Claude to find contradictions. It reads the entire RFP and surfaces where
it conflicts with itself — inconsistent deadlines, scope described differently
in different sections, and so on.

---

## Step 7 — Pre-bid clarification questions

Ask Claude to draft pre-bid questions — pulled from contradictions, vague
scope, missing specs, and risky clauses. Submit these before the pre-bid query
deadline stated in the RFP.

---

## Step 8 — Search the RFP

Ask any specific question — *"what does it say about payment terms?"* — at any
point in the process.

---

## Step 9 — Fill forms and annexures

Ask Claude to fill a specific annexure or form. It reads the annexure, maps
every field to your company data, and generates a filled document —
`.docx` via `.toolkit/docx_builder.py`, or `.xlsx` via `.toolkit/xlsx_builder.py`
for spreadsheet annexures like BOQs or pricing sheets — into `outputs/`.
Fields without data are flagged clearly, never guessed.

Run this for each annexure the RFP requires.

---

## Step 10 — Draft the proposal

Ask for the technical and/or commercial proposal. Claude drafts both using
your company capabilities, past experience, and the RFP requirements, saved
to `outputs/`.

**Review carefully before submission** — fill in any `[PRICE TBD]` placeholders
and have your team validate the technical content.

---

## Step 11 — Assemble and submit

Ask Claude to assemble the submission. It:
1. Matches every required enclosure to a file in `company/` or a generated
   output, and copies it into `outputs/submission/`.
2. Converts DOCX to PDF and merges supporting documents where the RFP requires
   a single combined PDF per annexure or bid part (via `.toolkit/pdf_tools.py`).
3. Organises `outputs/submission/` exactly as the RFP specifies (e.g. separate
   Eligibility/Technical/Commercial parts).
4. Generates a `MANIFEST.md` inside `outputs/submission/` — every required
   document, included or missing.
5. Flags every `⚠ MANUAL ACTION REQUIRED` item (stamp paper, wet signatures,
   bank transfers, notarisation) so nothing gets missed.

---

## Working on multiple RFPs simultaneously

Each bid is fully isolated in its own `bids/<slug>/` and `.rfp-kit/bids/<slug>/`
folder pair. You can have 10 bids in progress at once — just mention which one
you mean.
