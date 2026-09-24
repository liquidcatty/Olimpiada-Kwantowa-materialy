# Rozwiązania do rozdziału 06

## Z-06.1

(a) Dla $\lvert+\rangle=\frac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)$:

$$
\langle X\rangle=\langle+\lvert X\lvert+\rangle=1,\quad
\langle Y\rangle=0,\quad \langle Z\rangle=0\ \Rightarrow\ \vec r=(1,0,0).
$$

Dla $\lvert-\rangle=\frac{1}{\sqrt2}(\lvert0\rangle-\lvert1\rangle)$ analogicznie
$\langle X\rangle=-1$, więc $\vec r=(-1,0,0)$ (przeciwległy biegun na osi $x$).

(b) Ze wzoru $R_n(\theta)=\cos\frac\theta2 I-i\sin\frac\theta2\,(n\cdot\vec\sigma)$ i dla $\theta=\pi$:

$$
R_X(\pi)=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}=-iX,\quad
R_Y(\pi)=\begin{pmatrix}0&-1\\1&0\end{pmatrix}=-iY,\quad
R_Z(\pi)=\mathrm{diag}(-i,i)=-iZ.
$$

(c) Ponieważ $X+Z=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, mamy $\frac{1}{\sqrt2}(X+Z)=H$. Oś obrotu
$\hat n=\frac{1}{\sqrt2}(1,0,1)$ daje $\hat n\cdot\vec\sigma=\frac{1}{\sqrt2}(X+Z)=H$, więc

$$
R_{\hat n}(\pi)=\cos\tfrac\pi2 I-i\sin\tfrac\pi2\,H=-iH\ \Rightarrow\ H=i\,R_{\hat n}(\pi).
$$

**Odpowiedź:** (a) $\vec r_{|+\rangle}=(1,0,0)$, $\vec r_{|-\rangle}=(-1,0,0)$;
(b) $R_X(\pi)=-iX$, $R_Y(\pi)=-iY$, $R_Z(\pi)=-iZ$; (c) $H=\frac1{\sqrt2}(X+Z)=iR_{\hat n}(\pi)$.

*Fizycznie:* Hadamard to obrót o $\pi$ wokół osi w płaszczyźnie $xz$ pod $45^\circ$ — dlatego zamienia
bieguny $Z$ na osie $X$.

## Z-06.2

(a) $S=\mathrm{diag}(1,i)$, $S^\dagger=\mathrm{diag}(1,-i)$:

$$
SXS^\dagger=\begin{pmatrix}1&0\\0&i\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}
\begin{pmatrix}1&0\\0&-i\end{pmatrix}
=\begin{pmatrix}0&1\\i&0\end{pmatrix}\begin{pmatrix}1&0\\0&-i\end{pmatrix}
=\begin{pmatrix}0&-i\\i&0\end{pmatrix}=Y.
$$

(b) $HS=\frac{1}{\sqrt2}\begin{pmatrix}1&i\\1&-i\end{pmatrix}$,
$SH=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\i&-i\end{pmatrix}$,

$$
[H,S]=HS-SH=\frac{1}{\sqrt2}\begin{pmatrix}0&i-1\\1-i&0\end{pmatrix}\ne0,
$$

więc **nie komutują**.

(c) $T=\mathrm{diag}(1,e^{i\pi/4})$; $TXT^\dagger=\begin{pmatrix}0&e^{-i\pi/4}\\e^{i\pi/4}&0\end{pmatrix} =\frac{1}{\sqrt2}(X+Y)$, co **nie jest** macierzą Pauliego (nie da się zapisać jako $e^{i\varphi}X$).

**Odpowiedź:** (a) $SXS^\dagger=Y$; (b) $[H,S]\ne0$ — nie komutują; (c) $TXT^\dagger=\frac{1}{\sqrt2}(X+Y)$.

*Fizycznie:* bramki Clifforda ($H,S$) przenoszą macierze Pauliego w macierze Pauliego; $T$ tego nie robi,
więc „wychodzi” poza grupę Clifforda i jest źródłem pełnej uniwersalności.

## Z-06.3

(a) $\lvert\Phi^+\rangle=\frac{1}{\sqrt2}(\lvert00\rangle+\lvert11\rangle)$. Amplituda składników z $q_0=0$
to $\frac{1}{\sqrt2}$ (stan $\lvert00\rangle$), więc $P(q_0=0)=\left|\frac{1}{\sqrt2}\right|^2=\frac12$.

(b) Po wyniku $q_0=0$ zostaje składnik $\lvert00\rangle$ o amplitudzie $\frac{1}{\sqrt2}$; po normalizacji
przez $\sqrt{1/2}$: $\lvert\psi'\rangle=\lvert00\rangle$.

(c) Symetrycznie $q_0=1\Rightarrow\lvert\psi'\rangle=\lvert11\rangle$; w obu przypadkach $q_1=q_0$, więc
pomiar jednego kubita **determinuje** drugi: $P(\text{zgodne})=1$.

**Odpowiedź:** (a) $P(q_0=0)=\frac12$; (b) stan po pomiarze $=\lvert00\rangle$; (c) $P(\text{zgodne})=1$.

*Fizycznie:* w stanie Bella pojedynczy pomiar daje losowy wynik, ale oba kubity zawsze się zgadzają —
to najprostsza manifestacja korelacji splątanych.

## Z-06.4

(a) W bazie $(\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle)$ z kontrolą $q_1$, celem $q_0$:

$$
\mathrm{CNOT}=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}.
$$

(b) Rachunek macierzowy daje

$$
(H\otimes H)\,\mathrm{CNOT}\,(H\otimes H)=\begin{pmatrix}1&0&0&0\\0&0&0&1\\0&0&1&0\\0&1&0&0\end{pmatrix},
$$

czyli **CNOT z zamienionymi rolami** (kontrola $q_0$, cel $q_1$).

(c) Rozbijamy $\mathrm{CNOT}=\lvert0\rangle\langle0\rvert\otimes I+\lvert1\rangle\langle1\rvert\otimes X$
i używamy $HXH=Z$:

$$
(I\otimes H)\,\mathrm{CZ}\,(I\otimes H)=\lvert0\rangle\langle0\rvert\otimes(HH)+\lvert1\rangle\langle1\rvert\otimes(HZH)
=\lvert0\rangle\langle0\rvert\otimes I+\lvert1\rangle\langle1\rvert\otimes X=\mathrm{CNOT}.
$$

**Odpowiedź:** (a) jak wyżej; (b) $(H\otimes H)\mathrm{CNOT}(H\otimes H)=\mathrm{CNOT}_{q_0\to q_1}$;
(c) $HXH=Z$ daje $\mathrm{CNOT}=(I\otimes H)\mathrm{CZ}(I\otimes H)$.

*Fizycznie:* sprzężenie Hadamardami zamienia rolę kontroli i celu (bo $H$ zamienia $X$ z $Z$).

## Z-06.5

(a) Np. $\langle\Phi^+\vert\Psi^+\rangle=\frac12(\langle00\vert+\langle11\vert)(\lvert01\rangle+\lvert10\rangle)=0$;
podobnie wszystkie pary różnych stanów Bella są ortogonalne, a każdy ma normę $1$ — ortonormalna baza.

(b) Dla $\lvert\Psi^-\rangle$: $a=0$, $b=\frac{1}{\sqrt2}$, $c=-\frac{1}{\sqrt2}$, $d=0$, więc
$ad-bc=\frac12$, $C=2\cdot\frac12=1$ (maksymalne splątanie).

(c) Ślad częściowy po $q_1$ zachowuje tylko wyrazy diagonalne:

$$
\rho_{q_0}=\tfrac12(\lvert0\rangle\langle0\rvert+\lvert1\rangle\langle1\rvert)=\tfrac12 I
\quad(\mathrm{diag}(0{,}5,0{,}5)).
$$

**Odpowiedź:** (a) ortonormalne; (b) $ad-bc=\frac12$, $C=1$; (c) $\mathrm{Tr}_{q_1}\rho=\frac12 I$.

*Fizycznie:* zredukowany stan pojedynczego kubita jest maksymalnie mieszany — to „podpis” maksymalnego splątania.

## Z-06.6

(a) $\Lambda(Z)=\lvert0\rangle\langle0\rvert\otimes I+\lvert1\rangle\langle1\rvert\otimes Z$. Z $HXH=Z$:

$$
(I\otimes H)\,\mathrm{CNOT}\,(I\otimes H)=\lvert0\rangle\langle0\rvert\otimes(HIH)+\lvert1\rangle\langle1\rvert\otimes(HXH)
=\lvert0\rangle\langle0\rvert\otimes I+\lvert1\rangle\langle1\rvert\otimes Z=\Lambda(Z).
$$

(b) Dla $U=R_Y(\theta)$ bierzemy $A=R_Y(\theta/2)$, $B=R_Y(-\theta/2)$, $C=I$; wtedy $ABC=I$ oraz
$AXBXC=R_Y(\theta)$ (bo $XR_Y(\eta)X=R_Y(-\eta)$). Obwód: $A,B,C$ na kubicie docelowym, przedzielone
dwoma CNOT: $(I\otimes A)\,\mathrm{CNOT}\,(I\otimes B)\,\mathrm{CNOT}\,(I\otimes C)$.

(c) $R_Y(\pi/2)\lvert0\rangle=\frac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)$, więc (kontrola $q_1=1$):

$$
\Lambda(R_Y(\pi/2))\lvert10\rangle=\lvert1\rangle\otimes\frac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)
=\frac{1}{\sqrt2}(\lvert10\rangle+\lvert11\rangle).
$$

Pomiar dolnego kubita: $P(0)=P(1)=\frac12$.

**Odpowiedź:** (a) zachodzi; (b) $A=R_Y(\theta/2)$, $B=R_Y(-\theta/2)$, $C=I$;
(c) $\Lambda(R_Y(\pi/2))\lvert10\rangle=\frac{1}{\sqrt2}(\lvert10\rangle+\lvert11\rangle)$, $P(0)=P(1)=\frac12$.

*Fizycznie:* dowolną kontrolowaną bramkę jednokubitową realizujemy trzema obrotami i dwoma CNOT —
fundament uniwersalności i dekompozycji obwodów.
