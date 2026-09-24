# Rozwiązania modelowe zadań przykładowych P1–P4

Treść zadań pochodzi z oficjalnego arkusza „Zadania przykładowe”
Olimpiady Kwantowej (<https://olimpiadakwantowa.pl/zadania/>).

---

## P1. Cząstka w nieskończonej studni potencjału

**Dane:** $\psi_n(x)=\sqrt{2/L}\sin(n\pi x/L)$, $E_n=\frac{n^2\pi^2\hbar^2}{2mL^2}$,
stan $\psi=\frac{1}{\sqrt5}(2\psi_1+\psi_2)$.

**Kluczowa własność (ortogonalność i normalizacja stanów własnych):**

$$
\langle\psi_m\vert\psi_n\rangle=\int_0^L\psi_m(x)\psi_n(x)\,dx=\delta_{mn}
=\begin{cases}1,&m=n\\0,&m\ne n\end{cases}
$$

### (a) Normalizacja

$$
\langle\psi\vert\psi\rangle=\frac{1}{5}\Big\langle 2\psi_1+\psi_2\Big\vert 2\psi_1+\psi_2\Big\rangle
=\frac{1}{5}\Big(4\underbrace{\langle\psi_1\vert\psi_1\rangle}_{1}
+4\underbrace{\langle\psi_1\vert\psi_2\rangle}_{0}
+\underbrace{\langle\psi_2\vert\psi_2\rangle}_{1}\Big)
=\frac{4+1}{5}=1.
$$

**Stan jest unormowany.** ✔ (Numerycznie: $\int\psi^2dx=1{,}000000$.)

### (b) Prawdopodobieństwa w pomiarze energii

Rozkładamy stan na stany własne: $\psi=c_1\psi_1+c_2\psi_2$ z
$c_1=\frac{2}{\sqrt5}$, $c_2=\frac{1}{\sqrt5}$.

$$
P(E_n)=\lvert c_n\rvert^2\ \Rightarrow\
\boxed{P(E_1)=\frac{4}{5}=0{,}8,\qquad P(E_2)=\frac{1}{5}=0{,}2}
$$

Kontrola: $P(E_1)+P(E_2)=0{,}8+0{,}2=1$. ✔
Fizycznie: pomiar energii **nigdy** nie da innego wyniku niż $E_1$ lub $E_2$ — stan
jest superpozycją dokładnie dwóch stanów własnych.

### (c) Wartość oczekiwana energii

$$
\langle E\rangle=\sum_n\lvert c_n\rvert^2E_n=\frac45E_1+\frac15E_2
=\frac45E_1+\frac15\cdot 4E_1=\frac85E_1.
$$

$$
\boxed{\langle E\rangle=\frac85\cdot\frac{\pi^2\hbar^2}{2mL^2}
=\frac{4\pi^2\hbar^2}{5mL^2}\approx 7{,}896\,\frac{\hbar^2}{mL^2}}
$$

**Interpretacja.** $\langle E\rangle$ **nie** jest energią zmierzoną w jednym
doświadczeniu — to średnia z wielu pomiarów na identycznie przygotowanym stanie.
Sprawdzenie innego wzoru: $\langle E\rangle=\langle\psi\vert\hat H\vert\psi\rangle$
daje to samo, bo $E_1<E_2$ i każdy pomiar daje wartość własną.

### Rozszerzenie (d) — dodatkowa kontrola spójności

Wartość oczekiwana położenia z definicji $\langle x\rangle=(1/5)(4\langle x\rangle_{11} +\langle x\rangle_{22}+4\langle x\rangle_{12})$, gdzie
$\langle x\rangle_{nn}=L/2$ oraz

$$
\langle x\rangle_{12}=\int_0^L x\psi_1\psi_2\,dx=-\frac{16L}{9\pi^2}\approx-0{,}1801\,L .
$$

Stąd

$$
\langle x\rangle=\frac{1}{5}\left(4\cdot\frac L2+\frac L2-\frac{64L}{9\pi^2}\right)
=\frac{L}{2}-\frac{64L}{45\pi^2}\approx\boxed{0{,}3559\,L}.
$$

Wynik jest mniejszy od $L/2$ — dodanie $\psi_2$ (nieparzystej względem środka studni)
przesuwa gęstość prawdopodobieństwa w lewo. Dla porównania, sam $\psi_1$ dawałby
$\langle x\rangle=L/2$. ✔ (Sprawdzone numerycznie: $0{,}355899\,L$.)

---

## P2. Polaryzatory i pojedynczy foton

**Prawo Malusa dla natężenia:** $I=I_{\text{in}}\cos^2\alpha$, gdzie $\alpha$ to kąt
między kierunkiem polaryzacji światła padającego a osią przepuszczania polaryzatora.
**Po przejściu** przez polaryzator światło jest spolaryzowane **zgodnie z jego osią** —
dlatego przy kolejnych elementach liczymy kąty **między sąsiednimi elementami**.

### (a) Układ $P_1$ ($45^\circ$) → $P_2$ ($90^\circ$)

- Wiązka wejściowa: pozioma ($0^\circ$), natężenie $I_0$.
- $P_1$ pod $45^\circ$: $\alpha_1=45^\circ$,
  $I_1=I_0\cos^2 45^\circ=\dfrac{I_0}{2}$.
  Światło wychodzi spolaryzowane pod $45^\circ$.
- $P_2$ pionowy ($90^\circ$): kąt względem światła padającego to $90^\circ-45^\circ=45^\circ$,
  $I_{wy}=I_1\cos^2 45^\circ=\dfrac12\cdot\dfrac{I_0}{2}$.

$$
\boxed{I_{wy}=\frac{I_0}{4}}
$$

### (b) Usunięcie $P_1$

Światło jest znowu poziome i pada bezpośrednio na polaryzator pionowy:
$\alpha=90^\circ$, więc

$$
\boxed{I_{wy}=I_0\cos^2 90^\circ=0}
$$

**Komentarz.** Wynik jest zaskakujący tylko na pierwszy rzut oka: „wstawienie
polaryzatora w środku **zwiększyło** natężenie przechodzącego światła z $0$ do
$I_0/4$”. Wyjaśnienie: polaryzator $P_1$ **nie przepuszcza** światła poziomego —
on je **rzutuje** na kierunek $45^\circ$ i wypuszcza już spolaryzowane pod $45^\circ$.
Składowa pionowa światła „odtworzyła się” w wyniku pomiaru. To kwantowy efekt
rzutowania stanu, którego nie ma w klasycznym opisie fali. (Znany „paradoks trzech
polaryzatorów”: $0^\circ$ → $45^\circ$ → $90^\circ$ daje $I_0/8$ na każdym
skręceniu o kolejne $45^\circ$.)

### (c) Pojedynczy foton — to samo w języku kwantowym

Foton poziomy: $\lvert H\rangle$. Polaryzator pod kątem $\alpha$ realizuje pomiar
w bazie obróconej o $\alpha$:

$$
\lvert H\rangle=\cos\alpha\,\lvert\alpha\rangle-\sin\alpha\,\lvert\alpha_\perp\rangle
\ \Rightarrow\ P(\text{przejście})=\cos^2\alpha .
$$

- Przez $P_1$: $P_1=\cos^2 45^\circ=1/2$. Foton przechodzi i **jest** teraz w stanie
  $\lvert45^\circ\rangle$.
- Przez $P_2$: kąt między $\lvert45^\circ\rangle$ a osią pionową to $45^\circ$,
  $P_2=\cos^2 45^\circ=1/2$.

$$
P(\text{przejście przez cały układ})=P_1\cdot P_2=\frac12\cdot\frac12
\quad\Rightarrow\quad\boxed{P=\frac14}
$$

Po usunięciu $P_1$: foton poziomy pada na polaryzator pionowy:
$P=\lvert\langle V\vert H\rangle\rvert^2=\cos^2 90^\circ$
$\Rightarrow$ $\boxed{P=0}$.

**Interpretacja.** Ten sam wynik co dla natężenia, bo dla pojedynczego fotonu
natężenie wiązki jest proporcjonalne do częstości przejść: $I/I_0=P$. To pokazuje,
że klasyczne prawo Malusa jest konsekwencją prawdopodobieństw kwantowych, a nie
osobnym prawem. (Sprawdzenie numeryczne: `python kod/p2_polaryzatory.py`.)

---

## P3. Bramki H, Z, H na kubicie

**Konwencja:** $\lvert0\rangle=\binom10$, $\lvert1\rangle=\binom01$; bramka
wykonana jako pierwsza stoi najbliżej wektora, czyli
$\lvert\psi_3\rangle=HZH\lvert0\rangle$.

### (a) Stan przed pomiarem i prawdopodobieństwa

Krok 1 — bramka $H$ na $\lvert0\rangle$:

$$
H\lvert0\rangle=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\binom10
=\frac{1}{\sqrt2}\binom11=\lvert+\rangle .
$$

Krok 2 — bramka $Z$:

$$
Z\lvert+\rangle=\frac{1}{\sqrt2}\begin{pmatrix}1&0\\0&-1\end{pmatrix}\binom11
=\frac{1}{\sqrt2}\binom1{-1}=\lvert-\rangle .
$$

Krok 3 — bramka $H$:

$$
H\lvert-\rangle=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}\binom1{-1}
=\frac12\binom02=\binom01=\lvert1\rangle .
$$

$$
\boxed{\lvert\psi_3\rangle=\lvert1\rangle}
$$

Ponieważ $\lvert\psi_3\rangle$ jest stanem własnym pomiaru, wynik jest
**deterministyczny**:

$$
\boxed{P(0)=\lvert\langle0\vert1\rangle\rvert^2=0,\qquad P(1)=\lvert\langle1\vert1\rangle\rvert^2=1}
$$

To ważna obserwacja: sekwencja $H,Z,H$ zamienia $\lvert0\rangle$ na $\lvert1\rangle$
z prawdopodobieństwem 1 — nie ma tu żadnej losowości.

### (b) Czym jest $HZH$?

$$
ZH=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\cdot\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}
=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix},
$$

$$
HZH=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\cdot
\frac{1}{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}
=\frac12\begin{pmatrix}0&2\\2&0\end{pmatrix}
=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

$$
\boxed{HZH=X}
$$

To szczególny przypadek ogólnej reguły sprzężenia operatorem Hadamarda:
$HXH=Z$, $HYH=-Y$, $HZH=X$ (a także $H=\frac{1}{\sqrt2}(X+Z)$). Geometrycznie $H$
zamienia osie $x\leftrightarrow z$ sfery Blocha.

**Kontrola krzyżowa:** $HZH\lvert0\rangle=X\lvert0\rangle=\lvert1\rangle$ — zgadza
się z wynikiem (a). ✔ (Numerycznie: `python kod/p3_hzh.py`.)

---

## P4. Obwód dwukubitowy z $R_Y(\theta)$ i CNOT

**Konwencja.** Stan zapisujemy jako $\lvert q_1q_0\rangle$ (indeks binarny $2q_1+q_0$):

$$
\lvert00\rangle=\begin{pmatrix}1\\0\\0\\0\end{pmatrix},\quad
\lvert01\rangle=\begin{pmatrix}0\\1\\0\\0\end{pmatrix},\quad
\lvert10\rangle=\begin{pmatrix}0\\0\\1\\0\end{pmatrix},\quad
\lvert11\rangle=\begin{pmatrix}0\\0\\0\\1\end{pmatrix}.
$$

Bramka na $q_1$ to $H\otimes I$, bramka na $q_0$ to $I\otimes R_Y(\theta)$.
CNOT (kontrola $q_1$, cel $q_0$) nie zmienia $q_1$ i dodaje $q_1$ do $q_0$ modulo 2.

### Krok 1 — bramka $H$ na $q_1$

$$
(H\otimes I)\lvert00\rangle=\lvert+\rangle\otimes\lvert0\rangle
=\frac{1}{\sqrt2}\big(\lvert00\rangle+\lvert10\rangle\big).
$$

### Krok 2 — bramka $R_Y(\theta)$ na $q_0$

Korzystamy z $R_Y(\theta)\lvert0\rangle=\cos\frac\theta2\lvert0\rangle+\sin\frac\theta2\lvert1\rangle$:

$$
\lvert\psi_2\rangle=\frac{1}{\sqrt2}\Big[\cos\frac\theta2\big(\lvert00\rangle+\lvert10\rangle\big)
+\sin\frac\theta2\big(\lvert01\rangle+\lvert11\rangle\big)\Big].
$$

### Krok 3 — CNOT

Działanie CNOT: $\lvert q_1q_0\rangle\to\lvert q_1,\ q_0\oplus q_1\rangle$, czyli
$\lvert00\rangle\to\lvert00\rangle$, $\lvert01\rangle\to\lvert01\rangle$,
$\lvert10\rangle\to\lvert11\rangle$, $\lvert11\rangle\to\lvert10\rangle$. Zatem

$$
\boxed{\lvert\psi_3\rangle=\frac{1}{\sqrt2}\Big[
\cos\frac\theta2\lvert00\rangle+\sin\frac\theta2\lvert01\rangle
+\sin\frac\theta2\lvert10\rangle+\cos\frac\theta2\lvert11\rangle\Big]}
$$

| stan bazowy | amplituda |
| --- | --- |
| $\lvert00\rangle$ | $\cos\frac\theta2/\sqrt2$ |
| $\lvert01\rangle$ | $\sin\frac\theta2/\sqrt2$ |
| $\lvert10\rangle$ | $\sin\frac\theta2/\sqrt2$ |
| $\lvert11\rangle$ | $\cos\frac\theta2/\sqrt2$ |

### (a, c.d.) Czy stan $\lvert\psi_3\rangle$ jest splątany?

Zapiszmy amplitudy jako macierz $2\times2$: wiersze indeksuje $q_1$, kolumny $q_0$:

$$
C=\frac{1}{\sqrt2}\begin{pmatrix}
\cos\frac\theta2 & \sin\frac\theta2\\[2pt]
\sin\frac\theta2 & \cos\frac\theta2\end{pmatrix},
\qquad
\det C=\frac12\left(\cos^2\frac\theta2-\sin^2\frac\theta2\right)=\frac{\cos\theta}{2}.
$$

Stan jest **iloczynowy** wtedy i tylko wtedy, gdy $\det C=0$, czyli gdy
$\cos\theta=0$. Sprawdzenie wprost: dla $\theta=\frac\pi2$ otrzymujemy
$\lvert\psi_3\rangle=\lvert+\rangle\otimes\lvert+\rangle$, bo $\lvert++\rangle$ jest
stanem własnym CNOT-a z wartością własną $+1$ (CNOT go nie zmienia).

$$
\boxed{\text{Splątany dla }\theta\ne\frac\pi2,\ \frac{3\pi}2;\quad
\text{iloczynowy dla }\theta=\frac\pi2\ (\mathrm{mod}\ \pi)}
$$

Szczególne przypadki maksymalnego splątania:
- $\theta=0$: $\lvert\psi_3\rangle=\frac{1}{\sqrt2}(\lvert00\rangle+\lvert11\rangle)=\lvert\Phi^+\rangle$;
- $\theta=\pi$: $\lvert\psi_3\rangle=\frac{1}{\sqrt2}(\lvert01\rangle+\lvert10\rangle)=\lvert\Psi^+\rangle$.

### (b) Prawdopodobieństwa $P_{00},P_{01},P_{10},P_{11}$

Prawdopodobieństwo stanu bazowego to kwadrat modułu amplitudy:

$$
P_{ij}=\lvert\langle ij\vert\psi_3\rangle\rvert^2
\quad\Longrightarrow\quad
\boxed{P_{00}=P_{11}=\frac12\cos^2\frac\theta2,\qquad
P_{01}=P_{10}=\frac12\sin^2\frac\theta2}
$$

**Dowód, że suma wynosi 1** (jedynka trygonometryczna
$\cos^2\frac\theta2+\sin^2\frac\theta2=1$):

$$
P_{00}+P_{01}+P_{10}+P_{11}
=\tfrac12\cos^2\tfrac\theta2+\tfrac12\sin^2\tfrac\theta2
+\tfrac12\sin^2\tfrac\theta2+\tfrac12\cos^2\tfrac\theta2
=\cos^2\tfrac\theta2+\sin^2\tfrac\theta2=1 .\ \checkmark
$$

Kontrola numeryczna dla $\theta=0{,}7$:
$(P_{00},P_{01},P_{10},P_{11})=(0{,}441211;\ 0{,}058789;\ 0{,}058789;\ 0{,}441211)$,
suma $=1{,}000000$. ✔

### (c) Prawdopodobieństwo zgodnych wyników i $\langle Z\otimes Z\rangle$

Operator $Z$ daje $+1$ dla $\lvert0\rangle$ i $-1$ dla $\lvert1\rangle$. Wyniki są
**zgodne** dla $\lvert00\rangle$ i $\lvert11\rangle$, więc

$$
P_{\text{zgodne}}=P_{00}+P_{11}=\cos^2\frac\theta2=\frac{1+\cos\theta}{2}.
$$

Z definicji wartości oczekiwanej dla $\langle Z\otimes Z\rangle$:

$$
\langle Z\otimes Z\rangle
=P_{00}\,(+1)(+1)+P_{01}\,(+1)(-1)+P_{10}\,(-1)(+1)+P_{11}\,(-1)(-1)
$$

$$
=P_{00}+P_{11}-P_{01}-P_{10}
=\cos^2\frac\theta2-\sin^2\frac\theta2=\cos\theta .
$$

$$
\boxed{P_{\text{zgodne}}=\cos^2\frac\theta2=\frac{1+\cos\theta}{2},\qquad
\langle Z\otimes Z\rangle=\cos\theta}
$$

Kontrola spójności: $P_{\text{zgodne}}=\frac{1+\langle Z\otimes Z\rangle}{2}$ — dla
$\pm1$-wymiarowych wyników to zawsze prawda. ✔

**Komentarz do $\theta=0$ i $\theta=\pi$:**

| $\theta$ | stan | $P_{\text{zgodne}}$ | $\langle Z\otimes Z\rangle$ | interpretacja |
| --- | --- | --- | --- | --- |
| $0$ | $\lvert\Phi^+\rangle$ (Bella) | $1$ | $+1$ | wyniki **zawsze** zgodne |
| $\pi/2$ | $\lvert+\rangle\lvert+\rangle$ | $1/2$ | $0$ | **brak** korelacji (stan iloczynowy) |
| $\pi$ | $\lvert\Psi^+\rangle$ (Bella) | $0$ | $-1$ | wyniki **zawsze** przeciwne |

Dla $\theta=0$ i $\theta=\pi$ mamy więc **idealne korelacje** przy **zerowej
informacji lokalnej**: pojedynczy pomiar na $q_1$ daje wynik losowy (pół na pół),
ale po poznaniu tego wyniku wynik na $q_0$ jest już pewny. To jest istota splątania
i zasób wykorzystywany przez teleportację, supergęste kodowanie oraz protokół E91.

**Uwaga o konwencji kąta.** Gdyby ktoś zapisał $R_Y$ **bez** dzielenia $\theta/2$
(tzn. jak klasyczną macierz obrotu o kąt $\theta$), wyniki zmieniłyby się na
$P_{\text{zgodne}}=\frac{1+\cos2\theta}{2}$ i $\langle Z\otimes Z\rangle=\cos2\theta$.
Zawsze sprawdzaj definicję bramki podaną w zadaniu — tutaj jest jawnie $\theta/2$. ✔

(Weryfikacja numeryczna: `python kod/p4_cnot_ry.py`.)



