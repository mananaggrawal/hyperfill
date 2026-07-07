# Bids

One folder per RFP/RFE/tender. Each is a self-contained task.

## Start a new bid

Just tell Claude: *"I have a new RFP from [buyer name]"*. It creates the
folder, opens `source/` for you, and asks you to drop the RFP PDF in.
No command to run and no template to copy by hand.

## Per-bid layout (what you see)

```
<slug>/
├── source/            original RFP file(s), and any addenda/corrigenda
└── outputs/           filled annexures, proposals, and:
      └── submission/  final package, organised as the RFP requires,
                        with a MANIFEST.md listing what's included
```

The parsed RFP text, analysis (go/no-go, risks, synopsis, contradictions),
and the live requirements checklist for each bid live in the hidden
`.rfp-kit/bids/<slug>/` folder — Claude reads and writes these directly; you
never need to open them.

> Bid folders are git-ignored by default (they hold work-in-progress and may
> contain client material).
