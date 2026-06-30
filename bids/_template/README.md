# <Bid name>

> Copy of the bid template. Fill in the fields below when you start a new bid.

| Field | Value |
|-------|-------|
| Issuing org | |
| Reference / tender no. | |
| RFP type | <RFP / RFE / tender> |
| Categories applied | |
| Pre-bid query deadline | |
| Online submission deadline | |
| Physical submission deadline | |
| Submission address | |
| Status | Not started |

## Files

- `source/` — original RFP file(s)
- `parsed/` — RFP converted to Markdown
- `checklist.md` — live requirements tracker (the working document)
- `outputs/docx`, `outputs/pdf`, `outputs/pdf/combined` — generated documents
- `submission/` — final assembled package

## Process

Follow [`../../docs/workflow.md`](../../docs/workflow.md). Pull facts from
[`../../company/company-info.json`](../../company/company-info.json) and build with
the [`../../toolkit/`](../../toolkit/).
