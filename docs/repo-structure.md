# Repository structure

Guiding principle: **generic, reusable material is separated from per-bid task work.**

```
claude-rfp-kit/
├── README.md                  Orientation + quickstart.
├── CLAUDE.md                  Entry point Claude Code reads automatically.
├── AGENTS.md                  Operating contract for any agent.
├── pyproject.toml             Installs the `rfpkit` CLI + pypdf.
├── LICENSE                    MIT.
│
├── docs/                      Guides:
│   ├── setup.md               Make the kit yours (one-time).
│   ├── workflow.md            RFP → submission, step by step.
│   ├── repo-structure.md      This file.
│   ├── conventions.md         Naming, signing, formatting, manual-action rules.
│   └── knowledge-base.md      What goes in company-knowledge and how to use it.
│
├── company-knowledge/         YOUR reusable knowledge (shared by every bid). Ships empty.
│   ├── master-data.md         Single source of truth (human copy). Machine copy: toolkit/bidder_profile.py.
│   ├── proposal-library.md    Optional: record a live reference to an external proposal folder.
│   ├── profile/               Narrative docs (deck, business plan, technical/security write-ups).
│   └── submission-documents/
│       ├── company-documents/     Registration, tax, audited financials, certifications.
│       └── experience-proofs/     Client agreements / POs / completion certificates.
│
├── assets/                    Branding used to GENERATE documents. Ships empty.
│   ├── letterhead/            Drop your letterhead .docx here (auto-detected).
│   └── signature-stamp/       Drop your signature/stamp image here (auto-detected).
│
├── toolkit/                   Reusable, config-driven Python. See toolkit/README.md.
│   ├── paths.py               Repo-relative path resolver (finds letterhead/signature for you).
│   ├── bidder_profile.py      Machine-readable single source of truth (fill it in).
│   ├── docx_builder.py        Letterhead DOCX builder + helpers.
│   ├── pdf_tools.py           DOCX→PDF + PDF merge.
│   └── cli.py                 The `rfpkit` command.
│
├── bids/                      ONE folder per RFP task.
│   ├── README.md
│   └── _template/             Skeleton copied by `rfpkit new`.
│
└── examples/                  (Optional) finished reference bids you add yourself.
```

## Naming

- **Bid slug:** `<org>-<type>-<year>` — lowercase, hyphenated (`acme-bank-rfp-2026`).
- **Annexures:** `Annexure<N>_<Short_Title>.docx`.
- **Combined PDFs:** `Annexure<N>_Combined.pdf`.

## What goes where (quick rule)

- A fact about your company → `company-knowledge/master-data.md` + `toolkit/bidder_profile.py`.
- A document you attach → `company-knowledge/submission-documents/`.
- Anything produced for a specific RFP → `bids/<slug>/outputs/` then `bids/<slug>/submission/`.
- Never put bid-specific output in `company-knowledge/`, `assets/`, or `toolkit/`.
