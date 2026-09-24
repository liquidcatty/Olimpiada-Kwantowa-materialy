# Rozwiązania do rozdziału 11

## Z-11.1

(a) Dla $\varphi=\pi/2$ mamy $\varphi/2=\pi/4$, więc z (11.1):

$$
p(+)=\cos^2\frac{\pi}{4}=\left(\frac{\sqrt2}{2}\right)^2=\frac12,\qquad p(-)=\sin^2\frac{\pi}{4}=\frac12 .
$$

Suma $=\frac12+\frac12=1$ ✓ (rozkład jednostajny — maksymalna informacja o fazie).

(b) $\partial_\varphi p_\pm=\mp\frac12\sin\varphi=\mp\frac12$ dla $\varphi=\pi/2$, więc

$$
F=\frac{(1/2)^2}{1/2}+\frac{(1/2)^2}{1/2}=\frac12+\frac12=1 .
$$

Nierówność Craméra–Rao: $\Delta\varphi\ge\frac{1}{\sqrt{\nu F}}=\frac{1}{\sqrt{100}}=\mathbf{0{,}1}$ **rad**.

(c) $\Delta\varphi=\frac{1}{\sqrt\nu}=10^{-3}\Rightarrow\nu=10^6$ pomiarów (fotonów).
Dla $\varphi\to0$ rozkład staje się zdeterminowany ($p(+)\to1$, $p(-)\to0$): w granicy
$\varphi=0$ mamy $\partial_\varphi p\to0$ i informacja o fazie znika; dla małych $\varphi$
pochodna rośnie liniowo, ale liczba „sygnałowych” zliczeń to $\nu\sin^2(\varphi/2)\approx\nu\varphi^2/4$,
więc przy skończonym $\nu$ estymator jest obciążony, a nierówność CR nieopisująca rzeczywistości.
**Trzeba pracować w punkcie pracy $\varphi\approx\pi/2$.**

**Odpowiedź:** (a) $\frac12,\frac12$; (b) $F=1$, $\Delta\varphi\ge\mathbf{0{,}1}$ rad;
(c) $\mathbf{10^6}$ pomiarów; przy $\varphi\to0$ sygnał jest zdeterminowany i pomiar traci czułość.

*Fizycznie:* informacja Fishera jest geometryczna — zerowa tylko wtedy, gdy rozkład nie zmienia
się z parametrem; o fazie najłatwiej wnioskować przy maksymalnym kontraście ($p=1/2$).

## Z-11.2

(a) $\Delta\varphi_{\rm SNL}=1/\sqrt N=1/\sqrt{10^6}=\mathbf{10^{-3}}$ **rad**;
$\Delta\varphi_{\rm HL}=1/N=\mathbf{10^{-6}}$ **rad** — czynnik $1000=\sqrt N$.

(b) Warunek: $\varepsilon=10^{-8}$ rad.
- SNL: $1/\sqrt N=10^{-8}\Rightarrow N=10^{16}$ fotonów.
- HL: $1/N=10^{-8}\Rightarrow N=10^{8}$ fotonów.

(c) Stosunek zasobów: $10^{16}/10^{8}=10^{8}$. Ogólnie
$\dfrac{N_{\rm SNL}}{N_{\rm HL}}=\dfrac{\varepsilon^{-2}}{\varepsilon^{-1}}=\dfrac{1}{\varepsilon}$,
co dla $\varepsilon=10^{-8}$ daje dokładnie $10^8$; dla $\varepsilon=10^{-3}$ byłoby to już
tylko $10^3$ — **im wyższa wymagana precyzja, tym większa nagroda za kwantowość**.

**Odpowiedź:** (a) $10^{-3}$ i $10^{-6}$ rad; (b) $10^{16}$ i $10^{8}$ fotonów;
(c) $1/\varepsilon=\mathbf{10^8}$ razy mniej fotonów dla strategii heisenbergowskiej.

*Fizycznie:* przewaga splątania jest *skalowańcza*, więc rośnie nieograniczenie wraz z wymaganą
dokładnością (zakładając brak dekoherencji — por. sekcja 3.10).

## Z-11.3

(a) Dla stanu N00N $\langle n_a\rangle=N/2$, $\langle n_a^2\rangle=N^2/2$, dlatego
$\mathrm{Var}(n_a)=N^2/2-N^2/4=N^2/4$ i $F_Q=4\cdot N^2/4=N^2$.
$N=4$: $\mathrm{Var}(n_a)=4$, $F_Q=16$; $N=8$: $\mathrm{Var}(n_a)=16$, $F_Q=64$.

(b) Jeden pomiar: $\Delta\varphi=1/\sqrt{F_Q}$; $N=4$: $1/4=\mathbf{0{,}25}$ rad;
$N=8$: $1/8=\mathbf{0{,}125}$ rad. Dla $\nu=100$: $1/\sqrt{100\cdot16}=0{,}025$ rad
i $1/\sqrt{100\cdot64}=0{,}0125$ rad.

(c) Okres stanu N00N to $2\pi/N$, więc zgrubne oszacowanie musi mieścić się w połowie okresu:
$\delta\varphi<\pi/N$. Dla $N=4$: $\pi/4\approx0{,}785$ rad, więc dokładność $0{,}5$ rad
**wystarcza** („mieści się” w oknie $0{,}785$ rad).

**Odpowiedź:** (a) $\mathrm{Var}=4$ i $16$, $F_Q=\mathbf{16}$ i $\mathbf{64}$;
(b) $0{,}25$ i $0{,}125$ rad (po $100$ pomiarach: $0{,}025$ i $0{,}0125$ rad);
(c) warunek $\delta\varphi<\pi/N$; dla $N=4$, $0{,}5<\pi/4$ — OK.

*Fizycznie:* przy tym samym budżecie $4$ fotonów światło klasyczne daje $1/\sqrt4=0{,}5$ rad,
czyli **dwukrotnie** gorszy wynik niż N00N — to zysk $\sqrt{N}$ w najprostszym przypadku.

## Z-11.4

(a) $p=1$: $F_Q=N^2=200^2=40\,000$, $\Delta\varphi=1/\sqrt{F_Q}=1/200=\mathbf{0{,}005}$ rad.
Stan iloczynowy: $F_Q=N=200$, $\Delta\varphi=1/\sqrt{200}=\mathbf{0{,}0707}$ rad.
Zysk: $0{,}0707/0{,}005=14{,}14=\sqrt{200}$ ✓.

(b) $F_Q(p)=pN^2+(1-p)N=0{,}95\cdot40\,000+0{,}05\cdot200=38\,000+10=38\,010$, więc
$\Delta\varphi=1/\sqrt{38\,010}=\mathbf{5{,}13\cdot10^{-3}}$ rad. Zysk nad SNL:
$0{,}0707/0{,}00513=13{,}8$ (zamiast $14{,}1$).

(c) Zysk $\sqrt2$ oznacza $F_Q=2N$:

$$
pN^2+(1-p)N=2N\ \Rightarrow\ pN^2-pN=N\ \Rightarrow\ p=\frac{1}{N-1}=\frac{1}{199}=\mathbf{5{,}03\cdot10^{-3}}.
$$

**Odpowiedź:** (a) $40\,000$ i $200$; (b) $F_Q=38\,010$, $\Delta\varphi=\mathbf{5{,}13\cdot10^{-3}}$ rad,
zysk $13{,}8$; (c) $p=\mathbf{1/199\approx0{,}5\%}$.

*Fizycznie:* wystarczy $5\%$ utraty koherencji, by stracić $2{,}5\%$ zysku, ale $99{,}5\%$ utraty,
by zredukować go do $\sqrt2$ — próg jest nieproporcjonalnie ostry, bo $F_Q$ jest kwadratowa w $N$.

## Z-11.5

(a) Z definicji dB: $10\log_{10}(e^{2r})=\text{dB}$, więc $e^{2r}=10^{\text{dB}/10}$.
- $6$ dB: $e^{2r}=10^{0{,}6}=3{,}98$, $e^{r}=\sqrt{3{,}98}=1{,}995$.
- $10$ dB: $e^{2r}=10^{1}=10{,}0$, $e^{r}=\sqrt{10}=3{,}162$.

(b) Światło spójne: $\Delta\varphi=1/\sqrt{\bar n}=1/\sqrt{10^6}=10^{-3}$ rad.
Ściśnięte: $\Delta\varphi=e^{-r}/\sqrt{\bar n}$:
- $6$ dB: $10^{-3}/1{,}995=5{,}01\cdot10^{-4}$ rad,
- $10$ dB: $10^{-3}/3{,}162=3{,}16\cdot10^{-4}$ rad.

(c) We wzorze (11.9) ściśnięcie wchodzi wyłącznie przez czynnik $e^{-r}$, a liczba fotonów
nadal przez $1/\sqrt{\bar n}$: **skalowanie pozostaje śrutowe**, bo stan ściśnięty jest
gaussowski i nie wnosi korelacji „wszystkie fotony razem”. Aby uzyskać $\Delta\varphi\propto 1/\bar n$,
trzeba stanu o $F_Q\propto\bar n^2$ — czyli makroskopowej superpozycji typu N00N
($\lvert N,0\rangle+\lvert0,N\rangle$) lub GHZ (sekcja 3.6).

**Odpowiedź:** (a) $3{,}98$/$1{,}995$ i $10{,}0$/$3{,}162$; (b) spójne $10^{-3}$ rad,
ściśnięte $\mathbf{5{,}01\cdot10^{-4}}$ i $\mathbf{3{,}16\cdot10^{-4}}$ rad;
(c) brak — potrzebny stan N00N/GHZ.

*Fizycznie:* ściśnięcie to „przestawienie” nieoznaczoności między kwadraturami: daje stały
czynnik (np. $2\times$ przy $6$ dB), a stany N00N dają zmianę wykładnika skalowania.

## Z-11.6

(a) Po etapie $k$ znamy $\varphi$ z niepewnością $\delta_k=1/N_k$. Etap $k+1$ mierzy
$\cos(N_{k+1}\varphi)$ o okresie $\dfrac{2\pi}{N_{k+1}}$, więc jednoznaczny odczyt wymaga, by
$\delta_k$ było mniejsze od połowy okresu:

$$
\frac{1}{N_k}<\frac{\pi}{N_{k+1}}\quad\Longleftrightarrow\quad N_{k+1}<\pi N_k .
$$

Iloraz $c=3$ jest bezpieczny, bo $3<\pi=3{,}1416$ (margines $4{,}7\%$). Dla $c\ge\pi$ kolejny
etap „przeskoczyłby” o pełny okres i wynik byłby niejednoznaczny.

(b) $N_k=250\cdot3^{k}$: $250,\ 750,\ 2250,\ 6750$. Suma:
$250(1+3+9+27)=250\cdot40=10\,000$ fotonów. Końcowa niepewność
$\delta=1/6750=\mathbf{1{,}48\cdot10^{-4}}$ rad. Sprawdzenie warunku na każdym kroku:
$1/250=4{,}00\cdot10^{-3}<\pi/750=4{,}19\cdot10^{-3}$ ✓;
$1/750=1{,}33\cdot10^{-3}<\pi/2250=1{,}40\cdot10^{-3}$ ✓;
$1/2250=4{,}44\cdot10^{-4}<\pi/6750=4{,}65\cdot10^{-4}$ ✓.

(c) Granica śrutowa przy tym samym budżecie $10\,000$ fotonów: $1/\sqrt{10\,000}=10^{-2}$ rad.
Zysk: $10^{-2}/1{,}48\cdot10^{-4}=67{,}5$. Cena „niezdecydowania” o fazie: drabinka zużywa
$10\,000/6750=1{,}48$ razy więcej fotonów niż idealny pojedynczy pomiar z $N=10^4$
(który dałby $1/10^4=10^{-4}$ rad) — tracimy więc czynnik $\approx1{,}5$, zachowując
skalowanie $1/N$.

**Odpowiedź:** (a) warunek $N_{k+1}<\pi N_k$; (b) $250,750,2250,6750$, suma $\mathbf{10\,000}$,
$\delta=\mathbf{1{,}48\cdot10^{-4}}$ rad; (c) zysk $\mathbf{67{,}5}$, koszt czynnika $1{,}5$.

*Fizycznie:* drabinka adaptacyjna to sposób „opanowania” okresowości stanów splątanych —
bez niej nagroda za $1/N$ byłaby nieosiągalna, bo nie wiedzielibyśmy, któremu okresowi
przypisać wynik.

## Z-11.7

(a) $\Delta\nu=\dfrac{1}{2\pi T\sqrt N}=\dfrac{1}{2\pi\cdot1\cdot\sqrt{10^4}}=\dfrac{1}{2\pi\cdot100}=\dfrac{1}{628{,}32}=1{,}5915\cdot10^{-3}$ Hz $=\mathbf{1{,}59}$ **mHz**.
Względnie: $\dfrac{\Delta\nu}{\nu}=\dfrac{1{,}5915\cdot10^{-3}}{4{,}292\cdot10^{14}}=3{,}71\cdot10^{-18}$.

(b) Dla $T=10$ s: $\Delta\nu$ maleje dziesięciokrotnie, $\Delta\nu=1{,}59\cdot10^{-4}$ Hz,
czyli $\Delta\nu/\nu=\mathbf{3{,}71\cdot10^{-19}}$.

(c) Cel $\Delta\nu/\nu=10^{-19}$ daje $\Delta\nu=4{,}292\cdot10^{14}\cdot10^{-19}=4{,}292\cdot10^{-5}$ Hz.
Z $\Delta\nu=\frac{1}{2\pi T\sqrt N}$ przy $T=1$ s:

$$
\sqrt N=\frac{1}{2\pi\cdot4{,}292\cdot10^{-5}}=3708\ \Rightarrow\ N=1{,}38\cdot10^7\ \text{atomów}.
$$

Przy $N=10^5$ ($\sqrt N=316{,}23$) potrzeba
$T=\dfrac{1}{2\pi\cdot316{,}23\cdot4{,}292\cdot10^{-5}}=\mathbf{11{,}7}$ **s** — czyli samo
wydłużenie czasu integracji wystarcza, ale wymaga dwunastokrotnego zwiększenia $T$.

**Odpowiedź:** (a) $\Delta\nu=\mathbf{1{,}59}$ mHz, $\Delta\nu/\nu=\mathbf{3{,}7\cdot10^{-18}}$;
(b) $\mathbf{3{,}7\cdot10^{-19}}$; (c) $N=\mathbf{1{,}4\cdot10^7}$ atomów albo $T=\mathbf{11{,}7}$ s przy $N=10^5$.

*Fizycznie:* szum projekcyjny (kwantowy) to „koszt” odczytu stanu atomów; jego redukcja
odbywa się przez $\sqrt N$ i dłuższy czas Ramseya, natomiast ściśnięcie spinowe dałoby
jedynie stały czynnik — dlatego najlepsze zegary optyczne walczą o jak najwięcej atomów
i jak najdłuższy czas koherencji, a nie o „coraz większe splątanie”.


