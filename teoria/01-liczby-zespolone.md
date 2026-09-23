# 01. Liczby zespolone

> **Warsztat źródłowy:** „Liczby zespolone” (Tomasz Sowiński).
> **Czas nauki:** ~4 h teorii + ~3 h zadań.
> **Wymagana wiedza wstępna:** algebra i trygonometria ze szkoły ponadpodstawowej;
> podstawy Pythona z numpy ([konwencje](../docs/03-konwencje-i-notacja.md)).

## 1. Po co to jest

W mechanice kwantowej stan układu opisuje wektor, którego współrzędne są **liczbami
zespolonymi** — tzw. amplitudami. Reguła Borna mówi, że prawdopodobieństwo wyniku to
kwadrat modułu amplitudy, więc moduł, sprzężenie i faza liczby zespolonej to nie
ozdobniki, a podstawowe narzędzia obliczeniowe. Bez nich nie policzysz nawet
prawdopodobieństwa w zadaniu P2 (polaryzatory i pojedynczy foton) ani amplitudy
przejścia w zadaniu P1 (cząstka w studni potencjału).

Ten warsztat odpowiada na trzy pytania, wracające w każdym kolejnym rozdziale:

1. **jak dodawać, mnożyć i dzielić** liczby zespolone (algebra);
2. **jak je zapisać** w postaci biegunowej $z=\lvert z\rvert e^{i\varphi}$
   (trygonometria, wzór Eulera);
3. **co to jest faza** i dlaczego mnożenie przez $e^{i\varphi}$ nie zmienia
   prawdopodobieństw, a mimo to ma sens fizyczny (interferencja).

Ostatnia część wprowadza zespolone wektory i macierze oraz **unitarność** — pomost
do rozdziału [02](02-algebra-liniowa.md), gdzie te pojęcia stają się językiem bramek
kwantowych. Cały materiał staramy się od razu sprawdzać w numpy, bo na Olimpiadzie
Etapu I wolno używać narzędzi obliczeniowych (patrz [zakres](../docs/02-zakres-materialu.md)).

## 2. Najważniejsze definicje

- **Jednostka urojona** $i$: liczba spełniająca $i^2=-1$.
- **Liczba zespolona**: $z=a+bi$, gdzie $a,b\in\mathbb{R}$. $a=\operatorname{Re}z$
  (część rzeczywista), $b=\operatorname{Im}z$ (część urojona).
- **Sprzężenie** (*complex conjugate*): $z^*=a-bi$. W kodzie `z.conjugate()`.
- **Moduł** (*modulus*): $\lvert z\rvert=\sqrt{a^2+b^2}=\sqrt{z^*z}$.
- **Postać biegunowa**: $z=\lvert z\rvert(\cos\varphi+i\sin\varphi)=\lvert z\rvert e^{i\varphi}$,
  gdzie $\varphi=\arg z$ to **argument** (faza), wyznaczony z dokładnością do $2\pi$.
- **Wzór Eulera**: $e^{i\varphi}=\cos\varphi+i\sin\varphi$.
- **Wartość sprzężona modułu**: $z^*z=\lvert z\rvert^2$.
- **Norma wektora zespolonego** $\lvert\psi\rangle=(c_1,\dots,c_n)$:
  $\lVert\psi\rVert=\sqrt{\sum_k\lvert c_k\rvert^2}$; stan fizyczny ma $\lVert\psi\rVert=1$.
- **Macierz unitarna** (*unitary*): $U^\dagger U=I$, gdzie $U^\dagger=(U^*)^T$
  (sprzężenie po elementach + transpozycja).

## 3. Teoria krok po kroku

### 3.1 Algebra: dodawanie i mnożenie

Liczby zespolone dodajemy i mnożemy tak jak wielomiany zmiennej $i$, pamiętając
tylko o regule $i^2=-1$:

$$(a+bi)+(c+di)=(a+c)+(b+d)i,$$
$$(a+bi)(c+di)=(ac-bd)+(ad+bc)i.$$

Ostatni wzór bierze się z rozdzielności: $ac+adi+bci+bdi^2=(ac-bd)+(ad+bc)i$.

**Dzielenie** sprowadzamy do mnożenia przez sprzężenie mianownika:

$$\frac{a+bi}{c+di}=\frac{(a+bi)(c-di)}{c^2+d^2}
=\frac{ac+bd}{c^2+d^2}+\frac{bc-ad}{c^2+d^2}\,i.$$

Mnożymy licznik i mianownik przez $c-di$, bo $c^2+d^2$ jest rzeczywiste — to ta sama
sztuczka, co „usuwanie niewymierności” z mianownika.

### 3.2 Sprzężenie i moduł

Zachodzą użyteczne tożsamości (wszystkie wynikają bezpośrednio z definicji):

$$z+z^*=2a,\qquad z-z^*=2bi,\qquad zz^*=\lvert z\rvert^2,$$
$$(z_1z_2)^*=z_1^*z_2^*,\qquad (z_1+z_2)^*=z_1^*+z_2^*,\qquad
\left\lvert z_1z_2\right\rvert=\lvert z_1\rvert\lvert z_2\rvert.$$

Sprzężenie „odbija” liczbę względem osi rzeczywistej, a moduł to jej odległość od zera.

### 3.3 Postać biegunowa i wzór Eulera

Każdą liczbę $z\neq0$ można zapisać jako $z=\lvert z\rvert e^{i\varphi}$. Wynika to z
utożsamienia płaszczyzny zespolonej z płaszczyzną $(a,b)$ i zapisu punktu we
współrzędnych biegunowych: $a=r\cos\varphi$, $b=r\sin\varphi$, $r=\lvert z\rvert$.
Wzór Eulera $e^{i\varphi}=\cos\varphi+i\sin\varphi$ łączy oba opisy.

Szczególne przypadki, które trzeba znać na pamięć:

$$e^{i0}=1,\qquad e^{i\pi/2}=i,\qquad e^{i\pi}=-1,\qquad e^{i3\pi/2}=-i.$$

Równość $e^{i\pi}+1=0$ (tożsamość Eulera) wiąże pięć podstawowych stałych. Mnożenie
w postaci biegunowej jest proste: **moduły się mnożą, a fazy dodają**,

$$z_1z_2=\lvert z_1\rvert\lvert z_2\rvert\,e^{i(\varphi_1+\varphi_2)}.$$

W szczególności $e^{i\alpha}e^{i\beta}=e^{i(\alpha+\beta)}$ — to źródło wszystkich
zjawisk interferencyjnych.

### 3.4 Wzór de Moivre'a

Podnosząc $e^{i\varphi}=\cos\varphi+i\sin\varphi$ do potęgi $n$ i porównując obie
strony, dostajemy **wzór de Moivre'a**:

$$\bigl(\cos\varphi+i\sin\varphi\bigr)^n=\cos(n\varphi)+i\sin(n\varphi).$$

Wygodniej używać go w wersji $(e^{i\varphi})^n=e^{in\varphi}$: potęgowanie liczby
zespolonej to potęgowanie modułu i **mnożenie kąta przez $n$**. Dlatego np.
$(1+i)^8$ liczymy w jednym kroku, bez ośmiokrotnego mnożenia nawiasów.

### 3.5 Pierwiastki $n$-tego stopnia

Pierwiastkiem $n$-tego stopnia z $z=\lvert z\rvert e^{i\varphi}$ jest każda z $n$
liczb

$$w_k=\lvert z\rvert^{1/n}\exp\!\left(i\,\frac{\varphi+2\pi k}{n}\right),\qquad k=0,1,\dots,n-1.$$

„$+2\pi k$” jest istotne: kąt $\varphi$ jest określony tylko modulo $2\pi$, więc ten sam
$z$ ma $n$ różnych pierwiastków, leżących na okręgu o promieniu $\lvert z\rvert^{1/n}$,
w wierzchołkach foremnego $n$-kąta. Pierwiastki $n$-tego stopnia z jedynki to
$1,\omega,\omega^2,\dots,\omega^{n-1}$ z $\omega=e^{2\pi i/n}$.

### 3.6 Równania zespolone

W równaniach z $z$ rozdzielamy części rzeczywiste i urojone (dw równania na dwie
niewiadome $a,b$) **albo** przechodzimy do postaci biegunowej, gdy równanie jest
„potęgowe” (typu $z^n=c$). Metody pomocnicze:

- porównywanie modułów i argumentów: $z_1=z_2\Leftrightarrow \lvert z_1\rvert=\lvert z_2\rvert$ i $\arg z_1=\arg z_2\ (\mathrm{mod}\,2\pi)$;
- korzystanie ze sprzężenia: jeśli $z+\bar z$ i $z\bar z$ są rzeczywiste, to...
- podstawienie $z=a+bi$ i przyrównanie współczynników przy $1$ i $i$.

### 3.7 Nierówność trójkąta

Dla modułu zachodzi **nierówność trójkąta**:

$$\bigl\lvert z_1+z_2\bigr\rvert\le \lvert z_1\rvert+\lvert z_2\rvert,$$

z równością wtedy i tylko wtedy, gdy $z_1$ i $z_2$ mają ten sam argument (są
„współliniowe” na płaszczyźnie). Interpretacja geometryczna: najkrótsza droga z $0$
do $z_1+z_2$ to odcinek, a nie łamana przez $z_1$ i $z_2$. Wersja różnicowa to
$\lvert\lvert z_1\rvert-\lvert z_2\rvert\rvert\le\lvert z_1-z_2\rvert$.

W fizyce nierówność trójkąta rządzi **interferencją**: amplitudy dodają się
wektorowo, więc $\lvert c_1+c_2\rvert$ może być mniejsze, większe albo równe
$\lvert c_1\rvert+\lvert c_2\rvert$ — to właśnie wzmocnienie i wygaszanie.

### 3.8 $e^{i\varphi}$ jako faza amplitudy kwantowej

Stan kubitu zapisujemy jako superpozycję bazy:

$$\lvert\psi\rangle=c_0\lvert 0\rangle+c_1\lvert 1\rangle,\qquad
c_0,c_1\in\mathbb{C},\qquad \lvert c_0\rvert^2+\lvert c_1\rvert^2=1.$$

**Warunek normalizacji** gwarantuje, że prawdopodobieństwa sumują się do jedynki.
Sprzężenie $c^*$ pojawia się tam, gdzie „wracamy” od amplitudy do prawdopodobieństwa
(reguła Borna $P=\lvert c\rvert^2=c^*c$).

Faza ma dwie role:

1. **Faza globalna** $e^{i\gamma}$ mnożona przez cały stan nie zmienia żadnego
   prawdopodobieństwa: $\lvert e^{i\gamma}c_k\rvert^2=\lvert c_k\rvert^2$. Stan
   $\lvert\psi\rangle$ i $e^{i\gamma}\lvert\psi\rangle$ opisują **ten sam** układ
   fizyczny.
2. **Faza względna** między współczynnikami (np. w $c_0+c_1$) zmienia wynik
   interferencji i jest obserwowalna. Przykład: stany $\frac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)$
   oraz $\frac{1}{\sqrt2}(\lvert0\rangle-\lvert1\rangle)$ dają te same
   prawdopodobieństwa w pomiarze w bazie $\{\lvert0\rangle,\lvert1\rangle\}$
   ($P=1/2$ każdy), ale różnią się w bazie $\{\lvert\pm\rangle\}$.

Po pomiarze rzutowym w bazie $\{\lvert k\rangle\}$ stan „zapada się” do $\lvert k\rangle$
z prawdopodobieństwem $\lvert c_k\rvert^2$.

### 3.9 Zespolone wektory, macierze i unitarność (wstęp)

Wektory stanu i operatory na $\mathbb{C}^2$ zapisujemy jako kolumny i macierze:

$$\lvert 0\rangle=\begin{pmatrix}1\\0\end{pmatrix},\quad
\lvert 1\rangle=\begin{pmatrix}0\\1\end{pmatrix},\quad
\lvert\psi\rangle=\begin{pmatrix}c_0\\c_1\end{pmatrix},\quad
\langle\psi\rvert=(c_0^*\;\;c_1^*).$$

**Iloczyn skalarny** dwóch stanów to $\langle\phi\rvert\psi\rangle=\sum_k\phi_k^*\psi_k$ —
liczba zespolona. **Norma** $\lVert\psi\rVert=\sqrt{\langle\psi\rvert\psi\rangle}$.
Sprzężenie hermitowskie macierzy $M^\dagger=(M^*)^T$ uogólnia sprzężenie liczby.

**Macierz unitarna** spełnia $U^\dagger U=UU^\dagger=I$. Mnożenie przez nią zachowuje
normę (a więc i prawdopodobieństwa): $\lVert U\psi\rVert^2=\psi^\dagger U^\dagger U\psi=\lVert\psi\rVert^2$.
Dlatego każda ewolucja kwantowa (bramka, upływ czasu) jest unitarna. To główny motyw
rozdziału [02](02-algebra-liniowa.md).

### 3.10 Zapis w numpy

```python
import numpy as np
z = 3 + 4j                 # liczba zespolona
z.real, z.imag, z.conjugate(), abs(z)
np.exp(1j*np.pi)           # e^{i pi} = -1 + 1.2e-16j  (bliskie zeru)
np.sqrt(1j)                # pierwiastek (0.7071+0.7071j)
np.roots([1,0,0,-1])       # pierwiastki z^3 = 1
np.linalg.norm?            # tolerancja: porownuj z 1 zamiast == 1
```

W numpy jednostka urojona to `1j` (litera `j`). Sprzężenie to metoda `.conjugate()`
lub skrót `.conj()`; dla macierzy sprzężenie hermitowskie to `M.conj().T`. **Uwaga
praktyczna:** wyniki zmiennoprzecinkowe porównuj z tolerancją (`np.allclose`), bo
$e^{i\pi}$ wyjdzie jako $-1+1{,}2\cdot10^{-16}i$, a nie jako dokładne $-1$.

## 4. Przykłady rozwiązane

### Przykład 1 (łatwy): działania, moduł i faza

**Dane:** $z_1=3+4i$, $z_2=1-2i$.

**Metoda:** mnożenie wielomianowe z $i^2=-1$; moduł ze wzoru $\lvert z\rvert=\sqrt{a^2+b^2}$;
argument z $\tan\varphi=b/a$ z uwzględnieniem ćwiartki.

**Rachunek:**

$$z_1z_2=(3+4i)(1-2i)=3-6i+4i-8i^2=3-2i+8=11-2i.$$

$$\lvert z_1\rvert=\sqrt{3^2+4^2}=\sqrt{25}=5,\qquad
\lvert z_1z_2\rvert=\lvert 11-2i\rvert=\sqrt{121+4}=\sqrt{125}\approx11{,}2.$$

Sprawdzamy zgodność: $\lvert z_1\rvert\lvert z_2\rvert=5\cdot\sqrt{5}=5\sqrt5=\sqrt{125}$ ✓
(argument: $z_1$ w I ćwiartce, $\varphi_1=\arctan(4/3)\approx53{,}1^\circ$).

**Wynik:** $z_1z_2=11-2i$, $\lvert z_1\rvert=5$, $\lvert z_1z_2\rvert\approx11{,}2$.

**Interpretacja:** moduł iloczynu równa się iloczynowi modułów — sprzężenie i moduł
„rozprzęgają” się od fazy, co pozwala liczyć prawdopodobieństwa osobno od interferencji.

### Przykład 2 (trudniejszy): pierwiastek i faza amplitudy

**Dane:** liczby $z^4=-1$; oraz stan $\lvert\psi\rangle=(1+i)\lvert 0\rangle+(1-i)\lvert 1\rangle$.

**(a) Pierwiastki.** Zapisujemy $-1=e^{i\pi}=e^{i(\pi+2\pi k)}$, więc
$z=\exp\!\bigl(i\frac{\pi+2\pi k}{4}\bigr)$ dla $k=0,1,2,3$:

$$z_k=\exp\!\left(i\left(\tfrac{\pi}{4}+\tfrac{k\pi}{2}\right)\right)
=\tfrac{1}{\sqrt2}(\pm1\pm i).$$

Numerycznie: $z_0=\tfrac{1+i}{\sqrt2}$, $z_1=\tfrac{-1+i}{\sqrt2}$,
$z_2=\tfrac{-1-i}{\sqrt2}$, $z_3=\tfrac{1-i}{\sqrt2}$ (numpy: `np.roots([1,0,0,0,1])`
daje $0{,}7071\pm0{,}7071i$ i $-0{,}7071\pm0{,}7071i$) ✓.

**(b) Normalizacja i fazy.** Liczymy $\lvert 1+i\rvert^2=2$, $\lvert 1-i\rvert^2=2$, razem $4$.
Stan znormalizowany:

$$\lvert\psi\rangle=\tfrac{1+i}{2}\lvert 0\rangle+\tfrac{1-i}{2}\lvert 1\rangle.$$

Prawdopodobieństwa: $P(0)=\lvert(1+i)/2\rvert^2=1/2$, $P(1)=1/2$. Faza względna

$$\frac{c_1}{c_0}=\frac{1-i}{1+i}=\frac{(1-i)^2}{(1+i)(1-i)}=\frac{-2i}{2}=-i=e^{-i\pi/2}.$$

**Wynik:** pierwiastki $z_k=\tfrac{1}{\sqrt2}(\pm1\pm i)$; stan
$\tfrac{1+i}{2}\lvert0\rangle+\tfrac{1-i}{2}\lvert1\rangle$ z fazą względną $-i=e^{-i\pi/2}$.

**Interpretacja:** pomiar w bazie $\{\lvert0\rangle,\lvert1\rangle\}$ da wynik losowy
$1/2$–$1/2$, niezależnie od fazy; tę fazę ujawni dopiero pomiar w innej bazie (np.
$\lvert\pm\rangle$), bo tam wchodzi $1\pm 2\operatorname{Re}$ członu interferencyjnego.

### Przykład 3 (trudniejszy): równanie $z^2=3-4i$ i nierówność trójkąta

**Dane:** rozwiązać $z^2=3-4i$; dla $\lvert z_1\rvert=3$, $\lvert z_2\rvert=4$ oszacować
$\lvert z_1+z_2\rvert$.

**Metoda:** podstawienie $z=a+bi$ i przyrównanie części rzeczywistej i urojonej;
przy oszacowaniu — nierówność trójkąta.

**Rachunek:** $(a+bi)^2=(a^2-b^2)+2ab\,i=3-4i$, więc
$$a^2-b^2=3,\qquad 2ab=-4\ \Rightarrow\ ab=-2.$$
Z drugiego $b=-2/a$; po podstawieniu $a^2-4/a^2=3$, czyli $(a^2-4)(a^2+1)=0$.
Rzeczywiste $a^2=4\Rightarrow a=\pm2$, $b=\mp1$. Zatem $z=\pm(2-i)$
(sprawdzamy: $(2-i)^2=4-4i+i^2=3-4i$ ✓).

Dla szacowania: $\lvert\lvert z_1\rvert-\lvert z_2\rvert\rvert\le\lvert z_1+z_2\rvert
\le\lvert z_1\rvert+\lvert z_2\rvert$, czyli $1\le\lvert z_1+z_2\rvert\le7$.

**Wynik:** $z=\pm(2-i)$; oraz $1\le\lvert z_1+z_2\rvert\le7$.

**Interpretacja:** pierwiastki kwadratowe są zawsze dwa i różnią się znakiem — to
następstwo tego, że na płaszczyźnie zespolonej „połówka kąta” ma dwie wartości.
Nierówność trójkąta mówi, że sumę amplitud ogranicza suma ich modułów.

## 5. Typowe pułapki

1. **Mylenie $i$ z $-i$ w mianowniku.** Dzieląc przez $c+di$ mnożymy przez
   **sprzężenie** $c-di$, nie przez $-c-di$.
2. **Zapominanie $+2\pi k$** w pierwiastkach — prowadzi do znalezienia tylko jednego
   z $n$ pierwiastków.
3. **Traktowanie fazy jako nieistotnej.** Faza globalna istotna nie jest, ale **faza
   względna** wpływa na interferencję i na wyniki pomiarów w innych bazach.
4. **Porównywanie liczb zmiennoprzecinkowych znakiem `==`.** $e^{i\pi}$ nie wyjdzie
   równo $-1$; zawsze `np.allclose` z tolerancją.
5. **Złe określenie argumentu.** $\arctan(b/a)$ daje kąt w $(-\pi/2,\pi/2)$; dla
   II i III ćwiartki trzeba dodać $\pi$. Sprawdź znak, wybierając poprawną ćwiartkę.
6. **Zapominanie o normalizacji.** Amplitudy $(1+i)$ i $(1-i)$ **nie** są stanem
   fizycznym — trzeba je podzielić przez normę, zanim policzysz prawdopodobieństwa.

## 6. Zadania (Z-01)

**Z-01.1.** Dane są $z_1=2-3i$, $z_2=1+5i$. Oblicz
(a) $z_1+z_2$, (b) $z_1z_2$, (c) $\dfrac{z_1}{z_2}$.

**Z-01.2.** Dla $z=-1+\sqrt3\,i$ oraz $w=-2i$
(a) policz $\lvert z\rvert,\lvert w\rvert$; (b) zapisz je w postaci biegunowej;
(c) policz $w^8$ i podaj wynik.

**Z-01.3.** (a) Oblicz $(\sqrt3+i)^6$ wzorem de Moivre'a.
(b) Rozwiąż $z^3=8i$. (c) Sprawdź, że suma trzech pierwiastków z (b) jest zerem,
i wyjaśnij, dlaczego tak musi być.

**Z-01.4.** Rozwiąż równanie $z^2=3-4i$.
(a) metodą podstawienia $z=a+bi$; (b) sprawdź oba pierwiastki, wyliczając moduł;
(c) zapisz oba pierwiastki w postaci biegunowej.

**Z-01.5.** (a) Opisz słownie zbiór punktów $\lvert z-1\rvert=2$.
(b) Opisz zbiór $\lvert z-i\rvert<1$. (c) Dla $\lvert z_1\rvert=3$,
$\lvert z_2\rvert=4$ podaj ograniczenia $\lvert z_1+z_2\rvert$ i wskaż, kiedy
przyjmuje wartość najmniejszą.

**Z-01.6.** Stan zapisano jako $\lvert\psi\rangle=(2+i)\lvert0\rangle+(1-2i)\lvert1\rangle$.
(a) Znormalizuj go. (b) Podaj prawdopodobieństwa pomiaru $0$ i $1$.
(c) Wyznacz fazę względną $c_1/c_0$ i przedstaw ją jako $e^{i\varphi}$.

**Z-01.7.** Dana jest macierz
$U=\dfrac{1}{\sqrt2}\begin{pmatrix}1&i\\ i&1\end{pmatrix}$.
(a) Wykaż rachunkiem, że $U$ jest unitarna. (b) Wyznacz jej wartości własne.
(c) Wskaż wektory własne i sprawdź, że są to $\lvert\pm\rangle$.

**Z-01.8. [★]** (a) Wykaż, że suma wszystkich $n$-tych pierwiastków z jedynki jest
zerem. (b) Ile wynosi ich iloczyn? (c) Potwierdź wynik dla $n=5$ numerycznie w numpy.

## 7. Wskazówki do zadań

- **Z-01.1.** Mnożenie i dzielenie — jak w Przykładzie 1; w (c) mnóż licznik i
  mianownik przez $1-5i$.
- **Z-01.2.** (a)–(b) wzór $\lvert z\rvert=\sqrt{a^2+b^2}$ i dobranie ćwiartki;
  (c) skorzystaj z $w=\lvert w\rvert e^{i\varphi}$ i de Moivre'a.
- **Z-01.3.** (a) zapisz $\sqrt3+i$ w postaci biegunowej; (b) $8i=8e^{i\pi/2}$;
  (c) popatrz na współczynnik przy $z^2$ w wielomianie $z^3-8i$.
- **Z-01.4.** Układ $a^2-b^2=3$, $2ab=-4$; rozwiąż jak w Przykładzie 3.
- **Z-01.5.** (a)–(b) przypomnij sobie równanie okręgu i koła na płaszczyźnie;
  (c) nierówność trójkąta i jej wersja różnicowa.
- **Z-01.6.** Policz $\lvert2+i\rvert^2+\lvert1-2i\rvert^2$; do fazy użyj
  $\frac{c_1}{c_0}=\frac{(1-2i)(2-i)}{(2+i)(2-i)}$.
- **Z-01.7.** (a) policz $U^\dagger U$; (b) skorzystaj ze śladu i wyznacznika
  ($\det U=1$, $\operatorname{Tr}U=\sqrt2$); (c) podstaw $\lvert\pm\rangle$.
- **Z-01.8.** [★] Ze wzoru na sumę ciągu geometrycznego dla $\omega\ne1$;
  iloczyn — z twierdzenia Viète'a dla $z^n-1=0$.

## 8. Co dalej

Liczby zespolone stają się językiem wektorów i operatorów w rozdziale
[02. Algebra liniowa](02-algebra-liniowa.md) — tam zobaczysz macierze Pauliego,
unitarność i sferę Blocha. Fazę amplitudy wykorzystasz w rozdziale
[05. Podstawy mechaniki kwantowej](05-podstawy-mechaniki-kwantowej.md) przy prawie
Malusa (zadanie P2) i przy superpozycjach stanów stacjonarnych (zadanie P1).
Gdy będziesz gotowy, rozwiąż zadania i porównaj z
[rozwiązaniami](../zadania/rozwiazania/rozwiazania-01.md); praca domowa łącząca
rozdziały 01–05 to [PD-1](../praca-domowa/praca-domowa-01.md).

**Bibliografia.** Zasady i notacja: [konwencje](../docs/03-konwencje-i-notacja.md);
zakres i terminy: [zakres materiału](../docs/02-zakres-materialu.md). Pozycje
książkowe — patrz wykaz literatury w `docs/bibliografia.md`.
