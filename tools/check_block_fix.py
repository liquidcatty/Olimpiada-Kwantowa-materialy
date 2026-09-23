"""Kontrola bezpieczenstwa naprawy blokow $$: klasyfikuje linie poprzedzajace
wstawiana pusta linie oraz znajduje przypadki $$ w srodku linii z tekstem.

Uruchomienie:
    python tools/check_block_fix.py
"""

from __future__ import annotations

import collections
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fix_block_math import find_blocks, needs_blank_after, needs_blank_before  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"tools", "_tmp", ".git", "node_modules"}
LIST_RE = re.compile(r"^(?:[-*+]|\d+[.)])\s")


def main() -> int:
    kinds: collections.Counter[str] = collections.Counter()
    examples: dict[str, list[str]] = collections.defaultdict(list)
    mid_line: list[str] = []
    for path in sorted(ROOT.rglob("*.md")):
        if any(x in path.parts for x in SKIP):
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        for start, end in find_blocks(lines):
            if needs_blank_before(lines, start):
                prev = lines[start - 1]
                ps = prev.strip()
                if LIST_RE.match(ps):
                    kind = "LISTA"
                elif ps.startswith("|"):
                    kind = "TABELA"
                elif prev.startswith(" "):
                    kind = "WCIETE"
                else:
                    kind = "tekst"
                kinds[kind] += 1
                if kind != "tekst":
                    examples[kind].append(f"{path.relative_to(ROOT)}:{start}")
            if needs_blank_after(lines, end):
                kinds["po bloku: " + ("tekst" if not lines[end].strip().startswith("$$") else "kolejny blok")] += 1
        fence = False
        for i, line in enumerate(lines, 1):
            st = line.strip()
            if st.startswith("```") or st.startswith("~~~"):
                fence = not fence
                continue
            if fence:
                continue
            if "$$" in line and not st.startswith("$$"):
                mid_line.append(f"{path.relative_to(ROOT)}:{i}: {st[:80]}")
    print("klasyfikacja wstawianych pustych linii:")
    for key, value in kinds.most_common():
        print(f"  {value:>4}  {key}")
    for key, items in examples.items():
        print(f"  uwaga {key}: {items[:5]}")
    print(f"\n$$ w srodku linii z tekstem ({len(mid_line)}):")
    for item in mid_line:
        print("   ", item)
    return 0


if __name__ == "__main__":
    sys.exit(main())
