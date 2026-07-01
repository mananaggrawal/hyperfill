Search the RFP for specific information.

**Arguments:** `$ARGUMENTS` (format: `<slug> <search query>`)

## Steps

1. Parse the arguments:
   - First word = bid slug
   - Remaining words = search query
   - Example: `/search acme-bank-rfp-2026 payment terms` → slug is `acme-bank-rfp-2026`, query is `payment terms`
   - If only one word given, it's the slug — ask: "What would you like to search for in this RFP?"

2. Read `bids/<slug>/parsed/rfp.md`.

3. Find every section of the RFP that is relevant to the query. Look for:
   - Exact keyword matches
   - Synonyms and related terms
   - Sections that contain implicit answers to the query

4. For each relevant passage found, show:
   - The section heading / reference number
   - The relevant paragraph(s), quoted exactly
   - A one-line explanation of why it's relevant to the query

5. If nothing relevant is found, say: "No sections matching '[query]' were found in the RFP. The RFP may not address this topic, or it may be described using different terminology. Try searching for: [suggest 2–3 alternative terms]."

6. At the end, give a direct answer to the query in plain language, synthesising what you found.

## Format

```
## Search results: "[query]" in [slug]

### Result 1 — Section [X.X]: [Section title]
> [Quoted text]

**Relevance:** [One line]

---

### Result 2 — ...

---

## Summary answer
[Direct answer in 2–4 sentences]
```
