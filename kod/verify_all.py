"""Uruchamia wszystkie skrypty z katalogu kod/ i zbiera raport OK/FAIL.

Uruchomienie:
    python kod/verify_all.py
"""

from __future__ import annotations

import io
import sys
import traceback
from contextlib import redirect_stdout
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

KATALOG = Path(__file__).resolve().parent

MODULES = [
    "simulator",
    "p1_studnia",
    "p2_polaryzatory",
    "p3_hzh",
    "p4_cnot_ry",
    "grover",
    "chsh",
    "bb84",
    "teleportacja",
    "korekcja_3bit",
    "metrologia_faza",
    "analiza_danych",
]


def main() -> int:
    sys.path.insert(0, str(KATALOG))
    print("=== WERYFIKACJA NUMERYCZNA PRZEWODNIKA ===")
    wyniki = []
    for name in MODULES:
        buf = io.StringIO()
        try:
            module = __import__(name)
            with redirect_stdout(buf):
                module.main()
            wyniki.append((name, True, "OK", buf.getvalue().strip().splitlines()[-1]))
        except Exception:
            tb = traceback.format_exc(limit=3)
            wyniki.append((name, False, "FAIL", tb.strip().splitlines()[-1]))
    print("-" * 78)
    for name, ok, status, info in wyniki:
        print(f"[{status:<4}] {name + '.py':<22} - {info[:45]}")
    print("-" * 78)
    n_ok = sum(1 for _, ok, _, _ in wyniki if ok)
    print(f"WYNIK: {n_ok}/{len(wyniki)} OK")
    if n_ok < len(wyniki):
        print("Niepowodzenia:")
        for name, ok, _, info in wyniki:
            if not ok:
                print(f"  - {name}.py: {info}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
