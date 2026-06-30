# Bids

One folder per RFP/RFE/tender. Each is a self-contained task.

## Start a new bid

```bash
rfpkit new <org>-<type>-<year>      # e.g. acme-bank-rfp-2026
```

(or `cp -r bids/_template bids/<slug>`). Then follow [`../docs/workflow.md`](../docs/workflow.md):
put the RFP in `source/`, parse it to `parsed/`, build `checklist.md`, generate annexures
and the proposal into `outputs/`, and assemble `submission/`.

## Per-bid layout

```
<slug>/
├── README.md          bid name, reference no., deadlines, status
├── checklist.md       live requirements tracker
├── source/            original RFP file(s)
├── parsed/            RFP as Markdown
├── outputs/           docx / pdf / pdf/combined
└── submission/        final package, organised as the RFP requires
```

> Bid folders are git-ignored by default (they hold work-in-progress and may contain
> client material). Keep `_template/` tracked.
