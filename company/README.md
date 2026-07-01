# company/ — Drop all your files here

This folder holds everything Claude needs to know about your company.
**You don't need to organise files into subfolders** — just drop everything here
and Claude will find what it needs.

## What to drop in this folder

- Your company **letterhead** — a Word `.docx` file
- Your **signature** — an image of the authorised signatory's signature (`.png` or `.jpg`)
- Your **certificates** — GST cert, incorporation cert, ISO cert, etc. (PDFs)
- Your **audited financials** — one PDF per year
- Any other documents you regularly attach to bids (PDFs)

## What Claude fills in automatically

When you open Claude Code for the first time, it will ask you questions about your company
(name, registration number, GST, signatory, etc.) and write everything to `company-info.json`
for you. You never need to open or edit that file manually.

It will also ask you to describe your company and past projects in plain language —
and write those as structured files it can reference when drafting proposals.

## Privacy

Everything in this folder stays on your local machine. It is excluded from git.
