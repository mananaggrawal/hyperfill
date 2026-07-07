"""
Your organisation's bidder details — loaded from .rfp-kit/company-info.json.

Claude fills this file conversationally (ask one question at a time, then write
the JSON) — there's no wizard or CLI. This module reads that JSON and exposes it
as Python objects the rest of the toolkit uses, so when a fact changes you update
it in ONE place and regenerate. Always write through `save()` rather than the
Write tool directly, so the previous version gets backed up first.
"""

import json
import shutil
from datetime import datetime

from . import paths

# This is the canonical schema for company-info.json. Keep it in sync with
# reality — every field Claude might read via COMPANY/AUTHORISED_SIGNATORY/etc.
# or via the _Profile dot-access wrapper should have a default here.
_DEFAULT = {
    "company": {
        "legal_name": "", "short_name": "", "registration_no": "", "cin": "",
        "tax_id": "", "tan": "", "vat_gst": "", "incorporated_on": "",
        "business_size": "", "registered_office": "", "correspondence_address": "",
        "website": "", "industry_sector": "", "certifications": [],
    },
    "authorised_signatory": {"name": "", "designation": "", "phone": "", "email": "", "pan": ""},
    "bid_opening_rep": {"name": "", "designation": "", "id_number": "", "phone": "", "email": ""},
    "offices": [],
    "escalation_matrix": [],
    "financials": {},
    "banking": {"bank_name": "", "branch": "", "account_no": "", "ifsc": ""},
    "go_nogo_preferences": {
        "min_contract_value": "", "preferred_sectors": [], "avoid_sectors": [],
        "max_bid_timeline_days": None, "notes": "",
    },
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
BANKING              = _data["banking"]
GO_NOGO_PREFERENCES  = _data["go_nogo_preferences"]


def is_filled() -> bool:
    """True once the essentials are filled in."""
    return bool(COMPANY.get("legal_name") and AUTHORISED_SIGNATORY.get("name"))


def reload():
    """Re-read company-info.json (call after `save()` writes it elsewhere)."""
    global _data, COMPANY, AUTHORISED_SIGNATORY, BID_OPENING_REP
    global OFFICES, ESCALATION_MATRIX, FINANCIALS, BANKING, GO_NOGO_PREFERENCES
    _data = _load()
    COMPANY = _data["company"]
    AUTHORISED_SIGNATORY = _data["authorised_signatory"]
    BID_OPENING_REP = _data["bid_opening_rep"]
    OFFICES = _data["offices"]
    ESCALATION_MATRIX = _data["escalation_matrix"]
    FINANCIALS = _data["financials"]
    BANKING = _data["banking"]
    GO_NOGO_PREFERENCES = _data["go_nogo_preferences"]
    return _data


def save(data: dict) -> str:
    """Write company-info.json, backing up the previous version first.

    Keeps a single rolling backup at company-info.backup.json (not a growing
    pile of timestamped files) so an LLM mis-extraction during onboarding can
    always be undone by hand. Returns the path written.
    """
    paths.COMPANY_INFO.parent.mkdir(parents=True, exist_ok=True)
    if paths.COMPANY_INFO.exists():
        backup = paths.COMPANY_INFO.with_name("company-info.backup.json")
        shutil.copy(paths.COMPANY_INFO, backup)
    paths.COMPANY_INFO.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    reload()
    return str(paths.COMPANY_INFO)


class _Profile:
    """Dot-access wrapper around the company-info.json data."""
    def __init__(self, data):
        self._data = data

    @property
    def legal_name(self):      return self._data["company"].get("legal_name", "")
    @property
    def short_name(self):      return self._data["company"].get("short_name", "")
    @property
    def registration_no(self): return self._data["company"].get("registration_no", "")
    @property
    def cin(self):              return self._data["company"].get("cin", "")
    @property
    def tax_id(self):          return self._data["company"].get("tax_id", "")
    @property
    def tan(self):              return self._data["company"].get("tan", "")
    @property
    def vat_gst(self):         return self._data["company"].get("vat_gst", "")
    @property
    def incorporated_on(self): return self._data["company"].get("incorporated_on", "")
    @property
    def business_size(self):   return self._data["company"].get("business_size", "")
    @property
    def registered_office(self): return self._data["company"].get("registered_office", "")
    @property
    def correspondence_address(self): return self._data["company"].get("correspondence_address", "")
    @property
    def website(self):         return self._data["company"].get("website", "")
    @property
    def industry_sector(self): return self._data["company"].get("industry_sector", "")
    @property
    def certifications(self):  return self._data["company"].get("certifications", [])
    @property
    def signatory_name(self):  return self._data["authorised_signatory"].get("name", "")
    @property
    def signatory_designation(self): return self._data["authorised_signatory"].get("designation", "")
    @property
    def signatory_email(self): return self._data["authorised_signatory"].get("email", "")
    @property
    def signatory_phone(self): return self._data["authorised_signatory"].get("phone", "")
    @property
    def signatory_pan(self):   return self._data["authorised_signatory"].get("pan", "")
    @property
    def bid_opening_rep(self): return self._data.get("bid_opening_rep", {})
    @property
    def offices(self):         return self._data.get("offices", [])
    @property
    def escalation_matrix(self): return self._data.get("escalation_matrix", [])
    @property
    def financials(self):      return self._data.get("financials", {})
    @property
    def banking(self):         return self._data.get("banking", {})
    @property
    def go_nogo_preferences(self): return self._data.get("go_nogo_preferences", {})


def load_profile() -> _Profile:
    """Return a dot-access profile object from the current company-info.json."""
    return _Profile(_load())


if __name__ == "__main__":
    print(json.dumps(_data, indent=2))
