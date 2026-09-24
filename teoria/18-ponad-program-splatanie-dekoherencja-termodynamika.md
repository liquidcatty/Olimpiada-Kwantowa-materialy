# 18. Splątanie, dekoherencja i termodynamika kwantowa


## 1. Zakres rozdziału

Rozdział obejmuje splątanie, dekoherencję i termodynamikę kwantową: miary splątania (entropia von
Neumanna i entropia splątania, concurrence i formuła Woottersa, negatywność, kryterium PPT, świadek
splątania, monogamia i nierówność CKW), stany GHZ i W oraz *area law*.

Druga grupa zagadnień to utrata splątania: dekoherencja przez splątanie z otoczeniem, czasy $T_1$ i
$T_2$, równania Lindblada i Blocha, przybliżenie Borna–Markowa oraz spadek $S$ w nierówności CHSH.

Trzecia grupa dotyczy kosztu termodynamicznego informacji: zasada Landauera, demon Maxwella i
zasada kasowania. Podstawą są macierze gęstości i kanały z
[rozdziału 17](17-ponad-program-macierze-gestosci-i-kanaly.md), a wyniki wracają w
[rozdziale 19](19-ponad-program-algorytmy-zaawansowane-i-granice.md) (tw. Holevo, monogamia w
QKD) i [rozdziale 13](13-korekcja-i-mitygacja-bledow.md) (kontekst kodów korekcyjnych).

## 2. Najważniejsze definicje

- **Entropia von Neumanna**: $S(\rho)=-\mathrm{Tr}\,\rho\log_2\rho=-\sum_i\lambda_i\log_2\lambda_i$ (w bitach).
- **Entropia splątania**: $E(\lvert\psi\rangle_{AB})=S(\rho_A)=S(\rho_B)$ dla stanu czystego; $0$ dla iloczynowego, $\le\log_2 d$.
- **Concurrence**: $C(\rho)=\max\big(0,\lambda_1-\lambda_2-\lambda_3-\lambda_4\big)$, gdzie $\lambda_k$ to pierwiastki z wartości własnych $\rho\tilde\rho$, a $\tilde\rho=(Y\otimes Y)\rho^\ast(Y\otimes Y)$.
- **Formuła Woottersa** (entropia formacji): $E_{\rm f}=h\!\Big(\tfrac{1+\sqrt{1-C^2}}{2}\Big)$, gdzie $h(x)=-x\log_2x-(1-x)\log_2(1-x)$; dla stanu czystego $E_{\rm f}=S(\rho_A)$.
- **Negatywność (negativity)**: $N(\rho)=\frac{\lVert\rho^{T_B}\rVert_1-1}{2}$; **log-negatywność** $E_N=\log_2\lVert\rho^{T_B}\rVert_1$.
- **Kryterium PPT** (Peresa–Horodeckich): dla 2 kubitów stan jest **separowalny** $\Leftrightarrow\rho^{T_B}\succeq0$.
- **Świadek splątania (entanglement witness)**: obserwabla $W$ z $\mathrm{Tr}(W\rho_{\rm sep})\ge0$ i $\mathrm{Tr}(W\rho_{\rm ent})<0$.
- **Monogamia splątania**: silne splątanie $A$–$B$ ogranicza splątanie $A$–$C$.
- **CKW (Coffman–Kundu–Wootters)**: $C^2_{AB}+C^2_{AC}\le C^2_{A(BC)}$.
- **Stan GHZ**: $\lvert\mathrm{GHZ}\rangle=\tfrac{1}{\sqrt2}(\lvert000\rangle+\lvert111\rangle)$; **stan W**: $\tfrac{1}{\sqrt3}(\lvert001\rangle+\lvert010\rangle+\lvert100\rangle)$.
- **Area law** splątania: w stanach podstawowych układów lokalnych $S(\rho_A)\propto$ powierzchnia granicy $A$, nie objętość.
- **Dekoherencja (decoherence)**: utrata koherencji przez splątanie z otoczeniem; nieodwracalna w praktyce.
- **$T_1$**: czas relaksacji populacji ($\lvert1\rangle\to\lvert0\rangle$); **$T_2$**: czas koherencji fazy, $T_2\le2T_1$.
- **Równanie Lindblada**: $d\rho/dt=-\tfrac i\hbar[H,\rho]+\sum_k\gamma_k\big(L_k\rho L_k^\dagger-\tfrac12\{L_k^\dagger L_k,\rho\}\big)$.
- **Równanie Blocha**: $d\vec r/dt=\vec r\times\vec\omega-\big(\tfrac{r_x}{T_2},\tfrac{r_y}{T_2},\tfrac{r_z-r_z^{\rm eq}}{T_1}\big)$.
- **Przybliżenie Borna–Markowa**: otoczenie bez pamięci (Markov), słabe sprzężenie (Born).
- **Zasada Landauera**: usunięcie 1 bitu kosztuje co najmniej $kT\ln2$.
- **Demon Maxwella**: pozorny spadek entropii przez pomiar.
- **Zasada kasowania (erasure principle)**: to **kasowanie**, nie kopiowanie, jest kosztowne termodynamicznie.
- **Entropia a kanał**: ewolucja unitarna zachowuje $S$; kanał może $S$ zwiększyć lub zmniejszyć.
- **Subaddytywność**: $S(\rho_{AB})\le S(\rho_A)+S(\rho_B)$; **Araki–Lieb**: $S(\rho_{AB})\ge\lvert S(\rho_A)-S(\rho_B)\rvert$.

## 3. Teoria krok po kroku

### 3.1 Entropia von Neumanna i entropia splątania

Entropia von Neumanna mierzy **nieokreśloność** stanu; dla stanu czystego jest zero, dla
$\tfrac I2$ równa 1 bit:

$$
S(\rho)=-\mathrm{Tr}\,\rho\log_2\rho=-\sum_i\lambda_i\log_2\lambda_i,\qquad
S(\tfrac I2)=1\ \text{bit},\quad S(\lvert0\rangle\langle0\rvert)=0 .
$$

Dla stanu czystego **dwóch** układów definiujemy **entropię splątania**

$$
E(\lvert\psi\rangle_{AB})=S(\rho_A)=S(\rho_B),
$$

równą zero dla iloczynu i maksymalną ($\log_2 d$) dla $\lvert\Phi^+\rangle$. Przykład: dla
$\lvert\psi\rangle=\cos\theta\lvert00\rangle+\sin\theta\lvert11\rangle$ wartości własne $\rho_A$ to
$\cos^2\theta,\sin^2\theta$, więc $E=h(\cos^2\theta)$ z $h(x)=-x\log_2x-(1-x)\log_2(1-x)$.

### 3.2 Concurrence i formuła Woottersa

Dla **dwóch** kubitów najlepszą „jednoznaczną” miarą jest **concurrence**

$$
C(\rho)=\max\Big(0,\ \lambda_1-\lambda_2-\lambda_3-\lambda_4\Big),\qquad
\lambda_k=\text{(malejąco)}\ \sqrt{\text{eigen}(\rho\,\tilde\rho)},\quad
\tilde\rho=(Y\otimes Y)\rho^\ast(Y\otimes Y).
$$

Dla stanu czystego $C=2\lvert\alpha\beta\rvert$ (dla $\alpha\lvert00\rangle+\beta\lvert11\rangle$).
Granice: $0\le C\le1$; $C=1$ dla stanów Bella. **Formuła Woottersa** zamienia $C$ na entropię
formacji $E_{\rm f}=h\big(\tfrac{1+\sqrt{1-C^2}}2\big)$; dla stanów czystych $E_{\rm f}=S(\rho_A)$.

### 3.3 Negatywność i kryterium PPT

**Kryterium PPT** (Peres, Horodeccy): stan 2-kubitowy jest separowalny $\Leftrightarrow$
$\rho^{T_B}\succeq0$ (transpozycja tylko po jednym podukładzie). Z tego budujemy
**negatywność** i **log-negatywność**:

$$
N(\rho)=\frac{\lVert\rho^{T_B}\rVert_1-1}{2}=\sum_{\lambda_i<0}\lvert\lambda_i\rvert,\qquad
E_N(\rho)=\log_2\lVert\rho^{T_B}\rVert_1=\log_2(1+2N).
$$

$N>0$ **dowodzi** splątania; $N=0$ (dla 2 kubitów) dowodzi separowalności. Negatywność jest tania
w rachunku, ale nie wykrywa splątania „związanego” (*bound entanglement*).

### 3.4 Świadek splątania

**Świadek (witness)** to obserwabla $W$ z $\mathrm{Tr}(W\rho_{\rm sep})\ge0$ dla wszystkich stanów
separowalnych i $\mathrm{Tr}(W\rho_{\rm ent})<0$ dla pewnego stanu splątanego. Najprostszy świadek
dla $\lvert\Phi^+\rangle$ to $W_{\Phi^+}=\tfrac I2-\lvert\Phi^+\rangle\langle\Phi^+\rvert$: na stanie
Wernera $p\lvert\Phi^+\rangle\langle\Phi^+\rvert+\tfrac{1-p}4I$ mamy

$$
\mathrm{Tr}(W\rho)=\tfrac12-\langle\Phi^+\rvert\rho\lvert\Phi^+\rangle
=\tfrac12-\Big(p+\tfrac{1-p}4\Big)=\frac{1-3p}4,
$$

więc świadek wykrywa splątanie dla $p>\tfrac13$. To wyjaśnia, dlaczego weryfikacja splątania w
laboratorium (rozdział 09) wymaga **kilku** pomiarów.

### 3.5 Monogamia splątania i CKW

Splątanie nie „rozmnaża się”: dla trzech kubitów $A,B,C$

$$
C^2_{AB}+C^2_{AC}\le C^2_{A(BC)}\qquad\text{(Coffman–Kundu–Wootters)} .
$$

Dla stanu $\lvert\mathrm{GHZ}\rangle$: $C_{A(BC)}=1$ (bo $\rho_A=\tfrac I2$), ale $C_{AB}=C_{AC}=0$ —
splątanie jest „globalne”. Dla stanu $\lvert W\rangle$: $C_{AB}^2=C_{AC}^2=\tfrac49$,
$C_{A(BC)}^2=\tfrac89$, więc $C_{AB}^2+C_{AC}^2=\tfrac89=C_{A(BC)}^2$ — monogamia **nasycona**.
Ta nierówność to podstawa bezpieczeństwa QKD (rozdział 10): Eve nie może być równie splątana z
Alicją, co Bob.

### 3.6 GHZ kontra W i „area law”

Stany trójdzielne różnią się **typem** splątania, nie tylko ilością:

| Cecha | $\lvert\mathrm{GHZ}\rangle$ | $\lvert W\rangle$ |
| --- | --- | --- |
| $\rho_A$ (ślad po dwóch) | $\tfrac I2$, $S=1$ | $\mathrm{diag}(\tfrac23;\tfrac13)$, $S=0{,}918$ |
| $\rho_{AB}$ (ślad po jednym) | $\mathrm{diag}(\tfrac12,0,0,\tfrac12)$, $S=1$ | wartości własne $\{0,0,\tfrac13,\tfrac23\}$, $S=0{,}918$ |
| concurrence $C_{AB}$ | $0$ | $\tfrac23$ |
| $C_{A(BC)}$ | $1$ | $0{,}943$ |
| po pomiarze jednego kubita | splątanie **znika** | zostaje szczątkowe splątanie |

**„Area law”** (prawo powierzchni): w stanie podstawowym układu z lokalnymi oddziaływaniami
entropia splątania podukładu rośnie jak **powierzchnia** jego granicy, a nie jak objętość.
To dlatego symulacja takich stanów metodami sieci tensorowych (MPS) jest efektywna, a stany o
„objętościowym” splątaniu (jak $\lvert W\rangle$, $\lvert\Phi^+\rangle^{\otimes n}$) są trudne.

### 3.7 Dekoherencja: depolaryzowanie i tłumienie fazy

Dwa najprostsze modele dekoherencji to kanały z rozdziału 17:

$$
\text{depolaryzujący: } \vec r\to(1-p)\vec r,\qquad
\text{tłumienie fazy: } \rho_{01}\to(1-\lambda)\rho_{01},\quad \rho_{00},\rho_{11}\ \text{bez zmian}.
$$

Tłumienie fazy nie zmienia populacji, a mimo to **niszczy splątanie** — bo splątanie „siedzi” w
koherencjach. Dla pary Bella $\lvert\Phi^+\rangle$:

$$
\rho(t)=\tfrac12\Big(\lvert00\rangle\langle00\rvert+\lvert11\rangle\langle11\rvert
+e^{-t/T_2}\big(\lvert00\rangle\langle11\rvert+\lvert11\rangle\langle00\rvert\big)\Big),\qquad
C(t)=e^{-t/T_2}.
$$

Concurrence zanika więc **wykładniczo** z czasem $T_2$ — stąd walka o długie $T_2$ w sprzęcie
(rozdział 12).

### 3.8 $T_1$, $T_2$, równanie Blocha i Lindblada

Populacje relaksują z czasem $T_1$ (emisja/absorpcja), koherencje z czasem $T_2$ (szum fazy).
W modelu qubit–otoczenie z **przybliżeniem Borna–Markowa** (słabe sprzężenie + brak pamięci
otoczenia) ewolucja $\rho$ spełnia **równanie Lindblada**

$$
\dot\rho=-\tfrac i\hbar[H,\rho]+\sum_k\gamma_k\Big(L_k\rho L_k^\dagger-\tfrac12\{L_k^\dagger L_k,\rho\}\Big),
$$

np. $L=\sigma_-$ daje $T_1$, a $L=\sigma_z$ — $T_2$. Dla jednego kubita wygodniej użyć
**równania Blocha** na wektor Blocha:

$$
\dot r_x=-\tfrac{r_x}{T_2},\qquad \dot r_y=-\tfrac{r_y}{T_2},\qquad
\dot r_z=-\tfrac{r_z-r_z^{\rm eq}}{T_1}.
$$

Z relacji $T_2\le2T_1$ wynika, że **nie da się** mieć dowolnie długiej koherencji fazy bez
równoczesnej relaksacji populacji.

### 3.9 Dekoherencja a nierówność CHSH

Pod kanałem depolaryzującym o parametrze $p$ korelacje maleją liniowo, więc

$$
S(p)=2\sqrt2\,(1-p)\ \xrightarrow{\ \le\ }\ 2\ \text{ dla }\ p\ge1-\tfrac1{\sqrt2}=0{,}2929 .
$$

Innymi słowy: **~29% depolaryzowania wystarcza, by zniszczyć naruszenie CHSH** — i to jest jedna z
najczęstszych przyczyn „niespełnionej nierówności Bella” w eksperymencie. Analogiczna analiza dla
stanu Wernera $p\lvert\Phi^+\rangle\langle\Phi^+\rvert+\tfrac{1-p}4I$ daje próg splątania $p>\tfrac13$,
a próg naruszenia CHSH $p>1/\sqrt2=0{,}7071$.

### 3.10 Termodynamika kwantowa: Landauer, demon, kasowanie

**Zasada Landauera.** Aby usunąć (skasować) jeden bit informacji, trzeba wydać ciepło co najmniej

$$
Q\ge kT\ln2 .
$$

Dla $T=300$ K: $Q_{\min}=k_BT\ln2=2{,}871\cdot10^{-21}$ J $=0{,}0179$ eV. To fundamentalne: pamięć
komputera *musi* grzać się przy zapisie zer.

**Demon Maxwella.** Demon mierzy cząsteczkę i otwiera klapkę, pozornie zmniejszając entropię gazu.
Landaure/Bennett pokazali, że zysk znika, gdy uwzględnić **kasowanie** informacji zapisanej w
pamięci demona: koszt kasowania $kT\ln2$ na bit dokładnie kompensuje uzyskaną pracę. To
**zasada kasowania (erasure principle)**: to nie pomiar, lecz kasowanie jest kosztowne.

**Splątanie jako paliwo.** Z korelacji można wyciągnąć **pracę** — np. w silniku kwantowym
kolejne bramki na splątanej parze pozwalają uzyskać pracę $W$ większą niż z dwóch niezależnych
kubitów (*work extraction from correlations*). Ilość dostępnej pracy wiąże się z entropią
$S(\rho)$ i energią swobodną $F=E-TS$; dla stanu o mniejszej entropii można wyciągnąć więcej pracy.

**Entropia pod działaniem kanału.** Ewolucja unitarna nie zmienia entropii:
$S(U\rho U^\dagger)=S(\rho)$. Kanał (np. depolaryzujący) może entropię **zwiększyć** („zapominanie”
informacji), a kanał resetujący — **zmniejszyć**. Niezmiennikami są **subaddytywność**
$S(\rho_{AB})\le S(\rho_A)+S(\rho_B)$ oraz nierówność Araki–Lieba
$\lvert S(\rho_A)-S(\rho_B)\rvert\le S(\rho_{AB})$. Entropia warunkowa
$S(B\mid A)=S(\rho_{AB})-S(\rho_A)$ jest $\ge0$ dla stanów separowalnych, a dla splątanych potrafi
być **ujemna** — i to też jest sygnaturą splątania.

## 4. Przykłady rozwiązane

### Przykład 18.1 (łatwy): concurrence i entropia splątania

**Dane.** (a) $\lvert\psi\rangle=0{,}8\lvert00\rangle+0{,}6\lvert11\rangle$;
(b) stan Wernera $\rho=p\lvert\Phi^+\rangle\langle\Phi^+\rvert+\tfrac{1-p}4I$ przy $p=0{,}8$.

**Metoda.** Dla stanu czystego $C=2\lvert\alpha\beta\rvert$ i $E=S(\rho_A)$; dla Wernera
$\rho^{T_B}$ ma widmo $\{\tfrac{1+p}4,\tfrac{1+p}4,\tfrac{1+p}4,\tfrac{1-3p}4\}$.

**Rachunek.** (a) $\rho_A=\mathrm{diag}(0{,}64;0{,}36)$, $C=2\cdot0{,}8\cdot0{,}6=0{,}96$,
$E=-0{,}64\log_20{,}64-0{,}36\log_20{,}36=0{,}9427$; z formuły Woottersa
$E_{\rm f}=h\big(\tfrac{1+\sqrt{1-0{,}96^2}}2\big)=h(0{,}64)=0{,}9427$ — zgodne.
(b) $\rho^{T_B}$: $0{,}45$ (trzykrotnie) i $-0{,}35$, więc
$N=\tfrac12(3\cdot0{,}45+0{,}35-1)=0{,}35$ i $E_N=\log_2(1{,}7)=0{,}7655$; ponadto
$\lambda_{\Phi^+}=p+\tfrac{1-p}4=0{,}85$, stąd $C=\max(0,2\cdot0{,}85-1)=0{,}7$.

**Odpowiedź:** (a) $\mathbf{C=0{,}96}$, $\mathbf{E=0{,}9427}$;
(b) $\mathbf{N=0{,}35}$, $\mathbf{E_N=0{,}7655}$, $\mathbf{C=0{,}7}$.
*Interpretacja:* stan czysty $0{,}8/0{,}6$ jest prawie maksymalnie splątany; stan Wernera przy
$p=0{,}8$ pozostaje splątany ($C>0$, $N>0$), choć jego koherencje są „rozmyte” przez domieszkę $\tfrac I4$.

### Przykład 18.2 (trudniejszy): dekoherencja i zanik splątania

**Dane.** Para Bella $\lvert\Phi^+\rangle$ w kanale tłumienia fazy z czasem $T_2=2\ \mu$s;
osobno kanał depolaryzujący o $p$ na jednym kubicie pary.

**Metoda.** $\rho(t)$ i $C(t)=e^{-t/T_2}$ z 3.7; dla CHSH $S(p)=2\sqrt2(1-p)$ z 3.9.

**Rachunek.** Dla $t=4\ \mu$s: $e^{-4/2}=e^{-2}=0{,}1353$, więc $C(t)=0{,}135$.
Momenty: $t=T_2$ daje $C=1/e=0{,}368$; $t=2T_2$ daje $C=0{,}135$. Dla CHSH:
$S(0)=2{,}828$; $S(0{,}1)=2{,}546$; $S(0{,}2)=2{,}263$; próg $S=2$ przy $p=1-\tfrac1{\sqrt2}=0{,}2929$.
Dla stanu Wernera: progi $p>\tfrac13$ (splątanie) i $p>0{,}7071$ (CHSH).

**Odpowiedź:** $\mathbf{C(4\,\mu\text{s})=0{,}135}$;
$\mathbf{S(0{,}2)=2{,}26>2}$, a $\mathbf{p_{\rm kryt}=0{,}293}$ niszczy naruszenie CHSH;
próg splątania Wernera $\mathbf{p>0{,}333}$.
*Interpretacja:* splątanie ginie wykładniczo w czasie $T_2$, a nierówność Bella przestaje być
narusza**na** wcześniej niż sam stan traci splątanie — dlatego testy Bella są tak czułe na szum.

### Przykład 18.3 (średni): Landauer i demon Maxwella

**Dane.** Kasowanie $10^{12}$ bitów w temperaturze $T=300$ K.

**Rachunek.** Na bit $Q_{\min}=k_BT\ln2=1{,}380649\cdot10^{-23}\cdot300\cdot0{,}6931=2{,}871\cdot10^{-21}$ J.
Dla $10^{12}$ bitów: $Q=2{,}871\cdot10^{-9}$ J. Demon Maxwella, który zyskałby $W$ na sortowaniu
cząsteczek, musi zapłacić **co najmniej** $kT\ln2$ za każdy skasowany bit pamięci — zysk netto
$W-Q\le0$.

**Odpowiedź:** $\mathbf{Q_{\min}=2{,}87\cdot10^{-21}}$ **J/bit** ($0{,}0179$ eV), dla $10^{12}$ bitów
$\mathbf{2{,}87\cdot10^{-9}}$ **J**; demon nie łamie drugiej zasady.
*Interpretacja:* informacja ma cenę termodynamiczną; „darmowy” pomiar demona okazuje się płatny
przy kasowaniu pamięci — to kwantowy rdzeń paradoksu.

## 5. Typowe pułapki

1. **Entropia splątania tylko dla stanów czystych.** Dla $\rho$ mieszanego $S(\rho_A)$ nie jest
   miarą splątania; tam używa się entropii formacji lub negatywności.
2. **Utożsamienie $C$ z entropią.** $C=0{,}7$ (Werner, $p=0{,}8$) daje
   $E_{\rm f}=h\big(\tfrac{1+\sqrt{1-0{,}49}}2\big)=h(0{,}8571)=0{,}5919$, a nie $0{,}7$.
3. **Sądzenie, że $N=0$ zawsze znaczy „separowalny”.** Dla 2 kubitów tak, ale dla 3+ istnieje
   splątanie związane (*bound*), którego negatywność nie wykrywa.
4. **Mylenie $T_1$ i $T_2$.** $T_1$ = populacje, $T_2$ = koherencje, zawsze $T_2\le2T_1$; podanie
   $T_2=3T_1$ jest fizycznie niemożliwe w prostym modelu Markowa.
5. **„Dekoherencja = utrata energii”.** Tłumienie fazy **nie** zmienia energii (populacji), a
   jednak niszczy splątanie.
6. **Jednostki entropii.** Wszystkie wzory w tym rozdziale są w **bitach** ($\log_2$); użycie
   $\ln$ daje naty (×1,443 różnicy).
7. **PPT dla 3+ układów.** Kryterium PPT rozstrzyga tylko 2-kubitowy przypadek; w wyższych
   wymiarach PPT nie wyklucza splątania.
8. **Mylenie $C_{AB}$ z $C_{A(BC)}$.** Pierwsze to splątanie pary, drugie — całego podziału
   $A$|$BC$; w CKW potrzebne jest to drugie.
9. **Odwrócenie bilansu termodynamicznego.** Kasowanie **nie jest** darmowe; demon Maxwella płaci
   $kT\ln2$ za bit, a nie za pomiar.
10. **Zapominanie o pomiarze.** Pomiar jednego kubita $\lvert\mathrm{GHZ}\rangle$ niszczy splątanie
    całkowicie; nie ma „odzyskiwania” bez klasycznej komunikacji.

## 6. Zadania (Z-18)

**Z-18.1.** Entropia von Neumanna.
(a) Policz $S$ dla $\lvert+\rangle$ i dla $\lvert0\rangle$.
(b) Policz $S(\tfrac I2)$.
(c) Policz $S$ dla $\rho=\mathrm{diag}(0{,}75;0{,}25)$; porównaj z (b).

**Z-18.2.** Concurrence.
(a) Dla $\lvert\psi\rangle=0{,}8\lvert00\rangle+0{,}6\lvert11\rangle$ podaj $C$ i $E_{\rm f}$.
(b) Podaj $C$ dla każdego z czterech stanów Bella.
(c) Podaj $C$ dla stanu iloczynego $\lvert+\rangle\otimes\lvert0\rangle$.

**Z-18.3.** Stan Wernera przy $p=0{,}6$.
(a) Wyznacz widmo $\rho^{T_B}$.
(b) Policz negatywność $N$ i log-negatywność $E_N$.
(c) Policz concurrence i rozstrzygnij, czy stan jest splątany.

**Z-18.4.** Entropia splątania.
Dany $\lvert\psi\rangle=\cos\theta\lvert00\rangle+\sin\theta\lvert11\rangle$ z $\theta=\pi/8$.
(a) Podaj $\rho_A$ i $S(\rho_A)$.
(b) Czy splątanie jest maksymalne?
(c) Podaj $C$ i sprawdź zgodność $E_{\rm f}=S(\rho_A)$.

**Z-18.5.** Dekoherencja pary Bella.
Para $\lvert\Phi^+\rangle$ w kanale tłumienia fazy z $T_2$.
(a) Podaj $C(t)$.
(b) Policz $C$ przy $t=1{,}5\,T_2$.
(c) Po jakim czasie $t/T_2$ spada poniżej $C=0{,}1$?

**Z-18.6. [★]** CHSH pod szumem.
(a) Podaj $S(p)$ dla kanału depolaryzującego o parametrze $p$.
(b) Wyznacz próg $p$, przy którym $S=2$.
(c) Porównaj z progiem splątania stanu Wernera ($p>\tfrac13$).

**Z-18.7. [★]** Monogamia.
(a) Zapisz nierówność CKW.
(b) Policz $\tau_{AB}=C_{AB}^2$, $\tau_{AC}$ i $\tau_{A(BC)}$ dla $\lvert W\rangle$.
(c) Czy CKW jest nasycona? Co to mówi o rozkładzie splątania?

**Z-18.8.** Landauer.
(a) Policz $Q_{\min}=kT\ln2$ w $T=300$ K i w $T=4$ K.
(b) Ile ciepła wydzieli skasowanie $10^{9}$ bitów w $300$ K?
(c) Dlaczego komputery kwantowe w kriogenice „nie łamią” drugiej zasady termodynamiki?

## 7. Wskazówki do zadań

- **Z-18.1.** (a) stan czysty $\Rightarrow0$; (b) $\tfrac I2$ ma wartości własne $\tfrac12,\tfrac12$; (c) podstaw
  dwie wartości własne do $-x\log_2x$.
- **Z-18.2.** (a) $C=2\lvert\alpha\beta\rvert$; (b) wszystkie pary Bella mają $C=1$; (c) stan iloczynowy $C=0$.
- **Z-18.3.** (a) widmo $\{$trzy×$\tfrac{1+p}4$, $\tfrac{1-3p}4\}$; (b) $N=\lvert\lambda_{\min}\rvert$,
  $E_N=\log_2(1+2N)$; (c) $C=\max(0,2\lambda_{\Phi^+}-1)$ z $\lambda_{\Phi^+}=p+\tfrac{1-p}4$.
- **Z-18.4.** (a) $\rho_A=\mathrm{diag}(\cos^2\theta;\sin^2\theta)$; (b) max $\Leftrightarrow\theta=\pi/4$;
  (c) $C=2\lvert\cos\theta\sin\theta\rvert=\sin2\theta$ i $E_{\rm f}=h(\cos^2\theta)$.
- **Z-18.5.** (a) $C(t)=e^{-t/T_2}$; (b) podstaw $t/T_2=1{,}5$; (c) rozwiąż $e^{-x}=0{,}1$.
- **Z-18.6.** (a) $S(p)=2\sqrt2(1-p)$; (b) $S=2\Rightarrow p=1-\tfrac1{\sqrt2}$; (c) próg CHSH jest
  **wyższy** niż próg splątania.
- **Z-18.7.** (b) $\tau_{AB}=\tfrac49$, $\tau_{A(BC)}=\tfrac89$; (c) porównaj sumę z prawą stroną.
- **Z-18.8.** (a) $kT\ln2$ dla dwu temperatur; (b) pomnóż przez $10^9$; (c) wskaż na koszt kasowania
  i chłodzenia.

## 8. Co dalej

- **Algorytmy zaawansowane i granice** — [rozdział 19](19-ponad-program-algorytmy-zaawansowane-i-granice.md):
  tw. Holevo ($\chi\le S$), monogamia w QKD, QFT.
- **Mini-projekty** — [rozdział 20](20-ponad-program-mini-projekty.md): symulacja $T_2$, estymacja fazy.
- **Korekcja błędów** — [rozdział 13](13-korekcja-i-mitygacja-bledow.md): jak walczyć z dekoherencją.
- Pełne rozwiązania: [zadania/rozwiazania/rozwiazania-18.md](../zadania/rozwiazania/rozwiazania-18.md).
- Praca domowa: [PD-4](../praca-domowa/praca-domowa-04.md).
- Bibliografia: [Horodeccy, PPT](../docs/bibliografia.md); [Brunner i in., Bell nonlocality](../docs/bibliografia.md).
- Kod: [`kod/chsh.py`](../kod/chsh.py) (CHSH), [`kod/bb84.py`](../kod/bb84.py) (QBER i szum), [`kod/teleportacja.py`](../kod/teleportacja.py) (splątanie).





