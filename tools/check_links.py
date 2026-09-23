"""Sprawdza, czy wszystkie linki relatywne w plikach Markdown istnieja.

Uruchomienie:
    python tools/check_links.py

Kod wyjscia 0 = wszystkie linki OK, 1 = znaleziono brakujace pliki.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")
# Znaki typowe dla matematyki: pozwalaja odsiac falszywe trafienia typu "[x](\omega)"
SKIP_CHARS = ("\\", "{", "}", "|", "&")


def main() -> int:
    problems: list[str] = []
    checked = 0
    for md in sorted(ROOT.rglob("*.md")):
        if any(part in {".git", "_tmp", "node_modules"} for part in md.parts):
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.split("#", 1)[0].strip()
            if not target or target.startswith(SKIP_PREFIXES):
                continue
            if any(ch in target for ch in SKIP_CHARS):
                continue                      # falszywe trafienie w formule matematycznej
            checked += 1
            resolved = (md.parent / target).resolve()
            if not resolved.exists():
                rel = md.relative_to(ROOT)
                problems.append(f"{rel}: brakuje -> {raw_target}")
    print(f"sprawdzono {checked} linkow relatywnych w repo")
    if problems:
        print(f"ZNALEZIONO {len(problems)} problemow:")
        for p in problems:
            print("  -", p)
        return 1
    print("wszystkie linki relatywne sa poprawne")
    return 0


if __name__ == "__main__":
    sys.exit(main())
