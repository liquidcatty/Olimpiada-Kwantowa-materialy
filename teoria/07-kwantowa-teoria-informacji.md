# 07. Kwantowa teoria informacji


## 1. Zakres rozdziału

Rozdział opisuje różnice między informacją klasyczną a kwantową: zakaz klonowania, zakaz usuwania
oraz nierozróżnialność nieortogonalnych stanów pojedynczym pomiarem. Wprowadza miary ilościowe —
entropię von Neumanna, entropię Shannona, dystans śladowy, wierność (fidelity), granicę Helstroma
i ograniczenie Holevo — oraz kanały kwantowe w postaci Krausa.

Omawia supergęste kodowanie (wymagające wcześniej współdzielonego splątania), teleportację,
kryterium PPT i dekoherencję. Narzędzia te są wykorzystywane w kryptografii (rozdział 10),
algorytmach (rozdział 08), metrologii (rozdział 11) i przy granicach obliczeń (rozdział 19).

## 2. Najważniejsze definicje

- **Bit klasyczny:** $b\in\{0,1\}$; nosi 1 bit informacji.
- **Kubit:** stan $\lvert\psi\rangle=\alpha\lvert0\rangle+\beta\lvert1\rangle$, $\lvert\alpha\rvert^2+\lvert\beta\rvert^2=1$.
- **Entropia Shannona:** $H(p_1,\dots,p_n)=-\sum_i p_i\log_2 p_i$ (w bitach).
- **Entropia von Neumanna:** $S(\rho)=-\mathrm{Tr}(\rho\log_2\rho)=-\sum_i\lambda_i\log_2\lambda_i$,
  gdzie $\lambda_i$ to wartości własne $\rho$.
- **Kanał kwantowy (quantum channel):** odwzorowanie CPTP (completely positive, trace-preserving),
  $\rho\mapsto\mathcal{E}(\rho)$; zapis Krausa $\mathcal{E}(\rho)=\sum_k K_k\rho K_k^\dagger$,
  $\sum_k K_k^\dagger K_k=I$.
- **Dystans śladowy (trace distance):** $D(\rho,\sigma)=\frac12\mathrm{Tr}\lvert\rho-\sigma\rvert =\frac12\sum_i\lvert\lambda_i\rvert$, gdzie $\lambda_i$ to wartości własne $\rho-\sigma$.
- **Wierność (fidelity):** $F(\rho,\sigma)=\big(\mathrm{Tr}\sqrt{\sqrt\rho\,\sigma\sqrt\rho}\big)^2$.
- **POMV (POVM):** zbiór $\{E_i\}$, $E_i\succeq0$, $\sum_i E_i=I$; $P(i)=\mathrm{Tr}(E_i\rho)$.
- **Dekorherencja (decoherence):** utrata koherencji (wyzerowanie elementów pozadiagonalnych $\rho$)
  wskutek splątania z otoczeniem.

## 3. Teoria krok po kroku

### 3.1 Bit a kubit

Bit ma dwa *stany pewne*; kubit dopuszcza **superpozycję** $\alpha\lvert0\rangle+\beta\lvert1\rangle$.
Pozornie kubit „mieści nieskończenie wiele informacji” (para kątów $(\theta,\varphi)$ na sferze
Blocha), ale **odczyt** niszczy superpozycję: pomiar w bazie $\{\lvert0\rangle,\lvert1\rangle\}$
zwraca tylko jeden bit. Faza $\varphi$ staje się dostępna dopiero przez **interferencję** (zestawienie
z inną operacją), a nie przez pomiar w ustalonej bazie.

### 3.2 Twierdzenie o zakazie klonowania (no-cloning)

**Twierdzenie.** Nie istnieje operacja unitarna $U$ i stan $\lvert A\rangle$ takie, że
$U(\lvert\psi\rangle\otimes\lvert0\rangle\otimes\lvert A\rangle)=\lvert\psi\rangle\otimes\lvert\psi\rangle\otimes\lvert A_\psi\rangle$
dla wszystkich $\lvert\psi\rangle$.

**Dowód.** Załóżmy, że $U$ klonuje (przy ustalonym otoczeniu $\lvert A\rangle$) i pomińmy otoczenie.
Wtedy dla stanów bazowych $U\lvert0\rangle\lvert0\rangle=\lvert00\rangle$ oraz
$U\lvert1\rangle\lvert0\rangle=\lvert11\rangle$. Z liniowości $U$ dla superpozycji
$\lvert+\rangle=\frac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)$ dostajemy

$$
U\lvert+\rangle\lvert0\rangle=\frac{1}{\sqrt2}\big(U\lvert00\rangle+U\lvert10\rangle\big)
=\frac{1}{\sqrt2}\big(\lvert00\rangle+\lvert11\rangle\big)=\lvert\Phi^+\rangle.
$$

Ale klonowanie wymagałoby $U\lvert+\rangle\lvert0\rangle=\lvert+\rangle\lvert+\rangle =\frac{1}{2}(\lvert00\rangle+\lvert01\rangle+\lvert10\rangle+\lvert11\rangle)$, co nie jest równe
$\lvert\Phi^+\rangle$ (inne amplitudy). Sprzeczność kończy dowód. $\blacksquare$

**Wniosek.** Klonować można tylko stany **wzajemnie ortogonalne** (np. $\lvert0\rangle,\lvert1\rangle$) —
wtedy $\mathrm{CNOT}$ kopiuje stan bazowy na drugi kubit. Dla nieznanej superpozycji klonowanie
jest niemożliwe i to jest podstawa bezpieczeństwa QKD (rozdział 10).

### 3.3 Nierozróżnialność stanów nieortogonalnych

Dwa stany $\lvert\psi\rangle,\lvert\phi\rangle$ z $\lvert\langle\psi\vert\phi\rangle\rvert<1$ **nie są
jednoznacznie rozróżnialne** pojedynczym pomiarem. Powód: dowolny pomiar to POMV $\{E_i\}$; gdyby
rozróżniał je z pewnością, to z $\mathrm{Tr}(E_0\lvert\psi\rangle\langle\psi\rvert)=1$ i tego samego
dla $\lvert\phi\rangle$ mielibyśmy $E_0\lvert\psi\rangle=\lvert\psi\rangle$ i
$E_0\lvert\phi\rangle=\lvert\phi\rangle$, więc oba leżałyby w jednej podprzestrzeni własnej —
musiałyby być ortogonalne. **Optymalny** błąd dla dwóch stanów o równych prawdopodobieństwach
(granica Helstroma) to

$$
p_{\text{błąd}}=\tfrac12\Big(1-\sqrt{1-\lvert\langle\psi\vert\phi\rangle\rvert^2}\Big).
$$

Dla $\lvert0\rangle$ i $\lvert+\rangle$: $\lvert\langle0\vert+\rangle\rvert^2=\frac12$, stąd
$p_{\text{błąd}}=\frac12(1-\frac{1}{\sqrt2})\approx0{,}146$, czyli rozpoznajemy poprawnie w $\approx85{,}4\%$.

### 3.4 Twierdzenie o zakazie usuwania (no-deleting)

**Twierdzenie.** Nie istnieje unitary $U$ z $U\lvert\psi\rangle\lvert\psi\rangle=\lvert\psi\rangle\lvert0\rangle$
dla wszystkich $\lvert\psi\rangle$ (nie da się skasować jednej kopii, zostawiając drugą).

**Dowód.** Z $U\lvert00\rangle=\lvert00\rangle$, $U\lvert11\rangle=\lvert10\rangle$ i
$U\lvert++\rangle=\lvert+0\rangle$ oraz z liniowości:
$U\lvert++\rangle=\frac12(\lvert00\rangle+U\lvert01\rangle+U\lvert10\rangle+\lvert10\rangle)$.
Porównując z $\lvert+0\rangle=\frac{1}{\sqrt2}(\lvert00\rangle+\lvert10\rangle)$ dostajemy
$U\lvert01\rangle+U\lvert10\rangle=(\sqrt2-1)(\lvert00\rangle+\lvert10\rangle)$. Prawa strona to
niezerowy wektor w $\mathrm{span}\{\lvert00\rangle,\lvert10\rangle\}$; lewa to suma obrazów stanów
ortogonalnych do $\lvert00\rangle,\lvert11\rangle$, więc sama jest ortogonalna do tego $\mathrm{span}$
— czyli musi być zerem. Sprzeczność. $\blacksquare$

### 3.5 Entropia Shannona i von Neumanna

Dla rozkładu prawdopodobieństwa $H(p)=-\sum_i p_i\log_2 p_i$; dla stanu $\rho$ entropia von Neumanna
$S(\rho)=-\mathrm{Tr}(\rho\log_2\rho)$. **Związek:** entropia von Neumanna stanu diagonalnego
$\rho=\mathrm{diag}(p)$ to dokładnie $H(p)$, a entropia wyników dowolnego pomiaru spełnia
$H(\{p_i\})\le S(\rho)$ — pomiar nie może *zwiększyć* dostępnej informacji, a równość zachodzi gdy
mierzymy w bazie własnej $\rho$. Własności: $S(\rho)=0$ dla stanu czystego, $S(\frac12 I)=1$ bit,
$S$ jest wklęsła, $S(\rho_A)=S(\rho_B)$ dla stanu czystego dwóch układów. Użyteczne liczby:
$S(\frac12 I)=1$, $H(0{,}5)=1$, $H(0{,}1)\approx0{,}469$ bit.

### 3.6 Kanały kwantowe (zarys)

Ewolucja otwartego układu nie jest unitarna — opisuje ją kanał CPTP. Kanoniczny przykład:
**kanał depolaryzujący** (*depolarizing channel*)

$$
\mathcal{E}(\rho)=(1-p)\,\rho+p\,\frac{I}{2},
$$

który z prawdopodobieństwem $p$ zamienia stan na maksymalnie mieszany. Inne: bit-flip ($X\rho X$),
phase-flip ($Z\rho Z$), kanał amplitudowy (relaksacja). Pełny formalizm (tw. Krausa, reprezentacja
Stinespringa, ślad częściowy) rozwija [rozdział 17](17-ponad-program-macierze-gestosci-i-kanaly.md).

### 3.7 Dystans śladowy

$D(\rho,\sigma)=\frac12\sum_i\lvert\lambda_i\rvert$ mierzy „odległość” stanów. Własności:
$0\le D\le1$, $D(\rho,\sigma)=\max_{\{E_i\}}\big\lvert P_\rho(E_i)-P_\sigma(E_i)\big\rvert$ —
przewaga w rozróżnianiu najlepszym pomiarem — oraz **kontraktywność** pod działaniem kanału:
$D(\mathcal{E}(\rho),\mathcal{E}(\sigma))\le D(\rho,\sigma)$. Przykład: dla $\lvert0\rangle$ i
$\lvert+\rangle$ mamy $D=\frac{1}{\sqrt2}\approx0{,}707$.

### 3.8 Wierność (fidelity)

$F(\rho,\sigma)=\big(\mathrm{Tr}\sqrt{\sqrt\rho\,\sigma\sqrt\rho}\big)^2$; dla stanów czystych
$F=\lvert\langle\psi\vert\phi\rangle\rvert^2$. Własności: $0\le F\le1$, $F(\rho,\sigma)=1\iff\rho=\sigma$,
symetria $F(\rho,\sigma)=F(\sigma,\rho)$, wklęsłość w każdym argumencie. Nierówność
Fuchsa–van de Graafa wiąże oba pojęcia:

$$
1-\sqrt{F(\rho,\sigma)}\le D(\rho,\sigma)\le\sqrt{1-F(\rho,\sigma)}.
$$

Dla $\lvert0\rangle,\lvert+\rangle$: $F=\frac12$, więc $D\in[0{,}293,\,0{,}707]$ — i faktycznie
$D=0{,}707$, czyli górne ograniczenie jest tu osiągnięte (co zachodzi dla pary stanów czystych).

### 3.9 Kwantowa informacja Fishera

Klasyczna informacja Fishera $F(\theta)=\sum_i\frac{1}{p_i}(\partial_\theta p_i)^2$ wyznacza dolne
ograniczenie wariancji estymatora (nierówność Craméra–Rao $\Delta\theta\ge1/\sqrt{\nu F}$). Kwantowy
odpowiednik $F_Q(\theta)$ opisuje *najlepszy możliwy* pomiar; dla stanu czystego
$F_Q=4\big(\langle\partial_\theta\psi\vert\partial_\theta\psi\rangle-\lvert\langle\psi\vert\partial_\theta\psi\rangle\rvert^2\big)$.
Przykład: dla $\lvert\psi_\theta\rangle=\cos\frac\theta2\lvert0\rangle+\sin\frac\theta2\lvert1\rangle$
dostajemy $F_Q=1$ (granica śrutowa), a dla $N$ splątanych kubitów w stanie GHZ $F_Q=N$
(granica Heisenberga). Szczegóły w [rozdziale 11](11-metrologia-kwantowa.md).

### 3.10 Ograniczenie Holevo

Dla zespołu stanów $\{p_i,\rho_i\}$ dostępna informacja klasyczna nie przekracza **wielkości Holevo**

$$
\chi=S\Big(\sum_i p_i\rho_i\Big)-\sum_i p_i\,S(\rho_i)\ \le\ S(\rho)\ \le\ \log_2 d.
$$

Dla jednego kubita ($d=2$) zawsze $\chi\le1$ bit. Interpretacja: $n$ kubitów przenosi **co najwyżej
$n$ bitów** informacji klasycznej, niezależnie od kodowania. Dla zespołu BB84
($\tfrac14$ na każdy z $\lvert0\rangle,\lvert1\rangle,\lvert+\rangle,\lvert-\rangle$) średni stan
to $\tfrac12 I$, więc $\chi=1-0=1$ bit — nasycenie.

### 3.11 Supergęste kodowanie

Z **wcześniej współdzielonym** splątaniem $\lvert\Phi^+\rangle$ nadajemy i wysyłamy tylko **jeden**
kubit, a przekazujemy **dwa** bity. Alicja wykonuje jedną z czterech operacji na swoim kubicie:

$$
I\to\lvert\Phi^+\rangle,\quad X\to\lvert\Psi^+\rangle,\quad Z\to\lvert\Phi^-\rangle,\quad iY\to\lvert\Psi^-\rangle.
$$

Następnie wysyła swój kubit do Boba, który dekoduje obwodem $\mathrm{CNOT}$ (kontrola = kubit Boba)
i $H$ na kubicie Boba, po czym mierzy oba. **Nie łamie** to ograniczenia Holevo — 2 bity wymagają
2 „nośników”: wysłanego kubita i kubita już posiadanego.

### 3.12 Teleportacja (krótko)

Teleportacja przenosi **nieznany** stan $\lvert\psi\rangle$ przy użyciu splątania i 2 bitów
klasycznych; stan odtwarzany jest na drugim końcu, a oryginał ulega zniszczeniu (pomiar Alice) —
więc nie łamie zakazu klonowania. Pełny rachunek w [rozdziale 19](19-ponad-program-algorytmy-zaawansowane-i-granice.md).

### 3.13 Kryterium PPT (zapowiedź)

Dla stanu dwuczęściowego $\rho_{AB}$ **transpozycja częściowa** $\rho^{T_B}$ (transpozycja tylko po
kubicie $B$) dla stanów **separowalnych** jest zawsze półokreślona dodatnio (dodatnia transpozycja,
positive partial transpose, PPT). Zatem $\rho^{T_B}$ ma ujemną wartość własną $\Rightarrow$ stan
jest **splątany**. Wniosek (Peres): kryterium PPT jest konieczne, a dla $2\times2$ i $2\times3$ również
wystarczające. Przykład — stan Wernera $\rho_W=p\lvert\Phi^+\rangle\langle\Phi^+\rvert+\frac{1-p}{4}I$
jest splątany dokładnie dla $p>\frac13$. Rozwinięcie: [rozdział 09](09-splatanie-i-twierdzenie-bella.md).

### 3.14 Pomiary POMV

Pomiar rzutowy to szczególny przypadek POMV z $E_i=\lvert m_i\rangle\langle m_i\rvert$. Ogólnie
$E_i\succeq0$, $\sum_i E_i=I$, ale $E_i$ nie muszą być rzutami ani ortonormalne — pozwalają
optymalnie rozróżniać stany nieortogonalne (kosztem niedokładności) i realizować pomiary
„niezupełne” (inconclusive). Każdy POMV można zrealizować pomiarem rzutowym na rozszerzonym układzie
(tw. Neumarka).

### 3.15 Dekoherencja a informacja

Gdy stan splątuje się z otoczeniem, elementy pozadiagonalne $\rho$ maleją: $\rho_{ij}\to\rho_{ij}e^{-\gamma t}$.
Po czasie koherencji informacja fazowa „wycieka” do otoczenia i — nawet jeśli jest *zapisana* —
staje się praktycznie niedostępna. To tłumaczy, dlaczego przejście kwantowe$\to$klasyczne widzimy
jako utratę informacji (formalnie: zanik splątania, [rozdziały 13](13-korekcja-i-mitygacja-bledow.md) i
[18](18-ponad-program-splatanie-dekoherencja-termodynamika.md)). Miary splątania i entropie są
narzędziami, które to ilościowo opisują.

## 4. Przykłady rozwiązane

### Przykład 1: wielkość Holevo dla zespołu BB84

**Dane.** Zespół czterech stanów z jednakowymi prawdopodobieństwami $p_i=\tfrac14$:

$$
\rho_1=\lvert0\rangle\langle0\rvert,\ \rho_2=\lvert1\rangle\langle1\rvert,\
\rho_3=\lvert+\rangle\langle+\rvert,\ \rho_4=\lvert-\rangle\langle-\rvert.
$$

**Metoda.** $\chi=S(\bar\rho)-\sum_i p_i S(\rho_i)$, gdzie $\bar\rho=\sum_i p_i\rho_i$.

**Rachunek.** Każdy $\rho_i$ jest stanem czystym, więc $S(\rho_i)=0$. Średni stan:

$$
\bar\rho=\tfrac14\Big(\lvert0\rangle\langle0\rvert+\lvert1\rangle\langle1\rvert+\lvert+\rangle\langle+\rvert+\lvert-\rangle\langle-\rvert\Big).
$$

Ponieważ $\lvert+\rangle\langle+\rvert+\lvert-\rangle\langle-\rvert=I$, dostajemy
$\bar\rho=\tfrac14\big((\lvert0\rangle\langle0\rvert+\lvert1\rangle\langle1\rvert)+I\big)=\tfrac12 I$.
Entropia: $S(\tfrac12 I)=-\big(\tfrac12\log_2\tfrac12+\tfrac12\log_2\tfrac12\big)=1$ bit. Zatem
$\chi=1-0=1$ bit.

**Wynik.** **$\chi=1$ bit** — z jednego kubita można wycisnąć najwyżej 1 bit klasyczny.

**Interpretacja.** To nasycenie ograniczenia Holevo. Cztery nieortogonalne stany z BB84 *nie* kodują
2 bitów: mimo „czterech możliwości” pojedynczy pomiar nie odróżni ich wszystkich naraz. Dlatego BB84
nadaje 1 bit na kubit (a dodatkowo połowę odrzucamy przy siftingu).

### Przykład 2: supergęste kodowanie — 2 bity przez 1 kubit

**Dane.** Alicja i Bob dzielą $\lvert\Phi^+\rangle=\frac{1}{\sqrt2}(\lvert00\rangle+\lvert11\rangle)$
(kubit Alicji = $q_0$, Boba = $q_1$). Alicja chce przesłać 2 bity i wysyła **tylko** swój kubit.

**Metoda.** Alicja wykonuje na $q_0$ jedną z operacji $I,X,Z,iY$; powstaje jeden ze stanów Bella.
Bob dekoduje: $\mathrm{CNOT}$ (kontrola $q_1$, cel $q_0$), potem $H$ na $q_1$, potem pomiar obu.

**Rachunek.** Stany po operacji Alicji (działanie $U\otimes I$ na $\lvert\Phi^+\rangle$):

$$
I:\ \lvert\Phi^+\rangle,\quad X:\ \lvert\Psi^+\rangle,\quad Z:\ \lvert\Phi^-\rangle,\quad iY:\ \lvert\Psi^-\rangle.
$$

Dekodowanie: każdy stan Bella przechodzi w stan bazowy:

$$
\lvert\Phi^+\rangle\to\lvert00\rangle,\ \lvert\Psi^+\rangle\to\lvert01\rangle,\
\lvert\Phi^-\rangle\to\lvert10\rangle,\ \lvert\Psi^-\rangle\to\lvert11\rangle.
$$

Np. dla $I$: $\mathrm{CNOT}\lvert\Phi^+\rangle=\frac{1}{\sqrt2}(\lvert00\rangle+\lvert10\rangle)$;
następnie $H$ na $q_1$ daje $(H\otimes I)\,\frac{1}{\sqrt2}(\lvert0\rangle+\lvert1\rangle)\lvert0\rangle=\lvert00\rangle$.

**Wynik.** Parom bitów $(00,01,10,11)$ odpowiadają operacje $(I,X,Z,iY)$; **Bob odczytuje 2 bity
klasyczne**, choć Alicja wysłała 1 kubit.

**Interpretacja.** „Magia” pochodzi z wcześniej współdzielonego splątania — zasobu, który trzeba było
wytworzyć (i przesłać) uprzednio. Formalnie wysłany kubit + posiadany kubit to 2 nośniki, więc granica
Holevo ($n$ kubitów $\le n$ bitów) nie jest naruszona.

## 5. Typowe pułapki

1. **„Kubit niesie nieskończenie dużo informacji”.** Nie: nieznanego stanu nie da się odczytać, a
   dostępna informacja to $\le1$ bit (Holevo).
2. **Mylenie entropii von Neumanna z Shannona.** $S(\rho)$ liczy się z wartości własnych $\rho$,
   nie z amplitud; logarytm o podstawie 2 daje bity.
3. **Zakaz klonowania dotyczy *nieznanego* stanu.** Klonowanie stanu znanego (np. wiadomej $\lvert0\rangle$)
   jest trywialne i dozwolone.
4. **Nierozróżnialność a „zły detektor”.** To nie kwestia technologii: nieortogonalne stany są
   nierozróżnialne *z zasady* (granica Helstroma $>0$).
5. **Utożsamianie $F$ z $D$.** To różne miary; wiąże je nierówność Fuchsa–van de Graafa.
6. **Sądzenie, że supergęste kodowanie łamie Holevo.** Wymaga współdzielonego splątania; bez niego
   1 kubit $=$ 1 bit.
7. **Zapominanie o „nieznanym” w teleportacji.** Teleportacja niszczy oryginał — dlatego nie klonuje.

## 6. Zadania (Z-07)

**Z-07.1.** Zakaz klonowania.
(a) Sformułuj twierdzenie o zakazie klonowania.
(b) Przeprowadź dowód dla stanów $\lvert0\rangle,\lvert1\rangle,\lvert+\rangle$.
(c) Wyjaśnij, dlaczego klonowanie stanów $\lvert0\rangle$ i $\lvert1\rangle$ jest możliwe, a $\lvert+\rangle$ nie.

**Z-07.2.** Rozróżnianie stanów.
(a) Uzasadnij, że stany nieortogonalne nie są jednoznacznie rozróżnialne.
(b) Policz optymalne prawdopodobieństwo poprawnego rozróżnienia $\lvert0\rangle$ i $\lvert+\rangle$ (granica Helstroma).
(c) Wyjaśnij, jak wynik z (b) uzasadnia bezpieczeństwo BB84 wobec podsłuchu.

**Z-07.3.** Entropie.
(a) Policz $S$ dla stanu czystego $\lvert+\rangle$ oraz dla $\rho=\frac12 I$.
(b) Policz $H(p)$ dla $p=0{,}5$ i $p=0{,}1$; porównaj.
(c) Uzasadnij nierówność $H(\text{pomiar})\le S(\rho)$ na przykładzie $\rho=\mathrm{diag}(0{,}5,0{,}5)$
mierzonego w bazie $X$.

**Z-07.4.** Dystans śladowy i wierność.
(a) Policz $D(\lvert0\rangle,\lvert+\rangle)$.
(b) Policz $F(\lvert0\rangle,\lvert+\rangle)$.
(c) Sprawdź nierówność Fuchsa–van de Graafa dla tej pary.

**Z-07.5.** Holevo i supergęste kodowanie.
(a) Policz $\chi$ dla zespołu $\{\tfrac12\!:\!\lvert0\rangle,\ \tfrac12\!:\!\lvert+\rangle\}$.
(b) Wyjaśnij, dlaczego supergęste kodowanie daje 2 bity, mimo że $\chi\le1$ na kubit.
(c) Podaj dwa warunki wstępne, które musi spełnić supergęste kodowanie.

**Z-07.6. [★]** Kanał depolaryzujący.
(a) Zapisz działanie kanału depolaryzującego na $\lvert0\rangle\langle0\rvert$ i podaj wynikowe $\rho$.
(b) Policz $F\big(\mathcal{E}(\lvert0\rangle\langle0\rvert),\lvert0\rangle\langle0\rvert\big)$ jako funkcję $p$.
(c) Dla jakiego $p$ wierność spada do $\frac34$? Zinterpretuj wynik.

## 7. Wskazówki do zadań

- **Z-07.1.** W (b) skorzystaj z liniowości $U$ i porównaj $\lvert\Phi^+\rangle$ z $\lvert+\rangle\lvert+\rangle$;
  w (c) przypomnij, że $\lvert+\rangle$ to nieznana superpozycja.
- **Z-07.2.** W (b) użyj wzoru Helstroma z $\lvert\langle0\vert+\rangle\rvert^2=\frac12$; w (c) połącz
  z (a) — Eve nie może skopiować, więc wprowadza błędy.
- **Z-07.3.** W (b) licz w logarytmie dwójkowym; w (c) pomiar w bazie $X$ na $\frac12 I$ daje wyniki $50/50$.
- **Z-07.4.** W (b) dla stanów czystych $F=\lvert\langle\psi\vert\phi\rangle\rvert^2$; podstaw liczby do wzoru.
- **Z-07.5.** W (a) policz średni stan i jego entropię; w (b) wskaż, że w protokole uczestniczą dwa nośniki.
- **Z-07.6.** W (a) podstaw $\rho=\lvert0\rangle\langle0\rvert$; w (b) $\lvert0\rangle$ jest stanem własnym kanału.

## 8. Co dalej

- **Algorytmy kwantowe** — [rozdział 08](08-algorytmy-kwantowe.md).
- **Splątanie** — [rozdział 09](09-splatanie-i-twierdzenie-bella.md).
- **Kryptografia** — [rozdział 10](10-kryptografia-kwantowa.md).
- **Metrologia** — [rozdział 11](11-metrologia-kwantowa.md): informacja Fishera i granica Heisenberga.
- **Kanały i macierze gęstości** — [rozdział 17](17-ponad-program-macierze-gestosci-i-kanaly.md).
- Pełne rozwiązania: [zadania/rozwiazania/rozwiazania-07.md](../zadania/rozwiazania/rozwiazania-07.md).
- Praca domowa: [PD-2](../praca-domowa/praca-domowa-02.md).

