# 16. Analiza danych i obliczenia naukowe


## 1. Zakres rozdziału

Rozdział obejmuje narzędzia warsztatu „Analiza danych i obliczenia naukowe”: **NumPy** (tablice,
wektoryzacja, wydajność), **pandas** (arkusz danych w kodzie), **matplotlib** (wykres jako element
odpowiedzi), podstawy **dopasowania modelu** (LSM, macierz Vandermonde’a, $\chi^2$, $R^2$),
**propagację niepewności**, **bootstrap**, wykrywanie punktów odstających oraz **transformatę
Fouriera** (FFT, widmo, alias, okna, filtry).

Druga grupa zagadnień dotyczy **reprodukowalności** (*reproducibility*): raport odtwarzalny z
trzech elementów — **kod + dane + opis** — z ustalonym **ziarnem** (*seed*) i przykładami
uruchamianymi bez SciPy (SciPy pokazywane jako opcja).

Materiał rozwija estymację, rozkłady i $\chi^2$ z
[rozdziału 03](03-rachunek-prawdopodobienstwa-i-statystyka.md) oraz niepewność malejącą jak
$1/\sqrt N$ z [rozdziału 11](11-metrologia-kwantowa.md); niepewności są tu wyznaczane z
konkretnych danych. Analiza danych wraca jako narzędzie w
[rozdziale 12](12-realizacje-komputerow-kwantowych.md) (benchmarki, czasy $T_1/T_2$) i
[rozdziale 13](13-korekcja-i-mitygacja-bledow.md) (krzywe wierności bramek).

## 2. Najważniejsze definicje

- **Tablice (ndarray)**: blok liczb NumPy z jednym `dtype` i kształtem (`shape`); operacje są **wektoryzowane**.
- **Wektoryzacja / broadcasting**: zastąpienie pętli `for` operacją na tablicy; broadcasting rozciąga wymiary o rozmiarze 1, np. `(3,1)+(1,4)->(3,4)`.
- **DataFrame (pandas)**: tabela z nazwanymi kolumnami — odpowiednik arkusza kalkulacyjnego w kodzie.
- **Niepewność standardowa $u$**: oszacowanie odchylenia standardowego pomiaru; zapis $x=\bar x\pm u$.
- **Metoda najmniejszych kwadratów (LSM)**: minimalizacja $\chi^2=\sum_i((y_i-f(x_i))/\sigma_i)^2$.
- **Macierz Vandermonde’a** $V_{ik}=x_i^k$; rozwiązanie ważone $\hat\beta=(V^{\mathsf T}WV)^{-1}V^{\mathsf T}Wy$, $W=\mathrm{diag}(1/\sigma_i^2)$.
- **$\chi^2/\mathrm{ndof}$** (zredukowany $\chi^2$): miara zgodności modelu z danymi; $\approx1$ = dobrze.
- **Reszta** $r_i=y_i-f(x_i)$; **$R^2$** = ułamek wariancji wyjaśniony przez model.
- **Propagacja niepewności**: $u_z^2=\sum_j(\partial f/\partial x_j)^2u_{x_j}^2$ (dla niezależnych $x_j$).
- **Bootstrap**: rozkład estymatora z **próbkowania z powtórzeniami**; **przedział ufności (CI)** 68% $\approx\bar x\pm u$.
- **Punkt odstający (outlier)**: obserwacja niezgodna z resztą zbioru; wykrywanie regułą $3\sigma$ albo **MAD**.
- **Transformata Fouriera (DFT/FFT)**: rozkład sygnału na częstości; **widmo** $|X_k|^2$; **Nyquist** $f_N=f_s/2$.
- **Aliasing**: fałszywa częstość $|f_0-f_s|$ dla $f_0>f_N$.
- **Okno (window)**: wygładza końce sygnału przed FFT (np. Hanna), zmniejsza przeciek widma.
- **Filtr dolnoprzepustowy**: usuwa wysokie częstości; najprostszy to **średnia ruchoma** (*moving average*).
- **Szum $1/f$** (różowy): gęstość widmowa mocy $\propto1/f$; „pamięć” długozasięgowa, trudny do filtrowania.
- **Ziarno (seed)**: liczba startowa generatora pseudolosowego; ten sam seed $\Rightarrow$ te same losowania.
- **Zapis wyniku**: $x\pm u$ z tą samą liczbą miejsc po przecinku i niepewnością zaokrągloną do 1–2 cyfr znaczących.

## 3. Teoria krok po kroku

### 3.1 NumPy: tablice, wektoryzacja, broadcasting

Tablice tworzymy przez `np.array`, `np.arange`, `np.linspace`, `np.zeros`, `np.ones`.
Kształt i typ sprawdzamy przez `arr.shape`, `arr.dtype`. Kluczowa jest **wektoryzacja**:
```python
import numpy as np
t = np.linspace(0.0, 1.0, 5)        # 5 punktow, bez petli
y = np.sin(2 * np.pi * t)           # dziala na calej tablicy naraz
```
**Broadcasting** pozwala łączyć tablice różnych kształtów, gdy wymiary są zgodne „od prawej”
(1 oznacza rozciągnięcie):
```python
a = np.array([[1.0], [2.0], [3.0]])   # (3,1)
b = np.array([[0.0, 10.0, 20.0, 30.0]])  # (1,4)
c = a + b                             # (3,4)
```
Wydajność: dla $N=10^6$ pętla w Pythonie wykonuje $\sim10^6$ iteracji, a jedna operacja
NumPy działa w kodzie skompilowanym — praktycznie **setki razy szybciej**. Reguła: pisz
operacje na całych tablicach, a `for` rezerwuj do kroków algorytmu, nie do elementów.

### 3.2 Wczytywanie i zapis danych

Najprostszy format to plik tekstowy z kolumnami. NumPy czyta go bezpośrednio:
```python
data = np.loadtxt("pomiary.txt")          # cala tablica
t, y = np.loadtxt("pomiary.txt", unpack=True, usecols=(0, 1))
np.savetxt("wynik.txt", out, fmt="%.6f")  # zapis
```
Pliki CSV z nagłówkiem wygodniej czytać w pandas:
```python
import pandas as pd
df = pd.read_csv("pomiary.csv")           # kolumny = nazwy z naglowka
df = pd.read_csv("pomiary.csv", comment="#", sep=";")  # separator, komentarze
```
Zasada: **nigdy nie wpisuj danych do kodu na sztywno** — trzymaj je w pliku obok skryptu.
Dzięki temu ten sam skrypt powtórzy analizę na nowych danych.

### 3.3 pandas: filtrowanie, grupowanie, łączenie

DataFrame to tabela; operujemy na kolumnach jak na tablicach, ale z nazwami:
```python
df["y"]                       # kolumna
df[df["y"] > 5.0]             # filtrowanie warunkiem
df.groupby("seria")["y"].mean()   # srednia w grupach
df["z"] = df["x"] ** 2        # nowa kolumna
pd.merge(df1, df2, on="t")    # laczenie po wspolnej kolumnie
```
`groupby` to odpowiednik tabeli przestawnej: pozwala policzyć statystyki osobno dla każdego
eksperymentu/serii, co jest niezbędne przy porównywaniu warunków (np. pomiar z filtrem i bez).

### 3.4 matplotlib: wykres jako część odpowiedzi

Wykres to argument merytoryczny. Ustawiamy **podpisy osi z jednostkami**, tytuł i legendę:
```python
import matplotlib
matplotlib.use("Agg")                 # bez okna - zapis do pliku
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.errorbar(t, y, yerr=u, fmt="o", label="dane")
ax.plot(t, model, "-", label="model")
ax.set_xlabel("t [s]"); ax.set_ylabel("sygnal [V]")
ax.legend(); fig.savefig("wykres.png", dpi=150)
```
Typy wykresów: **liniowy** `plot` (zależność ciągła), **słupkowy** `bar` (porównanie kategorii),
**histogram** `hist` (rozkład zliczeń), **z błędami** `errorbar` (dane pomiarowe). W kodzie
traktuj matplotlib jako **opcjonalny** (`try: import ... except ImportError`), żeby skrypt
działał także bez niego.

### 3.5 Dopasowanie modelu

Dla modelu liniowego w parametrach — np. $y=a x+b$ albo $y=a_0+a_1x+a_2x^2$ — używamy
`np.polyfit(x, y, stopien)` (metoda najmniejszych kwadratów). Dla wag (różne niepewności)
budujemy **macierz Vandermonde’a** i rozwiązujemy układ normalny:

$$W=\mathrm{diag}(1/\sigma_i^2),\qquad \hat\beta=(V^{\mathsf T}W V)^{-1}V^{\mathsf T}W\,y,\qquad
\mathrm{Cov}(\hat\beta)=(V^{\mathsf T}W V)^{-1}.$$

Pierwiastek z przekątnej $\mathrm{Cov}$ to niepewność parametru. Dla modeli **nieliniowych**
(np. $y=Ae^{-t/T_2}$) trzy drogi: (i) linearyzacja przez logarytm i `polyfit`, (ii) własna
minimalizacja $\chi^2$, (iii) `scipy.optimize.curve_fit` (opcjonalnie — patrz [bibliografia](../docs/bibliografia.md)).

### 3.6 Ocena dopasowania: $\chi^2$, reszty, $R^2$

Trzy liczby odpowiadają na trzy różne pytania:

$$\chi^2=\sum_i\frac{(y_i-f(x_i))^2}{\sigma_i^2},\qquad
\chi^2_{\rm red}=\frac{\chi^2}{\mathrm{ndof}},\qquad
R^2=1-\frac{\sum_i r_i^2}{\sum_i (y_i-\bar y)^2}.$$

$\mathrm{ndof}=N-p$ ($p$ = liczba parametrów). **$\chi^2_{\rm red}\approx1$** → model zgodny z
danymi *i* niepewności są realistyczne; $\gg1$ → zły model lub zaniżone $\sigma_i$;
$\ll1$ → zawyżone $\sigma_i$. $R^2$ bliskie 1 mówi tylko, że model „idzie za” trendem — nie
weryfikuje niepewności. Dlatego zawsze raportujemy razem $\chi^2_{\rm red}$ i $R^2$.

### 3.7 Propagacja niepewności

Gdy wynik $z$ liczymy z kilku zmierzonych wielkości, niepewności się **propagują**. Dla
niezależnych zmiennych:

$$u_z^2=\sum_j\Big(\frac{\partial f}{\partial x_j}\Big)^2 u_{x_j}^2 .$$

Jeśli parametry dopasowania są skorelowane (niezerowe pozadiagonalne
elementy $\mathrm{Cov}$), trzeba użyć pełnej formy $u_z^2=\vec g^{\mathsf T}\mathrm{Cov}\,\vec g$,
gdzie $g_j=\partial f/\partial x_j$. Gdy wzór jest skomplikowany, wygodna jest **propagacja
Monte Carlo**: losujemy $\vec x$ z rozkładu $\mathcal N(\hat{\vec x},\mathrm{Cov})$, liczymy $z$
wiele razy i bierzemy odchylenie standardowe wyników.

### 3.8 Bootstrap i przedziały ufności

Bootstrap nie zakłada rozkładu normalnego: z $N$ danych losujemy **z powtórzeniami** $N$
punktów, powtarzamy dopasowanie $B$ razy (typowo $B=10^3$–$10^4$) i patrzymy na rozrzut
estymatora. Przedział $68\%$ to percentyle 16 i 84 rozkładu bootstrapowego. Bootstrap jest
szczególnie przydatny, gdy rozkład estymatora jest skośny albo próbka mała.

### 3.9 Punkty odstające

Punkt odstający potrafi przesunąć dopasowanie. Reguła $3\sigma$: odrzucamy $|r_i|>3\hat\sigma$.
Odporniejszą miarą rozrzutu jest **MAD**: $\mathrm{MAD}=\mathrm{median}(|x_i-\mathrm{median}(x)|)$,
a przybliżone odchylenie $\hat\sigma\approx1{,}4826\,\mathrm{MAD}$ (odporne na odstające).
Wykryty punkt **nie odrzucamy bezmyślnie** — najpierw sprawdzamy, czy to błąd pomiaru; decyzję
zawsze opisujemy w raporcie.

### 3.10 Transformata Fouriera, okna, aliasing, filtry

Widmo liczymy przez `np.fft.rfft` (sygnał rzeczywisty) i `np.fft.rfftfreq`:
```python
X  = np.fft.rfft(signal)
f  = np.fft.rfftfreq(N, d=1.0/fs)     # d = krok czasu
peak = f[np.argmax(np.abs(X))]
```
**Rozdzielczość** widma to $\Delta f=f_s/N$. **Częstość Nyquista** $f_N=f_s/2$: składowe powyżej
$f_N$ ulegają **aliasingowi** i pojawiają się jako $|f_0-f_s|$. **Okno** (np. Hanna:
`signal * np.hanning(N)`) wygładza końce i zmniejsza przeciek, kosztem nieco szerszych pików.
Najprostszy **filtr dolnoprzepustowy** to **średnia ruchoma** (`np.convolve` z jądrem
`np.ones(k)/k`) — usuwa szybkie oscylacje, nie zmieniając wolnego trendu.

### 3.11 Szum $1/f$ i losowość

Szum **różowy** ($1/f$) ma gęstość widmową mocy $\propto1/f$, czyli więcej energii na niskich
częstościach; generujemy go, mnożąc losowe fazy przez amplitudy $\propto1/\sqrt f$. Odróżniamy
go od szumu **białego** (stała gęstość). Filtr dolnoprzepustowy *nie* usuwa szumu $1/f$ — ten
szum ma moc właśnie na niskich częstościach. Liczby losowe generujemy przez nowoczesny
generator i **stałe ziarno**:
```python
rng = np.random.default_rng(seed=123)     # powtarzalne losowania
x = rng.normal(0.0, 1.0, size=10)
```

### 3.12 Raportowanie wyniku i reprodukowalność

Niepewność zaokrąglamy do **1–2 cyfr znaczących**, a wynik do tego samego miejsca po przecinku:
poprawnie $T_2=2{,}45\pm0{,}02$ s, niepoprawnie $2{,}4528\pm0{,}0238$. Podajemy jednostkę i
liczbę pomiarów. Raport (Jupyter albo PDF) zawiera: **cel**, **dane** (skąd), **kod** (ze
ziarnem), **wynik z niepewnością**, **$\chi^2_{\rm red}$**, **wykres**, **wnioski**. Jeśli
choć jednego elementu brakuje, wyniku nie da się odtworzyć.

## 4. Przykłady rozwiązane

### Przykład 16.1 (łatwy): ważone dopasowanie liniowe z $\chi^2$ i $R^2$

**Dane.** Sześć pomiarów $x_i=1,\dots,6$ z wynikami $y=(2{,}1;\ 4{,}0;\ 6{,}2;\ 7{,}9;\ 10{,}2;\ 11{,}8)$ i jednakową niepewnością $\sigma=0{,}2$.

**Metoda.** Model $y=ax+b$; macierz Vandermonde’a $V$ ($6\times2$) i rozwiązanie ważone
$\hat\beta=(V^{\mathsf T}WV)^{-1}V^{\mathsf T}Wy$.

**Rachunek.** $W=(1/0{,}04)I$, więc

$$V^{\mathsf T}WV=\frac{1}{0{,}04}\begin{pmatrix}\sum x_i^2&\sum x_i\\ \sum x_i&6\end{pmatrix}
=\begin{pmatrix}2275&525\\ 525&150\end{pmatrix},\qquad
(V^{\mathsf T}WV)^{-1}=\begin{pmatrix}0{,}002286&-0{,}008\\ -0{,}008&0{,}034667\end{pmatrix}.$$

Z $\sum x_iy_i=182{,}1$, $\sum y_i=42{,}2$ dostajemy $\hat\beta=(1{,}9657,\ 0{,}1533)$.
Niepewności to pierwiastki z przekątnej: $u_a=\sqrt{0{,}002286}=0{,}0478$,
$u_b=\sqrt{0{,}034667}=0{,}186$.
Reszty $r_i$ dają $\chi^2=\sum(r_i/0{,}2)^2=2{,}82$, $\mathrm{ndof}=4$, więc
$\chi^2_{\rm red}=0{,}70$; $R^2=1-\sum r_i^2/\sum(y_i-\bar y)^2=0{,}9983$.
Predykcja na $x=7$: $y=1{,}9657\cdot7+0{,}1533=13{,}913$, a
$u_y^2=\vec g^{\mathsf T}\mathrm{Cov}\,\vec g$ z $\vec g=(7,1)$ daje $u_y=0{,}186$.

**Odpowiedź:** $\mathbf{a=1{,}966\pm0{,}048}$, $\mathbf{b=0{,}153\pm0{,}186}$,
$\mathbf{\chi^2_{\rm red}=0{,}70}$, $\mathbf{R^2=0{,}998}$; na $x=7$:
$\mathbf{13{,}91\pm0{,}19}$.
*Interpretacja:* $\chi^2_{\rm red}$ bliskie 1 i wysokie $R^2$ — model liniowy opisuje dane
w granicach niepewności, a niepewności $\sigma=0{,}2$ są realistyczne.

### Przykład 16.2 (trudniejszy): zanik $T_2$, propagacja i bootstrap

**Dane.** $N=60$ punktów $t\in[0,8]$ s, model $y=Ae^{-t/T_2}$ z $A=0{,}98$, $T_2=2{,}5$ s,
szum gaussowski $\sigma=0{,}02$ (`seed=11`).

**Metoda.** Start z linearyzacji $\ln y=\ln A-t/T_2$ (`np.polyfit`), potem lokalna minimalizacja
$\chi^2$ (krok adaptacyjny), niepewności z numerycznego hesjanu; kontrolnie **bootstrap**
($B=200$) i **propagacja** niepewności na $y(3\,\text{s})$.

**Rachunek.** Dopasowanie daje $T_2=2{,}4528$ s, $A=0{,}9901$, $\chi^2=44{,}76$,
$\mathrm{ndof}=58$, czyli $\chi^2_{\rm red}=0{,}772$. Numeryczny hesjan daje
$u_{T_2}=0{,}0238$ s, $u_A=0{,}0065$. Propagacja na $y(3)=Ae^{-3/T_2}=0{,}2914$:

$$u_y^2=\Big(e^{-3/T_2}\Big)^2u_A^2+\Big(Ae^{-3/T_2}\tfrac{3}{T_2^2}\Big)^2u_{T_2}^2
\;\Rightarrow\; u_y=0{,}0040 .$$

Bootstrap (16.–84. percentyl) daje $T_2\in[2{,}427;\ 2{,}485]$ s, szerokość $0{,}058$ s —
zgodnie z $2u_{T_2}=0{,}048$ s.

**Odpowiedź:** $\mathbf{T_2=2{,}453\pm0{,}024}$ **s**, $\mathbf{A=0{,}990\pm0{,}007}$,
$\mathbf{\chi^2_{\rm red}=0{,}77}$; $\mathbf{y(3)=0{,}291\pm0{,}004}$.
*Interpretacja:* wartość prawdziwa $2{,}5$ s mieści się w $2u$, a przedział bootstrapowy
potwierdza niepewność bez założenia normalności.

## 5. Typowe pułapki

1. **Mylenie $s$ z $u$.** Odchylenie standardowe próbki $s$ opisuje rozrzut *pojedynczego*
   pomiaru; niepewność **średniej** to $s/\sqrt N$. Dla $N=100$ to czynnik $10$.
2. **Niepewności „po równo”.** Jeśli punkty mają różne $\sigma_i$, dopasowanie musi być
   **ważone**; niezważone `polyfit` faworyzuje punkty o dużej niepewności.
3. **Zbyt wiele cyfr.** $T_2=2{,}4528\pm0{,}0238$ s to błąd; poprawnie $2{,}45\pm0{,}02$ s.
4. **$R^2$ jako dowód poprawności.** Wysokie $R^2$ nie znaczy, że model jest właściwy ani że
   niepewności są realistyczne — zły model może mieć $R^2\approx1$ na wąskim zakresie.
5. **Mylenie $\chi^2$ z $\chi^2_{\rm red}$.** Sam $\chi^2$ rośnie z $N$; porównujemy
   $\chi^2/\mathrm{ndof}$.
6. **Brak ziarna.** Bez `seed` wyników nie da się powtórzyć; na Olimpiadzie liczy się
   reprodukowalność.
7. **Aliasing.** Próbkowanie z $f_s<2f_0$ produkuje fałszywy pik; nie da się go usunąć
   filtrem po próbkowaniu.
8. **Bezrefleksyjne odrzucanie „odstających”.** Usuwanie punktów, które psują dopasowanie,
   to fałszowanie danych; decyzję uzasadniamy (reguła $3\sigma$ / MAD + rewizja pomiaru).
9. **Szum $1/f$ i pętle.** Filtr dolnoprzepustowy zostawia moc $1/f$; pętla `for` po $10^6$ punktów
   trwa minuty tam, gdzie wektoryzowany NumPy — milisekundy.

## 6. Zadania (Z-16)

**Z-16.1.** NumPy i broadcasting.
(a) Dla `t = np.linspace(0, 1, 5)` policz `y = np.sin(2*np.pi*t)` bez pętli i podaj `y`.
(b) Wyjaśnij, jaki kształt ma `np.array([[1],[2]]) + np.array([[0,10,20]])` i ile ma elementów.
(c) Dlaczego wektoryzacja jest szybsza? Odpowiedz jakościowo (bez pomiaru czasu).

**Z-16.2.** Dane i statystyki. Plik `counts.csv` zawiera 12 zliczeń fotonów w kolejnych sekundach:
$22, 32, 24, 18, 21, 20, 30, 21, 26, 33, 23, 23$.
(a) Wczytaj kolumnę (`np.loadtxt`) i policz średnią, odchylenie standardowe i niepewność średniej.
(b) Oszacuj, czy zliczenia pochodzą z rozkładu Poissona (porównaj wariancję i średnią).
(c) Podaj wynik jako $\bar n\pm u_n$ z zaokrągleniem do 2 cyfr znaczących niepewności.

**Z-16.3.** Dopasowanie liniowe. Dane $x=(1,2,3,4,5,6)$,
$y=(2{,}1;4{,}0;6{,}2;7{,}9;10{,}2;11{,}8)$, $\sigma_i=0{,}2$.
(a) Zbuduj macierz Vandermonde’a i wyznacz ważone $a,b$.
(b) Policz $\chi^2_{\rm red}$ i $R^2$; oceń jakość modelu.
(c) Podaj predykcję $y(7)$ wraz z niepewnością.

**Z-16.4.** Propagacja niepewności. $y=Ae^{-t/T_2}$ z $A=0{,}99\pm0{,}01$,
$T_2=2{,}5\pm0{,}05$ s, $t=3$ s.
(a) Policz $y$ i $u_y$ z ogólnego wzoru na propagację.
(b) Powtórz metodą Monte Carlo ($10^4$ próbek, ziarno ustalone) i porównaj.
(c) Czy niepewność **względna** $y$ jest większa niż niepewności względne $A$ i $T_2$?
Uzasadnij krótko.

**Z-16.5.** Bootstrap. Dla danych z Z-16.2 wyznacz przedział ufności $68\%$ dla średniej
metodą bootstrap ($B=2000$).
(a) Opisz procedurę resamplowania.
(b) Podaj przedział (percentyle 16 i 84).
(c) Porównaj z przedziałem $\bar n\pm u_n$.

**Z-16.6.** Punkty odstające. Dane (jednostki umowne): $10{,}0;10{,}2;9{,}8;10{,}1;9{,}9;10{,}0;10{,}3;9{,}7;10{,}1;9{,}9;10{,}0;10{,}2;9{,}8;10{,}0;12{,}0$.
(a) Wykryj odstający regułą $3\sigma$.
(b) Zastosuj MAD i $\hat\sigma\approx1{,}4826\,\mathrm{MAD}$.
(c) Wyjaśnij, jak obecność punktu $12{,}0$ wpływa na średnią i na $\chi^2$.

**Z-16.7.** FFT i widmo.
(a) Sygnał $f_0=10$ Hz próbkowany z $f_s=12$ Hz — jaka częstość pojawi się w widmie? Uzasadnij.
(b) Jaka jest rozdzielczość widma dla $N=1000$ próbek i $f_s=100$ Hz?
(c) Po co stosuje się okno przed FFT?

**Z-16.8. [★]** Szum $1/f$ i filtr.
(a) Opisz, jak wygenerować szum o gęstości $1/f$ dla $N=4096$ punktów.
(b) Jak zmieni się odchylenie standardowe sygnału po filtrze średniej ruchomej $k=8$?
(c) Dlaczego filtr dolnoprzepustowy słabo radzi sobie z szumem $1/f$?

## 7. Wskazówki do zadań

- **Z-16.1.** (a) funkcja trygonometryczna na całej tablicy; (b) broadcasting rozciąga wymiar 1;
  (c) narzut interpretera Pythona vs kod C.
- **Z-16.2.** (a) $u=s/\sqrt N$; (b) dla Poissona wariancja $=$ średnia; (c) 1–2 cyfry niepewności.
- **Z-16.3.** (a) kolumny $V$ to $(x_i,1)$; (b) $\mathrm{ndof}=4$; (c) $\vec g=(7,1)$, $u^2=\vec g^{\mathsf T}\mathrm{Cov}\,\vec g$.
- **Z-16.4.** (a) $\partial_A y=e^{-t/T_2}$, $\partial_{T_2} y=Ae^{-t/T_2}t/T_2^2$; (b) `rng.normal`; (c) porównaj niepewności względne.
- **Z-16.5.** (a) indeksy z powtórzeniami; (b) `np.percentile`; (c) przedział $\approx2u_n$.
- **Z-16.6.** (a) $|x-\bar x|>3s$; (b) MAD = mediana odchyleń; (c) średnia z/bez $15{,}0$.
- **Z-16.7.** (a) alias $=|f_0-f_s|$; (b) $\Delta f=f_s/N$; (c) okno redukuje przeciek.
- **Z-16.8.** (b) dla szumu białego wariancja maleje jak $1/k$; (c) moc $1/f$ jest na niskich częstościach.

## 8. Co dalej

- **Macierze gęstości i kanały** — [rozdział 17](17-ponad-program-macierze-gestosci-i-kanaly.md):
  formalizm, w którym opisujemy szum mierzony w tych danych.
- **Dekoherencja i $T_1/T_2$** — [rozdział 18](18-ponad-program-splatanie-dekoherencja-termodynamika.md): model zaniku $Ae^{-t/T_2}$.
- **Mini-projekt 6** — [rozdział 20](20-ponad-program-mini-projekty.md): analiza danych z pliku CSV (zliczenia fotonów lub zanik $T_2$).
- Pełne rozwiązania: [zadania/rozwiazania/rozwiazania-16.md](../zadania/rozwiazania/rozwiazania-16.md).
- Praca domowa: [PD-4](../praca-domowa/praca-domowa-04.md).
- Kod: [`kod/analiza_danych.py`](../kod/analiza_danych.py) — dopasowanie, $\chi^2$, bootstrap, FFT.




