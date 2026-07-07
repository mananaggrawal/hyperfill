# Hyperfill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Built for Claude Code](https://img.shields.io/badge/built%20for-Claude%20Code-blueviolet)](https://claude.ai/code)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

An open-source RFP response assistant that runs entirely inside Claude. Drop in an RFP PDF, talk to the assistant in plain English, and get back analysis, filled forms, and a draft proposal — all using your real company data, on your letterhead.

**No scripts to run. No tools to install. No CLI to learn.**

---

## What it does

| Ask for | What you get |
|---|---|
| Go / No-Go | Eligibility check, risk score, clear bid recommendation |
| Synopsis | One-page brief — scope, deadline, value, evaluation method |
| Risks | Red-flag clauses — penalties, IP transfer, SLAs, liability |
| Contradictions | Places where the RFP conflicts with itself |
| Pre-bid questions | Draft clarification questions to submit to the buyer |
| Fill a form | Any annexure filled with your company data, on your letterhead — Word or Excel |
| Technical proposal | Full draft using your capabilities and past projects |
| Commercial proposal | Pricing narrative and commercial terms |
| Assemble submission | Every required document collected, renamed, and manifested into one folder |

Multiple RFPs can run in parallel — each lives in its own folder, and addenda/corrigenda
issued after the original RFP are reconciled against it rather than silently overwriting it.

---

## Example

You don't learn a syntax — you just talk to it.

```
you:  I have a new RFP from Acme Bank.

Claude:  I've set up a folder for Acme Bank and opened it — drop the RFP PDF in
         there and let me know when it's in.

you:  it's in

Claude:  Got it — reading the RFP now.

         Done. Here's what Acme Bank is asking for:

           A managed fraud-monitoring platform for their card portfolio, RFP
           value not disclosed, technical + commercial bids evaluated separately.

         Key dates:
           • Pre-bid queries: 12 Aug 2026
           • Submission deadline: 2 Sep 2026

         A few things caught my eye:
           • Uncapped liability clause in §9.3
           • Turnover threshold (₹15 Cr) — worth checking against your financials
           • Performance bank guarantee required within 30 days of award

         What would you like to do first?

           A  Go / No-Go — should you bid?
           B  Summarise the RFP in one page
           ...

you:  fill annexure 4

Claude:  Annexure 4 is the "Bidder's Declaration" form. I've filled it with your
         company details and put it on your letterhead —
         bids/acme-bank-rfp-2026/outputs/Annexure4_Bidders_Declaration.docx is ready.
         One field I couldn't fill: "Date of last regulatory audit" — what's the answer?
```

That's the whole interaction model — plain English in, a finished document or a
straight answer out.

---

## Features

**Understand the RFP**
- Go/No-Go scoring against eligibility criteria, with a clear bid/no-bid call
- One-page synopsis for stakeholders who don't want to read the whole document
- Risk scan for penalty clauses, IP transfer, uncapped liability, unreasonable SLAs
- Contradiction check across sections of the same RFP
- Ask any question about the RFP directly, in plain English
- Addenda/corrigenda reconciled against the original extract, not silently merged in

**Draft your response**
- Pre-bid clarification questions drawn from risks, contradictions, and gaps
- Any annexure or form filled from your company data — Word (on your letterhead,
  signature included) or Excel (BOQs, pricing sheets, pre-bid query formats)
- Technical and commercial proposal drafts using your capability narrative and
  past-project evidence
- Manual-only items (stamp paper, wet signatures, bank guarantees) are always
  flagged, never silently skipped or faked

**Wrap up**
- Submission assembly: matches every required enclosure to a file you already
  have, copies and renames it, converts/merges to PDF where the RFP requires it,
  and generates a manifest of what's included vs. still missing

**Under the hood**
- A single `company-info.json` as the source of truth, backed up automatically
  before every update
- Everything you don't need to see (parsed RFP text, analysis, checklists) lives
  in a hidden working folder — your view stays to two folders

---

## Who this is for

Anyone who responds to RFPs, RFEs, and tenders regularly enough that retyping the same
company facts into a new Word template every time has gotten old — solo founders and early
startups bidding for their first few contracts, agencies and consultancies running several
bids in parallel, and larger organisations with dedicated bid teams. If your bids involve
signed letterheads, standard annexures, and a folder of certificates you dig up every time,
this kit is for you. Single-user use is free and open source; if you're a larger org that
wants a custom/team plan, see [Free and open source](#free-and-open-source) below.

---

## Quickstart

**You need:** [Claude Code](https://claude.ai/code) (or Cowork) — nothing else.

```bash
git clone https://github.com/mananaggrawal/hyperfill
cd hyperfill
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

The assistant handles everything else — reading documents, extracting company data,
parsing RFPs, generating Word and Excel documents, and keeping track of what's been
done for each bid in a hidden `.rfp-kit/` working folder you never need to open.

See [`docs/setup.md`](docs/setup.md) for a walkthrough, and
[`docs/workflow.md`](docs/workflow.md) for the full RFP-to-submission sequence.

---

## Privacy

Your company files and bid documents stay on your local machine — nothing is committed to
git, and the kit itself never uploads anything anywhere. Note that using Claude at all means
the RFP text and company data you're working on are sent to Anthropic's API as part of the
conversation, the same as any other Claude Code session — that's inherent to how Claude
works, not something this kit adds on top. If you're handling especially sensitive tender
material, review Anthropic's data-handling terms for the product you're using before
proceeding.

---

## Free and open source

MIT licensed — use it, fork it, improve it. Single-user use is free. If you're building an
enterprise version or want to customise it for a team, reach out to manan190303@gmail.com.

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) for how the project is
organised and what to keep in mind before opening a PR. Please also read the
[Code of Conduct](CODE_OF_CONDUCT.md). Found a bug or have an idea? [Open an issue](https://github.com/mananaggrawal/hyperfill/issues).

---

## License

MIT — see [LICENSE](LICENSE).
