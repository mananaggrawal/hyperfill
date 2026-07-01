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
    """Search folder recursively for the first file matching any pattern."""
    for pat in patterns:
        # Search recursively so users can drop files anywhere inside company/
        hits = sorted(p for p in folder.rglob(pat)
                      if p.name not in (".gitkeep", "README.md") and p.is_file())
        if hits:
            return hits[0]
    return None


def letterhead() -> Path:
    """Letterhead .docx — found anywhere inside company/."""
    p = _first(COMPANY_DIR, ["*.docx"])
    if p is None:
        raise FileNotFoundError(
            "No letterhead .docx found in the company/ folder. "
            "Drop your Word letterhead file there.")
    return p


def sign_stamp() -> Path:
    """Signature image — found anywhere inside company/."""
    p = _first(COMPANY_DIR, ["*.png", "*.jpg", "*.jpeg"])
    if p is None:
        raise FileNotFoundError(
            "No signature image found in the company/ folder. "
            "Drop your signature .png file there.")
    return p


def all_documents() -> list:
    """All PDF documents found anywhere inside company/."""
    return sorted(p for p in COMPANY_DIR.rglob("*.pdf")
                  if p.name not in (".gitkeep", "README.md"))


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
