"""
rfpkit — command-line helper for the RFP Response Kit.

Run from the repo root:
    python -m toolkit.cli <command>
or, after `pip install -e .`:
    rfpkit <command>

Commands:
    init             Guided setup — asks questions and writes company/company-info.json.
    check            Verify your setup (details filled, letterhead/signature present, deps).
    new <slug>       Create a new bid folder from the template.
    list             List your company documents, experience proofs, and bids.
    build-pdf <f>    Convert a .docx to PDF (via LibreOffice).
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

from . import paths
from . import bidder_profile as profile

OK, WARN, BAD = "✅", "⚠️ ", "❌"


# ───────────────────────── init wizard ─────────────────────────

def _ask(label, current=""):
    """Prompt showing the current value; blank input keeps it."""
    shown = f" [{current}]" if current else ""
    try:
        ans = input(f"  {label}{shown}: ").strip()
    except EOFError:
        raise SystemExit("\nNo input available — run `rfpkit init` in an interactive terminal, "
                         "or edit company/company-info.json by hand.")
    return ans or current


def _ask_yes(label, default=False):
    d = "Y/n" if default else "y/N"
    ans = _ask(f"{label} ({d})").lower()
    if not ans:
        return default
    return ans.startswith("y")


def cmd_init(_args):
    print("rfpkit init — let's set up your company. Press Enter to keep the [current] value.\n")
    try:
        data = json.loads(paths.COMPANY_INFO.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"company": {}, "authorised_signatory": {}, "bid_opening_rep": {},
                "offices": [], "escalation_matrix": [], "financials": {}}

    c = data.setdefault("company", {})
    print("Company details")
    c["legal_name"]       = _ask("Legal name", c.get("legal_name", ""))
    c["short_name"]       = _ask("Short name", c.get("short_name", ""))
    c["registration_no"]  = _ask("Registration / company no.", c.get("registration_no", ""))
    c["tax_id"]           = _ask("Tax ID (PAN / EIN / VAT)", c.get("tax_id", ""))
    c["vat_gst"]          = _ask("GST / VAT / sales-tax reg.", c.get("vat_gst", ""))
    c["incorporated_on"]  = _ask("Date of incorporation", c.get("incorporated_on", ""))
    c["business_size"]    = _ask("Business size / MSME status", c.get("business_size", ""))
    c["registered_office"]= _ask("Registered office address", c.get("registered_office", ""))
    c["website"]          = _ask("Website", c.get("website", ""))

    s = data.setdefault("authorised_signatory", {})
    print("\nAuthorised signatory (signs the bid documents)")
    s["name"]        = _ask("Name", s.get("name", ""))
    s["designation"] = _ask("Designation", s.get("designation", ""))
    s["phone"]       = _ask("Phone", s.get("phone", ""))
    s["email"]       = _ask("Email", s.get("email", ""))

    print()
    if _ask_yes("Add a separate bid-opening representative?",
                default=bool(data.get("bid_opening_rep", {}).get("name"))):
        r = data.setdefault("bid_opening_rep", {})
        r["name"]        = _ask("  Name", r.get("name", ""))
        r["designation"] = _ask("  Designation", r.get("designation", ""))
        r["id_number"]   = _ask("  ID number", r.get("id_number", ""))
        r["phone"]       = _ask("  Phone", r.get("phone", ""))
        r["email"]       = _ask("  Email", r.get("email", ""))

    print()
    if _ask_yes("Enter office locations now?", default=not data.get("offices")):
        offices = []
        while True:
            print(f"  Office #{len(offices) + 1} (leave Place blank to stop)")
            place = _ask("  Place")
            if not place:
                break
            offices.append({
                "place": place,
                "address": _ask("  Address"),
                "contact": _ask("  Contact person"),
                "phone": _ask("  Phone"),
                "email": _ask("  Email"),
                "jurisdiction": _ask("  Jurisdiction (e.g. Pan India)"),
            })
        if offices:
            data["offices"] = offices

    print()
    if _ask_yes("Enter audited financials now?", default=not data.get("financials")):
        fin = {}
        while True:
            yr = _ask("  Financial year (e.g. FY2023-24; blank to stop)")
            if not yr:
                break
            fin[yr] = {"turnover": _ask("  Turnover"), "net_worth": _ask("  Net worth")}
        if fin:
            data["financials"] = fin

    paths.COMPANY_INFO.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    profile.reload()
    print(f"\n{OK} saved {paths.COMPANY_INFO.relative_to(paths.REPO_ROOT)}")
    print("   (escalation matrix and any extra fields can be added by editing that file)\n")
    print("Next, drop your files into the company/ folder:")
    print("   • company/letterhead/   — your letterhead .docx")
    print("   • company/signature/    — your signature + stamp image")
    print("   • company/documents/    — registration, tax, financials, certifications")
    print("   • company/experience/   — client agreements / completion certificates")
    print("   • company/about/        — deck, business plan, technical write-ups")
    print("\nThen run:  rfpkit check")
    return 0


# ───────────────────────── other commands ─────────────────────────

def cmd_check(_args):
    print("Checking RFP kit setup\n")
    rows = []
    rows.append((profile.is_filled(),
                 "company details filled (legal name + signatory)",
                 "run `rfpkit init`  (or edit company/company-info.json)"))
    try:
        lh = paths.letterhead(); rows.append((True, f"letterhead: {lh.name}", ""))
    except FileNotFoundError:
        rows.append((False, "letterhead .docx", "drop one in company/letterhead/"))
    try:
        ss = paths.sign_stamp(); rows.append((True, f"signature/stamp: {ss.name}", ""))
    except FileNotFoundError:
        rows.append((False, "signature/stamp image", "drop an image in company/signature/"))
    try:
        import pypdf  # noqa
        rows.append((True, "pypdf installed", ""))
    except ImportError:
        rows.append((False, "pypdf", "pip install -e ."))
    soffice = any(shutil.which(c) for c in ("soffice", "libreoffice"))
    rows.append((soffice, "LibreOffice (soffice) on PATH", "install LibreOffice for DOCX->PDF"))
    ndocs = _count(paths.DOCUMENTS_DIR)
    rows.append((ndocs > 0, f"company documents: {ndocs}",
                 "add PDFs to company/documents/"))

    failed = 0
    for ok, label, fix in rows:
        line = f"  {OK if ok else WARN} {label}"
        if not ok and fix:
            line += f"   -> {fix}"
        print(line)
        failed += 0 if ok else 1
    print()
    print(f"{OK} ready" if failed == 0
          else f"{WARN}{failed} item(s) need attention before you can generate documents")
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
    print("   (point Claude Code at this repo and it will follow AGENTS.md)")
    return 0


def cmd_list(_args):
    print("Company documents:")
    _print_dir(paths.DOCUMENTS_DIR)
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
    print(f"{OK} {pdf_tools.to_pdf(args.docx)}")
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
    sub.add_parser("init", help="guided setup — fills company/company-info.json").set_defaults(fn=cmd_init)
    sub.add_parser("check", help="verify your setup").set_defaults(fn=cmd_check)
    pn = sub.add_parser("new", help="create a new bid folder"); pn.add_argument("slug"); pn.set_defaults(fn=cmd_new)
    sub.add_parser("list", help="list company documents and bids").set_defaults(fn=cmd_list)
    pb = sub.add_parser("build-pdf", help="convert a docx to pdf"); pb.add_argument("docx"); pb.set_defaults(fn=cmd_build_pdf)

    args = p.parse_args(argv)
    if not getattr(args, "fn", None):
        p.print_help(); return 0
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
