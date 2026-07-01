Read the RFP PDF and extract it into structured text.

**Arguments:** `$ARGUMENTS` (the bid slug)

## What you do

You read the RFP PDF directly using your Read tool — no external conversion needed.

1. **Find the PDF.** Look in `bids/$ARGUMENTS/source/` for any PDF file.
   - If none found: "Please upload the RFP PDF to `bids/$ARGUMENTS/source/` and then run this command again."
   - If multiple files found: ask the user which one is the main RFP.

2. **Read the PDF.** Use your Read tool to open the PDF file. You can read PDFs natively.

3. **Extract and structure the content.** As you read, organise the content into clean markdown:
   - Preserve all section headings and numbering
   - Keep tables as markdown tables
   - Keep numbered lists and bullet points
   - Note page breaks with `---`
   - If a section is clearly an annexure/form, mark it with `## ANNEXURE: [name]`

4. **Write to `bids/$ARGUMENTS/parsed/rfp.md`.** Create the file with this structure:
   ```
   # [RFP Title]
   _Source: [filename] | Parsed: [today's date]_

   ---

   [Full structured content]
   ```

5. **After writing, report back:**
   - Approximate length (pages / sections found)
   - List of main sections identified
   - List of annexures/forms found
   - Submission deadline (if visible)
   - Any pages that looked unclear or may need review

6. **Build an initial checklist.** Update `bids/$ARGUMENTS/checklist.md` with every
   requirement, annexure, deadline, and fee/EMD found. Mark all as `Pending`.

Tell the user: "RFP parsed. Here's what I found: [summary]. Ready to run `/go-nogo $ARGUMENTS` or `/synopsis $ARGUMENTS` next."
