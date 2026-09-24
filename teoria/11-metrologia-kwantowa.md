# 11. Metrologia kwantowa


## 1. Zakres rozdziału

Rozdział obejmuje metrologię kwantową: estymację nieznanego parametru (fazy, częstości, pola
magnetycznego, odstępu czasu) przy użyciu $N$ cząstek, informację Fishera klasyczną (CFI)
i kwantową (QFI) oraz nierówność Craméra–Rao. Podaje granicę śrutową $\Delta\varphi=1/\sqrt N$
i granicę Heisenberga $\Delta\varphi=1/N$, opisuje stany N00N i GHZ, interferometr Macha–Zehndera,
ściśnięcie (squeezing), dekoherencję i strategie adaptacyjne, a także zastosowania: zegary atomowe
i magnometry kwantowe.

Materiał dotyczy zadań Z-11 (rozkład $p(\pm\mid\varphi)$, informacja Fishera, porównanie SNL i HL,
$F_Q$ dla N00N i GHZ, drabinka adaptacyjna, zegar optyczny) i łączy statystykę i estymację
(rozdział 03), pomiar rzutowy (rozdział 06), splątanie (rozdział 09) oraz dekoherencję
(rozdział 18).

## 2. Najważniejsze definicje

- **Parametr $\varphi$**: nieznana wielkość (u nas faza), $\varphi\in\mathbb{R}$.
- **Estymator $\hat\varphi$**: funkcja wyników pomiaru. **Obciążenie** $b=\mathbb{E}\hat\varphi-\varphi$; niepewność $\Delta\varphi=\sqrt{\mathrm{Var}(\hat\varphi)}$ przy małym obciążeniu.
- **Informacja Fishera (klasyczna, CFI)**: $F(\varphi)=\sum_k\frac{(\partial_\varphi p(k\mid\varphi))^2}{p(k\mid\varphi)}$.
- **Nierówność Craméra–Rao (CR)**: $\mathrm{Var}(\hat\varphi)\ge\frac{1}{\nu F(\varphi)}+b^2$, $\nu$ = liczba niezależnych powtórzeń; asymptotycznie nasyca ją estymator największej wiarygodności.
- **Zasób $N$**: liczba cząstek w **jednym** pomiarze; budżet całkowity to zwykle $\nu N$.
- **Granica śrutowa (shot-noise limit, SNL)**: $\Delta\varphi=1/\sqrt N$ — osiągalna światłem spójnym, czyli środkami klasycznymi.
- **Granica Heisenberga (HL)**: $\Delta\varphi=1/N$ — wymaga stanów splątanych lub ściśniętych.
- **Kwantowa informacja Fishera (QFI)**: $F_Q=\max_{\text{pomiar}}F$ — informacja o $\varphi$ zawarta w stanie, niezależna od wyboru pomiaru.
- **Stan GHZ**: $\lvert\mathrm{GHZ}\rangle=\frac{1}{\sqrt2}(\lvert0\ldots0\rangle+\lvert1\ldots1\rangle)$ (rozdział 09).
- **Stan N00N**: $\lvert\mathrm{N00N}\rangle=\frac{1}{\sqrt2}(\lvert N,0\rangle+\lvert0,N\rangle)$ — wszystkie $N$ fotonów „w lewej” **lub** „w prawej” odnodze.
- **Interferometr Macha–Zehndera (MZI)**: dwie odnogi, dzielnik wiązki (BS) z każdej strony, faza $\varphi$ w jednej odnodze.
- **Ściśnięcie (squeezing)**: wariancja jednej kwadratury pola mniejsza niż w próżni; parametr $r$ (wariancja $e^{-2r}$, amplituda $e^{-r}$), w dB: $10\log_{10}(e^{2r})$.
- **Widzialność (visibility)** $V$: kontrast prążków interferencyjnych; dekoherencja mnoży sygnał przez $V<1$.
- **Strategia adaptacyjna**: kolejne pomiary planowane na podstawie wcześniejszych wyników.

## 3. Teoria krok po kroku

### 3.1 Model estymacji parametru

Eksperyment ma trzy etapy: przygotowanie stanu sondy, oddziaływanie, które „zapisuje”
$\varphi$ w stanie, oraz pomiar i estymacja. Dane to $\nu$ niezależnych wyników
$k_1,\dots,k_\nu$ o rozkładzie $p(k\mid\varphi)$. Przykład kanoniczny: foton w superpozycji
$\lvert\psi(\varphi)\rangle=\frac{1}{\sqrt2}(\lvert0\rangle+e^{i\varphi}\lvert1\rangle)$ i pomiar w bazie
$X=\{\lvert+\rangle,\lvert-\rangle\}$; z reguły Borna

$$
p(+\mid\varphi)=\lvert\langle+\vert\psi(\varphi)\rangle\rvert^2=\frac{1+\cos\varphi}{2}=\cos^2\frac{\varphi}{2},
\qquad p(-\mid\varphi)=\sin^2\frac{\varphi}{2}. \qquad (11.1)
$$

Zapis $\cos^2(\varphi/2)$ (a nie $\cos^2\varphi$) to ta sama konwencja $\theta/2$, co
w bramkach $R_X,R_Y,R_Z$ — patrz [konwencje](../docs/03-konwencje-i-notacja.md).

### 3.2 Informacja Fishera i nierówność Craméra–Rao

**Skąd się bierze CFI.** Różniczkujemy tożsamość $\sum_k p(k\mid\varphi)=1$ i stosujemy
nierówność Cauchy'ego–Schwarza (rozdział 03):

$$
\mathrm{Var}(\hat\varphi)\ \ge\ \frac{1}{\nu F(\varphi)},\qquad
F(\varphi)=\sum_k\frac{\bigl(\partial_\varphi p(k\mid\varphi)\bigr)^2}{p(k\mid\varphi)}. \qquad (11.2)
$$

$F$ to informacja o $\varphi$ z jednego pomiaru, a $\nu F$ rośnie liniowo z liczbą powtórzeń.

**Rachunek dla (11.1).** $\partial_\varphi p_\pm=\mp\frac12\sin\varphi$, więc
$F=\frac{\sin^2\varphi}{4}\bigl(\frac{1}{\cos^2\frac\varphi2}+\frac{1}{\sin^2\frac\varphi2}\bigr) =\frac{\sin^2\varphi}{4}\cdot\frac{4}{\sin^2\varphi}=1$, bo $\cos^2\frac\varphi2\sin^2\frac\varphi2=\frac14\sin^2\varphi$.
Zatem dla jednego fotonu **$F=1$ dla każdego $\varphi$** i $\Delta\varphi\ge1/\sqrt\nu$.

### 3.3 Interferometr Macha–Zehndera

Dla jednego fotonu stan po pierwszym BS to $\frac{1}{\sqrt2}(\lvert\text{góra}\rangle+\lvert\text{dół}\rangle)$,
a prawdopodobieństwa detekcji są jak (11.1). Cały układ realizuje

$$
U=U_{\rm BS}\,\mathrm{diag}(1,e^{i\varphi})\,U_{\rm BS},\qquad
U_{\rm BS}=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}=H,
$$

czyli „$H$–faza–$H$”: **interferometr to dosłownie Hadamard, faza, Hadamard** (por. zadanie P3).
Dla wielu fotonów piszemy $\lvert n_a,n_b\rangle$ i używamy generatora

$$
H_{\rm gen}=\tfrac12(n_a-n_b),\qquad \lvert\psi(\varphi)\rangle=e^{-i\varphi H_{\rm gen}}\lvert\psi_0\rangle . \qquad (11.3)
$$

To definicja modelu: $\varphi$ jest fazą względną nagromadzoną między odnogami.

### 3.4 Granica śrutowa (shot noise)

$N$ niezależnych fotonów w tym samym stanie: liczba zliczeń jest zmienną dwumianową, więc
$\mathrm{Var}(k)=Np(1-p)$ (rozdział 03). Największa czułość jest w punkcie pracy
$\varphi=\pi/2$ ($p=\frac12$), gdzie informacja Fishera dodaje się liniowo:

$$
F_N=N F_1=N,\qquad \boxed{\Delta\varphi=\frac{1}{\sqrt N}}\quad\text{(SNL)}. \qquad (11.4)
$$

„Śrut” to ziarnistość światła: każdy foton jest niezależnym losowaniem.

| $N$ | $\Delta\varphi_{\rm SNL}=1/\sqrt N$ | $\Delta\varphi_{\rm HL}=1/N$ | zysk $\sqrt N$ |
| --- | --- | --- | --- |
| $10^2$ | $10^{-1}$ | $10^{-2}$ | $10$ |
| $10^4$ | $10^{-2}$ | $10^{-4}$ | $100$ |
| $10^6$ | $10^{-3}$ | $10^{-6}$ | $1000$ |
| $10^8$ | $10^{-4}$ | $10^{-8}$ | $10^4$ |

### 3.5 Kwantowa informacja Fishera i granica Heisenberga

Dla stanu **czystego** ewoluującego unitarnie $e^{-i\varphi H}$:

$$
F_Q=4\,\mathrm{Var}(H)=4\bigl(\langle H^2\rangle-\langle H\rangle^2\bigr). \qquad (11.5)
$$

Intuicja: parametr „obraca wskazówkę” o kąt proporcjonalny do $H$, więc im większa
nieoznaczoność $H$, tym szybciej rozkład wyników zmienia się z $\varphi$.

**Granica dla $N$ fotonów.** Niech $\langle n_a+n_b\rangle=N$ będzie ustalone; wtedy
$H_{\rm gen}=n_a-N/2$, czyli $\mathrm{Var}(H_{\rm gen})=\mathrm{Var}(n_a)$. Zmienna $n_a$
przyjmuje wartości tylko w $[0,N]$, a wariancja zmiennej ograniczonej do przedziału długości
$N$ nie przekracza $(N/2)^2$. Stąd

$$
\boxed{F_Q\le N^2,\qquad \Delta\varphi\ge\frac{1}{N}}\quad\text{(HL)}. \qquad (11.6)
$$

QFI rośnie **kwadratowo** z liczbą cząstek — dlatego splątanie daje zysk $\sqrt N$, a nie
stały czynnik.

argument przez zasadę nieoznaczoności: $\Delta\varphi\,\Delta n\ge\frac12$
i $\Delta n\le N$ dają $\Delta\varphi\gtrsim1/(2N)$. Jest prostszy, ale słabszy od (11.6):
nie mówi, jakim pomiarem granicę osiągnąć.

### 3.6 Stany N00N i GHZ jako zasoby

**Stan N00N.** $\lvert\mathrm{N00N}\rangle=\frac{1}{\sqrt2}(\lvert N,0\rangle+\lvert0,N\rangle)$:
$\langle n_a\rangle=\frac N2$, $\langle n_a^2\rangle=\frac{N^2}{2}$, więc
$\mathrm{Var}(n_a)=\frac{N^2}{2}-\frac{N^2}{4}=\frac{N^2}{4}$ i $F_Q=4\cdot\frac{N^2}{4}=N^2$.
Granica (11.6) jest **nasycona**.

**Stan GHZ.** Generator $H=\frac12\sum_{i=1}^N\sigma_z^{(i)}$ (fazę zbiera każdy kubit, np.
w zegarze atomowym). Dla obu składników superpozycji $H=\pm N/2$, więc
$\langle H^2\rangle=\frac{N^2}{4}$ i $F_Q=N^2$ — identycznie jak dla N00N. Dla porównania
stan iloczynowy $\lvert+\rangle^{\otimes N}$: $\mathrm{Var}(H)=\frac N4$, czyli $F_Q=N$ (SNL).

| Stan $N$-cząstkowy | $F_Q$ | $\Delta\varphi$ (1 pomiar) |
| --- | --- | --- |
| iloczynowy (światło spójne) | $N$ | $1/\sqrt N$ |
| N00N, GHZ | $N^2$ | $1/N$ |

**Jak je wytworzyć.** GHZ: $H$ na pierwszym kubicie i kaskada CNOT (rozdziały 06, 09) —
rutynowo dla $N$ rzędu kilkunastu–kilkudziesięciu. N00N: konwersja parametryczna (*SPDC*)
z **postselekcją** (czekamy na przypadek po jednym fotonie w każdej odnodze), co dla
dużych $N$ drastycznie zmniejsza wydajność.

**Ograniczenie praktyczne.** Stan N00N ma **fazę okresową**:
$\lvert\psi(\varphi+2\pi/N)\rangle=\pm\lvert\psi(\varphi)\rangle$ — pomiar daje $\varphi$ tylko
modulo $2\pi/N$, więc potrzebne jest zgrubne oszacowanie (sekcja 3.8). Dodatkowo utrata
choćby jednego fotonu niszczy superpozycję, dlatego w optyce używa się raczej światła ściśniętego.

### 3.7 Jaki pomiar osiąga granicę?

$F_Q$ to maksimum po **wszystkich** pomiarach — wybór pomiaru można więc „zepsuć”.

- **Dobry pomiar (N00N):** liczenie fotonów w jednej odnodze albo **parzystość**
  $\Pi=(-1)^{n_a}$ dają ten sam rozkład
  $p_\pm=\frac{1\pm\cos N\varphi}{2}=\cos^2\!\bigl(\frac{N\varphi}{2}\bigr)$ i $F=N^2$
  (rachunek jak w 3.2 z $\varphi\to N\varphi$): faza „nakręca się” $N$ razy szybciej.
- **Zły pomiar:** rozróżnianie $\lvert N,0\rangle$ i $\lvert0,N\rangle$ w bazie liczby
  fotonów (tj. $\sigma_z$ osobno na każdym fotonie) w ogóle nie zależy od $\varphi$, więc $F=0$.
- **Pomiar homodynowy** (mieszanie z lokalnym oscylatorem) to standard w detektorach fal
  grawitacyjnych: dla $N$ fotonów daje $1/\sqrt N$, dla światła ściśniętego — patrz 3.9.

### 3.8 Strategie adaptacyjne

Nieoznaczoność $\varphi$ modulo $2\pi/N$ rozwiązuje się **drabinką** pomiarów. Niech $k$-ty
etap używa $N_k$ cząstek i daje $1/N_k$. Kolejny etap wymaga, by jego okres był dłuższy niż
niepewność poprzedniego:

$$
\frac{1}{N_k}<\frac{\pi}{N_{k+1}}\qquad\Longleftrightarrow\qquad N_{k+1}<\pi N_k . \qquad (11.8)
$$

Wystarczy mnożyć $N$ przez $c<3{,}14$ (np. przez $3$); suma ciągu geometrycznego o ilorazie
$1/3$ to tylko $1{,}5$ ostatniego wyrazu, więc **budżet całkowity jest $\sim2\times$ większy
od budżetu ostatniego etapu** i skalowanie $1/N$ zostaje zachowane.

Przykład: drabinka $300,900,2700,8100$ daje sumę $12\,000$ cząstek i końcową niepewność
$1/8100=1{,}23\cdot10^{-4}$, gdy przy tym samym budżecie granica śrutowa to
$1/\sqrt{12\,000}=9{,}13\cdot10^{-3}$ — **zysk $73{,}9$**. Warunek (11.8) jest spełniony:
$1/300=3{,}33\cdot10^{-3}<\pi/900=3{,}49\cdot10^{-3}$.

### 3.9 Ściśnięcie (squeezing)

Światło spójne ma fluktuacje obu kwadratur na poziomie próżni. **Ściśnięcie** zmniejsza
fluktuacje jednej kwadratury kosztem drugiej (zasada nieoznaczoności pozostaje spełniona).
Parametr $r$: wariancja maleje o $e^{-2r}$, amplituda (czyli niepewność fazy) o $e^{-r}$:

$$
\Delta\varphi_{\rm squ}=\frac{e^{-r}}{\sqrt{\bar n}},\qquad \text{ściśnięcie [dB]}=10\log_{10}(e^{2r}). \qquad (11.9)
$$

| ściśnięcie | $e^{2r}$ (wariancja) | $e^{r}$ (poprawa amplitudy) |
| --- | --- | --- |
| $3$ dB | $2{,}00$ | $1{,}41$ |
| $6$ dB | $3{,}98$ | $2{,}00$ |
| $10$ dB | $10{,}0$ | $3{,}16$ |
| $15$ dB | $31{,}6$ | $5{,}62$ |

To **nie** jest skalowanie Heisenberga: przy ustalonym $\bar n$ zysk jest stałym czynnikiem.
W praktyce bywa bezcenny — LIGO/Virgo wprowadzają $\approx6$ dB ściśniętego światła
(zależnego od częstotliwości, przez „wnękę filtrującą”), co daje $\approx2\times$ lepszą
czułość amplitudową, czyli szybsze wykrywanie zlewających się czarnych dziur.

**ściśnięcie spinowe**: $\xi^2=\dfrac{N(\Delta J_z)^2}{\lvert\langle J_x\rangle\rvert^2}<1$
oznacza stan metrologicznie użyteczny. Ściśnięcie spinowe *implikuje* splątanie
(kryterium Winelanda) — to „splątanie widoczne w jednej liczbie”.

### 3.10 Dekoherencja i utrata przewagi

Jeśli koherencja stanu N00N/GHZ przetrwa z prawdopodobieństwem $p$, a z $1-p$ układ traci
informację fazową (wraca do SNL), to

$$
F_Q(p)=pN^2+(1-p)N . \qquad (11.10)
$$

Dla $N=100$ (idealnie $\Delta\varphi=0{,}01$):

| $p$ | $F_Q$ | $\Delta\varphi$ | zysk nad SNL |
| --- | --- | --- | --- |
| $1$ | $10\,000$ | $0{,}0100$ | $10$ |
| $0{,}9$ | $9010$ | $0{,}0105$ | $9{,}5$ |
| $0{,}5$ | $5050$ | $0{,}0141$ | $7{,}1$ |
| $0{,}1$ | $1090$ | $0{,}0303$ | $3{,}3$ |
| $0{,}01$ | $199$ | $0{,}0709$ | $1{,}4$ |

Przewaga kwantowa nie jest więc „darmowa”: utrzymuje się, dopóki $p\gg1/N$ (wtedy $pN^2\gg N$).
Zysk równy dokładnie $2$ występuje dla $F_Q=2N$, czyli $p=\frac{1}{N-1}$ — dla $N=10^4$
to $p\approx10^{-4}$: **koherencja musi przetrwać niemal idealnie**. Ponieważ dla stanu GHZ
dekoherencja każdej cząstki działa $N$ razy silniej (widzialność $\sim e^{-N\Gamma t}$),
powyżej pewnego $N$ zwiększanie zasobu przestaje pomagać.

**twierdzenie „no-go”.** Dla nieskorelowanej dekoherencji markowowskiej
skalowanie $1/N$ **załamuje się** i asymptotycznie wraca $1/\sqrt N$; splątanie daje wtedy
co najwyżej stały czynnik poprawy. Dowód używa QFI dla stanów mieszanych (operator SLD)
i zapisu szumu jako kanału kwantowego: Demkowicz-Dobrzański, Kołodyński, Guţă,
*Nat. Commun.* **3**, 1063 (2012); przegląd: arXiv:1506.02362. Skalowanie Heisenberga
jest **kruche**: istnieje dla szumu skorelowanego (kolektywnego), nie dla lokalnego.

### 3.11 Zegary atomowe i magnometry

**Zegar atomowy.** Schemat Ramseya: atomy w stanie $\lvert+\rangle$ (lub GHZ), czas swobodnej
ewolucji $T$, pomiar. Szum projekcyjny ogranicza częstość:

$$
\Delta\nu=\frac{1}{2\pi T\sqrt N}\ (\text{SNL}),\qquad \Delta\nu=\frac{1}{2\pi T N}\ (\text{HL}).
$$

Dla optycznego zegara strontowego ($\nu=429\,228\,004\,229\,873$ Hz, przejście $^1S_0\to{}^3P_0$):

| $N$ atomów | $T$ | $\Delta\nu_{\rm SNL}$ | $\Delta\nu/\nu$ |
| --- | --- | --- | --- |
| $10^4$ | $1$ s | $1{,}59$ mHz | $3{,}7\cdot10^{-18}$ |
| $10^5$ | $1$ s | $0{,}503$ mHz | $1{,}2\cdot10^{-18}$ |
| $10^4$ | $10$ s | $0{,}159$ mHz | $3{,}7\cdot10^{-19}$ |

Rząd $10^{-18}$ zgadza się z najlepszymi zegarami optycznymi i pokazuje, że do dalszej
poprawy trzeba **więcej atomów** lub **dłuższego $T$** — dopóki szum projekcyjny dominuje
nad szumem lasera i efektami systematycznymi (Doppler, promieniowanie ciała czarnego,
przesunięcie grawitacyjne).

**Magnometry.** Ten sam aparat, z $\omega=\gamma B$. Rzędy wielkości czułości:

| Technologia | Czułość | Uwagi |
| --- | --- | --- |
| pojedynczy centr NV w diamencie | $\approx10$ nT$/\sqrt{\rm Hz}$ | temperatura pokojowa |
| zespół centrów NV | $\approx1$ pT$/\sqrt{\rm Hz}$ | mikroskopia magnetyczna |
| magnetometr atomowy (SERF) | $\approx0{,}1$ fT$/\sqrt{\rm Hz}$ | pary atomów Rb/K |
| SQUID | $\approx1$ fT$/\sqrt{\rm Hz}$ | chłodzenie ciekłym helem |

Dla centrów NV $\mathrm{d}\nu/\mathrm{d}B\approx2{,}8$ MHz/G $=2{,}8\cdot10^{10}$ Hz/T, więc
rozdzielenie $1$ mHz odpowiada $3{,}6\cdot10^{-14}$ T $=36$ fT na pomiar; ostateczną granicę
wyznacza czas koherencji (sekcja 12.2).

## 4. Przykłady rozwiązane

### Przykład 11.1 (łatwy): jeden foton, $\varphi=\pi/3$

**Dane:** $\lvert\psi\rangle=\frac{1}{\sqrt2}(\lvert0\rangle+e^{i\varphi}\lvert1\rangle)$,
pomiar w bazie $X$, $\nu=2000$ powtórzeń. **Szukane:** $p(\pm)$, $F$, $\Delta\varphi$.
**Rachunek:** $p(+)=\cos^2\frac{\varphi}{2}=\cos^2\frac{\pi}{6}=\frac34$, $p(-)=\frac14$;
$\partial_\varphi p_\pm=\mp\frac12\sin\varphi$, więc
$F=\frac{(3/16)}{3/4}+\frac{(3/16)}{1/4}=\frac14+\frac34=1$ (ten sam wynik daje (11.2) dla
każdego $\varphi$). Zatem $\Delta\varphi\ge1/\sqrt{\nu}=\frac{1}{\sqrt{2000}}=0{,}0224$ rad,
a dla $\Delta\varphi=10^{-4}$ potrzeba $\nu=1/(10^{-4})^2=10^8$ fotonów.
**Odpowiedź:** $p(+)=\frac34$, $p(-)=\frac14$, $F=\mathbf{1}$,
$\Delta\varphi\ge\mathbf{0{,}0224}$ **rad**, na $10^{-4}$ rad trzeba $\mathbf{10^8}$ fotonów.
*Interpretacja:* pojedynczy foton daje dokładnie $1$ bit informacji o fazie (rozkład
$\frac34/\frac14$), a dokładność poprawia się tylko jak $1/\sqrt\nu$ — to granica śrutowa.

### Przykład 11.2 (trudniejszy): N00N kontra światło klasyczne

**Dane:** budżet $N=10^6$ fotonów, cel $\Delta\varphi=10^{-6}$ rad.
**Metoda:** wzory (11.4) i (11.7). Światło klasyczne: $\Delta\varphi=1/\sqrt{10^6}=10^{-3}$ rad,
więc na $10^{-6}$ rad trzeba $N=(1/10^{-6})^2=10^{12}$ fotonów. Stan N00N o $N=10^6$:
$F=N^2=10^{12}$, czyli $\Delta\varphi=10^{-6}$ rad **w jednym pomiarze**. Dekoherencja z $p=0{,}9$:
$F=0{,}9\cdot10^{12}+0{,}1\cdot10^{6}=9{,}0001\cdot10^{11}$, więc
$\Delta\varphi=1{,}054\cdot10^{-6}$ rad; zysk nad światłem klasycznym o tym samym $N$ wynosi
$10^{-3}/1{,}054\cdot10^{-6}=949$ (czyli $94{,}9\%$ zysku idealnego $1000=\sqrt N$).
**Odpowiedź:** klasycznie $\mathbf{10^{12}}$, ze stanem N00N $\mathbf{10^6}$ fotonów;
przy $p=0{,}9$ błąd to $\mathbf{1{,}05\cdot10^{-6}}$ **rad**.
*Interpretacja:* splątanie zamienia $N\to N^2$ w informacji Fishera — to zmiana *skalowania*,
nie stałego czynnika, i dlatego jest warta zachodu.

### Przykład 11.3 (skrót): zegar atomowy

$N=10^5$, $T=1$ s, $\nu_{\rm Sr}=4{,}292\cdot10^{14}$ Hz:
$\Delta\nu=\frac{1}{2\pi\cdot1\cdot\sqrt{10^5}}=\frac{1}{2\pi\cdot316{,}2}=0{,}503$ mHz,
czyli $\Delta\nu/\nu=1{,}2\cdot10^{-18}$. Ściśnięcie 10 dB ($e^{r}=3{,}16$) daje $0{,}159$ mHz
i $3{,}7\cdot10^{-19}$. Na $10^{-19}$ bez ściśnięcia trzeba
$N=(\frac{1}{2\pi\Delta\nu})^2=(3708)^2=\mathbf{1{,}4\cdot10^7}$ atomów albo $T=11{,}7$ s
przy $N=10^5$. Ściśnięcie daje stały czynnik $3{,}2$, a liczba atomów wchodzi
jak $\sqrt N$ — dlatego walka o $10^{-19}$ to walka o $\sqrt N$ i dłuższy czas integracji.

## 5. Typowe pułapki

1. **Mylenie $1/\sqrt N$ z $1/N$.** Dla $N=10^6$ to czynnik $1000$. Ustal, czy zadanie
   dotyczy światła klasycznego (SNL) czy stanu splątanego (HL).
2. **Zapominanie o powtórzeniach.** Niepewność to $1/\sqrt{\nu F}$, nie $1/\sqrt F$; ustal,
   czy budżet to $N$ cząstek w jednym pomiarze, czy $\nu N$ cząstek w $\nu$ pomiarach.
3. **Traktowanie $F_Q$ jako automatycznie osiągalnej.** To maksimum po pomiarach; „zły”
   pomiar (np. $\sigma_z$ zamiast parzystości dla N00N) daje $F=0$.
4. **Ignorowanie okresowości $2\pi/N$.** Bez zgrubnego oszacowania fazy wynik N00N jest
   obciążony (aliasing), a nie „dokładny”.
5. **Przekonanie, że splątanie zawsze daje zysk.** Przy dekoherencji zysk maleje do $\sqrt2$
   dla $p=1/(N-1)$.
6. **Mylenie decybeli.** 6 dB to $4\times$ mniejsza wariancja, ale tylko $2\times$ lepsza
   amplituda: $10\log_{10}(e^{2r})$ dB.
7. **$F_Q=4\mathrm{Var}(H)$ przy stanie mieszanym.** Wzór obowiązuje dla stanu **czystego**;
   dla mieszanego trzeba QFI z operatora SLD (lub ostrożnego oszacowania).
8. **Brak jednostek i konwencji kąta.** $\Delta\varphi$ w radianach; piszemy
   $\cos^2(\varphi/2)$, nie $\cos^2\varphi$.
## 6. Zadania (Z-11)

**Z-11.1.** Foton w interferometrze, $\varphi=\pi/2$, pomiar w bazie $X$. (a) Podaj $p(\pm\mid\varphi)$ i sprawdź, że suma $=1$. (b) Policz $F$ z definicji (11.2) i podaj $\Delta\varphi$ dla $\nu=100$. (c) Ile pomiarów daje $\Delta\varphi=10^{-3}$ rad? Co się dzieje, gdy $\varphi\to0$?

**Z-11.2.** Granica śrutowa kontra Heisenberg, $N=10^6$ fotonów. (a) Policz $\Delta\varphi_{\rm SNL}$ i $\Delta\varphi_{\rm HL}$. (b) Ile fotonów trzeba na $\Delta\varphi=10^{-8}$ rad w obu reżimach? (c) Wyraź stosunek tych liczb jako funkcję wymaganej dokładności $\varepsilon$ i sprawdź dla $\varepsilon=10^{-8}$.

**Z-11.3.** Stan N00N o $N=4$ i $N=8$. (a) Policz $\mathrm{Var}(n_a)$ i $F_Q$ z (11.7). (b) Podaj $\Delta\varphi$ dla jednego pomiaru i dla $\nu=100$ pomiarów. (c) Jaki warunek musi spełniać zgrubne oszacowanie fazy, by pomiar był jednoznaczny? Czy dla $N=4$ wystarczy dokładność zgrubna $0{,}5$ rad?

**Z-11.4.** GHZ w zegarze atomowym: $N=200$, koherencja z $p=0{,}95$. (a) Policz $F_Q$ i $\Delta\varphi$ dla $p=1$ oraz dla stanu iloczynowego. (b) Policz $F_Q(p)$ i $\Delta\varphi$ dla $p=0{,}95$; podaj zysk nad SNL. (c) Wyznacz $p$, przy którym zysk spada do $\sqrt2$.

**Z-11.5.** Światło ściśnięte 6 dB i 10 dB, $\bar n=10^6$. (a) Zamień dB na $e^{2r}$ i $e^{r}$. (b) Podaj $\Delta\varphi$ dla światła spójnego i obu poziomów ściśnięcia. (c) Dlaczego ściśnięcie *nie* daje skalowania $1/\bar n$ i jaki stan trzeba dołożyć, żeby je uzyskać?

**Z-11.6. [★]** Drabinka adaptacyjna. (a) Wyprowadź warunek (11.8) i uzasadnij, że $c=3$ jest bezpieczne. (b) Zaprojektuj drabinkę $N_k=250\cdot3^k$, $k=0,\dots,3$: podaj wyrazy, sumę i końcową niepewność. (c) Porównaj z granicą śrutową przy tym samym całkowitym budżecie fotonów; podaj zysk i wyjaśnij, ile kosztuje „niezdecydowanie” fazy.

**Z-11.7.** Zegar optyczny: $N=10^4$, $T=1$ s, $\nu=4{,}292\cdot10^{14}$ Hz. (a) Policz $\Delta\nu$ i $\Delta\nu/\nu$. (b) To samo dla $T=10$ s. (c) Ile atomów trzeba na $\Delta\nu/\nu=10^{-19}$ przy $T=1$ s? Czy przy $N=10^5$ wystarczy wydłużyć $T$ (ile)?

## 7. Wskazówki do zadań

- **Z-11.1, Z-11.2.** (11.1) dla tego modelu $F=1$; stosunek zasobów SNL/HL to $1/\varepsilon$; przy $\varphi\to0$ pochodna $\partial_\varphi p\to0$ — brak punktu pracy = brak informacji.
- **Z-11.3, Z-11.5.** $\mathrm{Var}(n_a)=N^2/4$; warunek jednoznaczności: niepewność zgrubna $<\pi/N$ (dla $N=4$: $0{,}785$); dB: $e^{2r}=10^{\text{dB}/10}$, niepewność z (11.9).
- **Z-11.4, Z-11.7.** (b) podstaw do (11.10); (c) rozwiąż $pN^2+(1-p)N=2N$; w Z-11.7 wszystko z $\Delta\nu=\frac{1}{2\pi T\sqrt N}$.
- **Z-11.6.** (a) użyj połowy okresu $\pi/N_{k+1}$; (b) wypisz i zsumuj wyrazy; (c) porównaj z $1/\sqrt{\sum_kN_k}$.

## 8. Co dalej

- **Realizacje komputerów kwantowych** — [rozdział 12](12-realizacje-komputerow-kwantowych.md): skąd bierze się szum psujący przewagę metrologiczną.
- **Korekcja i mitygacja błędów** — [rozdział 13](13-korekcja-i-mitygacja-bledow.md): jak walczy się z utratą koherencji.
- **Splątanie i dekoherencja** — [rozdział 18](18-ponad-program-splatanie-dekoherencja-termodynamika.md); **analiza danych** — [rozdział 16](16-analiza-danych-i-obliczenia-naukowe.md).
- Pełne rozwiązania: [zadania/rozwiazania/rozwiazania-11.md](../zadania/rozwiazania/rozwiazania-11.md); praca domowa: [PD-3](../praca-domowa/praca-domowa-03.md).
- Skrypt: `python kod/metrologia_faza.py` (Monte Carlo: $1/\sqrt N$ vs $1/N$, dekoherencja).
- Bibliografia: Giovannetti–Lloyd–Maccone, *Advances in quantum metrology* (2011); Demkowicz-Dobrzański–Jarzyna–Kołodyński, arXiv:1506.02362.






