# Rozwiązania do rozdziału 13

## Z-13.1

(a) Kod $\lbrack\!\lbrack3,1,3\rbrack\!\rbrack$: stabilizatory $S_1=Z_1Z_2$, $S_2=Z_2Z_3$
(kolejność małoendianowa $\lvert q_2q_1q_0\rangle$; $q_1$ jest „środkowym” kubitem).
Tabela syndromów: brak błędu $\to(0,0)$; $X$ na $q_2\to(1,0)$; $X$ na $q_1\to(1,1)$;
$X$ na $q_0\to(0,1)$.

(b) $\lvert\psi_L\rangle=\frac{1}{\sqrt2}(\lvert000\rangle+\lvert111\rangle)$, błąd $X$ na $q_2$
(dolnym w zapisie $q_2q_1q_0$ nie jest — $q_2$ to **starszy** bit, czyli trzeci kubit).
Po błędzie: $\frac{1}{\sqrt2}(\lvert100\rangle+\lvert011\rangle)$. Wartości $\sigma_z$:
$z(b)=+1$ dla $b=0$, $-1$ dla $b=1$, więc
- $\lvert100\rangle$: $q_2=1,q_1=0,q_0=0$: $Z_{q_2}Z_{q_1}=(-1)(+1)=-1$, $Z_{q_1}Z_{q_0}=(+1)(+1)=+1$;
- $\lvert011\rangle$: $q_2=0,q_1=1,q_0=1$: $Z_{q_2}Z_{q_1}=(+1)(-1)=-1$, $Z_{q_1}Z_{q_0}=(-1)(-1)=+1$.
Syndrom $(1,0)$ $\Rightarrow$ poprawka $X$ na $q_2$.

(c) Błędy $X$ na $q_0$ i $q_1$ dają syndrom $(1,0)$ — identyczny jak pojedynczy $X$ na $q_2$.
Kod „poprawi” więc $q_2$, zamieniając $\alpha\lvert011\rangle+\beta\lvert100\rangle$ na
$\alpha\lvert111\rangle+\beta\lvert000\rangle=\alpha\lvert1\rangle_L+\beta\lvert0\rangle_L$,
czyli wprowadzi **błąd logiczny $X_L$**. Kod naprawia tylko jeden błąd ($d=3\Rightarrow t=1$).

**Odpowiedź:** (a) $(0,0),(1,0),(1,1),(0,1)$; (b) syndrom $\mathbf{(1,0)}$, poprawka $X$ na $q_2$;
(c) syndrom $(1,0)$, ale „poprawka” daje błąd logiczny — kod nie radzi sobie z dwoma błędami.

*Fizycznie:* syndrom identyfikuje *przypuszczenie* o błędzie o najmniejszej wadze; przy dwóch
błędach to przypuszczenie jest błędne i kod pogarsza sytuację zamiast ją naprawić.

## Z-13.2

(a) Kanał depolaryzujący $\mathcal{E}(\rho)=(1-p)\rho+\frac p3(X\rho X+Y\rho Y+Z\rho Z)$ można
zapisać jednym parametrem $p_d=\frac{4p}{3}$ jako $\mathcal{E}(\rho)=(1-p_d)\rho+p_d\frac{I}{2}$.

(b) Dla stanu czystego $\langle X\rangle^2+\langle Y\rangle^2+\langle Z\rangle^2=1$, więc
$$F=\langle\psi\rvert\mathcal{E}(\lvert\psi\rangle\langle\psi\rvert)\lvert\psi\rangle
=(1-p)+\frac p3=\left(1-\frac{4p}{3}\right)+\frac{4p}{3}\cdot\frac12=1-\frac{2p}{3}=1-\frac{p_d}{2}.$$
Dla $p=0{,}05$: $F=1-0{,}0333=\mathbf{0{,}9667}$ (i $p_d=0{,}0667$, $1-p_d/2=0{,}9667$ ✓).

(c) Kolejne kanały mnożą wierność: $F^n=(0{,}9667)^n$. Warunek $0{,}9667^n<0{,}9$:
$$n>\frac{\ln0{,}9}{\ln0{,}9667}=\frac{-0{,}1054}{-0{,}0339}=3{,}11\ \Rightarrow\ n=4 .$$

**Odpowiedź:** (a) jak wyżej; (b) $F=\mathbf{0{,}9667}$ (zgodne z $1-p_d/2$);
(c) po $\mathbf{4}$ kanałach ($0{,}9667^3=0{,}903$, $0{,}9667^4=0{,}873$).

*Fizycznie:* kanał depolaryzujący działa jednakowo na wszystkie stany, więc wierność maleje
wykładniczo, a nie zależy od wybranego stanu logicznego — to najwygodniejszy model szumu
w analizie korekcji.

## Z-13.3

(a) $P_{\rm fail}=3p^2(1-p)+p^3=3p^2-2p^3$.
- $p=0{,}01$: $P=3\cdot10^{-4}-2\cdot10^{-6}=2{,}98\cdot10^{-4}$.
- $p=0{,}1$: $P=3\cdot0{,}01-2\cdot0{,}001=0{,}028$.

(b) Współczynnik poprawy $p/P_{\rm fail}$: $0{,}01/2{,}98\cdot10^{-4}=33{,}6\times$ oraz
$0{,}1/0{,}028=3{,}57\times$.

(c) Kod przestaje pomagać, gdy $P_{\rm fail}=p$:
$$3p^2-2p^3=p\ \Rightarrow\ 2p^2-3p+1=0\ \Rightarrow\ (2p-1)(p-1)=0
\ \Rightarrow\ p=\tfrac12\ \text{lub}\ p=1 .$$
Poniżej $p=\frac12$ kod zawsze zmniejsza prawdopodobieństwo błędu.

**Odpowiedź:** (a) $\mathbf{2{,}98\cdot10^{-4}}$ i $\mathbf{0{,}028}$; (b) $\mathbf{33{,}6\times}$
i $\mathbf{3{,}6\times}$; (c) próg $\mathbf{p=1/2}$.

*Fizycznie:* korzyść z kodu jest największa przy małym $p$ (bo $P_{\rm fail}\propto p^2$) —
dlatego wszystkie praktyczne kody wymagają błędu fizycznego znacznie poniżej progu.

## Z-13.4

(a) Generatory kodu Steane'a (kubity $q_1$–$q_7$), każdy o wadze $4$:
$$X_4X_5X_6X_7,\quad X_2X_3X_6X_7,\quad X_1X_3X_5X_7,\quad
Z_4Z_5Z_6Z_7,\quad Z_2Z_3Z_6Z_7,\quad Z_1Z_3Z_5Z_7 .$$
Komutują, bo każde dwa mają **parzystą** liczbę wspólnych kubitów ($0,2$ lub $4$).

(b) Syndrom błędu $X$ liczymy z generatorów $Z$-owych, a błędu $Z$ — z $X$-owych:
- $X$ na $q_5$: tylko $g_4$ ($Z_4Z_5Z_6Z_7$) i $g_6$ ($Z_1Z_3Z_5Z_7$) zawierają $q_5$,
  więc syndrom to $101$ — binarny zapis liczby $5$;
- $Z$ na $q_3$: $g_2$ ($X_2X_3X_6X_7$) i $g_3$ ($X_1X_3X_5X_7$) zawierają $q_3$: syndrom $011$
  — binarny zapis liczby $3$.

(c) Sześć generatorów daje $2^6=64$ klas syndromów. Błędów jednostkowych rozróżnialnych jest
$1$ (brak) $+7\cdot3=22$ (siedem kubitów razy $X,Y,Z$), a więc w $64$ klasach mieści się ich
z zapasem; wymiar przestrzeni $2^7=128$ podzielony przez $64$ daje $2$ wymiar podprzestrzeni kodu ✓.

**Odpowiedź:** (a) jak wyżej (każdy o wadze 4, komutujące); (b) $X$ na $q_5$: $\mathbf{101}$;
$Z$ na $q_3$: $\mathbf{011}$; (c) $2^{\,n-k}=\mathbf{64}$ klasy wobec $22$ błędów jednostkowych.

*Fizycznie:* struktura Hamminga sprawia, że syndrom *jest* numerem winnego kubitu (jak system
binarny parzystości w kodach klasycznych) — widzimy działanie klasycznego kodu $[7,4,3]$
„przeniesionego” na kubity.

## Z-13.5

(a) Kod powierzchniowy o dystansie $d$ używa $2d^2-1$ kubitów fizycznych na jeden logiczny:
- $d=5$: $2\cdot25-1=49$,
- $d=7$: $2\cdot49-1=97$.

(b) Dwadzieścia kubitów logicznych o $d=7$: $20\cdot97=1940$ kubitów fizycznych (plus kubity
pomiarowe są już wliczone w $2d^2-1$).

(c) Każdy krok $d\to d+2$ zmniejsza $p_L$ o czynnik $\Lambda=2{,}14$. Potrzebujemy
$$\Lambda^{k}=\frac{0{,}00143}{10^{-6}}=1430\ \Rightarrow\ k=\frac{\ln1430}{\ln2{,}14}=9{,}55,$$
czyli $d\approx7+2\cdot9{,}55=26{,}1$ — bierzemy najbliższy nieparzysty dystans $\mathbf{d=27}$
($1457$ kubitów fizycznych na kubit logiczny).

**Odpowiedź:** (a) $\mathbf{49}$ i $\mathbf{97}$; (b) $\mathbf{1940}$; (c) $\mathbf{d=27}$
($1457$ kubitów na kubit logiczny).

*Fizycznie:* poprawa jest wykładnicza w $d$, ale koszt rośnie jak $d^2$ — stąd „złoty środek”
między rozmiarem a dokładnością i ogromne liczby kubitów potrzebne do praktycznych zadań
(RSA-2048: $\approx2\cdot10^7$).

## Z-13.6

(a) Dopasowanie prostej $E(\lambda)=E(0)+a\lambda$ do $(1;0{,}90)$, $(2;0{,}79)$, $(3;0{,}68)$:
$$a=\frac{E(3)-E(1)}{3-1}=\frac{0{,}68-0{,}90}{2}=-0{,}11,\qquad
E(0)=E(1)-a=0{,}90+0{,}11=1{,}01 .$$
Wynik $E(0)=1{,}01>1$ jest **niemożliwy** dla wartości oczekiwanej operatora o widmie $[-1,1]$,
co sygnalizuje, że model liniowy jest zbyt prosty (albo dane mają fluktuacje) — w praktyce
należałoby użyć modelu wykładniczego lub $E(\lambda)=E(0)+a\lambda+b\lambda^2$.

(b) Odwracanie $\vec p_{\rm popr}=A^{-1}\vec p_{\rm zmierz}$ jest tym mniej stabilne, im
większa liczba warunkowa $\mathrm{cond}(A)$: błąd pomiaru $\delta$ daje błąd wyniku
$\approx\mathrm{cond}(A)\cdot\delta$. Gdy np. $P(1\mid0)\to0{,}3$ i $P(0\mid1)\to0{,}3$,
kolumny $A$ stają się niemal równoległe, $\mathrm{cond}(A)\to\infty$, a poprawki wychodzą
**ujemne** i muszą być rzutowane na sympleks (traci się wtedy część korekty). Pomaga
kalibracja na więcej niż dwóch stanach bazowych i regularyzacja.

(c) Połączenie: (i) zbieramy wyniki dla $\lambda=1,2,3$ (ZNE) w jednym przebiegu na tym samym
urządzeniu, (ii) do każdego punktu stosujemy poprawkę macierzy kalibracji (odczyt), (iii) na
końcu odrzucamy shots łamiące symetrię obwodu (postselekcja) i dopiero wtedy dopasowujemy
$E(\lambda)$ oraz ekstrapolujemy do $\lambda=0$. Ograniczenia: ZNE mnoży liczbę obwodów
(3 punkty $\times$ dodatkowe „składanie” bramek), postselekcja odbiera statystykę
(czynnik $\sqrt2$ przy odrzuceniu połowy), a macierz kalibracji traci stabilność przy dużym
szumie. Wszystkie trzy metody poprawiają **wartość oczekiwaną**, ale żadna nie daje skalowania
korekcji błędów.

**Odpowiedź:** (a) $E(0)=\mathbf{1{,}01}$ (nieco powyżej $1$ — model liniowy niedoskonały);
(b) winna jest liczba warunkowa $\mathrm{cond}(A)$ rosnąca przy dużym szumie;
(c) kalibracja + postselekcja + ZNE; koszt: więcej obwodów i mniej statystyki.

*Fizycznie:* mitygacja to statystyka i algebra liniowa nałożone na zaszumiony eksperyment —
skuteczna przy płytkich obwodach i dobrym sprzęcie, ale nie zastępuje kubitów logicznych.

> **Weryfikacja numeryczna.** Syndromy i tabele policzono macierzami Pauliego w NumPy:
> brak błędu $(0,0)$; $X$ na $q_2,q_1,q_0$: $(1,0),(1,1),(0,1)$; syndromy kodu Steane'a równe
> binarnym numerom kubitów; $F=0{,}9667$, $(0{,}9667)^4=0{,}873$ i $n=3{,}11$;
> $3p^2-2p^3$ dla $p=0{,}01,0{,}1,0{,}02$; $2d^2-1$; $k=9{,}55$ kroków $\Lambda=2{,}14$;
> ZNE $E(0)=1{,}01$. Skrypt: `python kod/korekcja_3bit.py`.

