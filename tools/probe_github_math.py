"""Sonda: jak GitHub (API /markdown) przetwarza matematyke w roznych kontekstach.

Wysyla kilka probek do https://api.github.com/markdown i wypisuje otrzymany HTML.
Dzieki temu wiadomo, czy $$ i $ sa zachowywane dla MathJax i jak dzielone sa akapity.

Uruchomienie:
    python tools/probe_github_math.py
"""

from __future__ import annotations

import json
import sys
import urllib.request

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CASES: list[tuple[str, str]] = [
    ("K: $$ osobno, zamkniecie na koncu tresci", "Tekst.\n\n$$\nx = y$$\n\nTekst.\n"),
    ("L: $$tresc, zamkniecie osobno", "Tekst.\n\n$$x = y\n$$\n\nTekst.\n"),
    ("M: $$ osobno, bez pustych linii po naglowku", "## Naglowek\n$$\nx = y\n$$\n\ntekst\n"),
    ("N: $$tresc$$ jedna linia bez pustych linii", "## Naglowek\n$$x = y$$\ntekst\n"),
    ("O: operatorname z podkresleniem", "$\\operatorname{rank}A + \\operatorname{Tr}\\rho$\n"),
    ("P: mathrm z podkresleniem", "$\\mathrm{rank}\\,A + \\mathrm{Tr}\\,\\rho$\n"),
]



def post(text: str) -> str:
    body = json.dumps({"text": text, "mode": "gfm"}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.github.com/markdown",
        data=body,
        headers={"Content-Type": "application/json", "User-Agent": "olimpiada-kwantowa-audit"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def main() -> int:
    for name, text in CASES:
        print("=" * 70)
        print(f"CASE: {name}")
        print("--- wejscie ---")
        print(text)
        try:
            html = post(text)
        except Exception as exc:                        # pragma: no cover
            print(f"BLAD: {exc}")
            continue
        print("--- HTML z GitHub ---")
        print(html)
        verdict = "RENDERUJE" if "math-renderer" in html else "BRAK RENDEROWANIA"
        print(f"--- WERDYKT: {verdict}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
