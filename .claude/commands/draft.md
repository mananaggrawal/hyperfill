Draft the technical or commercial proposal for an RFP.

**Arguments:** `$ARGUMENTS` (format: `<slug> tech` or `<slug> commercial`)

## Steps

1. Parse the arguments:
   - First word = slug
   - Second word = `tech` or `commercial`
   - If missing, ask: "Which proposal would you like to draft — technical or commercial?"

2. Read these files:
   - `bids/<slug>/parsed/rfp.md` — the full RFP
   - `bids/<slug>/analysis/synopsis.md` — if it exists
   - `bids/<slug>/analysis/go-nogo.md` — to understand requirements and risks
   - `company/company-info.json`
   - All files in `company/about/`
   - All files in `company/experience/` — select the most relevant projects

---

## If drafting TECHNICAL proposal

Structure the document to directly mirror the RFP's evaluation criteria and scope of work.
Use the exact section numbering and terminology from the RFP where possible.

Standard structure (adapt to match RFP requirements):

```
1. Executive Summary
   - Who we are (2–3 sentences)
   - Our understanding of the requirement
   - Why we are the right partner

2. Understanding of Requirements
   - Restate the buyer's objectives in our own words
   - Key challenges we have identified
   - Our approach to addressing them

3. Proposed Solution / Methodology
   - Technical architecture (describe, do not invent specs not in company/about/)
   - Implementation methodology
   - Tools, platforms, and technologies
   - Compliance with each technical specification in the RFP

4. Project Plan
   - Phases and milestones
   - Timeline (must fit within the contract duration stated in the RFP)
   - Dependencies and assumptions

5. Team and Expertise
   - Key personnel proposed (use names/roles from company-info.json if available)
   - Organisational chart for this engagement
   - CVs to be attached (flag as manual)

6. Past Experience / References
   - Select 3–5 projects from company/experience/ most relevant to this RFP
   - For each: client, scope, value, duration, outcome

7. Compliance Matrix
   - Table: each RFP requirement | our response (Compliant / Partially Compliant / Not Compliant) | remarks

8. Deviations (if any)
   - List any areas where full compliance is not possible, with alternatives proposed
```

---

## If drafting COMMERCIAL proposal

```
1. Covering Letter (on letterhead, signed)

2. Price Summary
   - Total bid price (exclusive of tax)
   - GST / taxes
   - Grand total

3. Detailed Price Breakdown
   - Line-item pricing matching the BOQ / price schedule in the RFP
   - ⚠ DO NOT invent prices. Write [PRICE TBD — fill in before submission] for every figure.

4. Payment Terms
   - Reference the company's preferred payment terms
   - Note how they compare to the RFP's stated terms

5. Price Validity
   - State the validity period required by the RFP

6. Assumptions and Exclusions
   - What is included in the price
   - What is excluded (travel, hardware, third-party licences, etc.)

7. Commercial Deviations (if any)
```

---

## Output

Save to `bids/<slug>/outputs/docx/TechProposal.docx` or `CommercialProposal.docx`
using the letterhead template and sign block.

```python
import sys
sys.path.insert(0, ".")
from toolkit import docx_builder as db, bidder_profile as bp, paths

profile = bp.load_profile()
bid = paths.bid_dir("<slug>")

# Build proposal content section by section
# Pull all facts from profile.* and the company/ markdown files
# Never hardcode facts

body = db.heading("Technical Proposal", size=28)
# ... sections ...
body += db.sign_block(profile)

filename = "TechProposal.docx"  # or CommercialProposal.docx
db.build_docx(body, bid / "outputs/docx" / filename)
```

After saving, tell the user:
"✓ Draft saved to bids/<slug>/outputs/docx/[filename].docx

Please review carefully before submission:
- [ ] All [PRICE TBD] placeholders filled (commercial)
- [ ] CV attachments prepared (technical)  
- [ ] Compliance matrix reviewed
- [ ] Sign block signed by authorised signatory
- ⚠ This is a draft — review with your team before submitting."
