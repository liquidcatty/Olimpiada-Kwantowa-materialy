# Praca domowa PD-4 (rozdziały 16–20)

Praca domowa po module czwartym obejmuje rozdział [16](../teoria/16-analiza-danych-i-obliczenia-naukowe.md)
(analiza danych i obliczenia naukowe) oraz tematy rozszerzające:
[17](../teoria/17-ponad-program-macierze-gestosci-i-kanaly.md) (macierze gęstości, kanały),
[18](../teoria/18-ponad-program-splatanie-dekoherencja-termodynamika.md) (splątanie, dekoherencja,
termodynamika), [19](../teoria/19-ponad-program-algorytmy-zaawansowane-i-granice.md) (algorytmy
zaawansowane i granice) i [20](../teoria/20-ponad-program-mini-projekty.md) (mini-projekty).

**Zasady:** rozwiązania pisemne, każde z pełnym uzasadnieniem i jawnym rachunkiem. Notacja jak w
`docs/03-konwencje-i-notacja.md` (kolejność kubitów $q_1q_0$, $\theta/2$ w bramkach obrotu, entropie
w bitach). Wyniki przybliżone z 3 cyframi znaczącymi; niepewności do 2 cyfr znaczących.
**Razem 20 punktów** (10 zadań po 2 pkt). Dopuszczalne (i zalecane) sprawdzenie rachunków w NumPy.

## Zadania

**PD-4.1 (2 pkt).** Statystyka zliczeń. Plik `zliczenia.csv` zawiera 10 zliczeń fotonów:
$16, 20, 27, 24, 27, 18, 13, 22, 17, 21$.
(a) Policz średnią $\bar n$, odchylenie standardowe $s$ i niepewność średniej $u=s/\sqrt N$.
(b) Sprawdź, czy dane są zgodne z rozkładem Poissona (porównaj wariancję $s^2$ ze średnią).
(c) Podaj wynik $\bar n\pm u$ z niepewnością zaokrągloną do 2 cyfr znaczących.

**PD-4.2 (2 pkt).** Dopasowanie i $\chi^2$. Dane $x=(0,1,2,3,4)$,
$y=(1{,}0;3{,}1;5{,}0;7{,}2;8{,}9)$, wszystkie $\sigma_i=0{,}2$.
(a) Metodą najmniejszych kwadratów (macierz Vandermonde’a, wagi $1/\sigma^2$) wyznacz $a$ i $b$ modelu $y=ax+b$.
(b) Policz $\chi^2$, $\chi^2_{\rm red}$ ($\mathrm{ndof}=3$) i $R^2$.
(c) Podaj predykcję $y(5)$ wraz z niepewnością (wzór $u^2=\vec g^{\mathsf T}\mathrm{Cov}\,\vec g$).

**PD-4.3 (2 pkt).** Propagacja niepewności. Gęstość ciała: $m=50\pm1$ g, $V=20{,}0\pm0{,}5$ cm$^3$.
(a) Policz $\rho=m/V$.
(b) Policz $u_\rho$ z ogólnego wzoru na propagację (niezależne $m$ i $V$).
(c) Uzasadnij, dlaczego $(u_\rho/\rho)^2=(u_m/m)^2+(u_V/V)^2$.

**PD-4.4 (2 pkt).** Ślad częściowy i entropia splątania — **policz ręcznie**.
Dany $\lvert\psi\rangle=\tfrac12\lvert00\rangle+\tfrac{\sqrt3}2\lvert11\rangle$.
(a) Wyznacz $\rho_A=\mathrm{Tr}_B\lvert\psi\rangle\langle\psi\rvert$.
(b) Policz entropię splątania $S(\rho_A)$ (bitach), bez kalkulatora symbolicznego.
(c) Wyznacz współczynniki Schmidta i concurrence $C$; czy splątanie jest maksymalne?

**PD-4.5 (2 pkt).** Kanał depolaryzujący. $D_p(\rho)=(1-p)\rho+p\,\tfrac I2$ przy $p=0{,}2$,
stan wejściowy $\rho=\lvert0\rangle\langle0\rvert$.
(a) Podaj $\rho'=D_{0{,}2}(\rho)$.
(b) Policz purity $\mathrm{Tr}\,\rho'^2$ i porównaj z $1$.
(c) Policz wierność $F(\rho,\rho')=1-\tfrac p2$ i odległość śladową $D=\tfrac p2$; sprawdź nierówność Fuchsa–van de Graafa.

**PD-4.6 (2 pkt).** Teleportacja kwantowa.
(a) Rozłóż $\lvert\psi\rangle_1\lvert\Phi^+\rangle_{23}$ w bazie Bella kubitów 1 i 2 (podaj cztery składniki).
(b) Podaj bramkę korekty Boba dla każdego z czterech wyników pomiaru Bella.
(c) Uzasadnij, że każdy wynik ma $P=\tfrac14$ i że bez 2 bitów klasycznych teleportacja nie działa.

**PD-4.7 (2 pkt).** Solovay–Kitaev. Koszt kompilacji bramki obrotu $\approx3\log_2(1/\varepsilon)$ bramek $T$.
(a) Oszacuj T-count dla $\varepsilon=10^{-5}$ i $\varepsilon=10^{-9}$.
(b) Ile bramek $T$ kosztuje obwód ze 100 takimi bramkami dla $\varepsilon=10^{-5}$?
(c) Wyjaśnij, dlaczego liczy się **liczbę bramek $T$**, a nie liczbę bramek Clifforda.

**PD-4.8 (2 pkt).** Grover dla $N=16$.
(a) Policz $\theta$ ($\sin\theta=1/\sqrt N$) i $k_{\rm opt}=\mathrm{round}(\tfrac\pi4\sqrt N-\tfrac12)$.
(b) Policz $P_{\rm sukces}$ dla $k=k_{\rm opt}$ i dla $k=4$.
(c) Ile zapytań potrzebuje klasycznie algorytm (średnio) i jaki jest zysk?

**PD-4.9 (2 pkt).** Dekoherencja i CHSH.
(a) Podaj concurrence pary Bella pod tłumieniem fazy z czasem $T_2$; oblicz $C$ przy $t=2T_2$.
(b) Podaj $S(p)=2\sqrt2(1-p)$ dla kanału depolaryzującego i próg $p$, przy którym $S=2$.
(c) Zinterpretuj: dlaczego naruszenie CHSH znika, zanim splątanie zniknie całkowicie?

**PD-4.10 (2 pkt).** Zasada Landauera.
(a) Policz $kT\ln2$ dla $T=300$ K i $T=77$ K (ciekły azot).
(b) Ile ciepła wydzieli skasowanie $10^6$ bitów w $300$ K?
(c) Wyjaśnij w 2–3 zdaniach, dlaczego demon Maxwella nie łamie drugiej zasady termodynamiki.

## Kryteria oceny

Każde zadanie jest warte **2 pkt**; punkty dzielą się tak:

| Element | Punkty |
| --- | --- |
| poprawny tok rozumowania i wzór (z uzasadnieniem) | 1,0 |
| poprawny rachunek liczbowy / wynik | 0,5 |
| wynik z jednostką i niepewnością oraz interpretacja fizyczna | 0,5 |

**Zasady ogólne.**
1. Wynik bez jednostki lub bez niepewności (tam, gdzie trzeba) — maksymalnie 1,5 pkt.
2. Zbyt wiele cyfr znaczących (np. $2{,}452837$) — $-0{,}25$ pkt w zadaniu.
3. Brak interpretacji fizycznej — $-0{,}5$ pkt.
4. Rozwiązania rachunkowe: za samą odpowiedź bez wyprowadzenia — 0,5 pkt (wyjątek: PD-4.4 (b),
   gdzie liczy się jawny rachunek entropii).
5. Sprawdzenie NumPy jest dodatkowo punktowane **tylko** wtedy, gdy podany jest wynik liczbowy
   i zgadza się z rachunkiem ręcznym.
6. Skala samooceny jak w [pracy domowej README](README.md).

## Wskazówki i odpowiedzi

**PD-4.1.** (a) $\bar n=20{,}5$, $s=4{,}649$, $u=s/\sqrt{10}=1{,}470$.
(b) $s^2=21{,}61$ wobec $\bar n=20{,}5$ — iloraz $1{,}05\approx1$, więc dane są zgodne z Poissonem.
(c) $\bar n=20{,}5\pm1{,}5$.

**PD-4.2.** (a) $V^{\mathsf T}WV=\tfrac1{0{,}04}\begin{pmatrix}30&10\\10&5\end{pmatrix}$,
$(V^{\mathsf T}WV)^{-1}=\begin{pmatrix}0{,}004&-0{,}008\\-0{,}008&0{,}024\end{pmatrix}$, więc
$a=1{,}99$, $b=1{,}06$ (z `polyfit` otrzymujemy to samo).
(b) $\chi^2=1{,}275$, $\chi^2_{\rm red}=0{,}425$, $R^2=0{,}9987$ (reszty:
$-0{,}06;0{,}05;-0{,}04;0{,}17;-0{,}12$).
(c) $y(5)=11{,}01$; $\vec g=(5,1)$ daje $u=0{,}210$, czyli $11{,}01\pm0{,}21$.
*Uwaga:* $\chi^2_{\rm red}<1$ sugeruje **zawyżone** $\sigma_i$ — to też wniosek.

**PD-4.3.** (a) $\rho=50/20=2{,}5$ g/cm$^3$.
(b) $u_\rho=\rho\sqrt{(u_m/m)^2+(u_V/V)^2}=2{,}5\sqrt{0{,}02^2+0{,}025^2}=2{,}5\cdot0{,}03202=0{,}080$ g/cm$^3$.
(c) Bo pochodne względne $(\partial\rho/\partial m)(m/\rho)=1$ i $(\partial\rho/\partial V)(V/\rho)=-1$;
wzór ogólny redukuje się do sumy kwadratów niepewności względnych.

**PD-4.4.** (a) $\rho_A=\mathrm{diag}\big(\tfrac14;\tfrac34\big)$ (ślad po $B$ zeruje wyrazy pozadiagonalne).
(b) $S=-\tfrac14\log_2\tfrac14-\tfrac34\log_2\tfrac34=0{,}5+0{,}3113=0{,}811$ bita.
(c) Współczynniki Schmidta: $(\tfrac12;\tfrac{\sqrt3}2)=(0{,}5;0{,}866)$;
$C=2\cdot\tfrac12\cdot\tfrac{\sqrt3}2=\tfrac{\sqrt3}2=0{,}866<1$ — splątanie **nie** jest maksymalne.

**PD-4.5.** (a) $\rho'=0{,}8\lvert0\rangle\langle0\rvert+0{,}1\,I=\mathrm{diag}(0{,}9;0{,}1)$.
(b) $\mathrm{Tr}\,\rho'^2=0{,}81+0{,}01=0{,}82<1$ — stan mieszany.
(c) $F=0{,}9$, $D=0{,}1$; Fuchs–van de Graaf: $1-\sqrt{0{,}9}=0{,}0513\le0{,}1\le\sqrt{0{,}1}=0{,}3162$ ✓.

**PD-4.6.** (a)
$\lvert\Psi\rangle=\tfrac12\big[\lvert\Phi^+\rangle(\alpha\lvert0\rangle+\beta\lvert1\rangle)
+\lvert\Phi^-\rangle(\alpha\lvert0\rangle-\beta\lvert1\rangle)
+\lvert\Psi^+\rangle(\beta\lvert0\rangle+\alpha\lvert1\rangle)
+\lvert\Psi^-\rangle(-\beta\lvert0\rangle+\alpha\lvert1\rangle)\big]$.
(b) Korekty: $\lvert\Phi^+\rangle\to I$, $\lvert\Phi^-\rangle\to Z$, $\lvert\Psi^+\rangle\to X$,
$\lvert\Psi^-\rangle\to ZX$.
(c) Stany Bella są ortonormalne, każdy współczynnik ma moduł $\tfrac12$; bez 2 bitów Bob nie zna
wyniku, więc nie wie, którą z czterech bramek zastosować (średnio odtwarza stan tylko w $\tfrac14$ przypadków).

**PD-4.7.** (a) $\varepsilon=10^{-5}$: $3\log_2(10^5)=3\cdot16{,}61=49{,}8\approx50$;
$\varepsilon=10^{-9}$: $3\log_2(10^9)=3\cdot29{,}90=89{,}7\approx90$.
(b) $100\cdot50=5000$ bramek $T$.
(c) Bramki Clifforda są symulowalne klasycznie (tw. Gottesmana–Knilla) i tanie w realizacji
transversalnej; cała „kwantowa trudność” i koszt fault-tolerancji siedzi w bramkach $T$.

**PD-4.8.** (a) $\theta=\arcsin(1/4)=0{,}2527$;
$k_{\rm opt}=\mathrm{round}\big(\tfrac\pi4\cdot4-\tfrac12\big)=\mathrm{round}(2{,}642)=3$.
(b) $P(3)=\sin^2(7\theta)=0{,}961$; $P(4)=\sin^2(9\theta)=0{,}582$.
(c) Klasycznie średnio $\sim N/2=8$ zapytań; zysk $\approx8/3\approx2{,}7\times$ (asymptotycznie $\sqrt N$).

**PD-4.9.** (a) $C(t)=e^{-t/T_2}$; przy $t=2T_2$: $C=e^{-2}=0{,}135$.
(b) $S(p)=2\sqrt2(1-p)$; $S=2\Rightarrow1-p=\tfrac1{\sqrt2}\Rightarrow p=1-\tfrac{1}{\sqrt2}=0{,}293$.
(c) Splątanie „siedzi” w koherencjach, ale CHSH wymaga ich odpowiednio dużo; dla $p\in(0{,}293;\ 0{,}707)$
stan jest jeszcze splątany, lecz zbyt „rozmyty”, by naruszyć $S=2$.

**PD-4.10.** (a) $kT\ln2$: dla $300$ K $=2{,}871\cdot10^{-21}$ J; dla $77$ K $=7{,}369\cdot10^{-22}$ J.
(b) $10^6\cdot2{,}871\cdot10^{-21}=2{,}871\cdot10^{-15}$ J.
(c) Demon musi zapisać wynik pomiaru; **kasowanie** tej informacji kosztuje co najmniej $kT\ln2$ na bit,
co równoważy pozyskany „zysk” — entropia całego układu (gaz + pamięć demona) nie maleje.

