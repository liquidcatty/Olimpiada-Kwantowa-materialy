# Rozwiązania do rozdziału 12

## Z-12.1

(a) Pięć kryteriów DiVincenzy:
1. skalowalne fizyczne kubity o dobrze zdefiniowanych dwupoziomowych stanach,
2. możliwość inicjalizacji do znanego stanu (np. $\lvert0\ldots0\rangle$),
3. czasy koherencji znacznie dłuższe od czasu bramki ($T_2\gg t_g$),
4. uniwersalny zbiór bramek (dowolna bramka jednokubitowa + jedna dwukubitowa),
5. pomiar pojedynczego kubita.

(b) **Annealer D-Wave** nie spełnia kryterium (4): nie realizuje dowolnego obwodu, tylko
ewolucję do stanu podstawowego **hamiltonianu Isinga**
$H=\sum_i h_i\sigma_z^{(i)}+\sum_{ij}J_{ij}\sigma_z^{(i)}\sigma_z^{(j)}$.
Kryterium (5) jest spełnione tylko częściowo — odczytujemy końcową konfigurację spinów,
a nie dowolny kubit w dowolnym momencie obliczeń. Kryteria (1)–(3) są spełnione.

(c) **Centrum NV** spełnia doskonale (2) (inicjalizacja optyczna), (3) ($T_2$ do ms przy echu,
bramki $\sim$10–100 ns, czyli $T_2/t_g\sim10^5$) oraz (5) (odczyt optyczny w temperaturze
pokojowej!). Fundamentalny problem to **(1)**: sprzężenie dwóch centrów NV maleje wykładniczo
z odległością, a odległości nie da się dowolnie zmniejszać — defekty wbudowuje się w sieć
krystaliczną, więc nie da się zbudować dużej tablicy silnie sprzężonych spinów.

**Odpowiedź:** (a) jak wyżej; (b) brak uniwersalności (4) i pełnego pomiaru pośredniego (5);
(c) NV: (2), (3), (5) bez zarzutu, problem ze skalowalnym sprzężeniem (1).

*Fizycznie:* kryteria DiVincenzy oddzielają „fizykę kubitu” (2, 3, 5) od „inżynierii
systemu” (1, 4) — większość współczesnych trudności leży właśnie w skalowaniu.

## Z-12.2

(a) Liczba bramek w czasie koherencji:
$$\frac{T_2}{t_g}=\frac{200\ \mu\text{s}}{50\ \text{ns}}=\frac{2\cdot10^{-4}}{5\cdot10^{-8}}=4000 .$$

(b) Po $n$ bramkach sukces $\approx F^n$ z $F=0{,}998$:
$$0{,}998^{500}=0{,}368\ (36{,}8\%),\qquad 0{,}998^{5000}=4{,}49\cdot10^{-5}\ (\approx0{,}004\%).$$

(c) $0{,}998^n=0{,}5\Rightarrow n=\frac{\ln0{,}5}{\ln0{,}998}=\frac{-0{,}6931}{-0{,}002002}=346{,}2$,
czyli **po 347 bramkach**.

**Odpowiedź:** (a) $\mathbf{4000}$ bramek; (b) $\mathbf{36{,}8\%}$ i $\mathbf{4{,}5\cdot10^{-5}}$;
(c) $\mathbf{347}$ bramek.

*Fizycznie:* nawet przy wierności $99{,}8\%$ (bardzo dobrej!) „połowa” algorytmu przepada
po $\sim350$ bramkach — dlatego w praktyce skraca się obwody (transpilacja, optymalizacja)
i stosuje mitygację (rozdział 13).

## Z-12.3

(a) Transmon: $T_2/t_g=150\ \mu\text{s}/60\ \text{ns}=2500$. Jon: $T_2/t_g=1\ \text{s}/200\ \mu\text{s}=5000$.
Jon wygrywa „budżetem bramek” dwukrotnie, choć każda jego bramka jest $\approx3000\times$ dłuższa.

(b) Dla $n=200$ bramek dwukubitowych:
$$0{,}997^{200}=0{,}548\ (54{,}8\%)\ \text{(transmon)},\qquad
0{,}999^{200}=0{,}819\ (81{,}9\%)\ \text{(jon)} .$$

(c) Dla $10^3$ bramek: transmon $0{,}997^{1000}=0{,}050$, jon $0{,}999^{1000}=0{,}368$.
**Wybór: jon**, jeśli liczy się wierność końcowa (ponad siedmiokrotnie wyższe
prawdopodobieństwo sukcesu), oraz **transmon**, jeśli liczy się szybkość zbierania
statystyki (obwód $10^3$ bramek to $60$ µs wobec $0{,}1$ s — przy $1000$ powtórzeniach
odpowiednio $60$ ms i $100$ s). Dla algorytmu o głębokości $10^3$ bramek obie technologie
wymagają już korekcji błędów.

**Odpowiedź:** (a) $2500$ (transmon) i $5000$ (jon); (b) $\mathbf{54{,}8\%}$ i $\mathbf{81{,}9\%}$;
(c) jon dla wierności ($\mathbf{36{,}8\%}$ vs $5{,}0\%$), transmon dla szybkości ($60$ µs vs $0{,}1$ s).

*Fizycznie:* to ten sam kompromis co w przykładzie 12.2 — „dokładnie i wolno” kontra
„szybko i z błędem”; sensowny wybór zależy od stosunku czasu bramki do czasu koherencji,
a nie od samej liczby kubitów.

## Z-12.4

(a) Odległość $d=6$ (w bramkach) wymaga $d=6$ SWAP-ów, a każdy SWAP to $3$ CNOT:
$$6\cdot3=18\ \text{CNOT}.$$

(b) Łączna wierność „transportu”: $0{,}997^{18}=0{,}947$ (czyli $94{,}7\%$), podczas gdy
pojedynczy CNOT miałby $99{,}7\%$ — koszt odległości to $5{,}3$ punktu procentowego wierności.

(c) W obwodzie ze $100$ dalekimi bramkami wykonamy $100\cdot12=1200$ bramek dwukubitowych
zamiast $100$ — **$12\times$ więcej**. Wierność całego obwodu spada z $0{,}997^{100}=0{,}740$
do $0{,}997^{1200}=0{,}027$ (z $74\%$ do $2{,}7\%$).

**Odpowiedź:** (a) $\mathbf{18}$ CNOT; (b) $F=\mathbf{0{,}947}$; (c) $\mathbf{12\times}$ więcej
bramek ($1200$ zamiast $100$), wierność obwodu $2{,}7\%$ zamiast $74\%$.

*Fizycznie:* łączność sprzętu zamienia się bezpośrednio w wierność — dlatego planując obwód
na kracie 2D, układa się bramki tak, by angażowały sąsiadów; robi to transpilator (rozdział 15).

## Z-12.5

(a) **Wolumetryka kwantowa (QV)** mierzy $2^n$, gdzie $n$ to największa głębokość kwadratowego
losowego obwodu, który urządzenie wykonuje poprawnie — w jednej liczbie mieści więc liczbę
kubitów, łączność i błędy. **XEB** mierzy, jak blisko ideału jest rozkład wyników losowych
obwodów: porównuje zmierzony rozkład z rozkładem idealnym (używa się jej w demonstracjach
„przewagi kwantowej”).

(b) Liczba kubitów **nie mówi nic** o wierności bramek ani o łączności. $1000$ kubitów w linii
z błędem $1\%$ na bramkę da wynik gorszy niż $50$ kubitów z błędem $10^{-4}$. Sensowne
porównanie wymaga miar „całościowych”: QV, EPLG, CLOPS oraz wierności bramek natywnych.

(c) CLOPS to liczba **warstw** obwodu na sekundę. Obwód o $20$ warstwach przy $5000$ CLOPS:
$$t=\frac{20}{5000}\ \text{s}=0{,}004\ \text{s}=\mathbf{4}\ \text{ms}.$$

**Odpowiedź:** (a) QV: zintegrowana jakość $2^n$; XEB: zgodność rozkładu z idealnym;
(b) liczba kubitów pomija wierności i łączność; (c) $\mathbf{4}$ ms.

*Fizycznie:* pojęcia „ile kubitów” i „jak dobry komputer” są rozłączne — dlatego
odpowiedzialne ogłoszenia podają kilka miar jednocześnie.

## Z-12.6

(a) **Dwa polskie systemy kwantowe:**
- ACK **Cyfronet AGH w Krakowie**: **IBM Quantum System One**, $27$ kubitów nadprzewodzących
  (układ Falcon), dostępny od 2023 r. dla polskich uczelni i jednostek naukowych przez chmurę.
- **PCSS** (Poznańskie Centrum Superkomputerowo-Sieciowe, Poznań): **IQM Garnet**,
  $20$ kubitów nadprzewodzących — pierwszy komercyjny system IQM zainstalowany u klienta;
  PCSS udostępnia go naukowcom i szkołom oraz prowadzi warsztaty i hackathony.

(b) Kroki od pomysłu do wyniku: (1) zapisanie obwodu w SDK (np. Qiskit); (2) wybór backendu
(przy braku wymagań — kolejka „least busy”); (3) **transpilacja** do bramek natywnych
i łączności urządzenia; (4) ustawienie liczby powtórzeń (*shots*) i opcjonalnej mitygacji;
(5) wysłanie zadania (identyfikator *job*) i oczekiwanie w kolejce; (6) pobranie wyników
(liczniki, histogram, wartości oczekiwane); (7) analiza statystyczna i poprawki.

(c) **Kalibracja** dryfuje w czasie: częstotliwości kubitów, wierności bramek i błędy odczytu
mierzy się co kilka godzin, więc identyczne zadania wysłane w różnym momencie mogą dać różne
histogramy (i inny obwód po transpilacji). **Kolejkowanie** decyduje, na której kalibracji
pracujesz i z jakim szumem. W pracy raportujemy: nazwę urządzenia, liczbę shots, identyfikator
zadania, datę i godzinę, informację o użytej mitygacji — to warunek powtarzalności i wymóg
organizatora (rozdział 14).

**Odpowiedź:** (a) Cyfronet/IBM $27$ kubitów; PCSS/IQM $20$ kubitów; (b) obwód → backend →
transpilacja → shots → job → wyniki → analiza; (c) kalibracja i kolejka wpływają na szum oraz
na transpilację, więc raportujemy metadane uruchomienia.

*Fizycznie:* komputer kwantowy jest **urządzeniem pomiarowym, które dryfuje** — jego parametry
zmieniają się z czasem, a wynik trzeba podawać razem z warunkami, w jakich go uzyskano.

> **Weryfikacja numeryczna.** Wszystkie liczby policzono w NumPy: $200\,\mu\text{s}/50\,\text{ns}=4000$,
> $0{,}998^{500}=0{,}3675$, $0{,}998^{5000}=4{,}49\cdot10^{-5}$, $n(50\%)=346{,}2$;
> $150\,\mu\text{s}/60\,\text{ns}=2500$, $1\,\text{s}/200\,\mu\text{s}=5000$;
> $0{,}997^{200}=0{,}548$, $0{,}999^{200}=0{,}819$, $0{,}999^{1000}=0{,}368$;
> $0{,}997^{18}=0{,}947$, $0{,}997^{100}=0{,}740$, $0{,}997^{1200}=0{,}027$; $20/5000=4$ ms.

