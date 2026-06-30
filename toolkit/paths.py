"""
Central path resolver. Every path is resolved RELATIVE to the repo root (the
folder containing this `toolkit/` directory), so the kit works wherever it's
cloned. Do NOT hard-code absolute paths elsewhere — import from here.

Everything the user provides lives under a single `company/` folder. The
letterhead and signature/stamp are discovered by scanning their subfolders, so
you just drop YOUR files in and the toolkit finds them (no filenames to edit).
"""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# --- The one folder the user fills in ---
COMPANY_DIR    = REPO_ROOT / "company"
COMPANY_INFO   = COMPANY_DIR / "company-info.json"
LETTERHEAD_DIR = COMPANY_DIR / "letterhead"
SIGN_STAMP_DIR = COMPANY_DIR / "signature"
DOCUMENTS_DIR  = COMPANY_DIR / "documents"
EXPERIENCE_DIR = COMPANY_DIR / "experience"
ABOUT_DIR      = COMPANY_DIR / "about"

# --- Per-bid task work ---
BIDS_DIR     = REPO_ROOT / "bids"
BID_TEMPLATE = BIDS_DIR / "_template"
EXAMPLES_DIR = REPO_ROOT / "examples"


def _first(folder: Path, patterns):
    for pat in patterns:
        hits = sorted(p for p in folder.glob(pat) if p.name != ".gitkeep")
        if hits:
            return hits[0]
    return None


def letterhead() -> Path:
    """Your letterhead .docx (first one found in company/letterhead/)."""
    p = _first(LETTERHEAD_DIR, ["*.docx"])
    if p is None:
        raise FileNotFoundError(
            f"No letterhead .docx in {LETTERHEAD_DIR}. Drop your letterhead there.")
    return p


def sign_stamp() -> Path:
    """Your signature/stamp image (first found in company/signature/)."""
    p = _first(SIGN_STAMP_DIR, ["*.png", "*.jpg", "*.jpeg"])
    if p is None:
        raise FileNotFoundError(
            f"No signature image in {SIGN_STAMP_DIR}. Drop your signature/stamp PNG there.")
    return p


def bid_dir(slug: str) -> Path:
    return BIDS_DIR / slug


def company_doc(filename: str) -> Path:
    return DOCUMENTS_DIR / filename


def experience_proof(filename: str) -> Path:
    return EXPERIENCE_DIR / filename


if __name__ == "__main__":
    print("Repo root:", REPO_ROOT)
    for label, fn in [("Letterhead", letterhead), ("Signature/stamp", sign_stamp)]:
        try:
            print(f"  {label:16}: OK  {fn()}")
        except FileNotFoundError as e:
            print(f"  {label:16}: MISSING — {e}")
