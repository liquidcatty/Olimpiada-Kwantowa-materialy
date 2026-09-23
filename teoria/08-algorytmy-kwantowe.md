# 08. Podstawowe algorytmy kwantowe

> **Warsztat źródłowy:** „Podstawowe algorytmy kwantowe” (Krzysztof Kurowski).
> **Czas nauki:** ~7 h teorii + ~9 h zadań.
> **Wymagana wiedza wstępna:** [05 — podstawy mechaniki kwantowej](05-podstawy-mechaniki-kwantowej.md), [06 — kubity, bramki, obwody, pomiary](06-kubity-bramki-obwody-pomiary.md), [07 — kwantowa teoria informacji](07-kwantowa-teoria-informacji.md).

## 1. Po co to jest

Algorytmy kwantowe to „serce” Olimpiady Kwantowej: pokazują, **po co** w ogóle budujemy komputery
kwantowe. Zaczynamy od prostych problemów wyroczni (Deutsch, Deutsch–Jozsa, Bernstein–Vazirani,
Simon), przez transformatę Fouriera (QFT) i estymację fazy, po Grovera i Shora. Te same narzędzia —
superpozycja, wyrocznia i **interferencja** — łączą ten rozdział z teorią informacji (07),
splątaniem (09) i zaawansowanymi algorytmami (19).

Kluczowe pytanie brzmi: *jak* uzyskać przyspieszenie, skoro pomiar daje tylko $n$ bitów z $n$ kubitów?
Odpowiedź: odpowiednio ustawioną **interferencją** wzmacniamy amplitudy „dobrych” odpowiedzi, zanim
zmierzymy. Ten rozdział tłumaczy ten mechanizm na trzech poziomach: Deutscha (1 zapytanie zamiast 2),
Grovera (kwadratowe przyspieszenie) i Shora (wykładnicze, dzięki QFT).

## 2. Najważniejsze definicje

- **Model obwodowy:** rejestr $n$ kubitów, start $\lvert0\rangle^{\otimes n}$, unitarne bramki, pomiar.
- **Wyrocznia (oracle):** czarna skrzynka realizująca $U_f\lvert x\rangle\lvert y\rangle=\lvert x\rangle\lvert y\oplus f(x)\rangle$;
  liczymy **zapytania** do $U_f$ (query complexity).
- **Złożoność zapytań:** liczba wywołań $U_f$ potrzebna do rozwiązania problemu (dolna/optymalna).
- **Kick-back fazy (phase kickback):** jeśli $U_f\lvert x\rangle\lvert-\rangle=(-1)^{f(x)}\lvert x\rangle\lvert-\rangle$,
  to faza „wraca” na rejestr danych — podstawa Deutscha i DJ.
- **QFT (quantum Fourier transform):** $n$-kubitowy operator $\lvert j\rangle\mapsto\frac{1}{\sqrt N}\sum_k\omega^{jk}\lvert k\rangle$,
  $\omega=e^{2\pi i/N}$, $N=2^n$.
- **Estymacja fazy (phase estimation):** odczyt fazy $\varphi$ wartości własnej $U\lvert u\rangle=e^{2\pi i\varphi}\lvert u\rangle$.
- **Amplituda sukcesu (amplitude amplification):** bazowy schemat Grovera wzmacniania „dobrej” amplitudy.
- **Interferencja:** składanie amplitud z fazami; nieodłączne od przewagi kwantowej.

## 3. Teoria krok po kroku

### 3.1 Model obwodowy i wyrocznia

Problem wyroczni: dana jest funkcja $f:\{0,1\}^n\to\{0,1\}$ dostępna tylko przez $U_f$. Chcemy poznać
jej własność (np. czy jest stała) zużywając jak najmniej zapytań. Kwantowo wywołujemy $U_f$ **raz na
superpozycji** — ale to nie znaczy, że „widzimy wszystkie wartości”: pomiar jednego wyjścia daje jedno
$f(x)$. Sztuka polega na takim ułożeniu amplitud, by pojedynczy pomiar ujawnił własność globalną.

### 3.2 Algorytm Deutscha

**Problem.** $f:\{0,1\}\to\{0,1\}$: rozstrzygnąć, czy $f$ jest stała ($f(0)=f(1)$), czy zbalansowana
($f(0)\ne f(1)$). Klasycznie (deterministycznie) trzeba 2 zapytań; kwantowo **1**.

**Obwód.** $\lvert0\rangle\lvert1\rangle\to(H\otimes H)\to U_f\to(H\otimes I)\to$ pomiar pierwszego kubita.
Klucz: dla $\lvert-\rangle=\frac{1}{\sqrt2}(\lvert0\rangle-\lvert1\rangle)$ mamy
$U_f\lvert x\rangle\lvert-\rangle=(-1)^{f(x)}\lvert x\rangle\lvert-\rangle$ (**kick-back fazy**).

**Rachunek.** Na wejściu $(H\otimes H)\lvert0\rangle\lvert1\rangle=\lvert+\rangle\lvert-\rangle
=\frac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)\lvert-\rangle$. Po $U_f$:
$$\frac{1}{\sqrt2}\big((-1)^{f(0)}\lvert0\rangle+(-1)^{f(1)}\lvert1\rangle\big)\lvert-\rangle
=\pm\begin{cases}\lvert+\rangle\lvert-\rangle, & f\ \text{stała},\\ \lvert-\rangle\lvert-\rangle, & f\ \text{zbalansowana}.\end{cases}$$
Po $H$ na pierwszym kubicie: $\lvert+\rangle\to\lvert0\rangle$, $\lvert-\rangle\to\lvert1\rangle$.
Zatem **zmierzony pierwszy kubit: $0$ $\Rightarrow$ stała, $1$ $\Rightarrow$ zbalansowana**.

### 3.3 Algorytm Deutscha–Jozsy

**Problem.** $f:\{0,1\}^n\to\{0,1\}$ jest **stała** albo **zbalansowana** (równo $2^{n-1}$ zer i jedynek).
Klasycznie w najgorszym razie $2^{n-1}+1$ zapytań; kwantowo **1**.

**Obwód.** $\lvert0\rangle^{\otimes n}\lvert1\rangle\to(H^{\otimes n}\otimes H)\to U_f\to(H^{\otimes n}\otimes I)
\to$ pomiar rejestru $n$ kubitów. Dla $\lvert x\rangle$:
$$U_f\lvert x\rangle\lvert-\rangle=(-1)^{f(x)}\lvert x\rangle\lvert-\rangle.$$
Po pierwszej warstwie $H^{\otimes n}$ stan to $\frac{1}{\sqrt N}\sum_x\lvert x\rangle\lvert-\rangle$, $N=2^n$.
Po $U_f$: $\frac{1}{\sqrt N}\sum_x(-1)^{f(x)}\lvert x\rangle\lvert-\rangle$. Po $H^{\otimes n}$ amplituda
stanu $\lvert0\rangle^{\otimes n}$ wynosi
$$\frac{1}{N}\sum_x(-1)^{f(x)}=\begin{cases}\pm1, & f\ \text{stała},\\ 0, & f\ \text{zbalansowana}.\end{cases}$$
**Wynik:** $P(0\dots0)=1$ dla stałej, $0$ dla zbalansowanej — jedno zapytanie rozstrzyga.

### 3.4 Algorytm Bernsteina–Vaziraniego

**Problem.** $f(x)=s\cdot x\bmod2$ dla nieznanego $s\in\{0,1\}^n$ ($s\cdot x=\sum_i s_ix_i\bmod2$);
znaleźć $s$. Klasycznie trzeba $n$ zapytań; kwantowo **1**.

**Idea.** Po $H^{\otimes n}U_fH^{\otimes n}$ z kick-backiem fazowym dostajemy produkt stanów
$\lvert s_1\rangle\lvert s_2\rangle\cdots\lvert s_n\rangle$, bo $(-1)^{s\cdot x}$ wstawia fazę zależną
od bitu $s$. Pomiar wprost daje $s$ — to „Deutsch–Jozsa z odpowiedzią ilościową”.

### 3.5 Algorytm Simona

**Problem.** $f:\{0,1\}^n\to\{0,1\}^n$ spełnia $f(x)=f(y)\iff y=x\oplus s$; znaleźć $s$. Klasycznie
$\Omega(2^{n/2})$ zapytań; kwantowo $O(n)$ (wykładnicze przyspieszenie). Klucz: po $H^{\otimes n}U_f$
mierzony $x$ spełnia $x\cdot s=0\bmod2$; powtarzając $n-1$ razy i rozwiązując układ liniowy nad
$\mathbb{F}_2$ odtwarzamy $s$. Simon to historyczny poprzednik Shora.

### 3.6 Transformata Fouriera (QFT)

Dla $N=2^n$ definiujemy **dyskretną** QFT działającą na indeksie bazy:
$$\mathrm{QFT}\lvert j\rangle=\frac{1}{\sqrt N}\sum_{k=0}^{N-1}e^{2\pi i\,jk/N}\lvert k\rangle
\quad\Rightarrow\quad (\mathrm{QFT})_{jk}=\frac{1}{\sqrt N}\,\omega^{jk},\ \ \omega=e^{2\pi i/N}.$$
Macierz jest unitarna i symetryczna. **Jawne macierze:**

$n=1$ ($N=2$, $\omega=e^{i\pi}=-1$): $\mathrm{QFT}_1=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}=H$.

$n=2$ ($N=4$, $\omega=i$):
$$\mathrm{QFT}_2=\frac12\begin{pmatrix}1&1&1&1\\1&i&-1&-i\\1&-1&1&-1\\1&-i&-1&i\end{pmatrix}.$$

$n=3$ ($N=8$, $\omega=e^{i\pi/4}$): $(\mathrm{QFT}_3)_{jk}=\frac{1}{\sqrt8}\omega^{jk}$, np. pierwszy
wiersz/kolumna to $\frac{1}{\sqrt8}(1,1,1,1,1,1,1,1)$, a element $(1,1)$ to $\omega=e^{i\pi/4}$.

**Obwód** (weryfikowalny macierzowo): $\mathrm{QFT}_2=\mathrm{SWAP}\cdot(I\otimes H)\cdot \mathrm{CS}\cdot(H\otimes I)$,
gdzie $\mathrm{CS}=\mathrm{diag}(1,1,1,i)$ to kontrolowana-$S$ (kontrola $q_1$, cel $q_0$). Ogólnie:
warstwy $H$ i kontrolowanych faz $R_k=\mathrm{diag}(1,e^{2\pi i/2^k})$ plus odwrócenie kolejności
(SWAP) na końcu. Uwaga: powyższa macierz działa na naturalny indeks $j$ w konwencji małoendianowej;
końcowe odwrócenie kolejności w obwodzie odpowiada czynnikowi $\mathrm{SWAP}$ obecnemu w rozkładzie.

> **Ponad program:** QFT nie daje żadnej informacji „za darmo” — to jednostkowa zmiana bazy.
> Wartość jest w tym, że **dla funkcji okresowych** jej wynik jest skoncentrowany na kilku stanach
> (mało niezerowych amplitud), a dobra implementacja ma koszt $O(n^2)$ bramek (wersja bez
> aproksymacji $O(n\log n)$ — algorytm Coppersmitha).

### 3.7 Estymacja fazy

**Problem.** Dany unitary $U$ i jego stan własny $\lvert u\rangle$ z $U\lvert u\rangle=e^{2\pi i\varphi}\lvert u\rangle$,
$\varphi\in[0,1)$. Znaleźć $\varphi$ z dokładnością $t$ bitów.

**Obwód.** $t$ kubitów ancilla w $\lvert0\rangle^{\otimes t}$ + rejestr w $\lvert u\rangle$; warstwa $H^{\otimes t}$,
$t$ bramek kontrolowanych-$U^{2^{k}}$ (kontrola ancilla $k$), na końcu **odwrotna QFT** na ancillach
i pomiar. Wynik to $t$-bitowe przybliżenie $2^t\varphi$. To podprogram: Shora (znajdowanie rzędu),
HHL (układy równań), kwantowej symulacji.

**Dokładność.** Z $t$ kubitów otrzymujemy $\varphi$ z błędem $\le2^{-t}$; z prawdopodobieństwem
$\ge1-\epsilon$ potrzeba $t=\lceil\log_2(1/\epsilon)\rceil+O(1)$ bitów (wersja standardowa i tak
powtarzana dla pewności).

### 3.8 Algorytm Grovera

**Problem.** W bazie danych $N=2^n$ elementów znaleźć **jedno** wyróżnione rozwiązanie, mając wyrocznię
$O\lvert x\rangle=(-1)^{f(x)}\lvert x\rangle$ ($f(x)=1$ dla rozwiązania). Klasycznie $\sim N/2$ prób;
kwantowo $O(\sqrt N)$.

**Geometria.** Niech $\lvert\alpha\rangle=\frac{1}{\sqrt{N-1}}\sum_{x\ne x_0}\lvert x\rangle$ (zły podzbiór)
oraz $\lvert\beta\rangle=\lvert x_0\rangle$ (dobry). Stan początkowy $\lvert s\rangle=H^{\otimes n}\lvert0\rangle
=\sin\theta\lvert\beta\rangle+\cos\theta\lvert\alpha\rangle$ z $\sin\theta=1/\sqrt N$. Obwód Grovera to
**dwa odbicia**:
$$G=\underbrace{\big(2\lvert s\rangle\langle s\rvert-I\big)}_{\text{dyfuzja}}\underbrace{O}_{\text{wyrocznia}}.$$
Oba odbicia zachowują dwuwymiarową podprzestrzeń $\mathrm{span}\{\lvert\alpha\rangle,\lvert\beta\rangle\}$
i składają się na **obrót o kąt $2\theta$**. Po $k$ iteracjach
$$\lvert\psi_k\rangle=\sin\big((2k+1)\theta\big)\lvert\beta\rangle+\cos\big((2k+1)\theta\big)\lvert\alpha\rangle
\quad\Rightarrow\quad P_{\text{sukces}}=\sin^2\big((2k+1)\theta\big).$$
**Liczba iteracji.** Maksimum dla $(2k+1)\theta\approx\pi/2$, czyli
$$k_{\text{opt}}\approx\frac{\pi}{4\theta}-\frac12\xrightarrow{\ \theta\approx1/\sqrt N\ }\frac{\pi}{4}\sqrt N.$$
Dla $N=2^n$ błąd rośnie, gdy wykonamy zbyt wiele iteracji (stan przestrzeliwuje rozwiązanie).

**Przykład liczbowy.** $N=4$ ($n=2$), 1 iteracja: $\theta=\pi/6$ ($\sin\theta=1/2$), $3\theta=\pi/2$,
więc $P_{\text{sukces}}=1$ (dokładnie). Dla $N=1024$: $k_{\text{opt}}\approx\frac\pi4\sqrt{1024}=25{,}13$,
czyli $25$ iteracji daje $P\approx0{,}9995$.

### 3.9 Amplifikacja amplitud

Grover to szczególny przypadek **amplifikacji amplitud (amplitude amplification)**. Dla dowolnego
obwodu $A$ przygotowującego $\lvert\psi\rangle=A\lvert0\rangle$ o amplitudzie sukcesu $a=\langle\text{dobry}\rvert\psi\rangle$
stosujemy $Q=-A S_0 A^\dagger S_\chi$ (odbicia o $\lvert0\rangle$ i o zbiór dobry). Liczba iteracji
$\sim\frac{\pi}{4\sqrt a}$ — kwadratowe przyspieszenie względem $\sim1/a$. To przepis na wzmacnianie
odpowiedzi w algorytmach heurystycznych (QAOA/optymalizacja).

### 3.10 Algorytm Shora (przegląd)

**Cel.** Faktoryzacja $N$ (i równoważnie znajdowanie rzędu $r$ elementu $a$ modulo $N$).

**Znajdowanie rzędu.** Funkcja $f(x)=a^x\bmod N$ jest **okresowa** o okresie $r$ (najmniejszym
$r$ z $a^r\equiv1\bmod N$). Obwód Shora: przygotuj $\frac{1}{\sqrt Q}\sum_x\lvert x\rangle\lvert1\rangle$
(dla $Q\sim N^2$), policz $f$ w wyroczni ($Q$ bramek modularnego potęgowania), i **zastosuj QFT** do
rejestru $x$. Amplitudy koncentrują się na wielokrotnościach $\frac Qr$; pomiar $\Rightarrow$ estymata
$\frac{cQ}{r}$, z której (ułamki łańcuchowe) odtwarzamy $r$, potem dzielnik z $\gcd(a^{r/2}\pm1,N)$.

**Koszt.** $O(n^2)$ bramek dla modularnego potęgowania, $O(n\log n)$ dla QFT, $O(1)$ powtórzeń —
razem $O(n^3)$ (dla $N\sim2^n$). Klasyczny najlepszy algorytm (GNFS) to czas podwykładniczy
$\exp(O(n^{1/3}\log^{2/3}n))$, więc Shor jest **wykładniczo** lepszy dla dużych $N$.

**Konsekwencja.** Shor łamie RSA i kryptografię krzywych eliptycznych — stąd pilna potrzeba
kryptografii postkwantowej (rozdział 10).

### 3.11 Złożoność: klasyczna a kwantowa

| Problem | Klasycznie | Kwantowo | Zysk |
| --- | --- | --- | --- |
| Deutsch (2 wartości) | 2 zapytania | 1 zapytanie | ×2 |
| Deutsch–Jozsa | $2^{n-1}+1$ | 1 | wykładniczy |
| Bernstein–Vazirani | $n$ | 1 | ×$n$ |
| Simon | $\Omega(2^{n/2})$ | $O(n)$ | wykładniczy |
| Grover (przeszukiwanie) | $\Theta(N)$ | $O(\sqrt N)$ | kwadratowy |
| Shor (faktoryzacja) | podwykładniczo | $O(n^3)$ | wykładniczy |

**Query complexity (złożoność zapytań).** Dla Grovera udowodniono dolne ograniczenie $\Omega(\sqrt N)$
zapytań — przyspieszenie jest optymalne, nie da się zejść do $O(1)$.

### 3.12 Dlaczego szybkość jest w ogóle możliwa

**Nie** chodzi o „próbkowanie równoległe” ani o „sprawdzanie wszystkich $N$ możliwości naraz” —
pomiar daje tylko jeden wynik. Kluczem jest **interferencja** (ang. *interference*):

1. Przygotowujemy stan w **superpozycji** wszystkich możliwych wejść.
2. Wyrocznia (lub QFT) nadaje każdej amplitudzie **fazę zależną od funkcji**.
3. Dobrane bramki tak **dodają amplitudy**, że odpowiedzi poprawne wzmacniają się konstruktywnie,
   a niepoprawne — destruktywnie (kasują się).
4. Dopiero tak „ukształtowany” rozkład mierzymy; prawdopodobieństwo sukcesu jest zdominowane przez
   poprawne odpowiedzi.

Innymi słowy informacja o funkcji jest „wpisana” w **względne fazy**, a nie w prawdopodobieństwa
pojedynczych pomiarów — i to jest istota przewagi kwantowej. Tego samego mechanizmu używamy
w metrologii (rozdział 11) i w splątaniu (rozdział 09).

## 4. Przykłady rozwiązane

### Przykład 1: algorytm Deutscha dla konkretnej wyroczni

**Dane.** Niech $f(x)=x$, tj. $f(0)=0$, $f(1)=1$ (funkcja zbalansowana). Wyrocznia
$U_f\lvert x\rangle\lvert y\rangle=\lvert x\rangle\lvert y\oplus x\rangle$, czyli $U_f=\mathrm{CNOT}$.

**Metoda.** Przepis Deutscha: $\lvert0\rangle\lvert1\rangle\to(H\otimes H)\to U_f\to(H\otimes I)$.

**Rachunek.** Start $\lvert0\rangle\lvert1\rangle$. Po $H\otimes H$: $\lvert+\rangle\lvert-\rangle$.
Kick-back: $U_f\lvert x\rangle\lvert-\rangle=(-1)^x\lvert x\rangle\lvert-\rangle$, więc
$$U_f\lvert+\rangle\lvert-\rangle=\tfrac{1}{\sqrt2}\big((-1)^0\lvert0\rangle+(-1)^1\lvert1\rangle\big)\lvert-\rangle
=\tfrac{1}{\sqrt2}(\lvert0\rangle-\lvert1\rangle)\lvert-\rangle=\lvert-\rangle\lvert-\rangle.$$
Po $H$ na pierwszym kubicie: $H\lvert-\rangle=\lvert1\rangle$.

**Wynik.** Pomiar pierwszego kubita daje **$1$** z prawdopodobieństwem 1 — funkcja zbalansowana.
(Potwierdzone numerycznie: $P(1)=1{,}0$.)

**Interpretacja.** Jedno zapytanie wystarcza, choć klasycznie trzeba było „zajrzeć” do obu wartości.
Faza $(-1)^{f(x)}$ „zebrała” obie wartości i po Hadamardzie dała jednoznaczny wynik.

### Przykład 2: algorytm Grovera dla $N=4$ (2 kubity), jedno rozwiązanie

**Dane.** Baza 4 elementów $\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle$; rozwiązaniem
jest $\lvert x_0\rangle=\lvert00\rangle$. Wyrocznia $O=\mathrm{diag}(-1,1,1,1)$ (flipuje fazę $\lvert00\rangle$).

**Metoda.** Jedna iteracja Grovera: $\lvert s\rangle=H^{\otimes2}\lvert00\rangle$, potem wyrocznia $O$,
potem **dyfuzja** $D=H^{\otimes2}\big(2\lvert00\rangle\langle00\rvert-I\big)H^{\otimes2}$, na końcu pomiar.

**Rachunek.** Start: $\lvert s\rangle=\tfrac12(\lvert00\rangle+\lvert01\rangle+\lvert10\rangle+\lvert11\rangle)
=\tfrac12(1,1,1,1)^\mathsf{T}$.
Po wyroczni: $O\lvert s\rangle=\tfrac12(-1,1,1,1)^\mathsf{T}$.
Dyfuzja (względem średniej $\bar c=\tfrac{-1+1+1+1}{4}=\tfrac14$): amplitudy zmieniają się na
$c_i\mapsto 2\bar c-c_i$, czyli
$$D\,O\lvert s\rangle=2\cdot\tfrac14\begin{pmatrix}1\\1\\1\\1\end{pmatrix}-\frac12\begin{pmatrix}-1\\1\\1\\1\end{pmatrix}
=\frac12\begin{pmatrix}1\\1\\1\\1\end{pmatrix}+\frac12\begin{pmatrix}1\\-1\\-1\\-1\end{pmatrix}
=\begin{pmatrix}1\\0\\0\\0\end{pmatrix}.$$

**Wynik.** Po jednej iteracji $\lvert\psi\rangle=\lvert00\rangle$, więc **$P(\text{sukces})=1$**.
Zgodność z wzorem: $\sin\theta=1/\sqrt4=1/2\Rightarrow\theta=\pi/6$, a $P=\sin^2(3\theta)=\sin^2(\pi/2)=1$.

**Interpretacja.** Dla $N=4$ jedna iteracja Grovera jest **dokładna** — interferencja całkowicie
kasuje amplitudy złych wyników, a wzmacnia dobrą. Dla większych $N$ sukces jest już tylko
prawdopodobny ($P\approx0{,}9995$ dla $N=1024$, $25$ iteracji), a nadmiar iteracji psuje wynik.

## 5. Typowe pułapki

1. **„Kwantowy komputer sprawdza wszystkie możliwości naraz”.** Nie: uzyskujemy przewagę przez
   interferencję, a pomiar daje jeden wynik.
2. **Zapominanie o kick-backu fazy.** Bez $\lvert-\rangle$ na kubicie docelowym Deutsch/DJ nie działają;
   faza $(-1)^{f(x)}$ musi wrócić na rejestr danych.
3. **Zła normalizacja stanu po iteracjach.** W Groverze pilnuj $\sin^2+\cos^2=1$; łatwo zgubić $\sqrt N$.
4. **Odwrotna QFT.** W estymacji fazy potrzebujemy $\mathrm{QFT}^\dagger$, nie $\mathrm{QFT}$.
5. **Mylenie $N$ i $n$.** $N=2^n$ to rozmiar bazy, $n$ to liczba kubitów; $\sqrt N$ w Groverze,
   $\log N$ w Shorze.
6. **Zbyt wiele iteracji Grovera.** Po przekroczeniu $k_{\text{opt}}$ prawdopodobieństwo sukcesu
   **maleje** — to nie jest „im więcej, tym lepiej”.
7. **Utożsamianie QFT z „transformacją Hadamarda”.** Dla $n=1$ to $H$, ale ogólnie to pełna
   macierz Fouriera z fazami $\omega^{jk}$.

## 6. Zadania (Z-08)

**Z-08.1.** Deutsch.
(a) Zapisz obwód algorytmu Deutscha i wyjaśnij rolę $\lvert-\rangle$.
(b) Przeanalizuj przypadek $f(0)=f(1)=1$ i podaj wynik pomiaru.
(c) Wykaż, że klasycznie w najgorszym razie potrzeba 2 zapytań.

**Z-08.2.** Deutsch–Jozsa.
(a) Wyprowadź amplitudę stanu $\lvert0\rangle^{\otimes n}$ po obwodzie dla $f$ stałej i zbalansowanej.
(b) Dla $n=3$ i $f(x)=x_1\oplus x_2$ sprawdź, czy $f$ jest zbalansowana, i podaj wynik pomiaru.
(c) Ile zapytań klasycznie w najgorszym razie dla $n=3$?

**Z-08.3.** QFT.
(a) Zapisz $\mathrm{QFT}_2$ jawnie i sprawdź unitarność.
(b) Policz $\mathrm{QFT}_2\lvert j\rangle$ dla $j=1$ i podaj prawdopodobieństwa pomiaru.
(c) Sprawdź, że $\mathrm{QFT}_2=\mathrm{SWAP}\cdot(I\otimes H)\cdot\mathrm{CS}\cdot(H\otimes I)$ dla $\mathrm{CS}=\mathrm{diag}(1,1,1,i)$.

**Z-08.4.** Grover — geometria.
(a) Dla $N=8$ policz $\theta$ i optymalną liczbę iteracji $k_{\text{opt}}$.
(b) Podaj $P_{\text{sukces}}$ dla $k=1$ i $k=k_{\text{opt}}$.
(c) Co się dzieje dla $k$ większego niż $k_{\text{opt}}$? Podaj przykład $N=8$, $k=3$.

**Z-08.5.** Estymacja fazy i Shor.
(a) Opisz obwód estymacji fazy (komponenty i kolejność).
(b) Jaką rolę pełni odwrotna QFT?
(c) Wyjaśnij, jak estymacja fazy prowadzi do znajdowania rzędu w algorytmie Shora.

**Z-08.6. [★]** Dolna granica Grovera.
(a) Wyjaśnij, dlaczego przyspieszenie Grovera jest tylko kwadratowe.
(b) Zapisz, jaką liczbę zapytań potrzebuje algorytm klasycznie, a ile kwantowo, dla $N=10^6$.
(c) Uzasadnij, czemu nie da się rozwiązać tego problemu w $O(1)$ zapytań.

## 7. Wskazówki do zadań

- **Z-08.1.** W (b) faza $(-1)^{f(x)}$ jest taka sama dla $x=0,1$, więc pierwszy kubit zostaje na $\lvert+\rangle$
  i po $H$ daje $\lvert0\rangle$.
- **Z-08.2.** W (a) rozbij sumę $\sum_x(-1)^{f(x)}$ na dwa przypadki; w (b) sprawdź liczbę jedynek w tablicy $f$.
- **Z-08.3.** W (a) sprawdź $M^\dagger M=I$; w (b) policz $\frac12(1,i,-1,-i)^\mathsf{T}$ i kwadraty modułów.
- **Z-08.4.** W (a) $\sin\theta=1/\sqrt8$; w (c) użyj $P=\sin^2((2k+1)\theta)$.
- **Z-08.5.** W (b) QFT zamienia fazę $\varphi$ w położenie bitu; w (c) połącz $f(x)=a^x\bmod N$ z okresem $r$.
- **Z-08.6.** W (b) klasycznie $\sim N/2=5\cdot10^5$, kwantowo $\sim\frac\pi4\cdot10^3\approx785$ iteracji.

## 8. Co dalej

- **Splątanie i Bella** — [rozdział 09](09-splatanie-i-twierdzenie-bella.md).
- **Kryptografia** — [rozdział 10](10-kryptografia-kwantowa.md): dlaczego Shor grozi RSA.
- **Metrologia** — [rozdział 11](11-metrologia-kwantowa.md): informacja Fishera i granica Heisenberga.
- **Algorytmy zaawansowane** — [rozdział 19](19-ponad-program-algorytmy-zaawansowane-i-granice.md):
  teleportacja, HHL, Solovay–Kitaev.
- Pełne rozwiązania: [zadania/rozwiazania/rozwiazania-08.md](../zadania/rozwiazania/rozwiazania-08.md).
- Praca domowa: [PD-2](../praca-domowa/praca-domowa-02.md).

> **Weryfikacja numeryczna.** Obwody tego rozdziału policzono w NumPy: Deutsch dla $f(x)=x$ daje
> $P(\text{pierwszy}=1)=1{,}0$; macierz $\mathrm{QFT}_2$ ma błąd unitarności $<10^{-16}$; Grover dla $N=4$
> po jednej iteracji daje wektor $(1,0,0,0)$ ($P(\text{sukces})=1$).