# Praca domowa PD-3 (rozdziały 11–15)

Praca domowa po module trzecim obejmuje rozdziały [11](../teoria/11-metrologia-kwantowa.md)
(metrologia kwantowa), [12](../teoria/12-realizacje-komputerow-kwantowych.md) (realizacje sprzętowe),
[13](../teoria/13-korekcja-i-mitygacja-bledow.md) (korekcja i mitygacja błędów),
[14](../teoria/14-narzedzia-informatyczne.md) (narzędzia informatyczne) oraz
[15](../teoria/15-oprogramowanie-kwantowe.md) (oprogramowanie kwantowe).

**Zasady:** rozwiązania pisemne z pełnym rachunkiem; notacja jak w
[konwencjach](../docs/03-konwencje-i-notacja.md) (Dirac, kolejność małoendianowa, $\theta/2$
w bramkach obrotu, przecinek dziesiętny jako `{,}`). Wyniki przybliżone podawaj z trzema cyframi
znaczącymi. W zadaniach programistycznych dołącz kod i wynik jego uruchomienia.
**Razem 20 punktów** (10 zadań po 2 pkt).

## Zadania

**PD-3.1 (2 pkt).** Metrologia: $N=10^4$ fotonów w interferometrze Macha–Zehndera.
(a) Policz $\Delta\varphi$ dla światła klasycznego (granica śrutowa) i dla stanu N00N.
(b) Ile fotonów trzeba w obu reżimach, aby osiągnąć $\Delta\varphi=10^{-6}$ rad?
(c) Koherencja stanu N00N przetrwała z prawdopodobieństwem $p=0{,}9$; policz $F_Q(p)$ i $\Delta\varphi$.

**PD-3.2 (2 pkt).** Kwantowa informacja Fishera.
(a) Policz $F$ dla pojedynczego fotonu w bazie $X$ (rozkład $\cos^2\frac\varphi2$, $\sin^2\frac\varphi2$).
(b) Policz $F_Q$ dla stanu N00N o $N$ fotonach, wychodząc z $\mathrm{Var}(n_a)=N^2/4$ i $F_Q=4\mathrm{Var}(H)$.
(c) Uzasadnij, dlaczego $F_Q\le N^2$ dla $N$ fotonów (wskaż krok z wariancją zmiennej ograniczonej).

**PD-3.3 (2 pkt).** Porównanie dwóch technologii sprzętowych. Transmon: $T_2=120$ µs,
bramka dwukubitowa $60$ ns, $F=99{,}7\%$. Jon: $T_2=0{,}5$ s, bramka $100$ µs, $F=99{,}9\%$.
(a) Policz $T_2/t_g$ dla obu. (b) Dla $500$ bramek dwukubitowych policz $F^n$. (c) Którą technologię
wybierzesz dla algorytmu o $500$ bramkach i dlaczego (uwzględnij czas obwodu)?

**PD-3.4 (2 pkt).** Kod 3-kubitowy bit-flip $\lbrack\!\lbrack3,1,3\rbrack\!\rbrack$, stan
$\lvert\psi_L\rangle=\frac{1}{\sqrt2}(\lvert000\rangle+\lvert111\rangle)$, kolejność małoendianowa
$\lvert q_2q_1q_0\rangle$.
(a) Podaj stabilizatory i **ręcznie** policz syndrom $(s_{12},s_{23})$ dla błędu $X$ na $q_0$.
(b) To samo dla błędu $X$ na $q_1$ i $q_2$ — zbuduj pełną tabelę i wskaż poprawki.
(c) Co się stanie, gdy błędy $X$ zajdą jednocześnie na $q_0$ i $q_1$? Odpowiedz, podając stan po „korekcie”.

**PD-3.5 (2 pkt).** Kod stabilizatorowy Steane'a $\lbrack\!\lbrack7,1,3\rbrack\!\rbrack$.
(a) Podaj sześć generatorów i sprawdź, że każdy ma wagę $4$. (b) Wyznacz syndrom dla błędu $X$ na
kubicie $q_5$ i dla błędu $Z$ na $q_3$. (c) Ile jest klas syndromów i dlaczego tabela syndromów
pozwala jednoznacznie rozpoznać każdy pojedynczy błąd?

**PD-3.6 (2 pkt).** Mitygacja błędów.
(a) Dla macierzy kalibracji odczytu $A$ danej wzorem

$$
A=\begin{pmatrix}0{,}96&0{,}08\\0{,}04&0{,}92\end{pmatrix}
$$

i pomiaru $\vec p_{\rm zmierz}=(0{,}70;0{,}30)$ wyznacz $\vec p_{\rm popr}=A^{-1}\vec p_{\rm zmierz}$
i sprawdź, że składowe sumują się do $1$. (b) Podaj liczbę warunkową $\mathrm{cond}(A)$ i wyjaśnij,
co się dzieje przy jej wzroście. (c) Punkty ZNE: $E(1)=0{,}85$, $E(2)=0{,}73$, $E(3)=0{,}61$ —
wyznacz $E(0)$ liniowo i oceń wiarygodność wyniku.

**PD-3.7 (2 pkt).** Terminal i git.
(a) Podaj polecenia (PowerShell lub bash) tworzące katalog `rozwiazania` i przenoszące do niego
plik `z1.md`. (b) Wypisz kolejność poleceń od zmiany pliku do wysłania zmian na GitHub oraz wyjaśnij
rolę `.gitignore` (podaj trzy typowe wpisy). (c) Przez pomyłkę zacommitowałeś plik z hasłem —
podaj polecenia naprawcze i wyjaśnij, dlaczego samo usunięcie pliku nie wystarcza.

**PD-3.8 (2 pkt).** Obwód w kodzie (Qiskit lub opis macierzowy).
(a) Napisz obwód, który ze stanu $\lvert00\rangle$ wytwarza
$\frac{1}{\sqrt2}(\lvert01\rangle-\lvert10\rangle)$ (kolejność małoendianowa, $q_0$ — kontrolny
w operacji CNOT). (b) Podaj prawdopodobieństwa pomiaru $P_{00},P_{01},P_{10},P_{11}$.
(c) Jak zmierzyć $\langle XX\rangle$ dla tego stanu i ile ona wynosi?

**PD-3.9 (2 pkt).** Transpilacja i VQE.
(a) Ile bramek CNOT kosztuje jedna bramka między $q_0$ i $q_3$ na linii $4$-kubitowej, jeśli każdy
SWAP to $3$ CNOT? (b) Policz wierność takiego „transportu” przy $F_{\rm CNOT}=99{,}7\%$.
(c) Dlaczego dla $H=X_0X_1+Z_0Z_1$ ansatz złożony z `ry,ry,cx` nie wystarcza do znalezienia
energii stanu podstawowego — i co trzeba dodać?

**PD-3.10 (2 pkt).** Kod powierzchniowy.
(a) Policz liczbę kubitów fizycznych $2d^2-1$ dla $d=5$ i $d=7$. (b) Ile kubitów fizycznych
potrzeba na $10$ kubitów logicznych o $d=7$? (c) Wyjaśnij, dlaczego przy błędzie fizycznym
**powyżej** progu zwiększanie dystansu $d$ nie poprawia wyniku.

## Kryteria oceny

Każde zadanie oceniamy w skali **0–2 pkt**:

| Punkty | Kryterium |
| --- | --- |
| 2 | poprawny wynik we wszystkich podpunktach + widoczny rachunek i poprawna interpretacja |
| 1 | poprawna metoda, drobny błąd rachunkowy lub brak jednego podpunktu |
| 0 | brak metody, błędna metoda lub wynik bez uzasadnienia |

Wymagania ogólne:

1. **Widoczny rachunek** (wzór → podstawienie → wynik); sam wynik to najwyżej 1 pkt.
2. **Notacja** zgodna z [konwencjami](../docs/03-konwencje-i-notacja.md); w zadaniach obwodowych
   jawnie deklaruj kolejność kubitów.
3. **Jednostki i dokładność** (rad, mHz, %, liczba kubitów) z trzema cyframi znaczącymi.
4. **Kod** w PD-3.8–PD-3.9: krótki, czytelny, z wynikiem uruchomienia i komentarzem.
5. **Oznaczenie narzędzi.** Jeśli użyto numpy, sympy lub AI — wskaż gdzie (wymagane).

## Wskazówki i odpowiedzi

**PD-3.1.** (a) Klasycznie $\Delta\varphi=1/\sqrt N=1/\sqrt{10^4}=10^{-2}$ rad; stan N00N:
$\Delta\varphi=1/N=10^{-4}$ rad. (b) Na $10^{-6}$ rad: klasycznie $N=1/\varepsilon^2=10^{12}$
fotonów, ze stanem N00N $N=1/\varepsilon=10^6$. (c) $F_Q(p)=pN^2+(1-p)N=0{,}9\cdot10^8+0{,}1\cdot10^4=9{,}0001\cdot10^7$,
więc $\Delta\varphi=1/\sqrt{F_Q}=1{,}05\cdot10^{-4}$ rad (zamiast $10^{-4}$ idealnie i $10^{-2}$
klasycznie).

**PD-3.2.** (a) $\partial_\varphi p_\pm=\mp\frac12\sin\varphi$ i
$F=\frac{\sin^2\varphi}{4}\left(\frac{1}{\cos^2\frac\varphi2}+\frac{1}{\sin^2\frac\varphi2}\right)=1$
(bo $\cos^2\frac\varphi2\sin^2\frac\varphi2=\frac14\sin^2\varphi$). (b) $F_Q=4\cdot\frac{N^2}{4}=N^2$.
(c) Przy ustalonym $N$ mamy $H=n_a-N/2$, więc $F_Q=4\mathrm{Var}(n_a)$; $n_a\in[0,N]$, a wariancja
zmiennej z przedziału o długości $N$ nie przekracza $(N/2)^2$, stąd $F_Q\le4\cdot\frac{N^2}{4}=N^2$.

**PD-3.3.** (a) Transmon: $120\,\mu\text{s}/60\,\text{ns}=2000$; jon: $0{,}5\,\text{s}/100\,\mu\text{s}=5000$.
(b) Transmon $0{,}997^{500}=0{,}223$; jon $0{,}999^{500}=0{,}606$. (c) Jon — wyższe
prawdopodobieństwo sukcesu ($0{,}606$ wobec $0{,}223$); czas obwodu: jon $500\cdot100\,\mu\text{s}=50$ ms
wobec $30$ µs dla transmona, więc jon jest $\approx1700\times$ wolniejszy — przy zadaniu
wymagającym wielu powtórzeń (statystyki) wybór może się odwrócić.

**PD-3.4.** (a) Stabilizatory $S_1=Z_1Z_2$, $S_2=Z_2Z_3$. Dla $X$ na $q_0$ stan przechodzi
w $\frac{1}{\sqrt2}(\lvert001\rangle+\lvert110\rangle)$; wartości $\sigma_z$: $q_2=q_1=0\Rightarrow S_1=+1$
oraz $q_1=0,q_0=1\Rightarrow S_2=-1$, czyli syndrom $(0,1)$. (b) Pełna tabela: brak błędu $(0,0)$;
$X$ na $q_0$: $(0,1)$ (poprawka $X$ na $q_0$); $X$ na $q_1$: $(1,1)$ ($X$ na $q_1$);
$X$ na $q_2$: $(1,0)$ ($X$ na $q_2$). (c) Dwa błędy $X$ na $q_0,q_1$ dają syndrom $(1,0)$ — taki jak
pojedynczy $X$ na $q_2$ — więc „poprawka” $X$ na $q_2$ zamienia stan w
$\alpha\lvert111\rangle+\beta\lvert000\rangle=\alpha\lvert1\rangle_L+\beta\lvert0\rangle_L$,
czyli wprowadza błąd logiczny $X_L$ (kod o dystansie $3$ naprawia tylko jeden błąd).

**PD-3.5.** (a) $g_1=X_4X_5X_6X_7$, $g_2=X_2X_3X_6X_7$, $g_3=X_1X_3X_5X_7$ oraz $g_4\ldots g_6$
z $Z$ na tych samych kubitach; każdy ma wagę $4$, a każde dwa mają parzystą liczbę wspólnych
kubitów ($0$, $2$ lub $4$), więc komutują. (b) $X$ na $q_5$: generatory $Z$-owe $g_4,g_6$ dają $-1$,
syndrom $101$ (binarnie $5$); $Z$ na $q_3$: generatory $X$-owe $g_2,g_3$ dają $-1$, syndrom $011$
(binarnie $3$). (c) $2^{\,n-k}=2^6=64$ klasy; błędów jednostkowych jest $1+7\cdot3=22$, a ich syndromy
są parami różne, więc każdy pojedynczy błąd rozpoznajemy jednoznacznie.

**PD-3.6.** (a) $\det A=0{,}88$ i macierz odwrotna

$$
A^{-1}=\frac{1}{0{,}88}\begin{pmatrix}0{,}92&-0{,}08\\-0{,}04&0{,}96\end{pmatrix},
$$

stąd $\vec p_{\rm popr}=(0{,}7045;\,0{,}2955)$, suma $=1{,}0000$ ✓. (b) $\mathrm{cond}(A)=1{,}144$;
gdy rośnie (kolumny $A$ stają się podobne), mały błąd pomiaru daje duży błąd wyniku, a poprawione
prawdopodobieństwa wychodzą poza $[0,1]$ i trzeba je rzutować na sympleks. (c) Prosta
$E(\lambda)=E(0)+a\lambda$ z $a=\frac{0{,}61-0{,}85}{2}=-0{,}12$ daje $E(0)=0{,}97$; wynik jest
fizyczny (nie przekracza $1$), ale mieści się w granicach fluktuacji pomiaru, więc traktujemy go
jako oszacowanie, nie jako „dokładną” wartość bez szumu.

**PD-3.7.** (a) `New-Item -ItemType Directory rozwiazania` (lub `mkdir -p rozwiazania`), potem
`Move-Item z1.md rozwiazania\` (PowerShell) albo `mv z1.md rozwiazania/` (bash). (b)
`git status` → `git add plik` → `git commit -m "opis"` → `git push origin main`; `.gitignore` to lista
plików nieśledzonych (np. `__pycache__/`, `.venv/`, `.env`). (c) `git rm --cached plik`, wpis do
`.gitignore`, `git commit`; **samo usunięcie nie wystarcza**, bo plik zostaje w historii poprzednich
commitów — trzeba natychmiast zmienić hasło/token (i w razie potrzeby przepisać historię).

**PD-3.8.** (a) `qc.x(0); qc.h(1); qc.cx(1, 0); qc.z(1)` — krok po kroku:
$\lvert00\rangle\xrightarrow{X_0}\lvert01\rangle\xrightarrow{H_1}\frac{1}{\sqrt2}(\lvert01\rangle+\lvert11\rangle) \xrightarrow{\mathrm{CNOT}(1,0)}\frac{1}{\sqrt2}(\lvert01\rangle+\lvert10\rangle)\xrightarrow{Z_1}\frac{1}{\sqrt2}(\lvert01\rangle-\lvert10\rangle)$.
(b) $P_{01}=P_{10}=\frac12$, $P_{00}=P_{11}=0$. (c) $\langle XX\rangle=-1$: pod działaniem $X_0X_1$
składniki zamieniają się miejscami i pojawia się minus, więc $X_0X_1\lvert\psi\rangle=-\lvert\psi\rangle$;
pomiar $\langle XX\rangle$ wykonuje się dodając $H$ na oba kubity przed pomiarem w bazie $Z$.

**PD-3.9.** (a) Odległość $3$ (linia $q_0-q_1-q_2-q_3$) $\Rightarrow$ $3$ SWAP-y $=9$ CNOT.
(b) $0{,}997^{9}=0{,}973$. (c) Ansatz `ry,ry,cx` daje tylko kombinacje
$a\lvert00\rangle+b\lvert01\rangle+d\lvert11\rangle$ (bez amplitudy na $\lvert10\rangle$), a stan
podstawowy $H$ to $\frac{1}{\sqrt2}(\lvert01\rangle-\lvert10\rangle)$ — w tej podprzestrzeni najniższa
energia wynosi $-1$, nie $-2$. Trzeba dodać obroty (np. `ry`) **po** bramce CNOT: ansatz
4-parametrowy osiąga $-2{,}0000$.

**PD-3.10.** (a) $d=5$: $2\cdot25-1=49$; $d=7$: $2\cdot49-1=97$. (b) $10\cdot97=970$ kubitów
fizycznych. (c) Twierdzenie o progu działa tylko dla $p<p_{\rm thr}$ ($\approx0{,}5$–$1\%$ dla kodu
powierzchniowego): powyżej progu dokładanie kubitów i pomiarów **zwiększa** liczbę błędów szybciej,
niż kod je usuwa, więc błąd logiczny rośnie z $d$.

## Rozkład punktów i tematy

| Zadanie | Rozdziały | Temat | Punkty |
| --- | --- | --- | --- |
| PD-3.1 | 11 | granica śrutowa vs Heisenberg, dekoherencja | 2 |
| PD-3.2 | 11 | informacja Fishera, $F_Q\le N^2$ | 2 |
| PD-3.3 | 12 | porównanie technologii (transmon vs jon) | 2 |
| PD-3.4 | 13 | syndrom kodu 3-kubitowego (ręcznie) | 2 |
| PD-3.5 | 13 | kod Steane'a, syndromy | 2 |
| PD-3.6 | 13 | macierz kalibracji, ZNE | 2 |
| PD-3.7 | 14 | terminal i git | 2 |
| PD-3.8 | 15 | obwód w kodzie, pomiar $\langle XX\rangle$ | 2 |
| PD-3.9 | 12, 15 | transpilacja, ansatz VQE | 2 |
| PD-3.10 | 13 | koszt zasobów kodu powierzchniowego | 2 |
| **Razem** | | | **20** |

**Kolejny krok.** Po zaliczeniu PD-3 przejdź do rozdziałów 16–20 i pracy domowej PD-4
(analiza danych, macierze gęstości, dekoherencja, algorytmy zaawansowane, mini-projekty);
rozwiązania zadań z rozdziałów znajdziesz w [`zadania/rozwiazania/`](../zadania/rozwiazania/rozwiazania-11.md).



