# Rozwiązania do rozdziału 09

## Z-09.1

(a) Dla $\lvert\Phi^+\rangle$: $a=d=\frac{1}{\sqrt2}$, $b=c=0$, więc $ad=\frac12$, $bc=0$, $ad\ne bc$
— **splątany**. Dla $\lvert+\rangle\otimes\lvert0\rangle=\frac{1}{\sqrt2}(\lvert00\rangle+\lvert10\rangle)$:
$a=c=\frac{1}{\sqrt2}$, $b=d=0$, więc $ad=bc=0$ — **iloczynowy**.

(b) $C=2\lvert ad-bc\rvert$: dla $\lvert\Phi^+\rangle$ $C=2\cdot\frac12=1$.
Dla $\frac{1}{\sqrt3}(\lvert00\rangle+\lvert01\rangle+\lvert10\rangle)$: $a=b=c=\frac{1}{\sqrt3}$, $d=0$,
$C=2\lvert-\frac13\rvert=\frac23\approx0{,}667$.

(c) $\frac12(\lvert00\rangle+\lvert01\rangle+\lvert10\rangle+\lvert11\rangle)$: $a=b=c=d=\frac12$,
$ad=\frac14=bc$ — **iloczynowy** ($=\lvert+\rangle\otimes\lvert+\rangle$), więc **nie jest splątany**.

**Odpowiedź:** (a) $\Phi^+$ splątany, $\lvert+\rangle\lvert0\rangle$ iloczynowy; (b) $C=1$ i $C=\frac23$;
(c) nie — to produkt $\lvert+\rangle\lvert+\rangle$.

*Fizycznie:* kryterium $ad=bc$ (lub concurrence) szybko rozstrzyga o splątaniu stanu czystego dwóch kubitów.

## Z-09.2

(a) Macierz współczynników stanu $\lvert\Psi^-\rangle=\frac{1}{\sqrt2}(\lvert01\rangle-\lvert10\rangle)$ ma postać:

$$
M=\frac{1}{\sqrt2}\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$

$MM^\dagger=\frac12 I$, wartości szczególne
$\frac{1}{\sqrt2},\frac{1}{\sqrt2}$, więc $\lambda_1=\lambda_2=\frac12$:

$$
\lvert\Psi^-\rangle=\tfrac{1}{\sqrt2}\lvert u_1\rangle\lvert v_1\rangle-\tfrac{1}{\sqrt2}\lvert u_2\rangle\lvert v_2\rangle
$$

(rozkład Schmidta z równymi współczynnikami — stan maksymalnie splątany).

(b) $S=-\frac12\log_2\frac12-\frac12\log_2\frac12=1$ bit.

(c) Dla stanu z Przykładu 1 rozdziału 09 rząd Schmidta $=2$ (obie $\lambda_i>0$) — stan jest splątany,
choć nie maksymalnie.

**Odpowiedź:** (a) $\lambda_{1,2}=\frac12$; (b) $S=1$ bit; (c) $r=2$.

*Fizycznie:* równe wartości Schmidta $=$ maksymalne splątanie; entropia splątania $1$ bit to maksimum
dla dwóch kubitów.

## Z-09.3

(a) $\rho_W^{T_B}$ dla $\rho_W=p\lvert\Phi^+\rangle\langle\Phi^+\rvert+\frac{1-p}{4}I$ ma wartości własne

$$
\lambda=\frac{1+p}{4}\ (\times3),\qquad \lambda=\frac{1-3p}{4}\ (\times1).
$$

(Suma $=3\frac{1+p}{4}+\frac{1-3p}{4}=1$; zgadza się z $\mathrm{Tr}\,\rho_W^{T_B}=1$.)

(b) Najmniejsza wartość własna $\frac{1-3p}{4}<0\iff p>\frac13$.

(c) $\mathrm{Tr}(W\rho_W)=p\,\mathrm{Tr}(W\lvert\Phi^+\rangle\langle\Phi^+\rvert)+\frac{1-p}{4}\mathrm{Tr}(W) =\frac12-\big(p+\frac{1-p}{4}\big)=\frac{1-3p}{4}<0\iff p>\frac13.$ Próg identyczny z PPT.

**Odpowiedź:** (a) $\frac{1+p}{4}$ (×3) i $\frac{1-3p}{4}$; (b) $p>\frac13$; (c) $\mathrm{Tr}(W\rho_W)=\frac{1-3p}{4}$.

*Fizycznie:* świadek splątania to „skrojona” obserwabla, która na stanach separowalnych jest nieujemna,
a na wybranym splątanym — ujemna.

## Z-09.4

(a) Dla LHV: $S(\lambda)=A_a(B_b-B_{b'})+A_{a'}(B_b+B_{b'})$. Jeśli $B_b=B_{b'}$, pierwszy nawias $=0$,
drugi $=\pm2$; jeśli $B_b=-B_{b'}$, drugi $=0$, pierwszy $=\pm2$. W obu przypadkach $\lvert S(\lambda)\rvert=2$,
więc $\lvert S\rvert=\lvert\int S(\lambda)\rho\,d\lambda\rvert\le\int\lvert S\rvert\rho\,d\lambda\le2$.

(b) Z $E(a,b)=-\cos(\theta_a-\theta_b)$:
$E(0,45)=-\frac{\sqrt2}{2}$, $E(0,135)=+\frac{\sqrt2}{2}$, $E(90,45)=-\frac{\sqrt2}{2}$, $E(90,135)=-\frac{\sqrt2}{2}$,

$$
S=-\tfrac{\sqrt2}{2}-\tfrac{\sqrt2}{2}-\tfrac{\sqrt2}{2}-\tfrac{\sqrt2}{2}=-2\sqrt2\ \Rightarrow\ \lvert S\rvert=2\sqrt2.
$$

(c) Brak korelacji $\Rightarrow$ każda $E(a,b)=0$, więc $S=0$ — trywialnie w granicach LHV.

**Odpowiedź:** (a) dowód jak wyżej; (b) $\lvert S\rvert=2\sqrt2$; (c) $S=0$.

*Fizycznie:* naruszenie CHSH to doświadczalne kryterium „prawdziwie kwantowych” korelacji.

## Z-09.5

(a) $\lvert\mathrm{GHZ}\rangle=\frac{1}{\sqrt2}(\lvert000\rangle+\lvert111\rangle)$. Ślad po trzecim
kubicie: $\rho_{AB}=\frac12(\lvert00\rangle\langle00\rvert+\lvert11\rangle\langle11\rvert)$.

(b) $\rho_{AB}$ jest diagonalne (klasyczna mieszanina stanów $\lvert00\rangle,\lvert11\rangle$),
więc $C(A,B)=0$. Z monogamii $C(A,B)^2+C(A,C)^2\le C(A,BC)^2$: całe splątanie
jest „zarezerwowane” dla pary $A$–$BC$.

(c) GHZ nie ma splątania dwustronnego po odrzuceniu kubita; stan W
$\frac{1}{\sqrt3}(\lvert001\rangle+\lvert010\rangle+\lvert100\rangle)$ **ma** — po śladzie dostajemy
$\rho_{AB}=\frac13\big(\lvert00\rangle\langle00\rvert+\lvert01\rangle\langle01\rvert+\lvert10\rangle\langle10\rvert+\lvert01\rangle\langle10\rvert+\lvert10\rangle\langle01\rvert\big)$
z concurrence $C=\frac23$.

**Odpowiedź:** (a) $\rho_{AB}=\frac12(\lvert00\rangle\langle00\rvert+\lvert11\rangle\langle11\rvert)$;
(b) $C=0$ — monogamia; (c) W ma $C=\frac23$, GHZ $C=0$.

*Fizycznie:* GHZ to „kruche” splątanie trójstronne; W jest odporne — upuszczając kubit, wciąż zostaje
splątanie dwustronne.

## Z-09.6

(a) $\rho=(1-p)\lvert\Phi^+\rangle\langle\Phi^+\rvert+p\,\frac{I}{4}$ w bazie Bella ma wagi
$\lambda_{\Phi^+}=1-\frac{3p}{4}$ oraz $\frac p4$ dla pozostałych. Concurrence dla stanów Bella-diagonalnych:

$$
C=\max\!\Big(0,\,2\big(1-\tfrac{3p}{4}\big)-1\Big)=\max\!\big(0,\,1-\tfrac{3p}{2}\big).
$$

(b) $C=0\iff 1-\frac{3p}{2}\le0\iff p\ge\frac23$. W Z-09.3(b) (parametr „sygnału” $p'=1-p$) próg PPT
to $p'>\frac13$, czyli $1-p>\frac13\Rightarrow p<\frac23$ — **ten sam próg** $p=\frac23$.

(c) Dla dwóch kubitów kryterium PPT jest **konieczne i wystarczające**, więc próg separowalności
z PPT pokrywa się z progiem zaniku concurrence. Dla układów wyżej wymiarowych istnieją stany splątane
o dodatniej transpozycji częściowej (PPT-entangled), dla których progi mogą się różnić.

**Odpowiedź:** (a) $C=\max(0,1-\frac{3p}{2})$; (b) $p=\frac23$, zgodnie z PPT; (c) dla $2\times2$ progi
pokrywają się (PPT wystarcza); różnie bywa dla bound entangled.

*Fizycznie:* dekoherencja „wypiera” splątanie stopniowo; przy $p\ge\frac23$ stan staje się formalnie
separowalny, mimo że „wygląda” jak zaburzony stan Bella.
