# 13. Korekcja i mitygacja błędów


## 1. Zakres rozdziału

Rozdział obejmuje korekcję i mitygację błędów: modele błędów (bit-flip, phase-flip, $Y$,
depolaryzacja, tłumienie amplitudowe, dekoherencja), redundancję, kod
$\lbrack\!\lbrack n,k,d\rbrack\!\rbrack$, dystans, syndrom, stabilizatory i pomiar pośredni —
pomiar syndromu wskazuje, *który* błąd zaszedł, nie ujawniając stanu logicznego. Opisuje kod
3-kubitowy, kod phase-flip, kod Shora i kod Steane'a, kody stabilizatorowe oraz kod powierzchniowy
wraz z twierdzeniem o progu i kosztem zasobów.

Druga część rozdziału dotyczy mitygacji dla ery NISQ (skalowanie szumu, macierz kalibracji odczytu,
postselekcja, randomized compiling, twirling, PEC, dynamical decoupling), która poprawia wyniki bez
budowania kubitów logicznych. Materiał dotyczy zadań Z-13 i łączy się z realizacjami sprzętu
(rozdział 12) oraz macierzami gęstości i kanałami kwantowymi (rozdział 17).

## 2. Najważniejsze definicje

- **Błąd bit-flip ($X$)**: zamiana $\lvert0\rangle\leftrightarrow\lvert1\rangle$ z prawdopodobieństwem $p$.
- **Błąd fazowy (phase-flip, $Z$)**: zmiana znaku amplitudy $\lvert1\rangle$; nie zmienia populacji, psuje superpozycję.
- **Błąd $Y$**: jednocześnie bit-flip i phase-flip; $Y=iXZ$ (z dokładnością do fazy).
- **Kanał depolaryzujący**: $(1-p)\rho+\frac p3(X\rho X+Y\rho Y+Z\rho Z)=(1-\frac{4p}{3})\rho+\frac{4p}{3}\frac{I}{2}$.
- **Amplitudowe tłumienie**: $E_0=\mathrm{diag}(1,\sqrt{1-\gamma})$, $E_1=\sqrt\gamma\lvert0\rangle\langle1\rvert$ (relaksacja $T_1$).
- **Dekoherencja fazowa**: zanik wyrazów pozadiagonalnych $\rho$; $1/T_2=\frac{1}{2T_1}+\frac{1}{T_\varphi}$.
- **Redundancja**: zakodowanie $1$ kubita logicznego w $n$ fizycznych; **kod $\lbrack\!\lbrack n,k,d\rbrack\!\rbrack$**: $k$ logicznych w $n$ fizycznych, dystans $d$.
- **Dystans $d$**: waga najmniejszego operatora nietrywialnego logicznie; kod naprawia błędy do wagi $t=\lfloor(d-1)/2\rfloor$.
- **Syndrom**: wynik pomiaru generatorów stabilizatora (np. $(0,1)$); mówi, gdzie zaszedł błąd, nie zdradzając stanu logicznego.
- **Kubit pomocniczy (ancilla)**: dodatkowy kubit $\lvert0\rangle$, przez który mierzymy syndrom.
- **Stabilizator**: operator $\hat S$ (iloczyn macierzy Pauliego) z $\hat S\lvert\psi_L\rangle=+\lvert\psi_L\rangle$; **kod stabilizatorowy** ma $n-k$ generatorów.
- **Kod powierzchniowy**: kod stabilizatorowy na kracie 2D, stabilizatory o wadze 4, tylko bramki najbliższego sąsiada.
- **Twierdzenie o progu**: dla błędu fizycznego $p<p_{\rm thr}$ zwiększanie $d$ daje dowolnie mały błąd logiczny.
- **Mitygacja**: ZNE, macierz kalibracji, postselekcja, randomized compiling, twirling, PEC (bez tworzenia kubitów logicznych).

## 3. Teoria krok po kroku

### 3.1 Modele błędów

Każdy błąd opisujemy operatorem (kanałem), który działa na macierz gęstości (rozdziały 07 i 17).

| Model | Działanie | Uwagi fizyczne |
| --- | --- | --- |
| bit-flip $X$ | $\rho\to X\rho X$ z prawd. $p$ | przeskok relaksacyjny, szum sterowania |
| phase-flip $Z$ | $\rho\to Z\rho Z$ z prawd. $p$ | szum fazowy, fluktuacje pola |
| $Y$ | $\rho\to Y\rho Y$ z prawd. $p$ | równoważnie $X$ i $Z$ naraz |
| depolaryzacja | $(1-p)\rho+\frac p3(X\rho X+Y\rho Y+Z\rho Z)$ | „zapomnienie” stanu; $(1-\frac{4p}{3})\rho+\frac{4p}{3}\frac{I}{2}$ |
| amplitudowe tłumienie | $E_0=\mathrm{diag}(1,\sqrt{1-\gamma})$, $E_1=\sqrt\gamma\lvert0\rangle\langle1\rvert$ | relaksacja $T_1$: $\rho_{11}\to(1-\gamma)\rho_{11}$, $\rho_{01}\to\sqrt{1-\gamma}\,\rho_{01}$ |
| dekoherencja fazowa | $\rho_{01}\to e^{-t/T_\varphi}\rho_{01}$ | $1/T_2=\frac{1}{2T_1}+\frac{1}{T_\varphi}$ |

Dla $p=0{,}05$ depolaryzacja daje wierność $F=1-\frac{2p}{3}=0{,}967$ dla dowolnego stanu
czystego (bo $\langle X\rangle^2+\langle Y\rangle^2+\langle Z\rangle^2=1$).

**Dyskretyzacja błędu.** Każdy operator na jednym kubicie rozkłada się w bazie
$\{I,X,Y,Z\}$: $E=\sum_{i}c_i\sigma_i$. Jeśli kod naprawia $X$ *i* $Z$, to naprawia też $Y$
(bo po poprawce zostaje faza globalna) oraz dowolne ich kombinacje — dlatego mówiąc „błąd”
mamy na myśli jedną z trzech macierzy Pauliego. To „twierdzenie o dyskretyzacji” jest
fundamentem całej korekcji.

### 3.2 Redundancja, syndrom i pomiar pośredni

Kodowanie: $1$ kubit logiczny $\to$ $n$ fizycznych, przy czym stan **nie jest kopiowany**
(zakaz klonowania!), tylko **splątany** w podprzestrzeń zwaną **podprzestrzenią kodu**.

**Jak zmierzyć syndrom, nie psując stanu?** Bierzemy kubit pomocniczy (ancillę) w stanie
$\lvert0\rangle$, wykonujemy CNOT-y z kubitów danych na ancillę i mierzymy ancillę. Dla
stabilizatora $Z_1Z_2$: CNOT z $q_1$ na ancillę, CNOT z $q_2$ na ancillę, pomiar ancilli
w bazie $Z$. Jeśli stan jest w podprzestrzeni kodu ($Z_1Z_2\lvert\psi_L\rangle=+\lvert\psi_L\rangle$),
ancilla wraca do $\lvert0\rangle$ — **pomiar nie zaburza stanu danych**. Jeśli zaszedł błąd,
ancilla obraca się do $\lvert1\rangle$ i dowiadujemy się o błędzie, ale nie o amplitudach
$\alpha,\beta$ stanu logicznego.

Formalnie: mierzymy obserwablę $\hat S$, która **komutuje** ze stanem kodu i z błędami,
a nie mierzymy pojedynczych $\sigma_z$. Pomiar $n-k$ niezależnych generatorów daje
syndrom — wektor $n-k$ bitów.

### 3.3 Kod 3-kubitowy bit-flip (pełny rachunek)

**Kodowanie.** $\lbrack\!\lbrack3,1,3\rbrack\!\rbrack$: $\lvert0\rangle_L=\lvert000\rangle$,
$\lvert1\rangle_L=\lvert111\rangle$, czyli $\alpha\lvert0\rangle+\beta\lvert1\rangle\to\alpha\lvert000\rangle+\beta\lvert111\rangle$.
Realizacja obwodowa: CNOT z $q_0$ na $q_1$ i CNOT z $q_0$ na $q_2$.

**Stabilizatory:** $S_1=Z_1Z_2$, $S_2=Z_2Z_3$ (kolejność kubitów małoendianowa: stan
$\lvert q_2q_1q_0\rangle$). Syndrom zapisujemy jako parę $(\langle Z_1Z_2\rangle,\langle Z_2Z_3\rangle)$
zamienioną na bity: $+1\to0$, $-1\to1$.

| Błąd | $\langle Z_1Z_2\rangle$ | $\langle Z_2Z_3\rangle$ | syndrom | poprawka |
| --- | --- | --- | --- | --- |
| brak | $+1$ | $+1$ | $(0,0)$ | — |
| $X$ na $q_2$ | $-1$ | $+1$ | $(1,0)$ | $X$ na $q_2$ |
| $X$ na $q_1$ | $-1$ | $-1$ | $(1,1)$ | $X$ na $q_1$ |
| $X$ na $q_0$ | $+1$ | $-1$ | $(0,1)$ | $X$ na $q_0$ |

Cztery możliwe syndromy odpowiadają czterem sytuacjom (brak błędu + trzy pozycje) — to
warunek jednoznacznej korekcji: dla kodu naprawiającego błędy do wagi $t$ każdy błąd
o wadze $\le t$ musi mieć **inny** syndrom.

**Czego kod nie naprawia.** Dwa błędy: $X$ na $q_0$ i $q_1$ dają syndrom $(1,0)$ — taki sam
jak pojedynczy $X$ na $q_2$ — więc „poprawka” $X$ na $q_2$ zamienia stan
$\alpha\lvert011\rangle+\beta\lvert100\rangle$ na $\alpha\lvert111\rangle+\beta\lvert000\rangle$,
czyli na $\alpha\lvert1\rangle_L+\beta\lvert0\rangle_L$: amplitudy się zamieniają, a kod
wprowadza **błąd logiczny** $X_L$ zamiast go naprawić. To konsekwencja dystansu $d=3$ —
kod naprawia $t=\lfloor(d-1)/2\rfloor=1$ błąd (patrz 3.6). Kod nie widzi też
**błędów fazowych**: $Z$ na jednym kubicie nie zmienia wartości $Z_1Z_2$ i psuje
$\lvert+\rangle_L$, przechodząc niezauważenie.

**Zysk.** Jeśli każdy z $3$ kubitów ma niezależnie błąd $X$ z prawdopodobieństwem $p$,
korekcja zawodzi przy $\ge2$ błędach:

$$
P_{\rm fail}=3p^2(1-p)+p^3=3p^2-2p^3 .
$$

Dla $p=0{,}01$: $P_{\rm fail}=2{,}98\cdot10^{-4}$ — **$34\times$ lepiej** niż $p$. Dla
$p=0{,}05$: $7{,}25\cdot10^{-3}$ ($6{,}9\times$ lepiej). Kod przestaje pomagać, gdy
$3p^2-2p^3=p$, czyli dla $p=\frac12$: **poniżej $50\%$ błędu kod zawsze coś poprawia**.

### 3.4 Kod phase-flip i kod Shora

**Kod phase-flip** powstaje przez zamianę baz: $\lvert0\rangle_L=\lvert+++\rangle$,
$\lvert1\rangle_L=\lvert---\rangle$, stabilizatory $X_1X_2$, $X_2X_3$. Nie trzeba nowej teorii:
bramka Hadamarda zamienia $Z\leftrightarrow X$ ($HZH=X$), więc kod bit-flip **w bazie $X$**
staje się kodem phase-flip. Syndromy są identyczne (z $X$-ów zamiast $Z$-ów), a poprawka to
$Z$ na wskazanym kubicie.

**Kod Shora** $\lbrack\!\lbrack9,1,3\rbrack\!\rbrack$ to **konkatenacja**: kod phase-flip na
3 „blokach” po 3 kubity, gdzie każde $\lvert0\rangle/\lvert1\rangle$ bloku samo jest kodem
bit-flip:

$$
\lvert0\rangle_L=\frac{1}{2\sqrt2}\bigl(\lvert000\rangle+\lvert111\rangle\bigr)^{ \otimes 3},
\qquad
\lvert1\rangle_L=\frac{1}{2\sqrt2}\bigl(\lvert000\rangle-\lvert111\rangle\bigr)^{ \otimes 3}.
$$

- Błąd bit-flip $X$ na jednym kubicie jest wychwytywany **wewnątrz bloku** (syndromy $Z_iZ_j$),
  a błąd fazowy $Z$ zmienia znak całego bloku ($\lvert000\rangle+\lvert111\rangle\to\lvert000\rangle-\lvert111\rangle$),
  co wychwytuje **kod zewnętrzny** (syndromy $X_iX_j$).
- Kod naprawia **każdy** pojedynczy błąd na dowolnym z $9$ kubitów, dla wszystkich trzech typów
  $X,Y,Z$ (bo $Y$ to jednocześnie flip bitu i fazy). Łącznie $1+9\cdot3=28$ klas błędów mieści
  się w $2^8=256$ syndromach ośmiu generatorów.
- Historyczna wartość: pierwszy kod pokazujący, że korekcja jest w ogóle możliwa (Shor, 1995);
  wada — $9$ kubitów fizycznych na $1$ logiczny i skomplikowana realizacja.

### 3.5 Kod Steane'a $\lbrack\!\lbrack7,1,3\rbrack\!\rbrack$

Kod Steane'a to kod **CSS** (*Calderbank–Shor–Steane*) zbudowany z klasycznego kodu Hamminga
$[7,4,3]$: bity parzystości dają stabilizatory, a komutowanie wynika z parzystej liczby
wspólnych kubitów. Sześć generatorów ($q_1$–$q_7$):

$$
g_1=X_4X_5X_6X_7,\quad g_2=X_2X_3X_6X_7,\quad g_3=X_1X_3X_5X_7,
$$

$$
g_4=Z_4Z_5Z_6Z_7,\quad g_5=Z_2Z_3Z_6Z_7,\quad g_6=Z_1Z_3Z_5Z_7 .
$$

Stan logiczny $\lvert0\rangle_L$ jest równą superpozycją ośmiu słów **o parzystej wadze**:
$\{0000000,\ 0001111,\ 0110011,\ 0111100,\ 1010101,\ 1011010,\ 1100110,\ 1101001\}$,
każde z amplitudą $1/\sqrt8$. $\lvert1\rangle_L$ to to samo dla słów nieparzystych
($\lvert1\rangle_L=X_1X_2\cdots X_7\lvert0\rangle_L$ — operacja logiczna $X_L$ jest „transwersalna”).

**Syndromy.** Dla błędu $X$ na $j$-tym kubicie (mierzymy generatory $Z$-owe) syndrom to
**zapis binarny numeru kubitu**:

| błąd $X$ na kubicie | $g_4$ | $g_5$ | $g_6$ | syndrom |
| --- | --- | --- | --- | --- |
| $q_1$ | $+1$ | $+1$ | $-1$ | $001$ |
| $q_2$ | $+1$ | $-1$ | $+1$ | $010$ |
| $q_3$ | $+1$ | $-1$ | $-1$ | $011$ |
| $q_4$ | $-1$ | $+1$ | $+1$ | $100$ |
| $q_5$ | $-1$ | $+1$ | $-1$ | $101$ |
| $q_6$ | $-1$ | $-1$ | $+1$ | $110$ |
| $q_7$ | $-1$ | $-1$ | $-1$ | $111$ |

Dla błędu $Z$ syndrom liczymy z generatorów $X$-owych i jest on **identyczny** (ta sama
tabela) — dlatego kod Steane'a naprawia każdy pojedynczy błąd. Kluczowa zaleta praktyczna:
**bramki H, S i CNOT można wykonać transwersalnie** (kubit po kubicie), bez łączenia
odległych kubitów i bez rozprzestrzeniania błędu jednego kubitu na wiele — to fundament
odporności na błędy (*fault tolerance*).

### 3.6 Kody stabilizatorowe

**Definicja.** Niech $\mathcal{P}_n$ będzie grupą macierzy Pauliego na $n$ kubitach.
Kod stabilizatorowy zadaje **przemienna podgrupa** $S\subset\mathcal{P}_n$:
podprzestrzeń kodu to wspólna przestrzeń własna $+1$ wszystkich elementów $S$:

$$
\lvert\psi_L\rangle\ \text{jest w kodzie}\iff \hat S\lvert\psi_L\rangle=+\lvert\psi_L\rangle
\ \text{ dla każdego } \hat S\in S .
$$

Dla $\lbrack\!\lbrack n,k,d\rbrack\!\rbrack$ grupa $S$ ma $n-k$ niezależnych generatorów,
więc syndrom ma $n-k$ bitów i istnieje $2^{\,n-k}$ klas błędów. **Dystans** $d$ to minimalna
waga operatora, który komutuje ze wszystkimi generatorami, ale **nie** należy do $S$ (czyli
nietrywialna operacja logiczna).

| Kod | $n$ | $k$ | $d$ | generatory | naprawia |
| --- | --- | --- | --- | --- | --- |
| 3-kubitowy | $3$ | $1$ | $3$ | $2$ | pojedynczy $X$ |
| phase-flip | $3$ | $1$ | $3$ | $2$ | pojedynczy $Z$ |
| Shor | $9$ | $1$ | $3$ | $8$ | dowolny pojedynczy błąd |
| Steane | $7$ | $1$ | $3$ | $6$ | dowolny pojedynczy błąd |
| powierzchniowy | $2d^2-1$ | $1$ | $d$ | $2d^2-2$ | do $\lfloor(d-1)/2\rfloor$ błędów |

Wzór Shannona dla kodów kwantowych mówi, że $k/n\to1$ tylko kosztem dystansu — nie da się
mieć jednocześnie dużej pojemności i dużej odporności.

**warunki Knilla–Laflamme.** Kod naprawia zbiór błędów $\{E_a\}$, gdy
$\langle\psi_i\rvert E_a^\dagger E_b\lvert\psi_j\rangle=C_{ab}\,\delta_{ij}$ dla wszystkich
stanów bazowych kodu — czyli błędy nie „przeciekają” między podprzestrzenie logiczne.
W języku stabilizatorów odpowiada to warunkowi, że syndromy różnych błędów są różne.

### 3.7 Kod powierzchniowy i twierdzenie o progu

**Kod powierzchniowy** (*surface code*) to dziś najważniejszy kod praktyczny. Konstrukcja:
- kubity **danych** leżą na krawędziach kraty $d\times d$,
- kubity **pomiarowe** leżą na ścianach (stabilizatory $Z^{\otimes4}$, tzw. plaquettes)
  i na wierzchołkach (stabilizatory $X^{\otimes4}$, tzw. stars),
- stabilizatory mają wagę $4$, więc syndrom mierzy się **wyłącznie bramkami najbliższego
  sąsiada** — idealnie dla krat 2D nadprzewodzących i tablic atomów.

**Obraz błędów.** Błąd $X$ na jednym kubicie danych „zapala” dwa sąsiednie stabilizatory
$Z$-owe; łańcuch błędów tworzy **parę defektów (anyonów)** na końcach łańcucha. Korekcja =
połączenie defektów najkrótszą drogą (algorytm dopasowania, *minimum weight perfect matching*).
Jeśli łańcuch pomyłek „zamknie pętlę” wokół całej kraty, powstaje **błąd logiczny** — dlatego
prawdopodobieństwo błędu logicznego maleje z $d$: potrzeba $\sim d/2$ błędów fizycznych
ułożonych w łańcuch, żeby oszukać dekoder.

**Twierdzenie o progu.** Dla szumu poniżej progu $p<p_{\rm thr}$ (dla kodu powierzchniowego
przy szumie obejmującym bramki i pomiary: $p_{\rm thr}\approx0{,}5$–$1\%$) błąd logiczny maleje
wykładniczo z dystansem:

$$
p_L\propto\Lambda^{-(d+1)/2},\qquad \Lambda>1 .
$$

Google (2024, kod powierzchniowy na 105 kubitach „Willow”) zaraportował $\Lambda\approx2{,}14$
i $p_L\approx0{,}14\%$ na cykl dla $d=7$ (przy $d=5$: $\approx0{,}65\%$, przy $d=3$: $\approx3\%$)
— pierwsza demonstracja **poniżej progu**, gdy większy kod naprawdę działa lepiej.

**Warunki praktyczne.** (i) Błąd nie może się rozprzestrzeniać — używa się bramek transwersalnych
i „syndromów w miejscu” (*flag qubits*); (ii) dekoder musi działać w czasie rzeczywistym, szybciej
niż cykl pomiarowy; (iii) brak transwersalnej bramki $T$ odzyskuje się przez **destylację stanów
magicznych** (15 kopii „brudnego” stanu daje 1 lepszy).

### 3.8 Koszt zasobów — kiedy korekcja się opłaca

| Dystans $d$ | kubity fizyczne ($2d^2-1$) | błąd logiczny na cykl |
| --- | --- | --- |
| $3$ | $17$ | $\approx3\%$ |
| $5$ | $49$ | $\approx0{,}65\%$ |
| $7$ | $97$ | $\approx0{,}14\%$ |
| $27$ | $1457$ | $\approx10^{-6}$ |

Do zejścia z $0{,}143\%$ do $10^{-6}$ potrzeba $\log_{2{,}14}(0{,}00143/10^{-6})=9{,}55$ kroków,
czyli $d\approx7+2\cdot9{,}55\approx27$ i $1457$ kubitów **na jeden kubit logiczny**. Sto
kubitów logicznych to ponad $145$ tysięcy kubitów fizycznych. Dla porównania: oszacowanie dla
algorytmu Shora łamiącego RSA-2048 to $\approx2\cdot10^7$ kubitów fizycznych i $\approx8$ godzin
pracy (Gidney i Ekerå, 2021).

**Kiedy korekcja NIE pomaga?** Gdy błąd fizyczny jest **powyżej progu** ($p>p_{\rm thr}$):
dokładanie kubitów i bramek tylko zwiększa liczbę błędów, dlatego najpierw poprawia się sprzęt
(rozdział 12). **Korekcja kontra mitygacja:** korekcja daje *skalowanie* (większe $d$ $\to$
mniejszy błąd), a mitygacja (3.9) tylko poprawia wynik przy ustalonym szumie — koszt PEC rośnie
wykładniczo z głębokością obwodu.

### 3.9 Mitygacja bez korekcji

- **Macierz kalibracji odczytu.** Błędy odczytu są systematyczne ($A_{ij}=P(\text{odczyt }i\mid\text{stan }j)$); odwracamy pomiar: $\vec p_{\rm popr}=A^{-1}\vec p_{\rm zmierz}$. Przykład — macierz $A$:

$$
A=\begin{pmatrix}0{,}95&0{,}10\\0{,}05&0{,}90\end{pmatrix}
$$

  $\vec p_{\rm zmierz}=(0{,}60;0{,}40)$ dają $\vec p_{\rm popr}=(0{,}588;0{,}412)$; $\mathrm{cond}(A)=1{,}19$. Przy dużym szumie poprawki wychodzą **ujemne** i trzeba je rzutować na sympleks.
- **ZNE (zero-noise extrapolation).** Ten sam obwód przy sztucznie zwiększonym szumie ($\lambda=1,2,3$ przez „składanie” bramek, *gate folding*), potem ekstrapolacja do $\lambda=0$. Dla $E(1)=0{,}80$, $E(2)=0{,}65$, $E(3)=0{,}55$ liniowe $E(\lambda)=E(0)+a\lambda$ daje $a=-0{,}15$ i $E(0)=\mathbf{1{,}00}$; model wykładniczy dałby to samo dla danych $0{,}80,0{,}64,0{,}512$.
- **Postselekcja i symetrie.** Odrzucamy *shots*, w których złamana została znana symetria obwodu (liczba cząstek, parzystość, ładunek). Odrzucenie połowy wyników zwiększa niepewność $\sqrt2$, więc metoda opłaca się tylko przy dużej statystyce.
- **Randomized compiling.** Losowe bramki Pauliego otaczające każdą bramkę dwukubitową zamieniają błędy **koherentne** (stałe przekręcenie kąta) w **stochastyczne**, łatwiejsze do usunięcia.
- **Twirling.** Uśrednianie po losowych Pauliego zamienia dowolny kanał w depolaryzujący: $\mathcal{E}(\rho)\to(1-p_d)\rho+p_d\frac{I}{2}$, co pozwala opisać szum jedną liczbą $p_d$.
- **PEC (probabilistic error cancellation).** Quasiprawdopodobieństwa (rozkład z ujemnymi wagami) „odwracają” kanał; wynik jest dokładny w wartości oczekiwanej, ale koszt rośnie wykładniczo z liczbą bramek.
- **Dynamical decoupling.** Impulsy $\pi$ w czasie bezczynności kubita uśredniają wolnozmienny szum (odpowiednik echa Hahna, rozdział 12).

## 5. Typowe pułapki

1. **Mylenie syndromu z wynikiem pomiaru stanu.** Mierzymy stabilizatory (parzystości), nie pojedyncze $\sigma_z$; inaczej zniszczylibyśmy superpozycję.
2. **Zapominanie o konwencji kubitów.** „$Z_1Z_2$” oznacza konkretne kubity w ustalonej kolejności małoendianowej; zamiana kolejności daje lustrzaną tabelę syndromów.
3. **Traktowanie kodu $d=3$ jako naprawiającego wszystko.** Naprawia **jeden** błąd; dwa błędy mogą dać poprawny syndrom i wprowadzić błąd logiczny.
4. **Zapominanie, że $Y=iXZ$.** Kod naprawiający $X$ i $Z$ naprawia też $Y$ — nie trzeba osobnej procedury.
5. **Mylenie progu kodu z progiem modelu $3p^2-2p^3$.** Ten drugi ($p=\frac12$) dotyczy tylko błędów $X$ przy idealnym pomiarze syndromu; realny próg kodu powierzchniowego to $0{,}5$–$1\%$.

## 6. Zadania (Z-13)

**Z-13.1.** Kod 3-kubitowy. (a) Podaj stabilizatory i pełną tabelę syndromów dla pojedynczych błędów $X$. (b) Dla $\lvert\psi_L\rangle=\frac{1}{\sqrt2}(\lvert000\rangle+\lvert111\rangle)$ i błędu $X$ na $q_2$ policz syndrom i wskaż poprawkę. (c) Co się dzieje przy błędach $X$ na $q_0$ i $q_1$?

**Z-13.2.** Kanał depolaryzujący z $p=0{,}05$. (a) Zapisz go jako $(1-\frac{4p}{3})\rho+\frac{4p}{3}\frac{I}{2}$. (b) Policz wierność $F=1-\frac{2p}{3}$ i sprawdź, że $F=1-p_d/2$ dla $p_d=\frac{4p}{3}$. (c) Po ilu kanałach wierność spada poniżej $0{,}9$?

**Z-13.3.** Kod 3-kubitowy jako „dźwignia”. (a) Policz $P_{\rm fail}=3p^2-2p^3$ dla $p=0{,}01$ i $p=0{,}1$. (b) Podaj współczynnik poprawy. (c) Wyznacz próg, przy którym kod przestaje pomagać.

**Z-13.4.** Kod Steane'a. (a) Podaj sześć generatorów i sprawdź, że każdy ma wagę 4. (b) Wyznacz syndrom dla $X$ na $q_5$ oraz dla $Z$ na $q_3$. (c) Ile jest klas syndromów i ile pojedynczych błędów (z typem) da się rozróżnić?

**Z-13.5.** Kod powierzchniowy. (a) Ile kubitów fizycznych mają kody $d=5$ i $d=7$? (b) Ile na $20$ kubitów logicznych o $d=7$? (c) Jaki dystans daje błąd logiczny $\approx10^{-6}$, jeśli $p_L(d{=}7)=0{,}143\%$ i $\Lambda=2{,}14$?

**Z-13.6. [★]** Mitygacja. (a) Z punktów $E(1)=0{,}90$, $E(2)=0{,}79$, $E(3)=0{,}68$ wyznacz $E(0)$ metodą ZNE (liniowo). (b) Oceń, dlaczego przy dużym szumie odczytu odwracanie macierzy $A$ staje się niestabilne. (c) Zaproponuj połączenie ZNE z postselekcją i wskaż, co ogranicza obie metody.

## 7. Wskazówki do zadań

- **Z-13.1.** Użyj tabeli z 3.3; $\sigma_z=+1$ dla $\lvert0\rangle$ i $-1$ dla $\lvert1\rangle$.
- **Z-13.2.** (c) rozwiąż $(1-\frac{2p}{3})^n<0{,}9$, czyli $0{,}9667^n<0{,}9$.
- **Z-13.3–13.5.** (13.3c) rozwiąż $3p^2-2p^3=p$; (13.4b) użyj binarnego numeru kubitu; (13.5c) liczbę kroków policz jako $\log_\Lambda(p_L/p_L^{\rm cel})$, każdy krok to $+2$ w dystansie.
- **Z-13.6.** (a) dopasuj prostą do trzech punktów i sprawdź, czy wynik leży powyżej $1$ (wtedy model jest źle dobrany); (b) patrz liczba warunkowa; (c) postselekcja odbiera statystykę, ZNE mnoży koszt pomiarów.

## 8. Co dalej

- **Narzędzia informatyczne** — [rozdział 14](14-narzedzia-informatyczne.md): jak policzyć macierz kalibracji i dopasowanie ZNE w Pythonie.
- **Oprogramowanie kwantowe** — [rozdział 15](15-oprogramowanie-kwantowe.md): mitygacja w Qiskit (ZNE, twirling).
- **Macierze gęstości i kanały kwantowe** — [rozdział 17](17-ponad-program-macierze-gestosci-i-kanaly.md): formalizm Krausa wykorzystany w 3.1.
- Pełne rozwiązania: [rozwiazania-13.md](../zadania/rozwiazania/rozwiazania-13.md); praca domowa: [PD-3](../praca-domowa/praca-domowa-03.md).
- Skrypt: `python kod/korekcja_3bit.py`; bibliografia: Terhal, *Quantum error correction for quantum memories* (2015).



## 4. Przykłady rozwiązane

### Przykład 13.1 (łatwy): syndrom kodu 3-kubitowego

**Dane:** $\lvert\psi_L\rangle=\frac{1}{\sqrt2}(\lvert000\rangle+\lvert111\rangle)$, błąd $X$ na środkowym kubicie ($q_1$).
**Rachunek:** po błędzie $\lvert\psi'\rangle=\frac{1}{\sqrt2}(\lvert010\rangle+\lvert101\rangle)$.
Dla bitu $b$ wartość $\sigma_z$ wynosi $+1$ dla $b=0$ i $-1$ dla $b=1$:
- $\lvert010\rangle$: $Z_{q_2}Z_{q_1}=(+1)(-1)=-1$, $Z_{q_1}Z_{q_0}=(-1)(+1)=-1$;
- $\lvert101\rangle$: $Z_{q_2}Z_{q_1}=(-1)(+1)=-1$, $Z_{q_1}Z_{q_0}=(+1)(-1)=-1$.

Oba składniki superpozycji dają **ten sam** syndrom $(1,1)$, więc pomiar jest nierozdzielający
i nie niszczy superpozycji. Z tabeli w 3.3 syndrom $(1,1)$ oznacza błąd na $q_1$, więc stosujemy
$X$ na $q_1$ i odtwarzamy $\lvert\psi_L\rangle$.

**Odpowiedź:** syndrom $\mathbf{(1,1)}$, poprawka $\mathbf{X}$ na $q_1$.
*Interpretacja:* syndrom niesie tylko informację o *pozycji* błędu (2 bity), a nie o stanach
$\lvert0\rangle_L,\lvert1\rangle_L$ — dlatego pomiar nie psuje informacji logicznej.

### Przykład 13.2 (trudniejszy): kalibracja odczytu i granica opłacalności korekcji

**Dane:** macierz kalibracji jednokubitowa $A$:

$$
A=\begin{pmatrix}0{,}95&0{,}10\\0{,}05&0{,}90\end{pmatrix}
$$

pomiar dwukubitowy $\vec p_{\rm zmierz}=(0{,}80;\,0{,}07;\,0{,}07;\,0{,}06)$, kod 3-kubitowy z $p=0{,}02$.

**Część 1 (mitygacja).** Przy niezależnych błędach odczytu $A_2=A\otimes A$ i
$\vec p_{\rm popr}=A_2^{-1}\vec p_{\rm zmierz}$ dostajemy
$\vec p_{\rm popr}=(0{,}8803;\,0{,}0256;\,0{,}0256;\,0{,}0685)$ (suma $1{,}0000$).
Liczba warunkowa $\mathrm{cond}(A_2)=1{,}41$; przy większym szumie poprawki wychodzą **ujemne**
(np. dla pomiaru $(0{,}97;0{,}01;0{,}01;0{,}01)$ dostajemy $1{,}085$ i $-0{,}050$) i trzeba je
rzutować na sympleks.

**Część 2 (korekcja).** $P_{\rm fail}=3p^2-2p^3=3(0{,}02)^2-2(0{,}02)^3=1{,}18\cdot10^{-3}$,
czyli poprawa wobec $p=0{,}02$ wynosi $16{,}9\times$. Kod przestaje pomagać, gdy
$3p^2-2p^3=p$, czyli $2p^2-3p+1=0$ — stąd próg $p=\frac12$ (albo $p=1$).

**Odpowiedź:** (1) $\vec p_{\rm popr}=\mathbf{(0{,}880;\,0{,}026;\,0{,}026;\,0{,}069)}$;
(2) $P_{\rm fail}=\mathbf{1{,}18\cdot10^{-3}}$, poprawa $\mathbf{16{,}9\times}$, próg $\mathbf{p=1/2}$.

*Interpretacja:* mitygacja to algebra liniowa na rozkładzie wyników (z ryzykiem ujemnych
prawdopodobieństw), a korekcja zmienia *skalowanie* — dlatego obie techniki są komplementarne.




