# Business proposal structure

How Vegapay's commercial/technology proposals (as opposed to RFP submission
documents) are structured. This applies when the ask is a standalone sales
proposal for a product/module — e.g. "write a proposal for X for client Y",
not a tender response. The canonical, living version of these conventions
lives in the **Proposal Builder** project (`_Templates/PROPOSAL_INSTRUCTIONS.md`
and `_Templates/VEGAPAY.md`) — this file mirrors the same rules so hyperfill
can produce a consistent proposal if asked, and should be kept in sync with it.

## File & folder conventions

- One folder per product line (e.g. `Credit Cards`, `Credit Line on UPI`,
  `Credit Line Management System`, `Forex Card Management System`). Create a
  new folder the first time a product line gets a proposal.
- Generic/template proposal (no named client): `Vegapay_<Product>_Proposal.docx`
  (version bumps: `_v2`, `_v3`, …).
- Client-specific proposal: `Vegapay_<ClientName>_<Product>_Proposal.docx`
  (e.g. `Vegapay_FederalBank_CLMS_Proposal.docx`).
- Draft/iterate in a scratch folder; only the final, reviewed version gets
  copied into the client-facing project folder.

## Two structural variants — pick based on scope

**Multi-module** (e.g. LOS+BRE+CCMS+Rewards bundled) — title page has a 3–4
column shaded "summary strip" table previewing each module; body has
"2. Product Offerings" with one `2.x` subsection per module (paragraph +
optional capability table + "Key Capabilities" bullets); includes a
"Why Vegapay" section; Commercial Terms uses a Year 1 flat-fee / Year 2+
usage-based structure with a "Module-Level Pricing" table (one row per
module).

**Single-module** (e.g. CLMS-only, FXCMS-only) — much leaner. Title page has
a single centered shaded box (module code + full name, no strip) instead of
the summary strip. Body is just: "1. About Vegapay" → "2. Product Offerings"
(one intro line + one `2.1` subsection for the single module, one paragraph,
no capability tables, no bullet lists) → "3. Commercial Terms" with a
"`<Module>` Pricing" sub-header, an optional one-time-setup-fee banner row
(spans the full table width, shaded, centered), then a 2-column
"Fee Component | Rate" table (rows like "Monthly minimum billing",
"Per user fee", "Spend/Processing fee" — stack multiple lines in one cell
for tiered/slab or year-differentiated values). **No "Why Vegapay" section
and no capability/lifecycle tables in this variant.**

- **Client-specific** single/multi-module proposals name the client in the
  subtitle ("For `<Client>`") and the header's right-hand cell (client
  logo/name).
- **Generic/template** proposals (no client given) use a subtitle like
  "Platform Proposal" instead of "For `<Client>`", and the header's
  right-hand cell shows the product name instead of a client logo.

## Standard section order (single-module)

1. Title page: Title → Subtitle → one intro paragraph → module box → muted
   byline (`Month Year · Confidential · contact@vegapay.tech`).
2. **1. About Vegapay** — one short paragraph, company identity + platform
   scope.
3. **2. Product Offerings** — one intro line, then `2.1 <Module>`.
4. **3. Commercial Terms** — pricing table + notes + confidentiality line.
5. Signature block (2-column borderless table: name/title/email left,
   Vegapay logo right).

## Commercial section conventions

Vegapay commercial models are typically a blend of:

- **One-time platform setup fee** — billed at signing, shown as a banner row
  spanning the pricing table.
- **Monthly minimum billing** — a floor commitment; if it differs by
  contract year (e.g. lower in Year 1 to ease ramp-up), show each year on its
  own line inside the same cell (`Year 1: ₹X per month` / `Year 2 onwards:
  ₹Y per month`), and note it's whichever is higher vs. the usage-based fees.
- **Per-user fee** — tiered/slab by active-user count. State whether the
  tier is whole-base (single rate applies to the entire active user count —
  Vegapay's default) or graduated/marginal (like income-tax slabs); default
  to whole-base and flag the assumption if not specified, offering graduated
  as an alternative.
- **Spend/processing fee** — basis points (bps) on transaction/spend value;
  1 bps = 0.01%.
- All fees exclusive of GST; billing monthly in arrears; Change Requests
  outside agreed scope billed separately (Vegapay standard: ₹15,000/man-day).

## Visual design spec

- Font: Arial throughout.
- Page: US Letter (12240×15840 DXA), margins top/bottom 1000 DXA, left/right
  1080 DXA.
- Colors: Navy `#1B2B6B` (titles, headings, table header fill), Orange
  `#E8882A` (subtitle/accent, email links), Body `#2D3748`, Muted grey
  `#6B7280` (captions/footnotes/dates), row tint `#F5F6FA`, summary-strip /
  module-box shade `#E8ECF2`, table borders `#CCCCCC` (0.5pt).
- Header (every page): borderless 2-column table — Vegapay logo left, client
  name/logo (or product name for generic proposals) right — then a single
  navy bottom-border rule. No footer, no page numbers.
- Type scale: Title 36pt bold navy · Subtitle 15pt orange (not bold) ·
  H1 36 (18pt) bold navy (`"1.  Heading"`) · H2 26 (13pt) bold navy
  (`"1.1  Heading"`) · body 22 (11pt) · table body 19–20 (9.5–10pt) · table
  header 19 (9.5pt) bold white on navy · footnotes 17–18 (8.5–9pt) muted
  grey italic.
- Bullets: en-dash `–`, never a round bullet.
- Tables: navy header row, white bold text; body rows alternate white /
  `#F5F6FA`; 0.5pt `#CCCCCC` borders; numeric columns centered, labels
  left-aligned.
- Signature block: name (bold navy) → title/company (body color) → email
  (orange) → Vegapay logo → italic muted-grey confidentiality line.

## Tone & audience

Bank/NBFC decision-makers (CXOs, product heads, IT heads) — professional,
precise, no filler fintech buzzwords. Use tables for anything comparative or
numeric rather than long prose. Only include sections relevant to the
requested scope.

## Build process

1. Confirm scope: which module(s), which client (or generic/template),
   which commercial terms — ask rather than invent numbers.
2. Draft content section-by-section before touching formatting.
3. Build the `.docx` (docx-js or `.toolkit/docx_builder.py`, whichever
   environment applies) following the house style above.
4. Render to PDF and visually check before delivering.
5. Save the final file into the correct product folder; don't overwrite
   prior versions — increment the version suffix.

*Last synced from Proposal Builder's `PROPOSAL_INSTRUCTIONS.md`/`VEGAPAY.md`: 2026-07-20.*
