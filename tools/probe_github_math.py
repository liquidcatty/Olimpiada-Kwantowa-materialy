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
    ("inline", "Tekst z wzorem $x^2+1$ w linii.\n"),
    ("block bez pustych linii", "Tekst wprowadzajacy:\n$$\nx = y\n$$\nTekst po.\n"),
    ("block z pustymi liniami", "Tekst wprowadzajacy.\n\n$$\nx = y\n$$\n\nTekst po.\n"),
    ("block na poczatku", "$$\nx = y\n$$\n"),
    ("backslash na koncu linii", "Tekst wprowadzajacy:\\\n$$\nx = y\n$$\nTekst po.\n"),
    ("inline z backtickami", "Tekst $" + "`x^2`" + "$ w linii.\n"),
    ("naglowek", "## Naglowek z $x^2$\n"),
    ("tabela", "| a | b |\n| --- | --- |\n| $x$ | $\\lvert y\\rvert$ |\n"),
    ("tabela z gołym |", "| a | b |\n| --- | --- |\n| $x|y$ | $z$ |\n"),
    ("block po naglowku", "### Naglowek\n$$\nx = y\n$$\n"),
    ("block po naglowku + pusta", "### Naglowek\n\n$$\nx = y\n$$\n"),
    ("block po elemencie listy", "1. Punkt pierwszy:\n$$\nx = y\n$$\n"),
    ("block po elemencie listy + pusta", "1. Punkt pierwszy:\n\n$$\nx = y\n$$\n"),
    ("block wewnatrz listy (wciety)", "1. Punkt pierwszy:\n\n   $$\n   x = y\n   $$\n\n   ciag dalszy punktu\n"),
    ("block w cytacie", "> Uwaga:\n> $$\n> x = y\n> $$\n"),
    ("czysty block bez otoczenia", "$$\nx = y\n$$\n\ntekst po pustej linii\n"),
    ("dwa bloki pod rzad", "$$\na = b\n$$\n$$\nc = d\n$$\n"),
    ("zamkniecie przed tekstem", "$$\nx = y\n$$\nTekst po bez pustej linii.\n"),
    ("tag i boxed", "$$\nx = y \\tag{1}\n$$\n\ntekst\n"),
    ("boxed", "$$\n\\boxed{x = y}\n$$\n\ntekst\n"),
    ("zamkniecie przed naglowkiem", "$$\nx = y\n$$\n## Naglowek\n"),
    ("repo-forma po tekscie", "Tekst wprowadzajacy:\n$$x = y$$\nTekst po.\n"),
    ("repo-forma wielolinijkowa po tekscie", "Tekst wprowadzajacy:\n$$x = y\n+ z$$\nTekst po.\n"),
    ("repo-forma po pustej linii", "Tekst wprowadzajacy.\n\n$$x = y$$\n\nTekst po.\n"),
    ("repo-forma po naglowku", "### Naglowek\n$$x = y$$\n"),
    ("repo-forma na poczatku akapitu", "$$x = y$$\n"),
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
