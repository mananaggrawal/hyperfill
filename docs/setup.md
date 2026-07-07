# Setup Guide

**You need:** Claude Code (or Cowork). Nothing else to install.

---

## Step 1 — Get the kit

```bash
git clone https://github.com/mananaggrawal/hyperfill
claude hyperfill
```

Claude Code won't say anything until you do — that's just how the tool works, nothing
to debug. Type `hi` (or anything at all) and it scans the folder and tells you what to
do next.

---

## Step 2 — Upload your company files

Claude will tell you exactly what's missing. Just drag and drop everything
into the single `company/` folder — it's a flat drop zone, no subfolders to
sort things into:

| What | Format |
|---|---|
| Company letterhead | Word `.docx` |
| Signature / stamp image | `.png` or `.jpg` |
| Incorporation certificate | PDF |
| GST / tax certificate | PDF |
| Audited financials (last 3 years) | PDF |
| Any other certificates | PDF |
| Past project write-ups | Claude asks about these conversationally and files them under `.rfp-kit/experience/` |
| Company capability descriptions | Claude asks about these conversationally and files them under `.rfp-kit/about/` |

Claude reads everything you drop in and extracts identity, registration,
signatory, and financial details into `.rfp-kit/company-info.json` — you never
edit that file by hand; tell Claude if anything's wrong and it updates it
(keeping a backup of the previous version).

---

## Step 3 — Start your first bid

Tell Claude:
> "I have a new RFP from [buyer name]"

It sets up `bids/<slug>/source/`, opens it, and asks you to drop the RFP PDF
in. Full workflow in [`workflow.md`](workflow.md).
