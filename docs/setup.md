# Setup Guide

Everything is done through Claude Code. You do not need to install packages,
run scripts, or use any other tool.

---

## What you need

1. **Claude Code** — installed on your computer ([download here](https://claude.ai/download))
2. **Google Drive for Desktop** — installed and signed in ([download here](https://www.google.com/drive/download/))

That's it.

---

## Step 1 — Get this repository

**Option A (recommended for teams):** Your admin clones or downloads this repository once,
then the `/setup-drive` command (Step 2) copies everything to Google Drive for the whole team.

**Option B:** Download the ZIP from GitHub and unzip it anywhere on your computer.

---

## Step 2 — Open Claude Code and run /setup-drive

1. Open Claude Code
2. Open this folder (File → Open Folder → select the `rfp-kit` folder)
3. Type:
   ```
   /setup-drive
   ```

Claude Code will:
- Find your Google Drive folder automatically
- Create the complete `RFP-Kit` folder structure on Drive
- Ask you a few questions about your company and fill in your profile
- Tell you exactly what files to upload and where

This takes about 5 minutes and only needs to be done once.

---

## Step 3 — Upload your company files

After `/setup-drive`, Claude will tell you which files to upload.
The main ones are:

| What | Where to upload | Format |
|---|---|---|
| Company letterhead | `company/letterhead/` | Word `.docx` |
| Authorised signatory's signature | `company/signature/` | Image `.png` |
| Incorporation / registration certificate | `company/documents/` | PDF |
| GST certificate | `company/documents/` | PDF |
| Audited financials (last 3 years) | `company/documents/` | PDF per year |
| Any other certificates | `company/documents/` | PDF |
| Past project write-ups | `company/experience/` | One `.md` per project |
| Company capability descriptions | `company/about/` | `.md` files |

Open the `README.md` inside each folder for detailed instructions.

---

## Step 4 — For team members

Once the admin has run `/setup-drive`:

1. Install Google Drive for Desktop and sign in with the company account
2. The `RFP-Kit` folder will sync automatically to their computer
3. Open Claude Code → Open Folder → select `RFP-Kit` from their local Drive mount
4. Start working on bids

No setup needed for team members — just open and go.

---

## Starting your first bid

Once setup is done, the full workflow is in `docs/workflow.md`.
The short version:

```
/new acme-bank-2026         ← create the bid folder
[upload RFP PDF to source/]
/parse acme-bank-2026       ← Claude reads and extracts the RFP
/go-nogo acme-bank-2026     ← should we bid?
/synopsis acme-bank-2026    ← one-page brief
...
```
