# 20. Mini-projekty zaliczeniowe


## 1. Zakres rozdziału

Rozdział zawiera sześć mini-projektów zaliczeniowych o jednakowej strukturze: **cel, wymagania,
plan krok po kroku, kryteria oceny, wariant trudniejszy, czas**. Projekty obejmują symulację
(rozdziały 06, 08), protokoły (10), metrologię (11), teleportację (19) i analizę danych (16), a
każdy z nich kończy się **raportem** (2–5 stron + kod w załączniku). Schemat projektu to
**cel → kod → dane → wynik → raport**.

Projekty wykonuje się w czystym NumPy (matplotlib opcjonalnie), bez SciPy i bez chmury; kod
wersjonuje się w `git`, a w raporcie podaje się **ziarno** generatora losowego. Podsekcja 3.2
zawiera szablon raportu, a 3.3 listę najczęstszych błędów obniżających ocenę.

## 2. Najważniejsze definicje

- **Cel projektu**: jedno zdanie „co chcemy zmierzyć/wykazać”, z liczbą i jednostką.
- **Wymagania (requirements)**: co musi działać (funkcje, wejście, wyjście, format danych).
- **Artefakt**: dostarczalny plik — kod `.py`, dane `.csv`, wykres `.png`, raport `.pdf`.
- **Punkt kontrolny (checkpoint)**: pośredni wynik, który da się sprawdzić **liczbą** (np. $P_{\rm sukces}=1$).
- **Test regresyjny**: asercja, która nie pozwala zepsuć wcześniejszej poprawki.
- **Reprodukowalność**: ten sam kod + dane + ziarno dają ten sam wynik.
- **Kryteria oceny**: jawna lista punktów (poprawność, wydajność, klarowność, raport).
- **Wariant trudniejszy**: rozszerzenie o szum, więcej kubitów lub sprzęt (Qiskit).
- **QBER**: współczynnik błędów w kluczu (rozdział 10); **granica Heisenberga**: $1/N$ (rozdział 11).
- **TDSE/symulator stanu**: reprezentacja $2^n$ amplitud i bramek jako macierzy (rozdział 06).

## 3. Teoria krok po kroku

### 3.1 Jak prowadzić projekt

1. **Zaplanuj cel liczbowo.** „Zbadać Grovera” to za mało; „policzyć $P_{\rm sukces}(k)$ dla
   $N=4,8$ i znaleźć $k_{\rm opt}$” to cel.
2. **Podziel na kroki.** Każdy krok kończy się działającym skryptem i **asercją**.
3. **Trzymaj stałą strukturę kodu.** Funkcje czyste (`build_state`, `measure`, `fit_curve`),
   `main()` z wypisaniem wyników i `OK/FAIL`.
4. **Zapisuj dane do CSV.** Wyniki uzupełniaj do pliku `wyniki.csv` (jedno uruchomienie = jeden plik).
5. **Rysuj jeden wykres na wynik.** Oś $x$, oś $y$ z jednostką, legenda, tytuł.
6. **Wersjonuj.** `git commit` po każdym działającym kroku; w raporcie podaj **hash commita**.
7. **Kontroluj losowość.** `rng = np.random.default_rng(seed)` i seed w raporcie.

### 3.2 Szablon raportu z projektu

```
1. Strona tytułowa: tytuł, autor, data, numer projektu (Z-20.k)
2. Cel: jedno–dwa zdania z liczbą (co i jak dokładnie mierzymy)
3. Metoda: model + wzory (numerowane), opis algorytmu pomiaru, ziarno
4. Wyniki: tabela + wykres; wartość z niepewnością w formacie x ± u (2 cyfry)
5. Dyskusja: zgodność z teorią, χ²/ndof, źródła rozbieżności, ograniczenia
6. Wnioski: 2–3 zdania; czego się nauczyliśmy
7. Załącznik A: kod (lub link do repo + hash), Załącznik B: surowe dane
8. Spis źródeł: podręczniki i dokumentacja (np. [bibliografia](../docs/bibliografia.md))
```

### 3.3 Najczęstsze błędy w raportach

1. **Brak niepewności i jednostek.** Wynik „$T_2=2{,}45$” bez $\pm$ i bez „s” — odrzucane.
2. **Brak ziarna / brak danych.** Wyniku nie da się odtworzyć.
3. **Wykres bez osi, jednostek, legendy.**
4. **Teoria bez numerów wzorów** — nie można się do nich odnieść.
5. **Wnioski sprzeczne z danymi** (np. „idealna zgodność” przy $\chi^2_{\rm red}=40$).
6. **Kod wklejony do treści** zamiast w załączniku; brak nagłówka z opisem i seedem.
7. **Zbyt wiele cyfr** w wyniku ($2{,}452837$) albo zbyt mało ($2$).
8. **Pomijanie przypadków granicznych** ($p=0$, $p=1$, $N=1$, brak detekcji).
9. **Brak porównania z teorią** albo z literą wzoru (ocena „co powinno wyjść”).
10. **Nieuczciwe „wygładzanie”** danych (usuwanie punktów bez uzasadnienia).

## 4. Przykłady rozwiązane

### Przykład 20.1 (łatwy): pełna tabela Grovera dla $N=4$ i $N=8$

**Cel.** Policzyć $P_{\rm sukces}(k)$ dla $k=0,1,2,3$ i wskazać $k_{\rm opt}$.

**Metoda.** $\sin\theta=1/\sqrt N$, $P(k)=\sin^2((2k+1)\theta)$; kontrola symulacją wektorową.

**Rachunek.** $N=4$: $\theta=\pi/6=0{,}5236$, więc $P(0)=\sin^2(\pi/6)=0{,}25$,
$P(1)=\sin^2(\pi/2)=1$, $P(2)=\sin^2(5\pi/6)=0{,}25$.
$N=8$: $\theta=\arcsin(1/\sqrt8)=0{,}3614$, stąd:

| $k$ | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| $P$ ($N=4$) | 0,25 | **1,00** | 0,25 | 0,25 |
| $P$ ($N=8$) | 0,125 | 0,781 | **0,945** | 0,330 |

**Odpowiedź:** $N=4$: $k_{\rm opt}=1$, $P=1$; $N=8$: $k_{\rm opt}=2$, $P=\mathbf{0{,}945}$.
*Interpretacja:* dla $N=8$ nadmiar iteracji ($k=3$) **psuje** wynik ($0{,}330$) — trzeba zatrzymać się
na $k_{\rm opt}$; tabela to punkt kontrolny projektu Z-20.3.

### Przykład 20.2 (trudniejszy): BB84 z podsłuchem intercept–resend

**Cel.** Wyznaczyć QBER jako funkcję odsetka $f$ podsłuchiwanych fotonów i zdecydować o przerwaniu
protokołu.

**Metoda.** Intercept–resend na jednym fotonie daje błąd z prawdopodobieństwem $\tfrac14$;
przy odsetku $f$ (reszta nietknięta) $\mathrm{QBER}=0{,}25f$.

**Rachunek.** Dla $f=0{,}2;0{,}5;1{,}0$: QBER $=0{,}05;0{,}125;0{,}25$. Próg bezpieczeństwa
$1-2H_2(e)=0$ daje $e\approx0{,}11$, czyli $f^\star=0{,}11/0{,}25=0{,}44$.

| $f$ | 0,0 | 0,2 | 0,44 | 0,5 | 1,0 |
| --- | --- | --- | --- | --- | --- |
| QBER | 0,000 | 0,050 | 0,110 | 0,125 | 0,250 |

**Odpowiedź:** $\mathbf{\mathrm{QBER}=0{,}25f}$; protokół **przerywamy** dla
$\mathbf{f>0{,}44}$ (QBER $>11\%$).

## 5. Typowe pułapki (w kodzie i pomiarach)

1. **Zła kolejność kubitów.** Konwencja małoendianowa: bramka na kubicie 0 to $I\otimes G$, a na
   kubicie 1 — $G\otimes I$; pomylenie daje pozornie „działający” obwód o błędnym wyniku.
2. **Eksplozja pamięci.** Symulator stanu trzyma $2^n$ amplitud (tablica gęstości $4^n$); powyżej
   $n\approx12$ (stan) i $n\approx7$ (macierz gęstości) trzeba zmienić metodę.
3. **Brak normalizacji po pomiarze.** Po rzucie stan trzeba podzielić przez $\sqrt{P(m)}$.
4. **Mylenie rzutu z wartością oczekiwaną.** Jednorazowy wynik $\ne\langle A\rangle$; trzeba
   powtórzyć eksperyment (rozdział 06).
5. **Zamiana kontroli i celu w CNOT.** Rezultat jest inny; testuj na $HZH=X$ i na parze Bella.
6. **Brak ziarna.** Symulacja statystyczna bez `default_rng(seed)` jest niereprodukowalna.
7. **Mylenie stanu z rozkładem.** $\lvert+\rangle$ i $\tfrac12I$ dają ten sam rozkład w bazie $Z$,
   a różnią się w bazie $X$ — testuj w dwóch bazach.
8. **Faza globalna vs względna.** Globalna nie ma znaczenia, względna decyduje o interferencji —
   nie „porównuj wektorów” bezpośrednio, używaj wierności $\lvert\langle\phi\vert\psi\rangle\rvert^2$.
9. **Wykres bez niepewności.** Krzywa bez słupków błędu (lub bez liczby pomiarów) nie jest wynikiem.
10. **Za mało pomiarów.** Dla $P=0{,}25$ i 100 rzutów błąd zliczania to $\approx0{,}043$ — raportuj $N$.

## 6. Zadania (Z-20)

**Z-20.1. Własny symulator stanu $n$ kubitów.**
(a) **Cel i wymagania:** funkcje `apply_1q(state, gate, qubit)`, `apply_2q(state, gate, q1, q2)`,
`measure(state, shots, seed)`; poprawna kolejność kubitów.
(b) **Plan:** (1) `kron` dla 1 kubita; (2) CNOT przez macierz $4\times4$ wbudowaną w $2^n$;
(3) pomiar przez rozkład $|c_k|^2$; (4) testy na $HZH=X$ oraz $\mathrm{CNOT}\,(H\otimes I)\lvert00\rangle=\lvert\Phi^+\rangle$.
(c) **Ocena i wariant:** 4 pkt za zgodność z teorią, 3 pkt za czytelność/aseracje, 3 pkt za raport;
**wariant trudniejszy:** symulator macierzy gęstości z kanałem depolaryzującym ($n=3$). **Czas: 8–12 h.**

**Z-20.2. Teleportacja kwantowa.**
(a) **Cel i wymagania:** przygotować $\lvert\psi\rangle$ i $\lvert\Phi^+\rangle$, wykonać pomiar
Bella, zastosować korektę; zweryfikować **wszystkie 4** wyniki.
(b) **Plan:** (1) stan 3 kubitów; (2) pomiar w bazie Bella przez rzuty na $\lvert\Phi^\pm\rangle,\lvert\Psi^\pm\rangle$;
(3) tabela $P$ i korekt; (4) wierność $\lvert\langle\psi\vert\psi_{\rm out}\rangle\rvert^2=1$.
(c) **Ocena i wariant:** 4 pkt za 4/4 przypadki, 3 pkt za kontrolę „bez korekty psuje”, 3 pkt raport;
**wariant trudniejszy:** dodać szum (kanał depolaryzujący na parę) i policzyć wierność $<1$. **Czas: 6–9 h.**

**Z-20.3. Grover dla $N=4$ i $N=8$.**
(a) **Cel i wymagania:** tabela i wykres $P_{\rm sukces}(k)$ vs $k$; znaleźć $k_{\rm opt}$ i porównać
z klasycznym $\sim N/2$.
(b) **Plan:** (1) wyrocznia i dyfuzja wektorowo; (2) skan $k=0\dots k_{\rm opt}+1$; (3) porównanie
z $\sin^2((2k+1)\theta)$; (4) histogramy z 2000 pomiarów.
(c) **Ocena i wariant:** 4 pkt za zgodność analityczno-numeryczną, 3 pkt za wykres, 3 pkt raport;
**wariant trudniejszy:** 2 rozwiązania (amplifikacja do $1/2$ amplitudy) lub $N=16$. **Czas: 6–8 h.**

*Interpretacja:* już 44% podsłuchanych fotonów wystarcza do wykrycia Eve — to empiryczny dowód
bezpieczeństwa BB84 (rozdział 10) i punkt kontrolny projektu Z-20.4.


**Z-20.4. BB84 z podsłuchem intercept–resend.**
(a) **Cel i wymagania:** symulacja 1000 bitów, losowe bazy (seed), QBER jako funkcja odsetka
podsłuchiwanych bitów $f\in\{0,0{,}1,\dots,1\}$.
(b) **Plan:** (1) generacja bitów i baz; (2) kanał + podsłuch na losowym podzbiorze; (3) sifting;
(4) QBER vs $f$ na wykresie + próg $f^\star\approx0{,}44$.
(c) **Ocena i wariant:** 4 pkt za $\mathrm{QBER}=0{,}25f$, 3 pkt za próg i decyzję, 3 pkt raport;
**wariant trudniejszy:** dodać szum detektora i porównać z progiem $11\%$. **Czas: 6–9 h.**

**Z-20.5. Estymacja fazy: klasycznie kontra GHZ.**
(a) **Cel i wymagania:** dla $N$ fotonów porównać niepewność $\Delta\varphi$: klasycznie $\propto1/\sqrt N$,
z GHZ $\propto1/N$ (granica Heisenberga); tabela dla kilku $N$.
(b) **Plan:** (1) model pomiaru i propagacja niepewności; (2) symulacja Monte Carlo dla obu strategii;
(3) tabela $\Delta\varphi(N)$ i zysk $\sqrt N$; (4) komentarz o dekoherencji.
(c) **Ocena i wariant:** 4 pkt za poprawny wykładnik skalowania, 3 pkt za tabelę i wykres, 3 pkt raport;
**wariant trudniejszy:** dodać widzialność $V<1$ i pokazać $\Delta\varphi\approx1/(VN)$. **Czas: 8–12 h.**

**Z-20.6. Analiza danych z pliku CSV.**
(a) **Cel i wymagania:** dopasować model do danych (do wyboru: zliczenia fotonów lub zanik $T_2$),
podać $\chi^2_{\rm red}$, niepewności i wykres z resztami.
(b) **Plan:** (1) wczytaj dane kolumnami; (2) wybierz model i metodę (`polyfit`/LSM/Monte Carlo);
(3) policz niepewności parametrów i propagację; (4) raport + zapis wykresu do PNG.
(c) **Ocena i wariant:** 4 pkt za poprawny wynik z niepewnością, 3 pkt za $\chi^2_{\rm red}$ i reszty,
3 pkt raport; **wariant trudniejszy:** wykryj punkt odstający i uzasadnij jego los. **Czas: 6–10 h.**

## 7. Wskazówki do zadań (projektów)

- **Z-20.1.** Zacznij od pojedynczej bramki i CNOT, potem skalowanie `kron`; testuj każdą funkcję
  osobno asercjami (np. $HZH=X$, $(H\otimes I)\lvert00\rangle$).
- **Z-20.2.** Rozłóż pomiar Bella na rzuty na cztery stany; zamiast „sprawdzać wektor”, licz
  wierność $\lvert\langle\psi_{\rm out}\vert\psi\rangle\rvert^2$ (odporna na fazę globalną).
- **Z-20.3.** Trzymaj $P$ analitycznie obok symulacji w tej samej tabeli; to natychmiast wykrywa błąd
  w wyroczni lub dyfuzji.
- **Z-20.4.** Nie porównuj bitów przed siftingiem; QBER licz tylko na bitach o zgodnych bazach.
- **Z-20.5.** Ustal, czy budżet to $N$ fotonów w jednym pomiarze, czy $\nu$ powtórzeń po $N$;
  inaczej porównasz $1/\sqrt{\nu N}$ z $1/N$.
- **Z-20.6.** Zawsze raportuj $\chi^2_{\rm red}$ **razem** z wynikiem; sam wykres nie wystarcza.

## 8. Co dalej

- Wróć do [rozdziału 16](16-analiza-danych-i-obliczenia-naukowe.md) i [19](19-ponad-program-algorytmy-zaawansowane-i-granice.md),
  jeśli któryś projekt sprawił trudność.
- Skrypty wzorcowe: [`kod/simulator.py`](../kod/simulator.py), [`kod/teleportacja.py`](../kod/teleportacja.py),
  [`kod/grover.py`](../kod/grover.py), [`kod/bb84.py`](../kod/bb84.py), [`kod/metrologia_faza.py`](../kod/metrologia_faza.py),
  [`kod/analiza_danych.py`](../kod/analiza_danych.py).
- Wskazówki realizacji i punkty kontrolne: [zadania/rozwiazania/rozwiazania-20.md](../zadania/rozwiazania/rozwiazania-20.md).
- Praca domowa: [PD-4](../praca-domowa/praca-domowa-04.md).

