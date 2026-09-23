# 10. Kryptografia kwantowa


## 1. Zakres rozdziału

Rozdział obejmuje kryptografię kwantową (QKD): szyfr Vernama i doskonałą tajność, kryptografię
symetryczną i asymetryczną oraz protokoły BB84, B92 i E91. Omawia sifting, uzgadnianie klucza
i wzmocnienie prywatności, a także QBER jako miarę podsłuchu, ataki intercept-resend i PNS,
stany dekoy oraz różnicę między QKD a kryptografią postkwantową (PQC).

Bezpieczeństwo QKD opiera się na prawach fizyki — zakazie klonowania (rozdział 07)
i nierozróżnialności stanów nieortogonalnych — a nie na trudności obliczeniowej. Materiał
wykorzystuje pomiar w różnych bazach (rozdział 06) i stanowi odpowiedź na przewagę
algorytmu Shora (rozdział 08).

## 2. Najważniejsze definicje

- **Szyfr Vernama (one-time pad):** $c=m\oplus k$; **doskonała tajność** (perfect secrecy) przy
  losowym kluczu $k$ tej samej długości co wiadomość $m$, użytym raz.
- **Kryptografia symetryczna:** ten sam klucz do szyfrowania i odszyfrowania.
- **Kryptografia asymetryczna (public key):** klucz publiczny i prywatny (np. RSA, ECC).
- **BB84:** protokół QKD z użyciem dwóch baz (Z: $\lvert0\rangle,\lvert1\rangle$; X: $\lvert+\rangle,\lvert-\rangle$).
- **B92:** protokół z dwoma nieortogonalnymi stanami ($\lvert0\rangle$, $\lvert+\rangle$).
- **E91:** protokół oparty na splątaniu i teście CHSH.
- **QBER (quantum bit error rate):** odsetek błędów w przesłanym kluczu.
- **Sifting:** uzgodnienie, które bity wchodzą do klucza (zgodne bazy).
- **Uzgadnianie klucza (reconciliation):** korekcja błędów (cascade, LDPC).
- **Wzmocnienie prywatności (privacy amplification):** skrócenie klucza do części wolnej od informacji podsłuchującego.
- **Atak PNS (photon-number splitting):** dzielenie liczby fotonów przez Eve; przeciwdziałanie — **stany dekoy (decoy states)**.
- **PQC (post-quantum cryptography):** algorytmy klasyczne odporne na komputery kwantowe.

## 3. Teoria krok po kroku

### 3.1 Szyfr Vernama i doskonała tajność

Szyfrujemy bit po bicie $c_i=m_i\oplus k_i$. **Twierdzenie Shannona:** jeśli klucz $k$ jest losowy,
tak samo długi jak $m$ i użyty tylko raz, to kryptogram $c$ jest **statystycznie niezależny** od $m$ —
podsłuchujący, nawet z nieograniczoną mocą obliczeniową, nie dowie się niczego (perfect secrecy).
**Problem:** jak bezpiecznie uzgodnić klucz? Kanał klasyczny może być podsłuchiwany. Właśnie tu wchodzi QKD.

### 3.2 Kryptografia symetryczna a asymetryczna

W kryptografii **symetrycznej** obie strony mają ten sam klucz. W **asymetrycznej** (RSA, ECC)
szyfruje się kluczem publicznym, a odszyfrowuje prywatnym. Bezpieczeństwo RSA opiera się na trudności
faktoryzacji, ECC — na logarytmie dyskretnym. **Algorytm Shora** (rozdział 08) łamie oba te problemy,
więc cała infrastruktura publiczna wymaga wymiany na **PQC** albo **QKD**. QKD rozwiązuje *wymianę
klucza* symetrycznego w sposób bezwarunkowo bezpieczny (fizycznie), a nie *obliczeniowo* trudny.

### 3.3 Protokół BB84 krok po kroku

Alicja i Bob dysponują klasycznym (publicznym, podsłuchiwalnym) kanałem oraz **kwantowym** kanałem
(pojedyncze fotony). Cztery stany kodują dwa bity — jeden „bit klucza” i jedną „bazę”:

| Bit | Baza | Stan | Uwaga |
| --- | --- | --- | --- |
| 0 | Z | $\lvert0\rangle$ | biegun północny sfery Blocha |
| 1 | Z | $\lvert1\rangle$ | biegun południowy |
| 0 | X | $\lvert+\rangle=\frac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)$ | równik, $\varphi=0$ |
| 1 | X | $\lvert-\rangle=\frac{1}{\sqrt2}(\lvert0\rangle-\lvert1\rangle)$ | równik, $\varphi=\pi$ |

**Przebieg:**
1. **Przygotowanie.** Alicja losuje bit $b_i$ i bazę $\beta_i\in\{Z,X\}$, wysyła stan $\lvert b_i\rangle_{\beta_i}$.
2. **Pomiar.** Bob losuje własną bazę $\beta_i'$ i mierzy; gdy $\beta_i'=\beta_i$, odczytuje $b_i$ poprawnie;
   gdy $\beta_i'\ne\beta_i$, wynik jest losowy.
3. **Sifting.** Publicznie porównują **tylko bazy** (nie bity!). Bity z $\beta_i\ne\beta_i'$ odrzucają.
4. **Test podsłuchu.** Ujawniają losową próbkę uzgodnionych bitów i liczą **QBER**. Jeśli $>$ próg
   (typowo $\sim11\%$), przerywają.
5. **Uzgadnianie i wzmocnienie prywatności.** Poprawiają resztę błędów i kompresują klucz, by usunąć
   informację Eve.

**Przykład przebiegu (8 bitów, 0 = baza Z, 1 = baza X):**

| $i$ | bit $b_i$ | baza Alicji | baza Boba | zgodne? | w kluczu |
| --- | --- | --- | --- | --- | --- |
| 0 | 1 | Z | Z | tak | 1 |
| 1 | 0 | X | X | tak | 0 |
| 2 | 1 | Z | X | nie | — |
| 3 | 1 | Z | Z | tak | 1 |
| 4 | 0 | X | X | tak | 0 |
| 5 | 0 | X | Z | nie | — |
| 6 | 1 | Z | Z | tak | 1 |
| 7 | 0 | Z | X | nie | — |

Po siftingu zostaje $5$ bitów ($1,0,1,0,1$); 3 odrzucono. Oczekiwany „plon” to $\tfrac12$ bitów.

### 3.4 Protokół B92

B92 używa **dwóch** nieortogonalnych stanów: $\lvert0\rangle$ (bit 0) i $\lvert+\rangle$ (bit 1).
Bob losowo mierzy w bazie $Z$ albo $X$, ale akceptuje tylko wyniki **konkluzywne**:
- pomiar w $Z$ dający $1$ $\Rightarrow$ Alicja wysłała $\lvert+\rangle$ (bo $\lvert0\rangle$ nigdy nie da $1$);
- pomiar w $X$ dający $\lvert-\rangle$ $\Rightarrow$ Alicja wysłała $\lvert0\rangle$.

Wyniki niekonkluzywne odrzuca się. B92 ma niższy plon niż BB84, ale prostszą implementację.
Bezpieczeństwo też opiera się na nieortogonalności ($\lvert\langle0\vert+\rangle\rvert^2=\tfrac12$).

### 3.5 Protokół E91 (splątanie)

Alicja i Bob dzielą pary w stanie $\lvert\Psi^-\rangle$. Każde mierzy w losowo wybranym kierunku;
część wyników służy do uzgodnienia klucza, a część — do **testu CHSH**. Zmierzona wartość $\lvert S\rvert>2$
potwierdza, że korelacje są kwantowe (rozdział 09), a więc kanał nie jest w rękach klasycznego
podsłuchującego. E91 wiąże bezpieczeństwo QKD z **monogamią splątania**.

### 3.6 Podsłuch „intercept-resend” i QBER

Najprostszy atak: Eve przechwytuje foton, mierzy go w losowej bazie i wysyła Bobowi stan, który
zmierzyła (**intercept-resend**). Policzmy błąd. Eve wybiera właściwą bazę z prawdopodobieństwem
$\tfrac12$. Jeśli trafi (prawd. $\tfrac12$), odtworzy stan bezbłędnie. Jeśli nie trafi ($\tfrac12$),
wysyła stan w złej bazie; Bob mierzy go w swojej (właściwej) bazie i z prawdopodobieństwem $\tfrac12$
odczyta zły bit. Zatem

$$\text{QBER}=\underbrace{\tfrac12}_{\text{Eve pudłuje}}\cdot\underbrace{\tfrac12}_{\text{Bob myli się}}=\tfrac14=25\%.$$

Bez podsłuchu QBER $\approx0$ (tylko szum kanału). Przekroczenie progu $\sim11\%$ oznacza, że Eve
ma za dużo informacji; protokół zostaje przerwany. To są **statystyczne dowody podsłuchu**.

### 3.7 Sifting, uzgadnianie klucza i wzmocnienie prywatności

- **Sifting** — zostawiamy bity z zgodnych baz (oczekiwany plon $50\%$).
- **Uzgadnianie (reconciliation)** — korekcja błędów resztkowych (algorytm kaskadowy, kody LDPC);
  ujawnia się przy tym dodatkowe bity (syndromy), co powiększa wiedzę Eve.
- **Wzmocnienie prywatności (privacy amplification)** — uniwersalne haszowanie skraca klucz tak, by
  informacja Eve była $<10^{-9}$ bitu. Końcowa długość to $l\approx n\big(1-H_2(\text{QBER})\big)-$ poprawki.

### 3.8 Zakaz klonowania jako podstawa bezpieczeństwa

Eve **nie może** skopiować nieznanego stanu (rozdział 07, sekcja 3.2). Skoro nie może wykonać kopii
„na zapas”, każdy jej pomiar zaburza stan — a zaburzenie objawia się jako dodatkowy QBER. To
odróżnia QKD od klasycznej wymiany Diffiego–Hellmana, gdzie podsłuch *jest* teoretycznie możliwy,
tylko obliczeniowo trudny do wykorzystania. Dodatkowo **nierozróżnialność** nieortogonalnych stanów
oznacza, że Eve nie odczyta bitu bez ryzyka błędu.

### 3.9 Ataki praktyczne

- **PNS (photon-number splitting).** Źródła słabych impulsów czasem emitują $>1$ foton; Eve blokuje
  jeden i zachowuje drugi, nie wprowadzając błędów. Obrona: **stany dekoy (decoy states)** — wysyłanie
  impulsów o losowanej intensywności i porównywanie statystyk.
- **Blinding (oślepianie detektorów).** Eve silnym światłem „steruje” lawinowymi fotodetektorami
  Boba, wymuszając wyniki. Obrona: detektory z monitorowaniem liczby fotonów, QKD bez detektorów
  po stronie odbiorcy (MDI-QKD).
- **Trojan-horse.** Eve wysyła do nadajnika Alicji sondę i odbiera jej odbicie. Obrona: filtry
  widmowe, izolatory, optyczne opóźnienia.
- **Ataki na kanał klasyczny** (mitm na autoryzacji) — obrona: autoryzacja kanału z jawnym kluczem.

### 3.10 Praktyczne QKD

Realne realizacje: światłowody (zasięg do $\sim100$–$500$ km) lub łącza satelitarne (Micius, 2017).
Tempo klucza: kbps–Mbps. Inżynierskie aspekty: **stany dekoy**, **QKD niezależne od
detektora (MDI-QKD)**, **TF-QKD** (twisted/dizzy — przekroczenie granicy liniowej), synchronizacja.
W Polsce infrastrukturę i eksperymenty prowadzi **PCSS (Poznańskie Centrum Superkomputerowo-Sieciowe)**,
a komputery kwantowe buduje m.in. **IQM** (Finlandia) — pojawiają się one jako partnerzy warsztatów
i projektów (rozdział 12).

### 3.11 QKD a PQC (post-quantum cryptography)

| Aspekt | QKD | PQC |
| --- | --- | --- |
| Typ bezpieczeństwa | fizyczne (bezwarunkowe) | obliczeniowe |
| Sprzęt | kanał kwantowy (fotony) | tylko klasyczny komputer |
| Odporność na Shora | tak (z zasady) | zakładana (brak dowodu) |
| Zasięg | ograniczony (światłowód/satelita) | nieograniczony (Internet) |
| Dojrzałość | niszowe wdrożenia | standaryzacja NIST (2024) |

PQC (np. kratowe KYBER/DILITHIUM) **uzupełnia**, a nie zastępuje QKD: działa na dzisiejszym Internecie,
ale opiera się na nieudowodnionych założeniach. QKD daje gwarancję z zasad fizyki, ale wymaga dedykowanej
infrastruktury.

## 4. Przykłady rozwiązane

### Przykład 1: prawdopodobieństwa pomiaru w BB84

**Dane.** Alicja wysyła stan $\lvert-\rangle=\frac{1}{\sqrt2}(\lvert0\rangle-\lvert1\rangle)$ (bit 1 w bazie X).
Bob mierzy w bazie $Z$ lub $X$.

**Metoda.** $P(m)=\lvert\langle m\vert-\rangle\rvert^2$ dla stanów $\lvert0\rangle,\lvert1\rangle$
(baza Z) oraz $\lvert+\rangle,\lvert-\rangle$ (baza X).

**Rachunek.** Baza Z: $\langle0\vert-\rangle=\frac{1}{\sqrt2}$, $\langle1\vert-\rangle=-\frac{1}{\sqrt2}$,
więc $P(0)=P(1)=\frac12$ — pomiar **nie daje informacji** o bicie (zła baza). Baza X:
$\langle+\vert-\rangle=0$, $\langle-\vert-\rangle=1$, więc $P(-)=1$ — pomiar **pewny** (dobra baza).

**Wynik.** **Zła baza: $P(0)=P(1)=\tfrac12$; dobra baza: $P(-)=1$.**

**Interpretacja.** Zgodność baz jest niezbędna do odczytania bitu; przy niezgodnych bazach wynik jest
losowy. To czyni sifting naturalnym i chroni bity przed ujawnieniem (Bob nie zgadnie bitu, gdy
bazy się różnią).

### Przykład 2: podsłuch intercept-resend i długość klucza

**Dane.** Kanał BB84, Eve wykonuje intercept-resend na każdym fotonie. W siftingu zostaje $n=1000$ bitów;
mierzony QBER wynosi $e$.

**Metoda.** Z sekcji 3.6 wiemy, że intercept-resend daje $e=25\%$. Uproszczona formuła
bezpiecznego klucza (Shor–Preskill) to $r=1-2H_2(e)$ bitów na bit siftowanego klucza.

**Rachunek.** $H_2(0{,}25)=-0{,}25\log_2 0{,}25-0{,}75\log_2 0{,}75=0{,}5+0{,}3113=0{,}8113$ bita.
Zatem $r=1-2\cdot0{,}8113=-0{,}623<0$. Długość klucza: $l=r\cdot n<0$, czyli **brak klucza**.
Dla porównania próg $r=0$ występuje, gdy $H_2(e)=\tfrac12$, tj. $e\approx11{,}0\%$.

**Wynik.** Intercept-resend daje **QBER $=25\%$**, dla którego $r=1-2H_2(0{,}25)\approx-0{,}62$ —
klucz jest niemożliwy; **próg bezpieczeństwa to $e\approx11\%$**.

**Interpretacja.** Atak Eve jest wykrywalny, bo podnosi QBER aż do poziomu, przy którym żaden
bezpieczny klucz nie powstanie. To pokazuje, że QKD nie polega na „wychwyceniu” Eve, lecz na tym, że
jej informacja **odbiera** możliwość uzgodnienia sekretu — sam atak staje się samobójczy.

## 5. Typowe pułapki

1. **Porównywanie bitów, nie tylko baz, na kanale publicznym.** Ujawnienie bitów niszczy klucz;
   porównujemy *bazy*, a bity tylko w małej próbce testowej.
2. **Mylenie QBER z „szumem”.** QBER $>11\%$ oznacza realny podsłuch (lub poważny szum) i przerwanie protokołu.
3. **Sądzenie, że QKD „szyfruje dane”.** QKD generuje *klucz*; szyfrowanie robi się potem (np. Vernam).
4. **Zapominanie o autoryzacji kanału.** Bez autoryzacji kanału klasycznego możliwy jest atak mitm.
5. **Ignorowanie ataków sprzętowych.** Idealny model BB84 nie opisuje PNS, blindingu czy trojan-horse.
6. **Utożsamianie QKD z PQC.** To dwie różne odpowiedzi na komputery kwantowe.
7. **Zły plon.** Oczekiwany plon siftingu to $\tfrac12$, nie całość; do tego dochodzą straty kanału.

## 6. Zadania (Z-10)

**Z-10.1.** BB84 — pomiary.
(a) Alicja wysyła $\lvert+\rangle$; podaj $P(0),P(1)$ przy pomiarze w bazie $Z$ i $P(+),P(-)$ w bazie $X$.
(b) Dla 12 bitów o losowych bazach oszacuj oczekiwaną liczbę bitów po siftingu.
(c) Uzasadnij, dlaczego ujawnienie bitów (nie tylko baz) przed siftingiem zniszczyłoby klucz.

**Z-10.2.** B92.
(a) Zapisz dwa stany używane w B92 i wskaż, że są nieortogonalne.
(b) Alicja wysyła $\lvert0\rangle$; jakie wyniki Boba są **konkluzywne**?
(c) Policz prawdopodobieństwo wyniku konkluzywnego przy losowym wyborze bazy przez Boba.

**Z-10.3.** Intercept-resend.
(a) Wyprowadź QBER $=25\%$ dla ataku intercept-resend.
(b) Policz $H_2(0{,}25)$ i oceń, czy możliwy jest klucz.
(c) Wyznacz próg QBER, przy którym $1-2H_2(e)=0$.

**Z-10.4.** Szyfr Vernama.
(a) Zapisz szyfrowanie i odszyfrowanie.
(b) Uzasadnij, dlaczego klucz musi być losowy, tak długi jak wiadomość i użyty raz.
(c) Pokaż na przykładzie 2-bitowym, że ponowne użycie klucza ujawnia XOR wiadomości.

**Z-10.5.** E91 i CHSH.
(a) Opisz rolę stanu $\lvert\Psi^-\rangle$ w E91.
(b) Jak zmierzona wartość $\lvert S\rvert$ wpływa na zaufanie do kanału?
(c) Wyjaśnij związek z monogamią splątania (rozdział 09).

**Z-10.6. [★]** Stany dekoy i PNS.
(a) Wyjaśnij, jak Eve wykorzystuje impulsy wielofotonowe (PNS).
(b) W jaki sposób losowe intensywności impulsów (stany dekoy) ujawniają PNS?
(c) Zaproponuj prosty test statystyczny wykrywający PNS.

## 7. Wskazówki do zadań

- **Z-10.1.** W (a) użyj $\lvert\langle m\vert+\rangle\rvert^2$; w (b) pomnóż $12\cdot\tfrac12$.
- **Z-10.2.** W (b) konkluzywny jest tylko wynik nieosiągalny dla drugiego stanu; w (c) $\tfrac12\cdot\tfrac12$.
- **Z-10.3.** W (a) rozbij na „Eve trafia bazę” i „Bob myli się”; w (c) rozwiąż $H_2(e)=0{,}5$.
- **Z-10.4.** W (c) zapisz $c_1=m_1\oplus k$, $c_2=m_2\oplus k$ i dodaj stronami.
- **Z-10.5.** W (b) $\lvert S\rvert>2$ wyklucza klasycznego podsłuchującego; w (c) monogamia ogranicza korelacje Eve.
- **Z-10.6.** W (a) Eve mierzy jedną kopię, przepuszcza drugą; w (b) porównaj plon dla intensywności sygnałowej i dekoy.

## 8. Co dalej

- **Metrologia kwantowa** — [rozdział 11](11-metrologia-kwantowa.md).
- **Realizacje komputerów kwantowych** — [rozdział 12](12-realizacje-komputerow-kwantowych.md): PCSS, IQM.
- **Korekcja błędów** — [rozdział 13](13-korekcja-i-mitygacja-bledow.md).
- **Algorytmy zaawansowane i granice** — [rozdział 19](19-ponad-program-algorytmy-zaawansowane-i-granice.md):
  teleportacja, tw. Holevo.
- Pełne rozwiązania: [zadania/rozwiazania/rozwiazania-10.md](../zadania/rozwiazania/rozwiazania-10.md).
- Praca domowa: [PD-2](../praca-domowa/praca-domowa-02.md).
