# Rozwiązania do rozdziału 08

## Z-08.1

(a) Obwód: $\lvert0\rangle\lvert1\rangle\xrightarrow{H\otimes H}\lvert+\rangle\lvert-\rangle \xrightarrow{U_f}\xrightarrow{H\otimes I}\text{pomiar }q_1$. Kubit docelowy przygotowany w $\lvert-\rangle$
pozwala „odbić” fazę: $U_f\lvert x\rangle\lvert-\rangle=(-1)^{f(x)}\lvert x\rangle\lvert-\rangle$
(kick-back), więc informacja o $f$ wraca na rejestr danych.

(b) Dla $f(0)=f(1)=1$: $\frac{1}{\sqrt2}\big((-1)^1\lvert0\rangle+(-1)^1\lvert1\rangle\big)\lvert-\rangle =-\lvert+\rangle\lvert-\rangle$. Po $H$: $-\lvert0\rangle\lvert-\rangle$, więc pomiar daje **$0$** —
funkcja **stała**.

(c) Klasycznie: trzeba poznać $f(0)$ **i** $f(1)$ (dwa zapytania), bo jedno zapytanie nie odróżnia
stałej od zbalansowanej. W najgorszym razie $2$.

**Odpowiedź:** (a) jak wyżej; (b) pomiar $q_1=0$ (stała); (c) $2$ zapytania.

*Fizycznie:* jedno zapytanie kwantowe przetwarza „obie wartości” przez fazę, dając odpowiedź globalną.

## Z-08.2

(a) Amplituda stanu $\lvert0\rangle^{\otimes n}$ po obwodzie to $\frac1N\sum_x(-1)^{f(x)}$.
Dla $f$ stałej znak jest wspólny, suma $=\pm N/N=\pm1$. Dla $f$ zbalansowanej mamy $2^{n-1}$ znaków $+$
i $2^{n-1}$ znaków $-$, więc suma $=0$.

(b) $f(x)=x_1\oplus x_2$ przyjmuje $0$ dla $4$ wejść i $1$ dla $4$ — funkcja **zbalansowana**.
Z (a) wynika $P(0\ldots0)=0$: pomiar nigdy nie da $\lvert000\rangle$ (wynik jest pewnym niezerowym ciągiem).

(c) Klasycznie w najgorszym razie $2^{n-1}+1=2^{2}+1=5$ zapytań (dla $n=3$).

**Odpowiedź:** (a) $1$ (stała) lub $0$ (zbalansowana); (b) zbalansowana, $P(000)=0$; (c) $5$.

*Fizycznie:* jedno zapytanie rozstrzyga problem, który klasycznie wymaga wykładniczo wielu — źródło
wykładniczego przyspieszenia.

## Z-08.3

(a)

$$
\mathrm{QFT}_2=\frac12\begin{pmatrix}1&1&1&1\\1&i&-1&-i\\1&-1&1&-1\\1&-i&-1&i\end{pmatrix}.
$$

Unitarność: kolumny są ortogonalne i mają normę $1$ ($\lVert M^\dagger M-I\rVert<10^{-16}$).

(b) Dla $j=1$: $\mathrm{QFT}_2\lvert1\rangle=\frac12(1,i,-1,-i)^{\mathsf T}$. Prawdopodobieństwa to
moduły kwadratów współczynników: $P=\frac14$ dla każdego z czterech stanów bazowych.

(c) $CS=\mathrm{diag}(1,1,1,i)$; rachunek macierzowy
$\mathrm{SWAP}\cdot(I\otimes H)\cdot CS\cdot(H\otimes I)$ daje dokładnie $\mathrm{QFT}_2$
(zgodność do $10^{-16}$).

**Odpowiedź:** (a) jak wyżej, macierz unitarna; (b) $\frac12(1,i,-1,-i)^{\mathsf T}$, każdy wynik $P=\frac14$;
(c) rozkład zachodzi.

*Fizycznie:* QFT to jednostkowa zmiana bazy — dla $n=1$ to Hadamard, ogólnie obwód z kontrolowanych faz
i SWAP.

## Z-08.4

(a) $\sin\theta=1/\sqrt8\Rightarrow\theta=\arcsin(1/\sqrt8)\approx0{,}3614$ rad.

$$
k_{\text{opt}}\approx\frac{\pi}{4\theta}-\frac12=\frac{\pi}{1{,}4455}-0{,}5\approx2{,}174-0{,}5=1{,}67\ \Rightarrow\ k=2.
$$

(b) $P=\sin^2\big((2k+1)\theta\big)$:
$k=1$: $P=\sin^2(3\theta)\approx0{,}78125$; $k=2$: $P=\sin^2(5\theta)\approx0{,}9453$.

(c) Dla $k=3$: $P=\sin^2(7\theta)\approx0{,}3301$ — **mniej** niż dla $k=2$. Nadmiar iteracji obraca
stan poza rozwiązanie.

**Odpowiedź:** (a) $\theta\approx0{,}3614$, $k_{\text{opt}}\approx1{,}67\to2$; (b) $0{,}781$ i $0{,}945$;
(c) dla $k=3$ $P\approx0{,}330$ — sukces maleje.

*Fizycznie:* Grover to obrót o kąt $2\theta$ w płaszczyźnie; trzeba zatrzymać się w pobliżu bieguna
(rozwiązania), inaczej „przestrzeliwujemy”.

## Z-08.5

(a) Obwód: $t$ kubitów ancilla w $\lvert0\rangle$, rejestr w $\lvert u\rangle$; $H^{\otimes t}$ na ancillach;
$t$ bramek kontrolowanych-$U^{2^k}$ (kontrola ancilla $k$); odwrotna QFT na ancillach; pomiar ancilli.

(b) Odwrotna QFT zamienia **fazę** zakodowaną w ancillach ($\varphi$) na **położenie bitu** ($2^t\varphi$),
tak by pomiar w bazie obliczeniowej odczytał $\varphi$ Z dokładnością $t$ bitów.

(c) W Shorze bierzemy $U\lvert y\rangle=\lvert ay\bmod N\rangle$, którego wartości własne mają fazy $s/r$.
Estymacja fazy daje przybliżenie $s/r$, a ułamki łańcuchowe odtwarzają rząd $r$; z $r$ wyznaczamy
czynnik $N$ przez $\gcd(a^{r/2}\pm1,N)$.

**Odpowiedź:** (a) jak wyżej; (b) zamiana fazy na pozycję bitu; (c) $r$ z faz $s/r$, potem $\gcd$.

*Fizycznie:* estymacja fazy to „serce” Shora i wielu algorytmów; pokazuje moc QFT wobec funkcji okresowych.

## Z-08.6

(a) Grover to sekwencja obrotów o stały kąt $2\theta\approx2/\sqrt N$; do obrotu o $\pi/2$ potrzeba
$k\sim\frac{\pi}{4}\sqrt N$ kroków. Złożoność $\sqrt N$ (a nie $N$) to **tylko** przyspieszenie
kwadratowe — dolna granica $\Omega(\sqrt N)$ jest udowodniona.

(b) $N=10^6$: klasycznie $\sim N/2=5\times10^5$ zapytań; kwantowo
$k_{\text{opt}}\approx\frac\pi4\sqrt{10^6}=\frac\pi4\cdot1000\approx785$ iteracji.

(c) Nie da się w $O(1)$: rozróżnienie $N$ możliwości wymaga wyciągnięcia $\Theta(N)$ informacji
z wyroczni, a każda iteracja wnosi ograniczoną ilość „amplitudy rozwiązania”; formalnie dowodzi się
dolnego ograniczenia $\Omega(\sqrt N)$ zapytań.

**Odpowiedź:** (a) $\sqrt N$, nie $N$; (b) klasycznie $\approx5\times10^5$, kwantowo $\approx785$;
(c) dolna granica $\Omega(\sqrt N)$.

*Fizycznie:* przyspieszenie Grovera jest realne, ale „tylko” kwadratowe — dlatego przy dużych $N$
klasyczne algorytmy szybsze (np. Shora) mają większe znaczenie.
