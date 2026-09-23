# Rozwiązania do rozdziału 07

## Z-07.1

(a) **Twierdzenie.** Nie istnieje unitary $U$ i stan otoczenia $\lvert A\rangle$ takie, że
$U\lvert\psi\rangle\lvert0\rangle\lvert A\rangle=\lvert\psi\rangle\lvert\psi\rangle\lvert A_\psi\rangle$
dla wszystkich $\lvert\psi\rangle$.

(b) Gdyby $U$ klonował (pomijamy otoczenie), to $U\lvert0\rangle\lvert0\rangle=\lvert00\rangle$,
$U\lvert1\rangle\lvert0\rangle=\lvert11\rangle$, a z liniowości

$$U\lvert+\rangle\lvert0\rangle=\tfrac{1}{\sqrt2}(U\lvert00\rangle+U\lvert10\rangle)
=\tfrac{1}{\sqrt2}(\lvert00\rangle+\lvert11\rangle)=\lvert\Phi^+\rangle.$$

Klonowanie wymagałoby jednak $\lvert+\rangle\lvert+\rangle=\frac12(\lvert00\rangle+\lvert01\rangle+\lvert10\rangle+\lvert11\rangle)$
— to inny stan. Sprzeczność.

(c) $\lvert0\rangle$ i $\lvert1\rangle$ są **ortogonalne**, więc CNOT daje
$\mathrm{CNOT}\lvert0\rangle\lvert0\rangle=\lvert00\rangle$, $\mathrm{CNOT}\lvert1\rangle\lvert0\rangle=\lvert11\rangle$ —
to poprawne klonowanie stanów bazowych. Dla nieortogonalnego $\lvert+\rangle$ liniowość wymusza
$\lvert\Phi^+\rangle$, czego nie da się uzyskać z klonowania.

**Odpowiedź:** (a) sformułowanie jak wyżej; (b) sprzeczność $\lvert\Phi^+\rangle\ne\lvert+\rangle\lvert+\rangle$;
(c) klonowanie działa tylko dla ortogonalnych stanów bazowych.

*Fizycznie:* to fundament bezpieczeństwa QKD — Eve nie zrobi kopii „na zapas”, więc każdy jej pomiar
zaburza sygnał.

## Z-07.2

(a) Gdyby pomiar (POMV) rozróżniał $\lvert\psi\rangle,\lvert\phi\rangle$ z pewnością, istniałby
rzut $E_0$ z $\langle\psi\vert E_0\vert\psi\rangle=\langle\phi\vert E_0\vert\phi\rangle=1$, co wymusza
$E_0\lvert\psi\rangle=\lvert\psi\rangle$, $E_0\lvert\phi\rangle=\lvert\phi\rangle$; wtedy $\lvert\psi\rangle,\lvert\phi\rangle$
leżą w tej samej podprzestrzeni własnej i muszą być ortogonalne. Dla nieortogonalnych to sprzeczność.

(b) Granica Helstroma dla jednakowych prawdopodobieństw:

$$p_{\text{poprawne}}=\tfrac12\Big(1+\sqrt{1-\lvert\langle0\vert+\rangle\rvert^2}\Big)
=\tfrac12\Big(1+\sqrt{1-\tfrac12}\Big)=\tfrac12\Big(1+\tfrac{1}{\sqrt2}\Big)\approx0{,}8536.$$

(c) Eve nie odróżni $\lvert0\rangle$ od $\lvert+\rangle$ lepiej niż $85{,}4\%$ (i to w optymalnym
pomiarze) — czyli z istotnym błędem. Próba odczytu bitu przez Eve wprowadza więc błędy, które
ujawniają się jako wzrost QBER (>11% przerywa protokół).

**Odpowiedź:** (a) uzasadnienie jak wyżej; (b) $p_{\text{poprawne}}=\frac12(1+\frac{1}{\sqrt2})\approx0{,}854$;
(c) niedoskonała rozróżnialność $\Rightarrow$ wykrywalny QBER.

*Fizycznie:* nieortogonalność stanów to drugi — obok no-cloning — filar bezpieczeństwa QKD.

## Z-07.3

(a) $\lvert+\rangle$ to stan czysty, więc $S(\lvert+\rangle\langle+\rvert)=0$. Dla $\rho=\frac12 I$
wartości własne $\frac12,\frac12$, więc $S=-\big(\frac12\log_2\frac12+\frac12\log_2\frac12\big)=1$ bit.

(b) $H(0{,}5)=-0{,}5\log_2 0{,}5-0{,}5\log_2 0{,}5=1$ bit.
$H(0{,}1)=-0{,}1\log_2 0{,}1-0{,}9\log_2 0{,}9\approx0{,}469$ bit. Rozkład bardziej „pewny” ($p=0{,}1$)
ma niższą entropię.

(c) $\rho=\mathrm{diag}(0{,}5,0{,}5)=\frac12 I$; pomiar w bazie $X$ daje $P(+)=P(-)=\frac12$,
więc $H=1$ bit $=S(\rho)$. Równość zachodzi, bo $\rho$ jest maksymalnie mieszany (każdy pomiar „pełny”).

**Odpowiedź:** (a) $S=0$ i $S=1$ bit; (b) $1$ bit i $\approx0{,}469$ bit; (c) $H=1=S(\rho)$.

*Fizycznie:* entropia mierzy niepewność; pomiar nie może jej zwiększyć ponad $S(\rho)$, a w bazie
własnej osiąga równość.

## Z-07.4

(a) $\rho=\lvert0\rangle\langle0\rvert$, $\sigma=\lvert+\rangle\langle+\rvert$; wartości własne
$\rho-\sigma$ to $\pm\frac{1}{\sqrt2}$, więc $D=\frac12\big(\frac{1}{\sqrt2}+\frac{1}{\sqrt2}\big)=\frac{1}{\sqrt2}\approx0{,}7071$.

(b) Dla stanów czystych $F=\lvert\langle0\vert+\rangle\rvert^2=\frac12$.

(c) Fuchsa–van de Graaf: $1-\sqrt{F}\le D\le\sqrt{1-F}$ daje
$1-\frac{1}{\sqrt2}\approx0{,}2929\le0{,}7071\le\sqrt{\frac12}\approx0{,}7071$. Ograniczenia zachodzą,
a górne jest osiągnięte (pary stanów czystych).

**Odpowiedź:** (a) $D=\frac{1}{\sqrt2}\approx0{,}707$; (b) $F=\frac12$; (c) $0{,}293\le0{,}707\le0{,}707$ ✓.

*Fizycznie:* wierność i dystans śladowy opisują „bliskość” stanów różnymi metrykami; dla stanów czystych
są jednoznacznie powiązane.

## Z-07.5

(a) Zespół: $\frac12$ na $\lvert0\rangle$, $\frac12$ na $\lvert+\rangle$. Średni stan

$$\bar\rho=\tfrac12\lvert0\rangle\langle0\rvert+\tfrac12\lvert+\rangle\langle+\rvert
=\begin{pmatrix}3/4&1/4\\1/4&1/4\end{pmatrix}.$$

Wartości własne: $\frac12(1\pm\frac{1}{\sqrt2})\approx0{,}8536,\,0{,}1464$. Entropia

$$S(\bar\rho)\approx-0{,}8536\log_2 0{,}8536-0{,}1464\log_2 0{,}1464\approx0{,}601\ \text{bitu}.$$

Oba stany czyste $\Rightarrow S(\rho_i)=0$, więc $\chi=S(\bar\rho)\approx0{,}601$ bita.

(b) Supergęste kodowanie zużywa **dwa** nośniki (shared ebit + wysłany kubit), więc 2 bity nie łamią
granicy $n$ kubitów $\le n$ bitów; gdyby liczyć tylko wysłany kubit, $\chi\le1$.

(c) Warunki wstępne: (i) **współdzielone splątanie** $\lvert\Phi^+\rangle$, (ii) **kanał kwantowy**
pozwalający przesłać kubit Alicji do Boba.

**Odpowiedź:** (a) $\chi\approx0{,}601$ bita; (b) dwa nośniki; (c) splątanie + kanał kwantowy.

*Fizycznie:* Holevo ogranicza informację na kubit; supergęste kodowanie „pożycza” drugi nośnik ze
współdzielonego splątania.

## Z-07.6

(a) $\mathcal{E}(\lvert0\rangle\langle0\rvert)=(1-p)\lvert0\rangle\langle0\rvert+p\,\frac{I}{2} =\begin{pmatrix}1-p/2&0\\0&p/2\end{pmatrix}$.

(b) $\lvert0\rangle$ jest stanem własnym kanału, więc
$F\big(\mathcal{E}(\lvert0\rangle\langle0\rvert),\lvert0\rangle\langle0\rvert\big)=\langle0\vert\mathcal{E}(\lvert0\rangle\langle0\rvert)\vert0\rangle=1-\frac p2$.

(c) $1-\frac p2=\frac34\Rightarrow p=\frac12$. Połowa „masy” stanu została zastąpiona szumem.

**Odpowiedź:** (a) $\mathrm{diag}(1-p/2,\,p/2)$; (b) $F=1-p/2$; (c) $p=\frac12$.

*Fizycznie:* kanał depolaryzujący stopniowo „rozmywa” stan; wierność maleje liniowo od $1$ do $\frac12$
(dla $p=1$ stan jest maksymalnie mieszany).
