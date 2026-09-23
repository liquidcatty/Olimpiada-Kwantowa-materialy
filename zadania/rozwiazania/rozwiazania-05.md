# Rozwiązania do rozdziału 05

Pełne rozwiązania Z-05.1–Z-05.8 z rozdziału
[05. Podstawy mechaniki kwantowej](../../teoria/05-podstawy-mechaniki-kwantowej.md).
Wyniki sprawdzono numerycznie (stałe: $\hbar=1{,}0546\cdot10^{-34}$ J·s,
$m_e=9{,}109\cdot10^{-31}$ kg, $1$ eV $=1{,}602\cdot10^{-19}$ J).

## Z-05.1

Stan $\lvert\psi\rangle=\cos\tfrac\pi8\lvert0\rangle+\sin\tfrac\pi8\lvert1\rangle$,
$c_0=\cos\tfrac\pi8\approx0{,}9239$, $c_1=\sin\tfrac\pi8\approx0{,}3827$.

**(a)** $P(0)=\cos^2\tfrac\pi8\approx0{,}8536$, $P(1)=\sin^2\tfrac\pi8\approx0{,}1464$
(sumujemy do $1$ ✓).

**(b)** $\langle Z\rangle=P(0)-P(1)=\cos^2\tfrac\pi8-\sin^2\tfrac\pi8=\cos\tfrac\pi4
=\tfrac{1}{\sqrt2}\approx0{,}7071$. Ponieważ współczynniki są rzeczywiste,
$\langle X\rangle=2c_0c_1=\sin\tfrac\pi4=\tfrac{1}{\sqrt2}\approx0{,}7071$.

**(c)** $\operatorname{Var}(Z)=\langle Z^2\rangle-\langle Z\rangle^2=1-\tfrac12=\tfrac12$,
$\Delta Z=\tfrac{1}{\sqrt2}\approx0{,}7071$.

**Odpowiedź:** **(a)** $P(0)\approx0{,}8536$, $P(1)\approx0{,}1464$;
**(b)** $\langle Z\rangle=\langle X\rangle\approx0{,}7071$; **(c)** $\Delta Z\approx0{,}7071$.

*Interpretacja:* kąt $\theta=\pi/4$ na sferze Blocha daje wektor
$\vec r=(\sin\theta,0,\cos\theta)=(\tfrac{1}{\sqrt2},0,\tfrac{1}{\sqrt2})$,
$|\vec r|=1$ — stan „przechylony” między osiami $X$ i $Z$, w płaszczyźnie $x$–$z$
($\langle Y\rangle=0$, bo faza względna zerowa).

## Z-05.2

**(a)** $E_1=\dfrac{\pi^2\hbar^2}{2m_eL^2}$ dla $L=2$ nm:
$$E_1=\frac{\pi^2(1{,}0546\cdot10^{-34})^2}{2\cdot9{,}109\cdot10^{-31}\cdot(2\cdot10^{-9})^2}
\approx1{,}506\cdot10^{-20}\ \text{J}\approx0{,}0940\ \text{eV}.$$

**(b)** $E_n\propto n^2$, więc $E_3/E_1=9$.

**(c)** $\psi_3\propto\sin(3\pi x/L)$ ma **dwa** węzły wewnątrz ($n-1=2$), w
$x=L/3$ i $x=2L/3$.

**Odpowiedź:** **(a)** $E_1\approx0{,}0940$ eV; **(b)** $E_3/E_1=9$;
**(c)** dwa węzły.

*Interpretacja:* każdy kolejny poziom to „wyższa harmoniczna” fali stojącej; liczba
węzłów rośnie liniowo, a energia kwadratowo.

## Z-05.3

**(a)** $P(\uparrow)=\cos^2(\pi/4)=\tfrac12$, $P(\downarrow)=\sin^2(\pi/4)=\tfrac12$.

**(b)** $\langle\sigma_x\rangle=\sin\theta=\sin\tfrac\pi2=1$,
$\langle\sigma_z\rangle=\cos\theta=\cos\tfrac\pi2=0$.

**(c)** Wektor Blocha $\vec r=(1,0,0)$ — stan $\lvert+\rangle$.

**Odpowiedź:** **(a)** $P(\uparrow)=P(\downarrow)=\tfrac12$;
**(b)** $\langle\sigma_x\rangle=1$, $\langle\sigma_z\rangle=0$; **(c)** $\vec r=(1,0,0)$.

*Interpretacja:* pomiar w osi $Z$ daje losowe wyniki, mimo że stan jest „idealnie”
ustalony względem osi $X$ — komplementarność osi pomiarowych.

## Z-05.4

**(a)** Działamy komutatorem na $\psi$: $\hat x\psi=x\psi$,
$\hat p\psi=-i\hbar\psi'$. Wtedy
$$\hat x\hat p\psi=-i\hbar x\psi',\qquad
\hat p\hat x\psi=-i\hbar(x\psi)'=-i\hbar(\psi+x\psi'),$$
skąd $[\hat x,\hat p]\psi=-i\hbar x\psi'+i\hbar\psi+i\hbar x\psi'=i\hbar\psi$, czyli
$[\hat x,\hat p]=i\hbar$.

**(b)** Z $\Delta A\,\Delta B\ge\tfrac12\lvert\langle[A,B]\rangle\rvert$ dla
$A=\hat x$, $B=\hat p$: $\Delta x\,\Delta p\ge\tfrac12\lvert i\hbar\rvert=\hbar/2$.

**(c)** Równość zachodzi dla **paczki gaussowskiej** minimalnej nieoznaczoności:
$\Delta x\,\Delta p=\hbar/2$.

**Odpowiedź:** **(a)** $[\hat x,\hat p]=i\hbar$; **(b)** $\Delta x\Delta p\ge\hbar/2$;
**(c)** stan gaussowski (spójny/koherentny).

*Interpretacja:* nieprzemienność $\hat x$ i $\hat p$ to fundamentalna przyczyna
nieoznaczoności; nie wynika z „niedoskonałości aparatury”, lecz ze struktury teorii.

## Z-05.5

**(a)** Światło niespolaryzowane przez pierwszy polaryzator: $I_1=\tfrac12I_0$.

**(b)** Dalej różnica kątów $\Delta\theta=45^\circ$:
$I_2=I_1\cos^2 45^\circ=\tfrac12I_0\cdot\tfrac12=\tfrac14I_0$.

**(c)** Trzeci polaryzator ($\Delta\theta=45^\circ$ względem drugiego):
$I_3=I_2\cos^2 45^\circ=\tfrac14I_0\cdot\tfrac12=\tfrac18I_0\approx0{,}125I_0$.
Bez środkowego polaryzatora $\Delta\theta=90^\circ$:
$I=\tfrac12I_0\cos^2 90^\circ=0$.

**Odpowiedź:** **(a)** $I_0/2$; **(b)** $I_0/4$; **(c)** $I_0/8$ (z środkowym), $0$ (bez).

*Interpretacja:* wynik $I_0/8$ pokazuje, że pomiar w bazie $45^\circ$ „przygotowuje”
nowy stan, nie będący prostopadłym do wejściowego — efekt nieklasyczny.

## Z-05.6

**(a)** Bariera prostokątna $V_0>E$:
$$T=\Bigl[1+\frac{V_0^2\sinh^2(\kappa a)}{4E(V_0-E)}\Bigr]^{-1},\qquad
\kappa=\frac{\sqrt{2m_e(V_0-E)}}{\hbar}.$$

**(b)** $\kappa=\dfrac{\sqrt{2\cdot9{,}109\cdot10^{-31}\cdot4\cdot1{,}602\cdot10^{-19}}}{1{,}0546\cdot10^{-34}}
\approx1{,}025\cdot10^{10}\ \text{m}^{-1}$, więc
$\kappa a\approx1{,}025\cdot10^{10}\cdot0{,}5\cdot10^{-9}\approx5{,}12$.
Wtedy $\sinh(5{,}12)\approx83{,}6$ i
$$T=\Bigl[1+\frac{(5\cdot1{,}602\cdot10^{-19})^2\cdot(83{,}6)^2}
{4\cdot1{,}602\cdot10^{-19}\cdot4\cdot1{,}602\cdot10^{-19}}\Bigr]^{-1}
\approx9{,}08\cdot10^{-5}.$$

**(c)** Podwojenie $a$ daje $2\kappa a\approx10{,}25$ i $T\approx3{,}22\cdot10^{-9}$;
stosunek $\approx3{,}55\cdot10^{-5}\approx e^{-2\kappa a}$ — gwałtowny, wykładniczy spadek.

**Odpowiedź:** **(a)** wzór jak wyżej; **(b)** $\kappa a\approx5{,}12$,
$T\approx9{,}1\cdot10^{-5}$; **(c)** $T\to3{,}2\cdot10^{-9}$ ($\approx e^{-2\kappa a}$ razy mniej).

*Interpretacja:* tunelowanie jest wykładniczo czułe na grubość bariery — dlatego
prąd STM zmienia się o rzędy wielkości przy zmianie odległości o jedną warstwę atomów.

## Z-05.7

**(a)** Dla studni $L=1$ nm: $E_1=\dfrac{\pi^2\hbar^2}{2m_eL^2}\approx6{,}025\cdot10^{-20}$ J.
Wtedy $E_2=4E_1$ i
$$\omega_{21}=\frac{E_2-E_1}{\hbar}=\frac{3E_1}{\hbar}\approx1{,}71\cdot10^{15}\ \text{rad/s}.$$

**(b)** Okres dudnień $T=\dfrac{2\pi}{\omega_{21}}\approx3{,}67\cdot10^{-15}$ s
$=3{,}67$ fs.

**(c)** Oscylują wielkości zależne od $\lvert\psi(t)\rvert^2$: gęstość
prawdopodobieństwa $\lvert\psi(x,t)\rvert^2$, położenie $\langle x\rangle(t)$ i
kształt paczki; energia i moduły $\lvert c_n\rvert$ pozostają stałe.

**Odpowiedź:** **(a)** $\omega_{21}\approx1{,}71\cdot10^{15}$ rad/s;
**(b)** $T\approx3{,}67$ fs; **(c)** $\langle x\rangle(t)$ i $\lvert\psi(x,t)\rvert^2$.

*Interpretacja:* superpozycja dwóch stanów stacjonarnych tworzy „falującą” chmurę
prawdopodobieństwa — klasycznie cząstka jakby „odbijała się” między ściankami.

## Z-05.8 [★]

**(a)** Rozwiązujemy $i\hbar\frac{d}{dt}\lvert\psi\rangle=\tfrac{\hbar\Omega}{2}X\lvert\psi\rangle$:
$$\lvert\psi(t)\rangle=e^{-iHt/\hbar}\lvert0\rangle
=\Bigl(\cos\tfrac{\Omega t}{2}I-i\sin\tfrac{\Omega t}{2}X\Bigr)\lvert0\rangle
=\cos\tfrac{\Omega t}{2}\lvert0\rangle-i\sin\tfrac{\Omega t}{2}\lvert1\rangle.$$

**(b)** $P(1)=\bigl|-i\sin\tfrac{\Omega t}{2}\bigr|^2=\sin^2\tfrac{\Omega t}{2}$.
Dla $\Omega t=\pi/2$: $P(1)=\sin^2\tfrac\pi4=\tfrac12$.
Dla $\Omega t=\pi$: $P(1)=\sin^2\tfrac\pi2=1$ (pełne odwrócenie).

**(c)** Pełny przeskok ($\lvert0\rangle\to\lvert1\rangle$) zachodzi przy $\Omega t=\pi$,
więc okres $\mathcal T=2\pi/\Omega$, a częstość Rabiego $\Omega$.

**Odpowiedź:** **(a)** $\cos\tfrac{\Omega t}{2}\lvert0\rangle-i\sin\tfrac{\Omega t}{2}\lvert1\rangle$;
**(b)** $P(1)=\tfrac12$ (przy $\pi/2$) i $1$ (przy $\pi$); **(c)** okres $2\pi/\Omega$.

*Interpretacja:* to **oscylacje Rabiego** — kubit przechodzi okresowo między $|0\rangle$
i $|1\rangle$ pod wpływem rezonansowego pola. Dokładnie tak steruje się kubity w
bramce $R_X(\theta)$ (rozdział 06): czas impulsu ustala kąt $\Omega t=\theta$.

## Podsumowanie rozdziału 05

Zadania te pokrywają cały rdzeń I etapu: pomiar i wartości oczekiwane (Z-05.1, Z-05.3),
studnię potencjału (P1, Z-05.2), zasadę nieoznaczoności (Z-05.4), prawo Malusa
(P2, Z-05.5), tunelowanie (Z-05.6), dudnienia (Z-05.7) i oscylacje Rabiego (Z-05.8).
Wszystkie wyniki odtwarzają się numerycznie — stany i operatory w konwencji
[konwencji](../../docs/03-konwencje-i-notacja.md).