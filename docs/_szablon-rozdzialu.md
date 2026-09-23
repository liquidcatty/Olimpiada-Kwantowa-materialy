# Szablon rozdziału teorii (obowiązkowy)

Każdy plik w `teoria/` ma **dokładnie** poniższą strukturę sekcji i nagłówek.

```markdown
# NN. Tytuł rozdziału


## 1. Po co to jest

2–4 akapity: gdzie w Olimpiadzie (i w fizyce/informatyce kwantowej) używa się
tych treści. Konkretne odwołania do zadań P1–P4 oraz do algorytmów, jeśli to możliwe.

## 2. Najważniejsze definicje

Definicje w punktach, każda z symbolem i intuicją.

## 3. Teoria krok po kroku

Podsekcje 3.1, 3.2, ... Wzory w LaTeX (`$...$`, `$$...$$`). Każdy nietrywialny wzór
z komentarzem „skąd to się bierze”. Tabele tam, gdzie pomagają.

## 4. Przykłady rozwiązane

Co najmniej **2 przykłady** rozwiązane w pełni: dane → metoda → rachunek → wynik →
interpretacja. Jeden przykład łatwy, jeden trudniejszy.

## 5. Typowe pułapki

Lista błędów, które uczestnicy popełniają najczęściej (z wyjaśnieniem, jak ich uniknąć).

## 6. Zadania (Z-NN)

5–8 zadań z poleceniami (a), (b), (c). Poziom: od „sprawdź definicję” do
„olimpijskie”. Trudniejsze oznaczamy **[★]**.

## 7. Wskazówki do zadań

Po jednym–dwóch zdaniach wskazówki na zadanie (BEZ gotowych wyników — pełne
rozwiązania są w `zadania/rozwiazania/rozwiazania-NN.md`).

## 8. Co dalej

Odsyłacze do kolejnych rozdziałów, bibliografia (pozycje z `docs/bibliografia.md`).
```

## Zasady treści

1. **Zero placeholderów.** Każdy wzór sprawdzony rachunkiem, każda liczba policzona.
2. **Definicja przed twierdzeniem**, twierdzenie przed przykładem.
3. Oznaczenia **zgodne z `docs/03-konwencje-i-notacja.md`** (Dirac, małoendianowa
   kolejność kubitów, $\theta/2$ w bramkach obrotu).
4. Zakres: pokryć temat warsztatu i wyjść ponad niego tam, gdzie jest to potrzebne
   do zrozumienia tematu.
5. Każdy rozdział kończy się działającym odsyłaczem do skryptu z `kod/`, jeśli
   temat da się zasymulować.
6. Długość: 150–350 linii.

## Zasady pliku z rozwiązaniami (`zadania/rozwiazania/rozwiazania-NN.md`)

```markdown
# Rozwiązania do rozdziału NN

## Z-NN.1
(a) ...krok po kroku...
**Odpowiedź:** ...
## Z-NN.2
...
```

- Każde rozwiązanie: pełny rachunek, wynik wyróżniony **pogrubieniem**, krótki
  komentarz „co to znaczy fizycznie”.
- Jeśli zadanie da się sprawdzić numerycznie — dopisz jedno zdanie, jak i podaj
  wynik (można wskazać skrypt z `kod/`).
