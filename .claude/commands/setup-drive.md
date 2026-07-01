Set up the RFP Kit folder structure on Google Drive automatically.

**Arguments:** `$ARGUMENTS` (optional — a Google Drive path if the user knows it)

## What you do

Google Drive for Desktop mounts the user's Drive as a local folder.
You find that folder, then create the complete RFP Kit structure inside it.
The user never has to do this manually.

---

## Step 1 — Find the Google Drive folder

If the user provided a path in `$ARGUMENTS`, use that. Otherwise, check these common locations:

**Mac:**
```python
import os
from pathlib import Path

candidates = [
    Path.home() / "Google Drive" / "My Drive",
    Path.home() / "Google Drive",
    Path("/Volumes/GoogleDrive/My Drive"),
    Path("/Volumes/GoogleDrive"),
]
# Also check ~/Library/CloudStorage/ (newer Drive for Desktop)
cloud = Path.home() / "Library" / "CloudStorage"
if cloud.exists():
    for d in cloud.iterdir():
        if "Google" in d.name:
            candidates.insert(0, d / "My Drive")
            candidates.insert(1, d)
```

**Windows:**
```python
candidates = [
    Path("G:/My Drive"),
    Path("G:/"),
    Path(os.environ.get("USERPROFILE", "C:/Users/User")) / "Google Drive" / "My Drive",
]
```

Check each candidate. Use the first one that exists.

---

## Step 2 — If Drive not found, ask the user

If none of the candidates exist:

"I couldn't find your Google Drive folder automatically. Could you tell me where it is?

On Mac it's usually at:
  `~/Google Drive/My Drive/`  or  `~/Library/CloudStorage/GoogleDrive-.../My Drive/`

On Windows it's usually at:
  `G:\My Drive\`

You can find it by opening Google Drive for Desktop in your menu bar and clicking 'Open in Finder' (Mac) or 'Open in Explorer' (Windows). Paste the path here and I'll set everything up."

Wait for their response, then use that path.

---

## Step 3 — Confirm with the user

"I found your Google Drive at: `[path]`

I'll create an `RFP-Kit` folder there with all the subfolders you need. Shall I go ahead?"

If they say no, ask where they'd prefer the folder.

---

## Step 4 — Create the full folder structure

```python
import os
from pathlib import Path
import json

drive_path = Path("[confirmed path]")
kit = drive_path / "RFP-Kit"

folders = [
    kit / "company" / "about",
    kit / "company" / "experience",
    kit / "company" / "documents",
    kit / "company" / "letterhead",
    kit / "company" / "signature",
    kit / "bids" / "_template" / "source",
    kit / "bids" / "_template" / "parsed",
    kit / "bids" / "_template" / "analysis",
    kit / "bids" / "_template" / "outputs" / "docx",
    kit / "bids" / "_template" / "outputs" / "pdf",
    kit / "bids" / "_template" / "submission",
]

for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)

# Write a blank company-info.json if it doesn't exist
info_path = kit / "company" / "company-info.json"
if not info_path.exists():
    # Copy from local repo's company/company-info.json
    import shutil
    shutil.copy("company/company-info.json", info_path)

# Write a drive-config.json to record where Drive is
config = {"drive_kit_path": str(kit)}
(Path(".") / "drive-config.json").write_text(json.dumps(config, indent=2))
```

Also copy these framework files into the Drive folder (so the team can use them without cloning):
- `CLAUDE.md`
- `AGENTS.md`
- `.claude/` directory (all slash commands)
- `toolkit/` directory
- `company/` README files
- `bids/` README and `_template/`
- `docs/`

```python
import shutil
from pathlib import Path

src = Path(".")  # current repo
dst = kit

for item in ["CLAUDE.md", "AGENTS.md", "docs", "toolkit", "bids/_template"]:
    s = src / item
    d = dst / item
    if s.is_file():
        shutil.copy2(s, d)
    elif s.is_dir():
        if d.exists():
            shutil.rmtree(d)
        shutil.copytree(s, d)

# Copy .claude/commands/
shutil.copytree(src / ".claude", dst / ".claude", dirs_exist_ok=True)

# Copy company README files (not the data files)
for readme in (src / "company").rglob("README.md"):
    rel = readme.relative_to(src / "company")
    target = dst / "company" / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(readme, target)
```

---

## Step 5 — Ask about company setup

"Your RFP Kit folder is ready on Google Drive at `[kit path]`.

Now let's set up your company profile. This is a one-time step — I'll ask you a few questions and fill everything in for you.

**What is your company's full legal name?**"

Then walk through the key fields conversationally:
- Legal name → short name
- Registration / company number
- GST / tax ID
- Registered office address
- Authorised signatory name and designation
- Their phone and email
- Last 3 years of turnover (optional — say they can add later)

After collecting answers, write them all to `[kit path]/company/company-info.json`.

---

## Step 6 — Final instructions

"You're all set! Here's what to do next:

**For your team:**
1. Install [Google Drive for Desktop](https://www.google.com/drive/download/) on each person's computer
2. They'll see the `RFP-Kit` folder appear in their Drive automatically
3. To use it: open Claude Code → File → Open Folder → select the `RFP-Kit` folder on their Drive

**To start your first RFP:**
1. Upload the RFP PDF to `bids/_template/source/` — or run `/new <bid-name>` first
2. Tell me: 'Start a new bid for [buyer name]'

**Still needed from you:**
- Upload your company letterhead (.docx) to `company/letterhead/`
- Upload your signature image (.png) to `company/signature/`
- Upload your certificates and documents to `company/documents/`

See the README files in each folder for exactly what to upload."
