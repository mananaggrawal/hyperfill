# RFP Kit

Respond to RFPs, tenders, and RFEs using Claude — conversationally, from your terminal or the Claude desktop app. Drop in an RFP PDF, talk to the assistant, get back analysis, filled forms, and a draft proposal — all using your real company data.

**No scripts to run. No tools to install. Just Claude.**

---

## What it does

Tell the assistant what you need in plain English. It handles the rest.

| Ask for | What you get |
|---|---|
| Go / No-Go | Eligibility check, risk score, bid recommendation |
| Synopsis | One-page brief — scope, deadline, value, evaluation method |
| Risks | Red-flag clauses — penalties, IP transfer, SLAs, liability |
| Contradictions | Places where the RFP conflicts with itself |
| Pre-bid questions | Draft clarification questions to submit to the buyer |
| Fill a form | Any annexure filled with your company data, on your letterhead |
| Technical proposal | Full draft using your capabilities and past projects |
| Commercial proposal | Pricing narrative and commercial terms |

Multiple RFPs can run in parallel — each lives in its own folder.

---

## Quickstart

**You need:** [Claude Code](https://claude.ai/code) — nothing else.

```bash
git clone https://github.com/mananaggrawal/claude-rfp-kit
cd claude-rfp-kit
claude .
```

Claude opens your company folder automatically and walks you through setup — no config files, no forms.

---

## Folder structure

You interact with two folders only:

```
company/     ←  drop your files here (letterhead, certs, financials, signature)
bids/
  └── acme-rfp-2026/
        ├── source/    ←  drop the RFP PDF here
        └── outputs/   ←  pick up finished documents from here
```

Everything else is managed by the assistant internally.

---

## Privacy

All your company files and bid documents stay on your local machine only.
Nothing is pushed to git — your data never leaves your computer.

---

## License

MIT — see [LICENSE](LICENSE).
