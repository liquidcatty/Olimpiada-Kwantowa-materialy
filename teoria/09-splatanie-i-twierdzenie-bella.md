# 09. Splątanie i twierdzenie Bella


## 1. Zakres rozdziału

Rozdział obejmuje splątanie (ang. *entanglement*) oraz twierdzenie Bella: rozkład Schmidta, kryterium
iloczynowości $ad=bc$ i concurrence, stany Bella i GHZ, kryterium PPT i świadki splątania. Omawia
nierówność CHSH $S=E(a,b)-E(a,b')+E(a',b)+E(a',b')$ (klasycznie $\lvert S\rvert\le2$, maksimum
kwantowe $2\sqrt2$), modele zmiennych ukrytych (local hidden variables, LHV) i monogamię splątania.

Materiał dotyczy zadania P4 (tworzenie stanów Bella z $\lvert00\rangle$ obwodem H–$R_Y$–CNOT)
oraz zagadnień o klasyczności korelacji kwantowych i łamaniu nierówności CHSH, włącznie
z obliczeniem wartości $2\sqrt2$.

## 2. Najważniejsze definicje

- **Stan iloczynowy (product state):** $\lvert\psi\rangle_{AB}=\lvert a\rangle_A\otimes\lvert b\rangle_B$.
- **Stan splątany (entangled):** niebędący stanem iloczynowym.
- **Stany Bella:** $\lvert\Phi^\pm\rangle=\frac{1}{\sqrt2}(\lvert00\rangle\pm\lvert11\rangle)$,
  $\lvert\Psi^\pm\rangle=\frac{1}{\sqrt2}(\lvert01\rangle\pm\lvert10\rangle)$.
- **Stan GHZ:** $\lvert\mathrm{GHZ}\rangle=\frac{1}{\sqrt2}(\lvert000\rangle+\lvert111\rangle)$ —
  maksymalne splątanie trójstronne.
- **Separowalny (mieszany):** $\rho=\sum_k p_k\,\rho_k^A\otimes\rho_k^B$, $\sum_k p_k=1$; inaczej splątany.
- **Rozkład Schmidta (Schmidt decomposition):** $\lvert\psi\rangle_{AB}=\sum_i\sqrt{\lambda_i}\lvert u_i\rangle_A\lvert v_i\rangle_B$;
  liczba niezerowych $\lambda_i$ to **rząd Schmidta**.
- **Kryterium PPT:** $\rho^{T_B}\succeq0$ dla stanów separowalnych (transpozycja częściowa).
- **Świadek splątania (entanglement witness):** obserwabla $W$ z $\mathrm{Tr}(W\sigma)\ge0$ dla
  separowalnych $\sigma$ i $\mathrm{Tr}(W\rho)<0$ dla pewnego splątanego $\rho$.
- **Nierówność CHSH:** $S=E(a,b)-E(a,b')+E(a',b)+E(a',b')$; klasycznie $\lvert S\rvert\le2$.
- **Model LHV:** wyniki wyznaczone przez wspólny parametr $\lambda$ o rozkładzie $\rho(\lambda)$.
- **Monogamia splątania:** splątanie nie „rozmnaża się”; jego nadmiar kosztuje gdzie indziej.

## 3. Teoria krok po kroku

### 3.1 Stany iloczynowe i splątane; rozkład Schmidta

Każdy stan dwóch układów $\lvert\psi\rangle_{AB}$ można zapisać w **rozkładzie Schmidta**

$$
\lvert\psi\rangle_{AB}=\sum_{i=1}^{r}\sqrt{\lambda_i}\,\lvert u_i\rangle_A\otimes\lvert v_i\rangle_B,
$$

gdzie $\{\lvert u_i\rangle\},\{\lvert v_i\rangle\}$ to ortonormalne bazy, $\lambda_i\ge0$, $\sum_i\lambda_i=1$,
a $r$ to rząd Schmidta. **Skąd to się bierze:** rozkład SVD macierzy współczynników
$M_{jk}=\langle j\vert_A\langle k\vert_B\psi\rangle$ daje $M=U\,\mathrm{diag}(\sqrt{\lambda})\,V^\dagger$;
kolumny $U,V$ to szukane bazy. **Wniosek:** $\lvert\psi\rangle$ jest iloczynowy $\iff r=1$. Sama liczba
Schmidta $>1$ jest świadectwem splątania (niezależnym od bazy).

**Kryterium iloczynowości „szkolne”** dla $\lvert\psi\rangle=a\lvert00\rangle+b\lvert01\rangle+c\lvert10\rangle+d\lvert11\rangle$:
iloczynowy $\iff ad=bc$; **concurrence** $C=2\lvert ad-bc\rvert\in[0,1]$ mierzy siłę splątania
($C=1$ dla stanu Bella).

### 3.2 Stany Bella i GHZ

Stany Bella tworzą ortonormalną bazę $\mathbb{C}^4$ i mają maksymalne splątanie. Powstają z
$\lvert00\rangle$ przez $H$ na górnym kubicie i CNOT (rozdział 06). Trójstronny odpowiednik to

$$
\lvert\mathrm{GHZ}\rangle=\tfrac{1}{\sqrt2}(\lvert000\rangle+\lvert111\rangle).
$$

GHZ pokazuje **monogamię** (sekcja 3.9): po odrzuceniu jednego kubita pozostała para jest
*separowalna*, choć całość ma maksymalne splątanie trójstronne. To odróżnia GHZ od stanu W
$\frac{1}{\sqrt3}(\lvert001\rangle+\lvert010\rangle+\lvert100\rangle)$, który ma również splątanie dwustronne.

### 3.3 Separowalność stanów mieszanych

Dla stanów mieszanych splątanie definiujemy przez **brak** rozkładu separowalnego
$\rho=\sum_k p_k\rho_k^A\otimes\rho_k^B$. W przeciwieństwie do stanów czystych, gdzie wystarczy rząd
Schmidta, dla mieszanych potrzebne są kryteria (PPT, świadkowie). Stan czysty $\lvert\psi\rangle_{AB}$
jest splątany $\iff$ jego **zredukowana** macierz $\rho_A=\mathrm{Tr}_B\lvert\psi\rangle\langle\psi\rvert$
jest mieszana ($S(\rho_A)>0$).

### 3.4 Kryterium PPT (Peresa–Horodeckiego)

Transpozycja częściowa $\rho^{T_B}$ (transpozycja po indeksach $B$) dla stanu **separowalnego** jest
półokreślona dodatnio, bo $(\rho_k^A\otimes\rho_k^B)^{T_B}=\rho_k^A\otimes(\rho_k^B)^T\succeq0$ i suma
dodatnich składników też jest dodatnia. Zatem

$$
\text{separowalny}\ \Rightarrow\ \rho^{T_B}\succeq0,\qquad \rho^{T_B}\not\succeq0\ \Rightarrow\ \text{splątany}.
$$

Peres (1996) udowodnił, że dla układów $2\times2$ i $2\times3$ jest to kryterium **konieczne i wystarczające**;
dla większych wymiarów istnieją stany PPT-splątane (bound entangled).

**Przykład — stan Wernera:** $\rho_W=p\lvert\Phi^+\rangle\langle\Phi^+\rvert+\frac{1-p}{4}I$.
Wartości własne $\rho_W^{T_B}$ to $\frac{1+p}{4}$ (trzykrotnie) oraz $\frac{1-3p}{4}$ — ta ostatnia
jest ujemna dokładnie gdy $p>\frac13$. Stąd granica splątania $p>\frac13$: dla $p=0{,}3$ najmniejsza
wartość własna wynosi $+0{,}025$, a dla $p=0{,}7$ wynosi $-0{,}275$.

### 3.5 Świadkowie splątania

Gdy PPT jest zbyt słabe (duże wymiary), używa się **świadków**. Świadek to obserwabla $W$ taka, że
$\mathrm{Tr}(W\sigma)\ge0$ dla wszystkich separowalnych $\sigma$. Kanoniczny przykład:

$$
W=\tfrac12 I-\lvert\Phi^+\rangle\langle\Phi^+\rvert.
$$

Dla stanu Wernera $\mathrm{Tr}(W\rho_W)=\tfrac12-p-\tfrac{1-p}{4}=\tfrac{1-3p}{4}$, więc $W$ „wykrywa”
splątanie dokładnie dla $p>\frac13$ — zgodnie z PPT. Każdy splątany stan ma świadka (twierdzenie
o separowalności zbioru stanów separowalnych).

### 3.6 Nierówność CHSH i jej wyprowadzenie

Dwie strony dzielą parę splątaną. Alicja wybiera pomiar $a$ lub $a'$, Bob $b$ lub $b'$; każdy wynik
to $\pm1$. Definiujemy **korelacje** $E(a,b)=\langle A_a B_b\rangle$. W **modelu LHV** każdy wynik
jest funkcją zmiennej ukrytej $\lambda$: $A_a(\lambda),B_b(\lambda)\in\{\pm1\}$, a
$E(a,b)=\int A_a(\lambda)B_b(\lambda)\rho(\lambda)\,d\lambda$.

**Wyprowadzenie nierówności.** Rozważ

$$
S(\lambda)=A_a(\lambda)\bigl(B_b(\lambda)-B_{b'}(\lambda)\bigr)+A_{a'}(\lambda)\bigl(B_b(\lambda)+B_{b'}(\lambda)\bigr).
$$

Dla ustalonego $\lambda$ zachodzi albo $B_b=B_{b'}$ (wtedy pierwszy nawias $=0$, drugi $=\pm2$),
albo $B_b=-B_{b'}$ (wtedy drugi $=0$, pierwszy $=\pm2$). Ponieważ $\lvert A_a\rvert=\lvert A_{a'}\rvert=1$,
w obu przypadkach $\lvert S(\lambda)\rvert=2$. Całkując i korzystając z $\lvert\int f\rho\,d\lambda\rvert\le\int\lvert f\rvert\rho\,d\lambda$:

$$
\boxed{\ \lvert S\rvert=\bigl\lvert E(a,b)-E(a,b')+E(a',b)+E(a',b')\bigr\rvert\ \le\ 2\ }
$$

dla **każdego** modelu LHV (lokalnego realistycznego).

### 3.7 Wartość kwantowa $2\sqrt2$

Dla stanu singletowego $\lvert\Psi^-\rangle$ i pomiarów w płaszczyźnie pod kątami $\theta_a,\theta_b$:

$$
E(a,b)=-\cos(\theta_a-\theta_b),
$$

co wynika z $\langle\Psi^-\rvert(\hat a\cdot\vec\sigma)\otimes(\hat b\cdot\vec\sigma)\lvert\Psi^-\rangle=-\hat a\cdot\hat b$.
Optymalny zestaw (Tsirelson): $\theta_a=0^\circ$, $\theta_{a'}=90^\circ$, $\theta_b=45^\circ$,
$\theta_{b'}=135^\circ$:

$$
E(a,b)=-\tfrac{\sqrt2}{2},\quad E(a,b')=+\tfrac{\sqrt2}{2},\quad E(a',b)=-\tfrac{\sqrt2}{2},\quad E(a',b')=-\tfrac{\sqrt2}{2},
$$

$$
S=-\tfrac{\sqrt2}{2}-\tfrac{\sqrt2}{2}-\tfrac{\sqrt2}{2}-\tfrac{\sqrt2}{2}=-2\sqrt2
\quad\Rightarrow\quad \lvert S\rvert=2\sqrt2\approx2{,}828.
$$

To **narusza** ograniczenie $\lvert S\rvert\le2$; maksimum kwantowe $2\sqrt2$ to **granica Tsirelsona**.

### 3.8 Model zmiennych ukrytych i twierdzenie Bella

**Twierdzenie Bella (CHSH).** Żaden model, w którym (i) wyniki są *zdeterminowane* (realizm) i
(ii) pomiar Alicji nie wpływa na wyniki Boba (lokalność), nie odtwarza wszystkich korelacji
kwantowych. Formalnie: korelacje stanu singletowego nie spełniają $\lvert S\rvert\le2$.

**Eksperymentalnie** (Aspect i in., 1981–82; później Zeilinger, 2015) zmierzono $S\approx2{,}4$–$2{,}7$,
wyraźnie powyżej $2$. Trzeba jednak „zamknąć luki” (**loopholes**): *locality* (brak komunikacji
światłopodobnej między pomiarami), *detection/fair-sampling* (detektory nie mogą preferować
podzbioru), oraz niezależność wejść. Współczesne eksperymenty (Hensen 2015 — „loophole-free”) zamykają
je jednocześnie i potwierdzają naruszenia CHSH.

### 3.9 Monogamia splątania

Splątanie jest zasobem **monogamicznym**. Dla stanu trójstronnego $\lvert\psi\rangle_{ABC}$:

$$
C(A,B)^2+C(A,C)^2\le C(A,BC)^2,
$$

gdzie $C$ to concurrence. Jeśli Alicja jest maksymalnie splątana z Bobem, nie może (tak samo silnie)
być splątana z Karolem. **Przykład GHZ:** dla $\lvert\mathrm{GHZ}\rangle$ całość $A|BC$ jest maksymalnie
splątana (uogólniona concurrence dla podziału $A|BC$ wynosi $1$), ale po odrzuceniu Karola (ślad
częściowy) dostajemy $\rho_{AB}=\tfrac12(\lvert00\rangle\langle00\rvert+\lvert11\rangle\langle11\rvert)$,
dla którego $C(A,B)=0$. Całe splątanie GHZ jest więc *trójstronne* — to podstawa
kryptografii opartej na monogamii i bezpieczeństwa klucza (rozdział 10).

### 3.10 Teleportacja jako zastosowanie

Splątanie pozwala przenieść nieznany stan przy 2 bitach klasycznych ([rozdział 19](19-ponad-program-algorytmy-zaawansowane-i-granice.md));
to pokazuje, że splątanie jest zasobem *operacyjnym*, a nie tylko formalną własnością korelacji.

### 3.11 Superpozycja a splątanie

To **różne** pojęcia. Superpozycja dotyczy jednego układu ($\lvert+\rangle$), splątanie — relacji
między układami. Stan $\lvert+\rangle\otimes\lvert+\rangle$ jest superpozycją (obydwu osobno), ale
*nie* jest splątany. Splątanie = superpozycji **nie da się rozłożyć** na iloczyn stanów części.

### 3.12 Splątanie a dekoherencja

Splątanie jest delikatne: kontakt z otoczeniem degraduje je w czasie koherencji $T_2$. Przykład:
dla stanu Bella z „kanałem depolaryzującym” na jednym kubicie $\rho=(1-p)\lvert\Phi^+\rangle\langle\Phi^+\rvert+p\,\frac{I}{4}$,
concurrence maleje i zeruje się przy pewnym $p$, po czym stan staje się separowalny — mimo że formalnie
„wygląda” podobnie. Dlatego komputery kwantowe wymagają izolacji, a korekcja błędów (rozdział 13)
walczy głównie z utratą splątania.

## 4. Przykłady rozwiązane

### Przykład 1: rozkład Schmidta i entropia splątania

**Dane.** Stan dwukubitowy

$$
\lvert\psi\rangle=\frac{1}{\sqrt3}\big(\lvert00\rangle+\lvert01\rangle+\lvert10\rangle\big).
$$

**Metoda.** Macierz współczynników $M$:

$$
M=\frac{1}{\sqrt3}\begin{pmatrix}1&1\\1&0\end{pmatrix}
$$

(wiersz = kubit $A$, kolumna = kubit $B$); wykonujemy SVD, wartości szczególne to $\sqrt{\lambda_i}$.

**Rachunek.**

$$
MM^\dagger=\frac13\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad \mathrm{Tr}=1,
$$

$\det=\frac19$, więc wartości własne

$$
\lambda_{1,2}=\frac{1}{2}\Big(1\pm\frac{\sqrt5}{3}\Big)\ \Rightarrow\ \lambda_1\approx0{,}8727,\ \lambda_2\approx0{,}1273.
$$

Wartości szczególne: $\sqrt{\lambda_1}\approx0{,}9342$, $\sqrt{\lambda_2}\approx0{,}3568$, więc

$$
\lvert\psi\rangle\approx0{,}9342\,\lvert u_1\rangle\lvert v_1\rangle+0{,}3568\,\lvert u_2\rangle\lvert v_2\rangle.
$$

Rząd Schmidta $r=2>1$ $\Rightarrow$ stan **splątany**. Entropia splątania:

$$
S=-\lambda_1\log_2\lambda_1-\lambda_2\log_2\lambda_2\approx0{,}550\ \text{bitu}.
$$

**Wynik.** Rząd Schmidta $2$; **$\lambda_{1,2}=\frac12(1\pm\frac{\sqrt5}{3})$**; **entropia splątania
$\approx0{,}550$ bitu**.

**Interpretacja.** Splątanie jest „częściowe” ($S<1$ bit, mniej niż dla stanu Bella). Ślad częściowy
$\rho_A=\mathrm{diag}(\lambda_1,\lambda_2)$ pokazuje mieszany stan pojedynczego kubita — a to właśnie
sygnał splątania w stanie czystym.

### Przykład 2: nierówność CHSH dla stanu singletowego

**Dane.** Stan $\lvert\Psi^-\rangle=\frac{1}{\sqrt2}(\lvert01\rangle-\lvert10\rangle)$; Alicja mierzy
wzdłuż $\hat a$ ($0^\circ$) lub $\hat a'$ ($90^\circ$), Bob wzdłuż $\hat b$ ($45^\circ$) lub $\hat b'$
($135^\circ$) w tej samej płaszczyźnie.

**Metoda.** Korzystamy z $E(a,b)=-\cos(\theta_a-\theta_b)$ i liczymy
$S=E(a,b)-E(a,b')+E(a',b)+E(a',b')$.

**Rachunek.** (Wszystkie kąty w stopniach.)

$$
E(a,b)=-\cos(-45^\circ)=-\tfrac{\sqrt2}{2},\qquad E(a,b')=-\cos(-135^\circ)=+\tfrac{\sqrt2}{2},
$$

$$
E(a',b)=-\cos(45^\circ)=-\tfrac{\sqrt2}{2},\qquad E(a',b')=-\cos(-45^\circ)=-\tfrac{\sqrt2}{2}.
$$

Zatem

$$
S=-\tfrac{\sqrt2}{2}-\tfrac{\sqrt2}{2}-\tfrac{\sqrt2}{2}-\tfrac{\sqrt2}{2}=-2\sqrt2.
$$

**Wynik.** **$\lvert S\rvert=2\sqrt2\approx2{,}828>2$** — korelacje kwantowe łamią ograniczenie LHV.

**Interpretacja.** Żaden model zmiennych ukrytych nie da $\lvert S\rvert>2$ (wyprowadzenie w sekcji 3.6),
więc zmierzona wartość przesądza przeciw lokalnemu realizmowi. Wartość $2\sqrt2$ to maksimum kwantowe
(granica Tsirelsona); potwierdzają to doświadczenia Aspecta i późniejsze „loophole-free”.

## 5. Typowe pułapki

1. **„Splątanie = superpozycja”.** Nie; $\lvert+\rangle\lvert+\rangle$ to superpozycja bez splątania.
2. **Badanie splątania przed normalizacją.** Najpierw znormalizuj stan, potem sprawdzaj $ad=bc$ / SVD.
3. **Mylenie PPT z „transpozycją całej macierzy”.** To **częściowa** transpozycja (po jednym podukładzie).
4. **Sądzenie, że jeden pomiar „odczyta” splątanie.** Splątanie to własność stanu; ujawnia się
   w korelacjach wielu pomiarów.
5. **Traktowanie $\lvert S\rvert\le2$ jako granicy kwantowej.** To granica **klasyczna**; kwantowe
   maksimum to $2\sqrt2$.
6. **Obojętne kąty w CHSH.** Bez optymalnych $45^\circ$ między osiami nie osiąga się $2\sqrt2$.
7. **Odwrócenie ról w monogamii.** Nierówność wiąże $C(A,B)^2+C(A,C)^2\le C(A,BC)^2$.

## 6. Zadania (Z-09)

**Z-09.1.** Stany iloczynowe i splątane.
(a) Sprawdź kryterium $ad=bc$ dla $\lvert\Phi^+\rangle$ i dla $\lvert+\rangle\otimes\lvert0\rangle$.
(b) Policz concurrence dla $\lvert\Phi^+\rangle$ i dla stanu $\frac{1}{\sqrt3}(\lvert00\rangle+\lvert01\rangle+\lvert10\rangle)$.
(c) Czy stan $\frac{1}{2}(\lvert00\rangle+\lvert01\rangle+\lvert10\rangle+\lvert11\rangle)$ jest splątany? Uzasadnij.

**Z-09.2.** Rozkład Schmidta.
(a) Wyznacz rozkład Schmidta stanu $\frac{1}{\sqrt2}(\lvert01\rangle-\lvert10\rangle)$.
(b) Policz entropię splątania tego stanu.
(c) Podaj rząd Schmidta stanu z Przykładu 1 i zinterpretuj wynik.

**Z-09.3.** Kryterium PPT.
(a) Zapisz macierz $\rho_W^{T_B}$ dla stanu Wernera i podaj jej wartości własne.
(b) Wyznacz próg $p$, powyżej którego stan jest splątany.
(c) Sprawdź, że świadek $W=\frac12 I-\lvert\Phi^+\rangle\langle\Phi^+\rvert$ wykrywa splątanie dokładnie dla tego progu.

**Z-09.4.** CHSH — granice.
(a) Wyprowadź $\lvert S\rvert\le2$ dla modelu LHV.
(b) Policz $S$ dla stanu Bella przy kątach $0^\circ,90^\circ,45^\circ,135^\circ$.
(c) Jaką wartość $S$ daje „brak korelacji” i dlaczego?

**Z-09.5.** Monogamia i GHZ.
(a) Zapisz stan GHZ i policz $\rho_{AB}$ po odrzuceniu trzeciego kubita.
(b) Policz concurrence $\rho_{AB}$ i uzasadnij monogamię.
(c) Czym różni się stan GHZ od stanu W pod względem splątania dwustronnego?

**Z-09.6. [★]** Dekoherencja splątania.
(a) Dla $\rho=(1-p)\lvert\Phi^+\rangle\langle\Phi^+\rvert+p\,\frac{I}{4}$ podaj concurrence jako funkcję $p$.
(b) Dla jakiego $p$ splątanie znika? Porównaj z progiem PPT z Z-09.3(b).
(c) Wyjaśnij, dlaczego dla dwóch kubitów oba progi się pokrywają i kiedy mogłyby się różnić.

## 7. Wskazówki do zadań

- **Z-09.1.** W (a) zapisz amplitudy $a,b,c,d$; w (c) sprawdź $ad=bc$.
- **Z-09.2.** W (a) użyj SVD macierzy $2\times2$; w (b) $S=-(\lambda_1\log_2\lambda_1+\lambda_2\log_2\lambda_2)$.
- **Z-09.3.** W (a) transponuj tylko drugi podukład; w (b)/(c) rozwiąż $\frac{1-3p}{4}<0$.
- **Z-09.4.** W (a) rozważ dwa przypadki $B_b=\pm B_{b'}$; w (c) brak korelacji $\Rightarrow E=0$.
- **Z-09.5.** W (a) ślad licz po trzecim kubicie: $\rho_{AB}=\mathrm{Tr}_C\lvert\mathrm{GHZ}\rangle\langle\mathrm{GHZ}\rvert$.
- **Z-09.6.** W (a) użyj postaci $C=\max(0,2\lambda-1)$-owej dla stanów Bella-diagonalnych.

## 8. Co dalej

- **Kryptografia kwantowa** — [rozdział 10](10-kryptografia-kwantowa.md): BB84, E91 i monogamia w praktyce.
- **Metrologia** — [rozdział 11](11-metrologia-kwantowa.md): splątanie jako zasób precyzji.
- **Kanały i macierze gęstości** — [rozdział 17](17-ponad-program-macierze-gestosci-i-kanaly.md): PPT, Kraus.
- **Splątanie, dekoherencja i termodynamika** — [rozdział 18](18-ponad-program-splatanie-dekoherencja-termodynamika.md).
- Pełne rozwiązania: [zadania/rozwiazania/rozwiazania-09.md](../zadania/rozwiazania/rozwiazania-09.md).
- Praca domowa: [PD-2](../praca-domowa/praca-domowa-02.md).
