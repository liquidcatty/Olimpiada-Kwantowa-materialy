"""Raport z sondy GitHub: co renderer faktycznie dostaje w matematyce.

Uruchomienie:
    python tools/probe_report.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from probe_github_math import CASES, post  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

MATH_RE = re.compile(r"<math-renderer[^>]*>(.*?)</math-renderer>", re.S)


def main() -> int:
    for name, text in CASES:
        try:
            html = post(text)
        except Exception as exc:                      # pragma: no cover
            print(f"== {name}\n   BLAD API: {exc}")
            continue
        found = MATH_RE.findall(html)
        print(f"== {name}")
        if not found:
            flat = re.sub(r"\s+", " ", html).strip()
            print(f"   BRAK math-renderer; HTML: {flat[:190]}")
            continue
        for expr in found[:3]:
            flat = re.sub(r"\s+", " ", expr).strip()
            flags = []
            if "*" in flat:
                flags.append("gwiazdka OK")
            if "&" in flat:
                flags.append("ampersand OK")
            if "\\\\" in flat:
                flags.append("podwojny backslash OK")
            if re.search(r"\^=|\^\{?\s*$|\^_", flat):
                flags.append("PODEJRZANY wykładnik")
            print(f"   MATH: {flat[:120]}   [{' , '.join(flags) if flags else '-'}]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
