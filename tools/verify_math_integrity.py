"""Kontrola integralnosci matematyki: porownuje wszystkie wzory w plikach roboczych
z wersja z ostatniego commita (git).

Cel: redakcja tresci nie moze zmienic ani usunac zadnego wzoru. Skrypt wyciaga
segmenty matematyczne (inline $...$ i bloki $$...$$), normalizuje biale znaki
i porownuje multizbiory.

Uruchomienie:
    python tools/verify_math_integrity.py
"""

from __future__ import annotations

import collections
import re
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "_tmp", "tools", "node_modules"}
# ten plik dokumentuje skladnie $$ poslugujac sie literalnymi przykladami
IGNORE_FILES = {"docs/03-konwencje-i-notacja.md"}


def git_show(rel: str, base: str) -> str | None:
    try:
        out = subprocess.run(
            ["git", "show", f"{base}:{rel}"],
            cwd=ROOT, capture_output=True, check=True,
        )
        return out.stdout.decode("utf-8")
    except subprocess.CalledProcessError:
        return None


def segments(text: str) -> collections.Counter[str]:
    """Multizbior tresci wzorow (bez rozrozniania inline/blok i bez \\ast).

    Normalizacje:
      * biale znaki -> pojedyncza spacja,
      * \\ast -> * (zamiana wykonana przez tools/fix_star_in_math.py jest kosmetyczna),
      * inline i blok traktowane tak samo (przenoszenie macierzy z inline do bloku
        nie zmienia tresci wzoru).
    """
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", " ", text)
    counter: collections.Counter[str] = collections.Counter()

    def norm(expr: str) -> list[str]:
        """Normalizuje wzor do porownania: \\ast->*, bez interpunkcji koncowej,
        wieloczesciowe wzory rozbite na czesci (\\qquad / \\quad)."""
        expr = expr.replace(r"\ast", "*")
        expr = re.sub(r"\s+", " ", expr).strip()
        parts = re.split(r"\\qquad|\\quad", expr)
        out = []
        for part in parts:
            part = part.strip().rstrip(".,;:")
            part = part.strip()
            if part:
                out.append(part)
        return out

    for block in re.finditer(r"\$\$(.+?)\$\$", text, flags=re.S):
        for part in norm(block.group(1)):
            counter["M:" + part] += 1
    stripped = re.sub(r"\$\$.+?\$\$", "", text, flags=re.S)
    for inline in re.finditer(r"\$([^$\n]+)\$", stripped):
        for part in norm(inline.group(1)):
            counter["M:" + part] += 1
    return counter


def main() -> int:
    base = "HEAD"
    if "--base" in sys.argv:
        base = sys.argv[sys.argv.index("--base") + 1]
    print(f"porownanie z wersja: {base}")
    problems = 0
    checked = 0
    for path in sorted(ROOT.rglob("*.md")):
        if any(x in path.parts for x in SKIP_DIRS):
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel in IGNORE_FILES:
            continue
        old = git_show(rel, base)
        if old is None:
            continue
        checked += 1
        before = segments(old)
        after = segments(path.read_text(encoding="utf-8"))
        if before == after:
            continue
        lost = before - after
        added = after - before
        problems += 1
        print(f"--- {rel}")
        for key, count in list(lost.items())[:5]:
            print(f"    UTRACONE ({count}x): {key[:110]}")
        for key, count in list(added.items())[:5]:
            print(f"    NOWE     ({count}x): {key[:110]}")
    print(f"\nsprawdzono plikow: {checked}; plikow z roznica we wzorach: {problems}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
