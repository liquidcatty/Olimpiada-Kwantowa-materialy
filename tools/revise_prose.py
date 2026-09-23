"""Rewizja prozy: usuwa komentarze motywacyjne/coachingowe z dokumentow.

Zamiany sa doslowne (str.replace), kazda jest weryfikowana - skrypt raportuje
te, ktore nie znalazly dopasowania.

Uzycie:
    python tools/revise_prose.py            # dry-run
    python tools/revise_prose.py --apply
"""

from __future__ import annotations

import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent

FIXES: list[tuple[str, str, str]] = [
    # ---------------- README ----------------
    ("README.md", "Zawsze zacznij od przeczytania:", "Kolejność czytania:"),
    ("README.md",
     "który pozwala sprawdzić rachunek numerycznie.",
     "który pozwala sprawdzić rachunek numerycznie. Przewodnik jest nieoficjalny;\n"
     "prawa do tekstów zadań organizatora należą do Fundacji Quantum AI."),
    # ---------------- docs/00 ----------------
    ("docs/00-jak-korzystac.md",
     "## 1. Pętla nauki (rób to zawsze tak samo)", "## 1. Kolejność pracy z rozdziałem"),
    ("docs/00-jak-korzystac.md",
     "   na kartce**, bez podglądania. To najważniejszy krok.",
     "   na kartce**, bez podglądania."),
    ("docs/00-jak-korzystac.md",
     "   z pamięci. To ujawnia prawdziwe braki.", "   z pamięci."),
    ("docs/00-jak-korzystac.md",
     "## 2. Notatnik wzorów\n\nProwadź własny plik `moja-sciaga.md`. Zasada: **jeden wzór = jedna linia + jedno\n"
     "zdanie, kiedy go użyć**. Po każdym rozdziale dopisz 5–10 pozycji. Ściąga wzorów tego\n"
     "repozytorium (`docs/06-sciaga-wzorow.md`) jest wzorem do naśladowania, nie do\n"
     "wkuwania — wzory trzeba umieć **wyprowadzić**, nie tylko rozpoznać.",
     "## 2. Ściąga wzorów\n\nWszystkie wzory z materiału są zebrane w [`docs/06-sciaga-wzorow.md`](06-sciaga-wzorow.md)."),
    ("docs/00-jak-korzystac.md",
     "wyników. Jeśli wszystko przejdzie, Twoje rachunki z teorii zgadzają się z\nsymulacją. To jest Twoja najszybsza metoda autokorekty.",
     "wyników. Zgodność z symulacją oznacza, że rachunki z teorii są poprawne."),
    ("docs/00-jak-korzystac.md", "## 5. Zasady pracy domowej (PD-N)", "## 5. Praca domowa (PD-N)"),
    ("docs/00-jak-korzystac.md",
     "Rozdział VII). Ten przewodnik ma Cię nauczyć rozumieć, a nie dać gotowca do\n"
     "przepisania — w Etapie II i tak zapytają Cię o każdy krok Twojego rozwiązania.",
     "Rozdział VII)."),
    # ---------------- docs/01 ----------------
    ("docs/01-plan-nauki.md",
     "## 3. Zasady, które robią różnicę\n\n1. **Krótkie sesje codziennie** (45 min) biją jedną długą sesję w weekend.\n"
     "2. **Prawo „kartki i długopisu”**: żadne rozwiązanie nie liczy się, jeśli nie\n"
     "   przepisałeś go bez podglądania.\n3. **Zapisuj błędy.** Prowadź `moje-bledy.md`: zadanie → co poszło nie tak → zasada\n"
     "   na przyszłość. Powtórka z błędów daje więcej niż powtórka z teorii.\n"
     "4. **Sprawdzaj liczby kodem** — to buduje intuicję i uczy interpretacji.\n"
     "5. **Umiej tłumaczyć.** Po każdym rozdziale spróbuj wyjaśnić temat na głos w 3\n"
     "   minuty. To bezpośrednie przygotowanie do rozmowy Etapu II.\n\n## 4. Wariant szybki (4 tygodnie)",
     "## 3. Wariant szybki (4 tygodnie)"),
    ("docs/01-plan-nauki.md",
     "**Uwaga na daty:** Etap I otwiera się 15.11.2026, a zamyka 28.02.2027. Zacznij\nnajpóźniej w połowie października 2026, żeby zdążyć z buforem.",
     "Etap I: 15.11.2026–28.02.2027. Rozpoczęcie nauki w połowie października 2026\n"
     "pozwala ukończyć plan z dwutygodniowym buforem."),
    ("docs/01-plan-nauki.md",
     "Pomiń na pierwszy raz: 14, 15, 18, 19, 20 — ale wróć do nich, jeśli chcesz finału.",
     "W tym wariancie pomija się rozdziały 14, 15, 18, 19, 20."),
    ("docs/01-plan-nauki.md", "## 5. Wariant ratunkowy (3 dni przed deadlinem)", "## 4. Wariant ratunkowy (3 dni)"),
    ("docs/01-plan-nauki.md", "## 6. Plan na Etap II i finał", "## 5. Etap II i finał"),
    # ---------------- docs/04 ----------------
    ("docs/04-strategia-rozwiazywania-zadan.md",
     "1. **Przeczytaj wszystkie zadania** przed startem i zacznij od tego, które umiesz\n   najlepiej (buduje czas i pewność siebie).",
     "1. **Przeczytaj wszystkie zadania** przed startem i zacznij od tego, które umiesz najlepiej."),
    # ---------------- docs/05 ----------------
    ("docs/05-przygotowanie-do-etapu-2.md", "## 1. Co to naprawdę znaczy „zakres = zadania Etapu I”", "## 1. Zakres rozmowy"),
    ("docs/05-przygotowanie-do-etapu-2.md", "4. Przećwicz to na głos z kolegą lub nagrywając się.", "4. Przećwicz odpowiedzi na głos."),
    ("docs/05-przygotowanie-do-etapu-2.md", "## 3. Ćwiczenie „obrona pracy” (rób je na 3 dni przed rozmową)", "## 3. Ćwiczenie „obrona pracy”"),
    ("docs/05-przygotowanie-do-etapu-2.md",
     "- Mów **strukturalnie**: „Najpierw…, potem…, dlatego…”. To buduje ocenę za tok\n  rozumowania nawet przy drobnym błędzie rachunkowym.",
     "- Mów **strukturalnie**: „Najpierw…, potem…, dlatego…”."),
    ("docs/05-przygotowanie-do-etapu-2.md",
     "- Jeśli nie wiesz — powiedz, jak byś to sprawdził. To lepsze niż zgadywanie.",
     "- Jeśli nie wiesz — opisz, jak byś to sprawdził."),
    ("docs/05-przygotowanie-do-etapu-2.md",
     "- Nie przepraszaj nadmiernie, ale przyznaj błąd i popraw się: to się liczy na plus.",
     "- Przyznaj błąd i popraw się."),
    ("docs/05-przygotowanie-do-etapu-2.md",
     "- Miej otwarty notatnik z własnymi notatkami — to Twoje notatki, masz do nich prawo.",
     "- Możesz korzystać z własnych notatek."),
    ("docs/05-przygotowanie-do-etapu-2.md",
     "- Nie oddawaj pracy, której nie rozumiesz — na rozmowie to wyjdzie.",
     "- Nie oddawaj pracy, której nie rozumiesz."),
    # ---------------- szablon ----------------
    ("docs/_szablon-rozdzialu.md",
     "4. Zakres: pokryć temat warsztatu **i lekko wyjść ponad** niego (zaznaczone jako\n   `> **Ponad program:**`), żeby nie było luk na finale.",
     "4. Zakres: pokryć temat warsztatu i wyjść ponad niego tam, gdzie jest to potrzebne\n   do zrozumienia tematu."),
    ("docs/_szablon-rozdzialu.md",
     "6. Długość: 150–350 linii. Nie skracamy kosztem kompletności, ale nie rozwlekamy.",
     "6. Długość: 150–350 linii."),
]


def main() -> int:
    apply = "--apply" in sys.argv
    missing = 0
    for rel, old, new in FIXES:
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        if old not in text:
            print(f"[BRAK DOPASOWANIA] {rel}: {old.splitlines()[0][:70]}")
            missing += 1
            continue
        if apply:
            path.write_text(text.replace(old, new, 1), encoding="utf-8")
        print(f"[OK] {rel}: {old.splitlines()[0][:60]}")
    print(f"\n{'ZAPISANO' if apply else 'DRY-RUN'}: zamian {len(FIXES) - missing}, brakujacych {missing}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())

