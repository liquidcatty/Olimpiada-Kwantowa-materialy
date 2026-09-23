# Strategia rozwiązywania zadań

Ten dokument opisuje **jak** pisać rozwiązania, żeby dostać maksimum punktów.
Kryteria organizatora mówią wprost: liczą się poprawność, kompletność i **jakość
uzasadnienia**, a przy zadaniach obliczeniowych także efektywność metody,
analiza błędów i interpretacja fizyczna.

## 1. Uniwersalny schemat rozwiązania (7 kroków)

1. **Dane i szukane.** Wypisz symbole z jednostkami oraz to, co masz wyznaczyć.
   Jeśli czegoś brakuje — nazwij to i założ.
2. **Model.** Napisz, jakim prawem opisujesz układ (np. „pomiar rzutowy w bazie
   obliczeniowej: $P(k)=|\langle k|\psi\rangle|^2$”).
3. **Rachunek symboliczny.** Przekształcaj symbole, nie liczby. Kolejność operacji
   zapisuj jawnie (np. stan po każdej bramce).
4. **Podstawienie liczb.** Osobny, wyraźnie oznaczony krok. Utrzymuj jednostki.
5. **Kontrola poprawności.**
   - wymiar wyniku (np. prawdopodobieństwo bezwymiarowe, energia w J),
   - rząd wielkości (nie $10^{23}$ tam, gdzie spodziewamy się $0{,}5$),
   - suma prawdopodobieństw $=1$,
   - granice: $\theta\to0$, $\theta\to\pi$, $L\to\infty$, $N\to1$, brak szumu.
6. **Weryfikacja numeryczna** (jeśli wolno używać narzędzi): „sprawdziłem
   symulacją w NumPy, wynik zgadza się do 12 cyfr”.
7. **Interpretacja.** 1–3 zdania: co wynik znaczy fizycznie, dlaczego jest
   zaskakujący/naturalny, co by się zmieniło przy innym ustawieniu.

## 2. Schematy dla typowych typów zadań

### 2.1 Obwód kwantowy (jak P3, P4)

```
1. Wypisz stan początkowy jako wektor.
2. Zapisz każdą bramkę jako macierz w ustalonej bazie.
3. Złóż macierze zgodnie z kolejnością działania (najpierw działająca najbardziej z prawej!).
4. Pomnóż macierz przez wektor — pokaż wynik pośredni po każdej bramce.
5. Prawdopodobieństwa = kwadraty modułów odpowiednich amplitud.
6. Wartość oczekiwana = ⟨ψ|A|ψ⟩ (nie mylić z pojedynczym wynikiem pomiaru!).
```

**Pułapka numer 1:** kolejność mnożenia. Reguła: $\lvert\psi'\rangle = U_2U_1\lvert\psi\rangle$,
jeśli najpierw zadziałała $U_1$, potem $U_2$. Najczęściej działającą bramką stoi
**najbliżej wektora**.

**Pułapka numer 2:** splątanie. Stan jest splątany wtedy i tylko wtedy, gdy
**nie da się** go zapisać jako $\lvert\psi_A\rangle\otimes\lvert\psi_B\rangle$.
Sama superpozycja (np. $(|00\rangle+|11\rangle)/\sqrt2$) to jeszcze nie dowód —
trzeba spróbować rozkładu; pomaga rozkład Schmidta.

### 2.2 Pomiar i prawdopodobieństwa

- Zawsze sprawdzaj $P_i\ge0$ i $\sum_i P_i=1$.
- Rozróżniaj **prawdopodobieństwo wyniku** od **wartości oczekiwanej**.
- Jeśli pytają „ile wynosi natężenie”, a Ty liczysz prawdopodobieństwo fotonu:
  przelicz $I = I_0\cdot P$ (prawo Malusa).

### 2.3 Mechanika kwantowa (studnia, oscylator)

```
1. Zapisz równanie własne Hψ = Eψ i warunki brzegowe.
2. Unormuj: ∫|ψ|²dx = 1.
3. Rozłóż stan na stany własne: ψ = Σ c_n ψ_n,  c_n = ⟨ψ_n|ψ⟩.
4. P(E_n) = |c_n|²,  ⟨E⟩ = Σ |c_n|² E_n.
```

### 2.4 Estymacja i statystyka

- $\mathrm{Var}$ granicy śrutowej: $\sigma(\hat\varphi)\ge\frac{1}{\sqrt{N}}$.
- Odpowiedź na „ile pomiarów potrzeba, żeby uzyskać dokładność ε” wyprowadzaj
  z nierówności Craméra–Rao, nie zgaduj.

### 2.5 Zadania programistyczne

- Kod **krótki i czytelny**; nazwy zmiennych mówiące.
- Wynik liczbowy wypisz z dokładnością, jakiej wymaga polecenie.
- Dołącz krótki komentarz: „co liczę i dlaczego wynik ma sens”.
- Jeśli używałeś AI jako pomocy: zaznacz to w pracy i opisz, do czego.

## 3. Jak nie tracić punktów

| Błąd | Skutek | Jak uniknąć |
| --- | --- | --- |
| Brak jednostek | punkty ujemne w kryteriach | zapisuj jednostki w każdym kroku |
| Skok w rachunku „oczywiste” | brak punktów za tok rozumowania | pokaż przejście |
| Wstawienie liczb na starcie | błędy i zaokrąglenia kumulują się | licz symbolicznie |
| Brak wniosku | brak punktów za interpretację | 1–3 zdania na koniec |
| Zły kąt: $\theta$ vs $\theta/2$ | wynik błędny w 100% | patrz `docs/03-konwencje-i-notacja.md` |
| Kolejność bramek odwrotna | stan błędny | zapisz iloczyn macierzy i sprawdź małym przypadkiem |
| Brak normalizacji stanu | prawdopodobieństwa nie sumują się do 1 | zawsze sprawdzaj |
| Imię i nazwisko w pracy | naruszenie anonimowości | prace są anonimowe — nie podpisuj się danymi osobowymi |

## 4. Technika egzaminacyjna

1. **Przeczytaj wszystkie zadania** przed startem i zacznij od tego, które umiesz
   najlepiej (buduje czas i pewność siebie).
2. **Budżet czasu**: tyle minut, ile (punktów za zadanie × 2), minimum 10 min.
3. **Najpierw szkic rozwiązania** (pół strony), potem czystopis.
4. **Nie zostawiaj pustych miejsc** — nawet niepełne rozwiązanie z widocznym
   tokiem myślenia daje punkty.
5. **Sprawdź przed wysłaniem**: normalizacja, jednostki, granice, czytelność
   pliku, brak danych osobowych.

## 5. Self-check: 10 pytań do każdego zadania

1. Czy wiem, czego szukam i w jakich jednostkach?
2. Czy nazwałem prawo/wzór, którego używam?
3. Czy kolejność operacji jest zgodna z fizyką (a nie z moim nawykiem)?
4. Czy sprawdziłem przypadek graniczny?
5. Czy prawdopodobieństwa sumują się do 1?
6. Czy wynik jest zgodny z intuicją (lub umiem wyjaśnić, dlaczego nie)?
7. Czy odpowiedź brzmi jak odpowiedź na zadane pytanie (a nie na inne)?
8. Czy zapisałem wynik z sensowną dokładnością?
9. Czy dałoby się sprawdzić to numerycznie (i czy to zrobiłem)?
10. Czy napisałem interpretację?
