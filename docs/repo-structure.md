# Repository structure

Guiding principle: **the user sees exactly two folders — `company/` and `bids/<slug>/{source,outputs}` — everything else is the engine.**

```
hyperfill/
├── README.md                  Orientation + quickstart.
├── CLAUDE.md                  Entry point Claude Code reads automatically. Canonical rules.
├── AGENTS.md                  Condensed operating contract for other agent modes.
├── CHANGELOG.md               Notable changes to the kit itself.
├── LICENSE                    MIT.
│
├── company/                   ★ THE ONE FOLDER YOU FILL IN. Flat drop zone, no
│                                 subfolders — letterhead, signature, certs,
│                                 financials, anything you'd attach to a bid.
│                                 Ships empty.
│
├── docs/                      Guides:
│   ├── setup.md               Make the kit yours (one-time).
│   ├── workflow.md            RFP → submission, step by step.
│   ├── repo-structure.md      This file.
│   ├── conventions.md         Naming, signing, formatting, manual-action rules.
│   ├── knowledge-base.md      What goes in company/ + .rfp-kit/ and how it's used.
│   └── business-proposal-structure.md
│                                 Standalone commercial/technology proposal structure
│                                 (not RFP submissions) — synced from Proposal Builder.
│
├── .toolkit/                  Reusable, config-driven Python. See .toolkit/README.md.
│   ├── paths.py               Repo-relative path resolver (finds your letterhead/signature).
│   ├── bidder_profile.py      Loads .rfp-kit/company-info.json and exposes it to the toolkit.
│   ├── docx_builder.py        Letterhead DOCX builder + helpers.
│   ├── xlsx_builder.py        Excel builder for annexures, BOQs, pricing sheets.
│   └── pdf_tools.py           RFP text extraction, DOCX→PDF, PDF merge.
│                                 No CLI — Claude imports these directly.
│
├── .rfp-kit/                  Hidden: Claude's memory + working files. Never
│                                 shown raw to the user.
│   ├── company-info.json      Single source of truth for company facts.
│   ├── about/                 Capability narrative.
│   ├── experience/            Past project write-ups.
│   └── bids/<slug>/           Parsed RFP, analysis, checklist — per bid.
│
├── bids/                      ONE folder per RFP task, user-visible.
│   ├── README.md
│   └── <slug>/
│         ├── source/          RFP PDF(s) go here.
│         └── outputs/         Finished documents land here, incl. outputs/submission/.
│
└── examples/                  (Optional) finished reference bids you add yourself.
```

## Naming

- **Bid slug:** `<org>-<type>-<year>` — lowercase, hyphenated (`acme-bank-rfp-2026`).
- **Annexures:** `Annexure<N>_<Short_Title>.docx` (or `.xlsx` for spreadsheet annexures).
- **Combined PDFs:** `Annexure<N>_Combined.pdf`.

## What goes where (quick rule)

- A fact about your company → `.rfp-kit/company-info.json` (Claude asks, then writes it).
- A document you attach → `company/` (flat — no subfolders).
- Anything produced for a specific RFP → `bids/<slug>/outputs/`, then `bids/<slug>/outputs/submission/`.
- Parsed RFP text, analysis, and the requirements checklist → `.rfp-kit/bids/<slug>/` (hidden).
- Never put bid-specific output in `company/` or `.toolkit/`.
