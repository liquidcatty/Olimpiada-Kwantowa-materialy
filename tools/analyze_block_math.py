"""Analiza blokow wyswietlania ($$) stojacych bezposrednio po linii tekstu.

Dla kazdego takiego przypadku klasyfikuje kontekst, zeby ocenic, czy bezpiecznie
mozna wstawic pusta linie przed $$ (poprawny blok na GitHubie) bez psucia list
i tabel.

Uruchomienie:
    python tools/analyze_block_math.py
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
LIST_RE = re.compile(r"^(?:[-*+]|\d+[.)])\s")


def main() -> int:
    counts: collections.Counter[str] = collections.Counter()
    examples: dict[str, list[str]] = collections.defaultdict(list)
    for path in sorted(ROOT.rglob("*.md")):
        if any(x in path.parts for x in SKIP):
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        fence = False
        for i, line in enumerate(lines):
            st = line.strip()
            if st.startswith("```") or st.startswith("~~~"):
                fence = not fence
                continue
            if fence or not st.startswith("$$") or i == 0:
                continue
            prev = lines[i - 1]
            if not prev.strip() or prev.rstrip().endswith("\\"):
                continue
            ps = prev.strip()
            if LIST_RE.match(ps):
                key = "lista"
            elif ps.startswith("|"):
                key = "tabela"
            elif ps.endswith(":"):
                key = "tekst z dwukropkiem"
            elif line.startswith(" "):
                key = "wciete"
            else:
                key = "zwykly tekst"
            counts[key] += 1
            examples[key].append(f"{path.relative_to(ROOT)}:{i + 1}")
    print("bloki $$ bezposrednio po linii tekstu (bez pustej linii):")
    for key, value in counts.most_common():
        print(f"  {value:>4}  {key:22} np. {examples[key][:3]}")
    print(f"\nrazem: {sum(counts.values())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
