# Contributing

Thanks for considering a contribution to RFP Kit. This is a small, focused project —
here's how to get a change in.

## Before you start

For anything beyond a small fix (a new feature, a change to the folder model, a new
toolkit module), please open an issue first to discuss the approach. It's much easier
to agree on direction before code is written than to rework a finished PR.

## Ground rules for this codebase

The whole point of this kit is that **the user never runs scripts, installs
packages, or touches a CLI** — Claude does everything conversationally. Keep that
invariant when contributing:

- No new CLI commands or scripts intended for the human to run directly. If you're
  adding toolkit functionality, it should be a Python function Claude calls, not a
  script the user invokes.
- The user-visible surface stays exactly two folders: `company/` (flat, no
  subfolders) and `bids/<slug>/{source,outputs}`. Anything else — parsed RFP text,
  analysis, checklists, company facts — belongs under the hidden `.rfp-kit/`.
- `CLAUDE.md` is the canonical operating contract; `AGENTS.md` is a condensed
  mirror for other agent runners. If you change one, check whether the other needs
  updating too, and keep `docs/*.md` in sync with both.
- Never hardcode a real company's name, numbers, or documents into the kit itself
  — use a generic placeholder like "Acme Corp" in examples and docstrings.

## Development

The toolkit modules under `.toolkit/` are plain Python with no import-time side
effects beyond reading `.rfp-kit/company-info.json` (which falls back to sensible
defaults if it doesn't exist yet). To sanity-check a change:

```bash
pip install -e .toolkit  # or: pip install python-docx openpyxl pypdf pdfplumber Pillow
python3 -m py_compile .toolkit/*.py
```

There's no test suite yet — if you're adding non-trivial logic (especially to
`docx_builder.py`'s XML injection or `paths.py`'s file resolution), a short script
that exercises it against a throwaway letterhead/signature and prints the result is
appreciated in the PR description.

## Submitting a change

1. Fork the repo and branch from `main`.
2. Keep the PR focused — one logical change per PR.
3. Update `CHANGELOG.md` under an "Unreleased" heading.
4. Open the PR with a short description of what changed and why.

## Reporting bugs / requesting features

Open a GitHub issue. For bugs, include what you expected, what happened instead,
and enough context to reproduce (redact any real company/RFP data first — issues
are public).
