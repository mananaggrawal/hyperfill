"""
Central path resolver. Every path is resolved RELATIVE to the repo root (the
folder containing this `toolkit/` directory), so the kit works wherever it's
cloned. Do NOT hard-code absolute paths elsewhere — import from here.

The user drops all their files (flat) into `company/` — no subfolders needed.
Claude's internal memory (company-info.json, extracted context) lives in `.rfp-kit/`,
which is hidden and never shown to the user.
"""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# --- User drop zone (flat — user drops files directly here) ---
COMPANY_DIR  = REPO_ROOT / "company"

# --- Claude's internal memory (hidden from user) ---
MEMORY_DIR   = REPO_ROOT / ".rfp-kit"
COMPANY_INFO = MEMORY_DIR / "company-info.json"
ABOUT_DIR    = MEMORY_DIR / "about"
EXPERIENCE_DIR = MEMORY_DIR / "experience"

# --- Per-bid task work ---
BIDS_DIR     = REPO_ROOT / "bids"
BID_TEMPLATE = BIDS_DIR / "_template"
EXAMPLES_DIR = REPO_ROOT / "examples"


def _first(folder: Path, patterns):
    """Search folder recursively for the first file matching any pattern."""
    for pat in patterns:
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
            "No letterhead .docx found. Drop your Word letterhead file into the company/ folder.")
    return p


def sign_stamp() -> Path:
    """Signature image — found anywhere inside company/."""
    p = _first(COMPANY_DIR, ["*.png", "*.jpg", "*.jpeg"])
    if p is None:
        raise FileNotFoundError(
            "No signature image found. Drop your signature .png file into the company/ folder.")
    return p


def all_documents() -> list:
    """All PDF documents found inside company/."""
    return sorted(p for p in COMPANY_DIR.rglob("*.pdf")
                  if p.name not in (".gitkeep", "README.md"))


def bid_dir(slug: str) -> Path:
    return BIDS_DIR / slug


if __name__ == "__main__":
    print("Repo root:", REPO_ROOT)
    print("Company drop zone:", COMPANY_DIR)
    print("Memory dir:", MEMORY_DIR)
    for label, fn in [("Letterhead", letterhead), ("Signature", sign_stamp)]:
        try:
            print(f"  {label:16}: OK  {fn()}")
        except FileNotFoundError as e:
            print(f"  {label:16}: MISSING — {e}")
