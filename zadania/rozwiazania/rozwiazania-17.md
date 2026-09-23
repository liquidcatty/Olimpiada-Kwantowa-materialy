# Rozwiązania do rozdziału 17

## Z-17.1

(a) Składanie diagonalnych rzutników daje macierz diagonalną:

$$\rho=\tfrac14\begin{pmatrix}1&0\\0&0\end{pmatrix}+\tfrac34\begin{pmatrix}0&0\\0&1\end{pmatrix}=\begin{pmatrix}0{,}25&0\\0&0{,}75\end{pmatrix}.$$

(b) $\mathrm{Tr}\,\rho^2=0{,}25^2+0{,}75^2=0{,}625$; skoro $r_x=r_y=0$, to
$\lvert\vec r\rvert=\lvert r_z\rvert=\lvert0{,}25-0{,}75\rvert=0{,}5$.
(c) $\mathrm{Tr}\,\rho^2=0{,}625<1$ oraz $\lvert\vec r\rvert=0{,}5<1$, więc to stan **mieszany**.

**Odpowiedź:** (a) $\mathbf{\mathrm{diag}(0{,}25;0{,}75)}$; (b) $\mathbf{\mathrm{Tr}\rho^2=0{,}625}$,
$\mathbf{\lvert\vec r\rvert=0{,}5}$; (c) stan mieszany.
*Fizycznie:* im mniej „czysty” stan, tym krótszy wektor Blocha — mieszanina leży wewnątrz sfery.

## Z-17.2

(a) Z $\rho=\tfrac12(I+\vec r\cdot\vec\sigma)$ i $\mathrm{Tr}(\sigma_j\sigma_k)=2\delta_{jk}$,
$\mathrm{Tr}\,\sigma_j=0$ mamy $r_j=\mathrm{Tr}(\rho\sigma_j)$; rozpisując na elementy:

$$r_x=2\,\mathrm{Re}\,\rho_{01},\qquad r_y=\mathrm{Tr}(\rho Y)=i\rho_{10}-i\rho_{01},\qquad r_z=\rho_{00}-\rho_{11}.$$

(b) Dla $\lvert+i\rangle$: $\rho_{01}=i/2$, więc $r_x=0$ oraz
$r_y=i(-\tfrac i2)-i(\tfrac i2)=\tfrac12+\tfrac12=1$, czyli $\vec r=(0,1,0)$.
(c) $\lvert+\rangle$: $\rho_{01}=1/2$ → $\vec r=(1,0,0)$; $\lvert-\rangle$: $\vec r=(-1,0,0)$.
Wektory różnią się **znakiem** $r_x$ — leżą na przeciwnych biegunach osi $X$.

**Odpowiedź:** (a) $r_j=\mathrm{Tr}(\rho\sigma_j)$; (b) $\mathbf{\vec r=(0,1,0)}$;
(c) $\mathbf{(1,0,0)}$ i $\mathbf{(-1,0,0)}$.
*Fizycznie:* ortogonalne stany leżą na przeciwległych końcach średnicy sfery Blocha.

## Z-17.3

(a) $\lvert\Phi^+\rangle\langle\Phi^+\rvert$ ma na diagonali $\tfrac12$ przy
$\lvert00\rangle\langle00\rvert$ i $\lvert11\rangle\langle11\rvert$ oraz $\tfrac12$ przy
$\lvert00\rangle\langle11\rvert,\lvert11\rangle\langle00\rvert$. Sumując po drugim kubicie:
$\rho_A=\mathrm{diag}\big(\tfrac12;\tfrac12\big)=\tfrac I2$.
(b) Dla $\lvert\Psi^-\rangle=\tfrac{1}{\sqrt2}(\lvert01\rangle-\lvert10\rangle)$ analogicznie
$\rho_A=\tfrac I2$.
(c) Dla $\tfrac I2$: $S=-\tfrac12\log_2\tfrac12-\tfrac12\log_2\tfrac12=1$ bit w obu przypadkach.

**Odpowiedź:** (a) $\mathbf{\tfrac I2}$; (b) $\mathbf{\tfrac I2}$; (c) $\mathbf{S=1}$ bita.
*Fizycznie:* każda maksymalnie splątana para daje po „zapomnieniu” maksymalnie mieszany kubit.

## Z-17.4

(a) Układamy amplitudy w macierz $M=\tfrac{1}{\sqrt3}\begin{pmatrix}1&1\\1&0\end{pmatrix}$ i liczymy
wartości szczególne (SVD): $\sqrt{\lambda_{1,2}}=(0{,}9342;\ 0{,}3568)$; kontrola
$0{,}8727+0{,}1273=1$ ✓.
(b) $S=-0{,}8727\log_20{,}8727-0{,}1273\log_20{,}1273=0{,}5500$ bita.
(c) Maksimum dla 2 kubitów to $\log_2 2=1$ bit, więc $0{,}55<1$ — splątanie **nie jest** maksymalne.

**Odpowiedź:** (a) $\mathbf{(0{,}9342;\ 0{,}3568)}$; (b) $\mathbf{S=0{,}550}$ **bita**;
(c) nie — mniej niż 1 bit.
*Fizycznie:* to stan „częściowo splątany”: rząd Schmidta równy 2, ale rozkład nierówny.

## Z-17.5

(a) $K_0=\mathrm{diag}(1,\sqrt{1-\gamma})$, $K_1=\begin{pmatrix}0&\sqrt\gamma\\0&0\end{pmatrix}$;
$K_0^\dagger K_0+K_1^\dagger K_1=\mathrm{diag}(1,1-\gamma)+\mathrm{diag}(0,\gamma)=I$ ✓.
(b) Dla $\gamma=0{,}3$: $\mathcal E(\lvert1\rangle\langle1\rvert)=\mathrm{diag}(0{,}3;0{,}7)$;
$\mathcal E(\lvert+\rangle\langle+\rvert)=\begin{pmatrix}0{,}65&0{,}4183\\0{,}4183&0{,}35\end{pmatrix}$
(populacja $\lvert1\rangle$ spada $1\to0{,}7$, koherencja $\tfrac12\to0{,}4183$).
(c) $\sum_i K_iK_i^\dagger=\mathrm{diag}(1,1-\gamma)+\mathrm{diag}(\gamma,0)=\mathrm{diag}(1+\gamma,\ 1-\gamma)\ne I$,
więc kanał **nie jest** unitalny.

**Odpowiedź:** (a) suma $=I$ ✓; (b) $\mathbf{\mathrm{diag}(0{,}3;0{,}7)}$ i
$\mathbf{\begin{pmatrix}0{,}65&0{,}4183\\0{,}4183&0{,}35\end{pmatrix}}$; (c) nie jest unitalny.
*Fizycznie:* tłumienie amplitudowe „ściąga” stan w stronę $\lvert0\rangle$ — dlatego nie jest unitalne.

## Z-17.6

(a) $p=0{,}3$: $K_0=\sqrt{1-\tfrac{3p}4}\,I=\sqrt{0{,}775}\,I=0{,}8803\,I$,
$K_j=\sqrt{\tfrac p4}\,P_j=\sqrt{0{,}075}\,P_j=0{,}2739\,P_j$ dla $P_j=X,Y,Z$; suma kwadratów
$=0{,}775+3\cdot0{,}075=1$ ✓.
(b) $\mathcal E(\lvert0\rangle\langle0\rvert)=0{,}7\lvert0\rangle\langle0\rvert+0{,}3\cdot\tfrac I2=\mathrm{diag}(0{,}85;0{,}15)$;
$\mathrm{Tr}\,\rho^2=0{,}85^2+0{,}15^2=0{,}745$.
(c) $(1-p)=(1-0{,}2)(1-0{,}3)=0{,}56$, więc $p=0{,}44$.

**Odpowiedź:** (a) $K_0=0{,}8803\,I$, $K_{1..3}=0{,}2739\,X,Y,Z$; (b)
$\mathbf{\mathrm{diag}(0{,}85;0{,}15)}$, purity $\mathbf{0{,}745}$; (c) $\mathbf{p=0{,}44}$.
*Fizycznie:* dwa kanały depolaryzujące „dodają się” w prawdopodobieństwie; po wielu krokach stan
zdąża do $\tfrac I2$.

## Z-17.7

(a) $\sqrt\rho=\rho=\mathrm{diag}(1,0)$, więc $\sqrt\rho\,\sigma\sqrt\rho=\mathrm{diag}(0{,}85;0)$ i
$F=\big(\mathrm{Tr}\,\mathrm{diag}(\sqrt{0{,}85};0)\big)^2=0{,}85=1-\tfrac p2$.
(b) $\rho-\sigma=\mathrm{diag}(0{,}15;-0{,}15)$, więc $D=\tfrac12(0{,}15+0{,}15)=0{,}15=\tfrac p2$.
(c) $1-\sqrt{0{,}85}=0{,}0398\le0{,}15\le\sqrt{0{,}15}=0{,}3873$ ✓ — nierówność spełniona.

**Odpowiedź:** (a) $\mathbf{F=0{,}85}$; (b) $\mathbf{D=0{,}15}$;
(c) $\mathbf{0{,}0398\le0{,}15\le0{,}3873}$ ✓.
*Fizycznie:* wierność i odległość śladowa to dwie strony tej samej „bliskości” stanów.

## Z-17.8

(a) Pomiar rzutowy w bazie $Z$: $K_0=\lvert0\rangle\langle0\rvert=\mathrm{diag}(1,0)$,
$K_1=\lvert1\rangle\langle1\rvert=\mathrm{diag}(0,1)$; $\sum K_i^\dagger K_i=I$ ✓.
(b) Kanał **nie jest** unitarny (bo $K_0^\dagger K_0=K_0\ne I$), ale **jest** unitalny:
$K_0K_0^\dagger+K_1K_1^\dagger=\mathrm{diag}(1,0)+\mathrm{diag}(0,1)=I$.
(c) Dla $\lvert+\rangle$: wyniki $0$ i $1$ po $\tfrac12$; z zapisem wyniku stan to $\lvert0\rangle$
lub $\lvert1\rangle$, a **uśredniony** po wynikach
$=\tfrac12(\lvert0\rangle\langle0\rvert+\lvert1\rangle\langle1\rvert)=\tfrac I2$. Koherencje, które
miało $\lvert+\rangle$ ($\rho_{01}=\tfrac12$), **znikają**.

**Odpowiedź:** (a) $K_i=\lvert i\rangle\langle i\rvert$; (b) nie jest unitarny, jest unitalny;
(c) $\mathbf{\rho\to\tfrac I2}$, koherencje zerowe.
*Fizycznie:* pomiar to nieodwracalny kanał — zamienia superpozycję na mieszaninę; to rdzeń
dekoherencji pomiarowej.
