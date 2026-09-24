"""Zamienia znak * wewnatrz matematyki na \\ast.

Powod (dowod empiryczny, tools/probe_report.py): GitHub przetwarza * wewnatrz
wzorow jako kursywe Markdowna. Gdy w akapicie sa co najmniej dwa takie znaki
(nawet w roznych wzorach), matematyka przestaje dzialac, a w bloku $$ znak *
zamienia sie na _, co daje blad "Missing open brace for superscript".

Uzycie:
    python tools/fix_star_in_math.py            # dry-run
    python tools/fix_star_in_math.py --apply
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"tools", "_tmp", ".git", "node_modules"}
FENCE_RE = re.compile(r"^\s*(```|~~~)")
# code-span | $$...$$ w jednej linii | $...$ inline
TOKEN_RE = re.compile(r"(`[^`\n]*`)|\$\$([^$\n]*)\$\$|\$([^$\n]+)\$")


def fix_text(text: str) -> tuple[str, int]:
    lines = text.splitlines()
    out: list[str] = []
    fence = False
    in_block = False
    replaced = 0
    for raw in lines:
        if FENCE_RE.match(raw):
            fence = not fence
            out.append(raw)
            continue
        if fence:
            out.append(raw)
            continue
        line = raw
        # bloki wyswietlania: same delimitery w linii
        if line.strip() == "$$":
            in_block = not in_block
            out.append(line)
            continue
        if in_block:
            if "*" in line:
                replaced += line.count("*")
                line = line.replace("*", r"\ast")
            out.append(line)
            continue

        def repl(match: re.Match) -> str:
            nonlocal replaced
            if match.group(1):            # code span - zostaw
                return match.group(1)
            expr = match.group(2) if match.group(2) is not None else match.group(3)
            if expr is None or "*" not in expr:
                return match.group(0)
            replaced += expr.count("*")
            fixed = expr.replace("*", r"\ast")
            return match.group(0).replace(expr, fixed, 1)

        out.append(TOKEN_RE.sub(repl, line))
    return "\n".join(out) + ("\n" if text.endswith("\n") else ""), replaced


def main() -> int:
    apply = "--apply" in sys.argv
    files = 0
    total = 0
    for path in sorted(ROOT.rglob("*.md")):
        if any(x in path.parts for x in SKIP):
            continue
        text = path.read_text(encoding="utf-8")
        new, count = fix_text(text)
        if count and new != text:
            files += 1
            total += count
            print(f"{path.relative_to(ROOT)}: gwiazdek {count}")
            if apply:
                path.write_text(new, encoding="utf-8")
    print(f"\n{'ZAPISANO' if apply else 'DRY-RUN'}: plikow {files}, gwiazdek {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
