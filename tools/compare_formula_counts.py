"""Porownuje LICZBE formul w plikach z wersja bazowa z gita.

Wypisuje pliki, w ktorych liczba blokow $$ lub formul inline sie zmienila,
zeby recznie potwierdzic, ze ubytki pochodza wylacznie z usunietych
meta-komentarzy (blokow cytatow), a nie z tresci merytorycznej.

Uruchomienie:
    python tools/compare_formula_counts.py --base 148b833
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "_tmp", "tools", "node_modules"}


def counts(text: str) -> tuple[int, int]:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", " ", text)
    blocks = len(re.findall(r"\$\$.+?\$\$", text, flags=re.S))
    stripped = re.sub(r"\$\$.+?\$\$", "", text, flags=re.S)
    inline = len(re.findall(r"\$[^$\n]+\$", stripped))
    return blocks, inline


def main() -> int:
    base = sys.argv[sys.argv.index("--base") + 1] if "--base" in sys.argv else "HEAD"
    changed = []
    for path in sorted(ROOT.rglob("*.md")):
        if any(x in path.parts for x in SKIP_DIRS):
            continue
        rel = path.relative_to(ROOT).as_posix()
        try:
            old = subprocess.run(["git", "show", f"{base}:{rel}"], cwd=ROOT,
                                 capture_output=True, check=True).stdout.decode("utf-8")
        except subprocess.CalledProcessError:
            continue
        ob, oi = counts(old)
        nb, ni = counts(path.read_text(encoding="utf-8"))
        if (ob, oi) != (nb, ni):
            changed.append((rel, ob, nb, oi, ni))
    print(f"{'plik':58} {'$$ przed':>9} {'$$ po':>7} {'inline przed':>13} {'inline po':>10}")
    for rel, ob, nb, oi, ni in changed:
        print(f"{rel:58} {ob:>9} {nb:>7} {oi:>13} {ni:>10}")
    print(f"\nplikow ze zmiana liczby formul: {len(changed)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
