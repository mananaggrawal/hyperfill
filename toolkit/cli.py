"""
rfpkit — command-line helper for the RFP Response Kit.

Run from the repo root:
    python -m toolkit.cli <command>
or, after `pip install -e .`:
    rfpkit <command>

Commands:
    check            Verify your setup (profile filled, letterhead/signature present, deps).
    new <slug>       Create a new bid folder from the template.
    list             List your knowledge base (company docs, experience proofs) and bids.
    build-pdf <f>    Convert a .docx to PDF (via LibreOffice).
"""

import argparse
import shutil
import sys
from pathlib import Path

from . import paths
from . import bidder_profile as profile

OK, WARN, BAD = "✅", "⚠️ ", "❌"


def cmd_check(_args):
    print("Checking RFP kit setup\n")
    rows = []

    rows.append((profile.is_filled(),
                 "bidder_profile.py filled (legal_name + signatory)",
                 "edit toolkit/bidder_profile.py"))

    try:
        lh = paths.letterhead(); rows.append((True, f"letterhead: {lh.name}", ""))
    except FileNotFoundError:
        rows.append((False, "letterhead .docx", "drop one in assets/letterhead/"))
    try:
        ss = paths.sign_stamp(); rows.append((True, f"signature/stamp: {ss.name}", ""))
    except FileNotFoundError:
        rows.append((False, "signature/stamp image", "drop a PNG in assets/signature-stamp/"))

    try:
        import pypdf  # noqa
        rows.append((True, "pypdf installed", ""))
    except ImportError:
        rows.append((False, "pypdf", "pip install pypdf"))

    soffice = any(shutil.which(c) for c in ("soffice", "libreoffice"))
    rows.append((soffice, "LibreOffice (soffice) on PATH", "install LibreOffice for DOCX->PDF"))

    ndocs = _count(paths.COMPANY_DOCS_DIR)
    rows.append((ndocs > 0, f"company documents: {ndocs}",
                 "add PDFs to company-knowledge/submission-documents/company-documents/"))

    failed = 0
    for ok, label, fix in rows:
        mark = OK if ok else WARN
        line = f"  {mark} {label}"
        if not ok and fix:
            line += f"   -> {fix}"
        print(line)
        failed += 0 if ok else 1
    print()
    print(f"{OK} ready" if failed == 0 else f"{WARN}{failed} item(s) need attention before you can generate documents")
    return 0 if failed == 0 else 1


def cmd_new(args):
    slug = args.slug.strip().lower().replace(" ", "-")
    dest = paths.bid_dir(slug)
    if dest.exists():
        print(f"{BAD} bids/{slug} already exists"); return 1
    shutil.copytree(paths.BID_TEMPLATE, dest)
    print(f"{OK} created bids/{slug}")
    print(f"   1. put the RFP file in bids/{slug}/source/")
    print(f"   2. parse it to bids/{slug}/parsed/")
    print(f"   3. fill bids/{slug}/checklist.md, then generate outputs")
    print(f"   (point Claude Code at this repo and it will follow AGENTS.md)")
    return 0


def cmd_list(_args):
    print("Company documents:")
    _print_dir(paths.COMPANY_DOCS_DIR)
    print("\nExperience proofs:")
    _print_dir(paths.EXPERIENCE_DIR)
    print("\nBids:")
    bids = [p for p in sorted(paths.BIDS_DIR.glob("*"))
            if p.is_dir() and p.name != "_template"]
    if not bids:
        print("  (none yet — `rfpkit new <slug>`)")
    for b in bids:
        print(f"  - {b.name}")
    return 0


def cmd_build_pdf(args):
    from . import pdf_tools
    out = pdf_tools.to_pdf(args.docx)
    print(f"{OK} {out}")
    return 0


_SKIP = {".gitkeep", "README.md", ".DS_Store"}


def _count(folder: Path) -> int:
    if not folder.exists():
        return 0
    return sum(1 for p in folder.iterdir() if p.is_file() and p.name not in _SKIP)


def _print_dir(folder: Path):
    files = [p for p in sorted(folder.glob("*")) if p.is_file() and p.name not in _SKIP]
    if not files:
        print("  (empty — add your files here)")
    for f in files:
        print(f"  - {f.name}")


def main(argv=None):
    p = argparse.ArgumentParser(prog="rfpkit", description="RFP Response Kit helper")
    sub = p.add_subparsers(dest="cmd")
    sub.add_parser("check", help="verify your setup").set_defaults(fn=cmd_check)
    pn = sub.add_parser("new", help="create a new bid folder"); pn.add_argument("slug"); pn.set_defaults(fn=cmd_new)
    sub.add_parser("list", help="list knowledge base and bids").set_defaults(fn=cmd_list)
    pb = sub.add_parser("build-pdf", help="convert a docx to pdf"); pb.add_argument("docx"); pb.set_defaults(fn=cmd_build_pdf)

    args = p.parse_args(argv)
    if not getattr(args, "fn", None):
        p.print_help(); return 0
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
