"""
Letterhead-based DOCX builder.

Mechanics (reusable for any organisation):
  1. copy your letterhead .docx (preserves logo, header, footer)
  2. inject WordprocessingML into document.xml just before <w:sectPr>
  3. embed your signature/stamp image under a relationship ID that's
     guaranteed free in that specific letterhead (never hardcoded — some
     letterheads already use rId9 for their own logo)
  4. repack the .docx

Compose the body with the helpers (para / heading / table / tr / tc / sign_block),
then call build_docx(body_xml, output_path). Content is bid-specific; plumbing isn't.
"""

import os
import re
import shutil
import zipfile
from datetime import datetime

from . import paths
from . import bidder_profile as profile

FONT = "Arial"

# sign_block() can't know the final relationship ID until build_docx() has
# inspected the specific letterhead's existing relationships, so it emits
# this placeholder and build_docx() substitutes the real, free rId before
# injecting the body into document.xml.
_SIGN_RID_PLACEHOLDER = "{{SIGN_IMAGE_RID}}"


# ───────────────────────── XML helpers ─────────────────────────

def xml_escape(text: str) -> str:
    return (str(text).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def para(text, bold=False, size=22, after=160, align="left", italic=False):
    b  = "<w:b/>" if bold else ""
    it = "<w:i/>" if italic else ""
    jc = f'<w:jc w:val="{align}"/>' if align != "left" else ""
    rpr = f'<w:rPr><w:rFonts w:ascii="{FONT}" w:hAnsi="{FONT}"/><w:sz w:val="{size}"/>{b}{it}</w:rPr>'
    return (f'<w:p><w:pPr><w:spacing w:after="{after}"/>{jc}{rpr}</w:pPr>'
            f'<w:r>{rpr}<w:t xml:space="preserve">{xml_escape(text)}</w:t></w:r></w:p>')


def heading(text, size=26, after=120):
    return para(text, bold=True, size=size, after=after, align="center")


def tc(width, text, bold=False, fill="FFFFFF", size=20, colspan=1):
    """Table cell. Newlines in `text` become separate paragraphs."""
    b = "<w:b/>" if bold else ""
    paras = ""
    for line in xml_escape(text).split("\n"):
        paras += (f'<w:p><w:pPr><w:spacing w:after="60"/></w:pPr>'
                  f'<w:r><w:rPr><w:rFonts w:ascii="{FONT}" w:hAnsi="{FONT}"/>'
                  f'<w:sz w:val="{size}"/>{b}</w:rPr>'
                  f'<w:t xml:space="preserve">{line}</w:t></w:r></w:p>')
    span = f'<w:gridSpan w:val="{colspan}"/>' if colspan > 1 else ""
    return (f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{span}'
            f'<w:shd w:val="clear" w:color="auto" w:fill="{fill}"/></w:tcPr>{paras}</w:tc>')


def tr(*cells):
    return f'<w:tr>{"".join(cells)}</w:tr>'


def _tbl_borders():
    edge = '<w:{0} w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
    return ("<w:tblBorders>" + "".join(edge.format(e) for e in
            ("top", "left", "bottom", "right", "insideH", "insideV")) + "</w:tblBorders>")


def table(col_widths, rows):
    """Bordered table. `rows` is a list of tr(...) strings."""
    total = sum(col_widths)
    grid = "".join(f'<w:gridCol w:w="{w}"/>' for w in col_widths)
    return (f'<w:tbl><w:tblPr><w:tblStyle w:val="TableGrid"/>'
            f'<w:tblW w:w="{total}" w:type="dxa"/>{_tbl_borders()}'
            f'<w:tblLook w:val="04A0"/></w:tblPr>'
            f'<w:tblGrid>{grid}</w:tblGrid>{"".join(rows)}</w:tbl>')


def sign_block(date_str=None, signatory=None, place=None):
    """Signature/stamp image followed by name/designation from the profile."""
    if date_str is None:
        date_str = datetime.now().strftime("%d %B %Y")
    s = signatory or profile.AUTHORISED_SIGNATORY
    place = place or profile.COMPANY.get("short_name") or ""
    img = (
        '<w:p><w:pPr><w:spacing w:before="400" w:after="80"/></w:pPr><w:r><w:drawing>'
        '<wp:inline distT="0" distB="0" distL="0" distR="0" '
        'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing">'
        '<wp:extent cx="1828800" cy="888693"/><wp:effectExtent l="0" t="0" r="0" b="0"/>'
        '<wp:docPr id="100" name="Signature"/>'
        '<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
        '<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        '<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        '<pic:nvPicPr><pic:cNvPr id="0" name="Signature"/><pic:cNvPicPr/></pic:nvPicPr>'
        f'<pic:blipFill><a:blip r:embed="{_SIGN_RID_PLACEHOLDER}" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"/>'
        '<a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
        '<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="1828800" cy="888693"/></a:xfrm>'
        '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>'
        '</pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>'
    )
    return (img
            + para(f"Name: {s.get('name','')}", bold=True, after=80)
            + para(f"Designation: {s.get('designation','')}", bold=True, after=80)
            + para(f"For {profile.COMPANY.get('legal_name','')}", bold=True, after=80)
            + para(f"Place: {place}\t\t\tDate: {date_str}", bold=True, after=80))


# ───────────────────────── core build ─────────────────────────

def _free_relationship_id(rels_xml: str) -> str:
    """Return an rId not already used in this letterhead's relationships file."""
    used = {int(n) for n in re.findall(r'Id="rId(\d+)"', rels_xml)}
    n = 1
    while n in used:
        n += 1
    return f"rId{n}"


def _free_media_filename(media_dir: str, ext: str = ".png") -> str:
    """Return a media filename that doesn't already exist in the letterhead's
    word/media/ folder, so we never overwrite an existing embedded image."""
    n = 1
    while True:
        candidate = f"hyperfill_image{n}{ext}"
        if not os.path.exists(os.path.join(media_dir, candidate)):
            return candidate
        n += 1


def build_docx(body_xml: str, output_path: str, letterhead=None, sign_image=None) -> str:
    """Clone the letterhead, inject body_xml before <w:sectPr>, embed the
    signature image under a relationship ID that's free in this specific
    letterhead, and write the finished .docx to output_path."""
    import tempfile

    letterhead = str(letterhead or paths.letterhead())
    sign_image = str(sign_image or paths.sign_stamp())
    output_path = str(output_path)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Build in a local system temp dir rather than alongside output_path —
    # some synced/cloud-backed mounts (iCloud Drive, OneDrive, etc.) briefly
    # lock newly-extracted files and refuse unlink/rmtree on them, which
    # breaks cleanup if we build in-place inside a synced folder.
    temp_dir = tempfile.mkdtemp(prefix="hyperfill_docx_build_")
    staged_docx = os.path.join(temp_dir, "_staged.docx")
    shutil.copy(letterhead, staged_docx)

    extract_dir = os.path.join(temp_dir, "extracted")
    os.makedirs(extract_dir)
    with zipfile.ZipFile(staged_docx, "r") as zf:
        zf.extractall(extract_dir)
    temp_dir = extract_dir  # rest of the function uses temp_dir as the extraction root

    # Only touch media/relationships if the body actually uses sign_block() —
    # documents without a signature shouldn't gain an unused image + relationship.
    if _SIGN_RID_PLACEHOLDER in body_xml:
        media = os.path.join(temp_dir, "word", "media")
        os.makedirs(media, exist_ok=True)
        media_filename = _free_media_filename(media)
        shutil.copy(sign_image, os.path.join(media, media_filename))

        rels_path = os.path.join(temp_dir, "word", "_rels", "document.xml.rels")
        with open(rels_path, encoding="utf-8") as f:
            rels = f.read()
        sign_rid = _free_relationship_id(rels)
        rel = (f'<Relationship Id="{sign_rid}" '
               'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" '
               f'Target="media/{media_filename}"/>')
        rels = rels.replace("</Relationships>", rel + "</Relationships>")
        with open(rels_path, "w", encoding="utf-8") as f:
            f.write(rels)

        # Now that we know the free rId, resolve the placeholder sign_block()
        # left in the body before injecting it into document.xml.
        body_xml = body_xml.replace(_SIGN_RID_PLACEHOLDER, sign_rid)

    doc_xml = os.path.join(temp_dir, "word", "document.xml")
    with open(doc_xml, encoding="utf-8") as f:
        content = f.read()
    sectpr = content.find("<w:sectPr>")
    last_p = content.rfind("</w:p>", 0, sectpr)
    content = content[:last_p + 6] + body_xml + content[last_p + 6:]
    with open(doc_xml, "w", encoding="utf-8") as f:
        f.write(content)

    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as docx:
        for root, _, files in os.walk(temp_dir):
            for fn in files:
                fp = os.path.join(root, fn)
                docx.write(fp, os.path.relpath(fp, temp_dir))

    shutil.rmtree(temp_dir)
    return output_path
