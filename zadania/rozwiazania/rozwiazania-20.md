# Rozwiązania do rozdziału 20 (wskazówki do projektów)

Rozdział 20 zawiera **mini-projekty**, a nie zadania rachunkowe — dlatego zamiast gotowych
rozwiązań podajemy dla każdego projektu: **wskazówki realizacji**, **punkty kontrolne** (z liczbami,
które powinny wyjść) i **kryteria oceny**. To odpowiednik „rozwiązań” dla pracy projektowej.

## Z-20.1. Własny symulator stanu $n$ kubitów

**(a) Wskazówki realizacji.** Bramkę 1-kubitową na kubicie $k$ buduj jako
`np.kron` złożony tak, by $G$ stał na pozycji $k$-tej **od prawej** (kubit 0 = najmłodszy bit).
CNOT dla kontroli $q_1$ i celu $q_0$ ma postać $4\times4$
$\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}$; ogólnie użyj
$\lvert0\rangle\langle0\rvert\otimes I+\lvert1\rangle\langle1\rvert\otimes X$. Pomiar: policz
$p=|\psi|^2$, potem `rng.choice(2**n, size=shots, p=p)`.

**(b) Punkty kontrolne.**
- $HZH=X$ (dokładnie, do $10^{-15}$).
- $\mathrm{CNOT}\,(H\otimes I)\lvert00\rangle=(0{,}7071;0;0;0{,}7071)=\lvert\Phi^+\rangle$.
- Statystyka pomiaru $\lvert\Phi^+\rangle$ w bazie $Z$: $P(00)=P(11)=0{,}5$, $P(01)=P(10)=0$.
- Dla 10 000 rzutów odsetki mieszczą się w $0{,}5\pm0{,}01$.

**(c) Kryteria oceny (10 pkt).** Poprawna kolejność kubitów i wyniki testów — 4 pkt; kod z asercjami
`OK/FAIL` i docstringiem — 3 pkt; raport (cel, metoda, wykres rozkładu, wniosek) — 3 pkt.

## Z-20.2. Teleportacja kwantowa

**(a) Wskazówki realizacji.** Ustaw stan $\lvert q_2q_1q_0\rangle$: $q_2$ = teleportowany,
$q_1$ = kubit Alicji z pary, $q_0$ = kubit Boba. Pomiar Bella to cztery rzuty na
$\lvert\Phi^\pm\rangle,\lvert\Psi^\pm\rangle$ kubitów $q_2,q_1$; zamiast porównywać wektory, licz
**wierność** $\lvert\langle\psi_{\rm out}\vert\psi\rangle\rvert^2$ (odporna na fazę globalną). Wzorzec:
[`kod/teleportacja.py`](../../kod/teleportacja.py).

**(b) Punkty kontrolne.**
- Cztery wyniki: każdy z $P=0{,}25$; suma $=1$.
- Korekty $I,Z,X,ZX$ dają wierność $1$ dla każdego wyniku.
- Bez korekty tylko $1$ z $4$ wyników odtwarza stan (dla nietrywialnego $\lvert\psi\rangle$).
- Dla $\lvert\psi\rangle=(2\lvert0\rangle+i\lvert1\rangle)/\sqrt5$: stany Boba przed korektą
  $(0{,}8944;0{,}4472i)$, $(0{,}8944;-0{,}4472i)$, $(0{,}4472i;0{,}8944)$, $(-0{,}4472i;0{,}8944)$.

**(c) Kryteria oceny (10 pkt).** 4/4 przypadki poprawne — 4 pkt; test „bez korekty psuje” — 3 pkt;
raport z tabelą prawdopodobieństw — 3 pkt.

## Z-20.3. Grover dla $N=4$ i $N=8$

**(a) Wskazówki realizacji.** Wyrocznię realizuj przez `psi[marked] *= -1`, dyfuzję przez
`psi = 2*s*np.vdot(s, psi) - psi`. Trzymaj $P$ analityczne ($\sin^2((2k+1)\theta)$) **obok**
symulacji w jednej tabeli — rozbieżność natychmiast wskaże błąd. Wzorzec: [`kod/grover.py`](../../kod/grover.py).

**(b) Punkty kontrolne.**

| $k$ | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| $P$ ($N=4$) | 0,250 | 1,000 | 0,250 | 0,250 |
| $P$ ($N=8$) | 0,125 | 0,781 | 0,945 | 0,330 |

Zgodność analityczno-numeryczna do $10^{-12}$; $k_{\rm opt}(4)=1$, $k_{\rm opt}(8)=2$.

**(c) Kryteria oceny (10 pkt).** Zgodność tabeli — 4 pkt; wykres $P(k)$ z zaznaczonym $k_{\rm opt}$ —
3 pkt; raport (porównanie z $\sim N/2$) — 3 pkt.

## Z-20.4. BB84 z podsłuchem intercept–resend

**(a) Wskazówki realizacji.** Losuj bity i bazy Alicji (`rng.integers(0,2,N)`), potem bazy Boba.
Podsłuch: z prawdopodobieństwem $f$ Eve mierzy w losowej bazie i odsyła stan. Sifting: zostaw bity
o zgodnych bazach. QBER licz **tylko** na bitach po siftingu. Wzorzec: [`kod/bb84.py`](../../kod/bb84.py).

**(b) Punkty kontrolne.**

| $f$ | 0,0 | 0,2 | 0,44 | 0,5 | 1,0 |
| --- | --- | --- | --- | --- | --- |
| QBER | 0,000 | 0,050 | 0,110 | 0,125 | 0,250 |

Dopasowanie liniowe $y=0{,}25f$ (nachylenie $0{,}25$); próg $f^\star=0{,}44$ dla QBER $=11\%$
($H_2(0{,}11)=0{,}4999$).

**(c) Kryteria oceny (10 pkt).** Poprawne $\mathrm{QBER}=0{,}25f$ — 4 pkt; próg i decyzja o przerwaniu —
3 pkt; raport z wykresem QBER vs $f$ — 3 pkt.

## Z-20.5. Estymacja fazy: klasycznie kontra GHZ

**(a) Wskazówki realizacji.** Ustal budżet: $N$ fotonów w **jednym** pomiarze. Klasycznie
$\Delta\varphi=\tfrac{1}{\sqrt{\nu N}}$, ze stanem GHZ (granica Heisenberga) $\Delta\varphi=\tfrac{1}{\nu N}$;
symuluj pomiary i licz odchylenie standardowe estymatora. Widzialność $V$ wchodzi jak
$\Delta\varphi\approx\tfrac{1}{V\nu N}$.

**(b) Punkty kontrolne.**
- $N=100$: klasycznie $0{,}1$ (rel.), GHZ $0{,}01$ — zysk $\sqrt N=10$.
- Nachylenie $\log\Delta\varphi$ vs $\log N$: $-1/2$ (klasycznie), $-1$ (GHZ).
- Dla $V=0{,}9$: $\Delta\varphi$ rośnie o $11\%$; dla $V=0{,}5$ — dwukrotnie.

**(c) Kryteria oceny (10 pkt).** Poprawne wykładniki skalowania — 4 pkt; tabela + wykres $\Delta\varphi(N)$ —
3 pkt; raport z komentarzem o dekoherencji — 3 pkt.

## Z-20.6. Analiza danych z pliku CSV

**(a) Wskazówki realizacji.** Wczytaj `np.loadtxt(..., unpack=True)`. Dla zaniku $T_2$: start z
log-linearyzacji, potem minimalizacja $\chi^2$; niepewności z hesjanu lub bootstrap. Zawsze raportuj
$\chi^2_{\rm red}$ **razem** z wynikiem i wykresem reszt. Wzorzec: [`kod/analiza_danych.py`](../../kod/analiza_danych.py).

**(b) Punkty kontrolne** (dane symulowane, $A=0{,}98$, $T_2=2{,}5$ s, szum $0{,}02$, seed 11):
- $T_2=2{,}4528\pm0{,}0238$ s, $A=0{,}9901\pm0{,}0065$.
- $\chi^2/\mathrm{ndof}=44{,}76/58=0{,}772$.
- Bootstrap (68%): $T_2\in[2{,}427;\ 2{,}485]$ s.
- Wariant odstający: punkt $>3\sigma$ podnosi $\chi^2_{\rm red}$ powyżej 1.

**(c) Kryteria oceny (10 pkt).** Wynik z niepewnością — 4 pkt; $\chi^2_{\rm red}$ i reszty — 3 pkt;
raport zgodny z szablonem z 3.2 — 3 pkt.

## Uwaga o ocenianiu projektów

Suma punktów za 6 projektów to 60 pkt. Powyżej 80% zaleca się przejść do powtórki przed finałem
([plan nauki](../../docs/01-plan-nauki.md)); poniżej 60% — powtórzyć rozdziały wskazane przez prowadzącego
projekt (najczęściej 16 i 19). Pełne rozwiązania zadań rachunkowych z rozdziałów 16–19 są w plikach
`rozwiazania-16.md` … `rozwiazania-19.md`.
