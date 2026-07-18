---
name: rfp-kit
description: "Use this skill whenever the user is responding to an RFP, tender, RFE, or similar bid document — inside a repo/folder that has (or should have) a company/ drop-zone, a bids/<slug>/ structure, and a hidden .rfp-kit/ + .toolkit/ working area. Triggers include: 'I have an RFP', 'respond to this tender', 'go/no-go', 'summarise this RFP', 'draft the proposal', 'fill this annexure', 'assemble the submission', or any request to analyse, draft, or submit a response to a buyer's RFP. Also covers mirroring documents to Google Drive or updating the bid's Blueprint Google Sheet tracker. This kit uses Google Sheets only for tracking — no Jira or other ticketing system. Do NOT use for general document editing unrelated to a bid/tender response."
license: Proprietary
---

# RFP Kit — RFP Response Assistant

This skill packages the full "RFP Response Assistant" operating contract used by
Hyperfill-style repos. It exists so a new user (or a new repo) gets the **same
behaviour — same folder layout, same menu, same Jira/Drive/Blueprint structure —
without anyone having to explain the workflow by hand.**

## First: locate or create the operating contract

1. Check whether the current working folder (or the folder the user has connected)
   already has a `CLAUDE.md` at its root.
   - **If yes:** that file is the authoritative, complete operating contract for
     this repo. Read it in full and follow it exactly — it supersedes the summary
     below wherever the two differ, since it reflects this specific repo's actual
     state (bid slugs, Jira project key, Drive folder IDs, company data already on
     file, etc.).
   - **If no:** this is a brand-new repo that wants the RFP Kit workflow. Copy the
     canonical `CLAUDE.md` template from this skill's `reference/CLAUDE.md` into
     the repo root, then follow it from that point on. Do not improvise a
     different folder layout or menu — the whole point of this skill is that every
     repo using it behaves identically.

## What this buys the user (summary — full detail lives in CLAUDE.md)

- A **two-folder-deep** structure the user actually sees: `company/` (drop zone for
  letterhead, signature, certs, financials) and `bids/<slug>/{source,outputs}`.
  Everything else (`.rfp-kit/`, `.toolkit/`) is internal working state, never
  surfaced to the user.
- A **lettered menu** (Go/No-Go, Synopsis, Risks, Contradictions, Pre-bid questions,
  Fill a form, Draft proposal, Assemble submission) that is always shown after any
  completed task, so the user never has to guess what's possible or type more than
  one letter.
- **Auto-run analysis on parse**: the moment an RFP (or addendum) is parsed, Go/No-Go,
  Synopsis, Risk Review, and Contradiction Check run automatically, unprompted,
  before the menu is ever shown.
- A **4-tab Blueprint Google Sheet** per bid (Analysis Documents / Documents to Create /
  Documents to Collate / Blueprint & Checklist) with matching Drive folders, consistent
  `SIB_<Document_Name>.docx`-style naming, and full cross-referencing between the Sheet's
  rows and the actual Drive files — so nothing is a dead end and nothing has to be
  re-explained across sessions. This kit is Google Sheets-only for tracking; it does not
  use Jira or any other ticketing system.
- **Parallel-by-default execution**: independent work (the four analysis outputs,
  a bid's full document set, Drive uploads, advancing multiple bids at once) is
  dispatched to concurrent sub-agents in a single message, not worked through one
  item at a time. See CLAUDE.md's "PARALLELISING WORK" section for the exact trigger
  list and dispatch pattern — treat that section as binding, not optional, whenever
  2+ independent units of work exist.

## Rule of thumb for applying this skill

Everything under `## GENERAL RULES` in CLAUDE.md applies without exception: never
show the user file paths/JSON, never ask more than one question at a time, always
end with the lettered menu, flag manual actions (wet signatures, stamp paper, demand
drafts) explicitly, and never fabricate a company fact — ask for it, one thing at a
time, if it's missing.

If the user's request implies Google Drive but that connector isn't available, don't
silently skip that part of the workflow — tell the user plainly what's missing (the
Blueprint sheet and Drive-mirrored documents both need it) and offer to proceed with
the parts that don't need it (local documents, analysis markdown files).
