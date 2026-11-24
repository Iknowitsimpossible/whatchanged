"""Build the Claude artifact copy of the site.

index.html is the real page (served by GitHub Pages). The Claude artifact host
wraps every page in its own <html>/<head>/<body> and charset/viewport tags, so
the artifact copy must leave those out. This script strips them and writes the
result to publish/whatchanged.html (git-ignored, since it's generated).

Usage:
    python3 build-artifact.py
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent
SOURCE = ROOT / "index.html"
OUTPUT = ROOT / "publish" / "whatchanged.html"

# Each pattern is anchored to the start of a line (re.MULTILINE), so it only
# removes the real wrapper tags. Text like "<html>" inside a comment survives.
WRAPPER_PATTERNS = [
    r"^<!DOCTYPE html>\n",
    r"^</?html[^>]*>\n?",
    r"^</?head>\n",
    r"^</?body>\n",
    r'^<meta charset="UTF-8">\n',
    r'^<meta name="viewport"[^>]*>\n',
]


def strip_wrapper(html: str) -> str:
    for pattern in WRAPPER_PATTERNS:
        html = re.sub(pattern, "", html, flags=re.IGNORECASE | re.MULTILINE)
    return html


def main() -> None:
    page = strip_wrapper(SOURCE.read_text(encoding="utf-8"))
    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(page, encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
