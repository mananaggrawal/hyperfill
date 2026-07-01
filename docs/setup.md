# Setup Guide

Follow these steps once. After that, every RFP you work on reuses what you set up here.

---

## Part A — Google Drive setup (for teams)

> Skip to Part B if you're working solo on your own machine.

1. **Install Google Drive for Desktop** on every team member's computer.
   Download from: https://www.google.com/drive/download/

2. **Create a folder in Google Drive** called `RFP-Kit`.

3. **Copy this entire repository** into that Google Drive folder.
   (Drag and drop the folder contents, or use the Drive web interface to upload.)

4. **Each team member:** Open Google Drive for Desktop → find `RFP-Kit` → click the
   sync icon to make it available offline on your computer.

5. Your local path will be something like:
   - Mac: `~/Google Drive/My Drive/RFP-Kit/`
   - Windows: `G:\My Drive\RFP-Kit\`

   Open Claude Code by navigating to this path in your terminal and running `claude`.

---

## Part B — Company setup (do this once)

### Step 1 — Install dependencies

Double-click `setup.sh` (Mac) or run in terminal:
```
bash setup.sh
```

This installs the required Python packages automatically.

Also install **LibreOffice** for converting Word documents to PDF:
- Mac: https://www.libreoffice.org/download/libreoffice/
- Windows: https://www.libreoffice.org/download/libreoffice/

### Step 2 — Fill in your company information

Open `company/company-info.json` in any text editor (TextEdit, Notepad, VS Code).
Replace every empty `""` with your company's real details.

Fields to fill:
- Company legal name, registration number, GST number
- Authorised signatory (the person who signs bid documents)
- Office address(es)
- Last 3 years of financials (turnover + net worth)

Or run the guided wizard instead:
```
python -m toolkit.cli init
```

### Step 3 — Upload your files

Read the README in each folder for instructions on what to upload:

| Folder | What to upload |
|---|---|
| `company/letterhead/` | Your Word letterhead template (`.docx`) |
| `company/signature/` | Authorised signatory's signature image (`.png`) |
| `company/documents/` | Certificates, financials, registration docs (PDFs) |
| `company/experience/` | Past project write-ups (one `.md` file per project) |
| `company/about/` | Company capability descriptions (`.md` files) |

### Step 4 — Verify

```
python -m toolkit.cli check
```

Or open Claude Code and say: **"Check my setup."**

Fix any items flagged as missing before starting your first bid.

---

## Part C — Starting your first bid

1. Get the RFP PDF from the buyer
2. Open Claude Code in the RFP-Kit folder
3. Say: **"Start a new bid for [buyer name]"** or run `/new acme-bank-rfp-2026`
4. Upload the RFP PDF to the folder Claude tells you
5. Run `/parse acme-bank-rfp-2026` and follow the sequence from there

See `docs/workflow.md` for the full command sequence.
