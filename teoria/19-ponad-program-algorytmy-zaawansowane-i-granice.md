# 19. Algorytmy zaawansowane i granice obliczeń kwantowych

> **Ponad program:** rozdział wykracza poza listę warsztatów, bo domyka algorytmy (teleportacja,
> Shor, HHL), teoretyczne granice (Holevo, BQP) i kompilację obwodów (Solovay–Kitaev) — to tematy
> pytań finałowych „jak daleko to działa i dlaczego”.
> **Czas nauki:** ~8 h teorii + ~10 h zadań.
> **Wymagana wiedza wstępna:** [07 — kwantowa teoria informacji](07-kwantowa-teoria-informacji.md), [08 — algorytmy kwantowe](08-algorytmy-kwantowe.md), [09 — splątanie i Bella](09-splatanie-i-twierdzenie-bella.md), [17 — macierze gęstości i kanały](17-ponad-program-macierze-gestosci-i-kanaly.md), [18 — dekoherencja](18-ponad-program-splatanie-dekoherencja-termodynamika.md).

## 1. Po co to jest

Rozdział 08 podał algorytmy w wersji „działającej”: Deutscha–Jozsy, Simona, QFT, Grover, Shor.
Tutaj robimy trzy rzeczy, które na finale dają punkty:

1. **Domykamy rachunki** — teleportacja i supergęste kodowanie z jawnym przejściem przez bazę
   Bella, Shor z konkretną faktoryzacją $N=15$,
2. **Pokazujemy granice** — twierdzenie Holevo ($\chi\le S$), permutacyjne granice, dlaczego
   Grover nie da się przyspieszyć ponad $\Theta(\sqrt N)$,
3. **Tłumaczymy „przemysł”** — przewaga kwantowa, modele złożoności (P, NP, BQP, QMA) oraz
   kompilacja obwodów do zbioru Clifford$+T$ z twierdzeniem Solovaya–Kitaewa.

To rozdział o **odpowiedzialnych twierdzeniach**: komputer kwantowy nie rozwiązuje „wszystkiego”,
a każde przyspieszenie ma cenę w liczbie bramek i w głębokości obwodu.

## 2. Najważniejsze definicje

- **Teleportacja kwantowa (quantum teleportation)**: przeniesienie 1 kubita przez **pomiar Bella** (baza $\{\lvert\Phi^\pm\rangle,\lvert\Psi^\pm\rangle\}$) + 1 **e-bit** + 2 **bity klasyczne**.
- **Supergęste kodowanie (superdense coding)**: przesłanie 2 bitów klasycznych przez 1 kubit (odwrotność teleportacji).
- **Zakaz klonowania**: nie istnieje $U$ z $U\lvert\psi\rangle\lvert0\rangle=\lvert\psi\rangle\lvert\psi\rangle$ dla wszystkich $\lvert\psi\rangle$.
- **Znajdowanie rzędu (order finding)**: najmniejsze $r$ z $a^r\equiv1\pmod N$; daje dzielnik $\gcd(a^{r/2}-1,N)$.
- **QFT mod $q$**: $\mathrm{QFT}\lvert x\rangle=\tfrac{1}{\sqrt q}\sum_y e^{2\pi ixy/q}\lvert y\rangle$; dla $q=2^n$ obwód z bramek $H$ i faz.
- **Amplifikacja amplitud / kąt Grovera**: iteracja wyroczni + dyfuzji $2\lvert s\rangle\langle s\rvert-I$; $\sin\theta=1/\sqrt N$, $P=\sin^2((2k+1)\theta)$.
- **Optymalność Grovera**: $\Omega(\sqrt N)$ zapytań — dolne ograniczenie (Boyer i in., 1998).
- **Estymacja fazy (phase estimation)**: $\lvert0\rangle^{\otimes t}\lvert\psi\rangle\to\lvert\tilde\varphi\rangle\lvert\psi\rangle$ z $\varphi\approx\tilde\varphi/2^t$.
- **HHL / kwantowe Monte Carlo**: rozwiązanie $Ax=b$ na **stanie kwantowym** (zastrzeżenia!) oraz estymacja $\mathbb E f$ z przyspieszeniem kwadratowym.
- **Twierdzenie Holevo**: dla $\{p_i,\rho_i\}$ informacja z pomiaru $\chi\le S(\sum_ip_i\rho_i)\le\log_2d$; **tw. Mayersa**: BB84 jest bezwarunkowo bezpieczny.
- **Klasy złożoności / przewaga kwantowa**: P, BPP, BQP, NP, QMA; przewaga = empiryczne szybsze wykonanie zadania (supremacja losowania, boson sampling).
- **Solovay–Kitaev / Clifford$+T$**: każdą $U$ aproksymuje się do $\varepsilon$ w $\{H,S,\text{CNOT},T\}$ kosztem $O(\log^c(1/\varepsilon))$; liczy się **T-count**.
- **Gottesman–Knill / magic states**: obwody Clifforda są klasycznie symulowalne w czasie polinomialnym; uniwersalność wymaga „magicznych” stanów wstrzykiwanych pomiarem.

## 3. Teoria krok po kroku

### 3.1 Teleportacja kwantowa: pełny rachunek

**Ustawienie.** Alicja ma kubit 1 w nieznanym stanie $\lvert\psi\rangle=\alpha\lvert0\rangle+\beta\lvert1\rangle$;
Alicja i Bob dzielą parę $\lvert\Phi^+\rangle_{23}$ (kubit 2 u Alicji, 3 u Boba). Stan całości:
$$\lvert\Psi\rangle=\tfrac{1}{\sqrt2}\big(\alpha\lvert000\rangle+\alpha\lvert011\rangle
+\beta\lvert100\rangle+\beta\lvert111\rangle\big).$$
**Kluczowe podstawienie.** Wyrażamy $\lvert00\rangle_{12},\lvert11\rangle_{12},\lvert01\rangle_{12},\lvert10\rangle_{12}$
przez bazy Bella, np. $\lvert00\rangle_{12}=\tfrac{1}{\sqrt2}(\lvert\Phi^+\rangle+\lvert\Phi^-\rangle)$,
$\lvert11\rangle_{12}=\tfrac{1}{\sqrt2}(\lvert\Phi^+\rangle-\lvert\Phi^-\rangle)$,
$\lvert01\rangle_{12}=\tfrac{1}{\sqrt2}(\lvert\Psi^+\rangle+\lvert\Psi^-\rangle)$,
$\lvert10\rangle_{12}=\tfrac{1}{\sqrt2}(\lvert\Psi^+\rangle-\lvert\Psi^-\rangle)$. Po uporządkowaniu:
$$\lvert\Psi\rangle=\tfrac12\Big[\lvert\Phi^+\rangle_{12}\underbrace{(\alpha\lvert0\rangle+\beta\lvert1\rangle)}_3
+\lvert\Phi^-\rangle_{12}(\alpha\lvert0\rangle-\beta\lvert1\rangle)_3
+\lvert\Psi^+\rangle_{12}(\beta\lvert0\rangle+\alpha\lvert1\rangle)_3
+\lvert\Psi^-\rangle_{12}(-\beta\lvert0\rangle+\alpha\lvert1\rangle)_3\Big].$$
**Wniosek.** Każdy z czterech wyników pomiaru Bella zdarza się z $P=\tfrac14$, a stan Boba różni
się od $\lvert\psi\rangle$ co najwyżej bramką Pauliego: dla $\lvert\Phi^+\rangle\to I$,
$\lvert\Phi^-\rangle\to Z$, $\lvert\Psi^+\rangle\to X$, $\lvert\Psi^-\rangle\to ZX$.
Po przesłaniu **2 bitów** klasycznych (informujących, który wynik) Bob odtwarza dokładnie
$\lvert\psi\rangle$. Oryginał zostaje zniszczony przez pomiar — dlatego teleportacja **nie**
łamie zakazu klonowania.

### 3.2 Supergęste kodowanie: odwrotność teleportacji

Alicja i Bob dzielą $\lvert\Phi^+\rangle_{AB}$. Alicja stosuje do **swojego** kubita jedną z bramek
$\{I,X,Z,ZX\}$ zależnie od 2 bitów, które chce wysłać, i **przesyła swój kubit** Bobowi:
$$(I\otimes I)\lvert\Phi^+\rangle=\lvert\Phi^+\rangle,\quad
(X\otimes I)\lvert\Phi^+\rangle=\lvert\Psi^+\rangle,\quad
(Z\otimes I)\lvert\Phi^+\rangle=\lvert\Phi^-\rangle,\quad
(ZX\otimes I)\lvert\Phi^+\rangle=-\lvert\Psi^-\rangle .$$
Bob zna bazę Bella, więc odczytuje dokładnie 2 bity z **jednego** kubita. To wymiana: w
teleportacji 1 e-bit + 2 bity klasyczne przenosi 1 kubit; tutaj 1 e-bit + 1 przesłany kubit
przenosi 2 bity.

### 3.3 Zakaz klonowania jako granica

Jeśli istniałoby $U$ klonujące ($U\lvert\psi\rangle\lvert0\rangle=\lvert\psi\rangle\lvert\psi\rangle$
dla każdego $\lvert\psi\rangle$), to z liniowości dla $\lvert+\rangle=\tfrac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)$
dostalibyśmy $\lvert+\rangle\lvert+\rangle$ zamiast $\tfrac{1}{\sqrt2}(\lvert00\rangle+\lvert11\rangle)$ —
sprzeczność. **Konsekwencje praktyczne**: nie da się skopiować nieznanego stanu (bezpieczeństwo QKD),
nie da się „zapisać” wyniku kwantowego bez pomiaru, a kopiowanie **bazy** (bity $0/1$) jest możliwe —
to jest różnica między informacją klasyczną a kwantową.

### 3.4 Algorytm Shora: znajdowanie rzędu i faktoryzacja

**Krok 1 — redukcja.** Faktoryzacja $N$ sprowadza się do znalezienia **rzędu** $r$ liczby $a$
($1<a<N$, $\gcd(a,N)=1$): najmniejszego $r$ z $a^r\equiv1\pmod N$. Jeśli $r$ jest parzyste i
$a^{r/2}\not\equiv-1\pmod N$, to
$$\gcd\big(a^{r/2}-1,\ N\big)\ \text{ oraz }\ \gcd\big(a^{r/2}+1,\ N\big)$$
są nietrywialnymi dzielnikami $N$ (tożsamość $a^r-1=(a^{r/2}-1)(a^{r/2}+1)$).

**Krok 2 — obwód kwantowy.** Przygotowujemy $\tfrac{1}{\sqrt q}\sum_{x=0}^{q-1}\lvert x\rangle\lvert0\rangle$
dla $q=2^n$ (typowo $N^2\le q<2N^2$), liczymy $\lvert x\rangle\to\lvert x\rangle\lvert a^x\bmod N\rangle$
(odwracalnie, przez kontrolowane mnożenia), a następnie stosujemy **odwrotną QFT** mod $q$ na
pierwszym rejestrze. Pomiar drugiego rejestru rzutuje pierwszy na superpozycję $x\equiv x_0\pmod r$:
$$\frac{1}{\sqrt{q/r}}\sum_{j=0}^{q/r-1}\lvert x_0+jr\rangle .$$
Po QFT amplitudy koncentrują się na wielokrotnościach $q/r$, więc pomiar daje $m\approx s\,q/r$.

**Krok 3 — odczyt $r$.** Z $m/q\approx s/r$ znajdujemy $r$ przez **rozwinięcie w ułamek łańcuchowy**.

**Przykład ($N=15$).** Dla $a=7$: $7^1\equiv7$, $7^2=49\equiv4$, $7^3\equiv13$, $7^4\equiv1$, więc $r=4$.
Wtedy $7^{2}=49\equiv4$ i $\gcd(4-1,15)=\gcd(3,15)=3$, a $15/3=5$. Dla $a=11$: $11^2=121\equiv1$,
czyli $r=2$ i $\gcd(11-1,15)=\gcd(10,15)=5$ (a stąd $3$). Zauważmy, że $a=14$ daje $r=2$ i
$\gcd(13,15)=1$ — to pechowy przypadek, trzeba wybrać inne $a$.

**Powtórzenia i prawdopodobieństwo.** Dla losowego $a$ „dobry” przypadek (parzyste $r$ i
$a^{r/2}\not\equiv-1$) zachodzi z prawdopodobieństwem $\ge\tfrac12$, więc kilka powtórzeń daje
sukces z prawdopodobieństwem bliskim 1. Złożoność: $O(n^3)$ bramek (z $q\approx N^2$, $n=\log_2N$)
wobec subeksponialnego najlepszego klasycznego **sita GNFS** ($\exp O(n^{1/3}\log^{2/3}n)$).

### 3.5 Grover: amplifikacja amplitud i optymalność

Dla $N$ stanów bazowych i jednego wyróżnionego, zaczynając od równomiernej superpozycji
$\lvert s\rangle$, kąt spełnia $\sin\theta=1/\sqrt N$, a po $k$ iteracjach
$$P_{\rm sukces}(k)=\sin^2\big((2k+1)\theta\big),\qquad
k_{\rm opt}=\mathrm{round}\Big(\tfrac{\pi}{4}\sqrt N-\tfrac12\Big).$$
Geometrycznie każda iteracja to **dwa odbicia**: od wyróżnionego stanu (wyrocznia) i od $\lvert s\rangle$
(dyfuzja $2\lvert s\rangle\langle s\rvert-I$) — suma dwóch odbić to obrót o $2\theta$.

**Optymalność.** Każdy algorytm kwantowy szukający w „czarnej skrzynce” potrzebuje $\Omega(\sqrt N)$
zapytań — dolne ograniczenie (Boyer, Brassard, Høyer, Tapp, 1998) pokazuje, że Grover jest
**optymalny co do rzędu**. Dla $N=10^6$: $k_{\rm opt}=785$ wobec średnio $\tfrac N2=5\cdot10^5$
zapytań klasycznych.

**Amplifikacja amplitud** uogólnia Grovera: jeśli wyrocznia „zaznacza” stan o nieznanej amplitudzie
$a$, to $O(1/\lvert a\rvert)$ iteracji doprowadza do $P\approx1$. To narzędzie wielu algorytmów
(np. kwantowe wyszukiwanie, Monte Carlo, szacowanie liczby rozwiązań).

### 3.6 Estymacja fazy jako uniwersalne narzędzie

Dla macierzy unitarnej $U$ i jej stanu własnego $U\lvert u\rangle=e^{2\pi i\varphi}\lvert u\rangle$
chcemy poznać $\varphi\in[0,1)$. Obwód: rejestr $t$ kubitów w $\lvert0\rangle^{\otimes t}$, operacje
kontrolowane $U^{2^j}$ ($j=0,\dots,t-1$) i **odwrotna QFT**. Wynik $m$ daje przybliżenie
$\varphi\approx m/2^t$ z dokładnością $\sim2^{-t}$. Estymacja fazy jest sercem **znajdowania rzędu**
(użytego w Shorze) i **HHL**; to jedno z najważniejszych „prymitywów” programowania kwantowego.

### 3.7 HHL: układy równań liniowych i jego zastrzeżenia

Problem: rozwiązać $A\lvert x\rangle=\lvert b\rangle$ dla rzadkiej, hermitowskiej, dobrze
uwarunkowanej $A$ (współczynnik uwarunkowania $\kappa$). Algorytm HHL:
$$\lvert b\rangle\ \xrightarrow{\text{estymacja fazy }e^{iAt}}\ \sum_j\beta_j\lvert\lambda_j\rangle\lvert\lambda_j\rangle
\ \xrightarrow{\text{odwrócenie własności}}\ \sum_j\beta_j\lambda_j^{-1}\lvert\lambda_j\rangle\lvert0\rangle
=\lvert x\rangle .$$
Złożoność $O(\log N\cdot\kappa^2/\varepsilon)$ na **kwantowy** stan $\lvert x\rangle$.

**Zastrzeżenia (o to pyta się na finale):** (1) wynikiem jest **stan kwantowy** — odczyt $N$ amplitud
kosztuje $O(N)$ pomiarów; (2) potrzebna jest wydajna symulacja $e^{iAt}$ i małe $\kappa$; (3) algorytm
nadaje się do pytań o cechy $\langle x\rvert M\lvert x\rangle$, nie do pełnego rozwiązania.

### 3.8 Kwantowe Monte Carlo

Klasyczna estymacja wartości oczekiwanej $\mathbb E f$ z dokładnością $\varepsilon$ wymaga
$O(1/\varepsilon^2)$ próbek (prawo $\sqrt N$). **Kwantowe Monte Carlo** (Montanaro, 2015) używa
amplifikacji amplitud i estymacji fazy, osiągając $O(1/\varepsilon)$ zapytań — **przyspieszenie
kwadratowe**. Ograniczenie jest fundamentalne (jak w Groverze): dokładność kwadratowa mieści się w
granicy $\Omega(\sqrt N)$ na liczbę zapytań o wyrocznię.

### 3.9 Granice informacyjne: Holevo, Bella, Mayers

**Twierdzenie Holevo.** Dla zbioru $\{p_i,\rho_i\}$ informacja dostępna w dowolnym pomiarze spełnia
$$\chi=S\Big(\sum_ip_i\rho_i\Big)-\sum_ip_iS(\rho_i)\ \le\ S\Big(\sum_ip_i\rho_i\Big)\ \le\ \log_2d .$$
**Przykład.** $\{\tfrac12,\lvert0\rangle;\ \tfrac12,\lvert+\rangle\}$: $\rho_{\rm avg}=\begin{pmatrix}0{,}75&0{,}25\\0{,}25&0{,}25\end{pmatrix}$
ma wartości własne $0{,}8536,0{,}1464$, więc $\chi\le S=0{,}6009$ bita — **mniej** niż 1 bit, mimo
dwóch „pół-bitowych” komunikatów. To dlatego $n$ kubitów nie daje $2n$ bitów klasycznych.

**Nierówność Bella jako zasób.** Naruszenie CHSH ($\lvert S\rvert>2$) **certyfikuje** splątanie
niezależnie od modelu urządzeń — to podstawa *device-independent* QKD (rozdział 09).

**Twierdzenie Mayersa.** BB84 jest bezpieczny (poprawny i tajny) przy dowolnym ataku zgodnym z
prawami fizyki, bez założeń o mocy obliczeniowej Eve — bezpieczeństwo **nieuwarunkowane** (rozdział 10).

### 3.10 Złożoność: BQP, P, NP, QMA i „przewaga kwantowa”

| Klasa | Znaczenie |
| --- | --- |
| **P** | rozwiązywalne klasycznie w czasie polinomialnym |
| **BPP** | klasycznie z błędem $\le1/3$ („praktycznie P”) |
| **BQP** | rozwiązywalne na komputerze kwantowym w czasie polinomialnym, błąd $\le1/3$ |
| **NP** | weryfikowalne klasycznie w czasie polinomialnym |
| **QMA** | kwantowy odpowiednik NP (kwantowy dowód, kwantowa weryfikacja) |

Znane relacje: $\mathrm{P}\subseteq\mathrm{BPP}\subseteq\mathrm{BQP}\subseteq\mathrm{PSPACE}$; nie wiadomo, czy
$\mathrm{NP}\subseteq\mathrm{BQP}$ (panuje zgoda, że **nie**). Faktoryzacja i logarytm dyskretny $\in$ BQP,
ale **nie są** znane jako NP-zupełne; problem lokalnego Hamiltona jest **QMA-zupełny**.

**Przewaga kwantowa (quantum advantage)** to *empiryczne* wykonanie zadania szybciej niż najlepszy
algorytm klasyczny. Przykłady: **losowanie losowych obwodów** (supremacja, Arute i in., Nature 2019)
oraz **boson sampling** (Zhong i in., Science 2020). To zadania **próbkowania**, nie „użyteczne”
obliczenia — dlatego raportuje się je ostrożnie.

**Mity i nadużycia:**
- „komputer kwantowy rozwiąże wszystko” — przyspieszenia są **zadaniowe** i często tylko kwadratowe;
- „Grover da wykładnicze przyspieszenie” — nie, tylko $\sqrt N$;
- „Shor złamie każdą kryptografię” — łamie RSA/ECC, a nie np. kryptografię postkwantową;
- „przewaga kwantowa = użyteczny komputer” — supremacja dowodzi *czegoś* o mocach, nie o aplikacjach.

### 3.11 Kompilacja obwodów: Solovay–Kitaev, Clifford$+T$, magic states

Sprzęt realizuje ograniczony zbiór bramek; teoretycy mówią o **uniwersalnym** zbiorze
$\{H,T,\text{CNOT}\}$. Bramki **Clifforda** ($\{H,S,\text{CNOT}\}$) można symulować klasycznie w
czasie polinomialnym (**twierdzenie Gottesmana–Knilla**, formalizm stabilizatorów); cała „kwantowa
trudność” siedzi w bramkach nie-Cliffordowskich, najlepiej w jednej — $T$.

**Twierdzenie Solovaya–Kitaewa.** Dla dowolnego zbioru uniwersalnego każdą operację unitarną $U$
można aproksymować do dokładności $\varepsilon$ (w normie operatorowej) obwodem o długości
$O(\log^{c}(1/\varepsilon))$; w praktyce liczba bramek $T$ (T-count) rośnie jak $\approx3\log_2(1/\varepsilon)$:
$$\varepsilon=10^{-3}\to\approx30,\quad10^{-6}\to\approx60,\quad10^{-10}\to\approx100 .$$
Dlatego w erze NISQ raportuje się **T-count** i **głębokość** obwodu — to one decydują o koszcie.

**Odporność na błędy (fault tolerance).** Obwód fault-tolerant używa kodu korekcyjnego
(rozdział 13) i bramek Clifforda „za darmo” (transversalnie), a bramki $T$ realizuje przez
**magic states** — specjalny stan pomocniczy produkowany w procesie *destylacji* i wstrzykiwany
przez pomiar (*gate injection*). Magia $T$ nie znika: trzeba ją **wytworzyć** i **zweryfikować**,
co jest dziś jednym z głównych obciążeń kosztowych kompilacji.

## 4. Przykłady rozwiązane

### Przykład 19.1 (łatwy): teleportacja stanu $\tfrac{1}{\sqrt5}(2\lvert0\rangle+i\lvert1\rangle)$

**Dane.** $\alpha=\tfrac{2}{\sqrt5}$, $\beta=\tfrac{i}{\sqrt5}$; para $\lvert\Phi^+\rangle$; pomiar Bella.

**Metoda.** Rozkład z 3.1: cztery składniki z amplitudą $\tfrac12$.

**Rachunek.** Każdy wynik ma $P=\lvert\tfrac12\rvert^2=\tfrac14=0{,}25$. Stany Boba **przed** korektą:
$\lvert\Phi^+\rangle:(0{,}8944;0{,}4472i)$, $\lvert\Phi^-\rangle:(0{,}8944;-0{,}4472i)$,
$\lvert\Psi^+\rangle:(0{,}4472i;0{,}8944)$, $\lvert\Psi^-\rangle:(-0{,}4472i;0{,}8944)$.
Po korektach $I,Z,X,ZX$ — wszystkie dają $(\alpha,\beta)$; suma prawdopodobieństw $=1$.

**Odpowiedź:** $\mathbf{P(\Phi^+)=P(\Phi^-)=P(\Psi^+)=P(\Psi^-)=\tfrac14}$;
korekty $\mathbf{\{I,Z,X,ZX\}}$ odtwarzają $\mathbf{\lvert\psi\rangle=(0{,}8944;\ 0{,}4472i)}$.
*Interpretacja:* teleportacja przenosi **nieznany** stan bez jego pomiaru; potrzebny jest 1 e-bit i
2 bity klasyczne, a oryginał znika (zgodnie z zakazem klonowania).

### Przykład 19.2 (trudniejszy): Shor dla $N=15$

**Dane.** $N=15$; $q=16$ ($n=4$ kubity); $a=7$.

**Metoda.** Znajdowanie rzędu $\to$ QFT mod $q$ $\to$ ułamek łańcuchowy $\to$ NWD.

**Rachunek.** Rząd: $7^1\equiv7$, $7^2=49\equiv4$, $7^3\equiv13$, $7^4\equiv1\pmod{15}$, więc $r=4$.
Rejestr pierwszy po pomiarze drugiego jest równomierny na $\{x_0,x_0+4,x_0+8,x_0+12\}$; QFT daje piki
na wielokrotnościach $q/r=4$, czyli na $\{0,4,8,12\}$ z prawdopodobieństwem $\tfrac14$ każdy.
Pomiar $m=4$: $m/q=\tfrac14$, ułamek łańcuchowy $\to r=4$ (parzyste), $a^{r/2}=7^2\equiv4$,
$\gcd(4-1,15)=3$ oraz $15/3=5$.

**Odpowiedź:** $\mathbf{r=4}$, dzielniki $\mathbf{15=3\cdot5}$; prawdopodobieństwo każdego piku
QFT wynosi $\mathbf{0{,}25}$, sukces (dla tego $a$) jest **pewny**.
*Interpretacja:* kwantowy obwód nie „dzieli” liczby bezpośrednio — wykrywa **okresowość** funkcji
$a^x\bmod N$, a dzielenie wykonuje elementarna teoria liczb.

### Przykład 19.3 (średni): Grover i koszt kompilacji

**Dane.** (a) $N=10^6$ elementów, 1 rozwiązanie; (b) kompilacja bramki obrotu do dokładności
$\varepsilon=10^{-6}$.

**Rachunek.** (a) $\theta=\arcsin(10^{-3})=0{,}001$, stąd
$k_{\rm opt}=\mathrm{round}\big(\tfrac\pi4\cdot1000-\tfrac12\big)=785$; klasycznie średnio
$\sim5\cdot10^5$ zapytań, więc zysk $\approx637\times$.
(b) T-count $\approx3\log_2(10^{6})=3\cdot19{,}93=59{,}8$, czyli $\approx60$ bramek $T$.

**Odpowiedź:** (a) $\mathbf{k_{\rm opt}=785}$ iteracji ($\Theta(\sqrt N)$); (b) $\mathbf{\approx60}$ bramek $T$ dla $\varepsilon=10^{-6}$.
*Interpretacja:* Grover daje przyspieszenie **kwadratowe**, a każda bramka $T$ kosztuje — dlatego
optymalizacja obwodów to walka o T-count i głębokość, nie tylko o liczbę kubitów.

## 5. Typowe pułapki

1. **„Teleportacja kopiuje stan”.** Nie: oryginał jest **niszczony** przez pomiar Bella — przenoszona jest informacja, nie kopia.
2. **Zapominanie o kanałach klasycznych.** Bez 2 bitów klasycznych Bob nie wie, którą bramkę zastosować.
3. **Mylenie zasobów supergęstego kodowania.** 2 bity wymagają **e-bitu** *oraz* przesłania kubita.
4. **Mylenie rzędu z okresem funkcji.** $r$ to najmniejsze $a^r\equiv1$; okres superpozycji to wielokrotność $r$.
5. **Pechowe $a$ w Shorze.** Dla $a=14$, $N=15$: $r=2$, ale $\gcd(13,15)=1$ — trzeba powtórzyć.
6. **Nadmiar iteracji Grovera.** Dla $N=8$: $k=2$ daje $0{,}945$, a $k=3$ tylko $0{,}330$.
7. **Mylenie $\sqrt N$ z $N$.** Grover daje przyspieszenie **kwadratowe**, nie wykładnicze.
8. **Mylenie BQP z NP.** Faktoryzacja nie jest NP-zupełna, więc Shor **nie** rozwiązuje NP-zupełnych.
9. **HHL jako „solver”.** Algorytm zwraca **stan kwantowy**; odczyt pełnego $x$ niweczy przyspieszenie.
10. **Mylenie T-count z liczbą kubitów.** Kompilacja do Clifforda$+T$ liczy **bramki**, nie kubity.

## 6. Zadania (Z-19)

**Z-19.1.** Teleportacja.
(a) Rozłóż $\lvert\psi\rangle_1\lvert\Phi^+\rangle_{23}$ w bazie Bella kubitów 1 i 2.
(b) Podaj bramkę korekty Boba dla każdego z czterech wyników.
(c) Uzasadnij, że $P=\tfrac14$ dla każdego wyniku.

**Z-19.2.** Supergęste kodowanie.
(a) Podaj stany, które otrzymuje Bob po bramkach $I,X,Z,ZX$ Alicji.
(b) Ile bitów klasycznych odczytuje Bob i z ilu kubitów?
(c) Porównaj bilans zasobów z teleportacją.

**Z-19.3.** Shor dla $N=15$, $a=11$.
(a) Wyznacz rząd $r$ liczby $11$ mod $15$.
(b) Wyznacz dzielniki $15$ z $\gcd(11^{r/2}-1,15)$.
(c) Co dzieje się dla $a=14$ i dlaczego trzeba powtórzyć?

**Z-19.4.** Grover dla $N=16$.
(a) Policz $\theta$, $k_{\rm opt}$ i $P_{\rm sukces}(k_{\rm opt})$.
(b) Policz $P$ dla $k=4$ i porównaj z (a).
(c) Wyjaśnij, dlaczego nadmiar iteracji „psuje” wynik.

**Z-19.5.** Granica Holevo.
(a) Policz $\chi$ dla $\{\tfrac12,\lvert0\rangle;\tfrac12,\lvert+\rangle\}$.
(b) Porównaj z $\log_2 2=1$ bita.
(c) Zinterpretuj wynik: ile informacji niosą dwa nieortogonalne „pół-bity”?

**Z-19.6. [★]** Solovay–Kitaev.
(a) Oszacuj T-count dla $\varepsilon=10^{-4}$ i $\varepsilon=10^{-8}$ ze wzoru $\approx3\log_2(1/\varepsilon)$.
(b) Dlaczego koszt rośnie logarytmicznie, a nie liniowo?
(c) Jaką rolę odgrywają magic states w obwodach fault-tolerant?

**Z-19.7. [★]** Złożoność.
(a) Wypisz relacje między P, BPP, BQP, PSPACE.
(b) Czy faktoryzacja jest problemem NP-zupełnym? Uzasadnij.
(c) Co to jest QMA i dlaczego problem lokalnego Hamiltona jest QMA-zupełny?

**Z-19.8.** Estymacja fazy.
(a) Jaką dokładność $\varphi$ daje $t=8$ kubitów?
(b) Dla $U$ z $\varphi=\tfrac14$ podaj najbardziej prawdopodobny wynik pomiaru.
(c) Wyjaśnij rolę estymacji fazy w algorytmie Shora.

## 7. Wskazówki do zadań

- **Z-19.1.** (a) podstaw $\lvert00\rangle,\lvert11\rangle$ przez $\lvert\Phi^\pm\rangle$; (b) dopasuj Pauliego; (c) amplitudy mają moduł $\tfrac12$.
- **Z-19.2.** (a) użyj tabeli 3.2; (b) 2 bity z 1 kubita; (c) e-bit + kubit vs e-bit + 2 bity.
- **Z-19.3.** (a) licz $11^k\bmod15$; (b) $\gcd(a^{r/2}-1,15)$; (c) sprawdź $\gcd$ dla $a=14$.
- **Z-19.4.** (a) $\theta=\arcsin(1/4)$; (b) $P=\sin^2(9\theta)$; (c) każda iteracja to obrót o $2\theta$.
- **Z-19.5.** (a) zdiagonalizuj $\rho_{\rm avg}$; (b) $\chi\le\log_2d$; (c) nieortogonalność ogranicza odczyt.
- **Z-19.6.** (a) wstaw $\varepsilon$; (b) błąd maleje geometrycznie z długością; (c) dostarczają „magię” bramki $T$.
- **Z-19.7.** (a) łańcuch zawierania; (b) nie — Shor nie implikuje P=NP; (c) kwantowy certyfikat.
- **Z-19.8.** (a) $\sim2^{-t}$; (b) $m=\varphi\cdot2^t$; (c) znajdowanie rzędu przez QFT.

## 8. Co dalej

- **Mini-projekty** — [rozdział 20](20-ponad-program-mini-projekty.md): symulator, teleportacja,
  Grover, BB84, estymacja fazy, analiza danych.
- **Korekcja błędów** — [rozdział 13](13-korekcja-i-mitygacja-bledow.md): kontekst dla magic states i T-count.
- **Teoria informacji** — [rozdział 07](07-kwantowa-teoria-informacji.md): tw. Holevo od podstaw.
- Pełne rozwiązania: [zadania/rozwiazania/rozwiazania-19.md](../zadania/rozwiazania/rozwiazania-19.md).
- Praca domowa: [PD-4](../praca-domowa/praca-domowa-04.md); kod: [`teleportacja.py`](../kod/teleportacja.py), [`grover.py`](../kod/grover.py).

> **Weryfikacja numeryczna.** Policzone w NumPy: teleportacja dla $(\alpha,\beta)=(2/\sqrt5,\ i/\sqrt5)$
> daje cztery wyniki po $P=0{,}25$ i korekty $I,Z,X,ZX$; supergęste kodowanie: $I\to\lvert\Phi^+\rangle$,
> $X\to\lvert\Psi^+\rangle$, $Z\to\lvert\Phi^-\rangle$, $ZX\to\lvert\Psi^-\rangle$; Shor: $r(7)=4$,
> $\gcd(4-1,15)=3$, piki QFT $\{0,4,8,12\}$ po $0{,}25$; Grover $N=10^6$: $k_{\rm opt}=785$;
> Holevo $\chi=0{,}6009$ bita; T-count $\approx30/40/60/100$ dla $\varepsilon=10^{-3},10^{-4},10^{-6},10^{-10}$.





