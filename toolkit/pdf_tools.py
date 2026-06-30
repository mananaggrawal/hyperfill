"""
PDF helpers for bid assembly:
  - to_pdf():  convert a .docx to .pdf via LibreOffice (soffice, headless)
  - merge():   concatenate an ordered list of PDFs into one combined PDF

These are the two mechanical steps every bid repeats: render each filled
annexure to PDF, then merge each annexure with the supporting documents that
must travel with it (see each bid's manifest / checklist for what goes where).
"""

import os
import shutil
import subprocess

try:
    from pypdf import PdfReader, PdfWriter
except ImportError:  # pragma: no cover
    PdfReader = PdfWriter = None


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
