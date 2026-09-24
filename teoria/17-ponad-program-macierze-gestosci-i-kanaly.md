# 17. Macierze gęstości i kanały kwantowe


## 1. Zakres rozdziału

Rozdział obejmuje opis stanu kwantowego w języku **macierzy gęstości** (*density matrix*) $\rho$ i
**kanałów kwantowych** (*quantum channel*): ślad częściowy, rozkład Schmidta, purity i wektor
Blocha, pomiar uogólniony (POVM), reprezentację Krausa i macierz $\chi$. Do formalizmu prowadzą
trzy sytuacje, w których wektor stanu nie wystarcza: **ignorancja** (klasyczna niepewność, który
stan przygotowano), **splątanie** (stan podukładu jest mieszany) oraz **szum i dekoherencja**
(oddziaływanie z otoczeniem).

Druga grupa zagadnień to kanały unitarny, depolaryzujący, tłumienia amplitudowego i przesunięcia
fazy oraz miary odległości stanów: wierność, odległość śladowa i nierówność Fuchsa–van de Graafa.

Materiał stanowi podstawę [rozdziału 13](13-korekcja-i-mitygacja-bledow.md) (mitygacja błędów),
[rozdziału 18](18-ponad-program-splatanie-dekoherencja-termodynamika.md) ($T_1/T_2$, entropia
splątania) i twierdzenia Holevo z
[rozdziału 19](19-ponad-program-algorytmy-zaawansowane-i-granice.md); definicje są ilustrowane
rachunkami na liczbach (ślad częściowy $\lvert\Phi^+\rangle$, kanał depolaryzujący, tłumienie
amplitudowe, wierność i odległość śladowa).

## 2. Najważniejsze definicje

- **Stan czysty (pure state)**: $\rho=\lvert\psi\rangle\langle\psi\rvert$; wtedy $\mathrm{Tr}\,\rho^2=1$.
- **Stan mieszany (mixed state)**: $\rho=\sum_k p_k\lvert\psi_k\rangle\langle\psi_k\rvert$, $p_k\ge0$, $\sum_k p_k=1$; $\mathrm{Tr}\,\rho^2<1$.
- **Własności $\rho$**: hermitowskość $\rho^\dagger=\rho$, $\mathrm{Tr}\,\rho=1$, dodatniość $\rho\succeq0$ (nieujemne wartości własne).
- **Rozkład spektralny**: $\rho=\sum_i\lambda_i\lvert i\rangle\langle i\rvert$, $\lambda_i\ge0$, $\sum_i\lambda_i=1$; liczby $\lambda_i$ to **populacje**.
- **Purity**: $\gamma=\mathrm{Tr}\,\rho^2=\sum_i\lambda_i^2$; $1$ dla czystego, $1/d$ dla maksymalnie mieszanego.
- **Wektor Blocha $\vec r$**: $\rho=\tfrac12(I+\vec r\cdot\vec\sigma)$; $\lvert\vec r\rvert\le1$ (równość $\Leftrightarrow$ stan czysty).
- **Ślad częściowy (partial trace)** $\mathrm{Tr}_B$: „zapomnienie” o podukładzie $B$; $\rho_A=\mathrm{Tr}_B\rho_{AB}$.
- **Macierz zredukowana (reduced state)** $\rho_A$: stan podukładu $A$ samego.
- **Rozkład Schmidta**: $\lvert\psi\rangle_{AB}=\sum_i\sqrt{\lambda_i}\lvert a_i\rangle\lvert b_i\rangle$; liczba niezerowych $\lambda_i$ = **rząd Schmidta**.
- **Entropia splątania**: $S(\rho_A)=-\mathrm{Tr}\,\rho_A\log_2\rho_A$ (patrz rozdział 18).
- **Oczyszczenie (purification)**: każdy $\rho_A$ można rozszerzyć do czystego $\lvert\psi\rangle_{AR}$.
- **Pomiar uogólniony (POVM)**: zbiór $\{M_i\}$ z $\sum_i M_i^\dagger M_i=I$ (pomiar rzutowy: $M_i=P_i$, $P_i^2=P_i$).
- **Kanał kwantowy** $\mathcal E$: liniowa, całkowicie dodatnia, zachowująca ślad (CPTP) mapa operatorów gęstości.
- **Reprezentacja Krausa**: $\mathcal E(\rho)=\sum_i K_i\rho K_i^\dagger$, z warunkiem $\sum_i K_i^\dagger K_i=I$.
- **Kanał unitarny**: $\mathcal E(\rho)=U\rho U^\dagger$ — przypadek odwracalny ($K_1=U$).
- **Kanał depolaryzujący**: $D_p(\rho)=(1-p)\rho+p\,\tfrac I2$ (z prawdopodobieństwem $p$ stan „zapomina” kierunek).
- **Tłumienie amplitudowe (amplitude damping)**: relaksacja $\lvert1\rangle\to\lvert0\rangle$ z prawdopodobieństwem $\gamma$ (model $T_1$).
- **Przesunięcie fazy / dekoherencja fazowa (dephasing)**: zanik elementów pozadiagonalnych (model $T_2$).
- **Macierz $\chi$ (process matrix)**: $\mathcal E(\rho)=\sum_{mn}\chi_{mn}P_m\rho P_n$ w bazie Pauliego $\{P_0=I,X,Y,Z\}$.
- **Odległość śladowa (trace distance)**: $D(\rho,\sigma)=\tfrac12\mathrm{Tr}\lvert\rho-\sigma\rvert$; **wierność** $F(\rho,\sigma)=\big(\mathrm{Tr}\sqrt{\sqrt\rho\,\sigma\sqrt\rho}\big)^2$.
- **Nierówność Fuchsa–van de Graafa**: $1-\sqrt F(\rho,\sigma)\le D(\rho,\sigma)\le\sqrt{1-F(\rho,\sigma)}$.

## 3. Teoria krok po kroku

### 3.1 Dlaczego wektor nie wystarcza

Wyobraźmy sobie, że ktoś rzuca monetą: z prawdopodobieństwem $\tfrac12$ przygotowuje
$\lvert0\rangle$, z $\tfrac12$ — $\lvert1\rangle$, ale **nie mówi nam, co wypadło**. Nie istnieje
wektor $\lvert\psi\rangle$ opisujący naszą wiedzę: każdy pomiar w bazie $X$ dałby dla stanu
czystego jednoznaczny wynik, a my dostajemy losowo $0$ lub $1$. Zbiór możliwych statystyk opisuje
**macierz**:

$$
\rho=\tfrac12\lvert0\rangle\langle0\rvert+\tfrac12\lvert1\rangle\langle1\rvert=\tfrac12 I .
$$

Ta sama macierz pojawia się, gdy bierzemy **ślad częściowy** stanu splątanego — ignorancja i
splątanie prowadzą do identycznego formalizmu.

### 3.2 Macierz gęstości: definicja i własności

$$
\rho=\sum_k p_k\lvert\psi_k\rangle\langle\psi_k\rvert .
$$

Trzy warunki ($\rho^\dagger=\rho$, $\mathrm{Tr}\rho=1$, $\rho\succeq0$) są **konieczne i wystarczające**,
by $\rho$ opisywał jakiś stan. Wartość oczekiwana obserwabli i prawdopodobieństwo wyniku to

$$
\langle A\rangle=\mathrm{Tr}(\rho A),\qquad P(m)=\mathrm{Tr}(P_m\rho),\qquad P_m=\lvert m\rangle\langle m\rvert .
$$

Czystość stanu mierzymy przez $\mathrm{Tr}\,\rho^2$: równa $1$ tylko dla stanu czystego.

### 3.3 Rozkład spektralny i oczyszczenie

Ponieważ $\rho$ jest hermitowska i dodatnia, ma rozkład własny

$$
\rho=\sum_i\lambda_i\lvert i\rangle\langle i\rvert,\qquad \lambda_i\ge0,\quad\sum_i\lambda_i=1 .
$$

Ten sam $\rho$ ma **nieskończenie wiele** rozkładów na stany czyste (np. $\tfrac12I$ z dowolnej
bazy), ale **jedno** widmo — dlatego wszystkie miary oparte na wartościach własnych (entropia,
purity) są dobrze określone. **Oczyszczenie**: każdy stan mieszany
$\rho_A=\sum_i\lambda_i\lvert i\rangle\langle i\rvert$ można przedstawić jako ślad częściowy stanu
czystego

$$
\lvert\psi\rangle_{AR}=\sum_i\sqrt{\lambda_i}\,\lvert i\rangle_A\lvert i\rangle_R .
$$

Kluczowy wniosek: **każdy szum można potraktować jako splątanie z otoczeniem**.

### 3.4 Sfera Blocha dla jednego kubita

Każdą macierz $2\times2$ rozkładamy w bazie $\{I,\sigma_x,\sigma_y,\sigma_z\}$:

$$
\rho=\tfrac12\big(I+r_x\sigma_x+r_y\sigma_y+r_z\sigma_z\big),\qquad \vec r\cdot\vec\sigma=\sum_j r_j\sigma_j .
$$

**Skąd to się bierze:** identyczność $\mathrm{Tr}\,\sigma_j=0$ i $\mathrm{Tr}(\sigma_j\sigma_k)=2\delta_{jk}$
dają $r_j=\mathrm{Tr}(\rho\sigma_j)$; z tego natychmiast

$$
r_x=2\,\mathrm{Re}\,\rho_{01},\qquad r_y=-2\,\mathrm{Im}\,\rho_{01},\qquad r_z=\rho_{00}-\rho_{11}.
$$

Sprawdzenie dodatniości: $\det\rho=\tfrac14(1-\lvert\vec r\rvert^2)\ge0$, więc $\lvert\vec r\rvert\le1$.
Stan czysty $\Leftrightarrow\lvert\vec r\rvert=1$ (punkt na sferze Blocha).

### 3.5 Ślad częściowy

Dla $\rho_{AB}$ w bazie $\{\lvert i\rangle_A\lvert j\rangle_B\}$ definiujemy

$$
(\rho_A)_{ii'}=\sum_j(\rho_{AB})_{ij,i'j}=\mathrm{Tr}_B\,\rho_{AB}.
$$

**Przykład fundamentalny.** Dla $\lvert\Phi^+\rangle=\tfrac{1}{\sqrt2}(\lvert00\rangle+\lvert11\rangle)$
macierz $\rho=\lvert\Phi^+\rangle\langle\Phi^+\rvert$ ma niezerowe elementy $(0,0),(0,3),(3,0),(3,3)=1/2$.
Sumując po indeksie $B$:

$$
\rho_A=\begin{pmatrix}\rho_{00,00}+\rho_{01,01}&\rho_{00,10}+\rho_{01,11}\\ \rho_{10,00}+\rho_{11,01}&\rho_{10,10}+\rho_{11,11}\end{pmatrix}
=\begin{pmatrix}\tfrac12&0\\0&\tfrac12\end{pmatrix}=\tfrac I2 .
$$

Stan czysty dwóch kubitów, po „zapomnieniu” jednego, daje **maksymalnie mieszany** kubit
($\mathrm{Tr}\,\rho_A^2=\tfrac12$, $\lvert\vec r\rvert=0$). To ilościowa twarz splątania.

### 3.6 Rozkład Schmidta i entropia splątania

Każdy stan dwóch układów można zapisać (tw. Schmidta) jako
$\lvert\psi\rangle_{AB}=\sum_i\sqrt{\lambda_i}\lvert a_i\rangle\lvert b_i\rangle$ z $\lambda_i\ge0$,
$\sum_i\lambda_i=1$. Wartości $\lambda_i$ to **jednocześnie** wartości własne $\rho_A$ i $\rho_B$;
liczba niezerowych = **rząd Schmidta**. Jeśli rząd $=1$, stan jest iloczynowy (brak splątania).
Entropia splątania $S(\rho_A)=-\sum_i\lambda_i\log_2\lambda_i$ jest zero dla stanów iloczynowych,
a równa $\log_2 d$ dla maksymalnego splątania w wymiarze $d$.

### 3.7 Pomiar opisany macierzą gęstości

Pomiar rzutowy w bazie $\{\lvert m\rangle\}$: $P(m)=\mathrm{Tr}(P_m\rho)$, a po pomiarze stan
$\rho\to P_m\rho P_m/P(m)$ (**kolaps**). Pomiar **uogólniony (POVM)** to zbiór $\{M_i\}$ z
$\sum_iM_i^\dagger M_i=I$; wtedy $P(i)=\mathrm{Tr}(M_i^\dagger M_i\rho)$. POVM obejmuje pomiar
rzutowy, ale też „niekonkluzywny” (np. B92 z rozdziału 10) i pomiar z błędem odczytu.

### 3.8 Kanały kwantowe i twierdzenie Krausa

**Kanał** to dowolna fizyczna ewolucja: bramka, pomiar, szum, oddziaływanie z otoczeniem. Formalnie
$\mathcal E$ jest **liniowa**, **całkowicie dodatnia** (CP — *completely positive*: dodatnia także
po rozszerzeniu o dowolny układ pomocniczy) i **zachowująca ślad** (TP — *trace preserving*).

**Twierdzenie Krausa (operator-sum).** $\mathcal E$ jest CPTP **wtedy i tylko wtedy**, gdy istnieją
operatory $K_i$ (operatory Krausa) takie, że

$$
\mathcal E(\rho)=\sum_i K_i\,\rho\,K_i^\dagger,\qquad \sum_i K_i^\dagger K_i=I .
$$

Warunek unitalności ($\sum_iK_iK_i^\dagger=I$) zachodzi np. dla kanału unitarnego i
depolaryzującego; dla tłumienia amplitudowego **nie** zachodzi. Liczba operatorów Krausa zależy od
reprezentacji, ale **kanał** jest ten sam. Każdy kanał można „rozluźnić” do
unitarności na większej przestrzeni ($\mathcal E(\rho)=\mathrm{Tr}_E\,U(\rho\otimes\lvert0\rangle\langle0\rvert)U^\dagger$).

### 3.9 Cztery kanały, które trzeba znać

| Kanał | Działanie | Operatory Krausa | Model fizyczny |
| --- | --- | --- | --- |
| depolaryzujący | $(1-p)\rho+p\tfrac I2$ | $\sqrt{1-\tfrac{3p}4}I,\ \sqrt{\tfrac p4}X,\ \sqrt{\tfrac p4}Y,\ \sqrt{\tfrac p4}Z$ | szum „bez kierunku” |
| tłumienie amplitudowe | $\lvert1\rangle\to\lvert0\rangle$ z p-stwem $\gamma$ | operatory Krausa $K_0$, $K_1$ | relaksacja $T_1$ |
| przesunięcie fazy | zanik $\rho_{01}$ o czynnik $(1-\lambda)$ | $\sqrt{1-\tfrac\lambda2}I,\ \sqrt{\tfrac\lambda2}Z$ | dekoherencja $T_2$ |
| bit-flip | $(1-p)\rho+p\,X\rho X$ | $\sqrt{1-p}I,\ \sqrt p\,X$ | błąd bitu |

$$
K_0=\begin{pmatrix}1&0\\0&\sqrt{1-\gamma}\end{pmatrix},\qquad
K_1=\begin{pmatrix}0&\sqrt\gamma\\0&0\end{pmatrix}
$$

Dla depolaryzującego $\sum K_i^\dagger K_i=(1-\tfrac{3p}4)+3\cdot\tfrac p4=1$; dla tłumienia
amplitudowego $K_0^\dagger K_0+K_1^\dagger K_1=\mathrm{diag}(1,1-\gamma)+\mathrm{diag}(0,\gamma)=I$.

### 3.10 Składanie kanałów i macierz $\chi$

Złożenie dwóch kanałów $\mathcal E=\mathcal E_2\circ\mathcal E_1$ to złożenie ich operatorów Krausa
indeksowane parami; dla kanałów „o jednym parametrze” często dostajemy kanał tego samego typu:

$$
D_{p_1}\circ D_{p_2}=D_{p},\qquad (1-p)=(1-p_1)(1-p_2).
$$

Dla tłumienia amplitudowego $(1-\gamma)=(1-\gamma_1)(1-\gamma_2)$ — to sedno wykładniczego zaniku
$T_1$. Alternatywny opis to **macierz $\chi$**: rozwijamy $\rho$ i $\mathcal E(\rho)$ w bazie
Pauliowskiej $\{P_0,\dots,P_3\}=\{I,X,Y,Z\}$ i piszemy

$$
\mathcal E(\rho)=\sum_{m,n=0}^{3}\chi_{mn}\,P_m\,\rho\,P_n .
$$

np. bit-flip o prawdopodobieństwie $p$ ma $\chi=\mathrm{diag}(1-p,\ p,\ 0,\ 0)$.

### 3.11 Kanały a splątanie: dekoherencja

Jeśli poddamy jeden kubit pary Bella kanałowi tłumienia fazy z $\lambda=1-e^{-t/T_2}$, to
koherencje $\rho_{01},\rho_{10}$ znikają jak $e^{-t/T_2}$, a splątanie maleje. Kanał depolaryzujący
z parametrem $p$ **skaluje wektor Blocha** danego kubita: $\vec r\to(1-p)\vec r$, więc maleje też
widzialność korelacji — w rozdziale 18 policzymy z tego spadek $S$ w nierówności CHSH.

Dwie metryki odległości między stanami:

$$
D(\rho,\sigma)=\tfrac12\mathrm{Tr}\lvert\rho-\sigma\rvert,\qquad
F(\rho,\sigma)=\Big(\mathrm{Tr}\sqrt{\sqrt\rho\,\sigma\sqrt\rho}\Big)^2 .
$$

$D=0\Leftrightarrow\rho=\sigma$, $D=1$ dla stanów ortogonalnych (nośniki rozłączne). **Nierówność
Fuchsa–van de Graafa** $1-\sqrt F\le D\le\sqrt{1-F}$ wiąże obie miary: znajomość jednej daje
oszacowanie drugiej. Wierność jest prawdopodobieństwem „przejścia testu” (tw. Uhlmanna).

## 4. Przykłady rozwiązane

### Przykład 17.1 (łatwy): wektor Blocha i ślad częściowy

**Dane.** (i) $\rho=0{,}7\lvert0\rangle\langle0\rvert+0{,}3\lvert1\rangle\langle1\rvert$;
(ii) $\lvert+i\rangle=\tfrac{1}{\sqrt2}(\lvert0\rangle+i\lvert1\rangle)$;
(iii) para Bella $\lvert\Phi^+\rangle$.

**Metoda.** Wzory $r_j=\mathrm{Tr}(\rho\sigma_j)$ z podsekcji 3.4 oraz ślad częściowy z 3.5.

**Rachunek.** (i) $\rho=\mathrm{diag}(0{,}7;0{,}3)$, więc $r_x=r_y=0$,
$r_z=0{,}7-0{,}3=0{,}4$; $\mathrm{Tr}\rho^2=0{,}49+0{,}09=0{,}58<1$ (stan mieszany, $\lvert\vec r\rvert=0{,}4<1$).
(ii) Z $r_y=\mathrm{Tr}(\rho Y)=i\rho_{10}-i\rho_{01}$ i $\rho_{01}=\tfrac i2$ dostajemy
$r_y=i(-\tfrac i2)-i(\tfrac i2)=\tfrac12+\tfrac12=1$, a $r_x=r_z=0$; stąd $\vec r=(0,1,0)$ —
biegun $+y$ sfery Blocha, czyli stan $\lvert+i\rangle$.
(iii) $\mathrm{Tr}_B\lvert\Phi^+\rangle\langle\Phi^+\rvert=\tfrac12 I$ (rachunek w 3.5).

**Odpowiedź:** (i) $\mathbf{\vec r=(0,0,0{,}4)}$, $\mathbf{\mathrm{Tr}\rho^2=0{,}58}$;
(ii) $\mathbf{\vec r=(0,1,0)}$; (iii) $\mathbf{\rho_A=\tfrac12 I}$.
*Interpretacja:* stan mieszany leży **wewnątrz** sfery Blocha; maksymalne splątanie daje po
„zapomnieniu” maksymalnie mieszany kubit.

### Przykład 17.2 (trudniejszy): trzy kanały i ich złożenie

**Dane.** (a) Tłumienie amplitudowe o $\gamma=0{,}3$ działające na $\lvert1\rangle$ i na
$\lvert+\rangle$; (b) depolaryzujący o $p=0{,}3$ na $\lvert0\rangle$; (c) przesunięcie fazy o
$\lambda=0{,}4$ na $\lvert+\rangle$; (d) złożenie depolaryzujących $p_1=0{,}2$, $p_2=0{,}3$.

**Metoda.** $\mathcal E(\rho)=\sum_iK_i\rho K_i^\dagger$ z tabeli 3.9; składanie ze wzoru
$(1-p)=(1-p_1)(1-p_2)$.

**Rachunek.** (a) $K_0=\mathrm{diag}(1,\sqrt{0{,}7})$, $K_1=\lvert0\rangle\langle1\rvert\sqrt{0{,}3}$:

$$
K_0\lvert1\rangle\langle1\rvert K_0^\dagger+K_1\lvert1\rangle\langle1\rvert K_1^\dagger
=\mathrm{diag}(0{,}3;\ 0{,}7),\qquad
\mathcal E(\lvert+\rangle\langle+\rvert)=\begin{pmatrix}0{,}65&0{,}4183\\0{,}4183&0{,}35\end{pmatrix}.
$$

Populacja $\lvert1\rangle$ spadła $1\to0{,}7$ (ubyło $0{,}3$), koherencja $\tfrac12\to0{,}4183$.
(b) $(0{,}7)\lvert0\rangle\langle0\rvert+0{,}3\cdot\tfrac I2=\mathrm{diag}(0{,}85;0{,}15)$;
$\mathrm{Tr}\rho^2=0{,}85^2+0{,}15^2=0{,}745$.
(c)

$$
(1-\tfrac\lambda2)\rho+\tfrac\lambda2 Z\rho Z=\begin{pmatrix}0{,}5&0{,}3\\0{,}3&0{,}5\end{pmatrix}
$$

— populacje bez zmian, koherencje $\times0{,}6$.
(d) $1-(1-0{,}2)(1-0{,}3)=1-0{,}8\cdot0{,}7=0{,}44$.

**Odpowiedź:** (a) $\mathbf{\mathrm{diag}(0{,}3;0{,}7)}$ oraz macierz

$$
\mathbf{\begin{pmatrix}0{,}65&0{,}4183\\0{,}4183&0{,}35\end{pmatrix}}
$$

(b) $\mathbf{\mathrm{diag}(0{,}85;0{,}15)}$, purity $\mathbf{0{,}745}$; (c) macierz

$$
\mathbf{\begin{pmatrix}0{,}5&0{,}3\\0{,}3&0{,}5\end{pmatrix}}
$$

(d) $\mathbf{p=0{,}44}$.
*Interpretacja:* tłumienie amplitudowe zmienia **populacje** i koherencje, przesunięcie fazy — tylko
koherencje, a złożenie szumów dodaje się „w prawdopodobieństwie” ($p=p_1+p_2-p_1p_2$).

### Przykład 17.3 (średni): wierność, odległość śladowa i Fuchs–van de Graaf

**Dane.** $\rho=\lvert0\rangle\langle0\rvert$, $\sigma=D_{0{,}3}(\rho)=\mathrm{diag}(0{,}85;0{,}15)$.

**Rachunek.** Ponieważ $\sqrt\rho=\rho=\mathrm{diag}(1;0)$, mamy
$\sqrt\rho\,\sigma\sqrt\rho=\mathrm{diag}(0{,}85;0)$, a jedyna wartość własna to $0{,}85$; stąd
$\sqrt{\sqrt\rho\,\sigma\sqrt\rho}=\mathrm{diag}(\sqrt{0{,}85};0)$ i
$F=\big(\mathrm{Tr}\,\mathrm{diag}(\sqrt{0{,}85};0)\big)^2=0{,}85$. Zgadza się to z wzorem ogólnym
$F(\lvert0\rangle,\ D_p(\lvert0\rangle))=1-\tfrac p2=0{,}85$. Odległość:
$\rho-\sigma=\mathrm{diag}(0{,}15;-0{,}15)$, więc $D=\tfrac12(0{,}15+0{,}15)=0{,}15=\tfrac p2$.
Nierówność Fuchsa–van de Graafa: $1-\sqrt{0{,}85}=1-0{,}9220=0{,}0398\le0{,}15\le\sqrt{0{,}15}=0{,}3873$. ✓

**Odpowiedź:** $\mathbf{F=0{,}85}$, $\mathbf{D=0{,}15}$, a
$\mathbf{0{,}0398\le0{,}15\le0{,}3873}$ — nierówność spełniona.
*Interpretacja:* depolaryzowanie z $p=0{,}3$ zmniejsza wierność do $0{,}85$ i przesuwa stan w
stronę $\tfrac I2$; obie miary dają spójny obraz „jak daleko” od stanu wyjściowego.

## 5. Typowe pułapki

1. **Mylenie superpozycji ze stanem mieszanym.** $\tfrac12I\ne\tfrac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)$:
   pierwszy nie ma żadnej fazy względnej (brak interferencji), drugi ma ją (pomiar w bazie $X$ daje
   zawsze $\lvert+\rangle$).
2. **Brak normalizacji Krausa.** Kanał jest fizyczny tylko przy $\sum_iK_i^\dagger K_i=I$; bez tego
   $\mathrm{Tr}\,\mathcal E(\rho)\ne1$.
3. **Oczekiwanie stanu czystego po śladzie częściowym.** Ślad częściowy stanu splątanego **musi**
   dać stan mieszany (chyba że stan był iloczynowy).
4. **Mylenie $\mathrm{Tr}\rho^2$ z entropią.** To dwie różne (choć powiązane) miary; $\mathrm{Tr}\rho^2$
   dla $\tfrac I2$ to $\tfrac12$, a entropia $S=1$ bita.
5. **Pomylenie „który kubit zostaje”.** $\mathrm{Tr}_B$ wyrzuca $B$; subskrypt mówi, **po czym**
   sumujemy — nie odwrotnie.
6. **Zły podział indeksów w śladzie częściowym.** Dla pary Bella elementy $(0,3),(3,0)$
   ($\lvert00\rangle\langle11\rvert$) nie znikają same — trzeba je poprawnie sparować z podukładami.

## 7. Wskazówki do zadań

- **Z-17.1.** (a) macierz diagonalna; (b) $\lvert\vec r\rvert=\lvert r_z\rvert=\lvert\rho_{00}-\rho_{11}\rvert$;
  (c) porównaj $\mathrm{Tr}\rho^2$ z 1.
- **Z-17.2.** (a) $r_j=\mathrm{Tr}(\rho\sigma_j)$; (b) podstaw $\rho_{01}=i/2$; (c) wektory różnią się
  znakiem $r_x$.
- **Z-17.3.** (a)–(b) sumuj po indeksie drugiego kubita; (c) dla $\tfrac I2$ entropia to 1 bit.
- **Z-17.4.** (a) ułóż amplitudy w macierz $2\times2$ i policz SVD (wartości szczególne);
  (b) $S=-\sum\lambda_i\log_2\lambda_i$; (c) porównaj $S$ z $\log_2 2=1$.
- **Z-17.5.** (a) $K_0^\dagger K_0+K_1^\dagger K_1=\mathrm{diag}(1,1-\gamma)+\mathrm{diag}(0,\gamma)$;
  (b) podstaw $\gamma=0{,}3$; (c) porównaj oba warunki sum.
- **Z-17.6.** (a) cztery operatory z tabeli 3.9; (b) $(1-p)\lvert0\rangle\langle0\rvert+\tfrac p2 I$;
  (c) $(1-p)=(1-p_1)(1-p_2)$.
- **Z-17.7.** (a) $F=1-\tfrac p2$; (b) $D=\tfrac p2$; (c) wstaw obie liczby do $1-\sqrt F\le D\le\sqrt{1-F}$.
- **Z-17.8.** (a) $K_0=\lvert0\rangle\langle0\rvert$, $K_1=\lvert1\rangle\langle1\rvert$; (b) czy
  $K_iK_i^\dagger=K_i^\dagger K_i$ i czy suma kwadratów $=$ I; (c) koherencje znikają, $\lvert+\rangle\to\tfrac I2$.

## 8. Co dalej

- **Splątanie, dekoherencja, termodynamika** — [rozdział 18](18-ponad-program-splatanie-dekoherencja-termodynamika.md):
  miary splątania, $T_1/T_2$, zasada Landauera.
- **Algorytmy zaawansowane i granice** — [rozdział 19](19-ponad-program-algorytmy-zaawansowane-i-granice.md):
  teleportacja i twierdzenie Holevo w języku kanałów.
- **Mini-projekty** — [rozdział 20](20-ponad-program-mini-projekty.md): symulator stanu i teleportacja.
- Pełne rozwiązania: [zadania/rozwiazania/rozwiazania-17.md](../zadania/rozwiazania/rozwiazania-17.md).
- Praca domowa: [PD-4](../praca-domowa/praca-domowa-04.md).
- Bibliografia: [Nielsen–Chuang, rozdz. 2 i 8](../docs/bibliografia.md); [Preskill, wykłady 3 i 5](../docs/bibliografia.md).
- Kod: [`kod/teleportacja.py`](../kod/teleportacja.py) (ślad częściowy i wierność), [`kod/korekcja_3bit.py`](../kod/korekcja_3bit.py) (kanał bit-flip, syndromy).

7. **Utożsamienie kanału unitarnego z depolaryzującym.** Unitarny jest **odwracalny**, depolaryzujący
   nie; dodatkowo depolaryzujący jest unitalny, a tłumienie amplitudowe nie.
8. **Zgubiony kwadrat we wierności.** $F$ w tym rozdziale to **kwadrat** $(\mathrm{Tr}\sqrt{\cdots})^2$;
   pierwiastek $\sqrt F$ jest probabilistyczną „wiernością pierwiastkową” (*root fidelity*).
9. **Przekonanie, że kanał opisuje rzeczywistość.** Kanał opisuje **niewiedzę** (oraz realny szum);
   ten sam $\mathcal E$ wynika z wielu różnych mikroskopowych oddziaływań.
10. **Zapominanie o pomiarze po kanale.** Kanał zmienia $\rho$; dopiero $\mathrm{Tr}(P_m\rho)$ daje
    prawdopodobieństwa, których szuka eksperyment.

## 6. Zadania (Z-17)

**Z-17.1.** Macierz gęstości jednego kubita.
(a) Zapisz $\rho=\tfrac14\lvert0\rangle\langle0\rvert+\tfrac34\lvert1\rangle\langle1\rvert$ jako macierz.
(b) Policz $\mathrm{Tr}\,\rho^2$ i $\lvert\vec r\rvert$.
(c) Czy to stan czysty? Uzasadnij.

**Z-17.2.** Sfera Blocha.
(a) Wyprowadź $r_x,r_y,r_z$ z $\rho=\tfrac12(I+\vec r\cdot\vec\sigma)$.
(b) Wyznacz $\vec r$ dla $\lvert+i\rangle=\tfrac{1}{\sqrt2}(\lvert0\rangle+i\lvert1\rangle)$.
(c) Wyznacz $\vec r$ dla $\lvert+\rangle$ i $\lvert-\rangle$; czym różnią się te wektory?

**Z-17.3.** Ślad częściowy.
(a) Policz $\rho_A=\mathrm{Tr}_B\lvert\Phi^+\rangle\langle\Phi^+\rvert$.
(b) Policz $\rho_A$ dla $\lvert\Psi^-\rangle=\tfrac{1}{\sqrt2}(\lvert01\rangle-\lvert10\rangle)$.
(c) Oblicz entropię $S(\rho_A)$ w obu przypadkach.

**Z-17.4.** Rozkład Schmidta.
Dany $\lvert\psi\rangle=\tfrac{1}{\sqrt3}(\lvert00\rangle+\lvert01\rangle+\lvert10\rangle)$.
(a) Wyznacz współczynniki Schmidta $\sqrt{\lambda_i}$.
(b) Policz entropię splątania.
(c) Czy splątanie jest maksymalne? Odpowiedz liczbą i zdaniem.

**Z-17.5.** Tłumienie amplitudowe.
(a) Zapisz operatory Krausa i sprawdź $\sum K_i^\dagger K_i=I$.
(b) Dla $\gamma=0{,}3$ policz $\mathcal E(\lvert1\rangle\langle1\rvert)$ i $\mathcal E(\lvert+\rangle\langle+\rvert)$.
(c) Czy ten kanał jest unitalny ($\sum K_iK_i^\dagger=I$)? Uzasadnij.

**Z-17.6.** Kanał depolaryzujący.
(a) Dla $p=0{,}3$ zapisz cztery operatory Krausa i sprawdź normalizację.
(b) Policz $\mathcal E(\lvert0\rangle\langle0\rvert)$ i jego purity.
(c) Wyznacz parametr $p$ kanału złożonego z $D_{0{,}2}\circ D_{0{,}3}$.

**Z-17.7. [★]** Wierność i odległość śladowa.
(a) Policz $F(\lvert0\rangle,\ D_p(\lvert0\rangle))$ dla $p=0{,}3$.
(b) Policz $D(\lvert0\rangle\langle0\rvert,\ D_p(\lvert0\rangle\langle0\rvert))$.
(c) Sprawdź nierówność Fuchsa–van de Graafa.

**Z-17.8. [★]** Pomiar jako kanał.
(a) Zapisz operatory Krausa pomiaru rzutowego w bazie $Z$.
(b) Czy taki kanał jest unitarny? Czy jest unitalny?
(c) Podaj $\rho$ po pomiarze w bazie $Z$ dla stanu $\lvert+\rangle$ (uśredniony po wynikach).



