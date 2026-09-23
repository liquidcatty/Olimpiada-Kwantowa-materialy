# Rozwiązania do rozdziału 15

## Z-15.1

(a) Obwód Bella i rozkład prawdopodobieństw:
```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
qc = QuantumCircuit(2)
qc.h(0); qc.cx(0, 1)                        # |00> -> (|00>+|11>)/sqrt(2)
sv = Statevector.from_instruction(qc)
print(sv.probabilities_dict())              # {'00': 0.5, '11': 0.5}
```

(b) Ręcznie: $\lvert\Phi^+\rangle=\frac{1}{\sqrt2}(\lvert00\rangle+\lvert11\rangle)$, więc
$$p_{00}=p_{11}=\tfrac12,\quad p_{01}=p_{10}=0 .$$
Wartości oczekiwane (każdy składnik superpozycji jest stanem własnym $ZZ$ i $XX$ z wartością $+1$):
$$\langle ZZ\rangle=\tfrac12(+1)+\tfrac12(+1)=1,\qquad \langle XX\rangle=1,\qquad
\langle Z\otimes I\rangle=\tfrac12(+1)+\tfrac12(-1)=0 .$$
Symulator: `sv.expectation_value("ZZ")` $=1{,}0$, `("XX")` $=1{,}0$, `("ZI")` $=0{,}0$ — zgodność
do $10^{-15}$.

(c) Dla $p=\frac12$ błąd statystyczny częstości wynosi $\Delta p=\sqrt{p(1-p)/n}=\frac{1}{2\sqrt n}$.
Warunek $\Delta p\le0{,}01$:
$$\frac{1}{2\sqrt n}\le10^{-2}\ \Rightarrow\ \sqrt n\ge50\ \Rightarrow\ n\ge2500 .$$

**Odpowiedź:** (a) `{'00': 0.5, '11': 0.5}`; (b) $\langle ZZ\rangle=\langle XX\rangle=\mathbf{1}$,
$\langle Z\otimes I\rangle=\mathbf{0}$; (c) $n\ge\mathbf{2500}$ shotów.

*Interpretacja:* dla stanu Bella wartości oczekiwane są maksymalnie skorelowane ($\langle ZZ\rangle
=\langle XX\rangle=1$), ale pojedyncze pomiary w $Z$ nie dają żadnej informacji ($\langle Z\otimes
I\rangle=0$) — to ta sama własność, którą wykorzystuje BB84 (rozdział 10).

## Z-15.2

(a) Ten sam obwód w dwóch standardach:
```
OPENQASM 2.0;                    OPENQASM 3.0;
include "qelib1.inc";            include "stdgates.inc";
qreg q[2];                       qubit[2] q;  bit[2] c;
creg c[2];                       h q[0];
h q[0];                          cx q[0], q[1];
cx q[0],q[1];                    c = measure q;
measure q -> c;
```

(b) W QASM 2 pomiar jest **operatorem kierującym** rejestr kwantowy do klasycznego:
`measure q -> c;`. W QASM 3 pomiar jest **wyrażeniem** zwracającym wartość, którą przypisuje się
do bitu, i można go używać w dalszych wyrażeniach/sterowaniu: `c = measure q;` (albo pojedynczo
`c[0] = measure q[0];`). Ta różnica pozwala w QASM 3 pisać `if (c == 3) { ... }` — czyli
klasyczne sprzężenie zwrotne w jednym programie.

(c) Różne narzędzia przyjmują różne konwencje indeksowania. **Test praktyczny:** obwód
`x q[0]` (albo `qc.x(0)`), pomiar wszystkich kubitów i odczyt liczników. W konwencji Qiskit
(i tego repozytorium) `q0` jest **najmłodszym** bitem, więc dla 2 kubitów wynik to `'01'`
(bity zapisywane od najstarszego: $q_1q_0$). Jeśli w innym SDK wynik brzmi `'10'`, to używa
odwrotnej konwencji — i wtedy **wszystkie** Twoje rachunki trzeba przeliczyć.

**Odpowiedź:** (a) jak wyżej; (b) QASM 2 ma `measure q -> c`, QASM 3 ma przypisanie
`c = measure q` (pomiar jako wyrażenie); (c) test `x q[0]` + odczyt liczników.

*Interpretacja:* format zapisu jest nieistotny tak długo, jak długo ustalimy konwencję bitów —
wymiana obwodów między SDK to najczęstsze źródło „niezgodnych” wyników.

## Z-15.3

(a) Na linii $q_0-q_1-q_2-q_3-q_4$ odległość między $q_0$ i $q_4$ wynosi $4$, więc transpilator
wstawia $4$ SWAP-y, a każdy SWAP to $3$ CNOT:
$$4\cdot3=12\ \text{CNOT}\ \text{zamiast}\ 1 .$$

(b) Wierność takiej bramki: $0{,}997^{12}=0{,}965$ (spadek o $3{,}5$ punktu procentowego).

(c) `optimization_level=0` tylko odwzorowuje obwód na sprzęt (rozkład na bramki natywne i layout),
a `=3` dodatkowo skleja obroty i kasuje pary odwrotnych bramek. W `count_ops()` zobaczysz zwykle
mniej bramek jednokubitowych, a czasem także mniej CNOT-ów po zmianie layoutu. Ma to znaczenie,
bo **każda dodatkowa bramka dwukubitowa to mnożnik wierności** $F^n$ (rozdział 12), więc
porównanie dwóch obwodów jest uczciwe tylko przy tych samych parametrach transpilacji
(`optimization_level` i `seed_transpiler`).

**Odpowiedź:** (a) $\mathbf{12}$ CNOT; (b) $F=\mathbf{0{,}965}$; (c) poziom 3 zmniejsza liczbę
bramek (głównie 1-kubitowych), więc podnosi $F^n$; porównuj przy tym samym poziomie i ziarnie.

*Interpretacja:* koszt łączności jest bezpośrednim kosztem wierności — dlatego obwody pisze się
pod topologię sprzętu, a nie „na abstrakcyjnym grafie”.

## Z-15.4

(a) Trzy typy symulatorów i granice praktyczne:
1. **statevector** — dokładny wektor $2^n$ amplitud; $\approx30$ kubitów (pamięć),
2. **macierz gęstości** — macierz $4^n$ elementów, modeluje szum i stany mieszane; $\approx15$ kubitów,
3. **sieci tensorowe** — stan jako graf; świetny dla obwodów o małym splątaniu (1D, płytkie),
słaby dla losowych obwodów o dużej głębokości (rośnie rząd tensora).

(b) Wektor stanu ma $2^n$ amplitud, a macierz gęstości $4^n$ elementów — czyli $2^n$ razy więcej.
Każdy dodatkowy kubit podwaja rozmiar wektora, ale **czterokrotnie** rozmiar macierzy gęstości,
dlatego macierz gęstości „kończy się” o połowę kubitów wcześniej ($30$ vs $15$).

(c) Sieci tensorowe **wygrywają**, gdy splątanie jest ograniczone (np. obwody 1D o małej głębokości,
stany iloczynowe, ewolucje lokalne) — wtedy koszt jest wielomianowy. **Przegrywają** dla obwodów
o pełnym splątaniu (losowe obwody na $50$+ kubitach), gdzie reprezentacja tensorowa staje się
tak samo droga jak wektor stanu.

**Odpowiedź:** (a) jak wyżej; (b) bo $4^n$ rośnie szybciej niż $2^n$; (c) wygrywają przy małym
splątaniu, przegrywają przy dużym.

*Interpretacja:* wybór symulatora to kompromis między dokładnością opisu szumu a rozmiarem
układu — dla mitygacji (rozdział 13) potrzebujesz macierzy gęstości lub modelu szumu.

## Z-15.5

(a) Kolejność kroków od obwodu do histogramu:
1. **obwód logiczny** (`QuantumCircuit`) — weryfikacja na symulatorze statevector,
2. **transpilacja** na konkretny backend (`transpile(qc, backend=..., optimization_level=3)`),
3. **wysłanie zadania** (`SamplerV2.run([isa], shots=n)`) z liczbą shotów i opcjonalną mitygacją,
4. **oczekiwanie w kolejce** (identyfikator zadania `job_id`),
5. **pobranie wyników** — liczniki i histogram,
6. **analiza** — zamiana liczników na prawdopodobieństwa, niepewności, porównanie z symulatorem.

(b) Pięć elementów raportu (bez nich wynik nie jest powtarzalny ani weryfikowalny): nazwa
urządzenia (backend), liczba shotów, identyfikator zadania, data i godzina uruchomienia oraz
informacja o transpilacji i mitygacji (`optimization_level`, użyte metody).

(c) Ten sam obwód wysłany dwa razy daje inne liczniki z trzech powodów: (i) **statystyka** —
liczniki są losowe, rozrzut rzędu $1/\sqrt n$; (ii) **kalibracja** — parametry urządzenia dryfują
w czasie (rozdział 12, sekcja 3.9), więc szum jest inny; (iii) **transpilacja** — przy tej samej
wartości `seed_transpiler` layout i bramki są zwykle takie same, ale bez ziarna mogą się różnić,
a kalibracja i tak zmienia mapowanie na sprzęt.

**Odpowiedź:** (a) obwód → transpilacja → zlecenie → kolejka → wyniki → analiza; (b) backend,
shots, `job_id`, data, transpilacja/mitygacja; (c) statystyka + dryf kalibracji (+ ewentualna
zmiana transpilacji).

*Interpretacja:* raport z urządzenia kwantowego jest **eksperymentem pomiarowym**, a nie
obliczeniem: musi zawierać warunki, w których został wykonany (rozdział 14, sekcja 3.10).

## Z-15.6

(a) **Zasada wariacyjna:** dla **dowolnego** stanu $\langle\psi(\vec\theta)\rvert H\lvert\psi(\vec\theta)\rangle\ge E_0$,
więc minimalizacja energii po parametrach obwodu daje z góry ograniczenie (a przy dobrym ansatzu —
dokładnie energię stanu podstawowego). **Ansatz** to rodzina stanów osiągalna przez obwód;
od niego zależy, czy stan podstawowy w ogóle da się wyrazić („wyrażalność”) i czy optymalizacja
jest wykonalna („trywializowalność” i koszt).

(b) Dla $H=X_0X_1+Z_0Z_1$: wektory własne to stany Bella, a wartości własne wynoszą
$\{2,0,0,-2\}$ — stan podstawowy to $\frac{1}{\sqrt2}(\lvert01\rangle-\lvert10\rangle)$ z $E_0=-2$.
Ansatz `ry,ry,cx` daje tylko kombinacje bez amplitudy na $\lvert10\rangle$
($\lvert\psi\rangle=a\lvert00\rangle+b\lvert01\rangle+d\lvert11\rangle$), a w tej podprzestrzeni
$H$ obcięte do macierzy $\begin{pmatrix}1&0&1\\0&-1&0\\1&0&1\end{pmatrix}$ ma wartości własne
$-1$ i $2$ — więc minimalna energia to $-1$. Dopiero dodanie kolejnych obrotów `ry` **po** CNOT
(4 parametry) pozwala wytworzyć $\lvert10\rangle$ i osiągnąć $E=-2{,}0000$.

(c) Gdy ansatz jest zbyt głęboki (dużo parametrów, losowo zainicjowanych), gradient funkcji
kosztu zanika wykładniczo z liczbą kubitów — zjawisko **barren plateaus**. Optymalizator
„nie widzi” kierunku poprawy, a koszt pomiarów rośnie. Praktyczne środki: ansatze o strukturze
fizycznej (np. UCC dla chemii), inicjalizacja „rozgrzewająca”, lokalne koszty, optymalizatory
warstwowe.

**Odpowiedź:** (a) $\langle H\rangle\ge E_0$, ansatz decyduje o wyrażalności; (b) $E_0=\mathbf{-2}$
dla stanu $\frac{1}{\sqrt2}(\lvert01\rangle-\lvert10\rangle)$; ansatz 2-parametrowy daje tylko
$\mathbf{-1}$; (c) barren plateaus — gradienty znikają wykładniczo.

*Interpretacja:* VQE to kompromis między sprzętem (płytki obwód, mało szumu) a klasycznym
optymalizatorem; wybór ansatzu jest *najważniejszą* decyzją projektową, bo błąd wyrażalności
nie da się naprawić optymalizacją. Więcej: [rozdział 19](../../teoria/19-ponad-program-algorytmy-zaawansowane-i-granice.md).

> **Weryfikacja numeryczna.** $p_{00}=p_{11}=0{,}5$, $\langle ZZ\rangle=\langle XX\rangle=1$,
> $\langle Z\otimes I\rangle=0$; $n\ge2500$ dla $\Delta p\le0{,}01$; $0{,}997^{12}=0{,}9646$;
> widmo $H=X_0X_1+Z_0Z_1$: $\{-2,0,0,2\}$, a dla ansatzu 2-parametrowego w podprzestrzeni
> $\mathrm{span}\{\lvert00\rangle,\lvert01\rangle,\lvert11\rangle\}$: $\{-1,2\}$ (VQE daje
> dokładnie $-2{,}000000$ przy 4 parametrach). Skrypty: `kod/simulator.py`, `kod/p4_cnot_ry.py`.

