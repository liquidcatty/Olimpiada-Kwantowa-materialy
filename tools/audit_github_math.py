"""Audyt renderowania matematyki na GitHubie.

Sprawdza reguly z dokumentacji GitHub (MathJax):
  * inline: $...$ lub $`...`$ (musza byc w jednej linii),
  * blok: $$...$$ musi zaczynac sie w nowej linii; jezeli poprzedza go tekst bez
    pustej linii, GitHub zaleca zakonczenie poprzedniej linii backslashem,
  * $$ nie dziala w wierszach tabeli,
  * znak | wewnatrz math w tabeli rozbija tabele,
  * naglowki z matematyka (ryzykowne - renderowanie w naglowkach bywa nieobecne).

Uzycie:
    python tools/audit_github_math.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"tools", "_tmp", ".git", "node_modules"}


def strip_code_spans(line: str) -> str:
    """Usuwa code-spany, zeby $ wewnatrz kodu nie bylo liczone jako matematyka."""
    return re.sub(r"`[^`\n]*`", "", line)


def iter_md() -> list[Path]:
    return [p for p in sorted(ROOT.rglob("*.md")) if not any(x in SKIP for x in p.relative_to(ROOT).parts)]


def main() -> int:
    issues = 0
    counts = {"inline_multi": 0, "block_after_text": 0, "block_and_text": 0, "heading_math_info": 0,
              "table_math_pipe": 0, "dollar_in_heading": 0}
    for path in iter_md():
        lines = path.read_text(encoding="utf-8").splitlines()
        rel = path.relative_to(ROOT)
        fence = False
        for i, line in enumerate(lines, 1):
            if line.lstrip().startswith("```") or line.lstrip().startswith("~~~"):
                fence = not fence
                continue
            if fence:
                continue
            line = strip_code_spans(line)
            if not line.strip():
                continue
            stripped = line.strip()
            if "$$" in line:
                if stripped.startswith("|"):
                    print(f"  {rel}:{i} [tabela] $$ w wierszu tabeli")
                    counts["table_math_pipe"] += 1
                    issues += 1
                elif not stripped.startswith("$$"):
                    # $$ w srodku lub na koncu linii z tekstem
                    if len(re.findall(r"\$\$", line)) == 2 and not re.match(r"^\s*\$\$.+\$\$\s*$", line):
                        print(f"  {rel}:{i} [blok] $$ w linii z tekstem (GitHub wymaga nowej linii)")
                        counts["block_and_text"] += 1
                        issues += 1
                else:
                    prev = lines[i - 2].rstrip() if i >= 2 else ""
                    if prev and not prev.endswith("\\"):
                        print(f"  {rel}:{i} [blok] $$ bez pustej linii ani '\\' po tekscie: ...{prev[-40:]}")
                        counts["block_after_text"] += 1
                        issues += 1
            if stripped.startswith("#") and len(re.findall(r"(?<!\$)\$(?!\$)", line)) >= 2:
                # sonda GitHub API potwierdzila, ze matematyka w naglowkach RENDERUJE sie
                counts["heading_math_info"] += 1
            if stripped.startswith("|"):
                for seg in re.findall(r"\$([^$\n]+)\$", line):
                    if re.search(r"(?<!\\)\|", seg):
                        print(f"  {rel}:{i} [tabela] | wewnatrz math -> ${seg[:50]}$")
                        counts["table_math_pipe"] += 1
                        issues += 1
    print("\nPodsumowanie:", counts)
    print(f"problemow: {issues}")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
