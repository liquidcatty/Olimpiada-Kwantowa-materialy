"""Analiza form zapisu blokow $$ i ich sasiedztwa (bez uzywania shella).

Uruchomienie:
    python tools/analyze_dollar_forms.py
"""

from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"tools", "_tmp", ".git", "node_modules"}


def main() -> int:
    forms: collections.Counter[str] = collections.Counter()
    close_before_text = 0
    close_examples: list[str] = []
    for path in sorted(ROOT.rglob("*.md")):
        if any(x in path.parts for x in SKIP):
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        fence = False
        inside = False
        for i, line in enumerate(lines):
            st = line.strip()
            if st.startswith("```") or st.startswith("~~~"):
                fence = not fence
                continue
            if fence:
                continue
            if st == "$$":
                forms["osobna linia $$"] += 1
                if inside:
                    inside = False
                    nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
                    if nxt and not nxt.startswith("$$") and not nxt.startswith("#"):
                        close_before_text += 1
                        close_examples.append(f"{path.relative_to(ROOT)}:{i + 1}")
                else:
                    inside = True
            elif st.startswith("$$") and st.endswith("$$") and len(st) > 4:
                forms["$$...$$ w jednej linii"] += 1
            elif "$$" in line:
                forms["$$ w linii mieszanej"] += 1
    print("formy zapisu:", dict(forms))
    print(f"zamkniecie $$ bezposrednio przed tekstem: {close_before_text}")
    for ex in close_examples[:15]:
        print("   ", ex)
    return 0


if __name__ == "__main__":
    sys.exit(main())
