# Rozwiązania do rozdziału 10

## Z-10.1

(a) Dla $\lvert+\rangle=\frac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)$:
w bazie $Z$: $P(0)=\lvert\langle0\vert+\rangle\rvert^2=\frac12$, $P(1)=\frac12$;
w bazie $X$: $P(+)=\lvert\langle+\vert+\rangle\rvert^2=1$, $P(-)=0$.

(b) Bity przechodzą sifting, gdy bazy się zgadzają — oczekiwane $\frac12$ z $12$ bitów, czyli
$12\cdot\frac12=6$ bitów.

(c) Bob (i Eve) znaliby wtedy bity **przed** wyborem próbki testowej; porównanie ujawniłoby cały klucz,
a Eve nie musiałaby nawet mierzyć stanów. Dlatego publicznie porównuje się wyłącznie **bazy**, a bity —
jedynie w małej próbce do estymacji QBER (i te bity są odrzucane).

**Odpowiedź:** (a) $\frac12,\frac12$ oraz $1,0$; (b) $6$; (c) ujawnienie bitów niszczy klucz.

*Fizycznie:* sifting „odsiewa” tylko niezgodne bazy, nie ujawniając samych bitów.

## Z-10.2

(a) Stany $\lvert0\rangle$ i $\lvert+\rangle$; iloczyn skalarny $\langle0\vert+\rangle=\frac{1}{\sqrt2}\ne0$,
więc są **nieortogonalne**.

(b) Alicja wysyła $\lvert0\rangle$: konkluzywny jest **pomiar w bazie $X$ dający $\lvert-\rangle$**
(wtedy bit $=0$). Pomiar w $Z$ dający $0$ jest niekonkluzywny ($\lvert+\rangle$ też może dać $0$), a wynik $1$
w $Z$ jest niemożliwy.

(c) Bob trafia w bazę $X$ z prawdopodobieństwem $\frac12$, a wtedy dostaje $\lvert-\rangle$ z prawdopodobieństwem
$\frac12$ (bo $\lvert0\rangle$ w bazie $X$ daje $50/50$). Zatem $P(\text{konkluzywny})=\frac12\cdot\frac12=\frac14$.

**Odpowiedź:** (a) $\lvert0\rangle,\lvert+\rangle$, nieortogonalne; (b) $X\to\lvert-\rangle$;
(c) $P=\frac14$.

*Fizycznie:* B92 osiąga bezpieczeństwo przy prostszej implementacji, ale niższym plonie (mniej wyników
konkluzywnych).

## Z-10.3

(a) Eve z prawdopodobieństwem $\frac12$ wybiera właściwą bazę (odtwarza stan bez błędu), a z $\frac12$
złą; wtedy Bob (we właściwej bazie) myli się z prawdopodobieństwem $\frac12$. Stąd

$$
\text{QBER}=\tfrac12\cdot\tfrac12=\tfrac14=25\%.
$$

(b) $H_2(0{,}25)=-0{,}25\log_2 0{,}25-0{,}75\log_2 0{,}75=0{,}5+0{,}3113=0{,}8113$ bita. Wtedy
$r=1-2H_2(0{,}25)=1-1{,}6226=-0{,}62<0$ — **klucz niemożliwy**.

(c) $1-2H_2(e)=0\Rightarrow H_2(e)=\frac12\Rightarrow e\approx0{,}11$, czyli QBER $\approx11\%$.

**Odpowiedź:** (a) $25\%$; (b) $H_2=0{,}811$, $r<0$ — brak klucza; (c) $e\approx11\%$.

*Fizycznie:* atak Eve jest wykryty, bo podnosi QBER powyżej progu, przy którym nie da się wyprowadzić
bezpiecznego klucza.

## Z-10.4

(a) Szyfrowanie: $c_i=m_i\oplus k_i$; odszyfrowanie: $m_i=c_i\oplus k_i$ (bo $\oplus$ jest odwracalne:
$c_i\oplus k_i=m_i$).

(b) **Losowość** — inaczej $c$ zdradza strukturę $m$; **długość** równa wiadomości — brak powtórzeń klucza;
**jednorazowość** — powtórzenie klucza pozwala wydedukować relacje między wiadomościami.

(c) Dwa kryptogramy z tym samym kluczem: $c_1\oplus c_2=(m_1\oplus k)\oplus(m_2\oplus k)=m_1\oplus m_2$.
Klucz się skraca, a $m_1\oplus m_2$ daje istotną informację o obu wiadomościach.

**Odpowiedź:** (a) $c=m\oplus k$, $m=c\oplus k$; (b) jak wyżej; (c) $c_1\oplus c_2=m_1\oplus m_2$.

*Fizycznie:* Vernam jest doskonale bezpieczny tylko przy rygorystycznym użyciu; QKD dostarcza właśnie
takiego jednorazowego, losowego klucza.

## Z-10.5

(a) E91 wykorzystuje pary splątane w stanie $\lvert\Psi^-\rangle$: pomiary na obu końcach dają idealnie
skorelowane (anty-korelowane) wyniki, które tworzą surowy klucz (po uzgodnieniu baz).

(b) Część par przeznacza się na **test CHSH**. Zmierzona wartość $\lvert S\rvert>2$ dowodzi, że korelacje
są kwantowe i nie da ich się odtworzyć klasycznym podsłuchem — zwiększa zaufanie do kanału. $\lvert S\rvert\le2$
sygnalizuje, że splątanie zostało zniszczone (podsłuch/szum).

(c) Monogamia splątania oznacza, że jeśli Alicja i Bob dzielą silne splątanie, Eve nie może być tak samo
splątana z ich kubitami — jej korelacje są ograniczone, co przekłada się na ograniczoną wiedzę o kluczu.

**Odpowiedź:** (a) pary $\lvert\Psi^-\rangle$ jako źródło klucza; (b) $\lvert S\rvert>2$ potwierdza
bezpieczeństwo, $\le2$ je podważa; (c) monogamia ogranicza korelacje Eve.

*Fizycznie:* E91 wiąże kryptografię kwantową z fundamentalnym testem Bella — bezpieczeństwo opiera się
na fizyce, nie na założeniach obliczeniowych.

## Z-10.6

(a) Źródło „słabych impulsów” czasem emituje $>1$ foton o tym samym stanie. Eve blokuje jeden foton,
a drugi zachowuje, by móc go zmierzyć **później** (po publicznym ujawnieniu baz) — nie wprowadzając
przy tym błędów.

(b) Alice losowo zmienia intensywność impulsów (sygnał vs. **decoy**). Statystyki plonu i QBER powinny być
takie same dla obu intensywności; PNS zmienia je różnie dla impulsów wielofotonowych, co ujawnia atak.

(c) Prosty test: policz **plon** ($Y$ = odsetek detekcji) i **QBER** osobno dla impulsów sygnałowych i dekoy.
Przy PNS plon/QBER dla dekoy będą istotnie różne niż dla sygnału — jeśli różnica przekracza fluktuacje
statystyczne, atak zostaje wykryty.

**Odpowiedź:** (a) Eve zachowuje nadmiarowy foton na później; (b) porównanie plonu/QBER dla losowanych
intensywności ujawnia PNS; (c) test statystyczny plonu i QBER dla sygnału vs dekoy.

*Fizycznie:* stany dekoy to standardowa obrona wdrożeniowa; zamieniają „idealny” model BB84 w protokół
odporny na realne słabe źródła fotonów.
