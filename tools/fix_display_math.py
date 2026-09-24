"""Sprowadza bloki wyswietlania do formy, ktora GitHub faktycznie renderuje.

Dowod empiryczny (POST api.github.com/markdown, mode=gfm):
  * `$$tresc` ... `tresc$$` (oba delimitery doklejone do tresci) -> BRAK renderowania,
  * `$$` w osobnej linii  -> RENDERUJE,
  * `$$tresc` na poczatku + `$$` w osobnej linii -> RENDERUJE,
  * caly wzor w jednej linii `$$tresc$$` -> RENDERUJE (ale tylko w osobnym akapicie).

Forma kanoniczna stosowana przez ten skrypt:

    $$
    tresc
    $$

z pusta linia przed i po (z zachowaniem wciecia, jesli blok jest w elemencie listy).

Uzycie:
    python tools/fix_display_math.py            # dry-run
    python tools/fix_display_math.py --apply
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


def iter_md() -> list[Path]:
    return [p for p in sorted(ROOT.rglob("*.md"))
            if not any(x in SKIP for x in p.relative_to(ROOT).parts)]


def fix_text(text: str) -> tuple[str, int]:
    lines = text.splitlines()
    out: list[str] = []
    fence = False
    i = 0
    fixed = 0
    while i < len(lines):
        raw = lines[i]
        if FENCE_RE.match(raw):
            fence = not fence
            out.append(raw)
            i += 1
            continue
        stripped = raw.strip()
        if fence or not stripped.startswith("$$"):
            out.append(raw)
            i += 1
            continue

        # zbierz caly blok: do linii wyrownujacej liczbe $$
        block = [raw]
        total = raw.count("$$")
        j = i
        while total % 2 == 1 and j + 1 < len(lines):
            j += 1
            block.append(lines[j])
            total += lines[j].count("$$")
        joined = "\n".join(block)
        first = joined.find("$$")
        last = joined.rfind("$$")
        inner = joined[first + 2:last] if last > first else joined[first + 2:]
        inner_lines = [line.rstrip() for line in inner.splitlines()]
        while inner_lines and not inner_lines[0].strip():
            inner_lines.pop(0)
        while inner_lines and not inner_lines[-1].strip():
            inner_lines.pop()
        indent = raw[: len(raw) - len(raw.lstrip())]

        need_before = bool(out) and out[-1].strip() and not out[-1].lstrip().startswith("#")
        if need_before:
            out.append("")
        out.append(f"{indent}$$")
        out.extend(f"{indent}{line}" if line else "" for line in inner_lines)
        out.append(f"{indent}$$")
        next_line = lines[j + 1] if j + 1 < len(lines) else ""
        if next_line.strip() and not next_line.lstrip().startswith("#"):
            out.append("")
        fixed += 1
        i = j + 1
    return "\n".join(out) + ("\n" if text.endswith("\n") else ""), fixed


def main() -> int:
    apply = "--apply" in sys.argv
    files = 0
    total = 0
    for path in iter_md():
        text = path.read_text(encoding="utf-8")
        new, fixed = fix_text(text)
        if fixed and new != text:
            files += 1
            total += fixed
            if apply:
                path.write_text(new, encoding="utf-8")
            print(f"{path.relative_to(ROOT)}: blokow {fixed}")
    print(f"\n{'ZAPISANO' if apply else 'DRY-RUN'}: plikow {files}, blokow $$ {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
