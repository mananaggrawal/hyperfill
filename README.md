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
| Jira ticket | Any request, task, or piece of analysis turned into a tracked ticket |

The moment an RFP (or a corrigendum/addendum) is parsed, Go/No-Go, the synopsis, the risk
review, the contradiction check, and the submission checklist all run automatically — you
don't have to ask for any of them. Multiple RFPs run in parallel, each in its own folder,
and an addendum is always reconciled against the original extract (with superseded clauses
called out) rather than silently overwriting it.

---

## In depth: how a bid actually moves through the kit

**1. Parse.** Drop the RFP PDF in `bids/<slug>/source/` and say it's in. The PDF is read
natively (no OCR step, no external converter) and turned into structured markdown — dates,
scope, eligibility criteria, submission-document list, penalty clauses, all extracted, not
summarised from memory.

**2. Auto-analysis.** As soon as parsing finishes, four analyses and a checklist are written
without being asked for: Go/No-Go (with a clear verdict and reasoning), a one-page synopsis,
a risk & red-flag review (penalties, uncapped liability, aggressive SLAs, unusual indemnities),
a contradiction check (places the RFP conflicts with itself or leaves something genuinely
ambiguous), and a submission checklist that separates real submission documents from manual
actions (stamp paper, notarisation, wet signatures, demand drafts) that can't be done digitally.

**3. Draft.** Every submission document — NDA, company details, technical proposal,
implementation plan, financials, client references, team structure, filled annexures — is
built on your actual letterhead using your real company data (from `company-info.json`,
`about/`, `experience/`, and whatever's in `company/`). Nothing is invented: a missing fact
is flagged as `[MISSING — please provide: ...]` and asked for, one thing at a time, never
guessed. Independent documents are drafted in parallel by sub-agents rather than one at a
time, so a bid with eight required documents doesn't take eight times as long.

**4. Assemble.** When you're ready to submit, every required enclosure is matched to a file
already in `company/`, copied (never moved) and renamed sensibly, converted/merged into a
single PDF where the RFP demands it, and written out with a manifest showing exactly what's
included and what's still missing or needs a manual step.

**5. Track (optional).** If you use Jira and/or Google Drive, the same bid can be tracked
there too — see "Optional integrations" below.

---

## Optional integrations

These are entirely opt-in — connect them once via Claude's connector settings, or skip this
section entirely and use the kit purely through the two local folders.

### Jira

Turn any request, follow-up, or piece of analysis into a tracked ticket just by asking
("make a ticket for this," "log this in Jira," or picking the ticket-creation option from
the menu). The kit never hardcodes a board — the first time you ask, it asks which
project to use and remembers your choice from then on.

Structure per bid:
- **One epic per bid**, holding the RFP synopsis and status. Its description links the
  bid's single Drive folder (see below) — nothing else — so it stays a clean entry point
  rather than a wall of links.
- **One submission-checklist ticket**, listing every required submission document with
  its status (not started / drafted / done) and its individual document link. This is
  updated in place as documents progress, not recreated per document.
  Individual per-document tickets can exist too, each carrying its own link — the
  checklist ticket is the one place you can see all of them at a glance.
- **Analysis tickets for Go/No-Go, the synopsis, risks, and contradictions** — the actual
  write-up lives directly in the ticket description or a comment. These are working notes,
  not submission deliverables, so they're never turned into a separate created document.

### Google Drive

If connected, actual submission documents (not analysis/notes) can be mirrored to Drive as
native Google Docs, so non-technical stakeholders can view or comment without needing the
local files. The real letterhead-based `.docx` is always built first and only then uploaded
to Drive for conversion — content is never hand-typed a second time as Markdown, since that
would lose the letterhead, tables, and layout the real document has. All of a bid's documents
live in one Drive folder, matching the folder linked from its Jira epic.

---

## Under the hood, worth knowing

- **Sub-agents for independent work.** Drafting a full set of submission documents, running
  several analyses on the same RFP, or advancing two unrelated bids at once — genuinely
  independent work is parallelised rather than worked through one item at a time.
- **File locks are surfaced, never silently worked around.** If your letterhead is open in
  another app (or, less obviously, still syncing down from iCloud/OneDrive/Drive as a
  cloud-only placeholder), you're told exactly which file is stuck rather than getting a
  degraded plain-text substitute with no explanation.
- **A single `company-info.json` as the source of truth**, backed up automatically before
  every update, so a bad extraction can always be undone.
- **Manual-only steps are always flagged**, never silently skipped or faked — stamp paper,
  wet signatures, notarisation, demand drafts, performance guarantees.

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

**Track & collaborate (optional)**
- Turn any request or piece of analysis into a Jira ticket, nested under one
  epic per bid with a dedicated submission-documents checklist ticket
- Mirror actual submission documents to Google Drive as native Google Docs,
  built from the real letterheaded file rather than retyped from scratch
- See [Optional integrations](#optional-integrations) below for the full picture

Everything you don't need to see (parsed RFP text, analysis, checklists) lives
in a hidden working folder — your view stays to two folders.

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

Claude Code waits for you to say something first — it won't speak until you do. Just type
`hi` (or anything) and it takes it from there: opens your company folder automatically,
reads whatever you drop in, and walks you through setup conversationally — no config files,
no forms to fill.

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
