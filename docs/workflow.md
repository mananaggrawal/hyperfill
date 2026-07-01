# Workflow — RFP to submission

The full sequence from receiving an RFP to a ready-to-submit package.
Each step corresponds to a Claude Code slash command.

**Multiple RFPs at once?** No problem — each bid has its own folder under `bids/`.
Run commands with the specific slug and they won't interfere with each other.

---

## Step 1 — Create the bid folder

```
/new acme-bank-rfp-2026
```

Pick a slug: `buyername-type-year`, all lowercase, hyphens only.
This creates `bids/acme-bank-rfp-2026/` with all the right subfolders.

Then **upload the RFP PDF** to `bids/acme-bank-rfp-2026/source/`.

---

## Step 2 — Parse the RFP

```
/parse acme-bank-rfp-2026
```

Converts the PDF to readable text at `bids/.../parsed/rfp.md`.
Claude also builds an initial checklist from the extracted requirements.

---

## Step 3 — Go / No-Go decision

```
/go-nogo acme-bank-rfp-2026
```

Claude checks your eligibility against every criterion in the RFP and scores
technical fit, commercial attractiveness, and risk. Output saved to `analysis/go-nogo.md`.

Share this with management before investing further effort.

---

## Step 4 — Tender synopsis

```
/synopsis acme-bank-rfp-2026
```

Produces a one-page summary: buyer, deadline, value, scope, evaluation method, key contacts.
Saved to `analysis/synopsis.md`. Good for briefing the team.

---

## Step 5 — Risk analysis

```
/risks acme-bank-rfp-2026
```

Scans every clause for penalty rates, IP transfer, unlimited liability, unreasonable SLAs,
and other red flags. Each risk is quoted exactly and rated High / Medium / Note.
Saved to `analysis/risks.md`.

---

## Step 6 — Find contradictions

```
/contradictions acme-bank-rfp-2026
```

Reads the entire RFP and finds where it contradicts itself — conflicting deadlines,
inconsistent specifications, scope described differently in different sections.
Saved to `analysis/contradictions.md`.

---

## Step 7 — Pre-bid clarification questions

```
/prebid acme-bank-rfp-2026
```

Drafts a formal list of questions to submit to the buyer — drawn from contradictions,
vague scope, missing specs, and risky clauses. Saved to `analysis/prebid-questions.md`.

Submit these before the pre-bid query deadline stated in the RFP.

---

## Step 8 — Search the RFP

```
/search acme-bank-rfp-2026 payment terms
/search acme-bank-rfp-2026 SLA requirements
```

Find specific information in the RFP at any point in the process.

---

## Step 9 — Fill forms and annexures

```
/fill acme-bank-rfp-2026 annexure-3
```

Claude reads the annexure, maps every field to your company data, and generates a
filled Word document in `outputs/docx/`. Fields without data are flagged clearly.

Run this for each annexure the RFP requires.

---

## Step 10 — Draft the proposal

```
/draft acme-bank-rfp-2026 tech
/draft acme-bank-rfp-2026 commercial
```

Drafts the technical and commercial proposal using your company capabilities,
past experience, and the RFP requirements. Saved to `outputs/docx/`.

**Review carefully before submission** — fill in any `[PRICE TBD]` placeholders
and have your team validate the technical content.

---

## Step 11 — Assemble and submit

1. Convert all DOCX to PDF (Claude Code can do this, or use LibreOffice directly)
2. Merge annexures with their required attachments
3. Organise the `submission/` folder exactly as the RFP specifies
4. Walk through `checklist.md` — every item must be ticked before submitting
5. Flag all `⚠ MANUAL ACTION REQUIRED` items to the relevant person

---

## Working on multiple RFPs simultaneously

Each bid is fully isolated in its own `bids/<slug>/` folder.
You can have 10 bids in progress at once — just specify the slug in each command.

To see all active bids:
```
python -m toolkit.cli list
```
