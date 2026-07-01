"""
PDF helpers for bid assembly:
  - parse_pdf_to_markdown(): extract text from an RFP PDF → structured markdown
  - to_pdf():  convert a .docx to .pdf via LibreOffice (soffice, headless)
  - merge():   concatenate an ordered list of PDFs into one combined PDF
"""

import os
import re
import shutil
import subprocess
from pathlib import Path

try:
    import pdfplumber
except ImportError:  # pragma: no cover
    pdfplumber = None

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:  # pragma: no cover
    PdfReader = PdfWriter = None


# ─────────────────────── PDF → Markdown parser ───────────────────────────────

def parse_pdf_to_markdown(pdf_path, output_path) -> str:
    """Extract text from a digital PDF and write clean markdown to output_path.

    Preserves headings, numbered lists, and tables as best as pdfplumber allows.
    Returns the output path as a string.
    """
    if pdfplumber is None:
        raise RuntimeError(
            "pdfplumber not installed. Run: pip install pdfplumber --break-system-packages"
        )

    pdf_path = Path(pdf_path)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    lines_out = []
    lines_out.append(f"# {pdf_path.stem}\n")
    lines_out.append(f"_Parsed from: {pdf_path.name}_\n\n---\n")

    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        for page_num, page in enumerate(pdf.pages, 1):
            lines_out.append(f"\n<!-- Page {page_num} of {total_pages} -->\n")

            # Extract tables first, then text
            tables = page.extract_tables()
            text = page.extract_text(x_tolerance=3, y_tolerance=3) or ""

            if tables:
                for table in tables:
                    if not table or not table[0]:
                        continue
                    md_table = _table_to_markdown(table)
                    if md_table:
                        lines_out.append(md_table + "\n")

            if text:
                lines_out.append(_clean_text(text) + "\n")

    content = "\n".join(lines_out)
    output_path.write_text(content, encoding="utf-8")
    print(f"✓ Parsed {total_pages} pages → {output_path}")
    return str(output_path)


def _table_to_markdown(table) -> str:
    """Convert a pdfplumber table (list of lists) to a markdown table."""
    if not table:
        return ""
    rows = []
    for i, row in enumerate(table):
        cells = [str(c or "").replace("\n", " ").strip() for c in row]
        rows.append("| " + " | ".join(cells) + " |")
        if i == 0:
            rows.append("|" + "|".join(["---"] * len(cells)) + "|")
    return "\n".join(rows)


def _clean_text(text: str) -> str:
    """Light cleanup: collapse excessive blank lines, promote numbered headings."""
    lines = text.splitlines()
    out = []
    prev_blank = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if not prev_blank:
                out.append("")
            prev_blank = True
            continue
        prev_blank = False
        # Promote lines that look like section headings (ALL CAPS or numbered)
        if re.match(r'^(\d+\.)+\s+[A-Z]', stripped) and len(stripped) < 120:
            out.append(f"\n## {stripped}")
        elif stripped.isupper() and 5 < len(stripped) < 100:
            out.append(f"\n## {stripped}")
        else:
            out.append(stripped)
    return "\n".join(out)


def _soffice() -> str:
    for cand in ("soffice", "libreoffice", "/opt/homebrew/bin/soffice",
                 "/Applications/LibreOffice.app/Contents/MacOS/soffice"):
        if shutil.which(cand) or os.path.exists(cand):
            return cand
    raise RuntimeError("LibreOffice (soffice) not found — install it to convert DOCX -> PDF.")


def to_pdf(docx_path: str, out_dir: str = None) -> str:
    """Convert a .docx to .pdf in out_dir (defaults to the docx's folder). Returns the pdf path."""
    docx_path = str(docx_path)
    out_dir = str(out_dir or os.path.dirname(docx_path))
    os.makedirs(out_dir, exist_ok=True)
    subprocess.run([_soffice(), "--headless", "--convert-to", "pdf",
                    "--outdir", out_dir, docx_path], check=True,
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pdf = os.path.join(out_dir, os.path.splitext(os.path.basename(docx_path))[0] + ".pdf")
    if not os.path.exists(pdf):
        raise RuntimeError(f"Conversion produced no PDF for {docx_path}")
    return pdf


def merge(parts, output_path: str) -> str:
    """Merge PDFs in order into output_path.

    `parts` is a list of file paths, or of (label, path) tuples. Missing files
    are skipped with a warning so an incomplete run still produces a usable PDF.
    """
    if PdfWriter is None:
        raise RuntimeError("pypdf not installed. Run: pip install pypdf --break-system-packages")
    os.makedirs(os.path.dirname(str(output_path)), exist_ok=True)
    writer = PdfWriter()
    missing = []
    for part in parts:
        label, path = part if isinstance(part, (tuple, list)) else (os.path.basename(str(part)), part)
        path = str(path)
        if not os.path.exists(path):
            print(f"  ⚠️  MISSING: {label} -> {path}")
            missing.append(label)
            continue
        for page in PdfReader(path).pages:
            writer.add_page(page)
        print(f"  ✓  appended: {label}")
    with open(output_path, "wb") as f:
        writer.write(f)
    print(f"→ saved: {output_path}")
    if missing:
        print(f"  ({len(missing)} missing: {', '.join(missing)})")
    return str(output_path)
