# 02. Algebra liniowa


## 1. Zakres rozdziału

Rozdział obejmuje rachunek na wektorach i macierzach: iloczyn skalarny, sprzężenie
hermitowskie, ślad, wyznacznik oraz iloczyn tensorowy (kron). Omawia operatory
hermitowskie i unitarne, wartości i wektory własne, twierdzenie spektralne,
diagonalizację, a także macierze Pauliego, sferę Blocha, funkcje macierzy
$e^{-iHt/\hbar}$ i rozkład Schmidta. Materiał dotyczy zadań P1 (studnia potencjału),
P2 (polaryzatory), P3 (bramki $H,Z,H$) i P4 (obwód z $R_Y(\theta)$ i CNOT).

## 2. Najważniejsze definicje

- **Przestrzeń wektorowa nad $\mathbb{C}$**: zbiór z dodawaniem i mnożeniem przez
  skalary zespolone. Dla $n$ kubitów wymiar wynosi $2^n$.
- **Iloczyn skalarny** $\langle\phi|\psi\rangle=\sum_k\phi_k^*\psi_k$; **norma**
  $\lVert\psi\rVert=\sqrt{\langle\psi|\psi\rangle}$.
- **Baza ortonormalna** $\{|e_k\rangle\}$: $\langle e_j|e_k\rangle=\delta_{jk}$.
- **Operator liniowy** $A$: $A(\alpha|\psi\rangle+\beta|\phi\rangle)=\alpha A|\psi\rangle+\beta A|\phi\rangle$;
  w bazie reprezentowany macierzą $A_{ij}=\langle e_i|A|e_j\rangle$.
- **Sprzężenie hermitowskie** $A^\dagger=(A^*)^T$.
- **Operator hermitowski** (*Hermitian*): $A^\dagger=A$ — obserwabla.
- **Operator unitarny** (*unitary*): $U^\dagger U=I$ — ewolucja/bramka.
- **Wektory własne i wartości własne**: $A|a\rangle=a|a\rangle$; dla hermitowskiego
  $a\in\mathbb{R}$, a wektory własne różnych wartości są ortogonalne.
- **Rozkład spektralny**: $A=\sum_a a\,|a\rangle\langle a|$.
- **Ślad** $\operatorname{Tr}A=\sum_i A_{ii}$; **wyznacznik** $\det A$;
  **rząd** $\operatorname{rank}A$ = wymiar obrazu.
- **Iloczyn tensorowy (kron)**: $(A\otimes B)_{(ip),(jq)}=A_{ij}B_{pq}$.
- **Rozkład Blocha**: $\rho=\frac12(I+\vec r\cdot\vec\sigma)$, $|\vec r|\le1$.

## 3. Teoria krok po kroku

### 3.1 Przestrzenie wektorowe nad $\mathbb{C}$

Wektory dodajemy po współrzędnych, a mnożymy przez **zespolone** skalary. Podstawowa
różnica wobec $\mathbb{R}^n$: współczynniki superpozycji mogą być zespolone, co daje
fazę. Bazę $\{|e_k\rangle\}$ nazywamy zupełną, gdy każdy wektor da się zapisać jako
$\sum_k c_k|e_k\rangle$; współczynniki liczymy rzutem $c_k=\langle e_k|\psi\rangle$.

### 3.2 Iloczyn skalarny i bazy ortonormalne

Iloczyn skalarny jest **antyliniowy** w pierwszym argumencie:
$\langle\phi|\alpha\psi+\beta\chi\rangle=\alpha\langle\phi|\psi\rangle+\beta\langle\phi|\chi\rangle$,
ale $\langle\alpha\phi|\psi\rangle=\alpha^*\langle\phi|\psi\rangle$. Konsekwencją jest
$\langle\phi|\psi\rangle=\langle\psi|\phi\rangle^*$ i $\langle\psi|\psi\rangle\ge0$.

Z każdej bazy robimy ortonormalną metodą Grama–Schmidta. Baza obliczeniowa kubitu
$\{|0\rangle,|1\rangle\}$ jest ortonormalna: $\langle0|0\rangle=\langle1|1\rangle=1$,
$\langle0|1\rangle=0$.

### 3.3 Operatory liniowe i ich macierze

Operator $A$ działa na wektory; jego macierz w bazie $\{|e_k\rangle\}$ ma element
$A_{ij}=\langle e_i|A|e_j\rangle$. Złożenie operatorów to mnożenie macierzy, a
działanie na stan $\lvert\psi\rangle=\sum_k c_k|e_k\rangle$ daje
$A|\psi\rangle$, którego współrzędne to $A\cdot(c_1,\dots,c_n)^T$.

Zmiana bazy: jeśli $U$ ma kolumny równe nowym wektorom bazy, to ta sama obserwabla
w nowej bazie to $A'=U^\dagger A U$.

### 3.4 Sprzężenie hermitowskie

$A^\dagger=(A^*)^T$: transpozycja połączona ze sprzężeniem zespolonym elementów.
Właściwości: $(AB)^\dagger=B^\dagger A^\dagger$, $(A^\dagger)^\dagger=A$,
$(\alpha A)^\dagger=\alpha^*A^\dagger$, $\langle\phi|A|\psi\rangle=\langle\psi|A^\dagger|\phi\rangle^*$.

### 3.5 Operatory hermitowskie i unitarne

Dwa typy operatorów w mechanice kwantowej:

- **Hermitowski** $A^\dagger=A$: ma rzeczywiste wartości własne, odpowiadają
  mierzalnym wielkościom (energia, spin, położenie). Przykłady: macierze Pauliego
  $\sigma_x,\sigma_y,\sigma_z$, hamiltonian $H$.
- **Unitarny** $U^\dagger U=I$: zachowuje iloczyn skalarny i normę, opisuje ewolucję
  i bramki. Zachodzi $U^\dagger=U^{-1}$.

**Związek:** dla hermitowskiego $H$ operator $U(t)=e^{-iHt/\hbar}$ jest unitarny —
to ewolucja czasowa ze wzoru z rozdziału
[05](05-podstawy-mechaniki-kwantowej.md).

### 3.6 Wartości i wektory własne

$|a\rangle\ne0$ jest wektorem własnym $A$ z wartością własną $a$, gdy $A|a\rangle=a|a\rangle$.
Wyznaczamy je z równania charakterystycznego $\det(A-aI)=0$. Dla $A$ hermitowskiego:
wartości własne rzeczywiste, wektory własne różnych wartości ortogonalne.

### 3.7 Twierdzenie spektralne i diagonalizacja

**Twierdzenie spektralne.** Każdy operator hermitowski $A$ ma ortonormalną bazę
wektorów własnych i rozkład $A=\sum_a a\,|a\rangle\langle a|$. W tej bazie $A$ jest
macierzą diagonalną $D=\operatorname{diag}(a_1,\dots,a_n)$, a przejście realizuje
macierz unitarna $U$ (kolumny = wektory własne):

$$A=U D U^\dagger,\qquad D=U^\dagger A U.$$

Posługując się rozkładem spektralnym, każdą „sensowną” funkcję $f$ liczymy na
wartościach własnych: $f(A)=\sum_a f(a)|a\rangle\langle a|$.

### 3.8 Funkcje macierzy: $e^{-iHt/\hbar}$

Dla hermitowskiego $H$ definiujemy

$$e^{-iHt/\hbar}=\sum_a e^{-ia t/\hbar}|a\rangle\langle a|,$$

gdzie $a$ to wartości własne $H$. To rozwiązanie równania Schrödingera:
$|\psi(t)\rangle=e^{-iHt/\hbar}|\psi(0)\rangle$. Praktycznie: diagonalizujemy $H$,
podnosimy $e^{-iat/\hbar}$ i wracamy do oryginalnej bazy.

**Przykład 2×2.** Dla $H=\tfrac{\hbar\omega}{2}Z$ wartości własne to $\pm\tfrac{\hbar\omega}{2}$,
więc

$$e^{-iHt/\hbar}=e^{-i\omega t Z/2}=\cos\!\Bigl(\tfrac{\omega t}{2}\Bigr)I-i\sin\!\Bigl(\tfrac{\omega t}{2}\Bigr)Z
=\operatorname{diag}\!\bigl(e^{-i\omega t/2},e^{i\omega t/2}\bigr).$$

Ostatnia macierz to dokładnie $R_Z(\omega t)$ w notacji konwencji (kąt $\theta/2$).

### 3.9 Ślad, wyznacznik, rząd

- **Ślad** $\operatorname{Tr}A=\sum_iA_{ii}$: liniowy, cykliczny
  $\operatorname{Tr}(AB)=\operatorname{Tr}(BA)$, niezmienniczy na zmianę bazy.
  $\operatorname{Tr}A=\sum_a a$ (suma wartości własnych).
- **Wyznacznik** $\det A=\prod_a a$; $\det(AB)=\det A\det B$. $\det A\ne0 \Leftrightarrow A$ odwracalny.
- **Rząd** $\operatorname{rank}A$ = liczba niezerowych wartości osobliwych = wymiar
  obrazu. Dla macierzy $A$ zachodzi $\operatorname{rank}A+\dim\ker A=n$.

Dla macierzy $2\times2$: $\operatorname{Tr}M=m_{11}+m_{22}$,
$\det M=m_{11}m_{22}-m_{12}m_{21}$.

### 3.10 Iloczyn tensorowy (kron)

Dla macierzy $A$ ($m\times n$) i $B$ ($p\times q$) blokowe złożenie:

$$A\otimes B=\begin{pmatrix}A_{11}B&\cdots&A_{1n}B\\ \vdots&&\vdots\\ A_{m1}B&\cdots&A_{mn}B\end{pmatrix},$$

wymiar $mp\times nq$. Dla wektorów: $(a\otimes b)_{ip}=a_ib_p$. Dla $n$ kubitów
$\dim=2^n$.

**Konwencja kolejności (małoendianowa).** Stan $|q_{n-1}\dots q_0\rangle$ ma indeks
$j=q_0 2^0+\dots+q_{n-1}2^{n-1}$ — **kubit 0 to najmłodszy bit**. Dlatego bramka na
kubicie 0 (dolnym) to $U=I\otimes G$, a na kubicie 1 (górnym) to $U=G\otimes I$.
Zawsze jawnie podaje się konwencję.

### 3.11 Macierze Pauliego, komutatory i antykomutatory

$$\sigma_x=X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\sigma_y=Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
\sigma_z=Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$

Relacje:

$$[\sigma_a,\sigma_b]=2i\sum_c\varepsilon_{abc}\sigma_c,\qquad
\{\sigma_a,\sigma_b\}=2\delta_{ab}I,\qquad
\sigma_a\sigma_b=\delta_{ab}I+i\sum_c\varepsilon_{abc}\sigma_c,\qquad
\sigma_a^2=I.$$

W szczególności $[X,Y]=2iZ$, $[Y,Z]=2iX$, $[Z,X]=2iY$, a $\{X,Y\}=0$ (antykomutują).
Skąd to się bierze: kolejność mnożenia Pauliego a Pauliego to „obrót o inny Pauli”,
a antykomutacja znika, bo każda $\sigma$ podniesiona do kwadratu daje $I$.

### 3.12 Sfera Blocha

Dowolny stan czysty kubitu (z dokładnością do fazy globalnej) to punkt na sferze
jednostkowej:

$$|\psi\rangle=\cos\tfrac\theta2|0\rangle+e^{i\varphi}\sin\tfrac\theta2|1\rangle,\qquad
\vec r=(\langle X\rangle,\langle Y\rangle,\langle Z\rangle).$$

Kąt $\theta$ to odchylenie od osi $Z$ („biegun $|0\rangle$”), $\varphi$ to azymut.
Przykłady: $|0\rangle\to\vec r=(0,0,1)$; $|+\rangle\to(1,0,0)$; $|i\rangle\to(0,1,0)$.
Dla stanu mieszanego $|\vec r|<1$, a macierz gęstości
$\rho=\tfrac12(I+\vec r\cdot\vec\sigma)$.

### 3.13 Rozkład Schmidta (zapowiedź splątania)

Dla dwukubitowego stanu $|\psi\rangle\in\mathbb{C}^2\otimes\mathbb{C}^2$ istnieje
rozkład

$$|\psi\rangle=s_1|u_1\rangle|v_1\rangle+s_2|u_2\rangle|v_2\rangle,$$

gdzie $s_1\ge s_2\ge0$ to **wartości osobliwe** (Schmidta) macierzy współczynników,
a $\{|u_k\rangle\},\{|v_k\rangle\}$ to bazy ortonormalne. Stan jest **iloczynowy**
(*product state*) wtedy i tylko wtedy, gdy tylko jedna $s_k$ jest niezerowa. Wtedy
„nic nie jest splątane”. Jeśli obie $s_k>0$ — stan jest splątany (*entangled*);
miarą splątania jest entropia $S=-\sum_k s_k^2\log_2 s_k^2$. Szczegóły w
[rozdziale 09](09-splatanie-i-twierdzenie-bella.md); rozkład Schmidta jest tu
ćwiczeniem z algebry.

### 3.14 Bramka CNOT

Kontrolowany NOT działa tak: jeśli kubit kontrolny jest w $|1\rangle$, odwraca kubit
docelowy (X); jeśli w $|0\rangle$ — nic nie robi. Jako operator:

$$\mathrm{CNOT}=|0\rangle\langle0|\otimes I+|1\rangle\langle1|\otimes X,$$

gdzie pierwszy czynnik to kubit kontrolny (**górny, kubit 1** w naszej konwencji), a
drugi to docelowy (**kubit 0**). Zapisując w porządku $|00\rangle,|01\rangle,|10\rangle,|11\rangle$:

$$\mathrm{CNOT}=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}.$$

Iloczyn tensorowy $|0\rangle\langle0|\otimes I+|1\rangle\langle1|\otimes X$
daje powyższą macierz. CNOT jest unitarny i hermitowski ($\mathrm{CNOT}^2=I$).

## 4. Przykłady rozwiązane

### Przykład 1 (łatwy): diagonalizacja obserwabli $2\times2$

**Dane:** $M=\begin{pmatrix}2&1-i\\ 1+i&3\end{pmatrix}$.

**Metoda:** sprawdzić hermitowskość ($M^\dagger=M$), znaleźć wartości własne
z $\det(M-aI)=0$, wektory własne z $(M-aI)v=0$, złożyć $D=U^\dagger MU$.

**Rachunek.** Sprzężenie: $M^\dagger=\begin{pmatrix}2&1-i\\ 1+i&3\end{pmatrix}=M$ ✓
(przekątna rzeczywista, wyrazy poza przekątną sprzężone). Równanie charakterystyczne:

$$\det(M-aI)=(2-a)(3-a)-(1-i)(1+i)=(2-a)(3-a)-2=a^2-5a+4=0,$$

stąd $a_1=1$, $a_2=4$. Wektory własne:

$$a_1=1:\ (M-I)v=0\Rightarrow v_1=(-1+i,\,1)/\sqrt3,\qquad
a_2=4:\ (M-4I)v=0\Rightarrow v_2=(1-i,\,2)/\sqrt6.$$

Sprawdzamy $M v_1=1\cdot v_1$, $M v_2=4\cdot v_2$ (wartości $\{1,4\}$) ✓.

**Wynik:** wartości własne $\{1,4\}$; $U=[v_1\ v_2]$ diagonalizuje:
$\operatorname{diag}(1,4)=U^\dagger MU$.

**Interpretacja:** skoro $M$ jest hermitowska, jej wartości własne są rzeczywiste i
odpowiadają możliwym wynikom pomiaru; prawdopodobieństwa wyników dostajemy rzutując
stan na $v_1,v_2$.

### Przykład 2 (trudniejszy): budowa CNOT i jej działanie

**Dane:** bramka CNOT, kontrolny = kubit 1 (górny), docelowy = kubit 0 (dolny), baza
$|00\rangle,|01\rangle,|10\rangle,|11\rangle$ (małoendianowo).

**Metoda:** $\mathrm{CNOT}=|0\rangle\langle0|\otimes I+|1\rangle\langle1|\otimes X$;
działanie przez mnożenie macierzy.

**Rachunek.** $|0\rangle\langle0|=\begin{pmatrix}1&0\\0&0\end{pmatrix}$,
$|1\rangle\langle1|=\begin{pmatrix}0&0\\0&1\end{pmatrix}$, $X=\begin{pmatrix}0&1\\1&0\end{pmatrix}$.

$$\mathrm{CNOT}=\begin{pmatrix}1&0\\0&0\end{pmatrix}\otimes\begin{pmatrix}1&0\\0&1\end{pmatrix}
+\begin{pmatrix}0&0\\0&1\end{pmatrix}\otimes\begin{pmatrix}0&1\\1&0\end{pmatrix}
=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}.$$

Działanie: $\mathrm{CNOT}|10\rangle=|11\rangle$, $\mathrm{CNOT}|11\rangle=|10\rangle$
(kubit 0 się odwraca, bo kontrolny $=1$); $\mathrm{CNOT}|00\rangle=|00\rangle$,
$\mathrm{CNOT}|01\rangle=|01\rangle$ (kontrolny $=0$, nic się nie zmienia). Kwadrat:
$\mathrm{CNOT}^2=I$, więc bramka jest sama swoją odwrotnością.

**Wynik:** macierz jak wyżej; $\mathrm{CNOT}^2=I$; zamiana $|10\rangle\leftrightarrow|11\rangle$.

**Interpretacja:** CNOT jest unitarny i hermitowski; razem z bramkami jednoargumentowymi
tworzy podstawowy zestaw bramek uniwersalnych (rozdział 06).

### Przykład 3 (trudniejszy): ewolucja $e^{-iHt/\hbar}$ dla $H$ Hadamarda

**Dane:** $H=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ (bramka Hadamarda,
traktowana jako hamiltonian), $\hbar=1$, $t=\pi/4$.

**Metoda:** $H^2=I\Rightarrow e^{-iHt}=\cos(t)I-i\sin(t)H$.

**Rachunek:** $\cos(\pi/4)=\sin(\pi/4)=1/\sqrt2$,

$$e^{-iH\pi/4}=\tfrac{1}{\sqrt2}I-\tfrac{i}{\sqrt2}H
=\begin{pmatrix}\frac{1}{\sqrt2}-\frac{i}{2}&-\frac{i}{2}\\-\frac{i}{2}&\frac{1}{\sqrt2}+\frac{i}{2}\end{pmatrix}.$$

Wartości: przekątna $0{,}7071\mp0{,}5i$, pozadiagonalne $-0{,}5i$ ✓.

**Wynik:** $e^{-iH\pi/4}=\begin{pmatrix}0{,}7071-0{,}5i&-0{,}5i\\-0{,}5i&0{,}7071+0{,}5i\end{pmatrix}$.

**Interpretacja:** to unitarna bramka $2\times2$ — bezpośredni związek między
hermitowskim hamiltonianem a unitarną ewolucją; wykorzystamy to przy bramkach $R_X,R_Y,R_Z$.

## 5. Typowe pułapki

1. **Mylenie $A^\dagger$ z $A^T$.** Sprzężenie hermitowskie to sprzężenie zespolone
   **i** transpozycja.
2. **Odwrotna kolejność w kronie.** $A\otimes B\ne B\otimes A$; kolejność czynników
   koduje, na którym kubicie działa bramka.
3. **Zapominanie konwencji kubitów.** Bez jawnego stwierdzenia „kontrolny = górny”
   macierz CNOT bywa odwrotna. Zawsze deklaruj konwencję.
4. **Diagonalizacja macierzy niehermitowskiej przez `eigh`.** `numpy.linalg.eigh`
   zakłada hermitowskość; dla ogólnej macierzy użyj `eig`.
5. **Branie wartości własnych $e^{-iHt/\hbar}$ zamiast $e^{-iat/\hbar}$.** Najpierw
   diagonalizuj $H$, potem eksponuj **jego** wartości własne $a$.
6. **Mylenie rzędu z wyznacznikiem.** $\det A=0$ równoważne brakowi odwracalności i
   $\operatorname{rank}A<n$, ale mały wyznacznik nie znaczy „mały rząd”.

## 6. Zadania (Z-02)

**Z-02.1.** Dla $|u\rangle=(1,i)^T$, $|v\rangle=(i,1)^T$
(a) policz $\langle u|v\rangle$; (b) policz normy; (c) znormalizuj oba i rozpoznaj,
że są to stany własne $Y$.

**Z-02.2.** Operator $X$ w bazie obliczeniowej.
(a) Zapisz jego macierz. (b) Wyznacz macierz w bazie
$\{|\pm\rangle=(|0\rangle\pm|1\rangle)/\sqrt2\}$: $X'=U^\dagger XU$ z $U=[|+\rangle\ |-\rangle]$.
(c) Zinterpretuj wynik.

**Z-02.3.** Dana $M=\begin{pmatrix}2&1-i\\1+i&3\end{pmatrix}$.
(a) Wykaż hermitowskość. (b) Wyznacz wartości własne. (c) Wyznacz wektory własne i
zapisz rozkład spektralny; policz $\langle+|M|+\rangle$.

**Z-02.4.** Rozważ $R_Z(\theta)=e^{-i\theta Z/2}$.
(a) Dowiedź $R_Z(\theta)=\cos\frac\theta2 I-i\sin\frac\theta2 Z$.
(b) Wykaż unitarność. (c) Policz $R_Z(\pi/2)$ i jego działanie na $|0\rangle,|1\rangle$.

**Z-02.5.** Dana $M=\begin{pmatrix}2&0&1\\1&3&0\\0&1&1\end{pmatrix}$.
(a) Policz $\operatorname{Tr}M$. (b) Policz $\det M$. (c) Wyznacz
$\operatorname{rank}M$ i rozstrzygnij o odwracalności.

**Z-02.6.** Bramka CNOT (kontrolny = kubit 1).
(a) Zbuduj macierz z $|0\rangle\langle0|\otimes I+|1\rangle\langle1|\otimes X$.
(b) Wskaż obrazy $|00\rangle,|01\rangle,|10\rangle,|11\rangle$. (c) Wykaż
$\mathrm{CNOT}^2=I$ i unitarność.

**Z-02.7.** Macierze Pauliego.
(a) Policz $[X,Y],[Y,Z],[Z,X]$. (b) Policz $\{X,Y\}$ i $\{X,X\}$.
(c) Sprawdź wzór $\sigma_a\sigma_b=\delta_{ab}I+i\sum_c\varepsilon_{abc}\sigma_c$
na parze $(a,b)=(X,Y)$.

**Z-02.8. [★]** Stan $|\psi\rangle=\cos\alpha|00\rangle+\sin\alpha|11\rangle$,
$\alpha=0{,}6$.
(a) Wyznacz wartości Schmidta. (b) Policz entropię splątania
$S=-\sum_k s_k^2\log_2 s_k^2$. (c) Rozstrzygnij, dla jakich $\alpha$ stan jest iloczynowy.

## 7. Wskazówki do zadań

- **Z-02.1.** $\langle u|v\rangle=u_1^*v_1+u_2^*v_2$; do (c) działaj $Y$ na
  znormalizowane wektory.
- **Z-02.2.** $U=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$; licz $U^\dagger XU$.
- **Z-02.3.** $\det(M-aI)=a^2-5a+4$; wektory własne z $(M-aI)v=0$.
- **Z-02.4.** Użyj $Z^2=I$ i rozwinięcia $e^{-i\theta Z/2}$; w (c) uwzględnij fazę
  $e^{\mp i\pi/4}$.
- **Z-02.5.** Ślad = suma na przekątnej; wyznacznik rozwinięciem; rząd z eliminacji
  Gaussa lub `np.linalg.matrix_rank`.
- **Z-02.6.** Kron blokowy; zachowaj małoendianową kolejności baz.
- **Z-02.7.** Mnożenie macierzy $2\times2$; $\varepsilon_{XYZ}=+1$ cyklicznie.
- **Z-02.8.** [★] Macierz współczynników
  $\begin{pmatrix}\cos\alpha&0\\0&\sin\alpha\end{pmatrix}$;
  $s_1=|\cos\alpha|$, $s_2=|\sin\alpha|$; iloczynowość, gdy jedna z nich znika.

## 8. Co dalej

Algebra liniowa jest podstawą dalszych rozdziałów: statystyki pomiarów w rozdziale
[03](03-rachunek-prawdopodobienstwa-i-statystyka.md), równania Schrödingera w
[04](04-elementy-analizy-matematycznej.md) i mechaniki kwantowej w
[05](05-podstawy-mechaniki-kwantowej.md). Rozkład Schmidta rozwija
[rozdział 09](09-splatanie-i-twierdzenie-bella.md). Rozwiązania zadań są w
[rozwiazania-02.md](../zadania/rozwiazania/rozwiazania-02.md); zadania łączące
rozdziały 01–05 to [PD-1](../praca-domowa/praca-domowa-01.md).

Konwencja kubitów wg [konwencji](../docs/03-konwencje-i-notacja.md).
