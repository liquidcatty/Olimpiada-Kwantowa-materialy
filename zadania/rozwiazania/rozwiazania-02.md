# Rozwiązania do rozdziału 02

Pełne rozwiązania zadań Z-02.1–Z-02.8 z rozdziału
[02. Algebra liniowa](../../teoria/02-algebra-liniowa.md). Konwencja baz
małoendianowa.

## Z-02.1

**(a)** $\langle u|v\rangle=u_1^*v_1+u_2^*v_2=1^*\cdot i+(-i)\cdot1=i-i=0$.
Wektory są **ortogonalne**.

**(b)** $\lVert u\rVert=\sqrt{|1|^2+|i|^2}=\sqrt2$,
$\lVert v\rVert=\sqrt{|i|^2+|1|^2}=\sqrt2$.

**(c)** Po normalizacji $|u'\rangle=\tfrac{1}{\sqrt2}(1,i)^T$,
$|v'\rangle=\tfrac{1}{\sqrt2}(i,1)^T$. Działamy $Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix}$:

$$Y|u'\rangle=\tfrac{1}{\sqrt2}\begin{pmatrix}-i\cdot i\\ i\cdot1\end{pmatrix}
=\tfrac{1}{\sqrt2}\begin{pmatrix}1\\ i\end{pmatrix}=|u'\rangle
\ \Rightarrow \text{wartość }+1,$$

$$Y|v'\rangle=\tfrac{1}{\sqrt2}\begin{pmatrix}-i\cdot1\\ i\cdot i\end{pmatrix}
=\tfrac{1}{\sqrt2}\begin{pmatrix}-i\\ -1\end{pmatrix}=-|v'\rangle
\ \Rightarrow \text{wartość }-1.$$

**Odpowiedź:** **(a)** $\langle u|v\rangle=0$; **(b)** $\lVert u\rVert=\lVert v\rVert=\sqrt2$;
**(c)** $|u'\rangle$ ma $Y=+1$, $|v'\rangle$ ma $Y=-1$.

*Interpretacja:* to dwie ortonormalne bazy własne obserwabli $Y$ — w notacji
konwencji stany $|{+}i\rangle$ i $|{-}i\rangle$ na sferze Blocha (bieguny osi $Y$).

## Z-02.2

**(a)** $X=\begin{pmatrix}0&1\\1&0\end{pmatrix}$.

**(b)** $U=[|+\rangle\ |-\rangle]=\tfrac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$,
$U^\dagger=U$ (rzeczywista symetryczna). Liczymy

$$X'=U^\dagger XU=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}
\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix}
=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}1&-1\\1&1\end{pmatrix}
=\begin{pmatrix}1&0\\0&-1\end{pmatrix}=Z.$$

**(c)** W bazie $\{|\pm\rangle\}$ operator $X$ jest diagonalny z wartościami
własnymi $+1$ (stan $|+\rangle$) i $-1$ (stan $|-\rangle$). Zgadza się z faktem, że
$|\pm\rangle$ to stany własne $X$.

**Odpowiedź:** **(a)** $X=\begin{pmatrix}0&1\\1&0\end{pmatrix}$;
**(b)** $X'=\operatorname{diag}(1,-1)=Z$; **(c)** $X$ w bazie $X$-owej jest diagonalny.

*Interpretacja:* ta sama obserwabla w różnej bazie ma inną macierz; wybór bazy
$X$ zamienia role $X$ i $Z$ — dlatego mówimy o „bazie $X$” i „bazie $Z$”.

## Z-02.3

**(a)** $M^\dagger=\begin{pmatrix}2&1-i\\1+i&3\end{pmatrix}^\dagger =\begin{pmatrix}2&1-i\\1+i&3\end{pmatrix}=M$ — hermitowska. (Przekątna rzeczywista,
elementy poza przekątną sprzężone.)

**(b)** $\det(M-aI)=(2-a)(3-a)-(1-i)(1+i)=a^2-5a+(6-2)=a^2-5a+4=0$, skąd

## Z-02.4

**(a)** Ponieważ $Z^2=I$, to $Z^k=I$ dla $k$ parzystych i $Z^k=Z$ dla $k$
nieparzystych. Rozwijamy $R_Z(\theta)=e^{-i\theta Z/2}=\sum_k\frac{(-i\theta/2)^k}{k!}Z^k$
i rozdzielamy obie części:

$$\sum_{m}\frac{(-1)^m(\theta/2)^{2m}}{(2m)!}\,I=\cos\tfrac\theta2\,I,\qquad
\sum_{m}\frac{-i(-1)^m(\theta/2)^{2m+1}}{(2m+1)!}\,Z=-i\sin\tfrac\theta2\,Z,$$

skąd $R_Z(\theta)=\cos\tfrac\theta2 I-i\sin\tfrac\theta2 Z$.

**(b)** $R_Z^\dagger R_Z=\bigl(\cos\tfrac\theta2 I+i\sin\tfrac\theta2 Z\bigr) \bigl(\cos\tfrac\theta2 I-i\sin\tfrac\theta2 Z\bigr) =\cos^2\tfrac\theta2 I+\sin^2\tfrac\theta2 I=I$, bo $Z^2=I$ i $Z$ hermitowskie.

**(c)** Dla $\theta=\pi/2$: $\cos\tfrac\pi4=\sin\tfrac\pi4=\tfrac{1}{\sqrt2}$, więc

$$R_Z(\tfrac\pi2)=\operatorname{diag}\!\Bigl(e^{-i\pi/4},e^{i\pi/4}\Bigr)
=\operatorname{diag}\!\bigl(0{,}7071-0{,}7071i,\ 0{,}7071+0{,}7071i\bigr).$$

Działanie: $R_Z(\tfrac\pi2)|0\rangle=e^{-i\pi/4}|0\rangle$,
$R_Z(\tfrac\pi2)|1\rangle=e^{i\pi/4}|1\rangle$ — same fazy, bez zmiany prawdopodobieństw.

**Odpowiedź:** **(a)** $R_Z(\theta)=\cos\tfrac\theta2 I-i\sin\tfrac\theta2 Z$;
**(b)** unitarna; **(c)** $R_Z(\pi/2)=\operatorname{diag}(e^{-i\pi/4},e^{i\pi/4})$.

*Interpretacja:* $R_Z$ obraca stan wokół osi $Z$ na sferze Blocha o kąt $\theta$;
na biegunach $|0\rangle,|1\rangle$ obrót objawia się tylko fazą.

## Z-02.5

**(a)** $\operatorname{Tr}M=2+3+1=6$.

**(b)** Rozwinięcie względem pierwszego wiersza:

$$\det M=2\begin{vmatrix}3&0\\1&1\end{vmatrix}-0+1\begin{vmatrix}1&3\\0&1\end{vmatrix}
=2\cdot3+1\cdot1=7.$$

**(c)** $\operatorname{rank}M=3$ (równoważnie
$\det M=7\ne0$), więc $M$ jest odwracalna.

**Odpowiedź:** **(a)** $6$; **(b)** $7$; **(c)** rząd $3$, macierz **odwracalna**.

*Interpretacja:* niezerowy wyznacznik i pełny rząd oznaczają, że $M$ nie ma
niezerowego jądra — układ $Mx=0$ ma tylko rozwiązanie $x=0$.

## Z-02.6

Deklaracja: kontrolny = kubit 1 (górny), docelowy = kubit 0 (dolny), baza

## Z-02.7

**(a)** Z definicji komutatora $[A,B]=AB-BA$ i mnożenia macierzy:

$$XY=\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}0&-i\\i&0\end{pmatrix}
=\begin{pmatrix}i&0\\0&-i\end{pmatrix}=iZ,$$

$$YX=\begin{pmatrix}0&-i\\i&0\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}
=\begin{pmatrix}-i&0\\0&i\end{pmatrix}=-iZ.$$

Stąd $[X,Y]=(i-(-i))Z=2iZ$. Cyklicznie: $[Y,Z]=2iX$, $[Z,X]=2iY$.

**(b)** $\{X,Y\}=XY+YX=iZ-iZ=0$ (antykomutują). Natomiast
$\{X,X\}=XX+XX=2X^2=2I$ (bo $X^2=I$).

**(c)** Dla $(a,b)=(X,Y)$: $\delta_{XY}=0$, a jedyny niezerowy symbol $\varepsilon_{XYZ}=+1$,
więc wzór daje $\sigma_X\sigma_Y=i\sigma_Z=iZ$. Z rachunku w (a): $XY=iZ$ ✓.

**Odpowiedź:** **(a)** $[X,Y]=2iZ$, $[Y,Z]=2iX$, $[Z,X]=2iY$; **(b)** $\{X,Y\}=0$,
$\{X,X\}=2I$; **(c)** zgadza się: $XY=iZ$.

*Interpretacja:* nieprzemienność Pauliego (niezerowy komutator) jest źródłem zasady
nieoznaczoności i relacji $[\sigma_a,\sigma_b]\propto\varepsilon_{abc}\sigma_c$;
antykomutacja $\{\sigma_a,\sigma_b\}=0$ dla $a\ne b$ jest równoważna ortogonalności
osobliwych wektorów na sferze Blocha.

## Z-02.8 [★]

Stan $|\psi\rangle=\cos\alpha|00\rangle+\sin\alpha|11\rangle$, współczynnik
$\alpha=0{,}6$ rad.

**(a)** Macierz współczynników w bazie iloczynowej:
$\Psi=\begin{pmatrix}\cos\alpha&0\\0&\sin\alpha\end{pmatrix}$. Jej wartości osobliwe
to wartości bezwzględne elementów przekątnej: $s_1=|\cos0{,}6|$, $s_2=|\sin0{,}6|$.

**(b)** $s_1^2=\cos^2 0{,}6\approx0{,}6812$, $s_2^2=\sin^2 0{,}6\approx0{,}3188$.

$$S=-\bigl(0{,}6812\log_2 0{,}6812+0{,}3188\log_2 0{,}3188\bigr)\approx0{,}903\ \text{bita}.$$

**(c)** Stan jest iloczynowy, gdy $S=0$, czyli gdy jeden ze współczynników znika:
$\sin\alpha=0$ (wtedy $|\psi\rangle=|00\rangle$) lub $\cos\alpha=0$ (wtedy
$|\psi\rangle=|11\rangle$), tzn. dla $\alpha=0,\ \tfrac{\pi}{2}$ (mod $\pi$).

**Odpowiedź:** **(a)** $s_1\approx0{,}8253$, $s_2\approx0{,}5646$;
**(b)** $S\approx0{,}903$ bita; **(c)** iloczynowy dla $\alpha=0,\pi/2$ (mod $\pi$).

*Interpretacja:* dla $\alpha=0{,}6$ obie $s_k>0$, więc stan jest **splątany**; entropia
$S\approx0{,}90$ bity mierzy „ilość splątania”. Dla $\alpha=\pi/4$ ($s_1=s_2=1/\sqrt2$)
entropia osiąga maksimum $S=1$ bit — to stan Bella
$\tfrac{1}{\sqrt2}(|00\rangle+|11\rangle)$.
$|00\rangle,|01\rangle,|10\rangle,|11\rangle$.

**(a)** Zgodnie ze wzorem $\mathrm{CNOT}=|0\rangle\langle0|\otimes I+|1\rangle\langle1|\otimes X$:

$$\mathrm{CNOT}=\begin{pmatrix}1&0\\0&0\end{pmatrix}\otimes I
+\begin{pmatrix}0&0\\0&1\end{pmatrix}\otimes X
=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}.$$

**(b)** $\mathrm{CNOT}|00\rangle=|00\rangle$, $\mathrm{CNOT}|01\rangle=|01\rangle$,
$\mathrm{CNOT}|10\rangle=|11\rangle$, $\mathrm{CNOT}|11\rangle=|10\rangle$.

**(c)** $\mathrm{CNOT}^2=I$ (iloczyn macierzy daje identyczność), a
$\mathrm{CNOT}^\dagger=\mathrm{CNOT}^T=\mathrm{CNOT}$ (macierz rzeczywista symetryczna),
skąd $\mathrm{CNOT}^\dagger\mathrm{CNOT}=\mathrm{CNOT}^2=I$ — unitarna i hermitowska.

**Odpowiedź:** **(a)** macierz jak wyżej; **(b)** kontrolny $=1$ odwraca docelowy;
**(c)** $\mathrm{CNOT}^2=I$, $\mathrm{CNOT}$ unitarna.

*Interpretacja:* CNOT to „kontrolowany flip”: jeśli górny kubit jest w $|1\rangle$,
dolny się odwraca. To bramka dwukubitowa generująca splątanie (rozdział 09).
$a=1$ lub $a=4$.

**(c)** Wektory własne: dla $a=1$ z $(M-I)v=0$ dostajemy $v_1=(-1+i,1)/\sqrt3$;
dla $a=4$ z $(M-4I)v=0$ dostajemy $v_2=(1-i,2)/\sqrt6$. Rozkład spektralny:

$$M=1\cdot v_1v_1^\dagger+4\cdot v_2v_2^\dagger.$$

Oczekiwana wartość w $|+\rangle=\tfrac{1}{\sqrt2}(1,1)^T$:

$$\langle+|M|+\rangle=\tfrac12\begin{pmatrix}1&1\end{pmatrix}
\begin{pmatrix}2&1-i\\1+i&3\end{pmatrix}\begin{pmatrix}1\\1\end{pmatrix}
=\tfrac12(3-i+4+i)=\tfrac72=3{,}5.$$

**Odpowiedź:** **(a)** $M=M^\dagger$; **(b)** $a\in\{1,4\}$;
**(c)** $v_1=\tfrac{1}{\sqrt3}(-1+i,1)^T$, $v_2=\tfrac{1}{\sqrt6}(1-i,2)^T$;
$\langle+|M|+\rangle=3{,}5$.

*Interpretacja:* wartości własne $1$ i $4$ to jedyne możliwe wyniki pomiaru $M$.
Rozkład prawdopodobieństw dla $|+\rangle$: rzuty dają $|\langle v_1|+\rangle|^2=\tfrac16$
i $|\langle v_2|+\rangle|^2=\tfrac56$, stąd
$\langle M\rangle=1\cdot\tfrac16+4\cdot\tfrac56=3{,}5$, co zgadza się z rachunkiem
macierzowym.
