# 03. Rachunek prawdopodobieństwa i statystyka


## 1. Zakres rozdziału

Rozdział obejmuje aksjomaty prawdopodobieństwa, prawdopodobieństwo warunkowe,
niezależność i twierdzenie Bayesa. Omawia zmienne losowe i rozkłady (Bernoulliego,
dwumianowy, Poissona, jednostajny, normalny), wartość oczekiwaną, wariancję, prawo
wielkich liczb i twierdzenie graniczne (CTG). Obejmuje też propagację niepewności,
estymację, przedział ufności, test chi-kwadrat, $p$-value, kowariancję, entropię
Shannona i Monte Carlo. Materiał dotyczy zadań P1 i P2 (rozkłady wyników pomiaru,
zliczenia fotonów) oraz analizy danych.

## 2. Najważniejsze definicje

- **Przestrzeń zdarzeń** $\Omega$; **zdarzenie** $A\subseteq\Omega$;
  **prawdopodobieństwo** $P:\mathcal{F}\to[0,1]$.
- **Prawdopodobieństwo warunkowe**: $P(A\mid B)=\dfrac{P(A\cap B)}{P(B)}$, $P(B)>0$.
- **Niezależność**: $P(A\cap B)=P(A)P(B)$ (równoważnie $P(A\mid B)=P(A)$).
- **Prawdopodobieństwo całkowite**: $P(A)=\sum_i P(A\mid B_i)P(B_i)$ dla rozbicia $\{B_i\}$.
- **Zmienna losowa** $X$; **dystrybuanta** $F(x)=P(X\le x)$; **gęstość/prawdopodobieństwo**.
- **Wartość oczekiwana** $\mathbb{E}X=\sum_k x_kP(X=x_k)$ (lub $\int x\,f(x)\,dx$).
- **Wariancja** $\mathrm{Var}X=\mathbb{E}(X-\mathbb{E}X)^2=\mathbb{E}X^2-(\mathbb{E}X)^2$;
  **odchylenie** $\sigma=\sqrt{\mathrm{Var}X}$.
- **Kowariancja** $\mathrm{Cov}(X,Y)=\mathbb{E}XY-\mathbb{E}X\,\mathbb{E}Y$;
  **korelacja** $\rho=\mathrm{Cov}(X,Y)/(\sigma_X\sigma_Y)\in[-1,1]$.
- **Entropia Shannona** $H=-\sum_k p_k\log_2 p_k$ (w bitach).
- **Estymator** $\hat\theta$ (funkcja danych); **przedział ufności** o poziomie $1-\alpha$.
- **Test $\chi^2$**: $\chi^2=\sum_i\frac{(O_i-E_i)^2}{E_i}$ (**O** — obserwowane,
  **E** — oczekiwane); **$p$-value** = $P(\chi^2_{\rm df}\ge\chi^2_{\rm obs})$.

## 3. Teoria krok po kroku

### 3.1 Aksjomaty (Kołmogorowa)

1. $P(A)\ge0$ dla każdego zdarzenia.
2. $P(\Omega)=1$.
3. dla zdarzeń rozłącznych $P(A\cup B)=P(A)+P(B)$ (i uogólnienie na sumy przeliczalne).

Wnioski: $P(\emptyset)=0$; $P(A^c)=1-P(A)$; $P(A\cup B)=P(A)+P(B)-P(A\cap B)$.
Aksjomaty to reguły „księgowości” prawdopodobieństw — cała reszta rozdziału z nich wynika.

### 3.2 Prawdopodobieństwo warunkowe i niezależność

$P(A\mid B)=P(A\cap B)/P(B)$ mierzy „udział $B$ w $A$”. Z tego wynika reguła iloczynu
$P(A\cap B)=P(A\mid B)P(B)$. Zdarzenia są niezależne, gdy warunkowanie nic nie zmienia.
Niezależność $\ne$ rozłączność — zdarzenia rozłączne ($A\cap B=\emptyset$)
są wręcz maksymalnie zależne (znając $A$, wiesz, że $B$ nie zaszło).

### 3.3 Twierdzenie Bayesa

Z $P(A\cap B)=P(A\mid B)P(B)=P(B\mid A)P(A)$:

$$
P(B\mid A)=\frac{P(A\mid B)P(B)}{P(A)},\qquad
P(A)=\sum_i P(A\mid B_i)P(B_i).
$$

Bayes „odwraca” warunkowanie: ze znajomości $P(\text{wynik}\mid\text{hipoteza})$
wnioskujemy o $P(\text{hipoteza}\mid\text{wynik})$. To podstawa diagnostyki i analizy
danych pomiarowych.

### 3.4 Zmienne losowe, $E$ i $\mathrm{Var}$

Wartość oczekiwana jest liniowa: $\mathbb{E}(aX+bY)=a\mathbb{E}X+b\mathbb{E}Y$.
Wariancja: $\mathrm{Var}(aX+b)=a^2\mathrm{Var}X$, a dla **niezależnych**
$\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y$. Dla $n$ niezależnych
kopii: $\sigma_{\bar X}=\sigma/\sqrt n$ (błąd maleje jak $1/\sqrt n$).

### 3.5 Rozkłady

| Rozkład | Parametry | $P$ lub gęstość | $\mathbb{E}X$ | $\mathrm{Var}X$ |
| --- | --- | --- | --- | --- |
| Bernoulliego | $p$ | $P(1)=p$, $P(0)=1-p$ | $p$ | $p(1-p)$ |
| dwumianowy | $n,p$ | $\binom nk p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ |
| Poissona | $\lambda$ | $e^{-\lambda}\lambda^k/k!$ | $\lambda$ | $\lambda$ |
| jednostajny | $[a,b]$ | $1/(b-a)$ | $(a+b)/2$ | $(b-a)^2/12$ |
| normalny | $\mu,\sigma$ | $\frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}$ | $\mu$ | $\sigma^2$ |

Rozkład dwumianowy opisuje liczbę sukcesów w $n$ próbach; **Poisson** to jego granica
dla dużego $n$ i małego $p$ przy $\lambda=np$ (rzadkie zdarzenia — np. zliczenia
fotonów w okienku czasu). Rozkład normalny to granica sum (CTG).

### 3.6 Prawo wielkich liczb i twierdzenie graniczne (CTG)

**Prawo wielkich liczb.** Średnia arytmetyczna $\bar X_n$ z $n$ niezależnych prób
zbiega do $\mathbb{E}X$ przy $n\to\infty$ — dlatego „częstotliwość $\to$
prawdopodobieństwo”.

**Centralne twierdzenie graniczne (CTG).** Dla $n$ niezależnych zmiennych o skończonej
wariancji suma (po standaryzacji) dąży do rozkładu normalnego:

$$
\frac{\sum_i X_i-n\mu}{\sigma\sqrt n}\xrightarrow{\,d\,}\mathcal{N}(0,1).
$$

Praktycznie: sumy i średnie z wielu małych, niezależnych przyczyn są w przybliżeniu
normalne. Wartości krytyczne: $P(|Z|<1)\approx0{,}683$, $P(|Z|<2)\approx0{,}954$,
$P(|Z|<3)\approx0{,}997$.

### 3.7 Propagacja niepewności

Dla wielkości $f(x_1,\dots,x_n)$ o **niezależnych** niepewnościach $\sigma_{x_i}$:

$$
\sigma_f^2=\sum_i\left(\frac{\partial f}{\partial x_i}\right)^2\sigma_{x_i}^2,
\qquad\text{a dla iloczynu/ilorazu}\qquad
\left(\frac{\sigma_f}{|f|}\right)^2=\sum_i\left(\frac{\sigma_{x_i}}{x_i}\right)^2.
$$

Szczególnie dla $f=x/y$ niepewności względne dodają się **kwadratowo**.

### 3.8 Estymacja punktowa i przedziałowa

- **Punktowa:** $\hat\mu=\bar X=\frac1n\sum X_i$ (średnia jest nieobciążonym
  estymatorem $\mu$); $\hat\sigma^2=\frac{1}{n-1}\sum(X_i-\bar X)^2$ (dzielnik $n-1$
  daje nieobciążoność).
- **Przedziałowa:** dla znanej $\sigma$ przedział ufności średniej na poziomie
  $1-\alpha$ to $\bar X\pm z_{1-\alpha/2}\,\sigma/\sqrt n$; dla $\alpha=0{,}05$
  mamy $z_{0{,}975}\approx1{,}96$, więc „$\pm2\sigma/\sqrt n$”.

### 3.9 Test $\chi^2$ i $p$-value

Test $\chi^2$ porównuje rozkład obserwowany z oczekiwanym:
$\chi^2=\sum_i(O_i-E_i)^2/E_i$ z $\mathrm{df}=k-1$ (minus liczba dopasowanych
parametrów). Duże $\chi^2$ przeczy hipotezie. **$p$-value** to prawdopodobieństwo
otrzymania wyniku co najmniej tak skrajnego, gdy hipoteza jest prawdziwa; przyjmuje
się próg $p<0{,}05$ jako „istotne”. Dla $\mathrm{df}=2$ zachodzi prosty wzór
$P(\chi^2>x)=e^{-x/2}$.

### 3.10 Kowariancja i korelacja

$\mathrm{Cov}(X,Y)=\mathbb{E}XY-\mathbb{E}X\mathbb{E}Y$ mierzy wspólną zmienność;
$\rho=\mathrm{Cov}(X,Y)/(\sigma_X\sigma_Y)$ jest znormalizowane do $[-1,1]$.
$\rho=0$ oznacza brak **liniowej** korelacji (nie brak zależności!). Kowariancja
macierzy gęstości to $\mathrm{Cov}(A,B)=\langle AB\rangle-\langle A\rangle\langle B\rangle$
— dla niezależnych obserwabli znika.

### 3.11 Entropia Shannona

$H=-\sum_k p_k\log_2 p_k$ to średnia nieoznaczoność rozkładu, w bitach.
Dla rozkładu dwupunktowego $p$: $H(p)=-p\log_2 p-(1-p)\log_2(1-p)$, maksimum
$H=1$ bit przy $p=1/2$, minimum $0$ przy $p=0$ lub $1$. To kwantowe tło entropii
von Neumanna (rozdział 18) i miary splątania ($S$ z rozdziału 02).

### 3.12 Metoda Monte Carlo

Gdy całka lub rozkład są trudne analitycznie, **losujemy** i uśredniamy. Dla całki
$I=\int_a^b f(x)dx$ bierzemy $N$ próbek jednostajnych i liczymy
$\hat I=(b-a)\frac1N\sum f(x_i)$, z błędem $\sim\sigma/\sqrt N$. Przykład: pole
ćwiartki koła w kwadracie $[0,1]^2$ daje $\pi\approx4\cdot(\text{odsetek trafień})$
(przy $N=10^5$ wychodzi $\approx3{,}14$).

### 3.13 Zastosowanie: zliczenia fotonów i statystyka pomiarów

Detektor fotonów w ustalonym okienku czasu rejestruje **rzadkie, niezależne** zdarzenia
— liczba zliczeń $K$ ma rozkład Poissona: $P(K=k)=e^{-\lambda}\lambda^k/k!$ z
$\lambda=$ średnia liczba fotonów. Charakterystyka: $\mathbb{E}K=\mathrm{Var}K=\lambda$,
więc szum zliczeń („shot noise”) ma $\sigma_K=\sqrt\lambda$ i względny błąd
$1/\sqrt\lambda$ — by poprawić precyzję dwukrotnie, trzeba czterokrotnie więcej
fotonów. To ta sama logika, co błąd $\sigma/\sqrt n$ przy uśrednianiu pomiarów.

Pomiar kwantowy: powtarzamy przygotowanie stanu i pomiar $N$ razy, dostając wyniki
$0/1$. Estymator prawdopodobieństwa $\hat p=k/N$ ma błąd $\sqrt{p(1-p)/N}$; dla
$N\to\infty$ z CTG dostajemy przedział ufności dla $p$ — tym sposobem weryfikujemy
teorię (np. prawo Malusa z zadania P2).

## 4. Przykłady rozwiązane

### Przykład 1 (łatwy): rozkład dwumianowy

**Dane:** rzucamy symetryczną monetą $n=10$ razy; $X$ = liczba orłów.

**Metoda:** $X\sim\mathrm{Bin}(10,\tfrac12)$; wzór $\binom nk p^k(1-p)^{n-k}$;
$\mathbb{E}X=np$, $\mathrm{Var}X=np(1-p)$.

**Rachunek:** $P(X=3)=\binom{10}{3}\bigl(\tfrac12\bigr)^{10}=\dfrac{120}{1024} \approx0{,}1172$. Wartość oczekiwana $\mathbb{E}X=10\cdot\tfrac12=5$, wariancja
$\mathrm{Var}X=10\cdot\tfrac12\cdot\tfrac12=2{,}5$, odchylenie $\sqrt{2{,}5}\approx1{,}58$.

**Wynik:** $P(X=3)\approx0{,}117$, $\mathbb{E}X=5$, $\sigma_X\approx1{,}58$.

**Interpretacja:** najbardziej prawdopodobne są wyniki blisko $5$; $P(X=3)$ jest
nieco większe niż $0{,}1$, mimo że $3$ jest odległe o $\approx1{,}3\sigma$ od średniej.

### Przykład 2 (trudniejszy): twierdzenie Bayesa w diagnostyce

**Dane:** choroba występuje z $P(C)=0{,}001$; test ma czułość
$P({+}\mid C)=0{,}99$ i swoistość $P({-}\mid H)=0{,}95$ ($H$ = zdrowy).

**Metoda:** prawdopodobieństwo całkowite w mianowniku + Bayes.

**Rachunek:**

$$
P(+)={0{,}99\cdot0{,}001}+{0{,}05\cdot0{,}999}=0{,}00099+0{,}04995=0{,}05094,
$$

$$
P(C\mid{+})=\frac{P({+}\mid C)P(C)}{P(+)}=\frac{0{,}00099}{0{,}05094}\approx0{,}0194.
$$

Dla wyniku negatywnego:
$P(H\mid{-})=\dfrac{0{,}95\cdot0{,}999}{0{,}95\cdot0{,}999+0{,}01\cdot0{,}001} \approx0{,}99999$.

**Wynik:** $P(C\mid{+})\approx1{,}9\%$, $P(H\mid{-})\approx99{,}999\%$.

**Interpretacja:** mimo $99\%$ czułości, dodatni wynik daje tylko $\approx2\%$
szansy choroby — bo choroba jest rzadka, więc większość dodatnich wyników to
**fałszywe alarmy**. To klasyczny przykład, jak rzadkość zaburza intuicję.

### Przykład 3 (trudniejszy): zliczanie fotonów (Poisson)

**Dane:** średnio $\lambda=3$ fotony na okienko.

**Metoda:** $P(K=k)=e^{-\lambda}\lambda^k/k!$.

**Rachunek:** $P(K=2)=e^{-3}\dfrac{3^2}{2}=e^{-3}\cdot4{,}5\approx0{,}2240$;
$P(K=0)=e^{-3}\approx0{,}0498$. Średnia i wariancja: $\mathbb{E}K=\mathrm{Var}K=3$,
szum $\sigma_K=\sqrt3\approx1{,}73$.

**Wynik:** $P(K=2)\approx0{,}224$, $P(K=0)\approx0{,}050$, $\sigma_K\approx1{,}73$.

**Interpretacja:** zliczenia fotonów mają „szum śrutowy” o względnym odchyleniu
$1/\sqrt3\approx58\%$ — żeby uzyskać $1\%$ precyzji, trzeba $\sim10^4$ fotonów.

## 5. Typowe pułapki

1. **Mylenie $P(A\mid B)$ z $P(B\mid A)$.** To nie to samo (Przykład 2).
2. **Traktowanie $\rho=0$ jako „brak zależności”.** Zerowa korelacja mówi tylko o
   braku **liniowego** związku.
3. **Dzielenie przez $n$ zamiast $n-1$** w wariancji z próbki — zaniża estymator.
4. **Dodawanie niepewności liniowo.** Niezależne niepewności dodajemy **kwadratowo**.
5. **Zapominanie o warunku normalizacji** rozkładu — suma prawdopodobieństw musi być $1$.
6. **Zbyt mocne wnioski z $p$-value.** Duże $p$ nie „dowodzi” hipotezy, a małe
   $p$ nie mierzy wielkości efektu.
7. **Mylenie $\sigma$ z $\sigma/\sqrt n$.** Odchylenie pojedynczego pomiaru to $\sigma$;
   błąd średniej maleje jak $1/\sqrt n$.

## 6. Zadania (Z-03)

**Z-03.1.** Rzucamy dwiema kostkami.
(a) Policz $P(\text{suma}=7)$. (b) Policz $P(\text{suma}=7\mid\text{pierwsza}=3)$.
(c) Czy zdarzenia „suma $=7$” i „pierwsza kostka $=3$” są niezależne?

**Z-03.2.** Test: choroba z $P(C)=0{,}001$, czułość $0{,}99$, swoistość $0{,}95$.
(a) Policz $P(C\mid{+})$. (b) Policz $P(H\mid{-})$. (c) Skomentuj rolę
prawdopodobieństwa apriorycznego.

**Z-03.3.** $X$ = wynik rzutu jedną kostką.
(a) Policz $\mathbb{E}X$. (b) Policz $\mathrm{Var}X$. (c) Policz $\mathbb{E}X^2$
i sprawdź związek $\mathrm{Var}X=\mathbb{E}X^2-(\mathbb{E}X)^2$.

**Z-03.4.** (a) Dla $X\sim\mathrm{Bin}(10,\tfrac12)$ policz $P(X=3)$.
(b) Dla $K\sim\mathrm{Pois}(3)$ policz $P(K=2)$ i $P(K=0)$.
(c) Porównaj $\mathbb{E}$ i $\mathrm{Var}$ obu rozkładów i wyjaśnij związek
dwumianowego z Poissona.

**Z-03.5.** (a) Podaj $P(|Z|<2)$ dla $Z\sim\mathcal{N}(0,1)$.
(b) Dla $100$ rzutów monetą oszacuj przez CTG $P(45\le\text{orłów}\le55)$ (z korekcją
ciągłości). (c) Porównaj z wynikiem dokładnym i skomentuj.

**Z-03.6.** Gęstość $\rho=m/V$; $m=(200\pm2)$ g, $V=(50{,}0\pm0{,}5)$ mL (niezależne).
(a) Policz $\rho$. (b) Policz $\sigma_\rho$. (c) Wskaż, który pomiar trzeba poprawić,
i uzasadnij.

**Z-03.7.** Obserwacje $[12,8,10]$, oczekiwane $[10,10,10]$.
(a) Policz $\chi^2$. (b) Policz $p$-value ($\mathrm{df}=2$) i sformułuj wniosek.
(c) Policz entropię $H(0{,}5)$ i $H(0{,}1)$.

**Z-03.8. [★]** (a) Opisz, jak estymować $\pi$ metodą Monte Carlo, i podaj wynik dla
$N=10^5$ (ziarno $0$). (b) Dla danych $x=(1,2,3,4,5)$, $y=(2,4,5,4,5)$ policz
$\mathrm{Cov}$ i $\rho$. (c) Zinterpretuj $|\rho|<1$.

## 7. Wskazówki do zadań

- **Z-03.1.** Wszystkie $36$ wyników jednakowo prawdopodobne; do (c) porównaj
  $P(A\cap B)$ z $P(A)P(B)$.
- **Z-03.2.** Prawdopodobieństwo całkowite w mianowniku, jak w Przykładzie 2.
- **Z-03.3.** $\mathbb{E}X=\frac16\sum_{k=1}^6k$; wariancja z definicji.
- **Z-03.4.** Wzory z tabeli w §3.5; Poisson jako granica dwumianowego ($\lambda=np$).
- **Z-03.5.** Standaryzacja $Z=(X-\mu)/\sigma$; dla korekcji ciągłości użyj
  granic $44{,}5$ i $55{,}5$.
- **Z-03.6.** Niepewności **względne** dodaj kwadratowo dla ilorazu.
- **Z-03.7.** $\chi^2=\sum(O-E)^2/E$; dla $\mathrm{df}=2$, $p=e^{-\chi^2/2}$;
  entropia ze wzoru $H(p)=-p\log_2p-(1-p)\log_2(1-p)$.
- **Z-03.8.** [★] Odsetek trafień $\times4$; kowariancja $\mathbb{E}XY-\mathbb{E}X\,\mathbb{E}Y$.

## 8. Co dalej

Statystyka jest podstawą metody Monte Carlo (rozdział 16) i metrologii kwantowej
(rozdział 11). Równania różniczkowe i całki są w rozdziale
[04](04-elementy-analizy-matematycznej.md), a probabilistyczna interpretacja funkcji
falowej — w [05](05-podstawy-mechaniki-kwantowej.md). Rozwiązania zadań są w
[rozwiazania-03.md](../zadania/rozwiazania/rozwiazania-03.md); zadania łączące
rozdziały 01–05 to [PD-1](../praca-domowa/praca-domowa-01.md).
