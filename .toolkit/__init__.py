"""Reusable, config-driven toolkit for generating bid documents.

There is no CLI and no scripts for the user to run — Claude imports and calls
these modules directly as part of the conversation. See CLAUDE.md at the repo
root for the operating rules.

Modules:
    paths          - repo-relative path resolver (no absolute paths anywhere else)
    bidder_profile - single source of truth for YOUR organisation's bidder details
    docx_builder   - letterhead-based DOCX builder + content helpers
    xlsx_builder   - spreadsheet builder for Excel annexures, BOQs, pricing sheets
    pdf_tools      - PDF parsing, DOCX -> PDF conversion, and PDF merging
"""

from . import paths, bidder_profile, docx_builder, xlsx_builder, pdf_tools  # noqa: F401
