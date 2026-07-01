# company/ — Set up once, reused on every bid

Everything the tool needs to know about your organisation lives here.
You fill this in once. Every RFP you work on pulls from it automatically.

---

## Step 1 — Fill in your company details

Open `company-info.json` in any text editor (Notepad, TextEdit, VS Code).
Replace every empty `""` with your real information.

Key fields to fill:
- Company legal name, registration number, GST/tax ID
- Authorised signatory (the person who signs bid documents)
- Office address(es)
- Last 3 years of financials (turnover + net worth)
- Your go/no-go preferences (minimum contract value, preferred sectors)

---

## Step 2 — Upload your files

Drag and drop files into the correct subfolder:

| Folder | What to upload | Format |
|---|---|---|
| `letterhead/` | Your branded letterhead | Word `.docx` (one file) |
| `signature/` | Signature of the authorised signatory | Image `.png` (transparent background is best) |
| `documents/` | Certificates and proofs you attach to every bid | PDF files |
| `experience/` | Past project write-ups | One `.md` file per project (see template) |
| `about/` | Company capability descriptions | `.md` files |

### What to upload to `documents/`
Upload these as PDFs (rename them clearly):
- Certificate of Incorporation / Registration
- GST Certificate
- PAN Card (company)
- Audited financials (last 3 years) — one PDF per year
- ISO / PCI / other certifications
- Bank details letter (on bank letterhead)
- Any other standing document you regularly attach to bids

### What to upload to `about/`
These are markdown text files that describe your company.
Claude reads them when drafting proposals. Create one file per topic:
- `overview.md` — what your company does, your mission, founding story
- `technical-capabilities.md` — technology stack, platforms, what you can build
- `team.md` — team size, key roles, leadership backgrounds
- `approach.md` — your methodology, how you work with clients
- `security.md` — data security, compliance posture (if relevant to your bids)

### What to upload to `experience/`
One markdown file per past project. See the example file in this folder.
Include: client name, project description, contract value, duration, outcome.

---

## Step 3 — Verify setup

Run this command from the RFP Kit folder:
```
python -m toolkit.cli check
```

Or simply open Claude Code in this folder and say: "Check my setup."

---

> Your files here are private — they are excluded from git and never uploaded anywhere automatically.
