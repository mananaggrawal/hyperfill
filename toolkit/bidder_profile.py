"""
SINGLE SOURCE OF TRUTH for your organisation's bidder details.

Fill this in once with YOUR company's information. Every annexure / proposal /
declaration pulls facts from here instead of re-typing them, so when something
changes you update it ONCE and regenerate. Keep this in sync with
company-knowledge/master-data.md.

Everything below ships blank on purpose — this is a framework, not a company.
"""

COMPANY = {
    "legal_name":        "",   # e.g. "Acme Technologies Private Limited"
    "short_name":        "",
    "registration_no":   "",   # CIN / company number
    "tax_id":            "",   # PAN / EIN / VAT — whatever applies in your country
    "vat_gst":           "",   # GST / VAT / sales-tax registration
    "secondary_tax_id":  "",   # TAN or other, optional
    "incorporated_on":   "",   # e.g. "17 June 2022"
    "msme_or_size":      "",   # business size / MSME / SME status, if relevant
    "registered_office": "",
    "website":           "",
}

# Person who signs the bid documents. The signature/stamp image goes in
# assets/signature-stamp/ and is inserted automatically by docx_builder.sign_block().
AUTHORISED_SIGNATORY = {
    "name":        "",
    "designation": "",
    "phone":       "",
    "email":       "",
}

# Person authorised to attend bid opening (if the RFP requires one).
BID_OPENING_REP = {
    "name":        "",
    "designation": "",
    "id_number":   "",
    "phone":       "",
    "email":       "",
}

# List your offices. Each: place, address, contact, phone, email, jurisdiction.
OFFICES = [
    # {"place": "", "address": "", "contact": "", "phone": "", "email": "", "jurisdiction": ""},
]

# Support / escalation matrix (L1 -> Ln), if the RFP asks for one.
ESCALATION_MATRIX = [
    # {"level": "L1", "name": "", "designation": "", "phone": "", "email": ""},
]

# Financials per year, e.g. {"FY2023-24": {"turnover": "", "net_worth": ""}}.
# Always verify against the audited statements you attach.
FINANCIALS = {
    # "FY2023-24": {"turnover": "", "net_worth": ""},
}


def is_filled() -> bool:
    """True once the essentials are filled in (used by `rfpkit check`)."""
    return bool(COMPANY["legal_name"] and AUTHORISED_SIGNATORY["name"])


if __name__ == "__main__":
    import json
    print(json.dumps({
        "COMPANY": COMPANY, "AUTHORISED_SIGNATORY": AUTHORISED_SIGNATORY,
        "BID_OPENING_REP": BID_OPENING_REP, "OFFICES": OFFICES,
        "ESCALATION_MATRIX": ESCALATION_MATRIX, "FINANCIALS": FINANCIALS,
    }, indent=2))
