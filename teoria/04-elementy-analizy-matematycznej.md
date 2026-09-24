# 04. Elementy analizy matematycznej


## 1. Zakres rozdziału

Rozdział obejmuje granice, pochodne i całki (przez części, przez podstawienie) oraz
szeregi Taylora. Omawia równania różniczkowe liniowe I i II rzędu, oscylator
klasyczny, obwód RLC i liczby zespolone w drganiach. Obejmuje też analizę Fouriera
(szereg, transformata, delta Diraca, twierdzenie Parsevala) oraz narzędzia kwantowe:
całkę Gaussa, reprezentację pędową, operator $\hat p=-i\hbar\,d/dx$, paczkę falową
i separację zmiennych w równaniu Schrödingera (rozdział
[05](05-podstawy-mechaniki-kwantowej.md)). Materiał dotyczy zadania P1 (cząstka
w studni potencjału).

## 2. Najważniejsze definicje

- **Granica** $\lim_{x\to x_0}f(x)=L$: wartości $f$ dowolnie blisko $L$, gdy $x$ blisko $x_0$.
- **Pochodna** $f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$ — chwilowa szybkość zmiany.
- **Całka oznaczona** $\int_a^b f(x)dx$ — pole ze znakiem / suma nieskończenie małych.
- **Szereg Taylora**: $f(x)=\sum_{n\ge0}\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n$.
- **Równanie różniczkowe liniowe** rzędu $n$: kombinacja $y,y',\dots,y^{(n)}$ równa
  funkcji znanej; rząd = najwyższa pochodna.
- **Szereg Fouriera**: rozkład funkcji okresowej na $\cos$ i $\sin$.
- **Transformata Fouriera** (*Fourier transform*): $\mathcal{F}[f](\omega) =\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(t)e^{-i\omega t}dt$.
- **Delta Diraca** $\delta(x)$: $\int_{-\infty}^{\infty}\delta(x)f(x)dx=f(0)$.
- **Wartość oczekiwana operatora** $\langle A\rangle=\int\psi^*(x)\,A\,\psi(x)\,dx$.

## 3. Teoria krok po kroku

### 3.1 Granice i pochodna

Granica jest podstawą pochodnych i całek. Kluczowa granica (z niej wynika pochodna
sinusa):

$$
\lim_{x\to0}\frac{\sin x}{x}=1.
$$

Pochodna mierzy **tempo zmiany**: jeśli $x(t)$ to położenie, to $x'(t)=v(t)$
(prędkość), a $x''(t)=a(t)$ (przyspieszenie). Reguły: iloczynu
$(fg)'=f'g+fg'$, ilorazu $\left(\frac fg\right)'=\frac{f'g-fg'}{g^2}$,
łańcuchowa $\frac{d}{dx}f(g(x))=f'(g(x))g'(x)$.

Pochodne, które wracają najczęściej: $(e^{ax})'=ae^{ax}$, $(\sin ax)'=a\cos ax$,
$(\cos ax)'=-a\sin ax$, $(x^n)'=nx^{n-1}$.

### 3.2 Całki: przez części i podstawienie

- **Przez części** (odwrotność reguły iloczynu): $\int u\,dv=uv-\int v\,du$.
  Klasyk: $\int x e^{-x}dx=-(x+1)e^{-x}$, więc $\int_0^\infty xe^{-x}dx=1$.
- **Przez podstawienie**: $\int f(g(x))g'(x)dx=\int f(u)du$. Klasyk:
  $\int x e^{-x^2}dx=-\tfrac12e^{-x^2}$.

Całka oznaczona z funkcji dodatniej to pole pod wykresem; w fizyce
$\int f\,dx$ bywa pracą ($\int F\,dx$), ładunkiem ($\int\rho\,dV$) itd.

### 3.3 Szereg Taylora

Rozwijamy funkcje wokół $x_0$:

$$
f(x)=\sum_{n\ge0}\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n.
$$

Wzory:

$$
e^{x}=\sum_{n\ge0}\frac{x^n}{n!},\quad
\sin x=\sum_{n\ge0}\frac{(-1)^nx^{2n+1}}{(2n+1)!},\quad
\cos x=\sum_{n\ge0}\frac{(-1)^nx^{2n}}{(2n)!},
$$

$$
(1+x)^\alpha=1+\alpha x+\frac{\alpha(\alpha-1)}{2}x^2+\dots,\qquad
\ln(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\dots
$$

Rozwój $e^{i\theta}$ daje wzór Eulera: $e^{i\theta}=\cos\theta+i\sin\theta$.

### 3.4 Równania różniczkowe liniowe I i II rzędu

**I rzędu**: $y'+ay=0\Rightarrow y=Ce^{-at}$ (zanik, rozpad promieniotwórczy).

**II rzędu o stałych współczynnikach**: $ay''+by'+cy=0$. Równanie charakterystyczne
$ar^2+br+c=0$ daje trzy przypadki:
- $r_1\ne r_2$ rzeczywiste: $y=C_1e^{r_1t}+C_2e^{r_2t}$ (przeregulowanie/tłumienie);
- $r_1=r_2$: $y=(C_1+C_2t)e^{rt}$;
- $r_\pm=\alpha\pm i\beta$: $y=e^{\alpha t}(C_1\cos\beta t+C_2\sin\beta t)$ (oscylacje!).

Dla $y''+\omega^2y=0$ mamy $r=\pm i\omega$ i rozwiązanie
$y=A\cos\omega t+B\sin\omega t$.

### 3.5 Oscylator klasyczny

Równanie $m\ddot x=-kx$, czyli $\ddot x=-\omega^2x$ z $\omega=\sqrt{k/m}$; rozwiązanie
$x(t)=A\cos(\omega t+\varphi)$. Energia jest zachowana:

$$
E=\tfrac12m\dot x^2+\tfrac12kx^2=\tfrac12m\omega^2A^2=\text{const}.
$$

Okres $T=2\pi/\omega=2\pi\sqrt{m/k}$ nie zależy od amplitudy. To obraz klasyczny, do
którego w granicy dużych liczb kwantowych wraca oscylator harmoniczny (rozdz. 05).

### 3.6 Liczby zespolone w obwodach RLC

Obwód szeregowy RLC opisuje równanie $L\ddot q+R\dot q+\frac1Cq=0$. Podstawienie
$q=e^{rt}$ daje $Lr^2+Rr+\frac1C=0$, skąd

$$
\omega_0=\frac{1}{\sqrt{LC}},\qquad \gamma=\frac{R}{2L}.
$$

Przy $R<2\sqrt{L/C}$ (niedotłumiony) dostajemy drgania z $\omega=\sqrt{\omega_0^2-\gamma^2}$,
zanikające jak $e^{-\gamma t}$. Zespolony zapis $e^{i\omega t}$ zamienia różniczkowanie
na mnożenie przez $i\omega$ — to „sztuczka” używana też w kwantowej ewolucji
$e^{-iHt/\hbar}$.

### 3.7 Szereg Fouriera

Funkcję okresową o okresie $T$ rozkładamy na składowe harmoniczne:

$$
f(t)=\frac{a_0}{2}+\sum_{n\ge1}\bigl(a_n\cos(n\omega t)+b_n\sin(n\omega t)\bigr),\quad
\omega=\frac{2\pi}{T},
$$

$$
a_n=\frac{2}{T}\int_{-T/2}^{T/2}f(t)\cos(n\omega t)\,dt,\qquad
b_n=\frac{2}{T}\int_{-T/2}^{T/2}f(t)\sin(n\omega t)\,dt.
$$

Dla fali prostokątnej (nieparzystej) zostają tylko nieparzyste sinusy o
amplitudach $b_n=\frac{4}{n\pi}$, $n=1,3,5,\dots$; numerycznie
$b_1\approx1{,}273$, $b_3\approx0{,}424$, $b_5\approx0{,}255$.

### 3.8 Transformata Fouriera, delta Diraca, Parseval

Dla funkcji nieokresowej:

$$
F(\omega)=\mathcal{F}[f](\omega)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(t)e^{-i\omega t}dt,\qquad
f(t)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}F(\omega)e^{i\omega t}d\omega.
$$

- **Gauss → Gauss**: dla $g(t)=e^{-t^2/(2a^2)}$ mamy $G(\omega)=a\,e^{-a^2\omega^2/2}$.
- **Przesunięcie**: $\mathcal{F}[f(t-t_0)](\omega)=e^{-i\omega t_0}F(\omega)$ — opóźnienie
  to liniowa faza.
- **Delta Diraca**: $\delta(t)=\frac{1}{2\pi}\int e^{i\omega t}d\omega$;
  $\int\delta(t-t_0)f(t)dt=f(t_0)$.
- **Parseval**: $\int\lvert f(t)\rvert^2dt=\int\lvert F(\omega)\rvert^2d\omega$ —
  „energia” w czasie = „energia” w częstości.

### 3.9 Całka Gaussa

Podstawowa całka i jej uogólnienie:

$$
\int_{-\infty}^{\infty}e^{-x^2}dx=\sqrt\pi\approx1{,}7725,\qquad
\int_{-\infty}^{\infty}e^{-ax^2}dx=\sqrt{\frac\pi a}.
$$

Pochodna po $a$ daje momenty, np. $\int x^2e^{-ax^2}dx=\frac{1}{2a}\sqrt{\frac\pi a}$.
Gaussowskie funkcje falowe (stan podstawowy oscylatora, paczka minimalna) są
całkowalne właśnie dzięki tym wzorom.

### 3.10 Reprezentacja pędowa i operator $\hat p$

W reprezentacji położenia operator pędu to **pochodna**:

$$
\hat p=-i\hbar\frac{d}{dx}.
$$

Funkcja falowa w reprezentacji pędowej to transformata Fouriera funkcji położeniowej:

$$
\tilde\psi(p)=\frac{1}{\sqrt{2\pi\hbar}}\int e^{-ipx/\hbar}\psi(x)\,dx.
$$

Operator pędu jest hermitowski (całkowanie przez części + znikanie na brzegach), a
jego wartości oczekiwane liczymy ze wzoru
$\langle\hat p\rangle=\int\psi^*(-i\hbar\partial_x)\psi\,dx$.

### 3.11 Paczka falowa i jej rozmywanie

**Paczka gaussowska** minimalnej nieoznaczoności:

$$
\psi(x)=\frac{1}{(\pi a^2)^{1/4}}e^{-x^2/(2a^2)},\qquad
\Delta x=\frac{a}{\sqrt2},\qquad \Delta p=\frac{\hbar}{a\sqrt2},\qquad
\Delta x\,\Delta p=\frac{\hbar}{2}.
$$

To stan nasycający zasadę nieoznaczoności. W czasie paczka **rozmywa się** (dyspersja),
bo składowe o różnych pędach biegną z różnymi prędkościami:

$$
\sigma(t)=\sigma_0\sqrt{1+\Bigl(\frac{\hbar t}{2m\sigma_0^2}\Bigr)^2}.
$$

Dla elektronu i $\sigma_0=1$ nm: po $t=1$ ps szerokość rośnie do $\approx57{,}9$ nm —
paczka „rozpływa się” w skali pikosekund.

### 3.12 Równanie Schrödingera z rozdzieleniem zmiennych

Stacjonarne równanie Schrödingera w 1D:

$$
-\frac{\hbar^2}{2m}\psi''(x)+V(x)\psi(x)=E\psi(x).
$$

Gdy $V(x)$ rozdziela się na sumę części zależnych od osobnych współrzędnych,
szukamy $\psi(x,y,z)=X(x)Y(y)Z(z)$; podstawienie dzieli równanie na niezależne
problemy jednowymiarowe, a całkowita energia jest sumą.
W nieskończonej studni ($V=0$ w $0<x<L$, $\infty$ poza) dostajemy
$\psi_n(x)=\sqrt{\tfrac2L}\sin\frac{n\pi x}{L}$ i $E_n=\frac{n^2\pi^2\hbar^2}{2mL^2}$
— pełne rozwiązanie w rozdziale [05](05-podstawy-mechaniki-kwantowej.md).

## 4. Przykłady rozwiązane

### Przykład 1 (łatwy): przybliżenie Taylora

**Dane:** oszacować $\sin(0{,}1)$ i $\sqrt{1{,}02}$ dwoma/trzema wyrazami.

**Metoda:** szeregi $\sin x=x-\frac{x^3}{6}+\frac{x^5}{120}-\dots$ oraz
$(1+x)^{1/2}=1+\frac12x-\frac18x^2+\dots$

**Rachunek:**

$$
\sin(0{,}1)=0{,}1-\frac{0{,}1^3}{6}+\frac{0{,}1^5}{120}-\dots
=0{,}1-0{,}0001667+0{,}0000000833\approx0{,}0998333,
$$

$$
\sqrt{1{,}02}=(1+0{,}02)^{1/2}=1+\tfrac12(0{,}02)-\tfrac18(0{,}02)^2
=1+0{,}01-0{,}00005=1{,}00995.
$$

Wartości dokładne: $\sin0{,}1=0{,}09983342$, $\sqrt{1{,}02}=1{,}00995049$ — zgodność
do $\approx10^{-7}$.

**Wynik:** $\sin(0{,}1)\approx0{,}0998333$, $\sqrt{1{,}02}\approx1{,}00995$.

**Interpretacja:** dla małych argumentów kilka wyrazów Taylora daje bardzo dużą
dokładność — dlatego w mechanice kwantowej małe kąty/odchyłki opisuje się liniowo
(np. $\sin\theta\approx\theta$ w prawie Malusa dla małych $\theta$).

### Przykład 2 (trudniejszy): oscylator z warunkami początkowymi

**Dane:** $\ddot x=-4x$, $x(0)=1$, $\dot x(0)=0$.

**Metoda:** równanie charakterystyczne, potem warunki początkowe.

**Rachunek:** $r^2=-4\Rightarrow r=\pm2i$, więc $x(t)=A\cos2t+B\sin2t$.
Z $x(0)=1$: $A=1$. Z $\dot x=-2\sin2t+2B\cos2t$, $\dot x(0)=2B=0\Rightarrow B=0$.
Ostatecznie $x(t)=\cos2t$; $\omega=2$, $T=\pi$.

**Wynik:** $x(t)=\cos(2t)$, okres $T=\pi$.

**Interpretacja:** dwie stałe $A,B$ ustala jednoznacznie para warunków początkowych —
to ogólna zasada rozwiązywania równań II rzędu, którą stosujemy potem do funkcji
falowej i jej pochodnej.

### Przykład 3 (trudniejszy): całka Gaussa i normalizacja paczki

**Dane:** znaleźć $A$ tak, by $\psi(x)=Ae^{-x^2/(2a^2)}$ był unormowany; policzyć
$\Delta x,\Delta p$.

**Metoda:** całka Gaussa $\int e^{-x^2/a^2}dx=a\sqrt\pi$.

**Rachunek:** $\int\lvert\psi\rvert^2dx=A^2\int e^{-x^2/a^2}dx=A^2\,a\sqrt\pi=1$,
więc $A=(\pi a^2)^{-1/4}$. Dla $a=1$ nm: $A\approx2{,}38\cdot10^{4}\ \text{m}^{-1/2}$.
Rozrzuty: $\Delta x=\frac{a}{\sqrt2}=0{,}707\ \text{nm}$,
$\Delta p=\frac{\hbar}{a\sqrt2}\approx7{,}46\cdot10^{-26}\ \text{kg\,m/s}$,
iloczyn $\Delta x\,\Delta p=\frac{\hbar}{2}$.

**Wynik:** $A=(\pi a^2)^{-1/4}\approx2{,}38\cdot10^4\ \text{m}^{-1/2}$; $\Delta x\,\Delta p=\hbar/2$.

**Interpretacja:** paczka gaussowska realizuje **minimalną** nieoznaczoność — nie da
się zlokalizować położenia i pędu dokładniej jednocześnie; to kwantowy sens zasady
nieoznaczoności Heisenberga.

## 5. Typowe pułapki

1. **Opuszczanie stałej całkowania.** $\int f'=f+C$; bez stałej rozwiązanie równania
   różniczkowego jest niepełne.
2. **Mylenie mnożenia przez pochodną.** $(fg)'\ne f'g'$; zastosuj regułę iloczynu.
3. **Złe rozwijanie wokół punktu.** Taylor rozwija wokół konkretnego $x_0$; dla
   $x\approx0$ licz na $0$, nie na $1$.
4. **Zapominanie o warunkach brzegowych.** To one „kwantyzują” energie (P1); bez nich
   rozwiązanie równania Schrödingera nie jest jednoznaczne.
5. **Traktowanie pędu klasycznie w reprezentacji położenia.** $\hat p$ to **operator**
   $-i\hbar\partial_x$, nie liczba.
6. **Mylenie szerokości paczki $a$ z $\Delta x$.** Dla gaussowskiej $\Delta x=a/\sqrt2$,
   nie $a$.
7. **Zapominanie o jednostkach $\hbar$.** W $\tilde\psi(p)$ w wykładniku jest
   $e^{-ipx/\hbar}$; zgubienie $\hbar$ to najczęstszy błąd rachunkowy.

## 6. Zadania (Z-04)

**Z-04.1.** (a) Policz $\displaystyle\lim_{x\to0}\frac{\sin x}{x}$.
(b) Policz pochodną $f(x)=x^2e^{-x}$ i drugą pochodną $g''(x)$ dla $g=e^{-x^2}$.
(c) Wyjaśnij fizyczne znaczenie pierwszej i drugiej pochodnej położenia.

**Z-04.2.** (a) Policz $\int_0^\infty xe^{-x}dx$ całkując przez części.
(b) Policz $\int xe^{-x^2}dx$ przez podstawienie. (c) Policz $\int_0^\infty e^{-2x}dx$.

**Z-04.3.** (a) Rozwiń $(1+x)^{1/2}$ do wyrazu $x^2$ i oszacuj $\sqrt{1{,}04}$.
(b) Korzystając z $e^{i\theta}=\cos\theta+i\sin\theta$, wskaż części rzeczywistą i
urojoną. (c) Oszacuj błąd przybliżenia $\cos\theta\approx1-\theta^2/2$ dla
$\theta=0{,}2$.

**Z-04.4.** (a) Rozwiąż $y'+2y=0$ z $y(0)=3$. (b) Rozwiąż $y''+4y=0$.
(c) Nałóż warunki $y(0)=0$, $y'(0)=2$.

**Z-04.5.** Oscylator $m\ddot x=-kx$.
(a) Podaj $\omega$ i rozwiązanie $x(t)$. (b) Wyznacz energię $E$. (c) Wykaż, że okres
nie zależy od amplitudy.

**Z-04.6.** (a) Podaj współczynniki $b_n$ fali prostokątnej (nieparzystej).
(b) Sprawdź twierdzenie Parsevala dla tej fali. (c) Zapisz transformatę Fouriera
$g(t)=e^{-t^2/(2a^2)}$.

**Z-04.7.** (a) Policz $\int_{-\infty}^\infty e^{-x^2}dx$. (b) Znormalizuj
$\psi(x)=Ae^{-x^2/(2a^2)}$. (c) Wyznacz $\Delta x$, $\Delta p$ i ich iloczyn.

**Z-04.8. [★]** Paczka gaussowska $\sigma_0=1$ nm dla elektronu.
(a) Podaj wzór na $\sigma(t)$. (b) Policz $\sigma$ po $t=1$ ps. (c) Wyjaśnij,
dlaczego paczka się rozmywa.

## 7. Wskazówki do zadań

- **Z-04.1.** (a) granica podstawowa; (b) reguła iloczynu i łańcuchowa;
  (c) $v=x'$, $a=x''$.
- **Z-04.2.** (a) $u=x$, $dv=e^{-x}dx$; (b) podstaw $u=-x^2\Rightarrow du=-2x\,dx$;
  (c) całka wykładnicza.
- **Z-04.3.** (a) podstaw $\alpha=\tfrac12$; (c) następny wyraz to $\theta^4/24$.
- **Z-04.4.** (a) rozdziel zmienne; (b)–(c) równanie charakterystyczne i warunki.
- **Z-04.5.** (a) $x=A\cos(\omega t+\varphi)$; (b) $E=\tfrac12m\omega^2A^2$;
  (c) popatrz na $T=2\pi\sqrt{m/k}$.
- **Z-04.6.** (a) $b_n=\frac{4}{n\pi}$ dla nieparzystych; (b) $\sum_{odd}1/n^2=\pi^2/8$;
  (c) skorzystaj z wzoru Gauss $\to$ Gauss.
- **Z-04.7.** (a) całka Gaussa; (b) $\int e^{-x^2/a^2}dx=a\sqrt\pi$; (c) uwzględnij
  $\Delta x=a/\sqrt2$, $\Delta p=\hbar/(a\sqrt2)$.
- **Z-04.8.** [★] Wzór $\sigma(t)=\sigma_0\sqrt{1+(\hbar t/2m\sigma_0^2)^2}$;
  podstaw $\sigma_0=1$ nm, $m=m_e$.

## 8. Co dalej

Te narzędzia są potrzebne w rozdziale
[05. Podstawy mechaniki kwantowej](05-podstawy-mechaniki-kwantowej.md): rozwiązanie
studni potencjału (P1), oscylatora i paczek falowych. Statystykę pomiarów rozwija
rozdział [03](03-rachunek-prawdopodobienstwa-i-statystyka.md), a obwody i sygnały —
rozdział 14 (narzędzia informatyczne). Rozwiązania zadań są w
[rozwiazania-04.md](../zadania/rozwiazania/rozwiazania-04.md); zadania łączące
rozdziały 01–05 to [PD-1](../praca-domowa/praca-domowa-01.md).
