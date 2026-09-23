# 05. Podstawy mechaniki kwantowej


## 1. Zakres rozdziału

Rozdział obejmuje **postulaty** mechaniki kwantowej (stan, obserwabla, pomiar,
ewolucja) oraz rachunek wartości oczekiwanej, wariancji i prawdopodobieństw pomiaru.
Omawia równanie Schrödingera, stany stacjonarne, nieskończoną studnię potencjału,
oscylator harmoniczny, atom wodoru i tunelowanie. Obejmuje też spin 1/2, polaryzację
fotonu i **prawo Malusa**, twierdzenie Ehrenfesta oraz ewolucję superpozycji
(dudnienia). Materiał dotyczy zadań P1 (cząstka w studni potencjału) i P2
(polaryzatory i pojedynczy foton).

## 2. Najważniejsze definicje

- **Stan kwantowy**: wektor $\lvert\psi\rangle$ w przestrzeni Hilberta (unormowany).
- **Funkcja falowa**: $\psi(x)=\langle x|\psi\rangle$; $\lvert\psi(x)\rvert^2$ to gęstość
  prawdopodobieństwa położenia (reguła Borna).
- **Obserwabla**: operator hermitowski $A$; możliwe wyniki to jego wartości własne $a$.
- **Wartość oczekiwana**: $\langle A\rangle=\langle\psi\lvert A\rvert\psi\rangle =\int\psi^*A\psi\,dx$; **wariancja** $\operatorname{Var}A=\langle A^2\rangle-\langle A\rangle^2$.
- **Komutator**: $[A,B]=AB-BA$; **zasada nieoznaczoności**
  $\Delta A\,\Delta B\ge\frac12\lvert\langle[A,B]\rangle\rvert$.
- **Hamiltonian** $H=\frac{\hat p^2}{2m}+V(\hat x)$; **stany stacjonarne** $H\lvert n\rangle=E_n\lvert n\rangle$.
- **Ewolucja**: $\lvert\psi(t)\rangle=e^{-iHt/\hbar}\lvert\psi(0)\rangle$.
- **Kubit**: układ dwupoziomowy; baza $\{\lvert0\rangle,\lvert1\rangle\}$; stany na
  sferze Blocha.
- **Polaryzacja fotonu**: kubit z bazą $\{\lvert H\rangle,\lvert V\rangle\}$ (pozioma/pionowa).

## 3. Teoria krok po kroku

### 3.1 Postulaty mechaniki kwantowej

1. **Stan** układu opisuje wektor $\lvert\psi\rangle$ w przestrzeni Hilberta.
2. **Obserwable** to operatory hermitowskie; wyniki pomiaru to ich wartości własne.
3. **Pomiar**: wynik $a$ pojawia się z prawdopodobieństwem
   $P(a)=\lvert\langle a\lvert\psi\rangle\rvert^2$; po pomiarze stan redukuje się do
   $\lvert a\rangle$ (projekcja).
4. **Ewolucja** między pomiarami: unitarna, $\lvert\psi(t)\rangle=e^{-iHt/\hbar}\lvert\psi(0)\rangle$
   (albo równanie Schrödingera).
5. **Układy złożone**: przestrzeń to iloczyn tensorowy $\mathcal H_1\otimes\mathcal H_2$.

### 3.2 Funkcja falowa i reguła Borna

W reprezentacji położenia $\psi(x)$ spełnia $\int\lvert\psi(x)\rvert^2dx=1$.
Prawdopodobieństwo znalezienia cząstki w $[a,b]$ to $\int_a^b\lvert\psi\rvert^2dx$.
Pęd realizuje operator $\hat p=-i\hbar\,d/dx$, a energia $\hat H$.

### 3.3 Obserwable hermitowskie

Do każdej mierzalnej wielkości przyporządkowujemy operator hermitowski $A=A^\dagger$
(rozdział [02](02-algebra-liniowa.md)). Jego wartości własne są rzeczywiste, wektory
własne różnych wartości — ortogonalne, i tworzą zupełną bazę pomiarową
$\{\lvert a\rangle\}$.

### 3.4 Pomiar i kolaps

Rzutowy pomiar w bazie $\{\lvert a\rangle\}$: prawdopodobieństwa $P(a)$ z reguły Borna,
a stan „zapada się” (kolaps) do $\lvert a\rangle$. Powtórny pomiar tej samej
obserwabli daje ten sam wynik — dlatego własne wartości są „ostre”, a superpozycja
nie. Rozróżniaj **jednorazowy wynik** od **wartości oczekiwanej** (średniej z wielu
identycznych przygotowań).

### 3.5 Wartość oczekiwana i wariancja

$$\langle A\rangle=\langle\psi\lvert A\rvert\psi\rangle,\qquad
\operatorname{Var}(A)=\langle A^2\rangle-\langle A\rangle^2,\qquad
\Delta A=\sqrt{\operatorname{Var}(A)}.$$

Na sferze Blocha dla spinu: $\langle\sigma_x\rangle=\langle X\rangle$ itd.

### 3.6 Komutatory i zasada nieoznaczoności

$[A,B]=AB-BA$. Dla położenia i pędu $[\hat x,\hat p]=i\hbar$, skąd
$\Delta x\,\Delta p\ge\hbar/2$. Ogólnie

$$\Delta A\,\Delta B\ge\Bigl\lvert\tfrac{1}{2i}\langle[A,B]\rangle\Bigr\rvert.$$

Obserwable, które komutują ($[A,B]=0$), mają wspólną bazę wektorów własnych i można
je mierzyć jednocześnie bez ograniczeń.

### 3.7 Równanie Schrödingera (zależne i niezależne od czasu)

Zależne od czasu: $i\hbar\frac{\partial}{\partial t}\lvert\psi\rangle=H\lvert\psi\rangle$.
Dla hamiltonianu niezależnego od czasu szukamy stanów stacjonarnych
$\lvert\psi(t)\rangle=e^{-iEt/\hbar}\lvert\psi\rangle$, co prowadzi do **równania
niezależnego od czasu** $H\lvert\psi\rangle=E\lvert\psi\rangle$ (zagadnienie własne
energii). W reprezentacji położenia:

$$-\frac{\hbar^2}{2m}\psi''(x)+V(x)\psi(x)=E\psi(x).$$

### 3.8 Stany stacjonarne

Stan stacjonarny $\lvert n\rangle$ ma ustaloną energię $E_n$; $\lvert\psi_n(x)\rvert^2$
nie zależy od czasu (faza $e^{-iE_nt/\hbar}$ znika w kwadracie modułu). Stan
nie-stacjonarny to superpozycja $\sum_nc_n\lvert n\rangle$ — wtedy obserwable
oscylują (dudnienia, §3.17).

### 3.9 Nieskończona studnia potencjału (zadanie P1)

Studnia $V(x)=0$ dla $0<x<L$ i $V=\infty$ poza. Wewnątrz $-\frac{\hbar^2}{2m}\psi''=E\psi$,
czyli $\psi''=-k^2\psi$ z $k=\sqrt{2mE}/\hbar$. Rozwiązanie ogólne
$\psi=A\sin kx+B\cos kx$. Warunki brzegowe $\psi(0)=\psi(L)=0$:
$B=0$ oraz $\sin kL=0\Rightarrow k_n=\frac{n\pi}{L}$, $n=1,2,\dots$ Zatem

$$\boxed{\psi_n(x)=\sqrt{\frac2L}\sin\!\Bigl(\frac{n\pi x}{L}\Bigr),\qquad
E_n=\frac{n^2\pi^2\hbar^2}{2mL^2}.}$$

Cechy: energia kwantowana ($E_n\propto n^2$); stan podstawowy $n=1$ ma $E_1>0$
(energia zerowa — skutek nieoznaczoności); funkcja $\psi_n$ ma $n-1$ węzłów wewnątrz.
Przykład liczbowy (elektron, $L=1$ nm): $E_1\approx0{,}376$ eV,
$E_2\approx1{,}50$ eV, $E_2-E_1\approx1{,}128$ eV (przejście o $\lambda\approx1100$ nm).

### 3.10 Studnia skończona

Dla $V=V_0$ poza studnią o skończonej głębokości funkcja falowa **nie znika** na
brzegach, lecz wykładniczo wnika w barierę ($\psi\sim e^{-\kappa x}$,
$\kappa=\sqrt{2m(V_0-E)}/\hbar$). Skutki: skończona liczba stanów związanych,
energie nieco niższe niż w studni nieskończonej, a „ogonki” pozwalają cząstce
przenikać do obszaru klasycznie zabronionego.

### 3.11 Tunelowanie i współczynniki przejścia

Cząstka o energii $E<V_0$ przechodzi przez barierę o szerokości $a$ z
prawdopodobieństwem (przybliżenie bariery prostokątnej)

$$T=\Bigl[1+\frac{V_0^2\sinh^2(\kappa a)}{4E(V_0-E)}\Bigr]^{-1},\qquad
\kappa=\frac{\sqrt{2m(V_0-E)}}{\hbar}.$$

Dla szerokiej bariery $\kappa a\gg1$: $T\approx16\frac{E(V_0-E)}{V_0^2}e^{-2\kappa a}$ —
maleje wykładniczo. Przykład: elektron, $E=1$ eV, $V_0=5$ eV, $a=0{,}5$ nm →
$\kappa a\approx5{,}12$ i $T\approx9{,}08\cdot10^{-5}$. Tunelowanie to podstawa STM
i bramek Josephsona.

### 3.12 Oscylator harmoniczny

Dla $V(x)=\tfrac12m\omega^2x^2$ równanie $H\psi=E\psi$ daje widmo równoodległe:

$$E_n=\Bigl(n+\tfrac12\Bigr)\hbar\omega,\qquad n=0,1,2,\dots$$

Energia zerowa $\tfrac12\hbar\omega$ (drgania punktu zerowego) jest nieusuwalna.
Funkcja stanu podstawowego to Gauss $\psi_0\propto e^{-x^2/(2x_0^2)}$ z
$x_0=\sqrt{\hbar/(m\omega)}$ — dlatego całka Gaussa (rozdział 04) wraca tu wprost.
Oscylator modeluje drgania sieci, fotony pola i stany kwantowych rezonatorów.

### 3.13 Atom wodoru (przegląd)

Dla $V(r)=-e^2/(4\pi\varepsilon_0 r)$ widmo zależy od głównej liczby kwantowej $n$:

$$E_n=-\frac{\mu e^4}{2(4\pi\varepsilon_0)^2\hbar^2}\cdot\frac{1}{n^2}
=-\frac{13{,}606\ \text{eV}}{n^2},$$

z degeneracją $n^2$ (liczby $l=0,\dots,n-1$, $m=-l,\dots,l$ oraz spin). Stan
podstawowy: $E_1\approx-13{,}6$ eV, promień Bohra $a_0=0{,}0529$ nm. Kwantyzacja
pojawia się z warunków brzegowych, jak w studni (P1), ale w 3D.

### 3.14 Spin 1/2 jako kubit

Spin-1/2 ma dwie wartości $m_s=\pm\tfrac12$; bazę tworzą
$\lvert\uparrow\rangle=\lvert0\rangle$, $\lvert\downarrow\rangle=\lvert1\rangle$.
Obserwable to $\hat S_i=\tfrac{\hbar}{2}\sigma_i$. Ogólny stan to punkt na sferze Blocha:

$$\lvert\psi\rangle=\cos\tfrac\theta2\lvert0\rangle+e^{i\varphi}\sin\tfrac\theta2\lvert1\rangle,$$

a wartości oczekiwane $\langle\sigma_x\rangle=\sin\theta\cos\varphi$,
$\langle\sigma_y\rangle=\sin\theta\sin\varphi$, $\langle\sigma_z\rangle=\cos\theta$.
Pomiar $\sigma_z$ daje $+1$ z $P=\cos^2(\theta/2)$.

Korelacje spinów splątanych cząstek prowadzą do nierówności
Bella (rozdział 09) — pomiar „jednej osi” nie wyznacza
wyniku dla innej osi.

### 3.15 Polaryzacja fotonu i prawo Malusa (zadanie P2)

Foton ma polaryzację, którą kodujemy jako kubit: $\lvert H\rangle$ (pozioma),
$\lvert V\rangle$ (pionowa). Polaryzator ustawiony pod kątem $\theta$ przepuszcza
składową $\cos\theta\lvert H\rangle+\sin\theta\lvert V\rangle$ i **mierzy** rzut —
prawdopodobieństwo przejścia fotonu wynosi $\cos^2\theta$. Dla wiązki o natężeniu $I$
**prawo Malusa**:

$$I(\theta)=I_0\cos^2\theta.$$

Dla światła **niespolaryzowanego** pierwszy polaryzator przepuszcza $I_0/2$, a każdy
kolejny działa jak wyżej na już spolaryzowaną wiązkę. Klasyczny paradoks: dwa
polaryzatory pod $90^\circ$ dają $I=0$, ale wstawienie między nie trzeciego pod
$45^\circ$ daje $I_0/8>0$ — bo pomiar „przygotowuje” nowy stan polaryzacji.

### 3.16 Twierdzenie Ehrenfesta

$$\frac{d}{dt}\langle x\rangle=\frac{\langle p\rangle}{m},\qquad
\frac{d}{dt}\langle p\rangle=-\Bigl\langle\frac{dV}{dx}\Bigr\rangle.$$

Wartości oczekiwane spełniają prawa Newtona — kwantowe średnie poruszają się
klasycznie. Dla oscylatora $\langle x\rangle(t)$ drga z częstością $\omega$.

### 3.17 Ewolucja stanu nie-stacjonarnego (dudnienia)

Dla superpozycji $\lvert\psi\rangle=\frac{1}{\sqrt2}(\lvert1\rangle+\lvert2\rangle)$
dwóch stanów stacjonarnych:

$$\lvert\psi(t)\rangle=\tfrac{1}{\sqrt2}\bigl(e^{-iE_1t/\hbar}\lvert1\rangle
+e^{-iE_2t/\hbar}\lvert2\rangle\bigr).$$

Gęstość prawdopodobieństwa oscyluje z częstością $\omega_{21}=(E_2-E_1)/\hbar$ —
to **dudnienia** (beats). Dla studni $L=1$ nm elektron: $\omega_{21}\approx1{,}71\cdot10^{15}$
rad/s, okres $T=2\pi/\omega_{21}\approx3{,}67$ fs.

### 3.18 Degeneracja

Poziom jest **zdegenerowany**, gdy kilku różnym stanom odpowiada ta sama energia
(np. wodór: $n^2$-krotna degeneracja bez spinu). Degeneracja znika, gdy zaburzenie
łagodzące symetrię zostanie włączone — to podstawa struktury subtelnej i efektu Zeemana.

## 4. Przykłady rozwiązane

### Przykład 1 (łatwy, styl P1): poziomy energii w studni

**Dane:** elektron ($m_e=9{,}109\cdot10^{-31}$ kg) w nieskończonej studni $L=2$ nm.

**Metoda:** $E_n=\dfrac{n^2\pi^2\hbar^2}{2mL^2}$; $\hbar=1{,}0546\cdot10^{-34}$ J·s,
$1$ eV $=1{,}602\cdot10^{-19}$ J.

**Rachunek:**

$$E_1=\frac{\pi^2(1{,}0546\cdot10^{-34})^2}{2\cdot9{,}109\cdot10^{-31}\cdot(2\cdot10^{-9})^2}
=\frac{1{,}0976\cdot10^{-67}}{7{,}287\cdot10^{-48}}\approx1{,}506\cdot10^{-20}\ \text{J},$$

$$E_1\approx\frac{1{,}506\cdot10^{-20}}{1{,}602\cdot10^{-19}}\approx0{,}0940\ \text{eV}.$$

Skalowanie $E_n=n^2E_1$: $E_2\approx0{,}376$ eV, $E_3\approx0{,}846$ eV.

**Wynik:** $E_1\approx0{,}0940$ eV, $E_2\approx0{,}376$ eV, $E_3\approx0{,}846$ eV.

**Interpretacja:** rozstępy rosną jak $2n+1$ (odstęp $E_2-E_1\approx0{,}282$ eV);
podwojenie $L$ czterokrotnie zmniejsza energie (skalowanie $\propto1/L^2$).

### Przykład 2 (trudniejszy): nieoznaczoność w stanie podstawowym studni

**Dane:** stan podstawowy studni $L=1$ nm, $\psi_1=\sqrt{2/L}\sin(\pi x/L)$.

**Metoda:** całki $\langle x\rangle=\int x\lvert\psi\rvert^2dx$,
$\langle x^2\rangle=\int x^2\lvert\psi\rvert^2dx$, oraz $\langle p\rangle=0$,
$\langle p^2\rangle=(n\pi\hbar/L)^2$ dla $n=1$.

**Rachunek:** przez symetrię i całkowanie

$$\langle x\rangle=\frac L2,\qquad
\langle x^2\rangle=L^2\Bigl(\frac13-\frac{1}{2\pi^2}\Bigr)\approx L^2\cdot0{,}2827,$$

$$\Delta x^2=\langle x^2\rangle-\langle x\rangle^2
=L^2\Bigl(\frac1{12}-\frac{1}{2\pi^2}\Bigr)\approx L^2\cdot0{,}03267
\Rightarrow\Delta x\approx0{,}181L,$$

$$\langle p^2\rangle=\Bigl(\frac{\pi\hbar}{L}\Bigr)^2\Rightarrow
\Delta p=\frac{\pi\hbar}{L}.$$

Iloczyn $\Delta x\,\Delta p=\pi\hbar\sqrt{\tfrac1{12}-\tfrac1{2\pi^2}}\approx0{,}568\,\hbar \approx1{,}14\cdot\tfrac{\hbar}{2}\ \ge\ \tfrac{\hbar}{2}$.

**Wynik:** $\Delta x\approx0{,}181L$, $\Delta p=\pi\hbar/L$,
$\Delta x\Delta p\approx0{,}568\hbar$ (zasada spełniona).

**Interpretacja:** stan podstawowy studni nie realizuje minimum nieoznaczoności
(iloczyn $\approx1{,}14\cdot\hbar/2$), w odróżnieniu od paczki gaussowskiej.

### Przykład 3 (trudniejszy, styl P2): prawo Malusa z trzema polaryzatorami

**Dane:** wiązka niespolaryzowana o natężeniu $I_0$; polaryzatory pod kątami
$0^\circ$, $45^\circ$, $90^\circ$.

**Metoda:** pierwszy polaryzator daje $I_0/2$; kolejne — prawo Malusa $I\cos^2\Delta\theta$.

**Rachunek:**

$$I_1=\tfrac12I_0,\qquad I_2=I_1\cos^2 45^\circ=\tfrac12I_0\cdot\tfrac12=\tfrac14I_0,$$

$$I_3=I_2\cos^2 45^\circ=\tfrac14I_0\cdot\tfrac12=\tfrac18I_0.$$

Bez polaryzatora $45^\circ$: $I=I_0/2\cdot\cos^2 90^\circ=0$.

**Wynik:** $I_3=\tfrac18I_0\approx0{,}125\,I_0$; usunięcie środkowego polaryzatora
daje $I=0$.

**Interpretacja:** „pomiar pośredni” przywraca światło — bo polaryzator $45^\circ$
przygotowuje nowy stan, pod którego kątem ostatni polaryzator nie jest już
prostopadły. To kwantowy (a nie klasyczny) efekt fazy pomiaru.

## 5. Typowe pułapki

1. **Mylenie wyniku pomiaru z wartością oczekiwaną.** Jednorazowy wynik to jedna z
   wartości własnych; $\langle A\rangle$ to średnia z wielu prób.
2. **Zapominanie o normalizacji** funkcji falowej przed liczeniem prawdopodobieństw.
3. **Traktowanie $E=0$ jako stanu podstawowego studni.** Najniższa energia to
   $E_1>0$ — skutek nieoznaczoności.
4. **Gubienie $\hbar$** w wykładnikach $e^{-iEt/\hbar}$ i $e^{-ipx/\hbar}$.
5. **Zła kąt w Malusie.** Liczy się **różnica** kątów $\cos^2(\theta_2-\theta_1)$,
   nie $\cos^2\theta$ osobno.
6. **Nazywanie kolapsu „siłą”.** Pomiar to akt informacyjny, nie oddziaływanie
   mechaniczne; nie „popycha” cząstki w klasycznym sensie.
7. **Mylenie $\Delta A$ z $\sigma_A$.** To to samo, ale nie myl wariancji
   $\operatorname{Var}=\Delta^2$ z odchyleniem $\Delta$.

## 6. Zadania (Z-05)

**Z-05.1.** Stan $\lvert\psi\rangle=\cos\tfrac\pi8\lvert0\rangle+\sin\tfrac\pi8\lvert1\rangle$.
(a) Policz $P(0),P(1)$ dla pomiaru $\sigma_z$. (b) Policz $\langle Z\rangle$ i $\langle X\rangle$.
(c) Policz $\Delta Z$.

**Z-05.2.** Elektron w nieskończonej studni $L=2$ nm.
(a) Policz $E_1$. (b) Ile wynosi $E_3/E_1$? (c) Ile węzłów wewnątrz ma $\psi_3$?

**Z-05.3.** Spin-1/2 w stanie $\lvert\psi\rangle=\cos\tfrac\theta2\lvert\uparrow\rangle+ \sin\tfrac\theta2\lvert\downarrow\rangle$, $\theta=\pi/2$.
(a) Policz $P(\uparrow),P(\downarrow)$. (b) Policz $\langle\sigma_x\rangle$,
$\langle\sigma_z\rangle$. (c) Podaj wektor Blocha.

**Z-05.4.** (a) Wykaz $[\hat x,\hat p]=i\hbar$ (działając na $\psi(x)$).
(b) Wyprowadź $\Delta x\,\Delta p\ge\hbar/2$. (c) Jaki stan realizuje równość?

**Z-05.5.** Prawo Malusa. (a) Jaka część $I_0$ przechodzi przez polaryzator
$0^\circ$ (światło niespolaryzowane)? (b) Ile przez układ $0^\circ,45^\circ$?
(c) Ile przez układ $0^\circ,45^\circ,90^\circ$, a ile bez środkowego?

**Z-05.6.** Tunelowanie: $E=1$ eV, $V_0=5$ eV, $a=0{,}5$ nm (elektron).
(a) Podaj wzór na $T$. (b) Policz $\kappa a$ i $T$. (c) Jak zmieni się $T$, gdy
podwoisz $a$?

**Z-05.7.** Superpozycja w studni $L=1$ nm, $\lvert\psi\rangle=\frac{1}{\sqrt2}(\lvert1\rangle+\lvert2\rangle)$.
(a) Podaj $\omega_{21}$. (b) Policz okres dudnień $T$. (c) Które wielkości oscylują
w czasie?

**Z-05.8. [★]** Kubit z $H=\tfrac{\hbar\Omega}{2}X$, start w $\lvert0\rangle$.
(a) Podaj $\lvert\psi(t)\rangle$. (b) Policz $P(1)$ dla $\Omega t=\pi/2$ i $\Omega t=\pi$.
(c) Podaj okres pełnego przeskoku.

## 7. Wskazówki do zadań

- **Z-05.1.** $P(k)=\lvert c_k\rvert^2$; $\langle X\rangle=2\operatorname{Re}(c_0^*c_1)$;
  $\Delta Z=\sqrt{1-\langle Z\rangle^2}$.
- **Z-05.2.** $E_n=n^2E_1$; funkcja $\psi_n$ ma $n-1$ węzłów wewnątrz.
- **Z-05.3.** $P(\uparrow)=\cos^2(\theta/2)$; użyj $\langle\sigma_x\rangle=\sin\theta$,
  $\langle\sigma_z\rangle=\cos\theta$.
- **Z-05.4.** (a) zastosuj $\hat p=-i\hbar d/dx$ i regułę iloczynu; (c) pomyśl o paczce
  gaussowskiej.
- **Z-05.5.** Pierwszy polaryzator na niespolaryzowane światło daje $I_0/2$; dalej
  $\cos^2(\Delta\theta)$.
- **Z-05.6.** $\kappa=\sqrt{2m(V_0-E)}/\hbar$; dla dużego $\kappa a$ użyj
  $T\approx16\frac{E(V_0-E)}{V_0^2}e^{-2\kappa a}$.
- **Z-05.7.** $\omega_{21}=(E_2-E_1)/\hbar$; $T=2\pi/\omega_{21}$.
- **Z-05.8.** [★] $e^{-iHt/\hbar}=\cos\frac{\Omega t}{2}I-i\sin\frac{\Omega t}{2}X$.

## 8. Co dalej

Rozdział 06 (kubity, bramki, obwody, pomiary) rozbudowuje formalizm kubitu z §3.14–3.15,
a rozdział 08 (algorytmy kwantowe) korzysta z aparatu wartości oczekiwanych i
ewolucji. Splątanie i twierdzenie Bella rozwija rozdział 09. Rozwiązania zadań są w
[rozwiazania-05.md](../zadania/rozwiazania/rozwiazania-05.md); praca domowa
łącząca rozdziały 01–05 to [PD-1](../praca-domowa/praca-domowa-01.md).

Stany i bramki w konwencji [konwencji](../docs/03-konwencje-i-notacja.md)
(małoendianowo, $\theta/2$ w obrotach).
