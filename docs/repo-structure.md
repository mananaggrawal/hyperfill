# Repository structure

Guiding principle: **the user fills one `company/` folder; everything else is the engine.**

```
claude-rfp-kit/
├── README.md                  Orientation + quickstart.
├── CLAUDE.md                  Entry point Claude Code reads automatically.
├── AGENTS.md                  Operating contract for any agent.
├── pyproject.toml             Installs the `rfpkit` CLI + pypdf.
├── LICENSE                    MIT.
│
├── company/                   ★ THE ONE FOLDER YOU FILL IN. Ships empty.
│   ├── README.md              Plain-language "drop X here" guide.
│   ├── company-info.json      Your details (written by `rfpkit init`, or edit by hand).
│   ├── letterhead/            Your letterhead .docx (auto-detected).
│   ├── signature/             Your signature/stamp image (auto-detected).
│   ├── documents/             Registration, tax, audited financials, certifications.
│   ├── experience/            Client agreements / POs / completion certificates.
│   └── about/                 Narrative (deck, business plan, technical/security write-ups).
│
├── docs/                      Guides:
│   ├── setup.md               Make the kit yours (one-time).
│   ├── workflow.md            RFP → submission, step by step.
│   ├── repo-structure.md      This file.
│   ├── conventions.md         Naming, signing, formatting, manual-action rules.
│   └── knowledge-base.md      What goes in company/ and how to use it.
│
├── toolkit/                   Reusable, config-driven Python. See toolkit/README.md.
│   ├── paths.py               Repo-relative path resolver (finds your letterhead/signature).
│   ├── bidder_profile.py      Loads company/company-info.json and exposes it to the toolkit.
│   ├── docx_builder.py        Letterhead DOCX builder + helpers.
│   ├── pdf_tools.py           DOCX→PDF + PDF merge.
│   └── cli.py                 The `rfpkit` command (init / check / new / list / build-pdf).
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

- A fact about your company → `company/company-info.json` (via `rfpkit init`).
- A document you attach → `company/documents/` or `company/experience/`.
- Letterhead / signature → `company/letterhead/` and `company/signature/`.
- Anything produced for a specific RFP → `bids/<slug>/outputs/` then `bids/<slug>/submission/`.
- Never put bid-specific output in `company/` or `toolkit/`.
