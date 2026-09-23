# Rozwiązania do rozdziału 03

Pełne rozwiązania Z-03.1–Z-03.8 z rozdziału
[03. Rachunek prawdopodobieństwa i statystyka](../../teoria/03-rachunek-prawdopodobienstwa-i-statystyka.md).

## Z-03.1

Przestrzeń zdarzeń to $36$ jednakowo prawdopodobnych par $(i,j)$, $i,j\in\{1,\dots,6\}$.

**(a)** Suma $=7$ dla par $(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)$ — $6$ sprzyjających:
$P=\dfrac{6}{36}=\dfrac16\approx0{,}1667$.

**(b)** Przy warunku „pierwsza $=3$” pozostaje $6$ wyników $(3,j)$; sprzyja tylko
$j=4$: $P=\dfrac16\approx0{,}1667$.

**(c)** $A$ = „suma $7$”, $B$ = „pierwsza $=3$”. Mamy $P(A)=P(B)=\tfrac16$,
$P(A\cap B)=P(\text{druga}=4)=\tfrac16$. Ponieważ $P(A)P(B)=\tfrac1{36}\ne\tfrac16$,
zdarzenia **nie są** niezależne: znajomość $B$ zmienia (tu: zwiększa) szansę $A$.

**Odpowiedź:** **(a)** $\tfrac16\approx0{,}167$; **(b)** $\tfrac16\approx0{,}167$;
**(c)** nie są niezależne.

*Interpretacja:* mimo że (a) i (b) dają tę samą liczbę, to nie przypadek — dla sumy
$7$ warunek „pierwsza $=3$” nie zmienia prawdopodobieństwa, bo $7$ jest „idealnie
środkową” sumą; ale globalnie zdarzenia są zależne, o czym świadczy $P(A\cap B)=1/6$.

## Z-03.2

**(a)** Prawdopodobieństwo całkowite wyniku dodatniego:
$P(+)=0{,}99\cdot0{,}001+0{,}05\cdot0{,}999=0{,}00099+0{,}04995=0{,}05094$.
Z Bayesa

$$P(C\mid +)=\frac{0{,}99\cdot0{,}001}{0{,}05094}=\frac{0{,}00099}{0{,}05094}\approx0{,}0194.$$

**(b)** Dla wyniku negatywnego prawdopodobieństwo całkowite
$P(-)=0{,}01\cdot0{,}001+0{,}95\cdot0{,}999=0{,}00001+0{,}94905=0{,}94906$;

$$P(H\mid -)=\frac{0{,}95\cdot0{,}999}{0{,}94906}\approx0{,}99999.$$

**(c)** Dodatni wynik daje tylko $\approx1{,}9\%$ szansy choroby, choć test jest
„dobry” (czułość $99\%$). Decyduje **małe prawdopodobieństwo aprioryczne**
$P(C)=0{,}001$: fałszywe alarmy powstają licznie ($\approx5\%$ ze $99{,}9\%$
zdrowych), zalewając nieliczne prawdziwe trafienia.

**Odpowiedź:** **(a)** $P(C\mid\!+)\approx0{,}019$; **(b)** $P(H\mid\!-)\approx0{,}99999$;
**(c)** priorytet ma prawdopodobieństwo aprioryczne.

*Interpretacja:* to lekcja pokory — pojedynczy „sygnał” przy rzadkim zdarzeniu jest
zwykle szumem; potrzebna jest powtórna weryfikacja.

## Z-03.3

**(a)** $\mathbb{E}X=\dfrac16(1+2+3+4+5+6)=\dfrac{21}{6}=3{,}5$.

**(b)** $\mathbb{E}X^2=\dfrac16(1+4+9+16+25+36)=\dfrac{91}{6}\approx15{,}167$,
więc $\operatorname{Var}X=\mathbb{E}X^2-(\mathbb{E}X)^2=\dfrac{91}{6}-\dfrac{49}{4} =\dfrac{182-147}{12}=\dfrac{35}{12}\approx2{,}917$.

**(c)** Otrzymaliśmy $\mathbb{E}X^2=\dfrac{91}{6}\approx15{,}17$, a związek
$\operatorname{Var}X=\mathbb{E}X^2-(\mathbb{E}X)^2=15{,}167-12{,}25=2{,}917$ się zgadza.

**Odpowiedź:** **(a)** $3{,}5$; **(b)** $\tfrac{35}{12}\approx2{,}92$;
**(c)** $\mathbb{E}X^2=\tfrac{91}{6}\approx15{,}17$, związek spełniony.

*Interpretacja:* średnia $3{,}5$ nie jest możliwym wynikiem rzutu — wartość oczekiwana
to środek rozkładu, nie „typowa” realizacja.

## Z-03.4

**(a)** $P(X=3)=\binom{10}{3}\bigl(\tfrac12\bigr)^{10}=\dfrac{120}{1024}\approx0{,}1172$.

**(b)** $P(K=2)=e^{-3}\dfrac{3^2}{2!}=e^{-3}\cdot4{,}5\approx0{,}2240$;
$P(K=0)=e^{-3}\approx0{,}0498$.

**(c)** Dwumianowy: $\mathbb{E}X=np=5$, $\operatorname{Var}X=np(1-p)=2{,}5$.
Poisson: $\mathbb{E}K=\operatorname{Var}K=\lambda=3$. Poisson powstaje z dwumianowego
w granicy rzadkich zdarzeń: $n\to\infty$, $p\to0$ przy $\lambda=np$ ustalonym
(wtedy $\operatorname{Var}=np(1-p)\to np=\lambda$, bo $1-p\to1$).

**Odpowiedź:** **(a)** $0{,}1172$; **(b)** $P(K=2)\approx0{,}224$, $P(K=0)\approx0{,}050$;
**(c)** Poisson ma $\mathbb{E}=\operatorname{Var}=\lambda$; jest granicą dwumianowego.

*Interpretacja:* w granicy rzadkich zdarzeń wariancja „przestaje” maleć z $p$ —
dlatego zliczenia fotonów cechuje charakterystyczny szum $\sqrt\lambda$.

## Z-03.5

**(a)** Dla $Z\sim\mathcal{N}(0,1)$: $P(|Z|<2)=2\Phi(2)-1\approx0{,}9545$.

**(b)** $X\sim\mathrm{Bin}(100,\tfrac12)$: $\mu=np=50$, $\sigma=\sqrt{np(1-p)}=\sqrt{25}=5$.
Z korekcją ciągłości zamieniamy $45\le X\le55$ na $44{,}5\le X\le55{,}5$:

$$z_1=\frac{44{,}5-50}{5}=-1{,}1,\qquad z_2=\frac{55{,}5-50}{5}=1{,}1,$$

$$P\approx\Phi(1{,}1)-\Phi(-1{,}1)=2\Phi(1{,}1)-1\approx0{,}7287.$$

**(c)** Dokładnie $\sum_{k=45}^{55}\binom{100}{k}/2^{100}\approx0{,}7287$ — zgadza się
do czterech cyfr. CTG z korekcją ciągłości daje praktycznie dokładny wynik nawet dla
$n=100$.

**Odpowiedź:** **(a)** $0{,}9545$; **(b)** $\approx0{,}729$; **(c)** wynik dokładny
$\approx0{,}7287$.

*Interpretacja:* „prawie cała masa” leży w $\pm2\sigma$ — dlatego błąd $2\sigma$ jest
standardowym kryterium rozrzutu, także przy pomiarach kwantowych.

## Z-03.6

**(a)** $\rho=\dfrac{m}{V}=\dfrac{200\ \text{g}}{50{,}0\ \text{mL}}=4{,}00\ \text{g/mL}$.

**(b)** Dla ilorazu niepewności względne dodają się kwadratowo:

$$\frac{\sigma_\rho}{\rho}=\sqrt{\Bigl(\frac{\sigma_m}{m}\Bigr)^2+\Bigl(\frac{\sigma_V}{V}\Bigr)^2}
=\sqrt{(0{,}01)^2+(0{,}01)^2}=0{,}01414,$$

skąd $\sigma_\rho=4{,}00\cdot0{,}01414\approx0{,}0566\ \text{g/mL}$.

**(c)** Oba pomiary mają **taką samą** niepewność względną $1\%$, więc poprawa
jednego z nich dałaby tylko częściową korzyść: obniżenie każdej z $1\%$ do $0{,}5\%$
zmniejsza $\sigma_\rho/\rho$ do $0{,}00707$, czyli $\sigma_\rho\approx0{,}028$.

**Odpowiedź:** **(a)** $4{,}00\ \text{g/mL}$; **(b)** $\sigma_\rho\approx0{,}057\ \text{g/mL}$;
**(c)** oba wkłady równe ($1\%$), trzeba poprawić oba.

*Interpretacja:* gdy jeden błąd dominuje, poprawa pozostałych nic nie daje; tu wkłady
są zrównoważone, więc oba pomiary wymagają poprawy, aby istotnie zwiększyć precyzję.

## Z-03.7

**(a)** $\chi^2=\dfrac{(12-10)^2}{10}+\dfrac{(8-10)^2}{10}+\dfrac{(10-10)^2}{10} =\dfrac{4+4+0}{10}=0{,}8$.

**(b)** Dla $\mathrm{df}=k-1=2$ zachodzi $p=P(\chi^2>0{,}8)=e^{-0{,}8/2}=e^{-0{,}4} \approx0{,}670$. Ponieważ $p\gg0{,}05$, **nie ma podstaw do odrzucenia** hipotezy —
obserwacje zgadzają się z rozkładem równomiernym.

**(c)** $H(0{,}5)=-0{,}5\log_2 0{,}5-0{,}5\log_2 0{,}5=1$ bit;
$H(0{,}1)=-0{,}1\log_2 0{,}1-0{,}9\log_2 0{,}9\approx0{,}469$ bita.

**Odpowiedź:** **(a)** $\chi^2=0{,}8$; **(b)** $p\approx0{,}670$, brak podstaw do
odrzucenia; **(c)** $H(0{,}5)=1$ bit, $H(0{,}1)\approx0{,}469$ bita.

*Interpretacja:* $\chi^2<1$ na jeden stopień swobody oznacza znakomite dopasowanie;
entropia jest maksymalna dla rozkładu równomiernego ($1$ bit) i maleje, gdy jeden
wynik staje się bardziej prawdopodobny.

## Z-03.8 [★]

**(a)** Losujemy $N$ punktów $(x_i,y_i)$ jednostajnie z kwadratu $[0,1]^2$. Odsetek
punktów wewnątrz ćwiartki koła $x^2+y^2\le1$ równa się stosunkowi pól
$\pi/4$, więc $\hat\pi=4\cdot\dfrac{\text{trafienia}}{N}$. Dla $N=10^5$ (ziarno $0$)
otrzymujemy $\hat\pi\approx3{,}1446$, z błędem
$\sigma_{\hat\pi}=4\sqrt{\hat p(1-\hat p)/N}\approx0{,}0052$.

**(b)** $\bar x=3$, $\bar y=4$. Liczymy

$$\mathbb{E}XY=\tfrac{1\cdot2+2\cdot4+3\cdot5+4\cdot4+5\cdot5}{5}
=\tfrac{2+8+15+16+25}{5}=\tfrac{66}{5}=13{,}2,$$

$$\operatorname{Cov}(X,Y)=\mathbb{E}XY-\bar x\,\bar y=13{,}2-3\cdot4=1{,}2.$$

Wariancje: $\sigma_x^2=\tfrac{1+4+9+16+25}{5}-3^2=11-9=2$,
$\sigma_y^2=\tfrac{4+16+25+16+25}{5}-4^2=17{,}2-16=1{,}2$, więc

$$\rho=\frac{1{,}2}{\sqrt{2\cdot1{,}2}}=\frac{1{,}2}{\sqrt{2{,}4}}\approx0{,}7746.$$

**(c)** $|\rho|<1$ oznacza, że związki są **liniowe tylko częściowo** — punkty nie
leżą dokładnie na prostej. $\rho\approx0{,}77$ to silna, ale nie doskonała korelacja
dodatnia: większym $x$ towarzyszą przeciętnie większe $y$, z rozrzutem.

**Odpowiedź:** **(a)** $\hat\pi\approx3{,}1446$ (błąd $\approx0{,}005$); **(b)**
$\operatorname{Cov}=1{,}2$, $\rho\approx0{,}775$; **(c)** korelacja silna, lecz
nie doskonała.

*Interpretacja:* Monte Carlo „zamienia całkowanie na losowanie” i ma błąd malejący
jak $1/\sqrt N$; to ta sama metodyka, którą na finale stosuje się do symulacji
układów kwantowych. Współczynnik $\rho$ jest niezmienniczy na jednostki, dlatego
nadaje się do porównywania zależności między różnymi wielkościami fizycznymi.
