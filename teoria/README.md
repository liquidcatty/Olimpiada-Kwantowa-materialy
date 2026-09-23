# Teoria — 20 rozdziałów

Każdy rozdział ma tę samą strukturę: **po co to jest → definicje → teoria krok po
kroku → przykłady rozwiązane → typowe pułapki → zadania (Z-NN) → wskazówki → co dalej**.
Pełne rozwiązania zadań są w [`../zadania/rozwiazania/`](../zadania/rozwiazania/).

Szablon rozdziału (dla autorów): [`../docs/_szablon-rozdzialu.md`](../docs/_szablon-rozdzialu.md).
Konwencje i notacja: [`../docs/03-konwencje-i-notacja.md`](../docs/03-konwencje-i-notacja.md).

## Moduł 1 — matematyka, na której stoi cała mechanika kwantowa

| # | Rozdział | Zawartość |
| --- | --- | --- |
| 01 | [Liczby zespolone](01-liczby-zespolone.md) | algebra, postać biegunowa, Eulera, de Moivre'a, faza amplitudy |
| 02 | [Algebra liniowa](02-algebra-liniowa.md) | przestrzenie, operatory, hermitowskość, unitarność, spektralne, kron |
| 03 | [Prawdopodobieństwo i statystyka](03-rachunek-prawdopodobienstwa-i-statystyka.md) | rozkłady, Bayes, CTG, estymacja, χ² |
| 04 | [Elementy analizy](04-elementy-analizy-matematycznej.md) | pochodne, całki, RRC, Fouriera, delta, Gauss |
| 05 | [Podstawy mechaniki kwantowej](05-podstawy-mechaniki-kwantowej.md) | postulaty, studnia, tunelowanie, spin, polaryzacja |

## Moduł 2 — informatyka kwantowa

| # | Rozdział | Zawartość |
| --- | --- | --- |
| 06 | [Kubity, bramki, obwody, pomiary](06-kubity-bramki-obwody-pomiary.md) | sfera Blocha, bramki, CNOT, obwody, pomiar |
| 07 | [Kwantowa teoria informacji](07-kwantowa-teoria-informacji.md) | no-cloning, entropia, Holevo, wierność |
| 08 | [Podstawowe algorytmy kwantowe](08-algorytmy-kwantowe.md) | Deutscha–Jozsy, Simona, QFT, Grover, Shor |
| 09 | [Splątanie i twierdzenie Bella](09-splatanie-i-twierdzenie-bella.md) | Bella, PPT, CHSH, monogamia |
| 10 | [Kryptografia kwantowa](10-kryptografia-kwantowa.md) | Vernam, BB84, B92, E91, QBER |

## Moduł 3 — sprzęt i inżynieria

| # | Rozdział | Zawartość |
| --- | --- | --- |
| 11 | [Metrologia kwantowa](11-metrologia-kwantowa.md) | Cramér–Rao, 1/√N vs 1/N, GHZ, N00N |
| 12 | [Realizacje komputerów kwantowych](12-realizacje-komputerow-kwantowych.md) | DiVincenzo, technologie, T1/T2, benchmarki |
| 13 | [Korekcja i mitygacja błędów](13-korekcja-i-mitygacja-bledow.md) | kody, syndromy, kod powierzchniowy, ZNE |
| 14 | [Narzędzia informatyczne](14-narzedzia-informatyczne.md) | terminal, git, LaTeX, HPC, wysyłka pracy |
| 15 | [Oprogramowanie kwantowe](15-oprogramowanie-kwantowe.md) | Qiskit, Cirq, PennyLane, QASM, symulatory |

## Moduł 4 — dane i tematy rozszerzające

| # | Rozdział | Zawartość |
| --- | --- | --- |
| 16 | [Analiza danych i obliczenia naukowe](16-analiza-danych-i-obliczenia-naukowe.md) | NumPy, dopasowanie, χ², bootstrap, FFT |
| 17 | [Macierze gęstości i kanały kwantowe](17-ponad-program-macierze-gestosci-i-kanaly.md) | stany mieszane, ślad częściowy, Kraus |
| 18 | [Splątanie, dekoherencja, termodynamika](18-ponad-program-splatanie-dekoherencja-termodynamika.md) | miary splątania, T1/T2, Landauer |
| 19 | [Algorytmy zaawansowane i granice](19-ponad-program-algorytmy-zaawansowane-i-granice.md) | teleportacja, Shor, Holevo, Solovay–Kitaev |
| 20 | [Mini-projekty zaliczeniowe](20-ponad-program-mini-projekty.md) | 6 projektów + szablon raportu |

## Jak czytać te rozdziały

1. Rozdziały **01–05 są warunkiem** wszystkiego dalej — nie pomijaj ich, nawet jeśli
   „znasz” algebrę liniową. Sprawdź się zadaniem Z-02.5 i Z-02.6.
2. Rozdziały **06–10** to rdzeń olimpiady (najczęstsze typy zadań).
3. Rozdziały **11–15** dają punkty na finale (sprzęt, błędy, narzędzia).
4. Rozdziały **16–20** podnoszą pułap: dane, formalizm, granice, projekty.
