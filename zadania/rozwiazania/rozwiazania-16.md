# Rozwiązania do rozdziału 16

## Z-16.1

(a) `t = np.linspace(0, 1, 5)` daje $t=(0;\ 0{,}25;\ 0{,}5;\ 0{,}75;\ 1)$, a
`y = np.sin(2*np.pi*t)` daje $y=(0;\ 1;\ 0;\ -1;\ 0)$ (pierwszy i ostatni element to $O(10^{-16})$,
czyli numeryczne zero).

(b) `np.array([[1],[2]])` ma kształt $(2,1)$, a `np.array([[0,10,20]])` — kształt $(1,3)$.
Broadcasting rozciąga oba do $(2,3)$: wynik to
$\begin{pmatrix}1&11&21\\2&12&22\end{pmatrix}$, czyli **6 elementów**.

(c) Pętla `for` wykonuje Python-owy kod per element (narzut na każdą iterację), a operacja NumPy
przetwarza całą tablicę w kodzie skompilowanym (C), bez narzutu interpretera na element. Dla
$N=10^6$ daje to różnicę rzędów wielkości.

**Odpowiedź:** (a) $y=(0;1;0;-1;0)$; (b) kształt $(2,3)$, 6 elementów; (c) brak narzutu interpretera.
*Fizycznie:* wektoryzacja to ten sam rachunek, tylko wykonany „hurtowo” — wynik matematyczny jest
identyczny.

## Z-16.2

(a) Niepewność pojedynczego pomiaru szacujemy odchyleniem standardowym próbki $s$ (z $N-1$ w
mianowniku), a niepewność **średniej** to $u=s/\sqrt N$. Dane:

$$s=\sqrt{\tfrac{1}{N-1}\sum(x_i-\bar x)^2}=4{,}85,\qquad u=\frac{4{,}85}{\sqrt{12}}=1{,}40 .$$

(b) Dla rozkładu Poissona wariancja równa się średniej. Tu $\bar n=24{,}42$, $s^2=23{,}54$ —
iloraz $s^2/\bar n=0{,}96\approx1$, więc dane **zgadzają się** z rozkładem Poissona.
(c) Niepewność zaokrąglamy do 2 cyfr znaczących: $\bar n=24{,}4\pm1{,}4$.

**Odpowiedź:** $\bar n=\mathbf{24{,}4}$, $s=\mathbf{4{,}85}$, $u=\mathbf{1{,}40}$; $s^2/\bar n\approx1$
(Poisson); wynik $\mathbf{24{,}4\pm1{,}4}$.
*Fizycznie:* zliczenia fotonów rządzi rozkład Poissona — fluktuacja $\sqrt{\bar n}$ to nie „szum
sprzętu”, lecz natura światła.

## Z-16.3

(a) $V=\begin{pmatrix}1&1\\2&1\\ \vdots&\vdots\\6&1\end{pmatrix}$, $W=\tfrac1{0{,}04}I$, więc
$V^{\mathsf T}WV=\begin{pmatrix}2275&525\\525&150\end{pmatrix}$ i
$\hat\beta=(V^{\mathsf T}WV)^{-1}V^{\mathsf T}Wy=(1{,}9657;\ 0{,}1533)$.
(b) Reszty dają $\chi^2=2{,}819$, $\mathrm{ndof}=6-2=4$, $\chi^2_{\rm red}=0{,}705$;
$R^2=1-\sum r_i^2/\sum(y_i-\bar y)^2=0{,}9983$.
(c) $y(7)=1{,}9657\cdot7+0{,}1533=13{,}913$; z $\vec g=(7,1)$ i
$\mathrm{Cov}=(V^{\mathsf T}WV)^{-1}$ mamy $u_y=\sqrt{\vec g^{\mathsf T}\mathrm{Cov}\,\vec g}=0{,}186$.

**Odpowiedź:** $\mathbf{a=1{,}966\pm0{,}048}$, $\mathbf{b=0{,}153\pm0{,}186}$,
$\mathbf{\chi^2_{\rm red}=0{,}70}$, $\mathbf{R^2=0{,}998}$, $\mathbf{y(7)=13{,}91\pm0{,}19}$.
*Fizycznie:* $\chi^2_{\rm red}\approx1$ oznacza, że model i niepewności są wzajemnie spójne.

## Z-16.4

(a) $y=Ae^{-t/T_2}=0{,}99\,e^{-1{,}2}=0{,}2982$;
$\partial y/\partial A=e^{-1{,}2}=0{,}3012$, $\partial y/\partial T_2=Ae^{-1{,}2}t/T_2^2=0{,}1431$, więc

$$u_y=\sqrt{(0{,}3012\cdot0{,}01)^2+(0{,}1431\cdot0{,}05)^2}=\sqrt{6{,}03\cdot10^{-5}}=0{,}0078 .$$

(b) Monte Carlo ($10^4$–$10^5$ próbek, $A\sim\mathcal N(0{,}99,0{,}01)$,
$T_2\sim\mathcal N(2{,}5,0{,}05)$) daje $y=0{,}2981\pm0{,}0078$ — zgodne z (a).
(c) Niepewności względne: $u_A/A=1{,}0\%$, $u_{T_2}/T_2=2{,}0\%$, a $u_y/y=2{,}6\%$. Niepewność $y$
jest **większa** od każdej z osobna, bo oba wkłady dodają się w kwadratach.

**Odpowiedź:** $\mathbf{y=0{,}298\pm0{,}008}$; MC daje to samo; $u_y/y=2{,}6\%$, czyli więcej niż
$1{,}0\%$ i $2{,}0\%$.
*Fizycznie:* eksponenta „wzmacnia” niepewność $T_2$, bo $t/T_2=1{,}2$ jest tu dużym wykładnikiem.

## Z-16.5

(a) Procedura: z $N=12$ danych losujemy **z powtórzeniami** $N$ indeksów (`rng.integers(0, N, N)`),
liczymy średnią resamplowania; powtarzamy $B=2000$ razy i bierzemy percentyle 16 i 84 rozkładu
średnich.
(b) Dla danych z Z-16.2: przedział $[23{,}1;\ 25{,}7]$, szerokość $2{,}58$.
(c) Przedział „normalny” $\bar n\pm u_n=[23{,}0;\ 25{,}8]$ ma szerokość $2u=2{,}80$ — praktycznie
taki sam, więc rozkład średniej jest bliski normalnemu.

**Odpowiedź:** $\mathbf{[23{,}1;\ 25{,}7]}$ (68%), zgodny z $\mathbf{[23{,}0;\ 25{,}8]}$.
*Fizycznie:* bootstrap nie zakłada rozkładu — działa też dla małych próbek i skośnych estymatorów.

## Z-16.6

(a) Średnia $\bar x=10{,}133$, odchylenie standardowe próbki $s=0{,}542$, więc $3s=1{,}626$.
Odchylenie punktu $12{,}0$ wynosi $\lvert12{,}0-10{,}133\rvert=1{,}867>1{,}626$ — reguła $3\sigma$
**wykrywa** punkt odstający.
(b) Mediana $=10{,}0$; $\mathrm{MAD}=0{,}10$;
$\hat\sigma=1{,}4826\cdot0{,}10=0{,}148$. Odchylenie $12{,}0$ to $1{,}867/0{,}148=12{,}6\hat\sigma$ —
MAD wykrywa punkt **znacznie** pewniej niż $3\sigma$ (bo jest odporny na samego odstającego).
(c) Średnia **z** punktem $=10{,}133$, **bez** $=10{,}000$ (przesunięcie o $+0{,}133$); punkt $12{,}0$
daje $\approx85\%$ sumy $\sum r_i^2$, więc $\chi^2$ niemal podwaja się przez jedną obserwację.

**Odpowiedź:** (a) $\mathbf{1{,}867>3s=1{,}626}$ — wykryty; (b) $\mathbf{12{,}6\hat\sigma}$ (MAD);
(c) średnia rośnie o $\mathbf{0{,}133}$, $\chi^2$ zdominowany przez ten punkt.
*Fizycznie:* pojedynczy odstający fałszuje i średnią, i $\chi^2$ — dlatego najpierw sprawdzamy
pomiar, a nie „poprawiamy” dane.

## Z-16.7

(a) Częstość Nyquista $f_N=f_s/2=6$ Hz, a $f_0=10$ Hz $>f_N$, więc sygnał ulega aliasowi do
$\lvert f_0-f_s\rvert=\lvert10-12\rvert=$ **2 Hz**; to fałszywy pik, którego nie da się odróżnić od
prawdziwego 2 Hz.
(b) Rozdzielczość $\Delta f=f_s/N=100/1000=0{,}1$ Hz.
(c) Okno (np. Hanna) wygładza końce próbki, bo DFT „widzi” sygnał jako okresowy — nieciągłość na
krańcach daje przeciek widmowy; okno go tłumi kosztem nieco szerszych pików.

**Odpowiedź:** (a) $\mathbf{2}$ **Hz**; (b) $\mathbf{0{,}1}$ **Hz**; (c) redukcja przecieku.
*Fizycznie:* poniżej $2f_0$ nie ma „wolniejszego świata” — jest tylko błędna identyfikacja.

## Z-16.8

(a) Generujemy szum biały (`rng.normal`), liczymy `np.fft.rfft`, mnożymy amplitudy przez $1/\sqrt f$
(pomijając $f=0$) i wracamy przez `np.fft.irfft`; po normalizacji mamy szum o gęstości mocy
$\propto1/f$.
(b) Średnia ruchoma $k=8$ uśrednia 8 niezależnych próbek, więc wariancja szumu **białego** maleje
jak $1/k$; odchylenie standardowe maleje jak $1/\sqrt k=0{,}354$ (symulacja: $0{,}34$).
(c) Szum $1/f$ ma moc skupioną na **niskich** częstościach, których filtr dolnoprzepustowy nie usuwa
(przepuszcza je); trzeba filtrować pasmowo lub uśredniać bardzo długo.

**Odpowiedź:** (a) amplitudy $\propto1/\sqrt f$; (b) $\sigma\to\sigma/\sqrt8=0{,}354\,\sigma$;
(c) moc $1/f$ leży w paśmie przepustowym filtra.
*Fizycznie:* filtr „wygładza” tylko szybkie fluktuacje; szum różowy to fluktuacje wolne, „z pamięcią”.
