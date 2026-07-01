# Setup Guide

**You need:** Claude Code. Nothing else to install.

---

## Step 1 — Get the kit

```bash
git clone https://github.com/mananaggrawal/claude-rfp-kit
claude claude-rfp-kit
```

Claude Code opens, scans the folder, and tells you what to do next.

---

## Step 2 — Upload your company files

Claude Code will show you exactly what's missing. The files go into these folders — just drag and drop using Finder (Mac) or File Explorer (Windows):

| What | Folder | Format |
|---|---|---|
| Company letterhead | `company/letterhead/` | Word `.docx` |
| Signature image | `company/signature/` | `.png` |
| Incorporation certificate | `company/documents/` | PDF |
| GST / tax certificate | `company/documents/` | PDF |
| Audited financials (last 3 years) | `company/documents/` | PDF |
| Any other certificates | `company/documents/` | PDF |
| Past project write-ups | `company/experience/` | One `.md` per project |
| Company capability descriptions | `company/about/` | `.md` files |

Each folder has a `README.md` explaining what to put there and how to name files.

---

## Step 3 — Start your first bid

Drop your RFP PDF into `bids/<bid-name>/source/` and tell Claude Code:
> "I have a new RFP from [buyer name]"

Claude handles the rest. Full workflow in `docs/workflow.md`.
