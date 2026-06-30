# 📁 company/ — fill this one folder, then you're done

Everything the kit needs about **your organisation** lives here. Set it up once; every
bid reuses it. You don't need to touch any code.

## 1. Your details → `company-info.json`

The easiest way: run the wizard, which asks you questions and fills the file for you:

```bash
rfpkit init
```

Prefer to type it yourself? Just open **`company-info.json`** and fill in the blanks
(name, registration number, tax IDs, signatory, offices, financials). It's a plain text
file — no coding.

## 2. Drop your files into these folders

| Folder | What to put here |
|--------|------------------|
| **letterhead/** | Your company letterhead as a **.docx** (one file). Generated documents are built on it. |
| **signature/** | The authorised signatory's **signature + company stamp** as one image (PNG/JPG). |
| **documents/** | Standing proofs you attach to bids: registration/incorporation, tax registrations, audited financials, certifications (ISO/PCI/etc.), bank details. |
| **experience/** | Proof of past work: client agreements, purchase orders, completion / satisfaction certificates. |
| **about/** | Narrative material used to write proposals: company deck, business plan, technical & security write-ups. |

That's it. Run `rfpkit check` to confirm everything's in place, then `rfpkit new <name>`
to start a bid.

> **Privacy:** the contents of these folders are kept out of git by default (see the
> repo's `.gitignore`) so you never push your letterhead, signature, or documents by
> accident. The folders themselves stay (via `.gitkeep`).
