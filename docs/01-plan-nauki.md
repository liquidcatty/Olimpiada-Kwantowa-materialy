# Plan nauki

Dwa warianty: pełny (20 tygodni) i szybki (4 tygodnie). Zasada: **każdy tydzień =
teoria + zadania + praca domowa**. Bez odrabiania prac domowych plan nie działa.

## 1. Wariant pełny — 20 tygodni (od października 2026 do końca lutego 2027)

| Tydzień | Rozdziały | Praca domowa | Kamień milowy |
| --- | --- | --- | --- |
| 1 | 01 Liczby zespolone | — | umiesz liczyć |z|, fazę, potęgi i pierwiastki |
| 2 | 02 Algebra liniowa | — | liczysz macierze 2×2, wektory własne, kron |
| 3 | 03 Prawdopodobieństwo i statystyka | PD-1 (po tygodniu 5) | znasz rozkłady i CTG |
| 4 | 04 Elementy analizy | — | liczysz całki i RRC, znasz transformatę Fouriera |
| 5 | 05 Podstawy mechaniki kwantowej + powtórka 01–04 | **PD-1** | rozwiązujesz P1 i P2 samodzielnie |
| 6 | 06 Kubity, bramki, obwody, pomiary | — | rozwiązujesz P3 i P4 samodzielnie |
| 7 | 06 (algorytmika obwodów) + 07 Teoria informacji | — | rozumiesz no-cloning i entropię |
| 8 | 08 Podstawowe algorytmy kwantowe | PD-2 (po tygodniu 10) | umiesz ręcznie przejść Grovera dla N=4 |
| 9 | 09 Splątanie i twierdzenie Bella | — | wyprowadzasz CHSH i znasz wartość 2√2 |
| 10 | 10 Kryptografia kwantowa + powtórka 06–09 | **PD-2** | przeprowadzasz BB84 na kartce |
| 11 | 11 Metrologia kwantowa | — | rozróżniasz 1/√N i 1/N |
| 12 | 12 Realizacje komputerów kwantowych | — | porównujesz technologie w tabeli |
| 13 | 13 Korekcja i mitygacja błędów | — | liczysz syndrom kodu 3-kubitowego |
| 14 | 14 Narzędzia informatyczne | PD-3 (po tygodniu 15) | pracujesz z terminalem i gitem |
| 15 | 15 Oprogramowanie kwantowe + powtórka 11–14 | **PD-3** | piszesz własny obwód w Qiskit/NumPy |
| 16 | 16 Analiza danych i obliczenia naukowe | — | dopasowujesz model i raportujesz χ² |
| 17 | 17 Macierze gęstości i kanały | — | liczysz ślad częściowy i kanał Krausa |
| 18 | 18 Splątanie, dekoherencja, termodynamika | PD-4 (po tygodniu 20) | rozumiesz T1/T2 i zasadę Landauera |
| 19 | 19 Algorytmy zaawansowane i granice | — | przeprowadzasz teleportację krok po kroku |
| 20 | 20 Mini-projekty + **powtórka całego materiału** | **PD-4** | robisz 1 mini-projekt i raport |
| 21–22 | bufor: powtórka, rozwiązywanie arkusza przykładowego, próba własnych zadań | — | gotowość na Etap I |

Etap I: 15.11.2026–28.02.2027. Rozpoczęcie nauki w połowie października 2026
pozwala ukończyć plan z dwutygodniowym buforem.

## 2. Rozkład tygodnia (7–9 h pracy)

| Blok | Czas | Co robisz |
| --- | --- | --- |
| Teoria | 2,0–2,5 h | rozdział + własna ściąga (5–10 wzorów) |
| Przykłady rozwiązane | 1,0 h | przepisujesz z pamięci |
| Zadania Z-NN | 2,0–2,5 h | samodzielnie, potem porównanie z rozwiązaniami |
| Kod | 0,5–1,0 h | `python kod/verify_all.py` + modyfikacja własna |
| Praca domowa (w tygodniu PD) | 1,5–2,0 h | pełny zestaw, na czas, bez podglądania |
| Powtórka | 0,5 h | 2 zadania z poprzedniego tygodnia |

## 3. Wariant szybki (4 tygodnie)

| Tydzień | Treść | Efekt |
| --- | --- | --- |
| 1 | 01, 02, 05, 06, P1–P4 | umiesz liczyć na macierzach i rozwiązywać obwody |
| 2 | 03, 07, 08, 09 | rozumiesz pomiary, splątanie i algorytmy |
| 3 | 04, 10, 11, 13 | kryptografia, metrologia, korekcja błędów |
| 4 | 12, 16, 17 + PD-1…PD-4 w skrócie | domykasz zakres i ćwiczysz rachunki |

W tym wariancie pomija się rozdziały 14, 15, 18, 19, 20.

## 4. Wariant ratunkowy (3 dni)

1. Przeczytaj [ściągę wzorów](06-sciaga-wzorow.md) (2 h).
2. Przerób [P1–P4 z rozwiązaniami](../zadania/treningowe/README.md) i spróbuj
   rozwiązać je bez patrzenia (3 h).
3. Zrób rozdziały 02, 05, 06: przykłady rozwiązane + 3 zadania z każdego (6 h).
4. Przygotuj sposób zapisu pracy: kartka → zdjęcie/PDF, albo Jupyter z rachunkami
   (1 h). Sprawdź check-listę wysyłki w `docs/00-jak-korzystac.md`.

## 5. Etap II i finał

- **Etap II** (1–30.04.2027): powtórz **własne** rozwiązania Etapu I i przygotuj
  się na pytania „skąd to wiesz?”. Instrukcja: [przygotowanie do Etapu II](05-przygotowanie-do-etapu-2.md).
- **Finał** (4–7.06.2027): tematy 17–20, mini-projekty, praca z danymi i szumem.
  Finał może zawierać zadania teoretyczne, programistyczne, analizę danych i część
  doświadczalną — dlatego rozdziały 16, 20 i kod w `kod/` są obowiązkowe.
