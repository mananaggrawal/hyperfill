# Claude RFP Kit

A **Claude Code framework** for generating RFP / RFE / tender responses. Point Claude
Code at this folder, fill it with **your** company's information once, and it will parse
an RFP, fill the annexures, draft the response proposal, and assemble a submission-ready
folder — following the rules in [`AGENTS.md`](AGENTS.md) / [`CLAUDE.md`](CLAUDE.md).

The repo ships **empty** on purpose. There's no company baked in — you bring your own
knowledge base.

## How it works

```
your knowledge base  ──►  RFP (a task)  ──►  Claude follows the workflow  ──►  submission folder
(filled once)             bids/<slug>/                                        bids/<slug>/submission/
```

- **`company-knowledge/`** — your reusable facts and documents (shared by every bid).
- **`assets/`** — your letterhead + signature/stamp, used to generate documents.
- **`toolkit/`** — config-driven Python that builds DOCX, converts to PDF, and merges attachments.
- **`bids/`** — one folder per RFP. `bids/_template/` is the skeleton.
- **`docs/`** — workflow, structure, conventions, knowledge-base, and setup guides.

## Quickstart

1. **Get the code**
   ```bash
   git clone <your-repo-url> && cd claude-rfp-kit
   pip install -e .            # installs the `rfpkit` command + pypdf
   ```
   Also install **LibreOffice** (for DOCX→PDF).

2. **Add your company** (one-time) — see [`docs/setup.md`](docs/setup.md):
   - Fill [`toolkit/bidder_profile.py`](toolkit/bidder_profile.py) and
     [`company-knowledge/master-data.md`](company-knowledge/master-data.md).
   - Drop your **letterhead** `.docx` into `assets/letterhead/`.
   - Drop your **signature/stamp** image into `assets/signature-stamp/`.
   - Drop your **company documents** (registration, tax, financials, certs) into
     `company-knowledge/submission-documents/`.
   - Add narrative/profile docs (deck, business plan) to `company-knowledge/profile/`.

3. **Verify**
   ```bash
   rfpkit check        # or: python -m toolkit.cli check
   ```

4. **Run a bid** — point Claude Code at the folder and give it the RFP:
   ```bash
   rfpkit new acme-bank-rfp-2026     # scaffolds bids/acme-bank-rfp-2026/
   # put the RFP in bids/acme-bank-rfp-2026/source/, then in Claude Code:
   #   "Process the RFP in bids/acme-bank-rfp-2026 following AGENTS.md"
   ```
   Claude reads `CLAUDE.md`/`AGENTS.md` and runs the workflow: parse → checklist →
   fill annexures → draft proposal → assemble `submission/`.

## CLI

| Command | Does |
|---------|------|
| `rfpkit check` | Verify setup (profile filled, letterhead/signature present, deps). |
| `rfpkit new <slug>` | Create a new bid folder from the template. |
| `rfpkit list` | List your knowledge base and bids. |
| `rfpkit build-pdf <file.docx>` | Convert a DOCX to PDF. |

(All also available as `python -m toolkit.cli <command>` without installing.)

## Privacy

This framework contains **no company data**. When you fill it with yours, your private
documents stay on your machine. The default [`.gitignore`](.gitignore) keeps your
letterhead, signature image, and submission documents **out of git** so you don't push
them by accident — adjust it if you intend to keep them in your own private repo.

## License

MIT — see [`LICENSE`](LICENSE).
