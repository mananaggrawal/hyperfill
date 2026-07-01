#!/bin/bash
# RFP Kit — one-time setup
# Double-click this file on Mac, or run: bash setup.sh

set -e

echo ""
echo "================================================"
echo "  RFP Kit Setup"
echo "================================================"
echo ""

# Check Python
if ! command -v python3 &>/dev/null; then
  echo "ERROR: Python 3 is not installed."
  echo "Download it from https://www.python.org/downloads/ and run this again."
  exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(sys.version_info.minor)')
if [ "$PYTHON_VERSION" -lt 9 ]; then
  echo "ERROR: Python 3.9 or newer is required."
  exit 1
fi

echo "✓ Python 3 found"

# Create virtual environment if needed
if [ ! -d ".venv" ]; then
  echo "→ Creating virtual environment..."
  python3 -m venv .venv
fi

# Activate and install
echo "→ Installing dependencies..."
source .venv/bin/activate
pip install --quiet --upgrade pip
pip install --quiet -e .

echo ""
echo "✓ Dependencies installed"
echo ""

# Run the check
echo "→ Checking your company profile..."
python3 -m toolkit.cli check

echo ""
echo "================================================"
echo "  Setup complete!"
echo ""
echo "  Next steps:"
echo "  1. Fill in company/company-info.json"
echo "  2. Upload your documents to company/documents/"
echo "  3. Open Claude Code in this folder:"
echo "       cd $(pwd) && claude"
echo "================================================"
echo ""

# Keep terminal open on Mac double-click
if [[ "$TERM_PROGRAM" == "" ]]; then
  read -p "Press Enter to close..."
fi
