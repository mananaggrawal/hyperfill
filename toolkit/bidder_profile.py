"""
Your organisation's bidder details — loaded from company/company-info.json.

You don't edit this file. Fill in your details by running `rfpkit init` (a guided
wizard) or by editing company/company-info.json directly. This module reads that
JSON and exposes it as Python objects the rest of the toolkit uses, so when a fact
changes you update it in ONE place and regenerate.
"""

import json

from . import paths

_DEFAULT = {
    "company": {
        "legal_name": "", "short_name": "", "registration_no": "", "tax_id": "",
        "vat_gst": "", "incorporated_on": "", "business_size": "",
        "registered_office": "", "website": "",
    },
    "authorised_signatory": {"name": "", "designation": "", "phone": "", "email": ""},
    "bid_opening_rep": {"name": "", "designation": "", "id_number": "", "phone": "", "email": ""},
    "offices": [],
    "escalation_matrix": [],
    "financials": {},
}


def _load():
    try:
        with open(paths.COMPANY_INFO, encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return dict(_DEFAULT)
    # merge onto defaults so missing keys never crash callers
    merged = json.loads(json.dumps(_DEFAULT))
    for k, v in data.items():
        if isinstance(v, dict) and isinstance(merged.get(k), dict):
            merged[k].update(v)
        else:
            merged[k] = v
    return merged


_data = _load()

COMPANY              = _data["company"]
AUTHORISED_SIGNATORY = _data["authorised_signatory"]
BID_OPENING_REP      = _data["bid_opening_rep"]
OFFICES              = _data["offices"]
ESCALATION_MATRIX    = _data["escalation_matrix"]
FINANCIALS           = _data["financials"]


def is_filled() -> bool:
    """True once the essentials are filled in (used by `rfpkit check`)."""
    return bool(COMPANY.get("legal_name") and AUTHORISED_SIGNATORY.get("name"))


def reload():
    """Re-read company-info.json (handy after the wizard writes it)."""
    global _data, COMPANY, AUTHORISED_SIGNATORY, BID_OPENING_REP
    global OFFICES, ESCALATION_MATRIX, FINANCIALS
    _data = _load()
    COMPANY = _data["company"]
    AUTHORISED_SIGNATORY = _data["authorised_signatory"]
    BID_OPENING_REP = _data["bid_opening_rep"]
    OFFICES = _data["offices"]
    ESCALATION_MATRIX = _data["escalation_matrix"]
    FINANCIALS = _data["financials"]
    return _data


if __name__ == "__main__":
    print(json.dumps(_data, indent=2))
