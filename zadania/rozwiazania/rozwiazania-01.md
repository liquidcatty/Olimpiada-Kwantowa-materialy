# Rozwiązania do rozdziału 01

Pełne rozwiązania zadań Z-01.1–Z-01.8 z rozdziału
[01. Liczby zespolone](../../teoria/01-liczby-zespolone.md).

## Z-01.1

Dane: $z_1=2-3i$, $z_2=1+5i$.

**(a)** Dodajemy części rzeczywiste i urojone oddzielnie:

$$z_1+z_2=(2+1)+(-3+5)i=3+2i.$$

**(b)** Mnożymy rozdzielnie, korzystając z $i^2=-1$:

$$z_1z_2=(2-3i)(1+5i)=2+10i-3i-15i^2=2+7i+15=17+7i.$$

**(c)** Mnożymy licznik i mianownik przez sprzężenie $z_2^*=1-5i$:

$$\frac{2-3i}{1+5i}=\frac{(2-3i)(1-5i)}{1^2+5^2}
=\frac{2-10i-3i+15i^2}{26}=\frac{2-13i-15}{26}=\frac{-13-13i}{26}.$$

**Odpowiedź:** **(a)** $3+2i$, **(b)** $17+7i$, **(c)** $-\tfrac12-\tfrac12 i$.

*Interpretacja:* mnożenie przez sprzężenie zamienia mianownik na liczbę rzeczywistą
$|z_2|^2=26$, co jest standardową metodą dzielenia liczb zespolonych.

## Z-01.2

**(a)** Moduły: $|z|=\sqrt{(-1)^2+(\sqrt3)^2}=\sqrt{1+3}=2$,
$|w|=\sqrt{0^2+(-2)^2}=2$.

**(b)** $z=-1+\sqrt3\,i$ leży w II ćwiartce, więc $\arg z=\pi-\arctan(\sqrt3/1) =\pi-\tfrac{\pi}{3}=\tfrac{2\pi}{3}$; stąd $z=2e^{i2\pi/3}$.
Dla $w=-2i$ leży na ujemnej osi urojonej: $w=2e^{-i\pi/2}=2e^{i3\pi/2}$.

**(c)** Z de Moivre'a $w^8=\bigl(2e^{-i\pi/2}\bigr)^8=2^8e^{-i4\pi}=256\cdot1=256$.

**Odpowiedź:** **(a)** $|z|=|w|=2$, **(b)** $z=2e^{i2\pi/3}$, $w=2e^{-i\pi/2}$,
**(c)** $w^8=256$.

*Interpretacja:* potęga leży na okręgu o promieniu $|w|^8=256$; kąt obraca się
o $8\cdot(-\pi/2)=-4\pi$, czyli wraca do zera — dlatego wynik jest dodatni i rzeczywisty.

## Z-01.3

**(a)** $\sqrt3+i=2\bigl(\tfrac{\sqrt3}{2}+\tfrac12 i\bigr)=2e^{i\pi/6}$. Zatem

$$(\sqrt3+i)^6=\bigl(2e^{i\pi/6}\bigr)^6=2^6e^{i\pi}=64\cdot(-1)=-64.$$

**(b)** $8i=8e^{i\pi/2}$. Pierwiastki trzeciego stopnia:

$$z_k=2\exp\!\Bigl(i\Bigl(\tfrac{\pi}{6}+\tfrac{2\pi k}{3}\Bigr)\Bigr),\quad k=0,1,2.$$

Kolejno: $z_0=2e^{i\pi/6}=\sqrt3+i$, $z_1=2e^{i5\pi/6}=-\sqrt3+i$,
$z_2=2e^{i3\pi/2}=-2i$.

**(c)** Suma: $(\sqrt3-\sqrt3)+(1+1-2)i=0$. Tak musi być, bo wielomian $z^3-8i$ ma
zerowy współczynnik przy $z^2$, a suma pierwiastków równa się temu współczynnikowi
ze znakiem minus: $z_0+z_1+z_2=0$.

**Odpowiedź:** **(a)** $-64$, **(b)** $z\in\{\sqrt3+i,\ -\sqrt3+i,\ -2i\}$,
**(c)** suma wynosi $0$.

*Interpretacja:* pierwiastki $z^3=8i$ tworzą wierzchołki trójkąta równobocznego na
okręgu o promieniu $2$; ich „środek ciężkości” wypada w zerze.

## Z-01.4

**(a)** Niech $z=a+bi$. Wtedy $z^2=(a^2-b^2)+2ab\,i=3-4i$, więc

$$a^2-b^2=3,\qquad 2ab=-4\ \Rightarrow\ ab=-2.$$

Z drugiego $b=-2/a$; podstawiając: $a^2-\dfrac{4}{a^2}=3$, czyli $a^4-3a^2-4=0$,
$(a^2-4)(a^2+1)=0$. Dla rzeczywistego $a$: $a^2=4\Rightarrow a=\pm2$, $b=\mp1$.

**(b)** Sprawdzenie: $(2-i)^2=4-4i+i^2=3-4i$ ✓ oraz $(-2+i)^2=3-4i$ ✓.
$|2-i|=\sqrt{4+1}=\sqrt5$, $|-2+i|=\sqrt5$ — oba pierwiastki mają ten sam moduł
$\sqrt{|3-4i|}=\sqrt5$.

**(c)** $2-i=\sqrt5\,e^{-i\theta}$ z $\theta=\arctan\tfrac12\approx0{,}464$ rad;
$-2+i=\sqrt5\,e^{i(\pi-\theta)}$, $\pi-\theta\approx2{,}678$ rad.

**Odpowiedź:** **(a)** $z=\pm(2-i)$; **(b)** $|z|=\sqrt5\approx2{,}236$;
**(c)** $\sqrt5\,e^{-i0{,}464}$ oraz $\sqrt5\,e^{i2{,}678}$.

*Interpretacja:* pierwiastkowanie „bierze połowę modułu i połowę kąta” — stąd dwa
rozwiązania różniące się o $\pi$ w fazie (czyli o znak).

## Z-01.5

**(a)** $|z-1|=2$ to zbiór punktów odległych od $z_0=1$ (punkt $(1,0)$) o dokładnie
$2$ — **okrąg** o środku $1$ i promieniu $2$.

**(b)** $|z-i|<1$ to punkty bliższe niż $1$ od $z_0=i$ (punkt $(0,1)$) — **otwarte
koło** o środku $i$ i promieniu $1$.

**(c)** Z nierówności trójkąta (i jej wersji różnicowej):

$$\bigl||z_2|-|z_1|\bigr|\le|z_1+z_2|\le|z_1|+|z_2|,\qquad 1\le|z_1+z_2|\le7.$$

Minimum $|z_1+z_2|=1$ zachodzi, gdy $z_1$ i $z_2$ są **przeciwnie skierowane**
($z_2=-\tfrac{4}{3}z_1$); maksimum $7$ — gdy są zgodnie skierowane.

**Odpowiedź:** **(a)** okrąg o środku $1$, promień $2$; **(b)** koło otwarte o środku
$i$, promień $1$; **(c)** $1\le|z_1+z_2|\le7$, minimum przy zwrocie przeciwnym.

*Interpretacja:* moduł sumy jest największy, gdy amplitudy „wzmacniają się” (zgodne
fazy), a najmniejszy, gdy „gaszą się” (fazy przeciwne) — to geometryczny obraz
interferencji.

## Z-01.6

Dane: $|\psi\rangle=(2+i)|0\rangle+(1-2i)|1\rangle$.

**(a)** Liczymy moduły kwadratowe: $|2+i|^2=4+1=5$, $|1-2i|^2=1+4=5$, razem
$N^2=5+5=10$, więc $N=\sqrt{10}$. Stan znormalizowany:

$$|\psi\rangle=\frac{2+i}{\sqrt{10}}|0\rangle+\frac{1-2i}{\sqrt{10}}|1\rangle.$$

**(b)** Prawdopodobieństwa (reguła Borna):
$P(0)=\bigl|\tfrac{2+i}{\sqrt{10}}\bigr|^2=\tfrac{5}{10}=\tfrac12$,
$P(1)=\tfrac{5}{10}=\tfrac12$. Sumują się do $1$ ✓.

**(c)** Faza względna:

$$\frac{c_1}{c_0}=\frac{1-2i}{2+i}=\frac{(1-2i)(2-i)}{(2+i)(2-i)}
=\frac{2-i-4i+2i^2}{5}=\frac{2-5i-2}{5}=-i=e^{-i\pi/2}.$$

**Odpowiedź:** **(a)** $\tfrac{2+i}{\sqrt{10}}|0\rangle+\tfrac{1-2i}{\sqrt{10}}|1\rangle$,
**(b)** $P(0)=P(1)=\tfrac12$, **(c)** $c_1/c_0=e^{-i\pi/2}$.

*Interpretacja:* pomiar w bazie $\{|0\rangle,|1\rangle\}$ da wynik losowy $50/50$;
faza względna $-i$ zmieni wynik dopiero w innej bazie pomiarowej.

## Z-01.7

Dana $U=\dfrac{1}{\sqrt2}\begin{pmatrix}1&i\\ i&1\end{pmatrix}$.

**(a)** $U^\dagger=\dfrac{1}{\sqrt2}\begin{pmatrix}1&-i\\ -i&1\end{pmatrix}$. Liczymy

$$U^\dagger U=\frac12\begin{pmatrix}1&-i\\ -i&1\end{pmatrix}
\begin{pmatrix}1&i\\ i&1\end{pmatrix}
=\frac12\begin{pmatrix}1-i^2&i-i\\ -i+i& -i^2+1\end{pmatrix}
=\frac12\begin{pmatrix}2&0\\ 0&2\end{pmatrix}=I.$$

Skoro $U^\dagger U=I$, to $U$ jest unitarna.

**(b)** $\operatorname{Tr}U=\dfrac{2}{\sqrt2}=\sqrt2$, $\det U=\dfrac{1}{2}\bigl(1\cdot1-i\cdot i\bigr) =\dfrac{1}{2}\bigl(1-i^2\bigr)=\dfrac{1}{2}(2)=1$. Jeśli $\lambda_1\lambda_2=1$ i
$\lambda_1+\lambda_2=\sqrt2=\lambda+\lambda^{-1}$, to $\lambda=e^{\pm i\pi/4}$
($\lambda=e^{i\pi/4},e^{-i\pi/4}$).

**(c)** Dla $|\pm\rangle=\tfrac{1}{\sqrt2}(1,\pm1)^T$:

$$U|+\rangle=\frac{1}{2}\begin{pmatrix}1+i\\ i+1\end{pmatrix}
=\frac{1+i}{\sqrt2}\cdot\frac{1}{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}
=e^{i\pi/4}|+\rangle,\qquad
U|-\rangle=e^{-i\pi/4}|-\rangle.$$

**Odpowiedź:** **(a)** $U^\dagger U=I$ (unitarna), **(b)** $\lambda=e^{\pm i\pi/4}$,
**(c)** wektory własne to $|\pm\rangle$ z fazami $\pm\pi/4$.

*Interpretacja:* $U$ nie zmienia prawdopodobieństw (jest unitarna), a jedynie
„dokleja” fazy do stanów w bazie $X$ — dobry przykład, że bramka fazowa jest
nietrywialna tylko względem wybranej bazy.

## Z-01.8 [★]

**(a)** Pierwiastki to $1,\omega,\omega^2,\dots,\omega^{n-1}$ z $\omega=e^{2\pi i/n}$.
Suma to ciąg geometryczny o ilorazie $\omega\ne1$:

$$\sum_{k=0}^{n-1}\omega^k=\frac{1-\omega^n}{1-\omega}=\frac{1-1}{1-\omega}=0.$$

**(b)** $z^n-1=\prod_{k}(z-\omega^k)$, więc z twierdzenia Viète'a iloczyn pierwiastków
równa się $(-1)^n\cdot(\text{wyraz wolny})=(-1)^n\cdot(-1)=(-1)^{n-1}$.

**(c)** Dla $n=5$: iloczyn $=1$ (zgodnie z
$(-1)^{5-1}=1$), a suma $\approx-7{,}8\cdot10^{-16}\approx0$ ✓.

**Odpowiedź:** **(a)** suma $=0$; **(b)** iloczyn $=(-1)^{n-1}$; **(c)** dla $n=5$:
suma $\approx0$, iloczyn $=1$.

*Interpretacja:* symetria obrotowa na płaszczyźnie zespolonej sprawia, że pierwiastki
z jedynki „znoszą się” w sumie — fakt wielokrotnie wykorzystywany przy dyskretnej
transformacie Fouriera (DFT) w algorytmach kwantowych.
