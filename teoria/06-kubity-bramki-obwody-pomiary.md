# 06. Kubity, bramki, obwody, pomiary

> **Warsztat źródłowy:** „Kubity, bramki, obwody, pomiary” (Krzysztof Pawłowski).
> **Czas nauki:** ~6 h teorii + ~8 h zadań.
> **Wymagana wiedza wstępna:** [01 — liczby zespolone](01-liczby-zespolone.md), [02 — algebra liniowa](02-algebra-liniowa.md), [05 — podstawy mechaniki kwantowej](05-podstawy-mechaniki-kwantowej.md).

## 1. Po co to jest

Model obwodowy (ang. *circuit model*) to uniwersalny język współczesnej informatyki
kwantowej: każdy algorytm — od Deutscha po Shora — zapisujemy jako sekwencję bramek
działających na rejestrze kubitów i zakończonych pomiarem. W Olimpiadzie Kwantowej ten
język pojawia się wprost w zadaniach przykładowych **P3** (sekwencja H–Z–H na kubicie) i
**P4** (obwód dwukubitowy H, $R_Y(\theta)$, CNOT). Oba rozwiązujemy tu w całości w sekcji 4.

Rozdział domyka najważniejszą lukę między „fizyką kwantową” (rozdział 05) a „informatyką
kwantową” (rozdziały 08–10): pokazuje, jak **zapisać** ewolucję układu (iloczyn macierzy),
jak **odczytać** z niej przewidywania (prawdopodobieństwa) oraz jak postępować z **wieloma
kubitami**, gdzie kluczowa jest kolejność i sposób indeksowania (konwencja małoendianowa).
Bez tych trzech umiejętności każde zadanie obwodowe na finał stanie się zgadywaniem.

Szczególnie ważne jest **splątanie**: to ono odróżnia obliczenia kwantowe od klasycznych.
Pokazujemy je na dwóch stanach Bella uzyskanych w P4 i tłumaczymy, dlaczego obwód z P4 jest
„generatorem splątania” o regulowanej sile ($\theta$).

## 2. Najważniejsze definicje

- **Kubit (qubit):** układ o dwóch stanach bazowych $\lvert0\rangle,\lvert1\rangle$;
  stan to $\lvert\psi\rangle=\alpha\lvert0\rangle+\beta\lvert1\rangle$, gdzie
  $\alpha,\beta\in\mathbb{C}$ i $\lvert\alpha\rvert^2+\lvert\beta\rvert^2=1$.
- **Baza obliczeniowa (computational basis):** $\{\lvert0\rangle,\lvert1\rangle\}$;
  ogólnie dla $n$ kubitów $\{\lvert k\rangle=\lvert q_{n-1}\dots q_0\rangle\}$,
  $k=0,\dots,2^n-1$.
- **Amplituda (amplitude):** współczynnik $c_k=\langle k\vert\psi\rangle$; prawdopodobieństwo
  wyniku $P(k)=\lvert c_k\rvert^2$ (reguła Borna).
- **Sfera Blocha (Bloch sphere):** geometryczna reprezentacja stanu jednego kubita punktem
  na sferze; dla stanu czystego $\lvert\vec r\rvert=1$.
- **Bramka (gate):** liniowa operacja unitarna $U$ ($U^\dagger U=I$) działająca na stan.
- **Obwód kwantowy (quantum circuit):** uporządkowana w czasie sekwencja bramek na
  rejestrze kubitów, zakończona pomiarem.
- **Iloczyn tensorowy:** dla dwóch operatorów $A,B$ operator $A\otimes B$; stan dwukubitowy
  $\lvert a\rangle\otimes\lvert b\rangle$ zapisujemy krótko $\lvert ab\rangle$.
- **Stan iloczynowy (product state):** taki, który da się zapisać jako
  $\lvert\psi_1\rangle\otimes\lvert\psi_2\rangle$.
- **Stan splątany (entangled state):** stan niebędący żadnym stanem iloczynowym.
- **Pomiar rzutowy (projective / von Neumanna):** pomiar w bazie ortonormalnej
  $\{\lvert m\rangle\}$: $P(m)=\lvert\langle m\vert\psi\rangle\rvert^2$; po pomiarze
  stan przeskakuje do $\lvert m\rangle$.
- **Pomiar częściowy (partial measurement):** zmierzenie tylko części kubitów rejestru.

## 3. Teoria krok po kroku

### 3.1 Kubit i sfera Blocha

Każdy stan czysty jednego kubita można zapisać w postaci parametrycznej
$$\lvert\psi(\theta,\varphi)\rangle=\cos\frac{\theta}{2}\,\lvert0\rangle+e^{i\varphi}\sin\frac{\theta}{2}\,\lvert1\rangle,$$
gdzie $\theta\in[0,\pi]$ to kąt od osi $z$, a $\varphi\in[0,2\pi)$ to faza. **Skąd to się
bierze:** z rozwiązania warunku normalizacji $\lvert\alpha\rvert^2+\lvert\beta\rvert^2=1$ —
dowolne $(\alpha,\beta)$ leżą na sferze jednostkowej w $\mathbb{C}^2$; globalna faza jest
nieobserwowalna, więc pozostają dwa rzeczywiste parametry. Dla $\theta=0$: $\lvert0\rangle$;
$\theta=\pi/2,\varphi=0$: $\lvert+\rangle$; $\theta=\pi$: $\lvert1\rangle$.

Wektor Blocha $\vec r=(r_x,r_y,r_z)$ odczytujemy z wartości oczekiwanych macierzy Pauliego:
$$r_x=\langle X\rangle,\quad r_y=\langle Y\rangle,\quad r_z=\langle Z\rangle,\qquad
\lvert\psi\rangle\ \text{czysty}\iff \lvert\vec r\rvert=1.$$
Zapis macierzowy: $\rho=\tfrac12(I+\vec r\cdot\vec\sigma)$. Bieguny sfery to $\lvert0\rangle$
i $\lvert1\rangle$ (stany własne $Z$), a równik — superpozycje z równymi modułami ($\lvert+\rangle$,
$\lvert-\rangle$, stany własne $X$ i $Y$).

### 3.2 Bramki jednokubitowe

Wszystkie macierze w bazie $\{\lvert0\rangle,\lvert1\rangle\}$ (por. `docs/03-konwencje-i-notacja.md`, tabela 2.4):

| Bramka | Macierz | Uwaga |
| --- | --- | --- |
| $I$ | $\mathrm{diag}(1,1)$ | nic nie robi |
| $X$ | $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ | NOT kwantowy, $X=HZH$ |
| $Y$ | $\begin{pmatrix}0&-i\\i&0\end{pmatrix}$ | $Y=iXZ$ |
| $Z$ | $\mathrm{diag}(1,-1)$ | faza $\pi$ na $\lvert1\rangle$ |
| $H$ | $\tfrac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ | $H^2=I$ |
| $S$ | $\mathrm{diag}(1,i)$ | $S^2=Z$, $S=T^2$ |
| $T$ | $\mathrm{diag}(1,e^{i\pi/4})$ | faza $\pi/8$ |
| $R_X(\theta)$ | $\begin{pmatrix}\cos\frac{\theta}{2}&-i\sin\frac{\theta}{2}\\-i\sin\frac{\theta}{2}&\cos\frac{\theta}{2}\end{pmatrix}$ | obrót $\theta$ wokół $X$ |
| $R_Y(\theta)$ | $\begin{pmatrix}\cos\frac{\theta}{2}&-\sin\frac{\theta}{2}\\\sin\frac{\theta}{2}&\cos\frac{\theta}{2}\end{pmatrix}$ | obrót $\theta$ wokół $Y$ |
| $R_Z(\theta)$ | $\mathrm{diag}(e^{-i\theta/2},e^{i\theta/2})$ | obrót $\theta$ wokół $Z$ |

**Zapamiętaj dwie tożsamości** (sprawdzone macierzowo): $HZH=X$ oraz $HXH=Z$ — Hadamard
„zamienia” osie $X$ i $Z$. Ponadto $T^2=S$, $S^2=Z$, a $H=X\,R_Y(\pi/2)$. Bramki $S$ i $T$
wprowadzają fazę **bez zmiany prawdopodobieństw** w bazie obliczeniowej, dlatego są kluczowe
przy interferencji (rozdział 08).

### 3.3 Bramki dwukubitowe

Podstawowa bramka dwukubitowa to **CNOT** (controlled-NOT). W konwencji małoendianowej
stan zapisujemy $\lvert q_1 q_0\rangle$, gdzie $q_1$ to górny (starszy) kubit, a $q_0$
dolny. Bierzemy CNOT z **kontrolą na górnym kubicie ($q_1$) i celem na dolnym ($q_0$)** —
dokładnie jak w P4:
$$\mathrm{CNOT}=\lvert0\rangle\langle0\rvert\otimes I+\lvert1\rangle\langle1\rvert\otimes X
=\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix},$$
w bazie $(\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle)$. Działanie na
stany bazowe (kolumna = wejście, przejście = wyjście): $\lvert00\rangle\to\lvert00\rangle$,
$\lvert01\rangle\to\lvert01\rangle$, $\lvert10\rangle\to\lvert11\rangle$,
$\lvert11\rangle\to\lvert10\rangle$ — czyli „flip $q_0$, gdy $q_1=1$”.

Pozostałe bramki dwukubitowe:
$$\mathrm{CZ}=\mathrm{diag}(1,1,1,-1),\qquad
\mathrm{SWAP}=\begin{pmatrix}1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1\end{pmatrix},\qquad
\mathrm{iSWAP}=\begin{pmatrix}1&0&0&0\\0&0&i&0\\0&i&0&0\\0&0&0&1\end{pmatrix}.$$
**CZ** zmienia znak tylko $\lvert11\rangle$ (jest symetryczna względem zamiany kubitów).
**SWAP** wymienia stany obu kubitów. Relacja użyteczna w dowodach: $\mathrm{CNOT}=(I\otimes H)\,\mathrm{CZ}\,(I\otimes H)$.

### 3.4 Kolejność mnożenia w obwodzie

Obwód czytamy od lewej do prawej (czas rośnie w prawo), ale **mnożenie macierzy jest
odwrotne**: bramka wykonana *później* stoi *bardziej z lewej* w iloczynie. Dla sekwencji
$G_1$, potem $G_2$, potem $G_3$ na stanie $\lvert\psi\rangle$:
$$\lvert\psi'\rangle=G_3\,G_2\,G_1\,\lvert\psi\rangle.$$
Bramka na kubicie $q_0$ (dolnym) to $I\otimes G$ — bo $\lvert q_1q_0\rangle=\lvert q_1\rangle\otimes\lvert q_0\rangle$,
więc operator działający na prawym czynniku ma $I$ na lewym miejscu. Bramka na kubicie $q_1$
(górnym) to $G\otimes I$. **Zawsze jawnie deklarujemy konwencję**, bo dla $\ge 3$ kubitów
błąd w uporządkowaniu jest najczęstszą przyczyną złego wyniku.

### 3.5 Uniwersalność zbioru bramek

**Zbiór $\{H,T,\mathrm{CNOT}\}$ jest uniwersalny (approksymacyjnie):** dowolna operacja
unitarna na $n$ kubitach da się przybliżyć z dowolną dokładnością skończonym obwodem z tych
bramek. Szkic argumentu: (i) $\mathrm{CNOT}$ wraz z bramkami jednokubitowymi generuje wszystkie
bramki kontrolowane (sekcja 3.8); (ii) $H$ i $T$ generują gęstą podgrupę $SU(2)$, bo kąty ich
obrotów są niewspółmierne z $\pi$; (iii) twierdzenie Solovay–Kitaeva mówi, że przybliżenie
z dokładnością $\epsilon$ wymaga $O(\log^c(1/\epsilon))$ bramek. Zbiór $\{H,T,S,\mathrm{CNOT}\}$
zawiera więc wszystko, czym się posługujemy; bramki $X,Y,Z$ są w nim pośrednio obecne.

> **Ponad program:** zbiór **Clifforda** $\{H,S,\mathrm{CNOT}\}$ sam nie jest uniwersalny —
> generuje tylko skończoną grupę operacji i daje się efektywnie symulować klasycznie
> (tw. Gottesmana–Knilla). Dopiero dodanie bramki $T$ „wypycha” obliczenia poza klasyczny
> zasięg. Dlatego koszt implementacji liczby bramek $T$ ($T$-count) jest kluczową metryką.

### 3.6 Pomiar

**Pomiar w bazie obliczeniowej.** Dla $\lvert\psi\rangle=\sum_k c_k\lvert k\rangle$ mamy
$P(k)=\lvert c_k\rvert^2$, a stan po pomiarze zapada się do $\lvert k\rangle$. Wartość
oczekiwana obserwabli $A=\sum_a a\,\lvert a\rangle\langle a\rvert$ to
$\langle A\rangle=\sum_a a\,P(a)$ — **nie** mylimy pojedynczego wyniku z wartością oczekiwaną.

**Pomiar w dowolnej bazie** $\{\lvert m\rangle=U\lvert 0\rangle,\ U\lvert1\rangle\}$ realizujemy
obwodowo: wykonaj $U^\dagger$, zmierz w bazie obliczeniowej. Bo
$\lvert\langle m\vert\psi\rangle\rvert^2=\lvert\langle 0\rvert U^\dagger\lvert\psi\rangle\rvert^2$.
Np. pomiar w bazie $X$ ($\{\lvert+\rangle,\lvert-\rangle\}$) to sekwencja $H$ i pomiar.

**Pomiar częściowy.** Mierząc tylko jeden kubit ze stanu $\lvert\psi\rangle=\sum c_{ij}\lvert ij\rangle$,
dostajemy wynik $i$ z prawdopodobieństwem $P(i)=\sum_j\lvert c_{ij}\rvert^2$, a stan redukuje się do
$\lvert\psi_i\rangle=\frac{1}{\sqrt{P(i)}}\sum_j c_{ij}\lvert j\rangle$ (dla drugiego kubita).

### 3.7 Stany Bella i splątanie

Cztery **stany Bella** (maksymalnie splątane, baza dwukubitowa):
$$\lvert\Phi^\pm\rangle=\tfrac{1}{\sqrt2}(\lvert00\rangle\pm\lvert11\rangle),\qquad
\lvert\Psi^\pm\rangle=\tfrac{1}{\sqrt2}(\lvert01\rangle\pm\lvert10\rangle).$$
Powstają z $\lvert00\rangle$ przez $H$ na górnym kubicie i $\mathrm{CNOT}$ (kontrola górny,
cel dolny). Sprawdzenie splątania: dla $\lvert\Phi^+\rangle$ nie istnieje rozkład
$(\alpha\lvert0\rangle+\beta\lvert1\rangle)\otimes(\gamma\lvert0\rangle+\delta\lvert1\rangle)$,
bo musiałoby zachodzić $\alpha\gamma=\beta\delta=1/\sqrt2$ i $\alpha\delta=\beta\gamma=0$
— sprzeczność. **Kryterium iloczynowości** dla $\lvert\psi\rangle=a\lvert00\rangle+b\lvert01\rangle+c\lvert10\rangle+d\lvert11\rangle$:
$\lvert\psi\rangle$ jest iloczynowy $\iff ad=bc$. Miarą splątania jest **concurrence**
(ang. *concurrence*) $C=2\lvert ad-bc\rvert$; $C=0$ dla iloczynu, $C=1$ dla stanu Bella.

### 3.8 Zasada odroczonego pomiaru i bramki kontrolowane-U

**Zasada odroczonego pomiaru (deferred measurement):** każdy pomiar pośredni można przesunąć
na koniec obwodu (z warunkowymi operacjami zastąpionymi operacjami kontrolowanymi), nie zmieniając
rozkładu wyników końcowych. Praktyczna konsekwencja: analizę obwodu można prowadzić na stanach
czystych, a pomiary dopisać na końcu.

**Kontrolowana-$U$.** Dla jednokubitowej $U$ definiujemy
$\Lambda(U)=\lvert0\rangle\langle0\rvert\otimes I+\lvert1\rangle\langle1\rvert\otimes U$
(kontrola to kubit górny). Kluczowy fakt: jeśli rozłożymy $U=e^{i\alpha}AXBXC$ przy $ABC=I$,
to (z dokładnością do fazy na kubicie kontrolnym)
$$\Lambda(U)=(I\otimes A)\,\mathrm{CNOT}\,(I\otimes B)\,\mathrm{CNOT}\,(I\otimes C),$$
gdzie $A,B,C$ działają na kubicie docelowym, a faza $e^{i\alpha}$ realizowana jest bramką
fazową na kubicie kontrolnym. **Przykład weryfikowalny rachunkiem:** dla $U=R_Y(\theta)$
bierzemy $A=R_Y(\theta/2)$, $B=R_Y(-\theta/2)$, $C=I$; wtedy $ABC=I$ oraz
$A\,X\,B\,X\,C=R_Y(\theta)$, a powyższy obwód daje dokładnie $\Lambda(R_Y(\theta))$.

Wielokrotne kontrole budujemy rekurencyjnie: jeśli $V^2=U$, to
$$C^{n}U=\big(C^{n-1}V\big)\cdot\big(C^{n-1}X\big)\cdot\big(C^{n-1}V^\dagger\big)\cdot\big(C^{n-1}X\big)\cdot\big(C^{n-1}V\big)$$
(gdzie $C^{n-1}$ działają na kontrolach $1,\dots,n-1$, a $X$ i $V$ na kubicie kontrolowanym).
Bramka Toffolego ($C^2X$) powstaje tak z $U=X$ oraz $V=\sqrt{X}=R_X(\pi/2)$.

> **Ponad program:** bramka **Toffolego** ($C^2X$) i **Fredkina** ($C^2\mathrm{SWAP}$) są
> uniwersalne w połączeniu z $H$; bramka Toffolego jest klasycznie odwracalna i pojawia się
> w korekcji błędów (rozdział 13).

## 4. Przykłady rozwiązane

### Przykład 1 (P3): sekwencja H–Z–H na jednym kubicie

**Dane.** Kubit startuje w $\lvert0\rangle$; wykonujemy kolejno $H$, $Z$, $H$;
$H=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, $Z=\mathrm{diag}(1,-1)$.

**Metoda.** Stan to $\lvert\psi\rangle=H\,Z\,H\lvert0\rangle$; najpierw policzymy $\lvert\psi\rangle$,
potem prawdopodobieństwa $P(k)=\lvert\langle k\vert\psi\rangle\rvert^2$; na koniec wyznaczymy macierz $HZH$.

**Rachunek.** Krok po kroku:
$$H\lvert0\rangle=\tfrac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)=\lvert+\rangle,\quad
Z\lvert+\rangle=\tfrac{1}{\sqrt2}(\lvert0\rangle-\lvert1\rangle)=\lvert-\rangle,\quad
H\lvert-\rangle=\lvert1\rangle.$$
Zatem $\lvert\psi\rangle=\lvert1\rangle$ i $P(0)=0$, $P(1)=1$.

Macierz złożenia (mnożymy od prawej, uwzględniając kolejność $H$, potem $Z$, potem $H$):
$$HZH=\tfrac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix}
=\tfrac12\begin{pmatrix}0&2\\2&0\end{pmatrix}=\begin{pmatrix}0&1\\1&0\end{pmatrix}=X.$$

**Wynik.** Stan przed pomiarem: $\lvert\psi\rangle=\lvert1\rangle$; **$P(0)=0$, $P(1)=1$**;
oraz **$HZH=X$**.

**Interpretacja.** Sekwencja H–Z–H to po prostu bramka NOT kwantowa: przygotowanie w $\lvert0\rangle$
i tej sekwencji daje pewny wynik „1”. Potwierdza to tożsamość $HZH=X$ — Hadamard sprzęga
konjugacyjnie $Z$ w $X$.

### Przykład 2 (P4): obwód dwukubitowy H–$R_Y(\theta)$–CNOT

**Dane.** Dwa kubity startują w $\lvert00\rangle$. Wykonujemy $H$ na górnym kubicie ($q_1$),
$R_Y(\theta)$ na dolnym ($q_0$), a następnie CNOT (kontrola $q_1$, cel $q_0$). Konwencja
małoendianowa: stan bazowy $\lvert q_1q_0\rangle$, bramka na $q_1$ to $G\otimes I$, na $q_0$ to $I\otimes G$.
$$R_Y(\theta)=\begin{pmatrix}\cos\frac\theta2&-\sin\frac\theta2\\ \sin\frac\theta2&\cos\frac\theta2\end{pmatrix}.$$

**Metoda.** Złożymy stan po obu „warstwowych” bramkach, zastosujemy CNOT (na wektorach bazowych),
a potem odczytamy amplitudy $c_{00},c_{01},c_{10},c_{11}$ i prawdopodobieństwa $P_{ij}=\lvert c_{ij}\rvert^2$.

**Rachunek.** Krok 1 (stan po $H\otimes R_Y(\theta)$):
$$\big(H\lvert0\rangle\big)\otimes\big(R_Y(\theta)\lvert0\rangle\big)
=\tfrac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)\otimes\Big(\cos\tfrac\theta2\lvert0\rangle+\sin\tfrac\theta2\lvert1\rangle\Big)
=\tfrac{1}{\sqrt2}\Big(\cos\tfrac\theta2\lvert00\rangle+\sin\tfrac\theta2\lvert01\rangle+\cos\tfrac\theta2\lvert10\rangle+\sin\tfrac\theta2\lvert11\rangle\Big).$$
Krok 2 (CNOT: $\lvert00\rangle\!\to\!\lvert00\rangle$, $\lvert01\rangle\!\to\!\lvert01\rangle$,
$\lvert10\rangle\!\to\!\lvert11\rangle$, $\lvert11\rangle\!\to\!\lvert10\rangle$):
$$\lvert\psi\rangle=\tfrac{1}{\sqrt2}\Big(\cos\tfrac\theta2\lvert00\rangle+\sin\tfrac\theta2\lvert01\rangle+\sin\tfrac\theta2\lvert10\rangle+\cos\tfrac\theta2\lvert11\rangle\Big).$$

Prawdopodobieństwa:
$$P_{00}=P_{11}=\tfrac12\cos^2\tfrac\theta2=\tfrac{1+\cos\theta}{4},\qquad
P_{01}=P_{10}=\tfrac12\sin^2\tfrac\theta2=\tfrac{1-\cos\theta}{4}.$$
Suma: $\tfrac{1+\cos\theta}{4}+\tfrac{1-\cos\theta}{4}+\tfrac{1-\cos\theta}{4}+\tfrac{1+\cos\theta}{4}=1$ ✓.

Prawdopodobieństwo zgodnych wyników: $P_{00}+P_{11}=\tfrac{1+\cos\theta}{2}=\cos^2\tfrac\theta2$.
Wartość oczekiwana $\langle Z\otimes Z\rangle$ (bo $Z\otimes Z=\mathrm{diag}(1,-1,-1,1)$):
$$\langle Z\otimes Z\rangle=P_{00}-P_{01}-P_{10}+P_{11}=\cos\theta.$$
Zgadza się to z $P(\text{zgodne})=\tfrac{1+\langle Z\otimes Z\rangle}{2}$.

Splątanie: concurrence $C=2\lvert c_{00}c_{11}-c_{01}c_{10}\rvert=\lvert\cos\theta\rvert$.

**Wynik.** Stan po CNOT: $\lvert\psi\rangle=\tfrac{1}{\sqrt2}\big(\cos\tfrac\theta2(\lvert00\rangle+\lvert11\rangle)+\sin\tfrac\theta2(\lvert01\rangle+\lvert10\rangle)\big)$;
**$P_{00}=P_{11}=\tfrac{1+\cos\theta}{4}$**, **$P_{01}=P_{10}=\tfrac{1-\cos\theta}{4}$**;
**$P(\text{zgodne})=\tfrac{1+\cos\theta}{2}$**, **$\langle Z\otimes Z\rangle=\cos\theta$**.

**Interpretacja.** To stan **splątany** dla każdego $\theta$ poza $\theta=\pi/2$ (wtedy $C=0$ i
stan jest iloczynem $\lvert+\rangle\otimes\lvert+\rangle$). Dla $\theta=0$: $P(\text{zgodne})=1$,
$\langle ZZ\rangle=1$, stan to $\lvert\Phi^+\rangle$ — idealna **korelacja**. Dla $\theta=\pi$:
$P(\text{zgodne})=0$, $\langle ZZ\rangle=-1$, stan to $\lvert\Psi^+\rangle$ — idealna
**antykorelacja**. Oba skrajne przypadki mają $C=1$ (maksymalne splątanie), a różni je tylko
znak korelacji. Dla $\theta=\pi/2$ splątanie znika — obwód nie tworzy już korelacji.

## 5. Typowe pułapki

1. **Odwrotna kolejność mnożenia.** Sekwencja na obwodzie $G_1,G_2$ daje $G_2G_1\lvert\psi\rangle$,
   nie $G_1G_2\lvert\psi\rangle$. Zawsze zapisuj iloczyn „od ostatniej bramki do pierwszej”.
2. **Zamiana miejsc w iloczynie tensorowym.** Bramka na dolnym kubicie to $I\otimes G$,
   na górnym $G\otimes I$. Pomylenie tych dwóch odwraca całe rozwiązanie.
3. **Zły stan bazowy.** Indeks $k$ stanu $\lvert q_1q_0\rangle$ to $q_0+2q_1$; nie utożsamiaj
   zapisu binarnego z „naturalną” kolejnością bitów.
4. **Amplituda vs prawdopodobieństwo.** $P=\lvert c\rvert^2$; dla $c$ zespolonego znak/faza
   nie wpływają na prawdopodobieństwo, ale wpływają na interferencję (i na wynik kolejnych bramek).
5. **Superpozycja to nie splątanie.** $\lvert+\rangle\otimes\lvert+\rangle$ jest superpozycją, ale
   nie jest splątane. Splątanie sprawdzaj kryterium $ad\ne bc$ (lub concurrence), nie „na oko”.
6. **Brak normalizacji po pomiarze częściowym.** Po zapadnięciu się stanu trzeba podzielić przez
   $\sqrt{P(\text{wynik})}$; inaczej norma $\ne 1$.
7. **$\theta$ vs $\theta/2$.** W $R_X,R_Y,R_Z$ macierz zawiera $\theta/2$; kąt geometryczny obrotu
   na sferze Blocha to $\theta$. Mieszanie ich to najczęstszy błąd w zadaniach typu P4.
8. **„CNOT kopiuje”.** Nie: CNOT splątuje, ale nie klonuje dowolnego stanu (tw. o zakazie
   klonowania, rozdział 07). Klonowanie działa tylko dla stanów bazowych.

## 6. Zadania (Z-06)

**Z-06.1.** Sfera Blocha i Hadamard.
(a) Wyznacz wektor Blocha stanów $\lvert+\rangle$ i $\lvert-\rangle$.
(b) Oblicz $R_X(\pi)$, $R_Y(\pi)$, $R_Z(\pi)$ i porównaj każdą z $X,Y,Z$ (podaj relację z fazą globalną).
(c) **[★]** Pokaż, że $H=\frac{1}{\sqrt2}(X+Z)$ i wywnioskuj, że $H$ jest (z dokładnością do fazy)
obrotem o $\pi$ wokół osi $(\hat x+\hat z)/\sqrt2$.

**Z-06.2.** Tożsamości bramek fazowych.
(a) Oblicz $SXS^\dagger$ i rozpoznaj wynik.
(b) Oblicz komutator $[H,S]=HS-SH$ i oceń, czy $H$ i $S$ komutują.
(c) Oblicz $TXT^\dagger$ i wyjaśnij, dlaczego fakt $TXT^\dagger\not\propto X$ czyni z $T$ bramkę
niedostępną w zbiorze Clifforda.

**Z-06.3.** Pomiar częściowy stanu Bella.
Niech $\lvert\Phi^+\rangle=\frac{1}{\sqrt2}(\lvert00\rangle+\lvert11\rangle)$.
(a) Podaj prawdopodobieństwo wyniku $q_0=0$ przy pomiarze dolnego kubita.
(b) Wyznacz unormowany stan po wyniku $q_0=0$.
(c) Uzasadnij, że pomiar jednego kubita w pełni determinuje wynik pomiaru drugiego, i podaj
$P(\text{zgodne})$.

**Z-06.4.** Sprzężenie Hadamardami.
(a) Zapisz macierz CNOT (kontrola $q_1$, cel $q_0$) w bazie $\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle$.
(b) Oblicz $(H\otimes H)\,\mathrm{CNOT}\,(H\otimes H)$ i zidentyfikuj otrzymaną bramkę.
(c) Sprawdź, że $\mathrm{CNOT}=(I\otimes H)\,\mathrm{CZ}\,(I\otimes H)$.

**Z-06.5.** Własności stanów Bella.
(a) Sprawdź ortonormalność czterech stanów Bella.
(b) Dla $\lvert\Psi^-\rangle=\frac{1}{\sqrt2}(\lvert01\rangle-\lvert10\rangle)$ sprawdź splątanie
kryterium $ad=bc$ i policz concurrence.
(c) Pokaż, że ślad częściowy $\mathrm{Tr}_{q_1}\lvert\Psi^-\rangle\langle\Psi^-\rvert=\frac12 I$.

**Z-06.6. [★]** Bramki kontrolowane.
(a) Pokaż, że $\Lambda(Z)=(I\otimes H)\,\mathrm{CNOT}\,(I\otimes H)$ (kontrola $q_1$).
(b) Podaj rozkład $ABC$ dla $U=R_Y(\theta)$ i opisz obwód $\Lambda(R_Y(\theta))$ z trzech obrotów i dwóch CNOT.
(c) Oblicz $\Lambda(R_Y(\pi/2))\,\lvert10\rangle$ i podaj prawdopodobieństwa obu wyników pomiaru dolnego kubita.

## 7. Wskazówki do zadań

- **Z-06.1.** $r_i=\langle i\rvert$-owe wartości oczekiwane macierzy Pauliego. W (b) pamiętaj, że
  $R_n(\pi)=-i\,(n\cdot\vec\sigma)$; w (c) porównaj $H$ ze wzorem $R_n(\theta)=\cos\frac\theta2 I-i\sin\frac\theta2\,n\cdot\vec\sigma$.
- **Z-06.2.** Mnoż macierze $2\times2$; w (b) komutator licz na macierzach, nie „ze wzoru”.
  W (c) sprawdź, czy $TXT^\dagger$ da się zapisać jako $e^{i\varphi}X$.
- **Z-06.3.** Amplituda przy $\lvert00\rangle$ to $1/\sqrt2$; po pomiarze zostaje tylko składnik zgodny
  z wynikiem, potem normalizacja.
- **Z-06.4.** Kolejność: bramka najpierw $H\otimes H$ z prawej. W (c) rozbij CNOT na
  $\lvert0\rangle\langle0\rvert\otimes I+\lvert1\rangle\langle1\rvert\otimes X$ i użyj $HXH=Z$.
- **Z-06.5.** W (c) ślad częściowy licz po drugim (górnym) kubicie: $\rho_{q_0}=\sum_{q_1}\langle q_1\rvert\rho\lvert q_1\rangle$.
- **Z-06.6.** W (b) użyj $A=R_Y(\theta/2)$, $B=R_Y(-\theta/2)$, $C=I$; w (c) podziałaj na $\lvert10\rangle$.

## 8. Co dalej

- **Teoria informacji kwantowej** — [rozdział 07](07-kwantowa-teoria-informacji.md): zakaz klonowania,
  entropia von Neumanna, kanały i dystans śladowy.
- **Algorytmy** — [rozdział 08](08-algorytmy-kwantowe.md): Deutsch, QFT, Grover, Shor (obwody z tego rozdziału).
- **Splątanie i Bella** — [rozdział 09](09-splatanie-i-twierdzenie-bella.md).
- **Kryptografia** — [rozdział 10](10-kryptografia-kwantowa.md): BB84 jako obwód pomiarowy.
- Macierze gęstości i kanały — [rozdział 17](17-ponad-program-macierze-gestosci-i-kanaly.md).
- Pełne rozwiązania zadań: [zadania/rozwiazania/rozwiazania-06.md](../zadania/rozwiazania/rozwiazania-06.md).
- Praca domowa: [PD-2](../praca-domowa/praca-domowa-02.md).

> **Weryfikacja numeryczna.** Wszystkie macierze w tym rozdziale (w tym $HZH=X$, macierz CNOT oraz
> obwód P4) policzono w NumPy; np. `np.allclose(H@Z@H, X)` daje `True`, a stan P4 dla $\theta=0$
> to wektor $(0{,}7071,\,0,\,0,\,0{,}7071)$ z $P(\text{zgodne})=1$ i $\langle Z\otimes Z\rangle=1$.
