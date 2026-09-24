# Rozwiązania do rozdziału 04

Pełne rozwiązania Z-04.1–Z-04.8 z rozdziału
[04. Elementy analizy matematycznej](../../teoria/04-elementy-analizy-matematycznej.md).

## Z-04.1

**(a)** $\displaystyle\lim_{x\to0}\frac{\sin x}{x}=1$. To pochodna sinusa w zerze:
$\sin'x=\cos x$ i $\cos0=1$.

**(b)** $f(x)=x^2e^{-x}$: reguła iloczynu daje
$f'(x)=2xe^{-x}-x^2e^{-x}=(2x-x^2)e^{-x}$.
Dla $g(x)=e^{-x^2}$: $g'=-2xe^{-x^2}$, a z reguły iloczynu
$g''=-2e^{-x^2}+(-2x)(-2x)e^{-x^2}=(4x^2-2)e^{-x^2}$.

**(c)** Jeśli $x(t)$ to położenie, to $x'(t)=v(t)$ to prędkość, a $x''(t)=a(t)$ to
przyspieszenie; druga pochodna wchodzi do II zasady dynamiki $F=mx''$.

**Odpowiedź:** **(a)** $1$; **(b)** $f'=(2x-x^2)e^{-x}$, $g''=(4x^2-2)e^{-x^2}$;
**(c)** $x'$ — prędkość, $x''$ — przyspieszenie.

*Interpretacja:* znikanie $g''$ w $x=\pm1/\sqrt2$ to punkty przegięcia krzywej
Gaussa — tam „gęstość” przestaje rosnąć i maleć.

## Z-04.2

**(a)** Przez części z $u=x$, $dv=e^{-x}dx$ (więc $du=dx$, $v=-e^{-x}$):

$$
\int_0^\infty xe^{-x}dx=\bigl[-xe^{-x}\bigr]_0^\infty+\int_0^\infty e^{-x}dx
=0+1=1.
$$

**(b)** Podstawiając $u=-x^2$, $du=-2x\,dx$:

$$
\int xe^{-x^2}dx=-\tfrac12\int e^{u}du=-\tfrac12e^{-x^2}+C.
$$

**(c)** $\int_0^\infty e^{-2x}dx=\bigl[-\tfrac12e^{-2x}\bigr]_0^\infty=\tfrac12$.

**Odpowiedź:** **(a)** $1$; **(b)** $-\tfrac12e^{-x^2}+C$; **(c)** $\tfrac12$.

*Interpretacja:* całka (a) to $\Gamma(2)=1!$; tego typu momenty rozkładu wykładniczego
opisują np. średni czas życia stanu wzbudzonego.

## Z-04.3

**(a)** $(1+x)^{1/2}=1+\tfrac12x-\tfrac18x^2+\dots$ Dla $x=0{,}04$:

$$
\sqrt{1{,}04}\approx1+0{,}02-\tfrac18(0{,}0016)=1+0{,}02-0{,}0002=1{,}0198.
$$

Wartość dokładna $1{,}019804$ — zgadza się do $\approx4\cdot10^{-6}$.

**(b)** $e^{i\theta}=\cos\theta+i\sin\theta$, więc $\mathrm{Re}= \cos\theta$,
$\mathrm{Im}=\sin\theta$; moduł $\lvert e^{i\theta}\rvert=1$.

**(c)** Błąd $\cos\theta-(1-\tfrac{\theta^2}{2})\approx\frac{\theta^4}{24}$. Dla
$\theta=0{,}2$: $\frac{0{,}0016}{24}\approx6{,}7\cdot10^{-5}$.

**Odpowiedź:** **(a)** $\approx1{,}0198$; **(b)** $\mathrm{Re}=\cos\theta$,
$\mathrm{Im}=\sin\theta$; **(c)** $\approx6{,}7\cdot10^{-5}$.

*Interpretacja:* przybliżenie małokątowe $\cos\theta\approx1-\theta^2/2$ jest znakomite
do $\theta\approx0{,}3$ rad; dalej trzeba brać więcej wyrazów.

## Z-04.4

**(a)** $y'+2y=0$: rozdzielamy $\frac{dy}{y}=-2dt$, stąd $\ln y=-2t+C$ i
$y=Ce^{-2t}$. Warunek $y(0)=3$ daje $C=3$, czyli $y=3e^{-2t}$.

**(b)** $y''+4y=0$: równanie charakterystyczne $r^2+4=0$, $r=\pm2i$, więc
$y=A\cos2t+B\sin2t$.

**(c)** $y(0)=A=0$; $y'=-2A\sin2t+2B\cos2t$, $y'(0)=2B=2\Rightarrow B=1$.
Ostatecznie $y=\sin2t$.

**Odpowiedź:** **(a)** $y=3e^{-2t}$; **(b)** $y=A\cos2t+B\sin2t$; **(c)** $y=\sin2t$.

*Interpretacja:* równanie II rzędu ma dwuwymiarową przestrzeń rozwiązań — dwie stałe
$A,B$ dobiera się z warunków początkowych, dokładnie jak amplitudy superpozycji
dwóch stanów.

## Z-04.5

**(a)** $m\ddot x=-kx\Rightarrow\ddot x=-\omega^2x$ z $\omega=\sqrt{k/m}$; rozwiązanie
$x(t)=A\cos(\omega t+\varphi)$.

**(b)** $E=\tfrac12m\dot x^2+\tfrac12kx^2=\tfrac12m\omega^2A^2\sin^2(\omega t+\varphi) +\tfrac12kA^2\cos^2(\omega t+\varphi)=\tfrac12kA^2=\tfrac12m\omega^2A^2$
(korzystamy z $k=m\omega^2$); stała ruchu.

**(c)** Okres $T=2\pi/\omega=2\pi\sqrt{m/k}$ zależy tylko od $m,k$, nie od $A$.

**Odpowiedź:** **(a)** $\omega=\sqrt{k/m}$, $x=A\cos(\omega t+\varphi)$;
**(b)** $E=\tfrac12m\omega^2A^2$; **(c)** $T=2\pi\sqrt{m/k}$ niezależne od $A$.

*Interpretacja:* izochronizm — okres drgań nie zależy od amplitudy (dla oscylatora
harmonicznego); to cecha odróżniająca go od wahadła matematycznego przy dużych kątach.

## Z-04.6

**(a)** Dla fali prostokątnej nieparzystej (wartość $+1$ na połowie okresu, $-1$
na drugiej) współczynniki cosinusowe znikają, a

$$
b_n=\frac{4}{n\pi}\quad(n=1,3,5,\dots).
$$

Wartości $b_1\approx1{,}273$, $b_3\approx0{,}424$, $b_5\approx0{,}255$.

**(b)** Średni kwadrat fali wynosi $\frac1T\int f^2dt=1$. Z Parsevala

$$
\frac1T\int f^2dt=\sum_{n\ \text{nieparzyste}}\frac{b_n^2}{2}
=\sum_{n\ \text{nieparzyste}}\frac{8}{n^2\pi^2}=\frac{8}{\pi^2}\cdot\frac{\pi^2}{8}=1.
$$

Zgadza się (korzystamy z $\sum_{n\ \text{nieparzyste}}1/n^2=\pi^2/8$).

**(c)** Dla $g(t)=e^{-t^2/(2a^2)}$: $G(\omega)=a\,e^{-a^2\omega^2/2}$ — Gauss
przechodzi w Gaussa, a szerokości są odwrotnie proporcjonalne.

**Odpowiedź:** **(a)** $b_n=4/(n\pi)$, $n$ nieparzyste; **(b)** Parseval spełniony,
suma $=1$; **(c)** $G(\omega)=ae^{-a^2\omega^2/2}$.

*Interpretacja:* im węższa fala prostokątna w czasie, tym więcej harmonicznych
potrzeba, by ją odtworzyć — to ta sama „komplementarność” szerokości, co przy paczce
falowej (czas–częstość ↔ położenie–pęd).

## Z-04.7

**(a)** $\int_{-\infty}^{\infty}e^{-x^2}dx=\sqrt\pi\approx1{,}7725$.

**(b)** $\int\lvert\psi\rvert^2dx=A^2\int e^{-x^2/a^2}dx=A^2\,a\sqrt\pi=1$,
więc $A=(\pi a^2)^{-1/4}$. Dla $a=1$ nm: $A\approx2{,}38\cdot10^4\ \text{m}^{-1/2}$.

**(c)** Dla rozkładu $\lvert\psi\rvert^2\propto e^{-x^2/a^2}$ (normalny o wariancji
$a^2/2$): $\Delta x=a/\sqrt2$. W przestrzeni pędowej paczka też jest gaussowska,
z $\Delta p=\hbar/(a\sqrt2)$. Iloczyn:
$\Delta x\,\Delta p=\frac{a}{\sqrt2}\cdot\frac{\hbar}{a\sqrt2}=\frac{\hbar}{2}$.

**Odpowiedź:** **(a)** $\sqrt\pi\approx1{,}7725$; **(b)** $A=(\pi a^2)^{-1/4}$;
**(c)** $\Delta x=a/\sqrt2$, $\Delta p=\hbar/(a\sqrt2)$, $\Delta x\Delta p=\hbar/2$.

*Interpretacja:* to stan minimalnej nieoznaczoności — dokładnie „najbardziej
klasyczna” paczka kwantowa, jaką można przygotować.

## Z-04.8 [★]

**(a)** Dla swobodnej paczki gaussowskiej o początkowym odchyleniu $\sigma_0$:

$$
\sigma(t)=\sigma_0\sqrt{1+\Bigl(\frac{\hbar t}{2m\sigma_0^2}\Bigr)^2}.
$$

**(b)** Dla elektronu $m=m_e=9{,}109\cdot10^{-31}$ kg, $\sigma_0=10^{-9}$ m,
$t=10^{-12}$ s:

$$
\frac{\hbar t}{2m\sigma_0^2}=\frac{1{,}0546\cdot10^{-34}\cdot10^{-12}}
{2\cdot9{,}109\cdot10^{-31}\cdot10^{-18}}\approx57{,}892,
$$

skąd $\sigma\approx10^{-9}\cdot57{,}892\approx5{,}79\cdot10^{-8}$ m $=57{,}9$ nm.

**(c)** Składowe o większym pędzie biegną szybciej niż o mniejszym; początkowo
„skorelowana” paczka rozjeżdża się, więc w przestrzeni położenia szerokość rośnie.
To klasyczna **dyspersja** fali materii.

**Odpowiedź:** **(a)** $\sigma(t)=\sigma_0\sqrt{1+(\hbar t/2m\sigma_0^2)^2}$;
**(b)** $\sigma(1\,\text{ps})\approx57{,}9$ nm (rozszerzenie $\approx58\times$);
**(c)** rozmycie spowodowane różnymi prędkościami składowych pędowych.

*Interpretacja:* paczka elektronowa zachowuje się jak „fala”, która rozpływa się
bardzo szybko — w nanoskali ps to ogromny efekt, kluczowy dla czasu koherencji
kubitów.
