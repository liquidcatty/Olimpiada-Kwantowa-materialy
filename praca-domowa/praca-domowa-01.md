# Praca domowa PD-1 (rozdziały 01–05)

> **Zakres:** rozdziały [01](../teoria/01-liczby-zespolone.md)–[05](../teoria/05-podstawy-mechaniki-kwantowej.md).
> **Punktacja:** 10 zadań po **2 pkt**, razem **20 pkt** (próg zaliczenia: 12 pkt).
> **Forma:** rachunek + krótkie uzasadnienie; wyniki przybliżone podawaj z trzema
> cyframi znaczącymi. Można (i warto) wspomagać się numpy — ale rachunek musi być
> widoczny. Stałe: $\hbar=1{,}0546\cdot10^{-34}$ J·s, $m_e=9{,}109\cdot10^{-31}$ kg,
> $c=3{,}00\cdot10^{8}$ m/s, $1$ eV $=1{,}602\cdot10^{-19}$ J.

## Zadania

**PD-1.1 (2 pkt).** (a) Zapisz $z=-1+i$ w postaci biegunowej $|z|e^{i\varphi}$.
(b) Policz $z^6$. (c) Dla stanu $|\psi\rangle=\frac{1}{\sqrt2}\bigl(|0\rangle+e^{i\pi/3}|1\rangle\bigr)$
podaj $P(0)$, $P(1)$ oraz $\langle Y\rangle$.

**PD-1.2 (2 pkt).** Dana $A=\begin{pmatrix}1&2i\\-2i&1\end{pmatrix}$.
(a) Wykaż, że $A$ jest hermitowska. (b) Wyznacz wartości własne. (c) Policz
$\langle A\rangle$ w stanie $|+\rangle$ i sprawdź, że leży między wartościami własnymi.

**PD-1.3 (2 pkt).** Stan $|\psi\rangle=\cos\frac\pi6|0\rangle+\sin\frac\pi6|1\rangle$.
(a) Podaj $P(0),P(1)$ dla pomiaru $\sigma_z$. (b) Policz $\langle\sigma_x\rangle$ i
$\langle\sigma_z\rangle$. (c) Policz $\Delta\sigma_z$.

**PD-1.4 (2 pkt).** (a) Policz $[\sigma_x,\sigma_y]$. (b) Dla stanu $|0\rangle$ policz
$\Delta\sigma_x$ i $\Delta\sigma_y$; sprawdź zasadę nieoznaczoności
$\Delta\sigma_x\Delta\sigma_y\ge\frac12|\langle[\sigma_x,\sigma_y]\rangle|$.
(c) Czy dla $|0\rangle$ nierówność jest nasycona?

**PD-1.5 (2 pkt).** Detektor fotonów rejestruje średnio $\lambda=4$ zliczenia na okienko
(rozkład Poissona). (a) Policz $P(K=3)$. (b) Podaj szum $\sigma_K$. (c) Ile okienek
trzeba zsumować, by wyznaczyć $\lambda$ z dokładnością $1\%$?

**PD-1.6 (2 pkt).** Test prawa Malusa: przez polaryzator pod $60^\circ$ przechodzi
frakcja $\cos^2 60^\circ$ fotonów. Na $1000$ fotonów wejściowych zaobserwowano $270$.
(a) Podaj liczbę oczekiwaną. (b) Policz $\chi^2$. (c) Wyznacz $p$-value i sformułuj
wniosek na poziomie $0{,}05$.

**PD-1.7 (2 pkt).** Paczka gaussowska $\psi(x)=Ae^{-x^2/(2a^2)}$, $a=0{,}5$ nm (elektron).
(a) Wyznacz $A$. (b) Policz $\Delta x$ i $\Delta p$. (c) Policz $\Delta x\,\Delta p$ i
skomentuj wynik.

**PD-1.8 (2 pkt).** Elektron w nieskończonej studni o $L=3$ nm.

## Kryteria oceny

Każde zadanie oceniamy w skali **0–2 pkt** według schematu:

| Punkty | Kryterium |
| --- | --- |
| 2 | poprawny wynik we wszystkich podpunktach + widoczny rachunek i poprawna interpretacja |
| 1 | poprawna metoda, drobny błąd rachunkowy lub brak jednego podpunktu |
| 0 | brak metody, błędna metoda lub wynik bez uzasadnienia |

Ogólne wymagania (dotyczą wszystkich zadań):

1. **Widoczny rachunek.** Sam wynik bez kroków pośrednich to najwyżej 1 pkt.
2. **Notacja** zgodna z [konwencjami](../docs/03-konwencje-i-notacja.md): Dirac,
   małoendianowa kolejność kubitów, $\theta/2$ w $R_X,R_Y,R_Z$.
3. **Jednostki i dokładność.** Wynik liczbowy z jednostką SI (lub eV, nm — jawnie)
   i trzema cyframi znaczącymi.
4. **Interpretacja.** Jedno zdanie „co to znaczy” (np. zgodność z teorią, splątanie,
   minimalna nieoznaczoność).
5. **Oznaczenie wspomagania.** Jeśli użyto numpy/AI, wskaż, gdzie i w jakim zakresie
   (wymóg regulaminu Etapu I).

## Wskazówki i odpowiedzi

**PD-1.1.** (a) $|z|=\sqrt2$, $\arg z=3\pi/4$, więc $z=\sqrt2\,e^{i3\pi/4}$.
(b) $z^6=(\sqrt2)^6e^{i9\pi/2}=8e^{i\pi/2}=8i$.
(c) $P(0)=P(1)=\tfrac12$; $\langle Y\rangle=\sin\varphi=\sin\frac\pi3=\frac{\sqrt3}{2}\approx0{,}866$.

**PD-1.2.** (a) $A^\dagger=A$ (przekątna rzeczywista, wyrazy poza sprzężone).
(b) $\det(A-\lambda I)=(1-\lambda)^2-4=0\Rightarrow\lambda\in\{-1,3\}$.
(c) $\langle A\rangle=\frac12(1+1)=1$; istotnie $-1\le1\le3$.

**PD-1.3.** (a) $P(0)=\cos^2\frac\pi6=\tfrac34$, $P(1)=\tfrac14$.
(b) $\langle\sigma_x\rangle=\sin\frac\pi3=\frac{\sqrt3}{2}\approx0{,}866$;
$\langle\sigma_z\rangle=\cos\frac\pi3=\tfrac12$.
(c) $\Delta\sigma_z=\sqrt{1-(1/2)^2}=\frac{\sqrt3}{2}\approx0{,}866$.

**PD-1.4.** (a) $[\sigma_x,\sigma_y]=2i\sigma_z$.
(b) $\Delta\sigma_x=\Delta\sigma_y=1$; prawa strona
$\frac12|2i\langle\sigma_z\rangle|=\langle\sigma_z\rangle=1$ —
nierówność $1\ge1$ spełniona.
(c) Tak, dla $|0\rangle$ nierówność jest **nasycona** (równość).

**PD-1.5.** (a) $P(K=3)=e^{-4}\frac{4^3}{3!}=e^{-4}\frac{64}{6}\approx0{,}1954$.
(b) $\sigma_K=\sqrt\lambda=2$.
(c) Błąd względny średniej to $1/\sqrt{N\lambda}$; przyrównanie do $0{,}01$ daje
$N\lambda=10^4$, czyli $N=2500$ okienek.

**PD-1.9.** (a) $|\psi(t)\rangle=\cos\frac{\Omega t}{2}|0\rangle-i\sin\frac{\Omega t}{2}|1\rangle$.
(b) $P(1)=\sin^2\frac{\Omega t}{2}$; dla $\Omega t=\pi/3$: $P(1)=\sin^2\frac\pi6=\frac14$.
(c) Pełny przeskok przy $\Omega t=\pi$, więc $t=\pi/\Omega$ (okres oscylacji Rabiego
$\mathcal T=2\pi/\Omega$).

**PD-1.10.** Deklaracja: baza $|00\rangle,|01\rangle,|10\rangle,|11\rangle$
(małoendianowo); kubit 1 = górny (starszy bit), kubit 0 = dolny (młodszy).
(a) Krok po kroku:
$$|00\rangle\xrightarrow{H\otimes I}\tfrac{1}{\sqrt2}(|00\rangle+|10\rangle)
\xrightarrow{I\otimes R_Y(\pi/3)}
\tfrac{1}{\sqrt2}\Bigl[\tfrac{\sqrt3}{2}|00\rangle+\tfrac12|01\rangle
+\tfrac{\sqrt3}{2}|10\rangle+\tfrac12|11\rangle\Bigr].$$
CNOT (kontrola = kubit 1) zamienia $|10\rangle\leftrightarrow|11\rangle$:
$$|\psi_{\rm out}\rangle=\frac{\sqrt3}{2\sqrt2}|00\rangle+\frac{1}{2\sqrt2}|01\rangle
+\frac{1}{2\sqrt2}|10\rangle+\frac{\sqrt3}{2\sqrt2}|11\rangle.$$
(b) $P(00)=P(11)=\frac38=0{,}375$, $P(01)=P(10)=\frac18=0{,}125$ (suma $=1$ ✓).
(c) Macierz współczynników
$\begin{pmatrix}\sqrt3&1\\1&\sqrt3\end{pmatrix}/(2\sqrt2)$ ma wartości osobliwe
$$s_1=\frac{\sqrt3+1}{2\sqrt2}\approx0{,}966,\qquad s_2=\frac{\sqrt3-1}{2\sqrt2}
\approx0{,}259.$$
Obie są niezerowe ($s_1^2\approx0{,}933$, $s_2^2\approx0{,}067$), więc stan **jest splątany**;
jego entropia splątania $S=-s_1^2\log_2 s_1^2-s_2^2\log_2 s_2^2\approx0{,}35$ bita.

## Rozkład punktów i tematy

| Zadanie | Rozdziały | Temat | Punkty |
| --- | --- | --- | --- |
| PD-1.1 | 01, 05 | postać biegunowa, potęgowanie, faza amplitudy | 2 |
| PD-1.2 | 02, 01 | operator hermitowski, wartości własne | 2 |
| PD-1.3 | 02, 05 | spin, sfera Blocha, wariancja | 2 |
| PD-1.4 | 02, 05 | komutator, zasada nieoznaczoności | 2 |
| PD-1.5 | 03, 05 | rozkład Poissona, szum zliczeń | 2 |
| PD-1.6 | 03, 02 | test $\chi^2$, prawo Malusa | 2 |
| PD-1.7 | 04, 05 | paczka gaussowska, nieoznaczoność | 2 |
| PD-1.8 | 04, 05 | studnia potencjału, emisja fotonu | 2 |
| PD-1.9 | 05, 02 | oscylacje Rabiego | 2 |
| PD-1.10 | 02, 05, 01 | obwód dwukubitowy, splątanie | 2 |
| **Razem** | | | **20** |

**Kolejny krok.** Po zaliczeniu PD-1 przejdź do rozdziałów 06–10 i pracy domowej
PD-2; rozwiązania zadań z rozdziałów znajdziesz w katalogu
[`zadania/rozwiazania/`](../zadania/rozwiazania/rozwiazania-01.md).

**PD-1.6.** (a) Oczekiwane $1000\cos^2 60^\circ=1000\cdot\frac14=250$.
(b) $\chi^2=\frac{(270-250)^2}{250}+\frac{(730-750)^2}{750}=1{,}6+0{,}533\approx2{,}133$.
(c) Dla $\mathrm{df}=1$, $p=2(1-\Phi(\sqrt{2{,}133}))\approx0{,}144>0{,}05$ — **brak podstaw**
do odrzucenia prawa Malusa.

**PD-1.7.** (a) $A=(\pi a^2)^{-1/4}\approx3{,}36\cdot10^{4}\ \text{m}^{-1/2}$.
(b) $\Delta x=\frac{a}{\sqrt2}\approx0{,}354\ \text{nm}$;
$\Delta p=\frac{\hbar}{a\sqrt2}\approx1{,}49\cdot10^{-25}\ \text{kg\,m/s}$.
(c) $\Delta x\,\Delta p=\hbar/2$ — stan minimalnej nieoznaczoności.

**PD-1.8.** (a) $E_1=\frac{\pi^2\hbar^2}{2m_eL^2}\approx0{,}0418$ eV.
(b) $E_2-E_1=3E_1\approx0{,}125$ eV.
(c) $\lambda=\frac{hc}{E_2-E_1}\approx9{,}89\ \mu\text{m}$ (podczerwień).
(a) Policz $E_1$. (b) Policz $E_2-E_1$. (c) Wyznacz długość fali fotonu emitowanego
przy przejściu $2\to1$.

**PD-1.9 (2 pkt).** Kubit z $H=\frac{\hbar\Omega}{2}X$, start w $|0\rangle$.
(a) Podaj $|\psi(t)\rangle$. (b) Policz $P(1)$ dla $\Omega t=\pi/3$. (c) Podaj czas
potrzebny na pełny przeskok $|0\rangle\to|1\rangle$.

**PD-1.10 (2 pkt).** Obwód dwukubitowy (styl zadania P4): start w $|00\rangle$, następnie
$H$ na kubicie 1, potem $R_Y(\pi/3)$ na kubicie 0, na końcu CNOT (kontrola: kubit 1,
cel: kubit 0). Konwencja małoendianowa.
(a) Wyznacz stan końcowy. (b) Podaj prawdopodobieństwa wszystkich czterech wyników.
(c) Sprawdź, czy stan jest splątany (oblicz wartości Schmidta).