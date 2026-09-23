# Praca domowa PD-2 (rozdziały 06–10)

Praca domowa po module drugim obejmuje rozdziały [06](../teoria/06-kubity-bramki-obwody-pomiary.md)
(kubity, bramki, obwody, pomiary), [07](../teoria/07-kwantowa-teoria-informacji.md) (teoria informacji),
[08](../teoria/08-algorytmy-kwantowe.md) (algorytmy), [09](../teoria/09-splatanie-i-twierdzenie-bella.md)
(splątanie i Bella) oraz [10](../teoria/10-kryptografia-kwantowa.md) (kryptografia).

**Zasady:** rozwiązania pisemne, każde z pełnym uzasadnieniem i jawnym rachunkiem. Konwencja
notacji: baza $\lvert q_1q_0\rangle$, bramka na $q_1$ $=G\otimes I$, na $q_0$ $=I\otimes G$,
$\theta/2$ w bramkach obrotu. Wyniki przybliżone z 3 cyframi znaczącymi. **Razem 20 punktów**
(10 zadań po 2 pkt).

## Zadania

**PD-2.1 (2 pkt).** Mnożenie macierzy $4\times4$. Dany CNOT z kontrolą $q_1$ i celem $q_0$.
(a) Oblicz $U_1=\mathrm{CNOT}\,(X\otimes I)\,\mathrm{CNOT}$ i rozpoznaj otrzymaną bramkę.
(b) Oblicz $U_2=\mathrm{CNOT}\,(I\otimes Z)\,\mathrm{CNOT}$ i rozpoznaj otrzymaną bramkę.
(c) Zinterpretuj oba wyniki: dlaczego $X$ „rozprzestrzenia się”, a $Z$ „propaguje wstecz”.

**PD-2.2 (2 pkt).** Obwód dwukubitowy, macierz $4\times4$. Start $\lvert00\rangle$; wykonaj $H$ na górnym
kubicie, $R_Y(\pi/2)$ na dolnym, potem CNOT (kontrola górny, cel dolny).
(a) Podaj wektor stanu po obwodzie.
(b) Podaj $P_{00},P_{01},P_{10},P_{11}$.
(c) Czy stan jest splątany? Odpowiedź uzasadnij (concurrence).

**PD-2.3 (2 pkt).** Informacja kwantowa. (a) Sformułuj twierdzenie o zakazie klonowania i naszkicuj dowód.
(b) Policz entropię von Neumanna dla $\lvert+\rangle$ oraz dla $\rho=\frac12 I$.
(c) Wyjaśnij, dlaczego (b) pokazuje, że pomiar bazie $X$ nie może dać więcej niż $1$ bit informacji o $\rho=\frac12 I$.

**PD-2.4 (2 pkt).** Algorytm Grovera. Baza $N=16$ ($4$ kubity), jedno rozwiązanie.
(a) Policz $\theta$ ($\sin\theta=1/\sqrt N$) i optymalną liczbę iteracji $k_{\text{opt}}$.
(b) Podaj $P_{\text{sukces}}$ dla $k=3$ oraz dla $k=4$.
(c) Ile zapytań potrzebuje klasyczny algorytm (średnio) i dlaczego $k_{\text{opt}}$ nie może być dowolnie duże?

**PD-2.5 (2 pkt).** Splątanie i PPT. Dany stan Wernera $\rho=p\lvert\Phi^+\rangle\langle\Phi^+\rvert+\frac{1-p}{4}I$
przy $p=0{,}8$. (a) Podaj wartości własne $\rho^{T_B}$ i wyznacz najmniejszą. (b) Oblicz concurrence.
(c) Czy stan jest splątany? Odpowiedz na podstawie (a) i (b).

**PD-2.6 (2 pkt).** Nierówność CHSH. Stan $\lvert\Psi^-\rangle$; Alicja mierzy pod $0^\circ$ oraz $90^\circ$,
Bob pod $45^\circ$ oraz $135^\circ$. (a) Policz cztery korelacje $E(a,b)=-\cos(\theta_a-\theta_b)$.
(b) Policz $S=E(a,b)-E(a,b')+E(a',b)+E(a',b')$ i jego moduł. (c) Porównaj z granicą klasyczną $2$
i z granicą Tsirelsona $2\sqrt2$.

**PD-2.7 (2 pkt).** BB84. Dane (0 = baza Z, 1 = baza X):

| $i$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bit Alicji | 1 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 0 |
| baza Alicji | Z | X | Z | Z | X | X | Z | X | Z | X | Z | X |
| baza Boba | Z | X | X | Z | X | Z | Z | X | Z | X | Z | X |

(a) Wykonaj sifting i podaj uzgodniony klucz Alicji.
(b) Oszacuj QBER, jeśli Eve stosuje intercept-resend na każdym fotonie.
(c) Na podstawie (b) zdecyduj, czy protokół należy przerwać, i uzasadnij progiem QBER.

**PD-2.8 (2 pkt).** QFT. (a) Zapisz macierz $\mathrm{QFT}_2$ jawnie i uzasadnij unitarność.
(b) Oblicz $\mathrm{QFT}_2\lvert2\rangle$ i podaj prawdopodobieństwa pomiaru.
(c) Dlaczego QFT „koncentruje” informację o okresie funkcji na kilku stanach?

**PD-2.9 (2 pkt).** Kanał i miary. Kanał depolaryzujący na jednym kubicie z parametrem $p$:
$\mathcal{E}(\rho)=(1-p)\rho+p\frac{I}{2}$; start $\rho_0=\lvert0\rangle\langle0\rvert$, $p=0{,}5$.
(a) Podaj $\mathcal{E}(\rho_0)$ w postaci macierzowej. (b) Policz wierność $F(\mathcal{E}(\rho_0),\rho_0)$.
(c) Policz dystans śladowy $D(\mathcal{E}(\rho_0),\rho_0)$ i sprawdź nierówność Fuchsa–van de Graafa.

**PD-2.10. [★] (2 pkt).** E91 i monogamia. (a) Wyjaśnij, jak w E91 pomiar $\lvert S\rvert>2$ w teście
CHSH daje zaufanie do kanału. (b) Dla stanu GHZ wyznacz $\rho_{AB}$ po odrzuceniu trzeciego kubita
i jego concurrence. (c) Wyjaśnij, dlaczego monogamia splątania jest kluczowa dla bezpieczeństwa QKD.

## Kryteria oceny

Każde zadanie jest warte **2 punkty**; oceniamy według schematu:

| Kryterium | Punkty |
| --- | --- |
| poprawna metoda i jawnie zapisane macierze / wzory | 1 |
| poprawny wynik liczbowy (3 cyfry znaczące) **oraz** interpretacja fizyczna | 1 |

Zasady szczegółowe:

- **Zadania obwodowe (PD-2.1, PD-2.2):** za sam wynik bez macierzy pośrednich maksymalnie 1 pkt.
  Błąd w kolejności mnożenia (odwrotna kolejność) — 0 pkt za wynik, 1 pkt za metodę, jeśli jawnie
  zadeklarowano konwencję.
- **Zadania rachunkowe (PD-2.3–PD-2.9):** punkty cząstkowe za poprawny krok (np. samą wartość
  własną) nawet przy błędnym końcowym wyniku.
- **Zadania z interpretacją (PD-2.1c, PD-2.3c, PD-2.6c, PD-2.7c, PD-2.8c, PD-2.10):** brak
  uzasadnienia fizycznego $\Rightarrow$ maksymalnie 1,5 pkt.
- **Błędy jednostek / brak zaokrągleń:** $-0{,}5$ pkt, jeśli wynik odbiega tylko zapisem.
- **Zadanie [★] (PD-2.10):** dopuszczamy równoważne sformułowania; liczy się poprawność logiczna
  i użycie właściwego pojęcia (monogamia).
- **Praca niezgodna z notacją** (zła kolejność kubitów, $\theta$ zamiast $\theta/2$): $-1$ pkt łącznie,
  nie za każde zadanie.

## Wskazówki i odpowiedzi

**PD-2.1.** (a) $U_1=X\otimes X$: liczymy $\mathrm{CNOT}(X\otimes I)\mathrm{CNOT}$ i otrzymujemy macierz
$\begin{pmatrix}0&0&0&1\\0&0&1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}$.
(b) $U_2=Z\otimes Z=\mathrm{diag}(1,-1,-1,1)$.
(c) $X$ na kontroli „rozprzestrzenia się” na oba kubity (bo $\mathrm{CNOT}$ kopiuje $X$ kontroli na cel),
a $Z$ na celu „propaguje wstecz” na kontrolę (bo kontrolowany-$Z$ jest symetryczny). Te tożsamości to
podstawa korekcji błędów (rozdział 13).

**PD-2.2.** (a) $\lvert\psi\rangle=\frac12(\lvert00\rangle+\lvert01\rangle+\lvert10\rangle+\lvert11\rangle)=\lvert+\rangle\otimes\lvert+\rangle$.
(b) $P_{00}=P_{01}=P_{10}=P_{11}=\frac14$.
(c) Concurrence $C=2\lvert c_{00}c_{11}-c_{01}c_{10}\rvert=2\lvert\frac14-\frac14\rvert=0$ — stan jest
**iloczynowy** (przypadek $\theta=\pi/2$ z P4).

**PD-2.3.** (a) Dowód jak w rozdziale 07: liniowość $U$ wymusza $U\lvert+\rangle\lvert0\rangle=\lvert\Phi^+\rangle$,
a klonowanie wymagałoby $\lvert+\rangle\lvert+\rangle$ — sprzeczność.
(b) $S(\lvert+\rangle)=0$; $S(\frac12 I)=1$ bit.
(c) Każdy pomiar $\frac12 I$ w bazie $X$ daje $P(+)=P(-)=\frac12$, więc entropia wyników $=1$ bit $=S(\rho)$ —
pomiar nie tworzy informacji ponad to, co zawiera stan.

**PD-2.4.** (a) $\theta=\arcsin(1/4)\approx0{,}2527$; $k_{\text{opt}}=\frac{\pi}{4\theta}-\frac12\approx2{,}61\to3$.
(b) $k=3$: $P=\sin^2(7\theta)\approx0{,}961$; $k=4$: $P=\sin^2(9\theta)\approx0{,}582$.
(c) Klasycznie średnio $\sim N/2=8$ zapytań. Nadmiar iteracji obraca stan poza rozwiązanie — sukces maleje.

**PD-2.5.** (a) Wartości własne $\rho^{T_B}$: $\frac{1+p}{4}=0{,}45$ (×3) i $\frac{1-3p}{4}=-0{,}35$;
najmniejsza wynosi $\mathbf{-0{,}35}$.
(b) $\lambda_{\Phi^+}=p+\frac{1-p}{4}=0{,}85$, $C=\max(0,2\cdot0{,}85-1)=\mathbf{0{,}7}$.
(c) Tak — ujemna wartość własna $\rho^{T_B}$ (PPT) oraz $C>0$ jednoznacznie wskazują na splątanie.

**PD-2.6.** (a) $E=-\frac{\sqrt2}{2},+\frac{\sqrt2}{2},-\frac{\sqrt2}{2},-\frac{\sqrt2}{2}$.
(b) $S=-2\sqrt2$, $\lvert S\rvert=2{,}828$.
(c) $\lvert S\rvert>2$ (naruszenie lokalnego realizmu), ale $\le2\sqrt2=2{,}828$ (granica Tsirelsona) —
wartość jest **maksymalna** dla stanu Bella przy optymalnych kątach.

**PD-2.7.** (a) Zgodne bazy na $i=0,1,3,4,6,7,8,9,10,11$ $\Rightarrow$ klucz Alicji
$=1,0,0,0,1,0,1,1,0,0$ (10 bitów; odrzucone $i=2,5$).
(b) Intercept-resend daje QBER $\approx25\%$.
(c) **Przerwać** — próg bezpieczeństwa to $\approx11\%$; przy $25\%$ zachodzi $1-2H_2(0{,}25)<0$,
więc żaden klucz nie powstanie.

**PD-2.8.** (a) $\mathrm{QFT}_2=\frac12\begin{pmatrix}1&1&1&1\\1&i&-1&-i\\1&-1&1&-1\\1&-i&-1&i\end{pmatrix}$;
kolumny ortonormalne $\Rightarrow M^\dagger M=I$.
(b) $\mathrm{QFT}_2\lvert2\rangle=\frac12(1,-1,1,-1)^{\mathsf T}$; każdy wynik $P=\frac14$.
(c) Dla funkcji okresowej amplitudy po QFT grupują się na wielokrotnościach $N/r$ — stąd odczyt okresu.

**PD-2.9.** (a) $\mathcal{E}(\rho_0)=\mathrm{diag}(0{,}75,0{,}25)$.
(b) $F=1-\frac p2=0{,}75$.
(c) Wartości własne $\mathcal{E}(\rho_0)-\rho_0=\mathrm{diag}(-0{,}25,0{,}25)$, więc $D=0{,}25$.
Nierówność Fuchsa–van de Graafa: $1-\sqrt{0{,}75}=0{,}134\le0{,}25\le\sqrt{0{,}25}=0{,}5$ ✓.

**PD-2.10.** (a) $\lvert S\rvert>2$ nie da się uzyskać żadnym klasycznym (LHV) opisem, więc silne
korelacje muszą pochodzić ze splątania nieznanego Eve; brak naruszenia ($\le2$) sygnalizuje ingerencję.
(b) $\rho_{AB}=\frac12(\lvert00\rangle\langle00\rvert+\lvert11\rangle\langle11\rvert)$, $C(A,B)=0$.
(c) Monogamia: silne splątanie Alicji z Bobem ogranicza splątanie Alicji z Eve, więc wiedza Eve
o kluczu jest ograniczona — to fizyczna, a nie obliczeniowa, gwarancja bezpieczeństwa.