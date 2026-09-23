# Współpraca (CONTRIBUTING)

Dzięki, że chcesz pomóc! Ten przewodnik jest materiałem społeczności i każda
poprawka merytoryczna jest cenna.

## 1. Zgłaszanie błędów

Otwórz **Issue** i podaj:

1. plik i numer linii (np. `teoria/06-kubity-bramki-obwody-pomiary.md:142`),
2. co Twoim zdaniem jest błędne,
3. poprawną wersję wraz z uzasadnieniem (rachunkiem albo źródłem).

Wzór błędu: `[literówka]` / `[rachunek]` / `[merytoryczny]` / `[niespójność notacji]`.

## 2. Zasady dla nowych treści

- **Notacja**: obowiązkowo zgodna z [docs/03-konwencje-i-notacja.md](docs/03-konwencje-i-notacja.md).
- **Struktura rozdziału teorii**: obowiązkowo wg [docs/_szablon-rozdzialu.md](docs/_szablon-rozdzialu.md)
  (sekcje 1–8, w tym „Przykłady rozwiązane”, „Typowe pułapki”, „Zadania (Z-NN)”,
  „Wskazówki do zadań”).
- **Każde nowe zadanie** musi mieć: treść w rozdziale, pełne rozwiązanie w
  `zadania/rozwiazania/rozwiazania-NN.md`, punktację i poziom trudności.
- **Każdy nowy wzór** musi być albo wyprowadzony, albo źródłowany.
- **Każdy nowy skrypt** w `kod/` musi:
  - mieć docstring z opisem i przykładowym wynikiem,
  - dać się uruchomić przez `python kod/<plik>.py`,
  - kończyć się asercjami wypisującymi `OK`/`FAIL`,
  - nie wymagać niczego poza NumPy (matplotlib tylko opcjonalnie, w `try/except`).
- Nowe skrypty rejestrujemy w `kod/verify_all.py` (lista `MODULES`).
- Język: polski. Terminy angielskie w nawiasie przy pierwszym użyciu.

## 3. Nazewnictwo plików

- Rozdziały teorii: `teoria/NN-krotki-tytul.md` (bez polskich znaków w nazwie).
- Rozwiązania: `zadania/rozwiazania/rozwiazania-NN.md`.
- Prace domowe: `praca-domowa/praca-domowa-NN.md`.
- Kod: `kod/snake_case.py`.

## 4. Checklist przed Pull Requestem

- [ ] Uruchomiłem `python kod/verify_all.py` i wszystko daje `OK`.
- [ ] Sprawdziłem wszystkie linki relatywne w zmienianych plikach.
- [ ] Zadania mają rozwiązania i odpowiedzi.
- [ ] Notacja jest zgodna z konwencjami (w tym kolejność kubitów i $\theta/2$).
- [ ] Nie dodałem danych osobowych ani cudzych rozwiązań bez zgody.

## 5. Prawa autorskie

- Kod: MIT (zobacz [LICENSE](LICENSE)).
- Teksty zadań i dokumenty Fundacji Quantum AI: używamy wyłącznie w celach
  edukacyjnych z podaniem źródła; nie kopiujemy ich w wersji zmodyfikowanej
  sugerującej autorstwo repo.
- Nie wklejamy rozwiązań zadań z innych olimpiad ani z cudzych prac bez zgody autora.
