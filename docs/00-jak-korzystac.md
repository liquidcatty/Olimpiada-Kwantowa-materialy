# Jak korzystać z tego przewodnika

## 1. Pętla nauki (rób to zawsze tak samo)

1. **Teoria** — przeczytaj rozdział z `teoria/`. Nie notuj całych wyprowadzeń:
   notuj tylko definicje, wzory i „dlaczego tak”.
2. **Przykłady rozwiązane** — przeczytaj, zamknij plik i rozwiąż je **jeszcze raz
   na kartce**, bez podglądania. To najważniejszy krok.
3. **Zadania Z-NN** — rozwiąż samodzielnie. Wskazówki są w rozdziale, pełne
   rozwiązania w `zadania/rozwiazania/rozwiazania-NN.md`. Zajrzyj tam
   **dopiero po** własnej próbie.
4. **Kod** — uruchom odpowiadający skrypt z `kod/` i sprawdź, czy Twoje liczby
   się zgadzają (patrz sekcja 4 poniżej).
5. **Praca domowa** — raz w tygodniu zrób pełny zestaw PD-N w warunkach
   egzaminacyjnych: bez podglądania, z czasem, na czystej kartce.
6. **Powtórka** — po tygodniu wróć do rozdziału i spróbuj rozwiązać 2 zadania
   z pamięci. To ujawnia prawdziwe braki.

## 2. Notatnik wzorów

Prowadź własny plik `moja-sciaga.md`. Zasada: **jeden wzór = jedna linia + jedno
zdanie, kiedy go użyć**. Po każdym rozdziale dopisz 5–10 pozycji. Ściąga wzorów tego
repozytorium (`docs/06-sciaga-wzorow.md`) jest wzorem do naśladowania, nie do
wkuwania — wzory trzeba umieć **wyprowadzić**, nie tylko rozpoznać.

## 3. Jak rozwiązywać zadania olimpijskie

Szczegółowo: [strategia rozwiązywania zadań](04-strategia-rozwiazywania-zadan.md).
Skrót:

1. Wypisz **dane** i **szukane**, z jednostkami.
2. Nazwij prawa, których użyjesz (nazwa + wzór).
3. Rachunek **symboliczny** tak długo, jak się da — liczby wstawiaj na końcu.
4. Sprawdź **wymiar i rząd wielkości** wyniku.
5. Sprawdź **przypadki brzegowe** (θ=0, θ=π, N→1, brak szumu) — tam wynik musi mieć
   sens fizyczny.
6. Napisz **interpretację** (1–3 zdania). Za to daje się punkty.
7. Brudnopis zostaw: częściowe rozwiązanie z widocznym tokiem myślenia też daje punkty.

## 4. Jak sprawdzać się kodem

Repozytorium zakłada **Python 3.11 + NumPy** (reszta opcjonalnie).

```powershell
python -m pip install numpy          # wymagane
python -m pip install matplotlib     # opcjonalne, tylko wykresy
```

Sprawdzenie wszystkich przykładów z repo jednym poleceniem:

```powershell
python kod/verify_all.py
```

Skrypt uruchamia wszystkie moduły numeryczne i wypisuje `OK`/`FAIL` oraz tabelę
wyników. Jeśli wszystko przejdzie, Twoje rachunki z teorii zgadzają się z
symulacją. To jest Twoja najszybsza metoda autokorekty.

## 5. Zasady pracy domowej (PD-N)

- Zestaw rozwiąż **na kartce** albo w Jupyterze — jak na Olimpiadzie.
- Nagłówek pracy: numer zestawu, data, czas pracy.
- Ocena własna: policz punkty z sekcji „Kryteria oceny” w pliku PD.
- Poniżej 60% punktów → **wróć do rozdziałów** wymienionych w nagłówku PD i zrób
  powtórkę przed kolejnym zestawem.

## 6. Wysyłka pracy na Olimpiadę (check-lista organizatora)

- Etap I: pliki PDF (typowe), dopuszczalne też `.ipynb` / `.py` — zależy od zadania.
- Rękopis można wysłać jako zdjęcie JPEG: całe, ostre, czytelne, bez cieni.
- W pracy **nie umieszczaj** imienia, nazwiska ani szkoły — prace są anonimowe i
  ocenia się je po kodzie uczestnika.
- Praca jest oddana w momencie wysłania pliku (skan antywirusowy nie opóźnia odbioru).
- Do końca etapu możesz wgrać nową wersję — oceniana jest zawsze najnowsza.
- Jeśli użyłeś AI lub narzędzi zewnętrznych — **opisz to w pracy**.

## 7. Źródła i uczciwość

Podawaj źródła, których użyłeś (podręcznik, wykład, artykuł). Nie kopiuj cudzych
rozwiązań: to podstawa dyskwalifikacji ([Regulamin](https://olimpiadakwantowa.pl/regulamin/),
Rozdział VII). Ten przewodnik ma Cię nauczyć rozumieć, a nie dać gotowca do
przepisania — w Etapie II i tak zapytają Cię o każdy krok Twojego rozwiązania.
