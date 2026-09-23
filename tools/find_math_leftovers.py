"""Lokalizuje pozostale problemy renderowania matematyki na GitHubie:
  * $$...$$ w linii z tekstem (poza poczatkiem linii),
  * znak | wewnatrz math w wierszu tabeli.

Uruchomienie:
    python tools/find_math_leftovers.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"tools", "_tmp", ".git", "node_modules"}
FULL_BLOCK = re.compile(r"^\s*\$\$.+?\$\$\s*$", re.S)


def main() -> int:
    for path in sorted(ROOT.rglob("*.md")):
        if any(x in path.parts for x in SKIP):
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        fence = False
        for i, line in enumerate(lines, 1):
            st = line.strip()
            if st.startswith("```") or st.startswith("~~~"):
                fence = not fence
                continue
            if fence:
                continue
            if "$$" in line and not FULL_BLOCK.match(line) and not st.startswith("$$"):
                if line.count("$$") >= 2:
                    print(f"[$$ w linii z tekstem] {path.relative_to(ROOT)}:{i}: {st[:100]}")
            if st.startswith("|"):
                for seg in re.findall(r"\$([^$\n]+)\$", line):
                    if re.search(r"(?<!\\)\|", seg):
                        print(f"[| w math w tabeli]  {path.relative_to(ROOT)}:{i}: {st[:100]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
