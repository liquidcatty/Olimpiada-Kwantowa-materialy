# Konwencje i notacja


## 1. Skąd bierze się zakres przewodnika

Przewodnik odzwierciedla zakres Olimpiady Kwantowej (Fundacja Quantum AI,
<https://olimpiadakwantowa.pl/>), wyznaczony przez:

1. listę **16 warsztatów przygotowawczych** I edycji (2026/2027),
2. **arkusz zadań przykładowych** (`Zadania przykładowe`, zadania P1–P4),
3. strukturę etapów: Etap I (zadania zdalne, 15.11.2026–28.02.2027),
   Etap II (rozmowa online, 1–30.04.2027), Etap III (finał, Kraków, 4–7.06.2027).

Rejestracja: 10.09.2026–28.02.2027. Udział bezpłatny, dla uczniów szkół
ponadpodstawowych (za zgodą opiekuna w przypadku osób niepełnoletnich).

## 2. Notacja matematyczna

### 2.1 Wektory i liczby zespolone

| Obiekt | Zapis | Znaczenie |
| --- | --- | --- |
| Liczba zespolona | $z = a + bi$, $a,b\in\mathbb{R}$ | $i^2 = -1$ |
| Sprzężenie | $z^\ast = a - bi$ | (w kodzie: `numpy.conjugate`) |
| Moduł | $\lvert z\rvert = \sqrt{z^\astz}$ | długość na płaszczyźnie zespolonej |
| Faza | $\arg z$, $z = \lvert z\rvert e^{i\varphi}$ | postać biegunowa |
| Wektor kolumnowy | $\lvert\psi\rangle$ | ket (element $\mathbb{C}^n$) |
| Wektor wierszowy sprzężony | $\langle\psi\rvert = (\lvert\psi\rangle)^\dagger$ | bra, $\dagger$ = sprzężenie + transpozycja |
| Iloczyn skalarny | $\langle\phi\vert\psi\rangle$ | liczba zespolona |
| Norma | $\lVert\psi\rVert = \sqrt{\langle\psi\vert\psi\rangle}$ | równa 1 dla stanu fizycznego |

### 2.2 Notacja Diraca (kety i bra)

- Stan układu: $\lvert\psi\rangle$. Baza obliczeniowa kubitu: $\lvert 0\rangle=\binom{1}{0}$, $\lvert 1\rangle=\binom{0}{1}$.
- $\langle 0\vert 0\rangle = \langle 1\vert 1\rangle = 1$, $\langle 0\vert 1\rangle = \langle 1\vert 0\rangle = 0$.
- Rozkład w bazie: $\lvert\psi\rangle = \sum_k c_k\lvert k\rangle$, gdzie $P(k)=\lvert c_k\rvert^2$.
- **Reguła**: $c_k = \langle k\vert\psi\rangle$ (rzut), nie $\langle\psi\vert k\rangle$.

### 2.3 Iloczyn tensorowy i uporządkowanie kubitów

- Iloczyn tensorowy: $\otimes$. Dla macierzy $A$ ($m\times n$) i $B$ ($p\times q$):
  $A\otimes B$ ma wymiar $mp\times nq$, elementy to bloki $A_{ij}B$.
- Dla $n$ kubitów przestrzeń ma wymiar $2^n$.
- **Konwencja kolejności (małoendianowa, jak w Qiskit):**
  stan $\lvert q_{n-1}\dots q_1 q_0\rangle$ ma indeks
  $j = q_0 2^0 + q_1 2^1 + \dots + q_{n-1}2^{n-1}$, czyli **kubit 0 to najmłodszy bit**.
  Dla dwóch kubitów $\lvert q_1 q_0\rangle$: $\lvert 00\rangle,\lvert 01\rangle,\lvert 10\rangle,\lvert 11\rangle$
  to wiersze o indeksach $0,1,2,3$.
- Konsekwencja: bramka na kubicie 0 („dolnym” w zapisie $q_1q_0$) to mnożenie z prawej
  $U = I \otimes G$; bramka na kubicie 1 to $U = G \otimes I$.
- Dlatego w zadaniu P4: $H \mapsto H\otimes I$ (górny kubit), $R_Y(\theta)\mapsto I\otimes R_Y(\theta)$
  (dolny kubit). **Zawsze jawnie deklarujemy konwencję w rozwiązaniu.**

### 2.4 Bramki i operatory

| Symbol | Nazwa | Macierz |
| --- | --- | --- |
| $I$ | identyczność | macierz $I$ |
| $X$ | Pauliego-X / NOT | macierz $X$ |
| $Y$ | Pauliego-Y | macierz $Y$ |
| $Z$ | Pauliego-Z | macierz $Z$ |
| $H$ | Hadamarda | macierz $H$ |
| $S$ | faza | $\mathrm{diag}(1, i)$ |
| $T$ | faza $\pi/8$ | $\mathrm{diag}(1, e^{i\pi/4})$ |
| $R_Z(\theta)$ | obrót wokół $Z$ | $\mathrm{diag}(e^{-i\theta/2}, e^{i\theta/2})$ |
| $R_Y(\theta)$ | obrót wokół $Y$ | macierz $R_Y(\theta)$ |
| $R_X(\theta)$ | obrót wokół $X$ | macierz $R_X(\theta)$ |
| CNOT | kontrolowany $X$ | $\lvert0\rangle\langle0\rvert\otimes I + \lvert1\rangle\langle1\rvert\otimes X$ |
| CZ | kontrolowany $Z$ | $\mathrm{diag}(1,1,1,-1)$ |

Macierze z tabeli (baza $\{\lvert0\rangle,\lvert1\rangle\}$):

$$
I=\begin{pmatrix}1&0\\0&1\end{pmatrix},\qquad
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}
$$

$$
H=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}
$$

$$
R_Y(\theta)=\begin{pmatrix}\cos\frac{\theta}{2}&-\sin\frac{\theta}{2}\\ \sin\frac{\theta}{2}&\cos\frac{\theta}{2}\end{pmatrix},\qquad
R_X(\theta)=\begin{pmatrix}\cos\frac{\theta}{2}&-i\sin\frac{\theta}{2}\\ -i\sin\frac{\theta}{2}&\cos\frac{\theta}{2}\end{pmatrix}
$$

**Konwencja kąta**: w $R_X,R_Y,R_Z$ występuje $\theta/2$ (jak w zadaniu P4). Kąt
geometryczny obrotu na sferze Blocha to $\theta$.

### 2.5 Wartości oczekiwane, wariancja, nieoznaczoność

- $\langle A\rangle = \langle\psi\vert A\vert\psi\rangle$ (stan czysty, obserwabla $A$).
- $\mathrm{Var}(A) = \langle A^2\rangle - \langle A\rangle^2$, $\Delta A = \sqrt{\mathrm{Var}(A)}$.
- $\Delta A\,\Delta B \ge \left\lvert\frac{1}{2i}\langle[A,B]\rangle\right\rvert$, gdzie $[A,B]=AB-BA$.
- Ewolucja unitarna: $\lvert\psi(t)\rangle = e^{-iHt/\hbar}\lvert\psi(0)\rangle$.
- Równanie Schrödingera: $i\hbar\,\frac{d}{dt}\lvert\psi\rangle = H\lvert\psi\rangle$.

### 2.6 Pomiar

- Pomiar w bazie ortonormalnej $\{\lvert m\rangle\}$ (rzutowy / von Neumanna):
  $P(m) = \lvert\langle m\vert\psi\rangle\rvert^2$, po pomiarze stan $\to\lvert m\rangle$.
- Pomiar obserwabli $A=\sum_a a\lvert a\rangle\langle a\rvert$: $P(a)=\lvert\langle a\vert\psi\rangle\rvert^2$,
  $\langle A\rangle=\sum_a a\,P(a)$.
- **Kluczowe rozróżnienie**: jednorazowy wynik $\ne\langle A\rangle$. Wartość oczekiwana
  to średnia z wielu pomiarów na identycznie przygotowanym stanie.

### 2.7 Macierz gęstości

- $\rho = \sum_k p_k\lvert\psi_k\rangle\langle\psi_k\rvert$, $\rho^\dagger=\rho$, $\mathrm{Tr}\,\rho=1$, $\rho\succeq0$.
- Stan czysty: $\mathrm{Tr}\,\rho^2=1$. Stan mieszany: $\mathrm{Tr}\,\rho^2<1$.
- Ślad częściowy: $\rho_A=\mathrm{Tr}_B\,\rho$.
- Rozkład Blocha: $\rho=\frac12\left(I+\vec r\cdot\vec\sigma\right)$; stan czysty $\Leftrightarrow\lvert\vec r\rvert=1$.

## 3. Notacja w kodzie

- Python 3.11 + **NumPy** (wymagane), `matplotlib` (opcjonalnie, tylko wykresy).
- Wektor stanu: kształt `(2**n, 1)` (kolumna) — **lub** `(2**n,)`; w obrębie pliku
  konsekwentnie i jawnie w nagłówku.
- Macierze: `(2**n, 2**n)`. Iloczyn tensorowy: `numpy.kron`. Sprzężenie: `arr.conj().T`.
- Kolejność kubitów: **małoendianowa** (identyczna jak w 2.3).
- Nazwy plików: `snake_case.py`, bez znaków diakrytycznych.
- Każdy skrypt uruchamiamy: `python kod/<nazwa>.py`; wypisuje wyniki i asercje
  zakończone `OK`/`FAIL`.

## 4. Styl pisania zadań

- Zadanie: numer, polecenia (a), (b), (c); w pliku z rozwiązaniami — pełne rozwiązanie
  z uzasadnieniem i odpowiedzią w ramce.
- Język polski; termin angielski w nawiasie przy pierwszym użyciu,
  np. „splątanie (*entanglement*)”.
- Jednostki SI, chyba że zadanie mówi inaczej; $\hbar=h/2\pi$.
- Wyniki przybliżone z jawną dokładnością, np. $\approx 0{,}854$ (3 cyfry znaczące).
- Rysunki opisujemy słownie lub w ASCII; wykresy generowane skryptem trafiają do `kod/`.

## 5. Numeracja i odsyłacze

- Linki relatywne: `[rozdział 02](../teoria/02-algebra-liniowa.md)`.
- Praca domowa: `PD-<nr modułu>` (np. `PD-2`).
- Zestaw zadań z teorii: `Z-<nr rozdziału>` (np. `Z-06`).
- Zadania oficjalne przykładowe: `P1`–`P4` (numeracji organizatora nie zmieniamy).

## 6. Zasady zapisu matematyki pod GitHub (zweryfikowane empirycznie)

Reguły sprawdzone przez `POST https://api.github.com/markdown` (`tools/probe_github_math.py`).
GitHub renderuje matematykę MathJaxem i **nie** opakowuje w `math-renderer` przypadków
wymienionych niżej jako błędne.

| Zapis | Czy GitHub renderuje |
| --- | --- |
| inline `$\psi$` w akapicie, w liście, w tabeli, w nagłówku | tak |
| inline w wariancie z backtickami (gdy wzór zawiera znaki kolidujące z Markdownem) | tak |
| blok: otwierające `$$` w osobnej linii, treść, zamykające `$$` w osobnej linii | tak |
| blok: `$$` w osobnej linii, treść, a zamykające `$$` na końcu ostatniej linii treści | tak |
| blok: `$$treść` na początku linii, a zamykające `$$` w osobnej linii | tak |
| blok `$$treść$$` w jednej linii, w osobnym akapicie | tak |
| blok: **oba** delimitery doklejone do treści (`$$treść` … `treść$$`) | **nie** |
| blok `$$` w tym samym akapicie co tekst (bez pustej linii przed nim) | **nie** |
| blok `$$` w elemencie listy bez pustej linii przed nim | **nie** |
| blok `$$` wewnątrz cytatu | **nie** |
| blok `$$` w wierszu tabeli | **nie** |
| inline `$...$` złamane na dwa wiersze | **nie** |
| `\operatorname{...}` | **nie** — błąd „the following macros are not allowed: operatorname”; używaj `\mathrm{...}` |
| `\tag{N}` we wzorze | ryzykowne — numer wpisuj jako `\qquad (N)` wewnątrz wzoru |
| goła kreska pionowa wewnątrz wzoru w tabeli (zamiast `\lvert`) | **nie** (rozbija tabelę) |
| znak `*` wewnątrz wzoru (`z^*`) | **nie**, gdy w akapicie są dwa takie znaki — Markdown robi z nich kursywę, a w bloku `$$` zamienia `*` na `_` (błąd „Missing open brace for superscript”); pisz `z^{\ast}` |
| `\\` (podwójny backslash) lub środowisko macierzowe w matematyce **inline** | **nie** — taki wzór nie jest rozpoznawany; macierze tylko w bloku `$$` |
| macierz w komórce tabeli | **nie** — wynieś macierz do bloku `$$` pod tabelą |

Praktyczne konsekwencje dla autora:

1. **Blok `$$` zapisuj w formie kanonicznej**: `$$` w osobnej linii, treść, `$$` w osobnej
   linii. Wystarczy, że jeden delimiter stoi w osobnej linii — ale oba doklejone do treści
   to błąd, który nie renderuje się wcale.
2. **Zostaw pustą linię przed blokiem i po nim** (wyjątkiem jest blok zaraz po nagłówku).
3. **Inline `$...$` musi zmieścić się w jednej linii.** Długi wzór przenieś do bloku `$$`.
4. **Zamiast `\operatorname{Tr}` pisz `\mathrm{Tr}`**, a zamiast `\tag{3}` — `\qquad (3)`
   wewnątrz wzoru.
5. **Zamiast `*` pisz `\ast`** (np. `z^{\ast}`), bo `*` w matematyce walczy z kursywą Markdowna.
6. **Macierze (`\begin{pmatrix}`, `cases`, `aligned`, …) tylko w blokach `$$`.**
   W zdaniu zostaw odnośnik, np. „macierz $A$ ma postać:”, a wzór umieść w bloku pod akapitem.
   To samo dotyczy tabel: w komórce opis, macierz w bloku pod tabelą.
7. W tabelach używaj `\lvert`/`\rvert`, nigdy gołego `|`.
6. Blok wewnątrz elementu listy zapisuj z pustą linią przed nim i wcięciem.

Automatyczna kontrola:

- `python tools/audit_github_math.py` — reguły zapisu bloków i tabel (0 problemów),
- `python tools/audit_content.py --math` — składnia LaTeX, w tym `\operatorname` i `\tag`.

Narzędzia naprawcze: `tools/fix_display_math.py` (forma kanoniczna bloków `$$`),
`tools/fix_math_wrap.py` (scala inline złamane na dwa wiersze),
`tools/fix_tex_macros.py` (`\operatorname` → `\mathrm`, `\tag` → `\qquad (N)`),
`tools/probe_github_math.py` (sonda: co faktycznie renderuje GitHub),
`tools/list_tex_macros.py` (inwentarz makr używanych w repo).



