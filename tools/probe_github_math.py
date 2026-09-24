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
    ("1 inline gwiazdka pojedyncza", "Niech $z^*$ oznacza sprzezenie.\n"),
    ("11 inline dwie gwiazdki zamienione na ast", "Mamy $z^{\\ast}$ oraz $zz^{\\ast}$.\n"),
    ("16 inline x*y jeden span", "Iloczyn $a*b$ i koniec.\n"),
    ("17 inline ast", "Iloczyn $a\\ast b$ i koniec.\n"),
    ("13 inline tylko podwojny backslash", "Wzor $\\begin{cases}1\\\\2\\end{cases}$ w linii.\n"),
    ("14 inline tylko ampersand", "Wzor $a&b$ w linii.\n"),
    ("15 inline cases", "Wzor $\\begin{cases}x&x>0\\\\-x&x\\le0\\end{cases}$ w linii.\n"),
    ("18 tabela z ast", "| Obiekt | Zapis |\n| --- | --- |\n| sprzezenie | $z^{\\ast} = a-bi$ |\n"),
    ("19 blok z cases", "Tekst.\n\n$$\nf(x)=\\begin{cases}x&x>0\\\\-x&x\\le0\\end{cases}\n$$\n\nTekst.\n"),
    ("20 tabela z pmatrix (pelny HTML)", "| Symbol | Macierz |\n| --- | --- |\n| $X$ | $\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}$ |\n"),
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
