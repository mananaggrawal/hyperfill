Draft the technical or commercial proposal for an RFP.

**Arguments:** `$ARGUMENTS` (format: `<slug> tech` or `<slug> commercial`)

## What you do

1. **Parse arguments:** first word = slug, second = `tech` or `commercial`.
   If missing, ask: "Which proposal — technical or commercial?"

2. **Read everything:**
   - `bids/<slug>/parsed/rfp.md` — full RFP
   - `bids/<slug>/analysis/synopsis.md` — if it exists
   - `bids/<slug>/analysis/go-nogo.md` — requirements and eligibility findings
   - `company/company-info.json`
   - All files in `company/about/`
   - Files in `company/experience/` — select 3–5 most relevant to this RFP's domain

---

## TECHNICAL proposal structure

Mirror the RFP's own section numbering and terminology wherever possible.

```
1. Executive Summary
   - Who we are (2–3 sentences from company/about/overview.md)
   - Our understanding of the requirement
   - Why we are the right partner

2. Understanding of Requirements
   - Restate the buyer's objectives in our own words
   - Key challenges we identified
   - Our approach

3. Proposed Solution / Methodology
   - Solution description (from company/about/technical-capabilities.md)
   - Implementation approach and phases
   - Technologies, platforms, integrations

4. Project Plan
   - Phases, milestones, timeline
   - Must fit within the contract duration from the RFP

5. Team
   - Key personnel (names/roles from company-info.json if available)
   - Team structure for this engagement

6. Past Experience
   - 3–5 projects from company/experience/ most relevant to this RFP
   - Per project: client, scope, contract value, duration, outcome

7. Compliance Matrix
   | RFP Requirement | Our Response | Remarks |
   (list every technical requirement from the RFP)

8. Deviations (if any)
```

---

## COMMERCIAL proposal structure

```
1. Covering Letter (on letterhead, signed)

2. Price Summary
   | Item | Amount (excl. tax) | GST | Total |

3. Detailed Pricing
   ⚠ DO NOT invent any figures. Write [PRICE — fill before submission] for every number.
   Match the line items to the BOQ / price schedule in the RFP exactly.

4. Payment Terms
   State preferred terms; note how they compare to the RFP's stated terms.

5. Price Validity
   As required by the RFP.

6. Assumptions and Exclusions

7. Commercial Deviations (if any)
```

---

## Generate the document

```python
import sys, subprocess
subprocess.run(["pip", "install", "python-docx", "--break-system-packages", "-q"], capture_output=True)

sys.path.insert(0, ".")
from toolkit import docx_builder as db, bidder_profile as bp, paths

profile = bp.load_profile()
bid = paths.bid_dir("<slug>")

body = db.heading("Technical Proposal", size=28)
# Build each section using db.heading(), db.para(), db.table()
# Pull ALL facts from profile.* and company/ files — never hardcode
body += db.sign_block()

filename = "TechProposal.docx"  # or CommercialProposal.docx
db.build_docx(body, bid / "outputs/docx" / filename)
```

**Tell the user:**
"Draft saved to `bids/<slug>/outputs/docx/[filename].docx`.

Before submitting, please:
- Review every section with your team
- Fill in all `[PRICE — fill before submission]` placeholders (commercial)
- Prepare and attach CVs for named personnel (technical)
- Have the authorised signatory sign the covering letter
- ⚠ This is a draft — do not submit without review."
