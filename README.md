# Przewodnik po Olimpiadzie Kwantowej

Kompletny, samowystarczalny materiał do przygotowania się do **Olimpiady Kwantowej**
(<https://olimpiadakwantowa.pl/>) — od liczb zespolonych, przez mechanikę kwantową,
bramki i algorytmy, aż po sprzęt, korekcję błędów i analizę danych. Zakres jest nieco szerszy niż program olimpiady.

Każdy temat ma: **teorię** (z wyprowadzeniami), **przykłady rozwiązane krok po kroku**,
**zadania** z pełnymi rozwiązaniami, **pracę domową** do oddania i **kod** w Pythonie,
który pozwala sprawdzić rachunek numerycznie. Przewodnik jest nieoficjalny;
prawa do tekstów zadań organizatora należą do Fundacji Quantum AI.


## 1. Najważniejsze informacje o Olimpiadzie (I edycja, 2026/2027)

| Element | Szczegóły |
| --- | --- |
| Organizator | Fundacja Quantum AI, ul. Sanocka 9/103, 02-110 Warszawa |
| Charakter | ogólnopolski, indywidualny, trzyetapowy konkurs edukacyjny |
| Dla kogo | uczniowie szkół ponadpodstawowych (także zdolni uczniowie szkół podstawowych z rekomendacją) |
| Rejestracja | 10.09.2026 – 28.02.2027, bezpłatnie, przez system na stronie Olimpiady |
| Etap I | zdalny · otwarcie 15.11.2026 12:00 · oddanie rozwiązań **28.02.2027 23:59** · wyniki do 31.03.2027 |
| Etap II | rozmowa kwalifikacyjna online · 01.04–30.04.2027 · 20–30 min, komisja ≥ 3 osoby · zakres = zadania Etapu I |
| Etap III | finał stacjonarny w Krakowie · 4–7.06.2027 |
| Wynik końcowy | **tylko punkty finału** (punkty I i II etapu nie są doliczane) |
| Dozwolone w Etapie I | podręczniki, publikacje, notatki, kalkulator, narzędzia obliczeniowe, AI jako pomoc (użycie trzeba opisać w pracy i **nie wolno** oddać pracy wygenerowanej w całości przez AI) |

Terminy i zasady weryfikuj na stronie organizatora — powyższe pochodzi z publicznego
regulaminu i harmonogramu w dniu tworzenia przewodnika.

## 2. Jak korzystać z przewodnika

Trzy ścieżki — wybierz swoją:

| Masz | Ścieżka | Od czego zacząć |
| --- | --- | --- |
| 5–6 miesięcy do deadline'u Etapu I | **pełna** | [plan nauki 20 tygodni](docs/01-plan-nauki.md) → rozdziały 01–16 → PD-1…PD-4 |
| 4 tygodnie | **skrócona** | [plan nauki](docs/01-plan-nauki.md) → rdzeń: 02, 05, 06, 08, 09, 13 |
| 3 dni | **ratunkowa** | [ściąga wzorów](docs/06-sciaga-wzorow.md) → [zadania przykładowe P1–P4](zadania/treningowe/README.md) z rozwiązaniami → [strategia rozwiązywania zadań](docs/04-strategia-rozwiazywania-zadan.md) |

Kolejność czytania:

1. [Jak korzystać z przewodnika](docs/00-jak-korzystac.md) — konwencje pracy, jak
   odrabiać pracę domową, jak sprawdzać swoje wyniki.
2. [Zakres materiału](docs/02-zakres-materialu.md) — mapowanie 16 warsztatów
   Olimpiady na rozdziały tego repo.
3. [Konwencje i notacja](docs/03-konwencje-i-notacja.md) — jeden język symboli
   w całym repo (Dirac, sfera Blocha, kolejność kubitów).
4. [Zadania przykładowe organizatora (P1–P4) z pełnymi rozwiązaniami](zadania/treningowe/README.md).

## 3. Struktura repozytorium

```
.
├── README.md                     ← ten plik (start tutaj)
├── docs/                         ← plan nauki, zakres, notacja, ściąga wzorów, bibliografia
│   ├── 00-jak-korzystac.md
│   ├── 01-plan-nauki.md
│   ├── 02-zakres-materialu.md
│   ├── 03-konwencje-i-notacja.md
│   ├── 04-strategia-rozwiazywania-zadan.md
│   ├── 05-przygotowanie-do-etapu-2.md
│   ├── 06-sciaga-wzorow.md
│   ├── bibliografia.md
│   └── _szablon-rozdzialu.md
├── teoria/                       ← 20 rozdziałów: teoria + przykłady + zadania
├── zadania/
│   ├── treningowe/               ← oficjalne P1–P4 (treść + rozwiązania modelowe)
│   └── rozwiazania/              ← pełne rozwiązania zadań Z-NN z rozdziałów teorii
├── praca-domowa/                 ← PD-1 … PD-4 (do oddania) + kryteria oceny
├── kod/                          ← symulatory i weryfikacja numeryczna (Python + NumPy)
├── tools/                        ← skrypty pomocnicze (kontrola linków w CI)
└── .github/workflows/            ← CI: uruchamia verify_all.py i kontrolę linków
```

## 4. Spis rozdziałów teorii

### Moduł 1 — matematyka (rozdziały 01–05)

| # | Rozdział | Warsztat Olimpiady |
| --- | --- | --- |
| 01 | [Liczby zespolone](teoria/01-liczby-zespolone.md) | Liczby zespolone |
| 02 | [Algebra liniowa](teoria/02-algebra-liniowa.md) | Algebra liniowa |
| 03 | [Rachunek prawdopodobieństwa i statystyka](teoria/03-rachunek-prawdopodobienstwa-i-statystyka.md) | Rachunek prawdopodobieństwa i statystyka |
| 04 | [Elementy analizy matematycznej](teoria/04-elementy-analizy-matematycznej.md) | Elementy analizy matematycznej |
| 05 | [Podstawy mechaniki kwantowej](teoria/05-podstawy-mechaniki-kwantowej.md) | Podstawy mechaniki kwantowej i układy kwantowe |

### Moduł 2 — kubity, informacja, algorytmy (06–10)

| # | Rozdział | Warsztat Olimpiady |
| --- | --- | --- |
| 06 | [Kubity, bramki, obwody, pomiary](teoria/06-kubity-bramki-obwody-pomiary.md) | Kubity, bramki, obwody, pomiary |
| 07 | [Kwantowa teoria informacji](teoria/07-kwantowa-teoria-informacji.md) | Kwantowa teoria informacji |
| 08 | [Podstawowe algorytmy kwantowe](teoria/08-algorytmy-kwantowe.md) | Podstawowe algorytmy kwantowe |
| 09 | [Splątanie i twierdzenie Bella](teoria/09-splatanie-i-twierdzenie-bella.md) | Splątanie i twierdzenie Bella |
| 10 | [Kryptografia kwantowa](teoria/10-kryptografia-kwantowa.md) | Kryptografia kwantowa |

### Moduł 3 — sprzęt, błędy, narzędzia (11–15)

| # | Rozdział | Warsztat Olimpiady |
| --- | --- | --- |
| 11 | [Metrologia kwantowa](teoria/11-metrologia-kwantowa.md) | Podstawy metrologii kwantowej |
| 12 | [Realizacje komputerów kwantowych](teoria/12-realizacje-komputerow-kwantowych.md) | Realizacje komputerów kwantowych |
| 13 | [Korekcja i mitygacja błędów](teoria/13-korekcja-i-mitygacja-bledow.md) | Korekcja i mitygacja błędów |
| 14 | [Narzędzia informatyczne](teoria/14-narzedzia-informatyczne.md) | Narzędzia informatyczne |
| 15 | [Oprogramowanie kwantowe](teoria/15-oprogramowanie-kwantowe.md) | Oprogramowanie kwantowe |

### Moduł 4 — dane i tematy rozszerzające (16–20)

| # | Rozdział | Uwaga |
| --- | --- | --- |
| 16 | [Analiza danych i obliczenia naukowe](teoria/16-analiza-danych-i-obliczenia-naukowe.md) | warsztat Olimpiady |
| 17 | [Macierze gęstości i kanały kwantowe](teoria/17-ponad-program-macierze-gestosci-i-kanaly.md) | ponad program |
| 18 | [Splątanie, dekoherencja, termodynamika](teoria/18-ponad-program-splatanie-dekoherencja-termodynamika.md) | ponad program |
| 19 | [Algorytmy zaawansowane i granice informacyjne](teoria/19-ponad-program-algorytmy-zaawansowane-i-granice.md) | ponad program |
| 20 | [Mini-projekty zaliczeniowe](teoria/20-ponad-program-mini-projekty.md) | ponad program |

Każdy rozdział `NN` ma lustrzany plik z rozwiązaniami:
`zadania/rozwiazania/rozwiazania-NN.md`.

## 5. Prace domowe

| Zestaw | Zakres | Plik |
| --- | --- | --- |
| PD-1 | rozdziały 01–05 (matematyka + mechanika kwantowa) | [praca-domowa-01.md](praca-domowa/praca-domowa-01.md) |
| PD-2 | rozdziały 06–10 (kubity, informacja, algorytmy, splątanie, QKD) | [praca-domowa-02.md](praca-domowa/praca-domowa-02.md) |
| PD-3 | rozdziały 11–15 (metrologia, sprzęt, błędy, narzędzia, software) | [praca-domowa-03.md](praca-domowa/praca-domowa-03.md) |
| PD-4 | rozdziały 16–20 (dane + tematy rozszerzające) | [praca-domowa-04.md](praca-domowa/praca-domowa-04.md) |

Każdy zestaw: 10 zadań, 20 punktów, kryteria oceny, wskazówki i odpowiedzi.
Szczegóły: [praca-domowa/README.md](praca-domowa/README.md).

## 6. Kod — sprawdzaj rachunki numerycznie

```powershell
python -m pip install numpy            # wymagane
python -m pip install matplotlib       # opcjonalne (wykresy)
python kod/verify_all.py               # uruchamia wszystkie skrypty i wypisuje OK/FAIL
```

| Skrypt | Co robi |
| --- | --- |
| `kod/verify_all.py` | uruchamia wszystkie moduły, zbiera wyniki, wypisuje raport |
| `kod/simulator.py` | własny symulator obwodów n kubitów (m.in. H, X, Y, Z, S, T, R_X/Y/Z, CNOT, CZ) |
| `kod/p1_studnia.py` | zadanie P1: normalizacja, prawdopodobieństwa, ⟨E⟩ |
| `kod/p2_polaryzatory.py` | zadanie P2: prawo Malusa dla wiązki i pojedynczego fotonu |
| `kod/p3_hzh.py` | zadanie P3: HZH = X, rozkład wyników pomiaru |
| `kod/p4_cnot_ry.py` | zadanie P4: stan po CNOT, P_00…P_11, ⟨Z⊗Z⟩ |
| `kod/grover.py` | Grover dla N=4 i N=8: liczba iteracji vs sukces |
| `kod/chsh.py` | nierówność CHSH: maksimum kwantowe 2√2 |
| `kod/bb84.py` | symulacja BB84 z podsłuchem i statystyką QBER |
| `kod/teleportacja.py` | teleportacja kwantowa z pełnym rachunkiem |
| `kod/korekcja_3bit.py` | kod powtarzalny 3-kubitowy: syndromy i korekta |
| `kod/metrologia_faza.py` | estymacja fazy: granica śrutowa vs Heisenberga |
| `kod/analiza_danych.py` | dopasowanie, χ², niepewności, bootstrap, FFT |

## 7. Dokumenty pomocnicze

| Plik | Zawartość |
| --- | --- |
| [docs/00-jak-korzystac.md](docs/00-jak-korzystac.md) | pętla nauki, wysyłka pracy, check-lista |
| [docs/01-plan-nauki.md](docs/01-plan-nauki.md) | plan 20 tygodni, plan 4 tygodni, plan ratunkowy |
| [docs/02-zakres-materialu.md](docs/02-zakres-materialu.md) | mapa warsztatów i tematy rozszerzające |
| [docs/03-konwencje-i-notacja.md](docs/03-konwencje-i-notacja.md) | jeden język symboli, konwencje kodu |
| [docs/04-strategia-rozwiazywania-zadan.md](docs/04-strategia-rozwiazywania-zadan.md) | schematy rozwiązań, jak nie tracić punktów |
| [docs/05-przygotowanie-do-etapu-2.md](docs/05-przygotowanie-do-etapu-2.md) | rozmowa kwalifikacyjna: pytania i odpowiedzi |
| [docs/06-sciaga-wzorow.md](docs/06-sciaga-wzorow.md) | wszystkie wzory w jednym miejscu |
| [docs/07-faq-i-organizacja.md](docs/07-faq-i-organizacja.md) | rejestracja, wysyłka pracy, co wolno, check-lista |
| [docs/08-slownik-pojec-pl-en.md](docs/08-slownik-pojec-pl-en.md) | słownik pojęć polsko-angielski |
| [docs/bibliografia.md](docs/bibliografia.md) | książki, kursy, dokumentacje, filmy |
| [tools/README.md](tools/README.md) | opis wszystkich narzędzi kontroli jakości |
| [tools/check_links.py](tools/check_links.py) | kontrola linków relatywnych (używana w CI) |
| [tools/audit_github_math.py](tools/audit_github_math.py) | kontrola renderowania matematyki na GitHub (używana w CI) |
| [tools/audit_content.py](tools/audit_content.py) | kontrola składni LaTeX i pozostałości meta-komentarzy |
| [tools/verify_structure.py](tools/verify_structure.py) | kontrola struktury rozdziałów, zadań i prac domowych (używana w CI) |

## 8. Publikacja tego repo na GitHub

Repozytorium jest już zainicjalizowane lokalnie (branch `main`). Aby opublikować je
na GitHubie:

```powershell
git add -A
git commit -m "Przewodnik po Olimpiadzie Kwantowej: teoria, zadania, prace domowe, kod"
gh repo create olimpiada-kwantowa-przewodnik --public --source=. --remote=origin --push
# ...albo bez GitHub CLI:
git remote add origin https://github.com/<twoj-login>/olimpiada-kwantowa-przewodnik.git
git push -u origin main
```

CI (`.github/workflows/verify.yml`) automatycznie uruchomi `python kod/verify_all.py`
oraz `python tools/check_links.py` przy każdym pushu i pull requeście.

## 9. Współpraca i licencja

- Znalazłeś błąd albo chcesz dodać zadanie? Zobacz [CONTRIBUTING.md](CONTRIBUTING.md).
- Kod: licencja MIT (plik [LICENSE](LICENSE)).
- Teksty zadań organizatora i dokumenty Fundacji Quantum AI pozostają własnością
  ich twórców — używamy ich wyłącznie w celach edukacyjnych, z podaniem źródła.

