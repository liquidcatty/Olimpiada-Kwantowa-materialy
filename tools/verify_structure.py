"""Kontrola struktury materialow: sekcje rozdzialow, zadania Z-NN i ich rozwiazania.

Uruchomienie:
    python tools/verify_structure.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ["## 1.", "## 2.", "## 3.", "## 4.", "## 5.", "## 6.", "## 7.", "## 8."]
CHAPTER_RE = re.compile(r"^(\d{2})-", re.M)


def main() -> int:
    problems = 0
    print("--- rozdzialy teorii ---")
    for path in sorted((ROOT / "teoria").glob("[0-9][0-9]-*.md")):
        text = path.read_text(encoding="utf-8")
        missing = [s for s in SECTIONS if s not in text]
        tasks = sorted({int(m.group(1)) for m in re.finditer(r"\*\*Z-(\d{2})\.\d+", text)})
        first = "Zakres rozdziału" if "## 1. Zakres rozdziału" in text else "!! " + (
            "Po co to jest" if "## 1. Po co to jest" in text else "brak sekcji 1")
        number = int(path.name[:2])
        flag = ""
        if missing:
            flag += f" BRAKI_SERII={missing}"
        if not tasks or tasks != [number]:
            flag += f" ZLE_ZADANIA={tasks}"
        if first.startswith("!!"):
            flag += f" SEKCJA1={first}"
        if flag:
            problems += 1
        count_z = len(re.findall(r"\*\*Z-", text))
        print(f"  {path.name:56} Z={count_z:2}  sekcja1={first}{flag}")

    print("--- pliki z rozwiązaniami ---")
    for path in sorted((ROOT / "zadania" / "rozwiazania").glob("rozwiazania-*.md")):
        text = path.read_text(encoding="utf-8")
        number = path.name[len("rozwiazania-"):-3]
        chapter = ROOT / "teoria"
        chap = list(chapter.glob(f"{number}-*.md"))
        if not chap:
            print(f"  {path.name}: BRAK ROZDZIAŁU")
            problems += 1
            continue
        chapter_text = chap[0].read_text(encoding="utf-8")
        prefix = f"Z-{number}."
        chapter_tasks = sorted({m.group(0) for m in re.finditer(r"Z-\d{2}\.\d+", chapter_text)
                                if m.group(0).startswith(prefix)})
        solved = sorted({m.group(0) for m in re.finditer(r"Z-\d{2}\.\d+", text)
                         if m.group(0).startswith(prefix)})
        missing = [t for t in chapter_tasks if t not in solved]
        if missing:
            problems += 1
        print(f"  {path.name:22} zadan w rozdziale={len(chapter_tasks):2} "
              f"rozwiazanych={len(solved):2} braki={missing if missing else '-'}")

    print("--- prace domowe ---")
    for path in sorted((ROOT / "praca-domowa").glob("praca-domowa-*.md")):
        text = path.read_text(encoding="utf-8")
        tasks = len({m.group(1) for m in re.finditer(r"\*\*PD-\d+\.(\d+)", text)})
        checks = {"Zadania": "## Zadania" in text,
                  "Kryteria oceny": "## Kryteria oceny" in text,
                  "Wskazówki i odpowiedzi": "## Wskazówki i odpowiedzi" in text}
        bad = [k for k, ok in checks.items() if not ok]
        if bad or tasks != 10:
            problems += 1
        print(f"  {path.name:26} zadan={tasks:2} braki={bad if bad else '-'}")

    print(f"\nproblemow strukturalnych: {problems}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
