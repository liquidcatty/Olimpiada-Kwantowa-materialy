# 12. Realizacje komputerów kwantowych

> **Warsztat źródłowy:** „Realizacje komputerów kwantowych” (Grzegorz Czelusta, PCSS).
> **Czas nauki:** ~6 h teorii + ~6 h zadań.
> **Wymagana wiedza wstępna:** [05 — podstawy mechaniki kwantowej](05-podstawy-mechaniki-kwantowej.md), [06 — kubity, bramki, obwody, pomiary](06-kubity-bramki-obwody-pomiary.md), [07 — kwantowa teoria informacji](07-kwantowa-teoria-informacji.md), [09 — splątanie i twierdzenie Bella](09-splatanie-i-twierdzenie-bella.md).

## 1. Po co to jest

Rozdziały 06–10 opisywały obwody i algorytmy zakładając, że bramki są idealne. Ten rozdział
pokazuje, **z czego naprawdę robi się kubity**: nadprzewodzące obwody w 10 mK, pojedyncze
jony w pułapkach, atomy w pęsetach optycznych, fotony, centra barwne w diamencie, spiny
w krzemie. Okazuje się, że każda technologia to inny kompromis: szybkość kontra wierność,
liczba kubitów kontra łączność, temperatura pracy kontra koszt chłodzenia.

Ta wiedza jest na Olimpiadzie potrzebna z trzech powodów. Po pierwsze, pytania typu
„dlaczego kubity nadprzewodzące są w 10 mK?” albo „czym jest $T_1$ i $T_2$?” pojawiają się
w warsztatach i na finale. Po drugie, **realne zadania algorytmiczne i programistyczne**
(kod na IBM Quantum, IQM, chmurę PCSS) wymagają rozumienia transpilacji, kolejkowania zadań
i kalibracji. Po trzecie, to tu widać, dlaczego korekcja błędów (rozdział 13) jest
koniecznością, a nie ciekawostką: dzisiejsze bramki mają wierność $99{,}5\%$–$99{,}9\%$,
czyli 1000 bramek psuje algorytm z prawdopodobieństwem kilkudziesięciu procent.

> **Ponad program:** rozróżnienie NISQ i FTQC. *NISQ* (*noisy intermediate-scale quantum*,
> termin J. Preskilla z 2018 r.) to era 50–1000 fizycznych kubitów bez pełnej korekcji
> błędów: wyniki są „zaszumione”, a algorytmy muszą być płytkie. *FTQC* (*fault-tolerant
> quantum computing*) to era kubitów logicznych korygowanych kodami — pełne wersje algorytmu
> Shora czy symulacji chemii są możliwe dopiero tam.

## 2. Najważniejsze definicje

- **Kryteria DiVincenzy**: pięć warunków, które musi spełnić fizyczny układy, by dało się
  na nim zbudować uniwersalny komputer kwantowy (szczegóły w 3.1); dwa dodatkowe dotyczą
  przesyłania kubitów światłem.
- **Kubit fizyczny (physical qubit)**: realny układ dwupoziomowy (obwód LC z złączem
  Josephsona, jon, atom, foton, spin). **Kubit logiczny (logical qubit)**: zakodowana
  informacja, odporna na błędy (rozdział 13).
- **Czas relaksacji $T_1$**: stała czasu zaniku wzbudzenia $\lvert1\rangle\to\lvert0\rangle$;
  „jak długo kubit żyje”.
- **Czas koherencji $T_2$**: stała czasu zaniku superpozycji (faz); **$T_2^\ast$** to czas
  koherencji bez impulsów echa (z uwzględnieniem wolnozmiennego szumu), a **$T_2$ (echo)**
  z sekwencją odwracającą (Hahn echo, CPMG).
- **Czas bramki $t_g$**: czas trwania operacji; stosunek $T_2/t_g$ mówi, ile bramek zmieści
  się przed dekoherencją.
- **Wierność bramki (gate fidelity)** $F$: prawdopodobieństwo poprawnego działania bramki
  (dla bramek dwukubitowych podajemy zwykle medianę po parach kubitów); **błąd bramki**
  $\epsilon=1-F$.
- **Łączność (connectivity)**: które pary kubitów mogą wykonać bramkę dwukubitową;
  architektury: „linia” (1D), „krata” (2D grid), „gwiazda”, **all-to-all** (każdy z każdym).
- **Transpilacja**: przełożenie obwodu logicznego na obwód z bramek natywnych danego
  sprzętu, z uwzględnieniem łączności; **koszt transpilacji** mierzymy dodatkowymi
  bramkami SWAP (każdy SWAP $=3$ CNOT).
- **Bramka natywna (native gate)**: bramka realizowana fizycznie bez dekompozycji
  (np. $\sqrt{X}=SX$, $R_Z$, ECR, CZ, $i$SWAP, $x_{\pi/2}$).
- **Czas koherencji vs. wierność**: dwie różne miary „jakości” — można mieć wolne i dokładne
  bramki (jony) albo szybkie i mniej dokładne (transmon).
- **Kubit topologiczny (topological qubit)**: kubit, którego odporność na błędy wynika
  z topologii (nieabelowe anyony), a nie z korekcji zewnętrznej.
- **Benchmarki**: **XEB** (cross-entropy benchmarking), **wolumetryka kwantowa** (quantum
  volume, QV), **CLOPS** (circuit layer operations per second), EPLG (error per layered gate).
- **Przewaga kwantowa (quantum advantage / supremacy)**: wykonanie zadania, którego nie da
  się powtórzyć klasycznie w praktycznym czasie. **Przewaga praktyczna (practical/economic)**
  wymaga dodatkowo, by zadanie było *użyteczne*.

## 3. Teoria krok po kroku

### 3.1 Kryteria DiVincenzy

Aby fizyczny układ mógł być komputerem kwantowym, musi spełniać pięć warunków:

1. **Skalowalne kubity o dobrze zdefiniowanych stanach.** Dwa wyróżnione poziomy (kubit), powielalne w tysiącach egzemplarzy bez utraty kontroli nad parametrami. Przykład naruszenia: sprzężenie dwóch spinów musi być silne *i* kontrolowalne (dlatego centra NV trudno skalować, mimo świetnej koherencji).
2. **Inicjalizacja do znanego stanu** ($\lvert000\ldots0\rangle$): schłodzenie do stanu podstawowego (transmon w 10 mK praktycznie *jest* w $\lvert0\rangle$), pompowanie optyczne, chłodzenie laserowe.
3. **Długie czasy koherencji w porównaniu z czasem bramki**: $T_2\gg t_g$; potrzebujemy $T_2/t_g\gtrsim10^3$–$10^4$, inaczej algorytm „nie zdąży” się wykonać.
4. **Uniwersalny zbiór bramek**: bramka dwukubitowa (np. CNOT) plus obroty jednokubitowe o dowolny kąt (rozdział 06).
5. **Pomiar pojedynczego kubita** (dyspersyjny odczyt rezonatora, fluorescencja jonu, detekcja fotonów).

Dla komputerów **sieciowych** dochodzą dwa warunki: konwersja kubita stacjonarnego na
„latający” (foton) i wierne przesyłanie fotonów na duże odległości. **Skalowalność** to szósty,
nieoficjalny warunek: transmon mnoży się litograficznie (kolejne pętle na chipie), jony — przez
dodawanie pułapek i modułów optycznych, atomy — przez większe tablice, fotonika — przez
multipleksowanie źródeł i detektorów.

### 3.2 Jak opisuje się sprzęt — siedem liczb

| Parametr | Znaczenie | Typowe wartości |
| --- | --- | --- |
| liczba kubitów | ile fizycznych kubitów działa | $20$–$1121$ (nadprzewodzące), $20$–$60$ (jony) |
| $T_1$ | czas życia wzbudzenia | $50$–$300$ µs (transmon), $>1$ s (jony) |
| $T_2$ | czas koherencji fazy | $100$–$300$ µs (transmon), $0{,}1$–$10$ s (jony) |
| $t_g^{1\rm Q}$ | czas bramki jednokubitowej | $25$ ns (transmon), $10$–$30$ µs (jony) |
| $t_g^{2\rm Q}$ | czas bramki dwukubitowej | $30$–$70$ ns (transmon), $50$–$600$ µs (jony) |
| $F_{2\rm Q}$ | wierność bramki dwukubitowej | $99{,}5\%$–$99{,}9\%$ |
| łączność | kto z kim może wejść w bramkę | krata 2D, linia, all-to-all |

Reguła kciuka: **liczba bramek, jaką można wykonać, to $T_2/t_g$** — dzielimy „jak długo
kubit pamięta” przez „jak długo trwa operacja”. Dla transmona ($T_2=100$ µs, $t_g=68$ ns)
to $\approx1470$ bramek dwukubitowych; dla jonu ($T_2=1$ s, $t_g=100$ µs) to $10^4$ bramek —
choć jon jest *tysiące razy wolniejszy*. Oba warunki da się więc spełnić na dwa sposoby:
„szybko i krótko żyjący” (transmon) albo „wolno i długo żyjący” (jon).

Drugą kluczową liczbą jest **skumulowany błąd**. Jeśli bramka ma wierność $F$, to po $n$
bramkach prawdopodobieństwo, że obwód zadziała bez błędu, wynosi w przybliżeniu $F^n$:

| $F_{2\rm Q}$ | $n=100$ | $n=1000$ | $n=10^4$ |
| --- | --- | --- | --- |
| $99{,}9\%$ | $90\%$ | $37\%$ | $4{,}5\cdot10^{-5}$ |
| $99{,}7\%$ | $74\%$ | $5{,}0\%$ | $\approx0$ |
| $99{,}5\%$ | $61\%$ | $0{,}67\%$ | $\approx0$ |

Wniosek: **bez korekcji błędów algorytmy potrzebujące $10^4$+ bramek są bezużyteczne.**
Algorytm Shora dla RSA-2048 wymaga rzędów $10^9$ bramek $T$; przy wierności $99{,}7\%$
już po $10^6$ bramkach szansa sukcesu spada do $\approx10^{-1305}$ (bo
$0{,}997^{10^6}=e^{-3004{,}5}$).

### 3.3 Kubity nadprzewodzące

**Kubit nadprzewodzący** to sztuczny atom: obwód LC, w którym nieliniowość wnosi **złącze
Josephsona** (dwa nadprzewodniki rozdzielone cienką barierą izolatora). Nieliniowość jest
konieczna — bez niej poziomy obwodu LC byłyby równoodległe i nie dałoby się wybrać dwóch
z nich jako kubitu.

- **Transmon** (najpopularniejszy typ): ładunek jest „rozmyty” dzięki dużej pojemności
  bocznikującej ($E_J/E_C\approx50$), co czyni kubit odpornym na szum $1/f$ ładunku.
  Częstotliwość pracy $4$–$8$ GHz, anharmoniczność $200$–$300$ MHz.
- **Chłodzenie**: rozcieńczalnik (dilution refrigerator) do $\approx10$ mK. Przy 10 mK
  $k_BT/h\approx200$ MHz, więc obsadzenie stanu wzbudzonego jest pomijalne. Etapy chłodzenia:
  $50$ K → $4$ K → $1$ K → $100$ mK → $10$ mK.
- **Bramki**: impulsy mikrofalowe (1Q, $\approx25$ ns) i bramki dwukubitowe przez sprzężenie
  pojemnościowe lub przez rezonator (natywne: CZ, $i$SWAP, ECR; $30$–$70$ ns).
- **Odczyt**: dyspersyjny — kubit przesuwa częstotliwość rezonatora, mierzymy fazę odbitego
  sygnału (pomiar nierozdzielający; rozdziały 13 i 17).
- **Szum**: straty dielektryczne (TLS — *two-level systems* w tlenkach), szum strumienia
  magnetycznego $1/f$, kwazicząstki, a nawet promieniowanie kosmiczne (skoki $T_1$).
- **Systemy**: IBM (Eagle 127, Osprey 433, Condor 1121; obecnie rodzina Heron 133/156 kubitów
  w architekturze „heavy-hex”), Google (Sycamore 53, Willow 105), Rigetti (Ankaa-3, 84),
  IQM (20 i 54).

### 3.4 Jony w pułapkach

Pojedyncze jony ($^{171}\mathrm{Yb}^+$, $^{40}\mathrm{Ca}^+$, $^{88}\mathrm{Sr}^+$) unoszą się
w **pułapce Paula** (zmienne pole elektryczne) lub Penninga. Kubitem jest para poziomów
nadsubtelnych lub optycznych.

- **Zalety**: $T_1,T_2$ rzędu sekund (stany nadsubtelne, doskonała izolacja od otoczenia),
  wierność bramek 1Q $>99{,}99\%$, 2Q $99{,}5\%$–$99{,}9\%$, **łączność all-to-all**
  w łańcuchu — bramka angażuje wspólny mod ruchu, więc nie trzeba „przesuwać” informacji SWAP-ami.
- **Wady**: wolne bramki ($50$–$600$ µs), rozbudowana optyka (dziesiątki wiązek laserowych),
  trudne skalowanie poza łańcuch (rozwiązania: transport jonów „quantum CCD”, moduły
  połączone fotonami).
- **Bramka Mølmera–Sørensena (MS)**: impuls działający na oba jony jednocześnie; dzięki
  wspólnemu modowi fononowemu realizuje obrót kolektywny
  $R_{XX}(\theta)=\exp\left(-i\frac{\theta}{2}\sigma_x\otimes\sigma_x\right)$ — to natywna
  bramka dwukubitowa w tej technologii.
- **Systemy**: Quantinuum H1/H2 (20 i 56 kubitów), IonQ Forte; dostęp przez chmury
  (również z Polski).

### 3.5 Zimne atomy: sieci optyczne i pęsety

Neutralne atomy (Rb, Cs, Sr, Yb) chłodzone laserowo do µK. Kubit to dwa stany nadsubtelne
albo dwa poziomy Rydberga; oddziaływanie między atomami jest **przełączane światłem**.

- **Sieci optyczne** (optical lattices): atomy w periodycznym potencjale fali stojącej;
  architektura stosowana głównie w symulatorach kwantowych (model Hubbarda, rozdział 18).
- **Pęsety optyczne** (*optical tweezers*): pojedyncze atomy w ogniskach silnie skupionych
  wiązek, rozmieszczane w dowolnych tablicach 2D (do $1000$+ atomów). Świetna skalowalność
  i **rekonfigurowalna łączność** — atomy można fizycznie przemieszczać.
- **Bramka Rydberga**: wzbudzenie do stanu Rydberga ($n\approx50$–$100$) blokuje wzbudzenie
  sąsiada („blokada Rydberga”), co daje kontrolowane przesunięcie fazy; czasy $0{,}1$–$1$ µs,
  wierności $\approx99\%$–$99{,}9\%$.
- **Parametry**: koherencja $\sim$ms, życie atomu w pułapce $\sim10$ s.
- **Systemy**: QuEra (Aquila, 256 atomów; demonstracje kodów korekcyjnych na 48 kubitach
  logicznych), Pasqal (analogowy i cyfrowy, setki atomów), Atom Computing.

### 3.6 Fotonika, spiny i centra barwne

**Kubity fotonowe.** Kubitem jest polaryzacja, ścieżka albo obecność fotonu w dwóch modach. Zaleta: fotony nie dekoherują w spoczynku i łatwo je przesyłać (naturalne „latające” kubity, rozdział 10). Wada: brak bezpośredniego oddziaływania — bramki dwukubitowe wymagają interferencji, fotonów pomocniczych i pomiaru.

- **KLM** (Knill–Laflamme–Milburn, 2001): bramki da się zbudować z liniowej optyki, pomiarów i splątania pomocniczego, ale potrzebne są źródła pojedynczych fotonów i detektory o bardzo wysokiej wydajności.
- **Realizacje**: Xanadu Borealis (setki ściśniętych modów, „advantage” w próbkowaniu bozonowym), ORCA PT-1 (kubity czasowe, temperatura pokojowa), PsiQuantum („fusion-based”, fotonika krzemowa).
- **Detektory**: SNSPD (nadprzewodzące nanodruty) o wydajności $>95\%$; źródła pojedynczych fotonów o nierozróżnialności $\approx99\%$.

**Spiny w krzemie (kropki kwantowe).** Elektron lub jądro w kropce zdefiniowanej elektrodami na krzemie; bramkowanie elektryczne, zgodność z technologią CMOS. Zaleta: minimalne rozmiary i produkcja litograficzna; wady: krótka koherencja ($T_2^\ast\approx1$–$20$ µs, $T_2$ z echem $100$ µs–$1$ ms), szum ładunku i jąder $^{29}\mathrm{Si}$, wierność 2Q $\approx99\%$–$99{,}5\%$.

**Centra barwne w diamencie (NV, SiV).** Defekt sieci diamentu z elektronowym spinem $S=1$: temperatura pokojowa, $T_2$ rzędu ms przy echu, możliwość pomiaru pola pojedynczej cząsteczki. Wada: skalowanie (sprzężenie spinów maleje z odległością) — dlatego NV to dziś przede wszystkim **sensory** (rozdział 11), a nie kubity komputera. Uwaga terminologiczna: „kropka kwantowa” w optyce oznacza też nanostrukturę emitującą pojedyncze fotony.

### 3.7 Kubity topologiczne i anyony

Idea: zamiast korygować błędy, **zakodować informację w topologii** — lokalne zaburzenia nie
mogą jej zniszczyć, bo zmiana stanu wymaga manipulacji całym układem (jak rozcięcie wstęgi
Möbiusa zamiast przecięcia zwykłej nitki).

- **Anyony**: kwazicząstki w układach 2D (efekt Halla, warstwy topologiczne, kody
  powierzchniowe) o statystyce pośredniej między bozonami a fermionami. Anyony **nieabelowe**
  pozwalają na operacje zależne od kolejności splatania — stąd „topologiczna” bramka.
- **Kubity Majorany**: para kwazicząstek Majorany (np. na końcach nanodrutu InAs/Al
  z nadprzewodnikiem) koduje jeden kubit niezlokalizowany — informacja jest „niewidoczna”
  lokalnie.
- **Stan na 2025 r.**: istnieją eksperymenty pokazujące sygnatury stanów Majorany i
  topologiczną przerwę energetyczną, ale **brak przekonującej demonstracji kubitu
  topologicznego z nieabelową statystyką** i skalowalnego procesora. To najbardziej
  obiecująca, ale wciąż nieudowodniona ścieżka (Microsoft, Delft, Copenhagen).

### 3.8 Architektury, dostawcy i chmura

Dwie ważne decyzje architektoniczne: **(i)** jak połączyć kubity (łączność), **(ii)** czy
urządzenie stoi u użytkownika, czy jest udostępniane przez chmurę.

| Dostawca | Technologia | Skala (rzędy wielkości) | Dostęp |
| --- | --- | --- | --- |
| IBM | transmony nadprzewodzące | $100$–$1000$ kubitów | chmura IBM Quantum, także Cyfronet AGH (Kraków) |
| Google | transmony (krata 2D) | $\approx100$ kubitów | badania, brak otwartego dostępu |
| IQM | transmony | $20$–$54$ | chmura, system on-premise w PCSS (Poznań) |
| Rigetti | transmony | $\approx84$ | chmura |
| D-Wave | **annealer** (nie uniwersalny) | $>5000$ spinów | chmura |
| Quantinuum | jony w pułapce | $20$–$56$ | chmura |
| IonQ | jony | $20$–$36$ | chmura |
| Pasqal, QuEra | neutralne atomy | $100$–$1000$ | chmura |
| ORCA | fotonika | $8$+ | chmura |
| PsiQuantum | fotonika | w budowie (cel: $10^6$) | brak dostępu publicznego |

**W Polsce.** W ACK Cyfronet AGH w Krakowie od 2023 r. pracuje **IBM Quantum System One**
(27 kubitów, układ Falcon) — pierwszy taki system w Europie poza Niemcami; dostęp przez
chmurę dla polskich uczelni. W **PCSS** (Poznańskie Centrum Superkomputerowo-Sieciowe) działa
**IQM Garnet** (20 kubitów nadprzewodzących) — pierwszy komercyjny system IQM zainstalowany
u klienta; PCSS udostępnia go naukowcom i szkołom oraz prowadzi warsztaty i konkursy
(m.in. Quantum Computing Hackathon). Prowadzący warsztat „Realizacje komputerów kwantowych”
związany jest właśnie z PCSS.

**Uwaga o D-Wave:** to nie jest komputer bramkowy, lecz **annealer kwantowy** — rozwiązuje
zadania optymalizacyjne zapisane jako problem Isinga. Nie jest uniwersalny (nie realizuje
dowolnego obwodu), ale ma tysiące kubitów i służy jako realny test „czy kwantowe fluktuacje
pomagają w optymalizacji”.

### 3.9 Transpilacja, benchmarki i ograniczenia

**Koszt transpilacji.** Sprzęt nie ma łączności all-to-all, więc bramkę między odległymi
kubitami trzeba „przenieść” przez SWAP-y. Na linii odległość $d$ (w bramkach) wymaga $d$
SWAP-ów, a każdy SWAP to $3$ CNOT, czyli **$3d$ bramek dwukubitowych zamiast jednej**.
Dla kubitów 0 i 4 na 5-kubitowej linii: $4$ SWAP-y $=12$ CNOT. Przy wierności $99{,}7\%$
pojedynczy CNOT ma $F=0{,}997$, ale dwanaście kolejnych już $0{,}997^{12}=0{,}965$ —
**koszt łączności natychmiast zamienia się w koszt wierności**. Dlatego algorytmy „all-to-all”
(QFT, algorytm Shora) lubią jony i atomy w pęsetach, a algorytmy lokalne (obwody wariacyjne)
pasują do krat 2D.

**Benchmarki — jak porównuje się komputery kwantowe?**

- **Wolumetryka kwantowa (quantum volume, QV)**: $2^n$, gdzie $n$ to największa głębokość „kwadratowego” obwodu losowego dającego poprawne wyniki; łączy liczbę kubitów, łączność i błędy w jedną liczbę. Quantinuum raportował QV $2^{21}\approx2{,}1\cdot10^6$.
- **XEB** (cross-entropy benchmarking): porównanie rozkładów wyników obwodów losowych (Google). Sycamore (53 kubity, 2019): $200$ s vs klasyczne oszacowanie tysięcy lat; Willow (105 kubitów, 2024): $<5$ min vs $\sim10^{25}$ lat. Te liczby bywają krytykowane — lepsze algorytmy klasyczne (sieci tensorowe) skracają oszacowania.
- **CLOPS** (circuit layer operations per second): warstwy obwodu na sekundę dla całego systemu (z narzutem sterowania); dla nadprzewodzących $10^3$–$10^4$.
- **EPLG** (error per layered gate): błąd na „warstwę bramek”, czytelny dla algorytmicysty; dla dobrych systemów $1$–$3\%$.
- **Wierność bramek** (randomized benchmarking): miara *fizyczna*, niezależna od rozmiaru problemu — to ją podajemy w tabelach parametrów.

**Ograniczenia i uczciwy bilans.**

1. **Szum.** Typowy błąd to $10^{-3}$–$10^{-4}$ na bramkę. Korekcja błędów wymaga błędu
   fizycznego *poniżej progu* (rozdział 13; dla kodu powierzchniowego $\approx1\%$) i kosztuje
   $2d^2-1$ kubitów fizycznych na jeden logiczny ($d=7$: $97$ kubitów, $d=17$: $577$).
2. **Brak praktycznej przewagi.** Do 2025 r. nie pokazano *użytecznego* zadania (chemia,
   optymalizacja, kryptografia), w którym komputer kwantowy wygrywa z klasycznym. Demonstracje
   „supremacji” dotyczą zadań sztucznych, dobranych pod słabość klasyki.
3. **Wąskie gardło sterowania.** Każdy kubit nadprzewodzący potrzebuje własnej linii
   mikrofalowej i elementów chłodzonych; kable, wzmacniacze i multipleksacja stają się limitem
   (IBM dzieli układ na moduły „chiplets”).
4. **Odczyt i inicjalizacja.** Odczyt jest wolniejszy niż bramki (setki ns–µs) i obarczony
   błędem $1$–$5\%$ — jeden z głównych limitów nadprzewodzących.
5. **Koszt.** Rozcieńczalnik z elektroniką mikrofalową lub pułapka jonowa z laserami to koszt
   milionów złotych. Dlatego większość uczniów pracuje na **chmurze** (IBM, IQM/PCSS,
   Quantinuum), a nie we własnym laboratorium.




## 4. Przykłady rozwiązane

### Przykład 12.1 (łatwy): budżet bramek transmona

**Dane:** $T_1=T_2=100$ µs, $t_g^{1\rm Q}=25$ ns, $t_g^{2\rm Q}=68$ ns, $F_{1\rm Q}=99{,}9\%$, $F_{2\rm Q}=99{,}7\%$.
**Rachunek:** (a) ile bramek „zmieści się” w czasie koherencji: $T_2/t_g^{1\rm Q}=100\,\mu\text{s}/25\,\text{ns}=4000$;
$T_2/t_g^{2\rm Q}=100\,\mu\text{s}/68\,\text{ns}\approx1470$. (b) Po $n$ bramkach $F^n$: $0{,}997^{100}=0{,}74$,
$0{,}997^{1000}=0{,}050$. (c) Granica $50\%$: $0{,}997^n=0{,}5\Rightarrow n=\ln0{,}5/\ln0{,}997=231$ bramek.
**Odpowiedź:** (a) $\mathbf{4000}$ bramek 1Q lub $\mathbf{1470}$ bramek 2Q; (b) $74\%$ po $100$ i
$\mathbf{5{,}0\%}$ po $1000$ bramkach; (c) połowa sukcesu już po $\mathbf{231}$ bramkach.
*Interpretacja:* „$T_2=100$ µs” brzmi dużo, ale $1470$ bramek 2Q to dla algorytmów Shora
($10^9$ bramek) kropla w morzu — stąd konieczność korekcji błędów.

### Przykład 12.2 (trudniejszy): transmony kontra jony

**Dane:** zadanie wymaga $1000$ bramek dwukubitowych. Transmon: $t_g^{2\rm Q}=68$ ns, $F=99{,}7\%$,
$T_2=100$ µs. Jon: $t_g^{2\rm Q}=100$ µs, $F=99{,}8\%$, $T_2=1$ s. Chcemy $1000$ powtórzeń (shots).
**Rachunek:** czas obwodu: transmony $1000\cdot68\,\text{ns}=68$ µs $<T_2$ ✓; jony $1000\cdot100\,\mu\text{s}=0{,}1$ s $<T_2$ ✓.
Wierność: transmony $0{,}997^{1000}=0{,}050$; jony $0{,}998^{1000}=0{,}135$. Czas $1000$ powtórzeń:
transmony $68$ ms, jony $100$ s.
**Odpowiedź:** jony dają $\mathbf{13{,}5\%}$ szansy bezbłędnego przebiegu wobec $\mathbf{5{,}0\%}$ dla
transmonów ($2{,}7\times$ lepiej), ale każdy przebieg trwa $\mathbf{0{,}1}$ s zamiast $68$ µs
($\approx1500\times$ wolniej).
*Interpretacja:* to klasyczny kompromis „wierność kontra szybkość”; obie technologie nadają się
pod korekcję błędów, ale ich profile błędów są różne (jony: bardzo dokładne, wolne; transmony:
szybkie, „cieknące” w czasie).

## 5. Typowe pułapki

1. **Mylenie $T_1$, $T_2$ i $T_2^\ast$.** $T_1$ to zanik populacji, $T_2$ — zanik fazy; zawsze $T_2\le2T_1$, a $T_2^\ast\le T_2$.
2. **Traktowanie wierności jak „prawie $1$”.** $99{,}7\%$ po $1000$ bramkach daje $5\%$ — błędy mnożą się wykładniczo.
3. **Mylenie liczby kubitów z mocą obliczeniową.** $1000$ kubitów w „linii” z błędem $1\%$ jest praktycznie bezużyteczne; liczy się QV/EPLG, nie liczba kubitów.
4. **Zapominanie o transpilacji.** Łączność i bramki natywne zmieniają obwód; jedna bramka daleka może kosztować kilkanaście CNOT.
5. **Mylenie D-Wave z uniwersalnym komputerem.** Annealer rozwiązuje tylko problem Isinga.
6. **Wnioskowanie „przewaga kwantowa = użyteczność”.** Demonstracje XEB są użyteczne dla fizyki urządzenia, nie dla użytkownika.

## 6. Zadania (Z-12)

**Z-12.1.** Kryteria DiVincenzy. (a) Wymień pięć warunków. (b) Które z nich łamie (i dlaczego) annealer D-Wave? (c) Które warunki doskonale spełnia centrum NV, a z którym ma fundamentalny problem?

**Z-12.2.** Budżet bramek: $T_2=200$ µs, bramka dwukubitowa $t_g=50$ ns, wierność $F=99{,}8\%$. (a) Ile bramek zmieści się w $T_2$? (b) Policz $F^n$ dla $n=500$ i $n=5000$. (c) Po ilu bramkach szansa sukcesu spada do $50\%$?

**Z-12.3.** Porównanie technologii. (a) Policz $T_2/t_g$ dla transmona ($T_2=150$ µs, $t_g=60$ ns) i jonu ($T_2=1$ s, $t_g=200$ µs). (b) Dla $200$ bramek dwukubitowych policz $F^n$ dla $F=99{,}7\%$ (transmon) i $F=99{,}9\%$ (jon). (c) Którą technologię wybierzesz dla zadania z $10^3$ bramek i dlaczego?

**Z-12.4.** Transpilacja. (a) Ile CNOT kosztuje jedna bramka między kubitami o odległości $6$ na linii? (b) Policz łączną wierność takiego „transportu” przy $F_{\rm CNOT}=99{,}7\%$. (c) O ile wzrośnie liczba bramek dwukubitowych w obwodzie ze $100$ takimi dalekimi bramkami?

**Z-12.5.** Benchmarki. (a) Co mierzy wolumetryka kwantowa, a co XEB? (b) Dlaczego liczba kubitów jest złą miarą jakości? (c) Ile trwa obwód o $20$ warstwach przy $5000$ CLOPS? Podaj wynik w sekundach i milisekundach.

**Z-12.6. [★]** Sprzęt w Polsce i w chmurze. (a) Podaj dwa polskie systemy kwantowe (lokalizacja, technologia, liczba kubitów). (b) Wymień kroki od napisania obwodu do otrzymania histogramu z prawdziwego urządzenia. (c) Dlaczego kalibracja i kolejkowanie wpływają na wynik i jak to raportuje się w pracy?

## 7. Wskazówki do zadań

- **Z-12.1.** Warunek 4 (uniwersalność) i 5 (pomiar) analizuj „wolno/nie wolno” — annealer nie realizuje dowolnego obwodu.
- **Z-12.2.** Użyj $F^n$; w (c) rozwiąż $\ln0{,}5/\ln F$.
- **Z-12.3.** W (b) użyj $F^n$; w (c) porównaj czasy obwodu, nie tylko wierności.
- **Z-12.4.** Każdy SWAP $=3$ CNOT; odległość $d$ wymaga $d$ SWAP-ów.
- **Z-12.5.** QV to $2^n$ z głębokości obwodu; XEB porównuje rozkłady; CLOPS to warstwy na sekundę.
- **Z-12.6.** Szukaj informacji w dokumentacji Cyfronetu i PCSS; opis kroków jak w rozdziale 15.

## 8. Co dalej

- **Korekcja i mitygacja błędów** — [rozdział 13](13-korekcja-i-mitygacja-bledow.md): co zrobić z błędem $10^{-3}$ na bramkę.
- **Oprogramowanie kwantowe** — [rozdział 15](15-oprogramowanie-kwantowe.md): jak *naprawdę* wysłać obwód do chmury.
- **Narzędzia informatyczne** — [rozdział 14](14-narzedzia-informatyczne.md): git, PowerShell, praca zdalna na klastrach.
- Pełne rozwiązania: [zadania/rozwiazania/rozwiazania-12.md](../zadania/rozwiazania/rozwiazania-12.md); praca domowa: [PD-3](../praca-domowa/praca-domowa-03.md).
- Bibliografia: Kjaergaard i in., *Superconducting qubits* (2019); Bruzewicz i in., *Trapped-ion quantum computing* (2019); Saffman, *Quantum computing with atomic qubits* (2016) — zob. [bibliografia](../docs/bibliografia.md).

> **Weryfikacja numeryczna.** Liczby w rozdziale policzono w NumPy: $T_2/t_g=1470$ i $4000$;
> $0{,}997^{1000}=0{,}0496$, $0{,}998^{1000}=0{,}135$, $0{,}999^{1000}=0{,}368$; $0{,}997^{12}=0{,}965$;
> $0{,}997^{10^6}=e^{-3004{,}5}$; $2d^2-1$ dla $d=7,17$.


