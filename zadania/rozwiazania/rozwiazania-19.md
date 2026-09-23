# Rozwiązania do rozdziału 19

## Z-19.1

(a) Rozpisujemy $\lvert\psi\rangle_1\lvert\Phi^+\rangle_{23}$ i grupujemy po stanach Bella kubitów 1 i 2
(używając $\lvert00\rangle=\tfrac{1}{\sqrt2}(\lvert\Phi^+\rangle+\lvert\Phi^-\rangle)$,
$\lvert11\rangle=\tfrac{1}{\sqrt2}(\lvert\Phi^+\rangle-\lvert\Phi^-\rangle)$,
$\lvert01\rangle=\tfrac{1}{\sqrt2}(\lvert\Psi^+\rangle+\lvert\Psi^-\rangle)$,
$\lvert10\rangle=\tfrac{1}{\sqrt2}(\lvert\Psi^+\rangle-\lvert\Psi^-\rangle)$):
$$\lvert\Psi\rangle=\tfrac12\Big[\lvert\Phi^+\rangle_{12}(\alpha\lvert0\rangle+\beta\lvert1\rangle)_3
+\lvert\Phi^-\rangle_{12}(\alpha\lvert0\rangle-\beta\lvert1\rangle)_3
+\lvert\Psi^+\rangle_{12}(\beta\lvert0\rangle+\alpha\lvert1\rangle)_3
+\lvert\Psi^-\rangle_{12}(-\beta\lvert0\rangle+\alpha\lvert1\rangle)_3\Big].$$
(b) Z porównania ze stanem wyjściowym: $\lvert\Phi^+\rangle\to I$, $\lvert\Phi^-\rangle\to Z$
(zmienia znak $\beta$), $\lvert\Psi^+\rangle\to X$ (zamienia $\alpha\leftrightarrow\beta$),
$\lvert\Psi^-\rangle\to ZX$.
(c) Wszystkie cztery stany Bella są ortonormalne, a każdy składnik ma amplitudę $\tfrac12$; zatem
$P=\lvert\tfrac12\rvert^2=\tfrac14$ dla każdego wyniku.

**Odpowiedź:** (b) korekty $\mathbf{\{I,Z,X,ZX\}}$; (c) $\mathbf{P=\tfrac14=0{,}25}$.
*Fizycznie:* pomiar Bella nie ujawnia $\alpha,\beta$ — przenosi je w formie „zaszyfrowanej” bramką
Pauliego, którą Bob odwraca po otrzymaniu 2 bitów.

## Z-19.2

(a) $(I\otimes I)\lvert\Phi^+\rangle=\lvert\Phi^+\rangle$,
$(X\otimes I)\lvert\Phi^+\rangle=\lvert\Psi^+\rangle$,
$(Z\otimes I)\lvert\Phi^+\rangle=\lvert\Phi^-\rangle$,
$(ZX\otimes I)\lvert\Phi^+\rangle=-\lvert\Psi^-\rangle$.
(b) Bob mierzy dwa kubity, ale drugi kubit nigdy nie był przesyłany — więc odczytuje **2 bity** z
**jednego** przesłanego kubita.
(c) Bilans: supergęste kodowanie = 1 e-bit + **przesłanie 1 kubita** → 2 bity; teleportacja =
1 e-bit + **2 bity klasyczne** → 1 kubit. To dokładnie odwrotne wymiany tych samych zasobów.

**Odpowiedź:** (a) $\mathbf{\lvert\Phi^+\rangle,\lvert\Psi^+\rangle,\lvert\Phi^-\rangle,\lvert\Psi^-\rangle}$;
(b) $\mathbf{2}$ **bity** z 1 kubita; (c) odwrotność teleportacji.
*Fizycznie:* splątanie pozwala „przenieść” dwa bity klasyczne przez jedną cząstkę kwantową.

## Z-19.3

(a) $11^1=11$, $11^2=121=8\cdot15+1\equiv1\pmod{15}$, więc $r=2$.
(b) $11^{r/2}=11$; $\gcd(11-1,15)=\gcd(10,15)=5$, a $15/5=3$, czyli $15=3\cdot5$.
(c) Dla $a=14$: $14\equiv-1$, $14^2\equiv1$, więc $r=2$, ale $a^{r/2}\equiv-1\pmod{15}$ i
$\gcd(14-1,15)=\gcd(13,15)=1$ — przypadek **pechowy** (nie daje dzielnika); trzeba powtórzyć z innym $a$.

**Odpowiedź:** (a) $\mathbf{r=2}$; (b) $\mathbf{\gcd(10,15)=5}$, $15=3\cdot5$; (c) dla $a=14$
$\gcd=1$ — powtórzenie.
*Fizycznie:* algorytm Shora ma niezerowe prawdopodobieństwo porażki; uruchamiamy go kilka razy,
aż trafimy „dobre” $a$ lub „dobry” wynik pomiaru.

## Z-19.4

(a) $\theta=\arcsin(1/4)=0{,}2527$; $k_{\rm opt}=\mathrm{round}\big(\tfrac\pi4\cdot4-\tfrac12\big)=\mathrm{round}(2{,}642)=3$;
$P(3)=\sin^2(7\theta)=\sin^2(1{,}7688)=0{,}9613$.
(b) $P(4)=\sin^2(9\theta)=\sin^2(2{,}2741)=0{,}5817$ — mniej niż w (a).
(c) Każda iteracja obraca wektor o $2\theta$; po $k_{\rm opt}$ jesteśmy najbliżej rozwiązania, a
kolejne obroty oddalają nas od niego (amplituda $=\sin((2k+1)\theta)$ maleje).

**Odpowiedź:** (a) $\mathbf{\theta=0{,}2527}$, $\mathbf{k_{\rm opt}=3}$, $\mathbf{P=0{,}961}$;
(b) $\mathbf{P(4)=0{,}582}$; (c) nadmiar iteracji zmniejsza amplitudę rozwiązania.
*Fizycznie:* Grover to obrót w 2-wymiarowej podprzestrzeni — nie „coraz lepsze przybliżenie”, lecz
oscylacja wokół optimum.

## Z-19.5

(a) Oba stany wejściowe są czyste, więc $\sum_ip_iS(\rho_i)=0$ i
$\chi=S(\rho_{\rm avg})$. Macierz
$$\rho_{\rm avg}=\tfrac12\lvert0\rangle\langle0\rvert+\tfrac12\lvert+\rangle\langle+\rvert=\begin{pmatrix}0{,}75&0{,}25\\0{,}25&0{,}25\end{pmatrix}$$
ma wartości własne $0{,}8536$ i $0{,}1464$, więc
$\chi=-0{,}8536\log_20{,}8536-0{,}1464\log_20{,}1464=0{,}6009$ bita.
(b) $\chi=0{,}6009<1=\log_2 2$ — informacja jest **mniejsza** niż przy dwóch stanach ortogonalnych.
(c) Dwa nieortogonalne „pół-bity” niosą tylko $0{,}60$ bita, bo nie da się ich rozróżnić jednym
pomiarem — nieortogonalność „zjada” część informacji.

**Odpowiedź:** (a) $\mathbf{\chi=0{,}601}$ **bita**; (b) $\mathbf{\chi<1}$;
(c) nieortogonalność ogranicza odczyt do $0{,}60$ bita.
*Fizycznie:* to twierdzenie Holevo w praktyce — $n$ kubitów nie zastąpi $2n$ bitów klasycznych.

## Z-19.6

(a) T-count $\approx3\log_2(1/\varepsilon)$: dla $\varepsilon=10^{-4}$
$3\log_2(10^4)=3\cdot13{,}29=39{,}9\approx40$; dla $\varepsilon=10^{-8}$
$3\log_2(10^8)=3\cdot26{,}58=79{,}7\approx80$.
(b) Koszt jest logarytmiczny, bo dokładność poprawia się **geometrycznie**: każdy dodatkowy „poziom”
obwodu zmniejsza błąd o stały czynnik, więc na każde $\times10$ dokładności wystarczy stała liczba
bramek — a nie liczba rosnąca liniowo.
(c) Magic states dostarczają „nie-Cliffordowskiej” części — są wstrzykiwane pomiarem, by zrealizować
bramkę $T$ w sposób odporny na błędy; ich produkcja (destylacja) jest głównym kosztem.

**Odpowiedź:** (a) $\mathbf{\approx40}$ ($\varepsilon=10^{-4}$) i $\mathbf{\approx80}$
($\varepsilon=10^{-8}$); (b) geometryczny (log) wzrost dokładności; (c) źródło bramek $T$.
*Fizycznie:* aproksymacja bramek to koszt „tłumaczenia” algorytmu na sprzęt; T-count mówi, ile
„magii” trzeba dokupić.

## Z-19.7

(a) $\mathrm{P}\subseteq\mathrm{BPP}\subseteq\mathrm{BQP}\subseteq\mathrm{PSPACE}$; klasa NP jest
osobną gałęzią — nie wiadomo, jak się ma do BQP (oczekuje się, że $\mathrm{NP}\not\subseteq\mathrm{BQP}$).
(b) Nie: faktoryzacja jest w BQP, ale **nie jest znana** jako NP-zupełna. Gdyby była NP-zupełna, to
BQP zawierałoby NP-zupełny problem, co uzna się za nieprawdziwe — dlatego Shor nie „rozwiąże NP”.
(c) QMA to kwantowy odpowiednik NP: weryfikator kwantowy przyjmuje **kwantowy** dowód. Problem
lokalnego Hamiltona (znalezienie energii stanu podstawowego) jest QMA-zupełny, co pokazuje, że
przewidywanie fizyki kwantowej jest trudne nawet dla komputerów kwantowych.

**Odpowiedź:** (a) łańcuch jak wyżej; (b) nie — nie jest NP-zupełna; (c) QMA = kwantowy certyfikat,
lokalny Hamilton ∈ QMA-zupełne.
*Fizycznie:* komputer kwantowy przyspiesza **konkretne** problemy; nie „rozwiąże wszystkiego”.

## Z-19.8

(a) $t=8$ kubitów daje dokładność $\Delta\varphi\sim2^{-8}=0{,}0039$.
(b) Dla $\varphi=\tfrac14$ najbardziej prawdopodobny wynik to $m=\varphi\cdot2^t=0{,}25\cdot256=64$
(czyli $64/256=\tfrac14$ dokładnie).
(c) W Shorze estymacja fazy (na kontrolowanych mnożeniach $a^{2^j}$) pozwala odczytać $s/r$, a
stąd okres $r$ — to dokładnie „odwrotna QFT” z podsekcji 3.4.

**Odpowiedź:** (a) $\mathbf{\sim0{,}0039}$; (b) $\mathbf{m=64}$ ($\varphi=0{,}25$);
(c) odczyt $s/r$ → okres → faktoryzacja.
*Fizycznie:* estymacja fazy to „miernik” wartości własnych unitarnych — wspólny mianownik Shora i HHL.