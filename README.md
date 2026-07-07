# RFP Kit

An open-source RFP response assistant that runs entirely inside Claude. Drop in an RFP PDF, talk to the assistant in plain English, and get back analysis, filled forms, and a draft proposal — all using your real company data, on your letterhead.

**No scripts to run. No tools to install. No data leaves your machine.**

---

## What it does

| Ask for | What you get |
|---|---|
| Go / No-Go | Eligibility check, risk score, clear bid recommendation |
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

The assistant opens your company folder automatically, reads whatever you drop in, and walks you through setup conversationally — no config files, no forms to fill.

---

## How it works

You interact with two folders only:

```
company/     ←  drop your files here (letterhead, certs, financials, signature image)
bids/
  └── acme-rfp-2026/
        ├── source/    ←  drop the RFP PDF here
        └── outputs/   ←  pick up finished documents from here
```

The assistant handles everything else — reading documents, extracting company data, parsing RFPs, generating Word documents, and keeping track of what's been done for each bid.

---

## Privacy

All your company files and bid documents stay on your local machine only. Nothing is pushed to git — your data never leaves your computer.

---

## Free and open source

MIT licensed — use it, fork it, improve it. Single-user use is free. If you're building an enterprise version or want to customise it for a team, reach out to manan190303@gmail.com

Contributions welcome — open a PR or file an issue.

---

## License

MIT — see [LICENSE](LICENSE).
