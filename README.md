# RFP Kit — for Claude Code

Respond to RFPs, tenders, and RFEs using Claude Code. Drop in an RFP PDF, run a
slash command, get back analysis, filled forms, and a draft proposal — all on your
company letterhead, with your signature, using your real company data.

**Everything runs inside Claude Code. No other tools needed.**

---

## What it does

| Command | Output |
|---|---|
| `/setup-drive` | Finds your Google Drive, creates all folders, walks you through company setup |
| `/parse acme-bank-2026` | Reads the RFP PDF, extracts it to text, builds a requirements checklist |
| `/go-nogo acme-bank-2026` | Scores eligibility, technical fit, risk — recommends Go / No-Go |
| `/synopsis acme-bank-2026` | One-page brief: deadline, value, scope, evaluation method |
| `/risks acme-bank-2026` | Flags penalty clauses, IP transfer, unlimited liability, unreasonable SLAs |
| `/contradictions acme-bank-2026` | Finds where the RFP contradicts itself |
| `/prebid acme-bank-2026` | Drafts formal clarification questions to submit to the buyer |
| `/search acme-bank-2026 payment terms` | Finds any topic in the RFP instantly |
| `/fill acme-bank-2026 annexure-3` | Fills the form with your company data, signs it, puts it on letterhead |
| `/draft acme-bank-2026 tech` | Drafts the full technical or commercial proposal |

Multiple RFPs can be in progress simultaneously — each lives in its own folder.

---

## How to get started

**You need:** Claude Code. Nothing else.

```bash
git clone https://github.com/mananaggrawal/claude-rfp-kit
claude claude-rfp-kit
```

Claude Code reads the folder, checks what's set up, and tells you exactly what to do next.
If it's your first time, it walks you through your company profile conversationally — no forms, no config files.

Full setup guide: [`docs/setup.md`](docs/setup.md)

---

## How it works

```
company/          ←  your details, filled once, reused on every bid
  company-info.json
  about/          ←  what your company does (markdown files)
  experience/     ←  past project write-ups (one per project)
  documents/      ←  certificates, financials (PDFs)
  letterhead/     ←  your Word template (.docx)
  signature/      ←  your signature image (.png)

bids/
  acme-bank-2026/ ←  one folder per RFP
    source/       ←  drop the RFP PDF here
    parsed/       ←  Claude extracts text here
    analysis/     ←  go-nogo, synopsis, risks, etc.
    outputs/      ←  filled forms and proposals
    submission/   ←  final package
```

Claude Code reads your company data once and reuses it across every bid.
Your data never leaves your machine.

---

## Privacy

This repository contains no company data. Your certificates, financials, letterhead,
and bid documents are excluded from git by default — they only exist on your local
machine or Google Drive.

## License

MIT — see [LICENSE](LICENSE).
