Parse an RFP PDF into clean, readable text.

**Arguments:** `$ARGUMENTS` (the bid slug)

## Steps

1. The slug is: `$ARGUMENTS`. If missing, ask which bid to parse.

2. Find the RFP file:
   - Look in `bids/$ARGUMENTS/source/` for any PDF file.
   - If no file found, tell the user: "Please upload the RFP PDF to bids/$ARGUMENTS/source/ and try again."
   - If multiple files found, ask which one to parse.

3. Run the parser:
```python
import sys
sys.path.insert(0, ".")
from toolkit.pdf_tools import parse_pdf_to_markdown
from toolkit.paths import bid_dir

source_files = list((bid_dir("$ARGUMENTS") / "source").glob("*.pdf"))
rfp_path = source_files[0]
output_path = bid_dir("$ARGUMENTS") / "parsed" / "rfp.md"
parse_pdf_to_markdown(rfp_path, output_path)
print(f"Parsed to: {output_path}")
```

4. After parsing, read `bids/$ARGUMENTS/parsed/rfp.md` and:
   - Report the approximate page count and word count
   - List the main sections found (headings)
   - Note anything that looks unusual (e.g. tables that may not have parsed cleanly)

5. Update `bids/$ARGUMENTS/checklist.md` with a first pass of requirements:
   - Eligibility criteria found
   - Annexures / forms required
   - Submission deadline
   - EMD / bid fee amount
   - Submission format (physical / online / email)
   - Mark each as `Pending`

6. Tell the user:
   "✓ RFP parsed successfully. Review bids/$ARGUMENTS/parsed/rfp.md to confirm it looks correct.

   Recommended next commands:
   - /go-nogo $ARGUMENTS  — should we bid?
   - /synopsis $ARGUMENTS — one-page summary"
