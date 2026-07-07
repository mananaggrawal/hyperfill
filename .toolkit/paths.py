"""
Central path resolver for Hyperfill.

User-visible structure (two folders only):
  company/                  ← flat drop zone for all company files
  bids/<slug>/
    source/                 ← user drops RFP PDF here
    outputs/                ← user picks up finished docs here
      submission/           ← assembled submission package

Hidden working structure:
  .rfp-kit/
    company-info.json
    about/
    experience/
    bids/<slug>/
      parsed/rfp.md         ← extracted RFP text
      analysis/             ← go-nogo, synopsis, risks, etc.
      checklist.md          ← requirements tracker

  .toolkit/                 ← this file and Python helpers
"""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent  # .toolkit/../ = repo root

# ── User-visible ──────────────────────────────────────────────────────────────
COMPANY_DIR = REPO_ROOT / "company"
BIDS_DIR    = REPO_ROOT / "bids"

# ── Hidden memory + working files ─────────────────────────────────────────────
MEMORY_DIR     = REPO_ROOT / ".rfp-kit"
COMPANY_INFO   = MEMORY_DIR / "company-info.json"
ABOUT_DIR      = MEMORY_DIR / "about"
EXPERIENCE_DIR = MEMORY_DIR / "experience"
WORKING_BIDS   = MEMORY_DIR / "bids"   # parsed, analysis, checklist live here


def working_dir(slug: str) -> Path:
    """Hidden working directory for a bid — parsed RFP, analysis, checklist."""
    return WORKING_BIDS / slug


def bid_dir(slug: str) -> Path:
    """Visible bid folder — source/ and outputs/ only."""
    return BIDS_DIR / slug


def submission_dir(slug: str) -> Path:
    """Final submission package folder."""
    return BIDS_DIR / slug / "outputs" / "submission"


def _first(folder: Path, patterns):
    """Return the first file in folder matching any glob pattern (recursive)."""
    for pat in patterns:
        hits = sorted(
            p for p in folder.rglob(pat)
            if p.name not in (".gitkeep", "README.md") and p.is_file()
        )
        if hits:
            return hits[0]
    return None


def letterhead() -> Path:
    """Letterhead .docx — prefers a file with 'letterhead' in its name."""
    p = _first(COMPANY_DIR, ["*letterhead*.docx"]) or _first(COMPANY_DIR, ["*.docx"])
    if p is None:
        raise FileNotFoundError(
            "No letterhead .docx found. Drop your Word letterhead into the company folder.")
    return p


def sign_stamp() -> Path:
    """Signature image (.png / .jpg) from company/."""
    p = _first(COMPANY_DIR, ["*sign*.png", "*sign*.jpg", "*.png", "*.jpg", "*.jpeg"])
    if p is None:
        raise FileNotFoundError(
            "No signature image found. Drop your signature .png into the company folder.")
    return p


def all_documents() -> list[Path]:
    """All PDF files in company/ — used for submission assembly matching."""
    return sorted(
        p for p in COMPANY_DIR.rglob("*.pdf")
        if p.name not in (".gitkeep", "README.md")
    )


def company_doc(name_fragment: str) -> Path | None:
    """Find a file in company/ whose name contains `name_fragment` (case-insensitive).

    Used for submission assembly — matching a required enclosure (e.g. "GST",
    "incorporation") to whatever the user actually dropped into company/.
    Returns None if nothing matches rather than raising, since submission
    assembly needs to keep going and flag the miss instead of crashing.
    """
    frag = name_fragment.lower()
    hits = sorted(
        p for p in COMPANY_DIR.rglob("*")
        if p.is_file() and p.name not in (".gitkeep", "README.md")
        and frag in p.name.lower()
    )
    return hits[0] if hits else None


def experience_proof(name_fragment: str) -> Path | None:
    """Find a file in .rfp-kit/experience/ whose name contains `name_fragment`."""
    frag = name_fragment.lower()
    if not EXPERIENCE_DIR.exists():
        return None
    hits = sorted(
        p for p in EXPERIENCE_DIR.rglob("*")
        if p.is_file() and p.name not in (".gitkeep", "README.md")
        and frag in p.name.lower()
    )
    return hits[0] if hits else None


if __name__ == "__main__":
    print("Repo root    :", REPO_ROOT)
    print("Company dir  :", COMPANY_DIR)
    print("Memory dir   :", MEMORY_DIR)
    print("Working bids :", WORKING_BIDS)
    for label, fn in [("Letterhead", letterhead), ("Signature", sign_stamp)]:
        try:
            print(f"  {label:12}: {fn()}")
        except FileNotFoundError as e:
            print(f"  {label:12}: MISSING — {e}")
