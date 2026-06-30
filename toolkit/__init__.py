"""Reusable, config-driven toolkit for generating bid documents.

Modules:
    paths          - repo-relative path resolver (no absolute paths anywhere else)
    bidder_profile - single source of truth for YOUR organisation's bidder details
    docx_builder   - letterhead-based DOCX builder + content helpers
    pdf_tools      - DOCX -> PDF conversion and PDF merging
    cli            - the `rfpkit` command-line interface
"""

from . import paths, bidder_profile, docx_builder, pdf_tools  # noqa: F401
