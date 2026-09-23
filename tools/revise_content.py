"""Rewizja materialu: usuwa meta-infokramki i komentarze motywacyjne.

Co robi:
  1. USUWA bloki cytatow bedace czysta metainformacja (warsztat zrodlowy, czas nauki,
     weryfikacja numeryczna, status materialu, naglowki rozdzialow 17-20).
  2. ODRAMKOWUJE (usuwa "> " i etykiete "Ponad program:") bloki z trescia merytoryczna.
  3. ZASTEPUJE zdania motywacyjne/coachingowe wersjami neutralnymi.

Uzycie:
    python tools/revise_content.py           # dry-run + raport
    python tools/revise_content.py --apply
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"tools", "_tmp", ".git", "node_modules"}

# 1. bloki do usuniecia (dopasowanie po poczatku pierwszej linii bez "> ")
DELETE_STARTS = (
    "**Warsztat źródłowy:**",
    "**Weryfikacja numeryczna.**",
    "**Status materiału.**",
    "Ten dokument jest **obowiązujący",
    "**Ponad program:** rozdział wykracza",
)

# 2. bloki do odramkowania (usuniecie "> " oraz ewentualnej etykiety)
UNBOX_STARTS = (
    "**Ponad program:**",
    "**Uwaga:**",
    "**Wniosek:**",
    "Wartość jest w tym",
    "Materiał wykorzystany wyłącznie",
    "**Zakres:**",
    "Rozwiązania przygotowane",
)

# 3. drobne zamiany tekstu: (plik, wzorzec regex, zamiana)
SMALL_FIXES: list[tuple[str, str, str]] = [
    ("README.md",
     r"Wychodzi\n\*\*lekko poza\*\* zakres olimpiady, żeby na finale nie zaskoczyła Cię żadna luka\.",
     "Zakres jest nieco szerszy niż program olimpiady."),
    ("README.md",
     r"\n\*\*Powodzenia!\*\* Pamiętaj: na Olimpiadzie nie liczy się to, ile wzorów znasz, tylko\nto, czy umiesz ich użyć w nowej sytuacji\.\n",
     ""),
    ("docs/05-przygotowanie-do-etapu-2.md",
     r"## 6\. Mini-ściąga: 12 pytań, które warto umieć odpowiedzieć w 60 sekund",
     "## 6. Dwanaście pytań kontrolnych"),
    ("teoria/14-narzedzia-informatyczne.md",
     r"Warto znać `conda`",
     "Przydatne narzędzia: `conda`"),
    ("teoria/06-kubity-bramki-obwody-pomiary.md", r"\*\*Zapamiętaj dwie tożsamości\*\*", "**Dwie tożsamości**"),
    ("teoria/02-algebra-liniowa.md", r"pamiętaj o fazie", "uwzględnij fazę"),
    ("teoria/02-algebra-liniowa.md", r"pamiętaj o małoendianowej", "zachowaj małoendianową"),
    ("teoria/04-elementy-analizy-matematycznej.md", r"pamiętaj o regule iloczynu", "zastosuj regułę iloczynu"),
    ("teoria/06-kubity-bramki-obwody-pomiary.md", r"W \(b\) pamiętaj, że", "W (b) uwzględnij, że"),
    ("teoria/13-korekcja-i-mitygacja-bledow.md", r"pamiętaj \$\\sigma_z=+1\$", r"uwzględnij $\sigma_z=+1$"),
    ("zadania/treningowe/P3.md", r"pamiętaj, że bramka wykonana jako pierwsza stoi", "bramka wykonana jako pierwsza stoi"),
    ("praca-domowa/praca-domowa-04.md",
     r"Dopuszczalne \(i zalecane\) sprawdzenie rachunków w NumPy\.",
     "Dopuszczalne jest sprawdzenie rachunków w NumPy."),
]

# naglowek arkusza P1-P4 -> zwykla linia ze zrodlem i linkiem do teorii
P_HEADER_RE = re.compile(
    r"> Zadanie z oficjalnego arkusza \*\*„Zadania przykładowe”\*\* Olimpiady Kwantowej\n"
    r"> \(<https://olimpiadakwantowa\.pl/zadania/>\)\. Materiał edukacyjny\.\n"
    r"> \*\*Działka teorii:\*\* (.+?)\n"
)


def unbox(block: list[str]) -> list[str]:
    out = []
    for line in block:
        text = re.sub(r"^>\s?", "", line)
        out.append(text.rstrip())
    text = "\n".join(out)
    text = text.replace("**Ponad program:** ", "")
    return text.splitlines()


def iter_md() -> list[Path]:
    return [p for p in sorted(ROOT.rglob("*.md")) if not any(x in SKIP for x in p.relative_to(ROOT).parts)]


def blocks(lines: list[str]):
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith(">"):
            s = i
            while i < len(lines):
                if lines[i].lstrip().startswith(">"):
                    i += 1
                elif lines[i].strip() == "" and i + 1 < len(lines) and lines[i + 1].lstrip().startswith(">"):
                    i += 1
                else:
                    break
            yield s, i, lines[s:i]
        else:
            i += 1


def revise_file(path: Path, apply: bool) -> list[str]:
    original = path.read_text(encoding="utf-8")
    text = original
    log: list[str] = []

    # 3a. naglowki zadan P1-P4
    def p_repl(m: re.Match) -> str:
        return ("Źródło: arkusz „Zadania przykładowe” Olimpiady Kwantowej\n"
                "(<https://olimpiadakwantowa.pl/zadania/>).\n"
                f"Teoria: {m.group(1)}\n")

    text, n = P_HEADER_RE.subn(p_repl, text)
    if n:
        log.append(f"odramkowano naglowek zadania P ({n}x)")

    # 3b. bloki cytatow
    lines = text.splitlines()
    out: list[str] = []
    idx = 0
    removed = unboxed = 0
    for s, e, block in blocks(lines):
        out.extend(lines[idx:s])
        first = block[0].lstrip("> ").strip()
        if first.startswith(DELETE_STARTS):
            removed += 1
            log.append(f"usunieto blok metainfo w linii {s + 1}: {first[:60]}")
        elif first.startswith(UNBOX_STARTS):
            new = unbox(block)
            # naglowek pracy domowej: neutralne sformulowanie zdania o NumPy
            new = [re.sub(
                r"Można \(i warto\) wspomagać się numpy — ale rachunek musi być widoczny\.",
                "Rachunek musi być widoczny (można wspomagać się NumPy).",
                line) for line in new]
            if first.startswith("Rozwiązania przygotowane"):
                new = ["Treść zadań pochodzi z oficjalnego arkusza „Zadania przykładowe”",
                       "Olimpiady Kwantowej (<https://olimpiadakwantowa.pl/zadania/>)."]
            out.extend(new)
            unboxed += 1
            log.append(f"odramkowano blok w linii {s + 1}: {first[:55]}")
        else:
            out.extend(block)
        idx = e
    out.extend(lines[idx:])
    text = "\n".join(out) + ("\n" if original.endswith("\n") else "")

    # 3c. drobne zamiany
    for file_name, pattern, repl in SMALL_FIXES:
        if file_name != path.relative_to(ROOT).as_posix():
            continue
        text, n = re.subn(pattern, lambda _m, r=repl: r, text)
        if n:
            log.append(f"zamiana tekstu ({n}x): {pattern[:45]}")

    if apply and text != original:
        path.write_text(text, encoding="utf-8")
    return log


def main() -> int:
    apply = "--apply" in sys.argv
    changed = 0
    for path in iter_md():
        log = revise_file(path, apply)
        if log:
            changed += 1
            print(f"--- {path.relative_to(ROOT)}")
            for entry in log:
                print("   ", entry)
    print(f"\n{'ZAPISANO' if apply else 'DRY-RUN'}: plikow zmienionych {changed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

