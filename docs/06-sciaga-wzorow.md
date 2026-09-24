# Ściąga wzorów

Jedno miejsce ze wszystkimi wzorami z przewodnika. **Zasada użycia:** nie wkuwaj,
tylko przy każdym wzorze umiej odpowiedzieć „skąd to wynika i kiedy to stosuję”.
Odsyłacze prowadzą do rozdziałów z wyprowadzeniami.

## 1. Liczby zespolone (rozdział 01)

| Wzór | Zapis | Uwaga |
| --- | --- | --- |
| Postać algebraiczna | $z=a+bi$, $i^2=-1$ | |
| Sprzężenie | $z^*=a-bi$ | $zz^*=\lvert z\rvert^2$ |
| Moduł | $\lvert z\rvert=\sqrt{a^2+b^2}$ | nieujemny |
| Postać biegunowa | $z=r e^{i\varphi}$, $r=\lvert z\rvert$, $\varphi=\arg z$ | $\varphi\in(-\pi,\pi]$ |
| Wzór Eulera | $e^{i\varphi}=\cos\varphi+i\sin\varphi$ | podstawa wszystkiego |
| Wzór de Moivre'a | $(\cos\varphi+i\sin\varphi)^n=\cos n\varphi+i\sin n\varphi$ | czyli $(e^{i\varphi})^n=e^{in\varphi}$ |
| Pierwiastki | $z^{1/n}=\sqrt[n]{r}\,e^{i(\varphi+2\pi k)/n}$, $k=0,\dots,n-1$ | $n$ różnych pierwiastków |
| Odwrotność | $1/z=z^*/\lvert z\rvert^2$ | |
| Nierówność trójkąta | $\lvert z+w\rvert\le\lvert z\rvert+\lvert w\rvert$ | |
| Tożsamości trygonometryczne | $\cos\varphi=\frac{e^{i\varphi}+e^{-i\varphi}}{2}$, $\sin\varphi=\frac{e^{i\varphi}-e^{-i\varphi}}{2i}$ | świetne do całek |
| Amplituda kwantowa | $\lvert\psi\rangle=\sum_k c_k\lvert k\rangle$, $\sum_k\lvert c_k\rvert^2=1$ | $c_k$ zespolone, faza ma znaczenie |

**Kiedy używać:** zawsze, gdy w zadaniu jest faza, interferencja, $e^{i\theta}$ albo
prawdopodobieństwo $\lvert c\rvert^2$.

## 2. Algebra liniowa (rozdział 02)

| Wzór | Zapis |
| --- | --- |
| Iloczyn skalarny | $\langle\phi\vert\psi\rangle=\sum_k \phi_k^*\psi_k$ |
| Norma | $\lVert\psi\rVert=\sqrt{\langle\psi\vert\psi\rangle}$ |
| Sprzężenie hermitowskie | $(A^\dagger)_{ij}=A_{ji}^*$ |
| Hermitowskość | $A^\dagger=A$ (obserwable, rzeczywiste wartości własne) |
| Unitarność | $U^\dagger U=UU^\dagger=I$ (zachowuje normę) |
| Równanie własne | $A\lvert a\rangle=a\lvert a\rangle$ |
| Tw. spektralne | $A=\sum_a a\lvert a\rangle\langle a\rvert$ dla $A$ hermitowskiego |
| Rozkład w bazie własnej | $\lvert\psi\rangle=\sum_a c_a\lvert a\rangle$, $c_a=\langle a\vert\psi\rangle$ |
| Diagonalizacja | $A=U D U^\dagger$, $D=\mathrm{diag}(\lambda_i)$ |
| Ślad | $\mathrm{Tr}\,A=\sum_i A_{ii}=\sum_i\lambda_i$; $\mathrm{Tr}(AB)=\mathrm{Tr}(BA)$ |
| Wyznacznik | $\det(AB)=\det A\det B$; $\det U=e^{i\alpha}$ dla unitarnej |
| Macierz odwrotna 2×2 | $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}=\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ |
| Iloczyn tensorowy | $(A\otimes B)_{(ik),(jl)}=A_{ij}B_{kl}$ |
| Własność kron | $(A\otimes B)(C\otimes D)=(AC)\otimes(BD)$ |
| Eksponenta | $e^{A}=\sum_k A^k/k!$; dla hermitowskiego $H$: $U(t)=e^{-iHt/\hbar}$ |
| Diagonalna eksponenta | jeśli $A=UDU^\dagger$, to $e^{A}=Ue^{D}U^\dagger$ |
| Rozkład Schmidta | $\lvert\psi\rangle=\sum_i s_i\lvert u_i\rangle\otimes\lvert v_i\rangle$, $s_i\ge0$ |

**Macierze Pauliego**

$$
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
I=\begin{pmatrix}1&0\\0&1\end{pmatrix}
$$

- $\sigma_i^2=I$, $\{\sigma_i,\sigma_j\}=2\delta_{ij}I$ (antykomutacja),
  $[\sigma_i,\sigma_j]=2i\varepsilon_{ijk}\sigma_k$.
- $[X,Y]=2iZ$, $[Y,Z]=2iX$, $[Z,X]=2iY$.
- $XY=iZ$, $YZ=iX$, $ZX=iY$ (cyklicznie), $XYZ=iI$.
- Sfera Blocha: $\lvert\psi\rangle=\cos\frac{\theta}{2}\lvert0\rangle+e^{i\varphi}\sin\frac{\theta}{2}\lvert1\rangle$.

**Szybkie tożsamości bramek**

$$
HXH=Z,\quad HZH=X,\quad H YH=-Y,\quad H^2=I,\quad XZX=-Z,\quad H=\tfrac{1}{\sqrt2}(X+Z)
$$

$$
H^{\otimes 2}\lvert00\rangle=\tfrac12\big(\lvert00\rangle+\lvert01\rangle+\lvert10\rangle+\lvert11\rangle\big)
$$

$$
S=T^2,\quad T^2S=Z\cdot e^{i\pi/4}\ \text{(do fazy)}\quad\text{— uwaga na fazy globalne}
$$

## 3. Rachunek prawdopodobieństwa i statystyka (rozdział 03)

| Pojęcie | Wzór |
| --- | --- |
| Prawdopodobieństwo warunkowe | $P(A\lvert B)=P(A\cap B)/P(B)$ |
| Niezależność | $P(A\cap B)=P(A)P(B)$ |
| Wzór na prawdopodobieństwo całkowite | $P(A)=\sum_i P(A\lvert B_i)P(B_i)$ |
| Wzór Bayesa | $P(A\lvert B)=\dfrac{P(B\lvert A)P(A)}{P(B)}$ |
| Wartość oczekiwana | $\mathbb{E}[X]=\sum_i x_i p_i$ |
| Wariancja | $\mathrm{Var}(X)=\mathbb{E}[X^2]-\mathbb{E}[X]^2$ |
| Kowariancja | $\mathrm{Cov}(X,Y)=\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y]$ |
| Rozkład dwumianowy | $P(k)=\binom nk p^k(1-p)^{n-k}$, $\mathbb{E}=np$, $\mathrm{Var}=np(1-p)$ |
| Rozkład Poissona | $P(k)=\lambda^k e^{-\lambda}/k!$, $\mathbb{E}=\mathrm{Var}=\lambda$ |
| Rozkład normalny | $\mathcal{N}(\mu,\sigma)$: gęstość $\frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}$ |
| Prawo wielkich liczb | $\bar X_n\;\xrightarrow{n\to\infty}\;\mu$ |
| CTG | $\bar X_n\approx\mathcal{N}(\mu,\sigma^2/n)$ dla dużych $n$ |
| Rozkład próbkowy | $\sigma_{\bar X}=\sigma/\sqrt n$ |
| Propagacja niepewności | $\sigma_f^2=\sum_i\left(\frac{\partial f}{\partial x_i}\right)^2\sigma_{x_i}^2$ (dla niezależnych) |
| Entropia Shannona | $H=-\sum_i p_i\log_2 p_i$ |
| Test $\chi^2$ | $\chi^2=\sum_i\frac{(O_i-E_i)^2}{E_i}$, $\mathrm{ndof}=\text{liczba punktów}-\text{liczba parametrów}$ |
| Niepewność standardowa | $u_c=\sqrt{\sum_i u_i^2}$ (suma geometryczna) |

**Kluczowa intuicja kwantowa:** pomiar jednorazowy daje wynik probabilistyczny;
$\langle A\rangle$ to średnia z **wielu** pomiarów, a nie „wynik jednego pomiaru”.

## 4. Elementy analizy matematycznej (rozdział 04)

| Wzór | Zapis |
| --- | --- |
| Pochodna złożenia | $(f\circ g)'=f'(g)g'$ |
| Pochodna iloczynu | $(fg)'=f'g+fg'$ |
| Całkowanie przez części | $\int u\,dv=uv-\int v\,du$ |
| Podstawienie | $\int f(g(x))g'(x)\,dx=\int f(u)\,du$ |
| Szereg Taylora | $f(x)=\sum_{n\ge0}\frac{f^{(n)}(a)}{n!}(x-a)^n$ |
| Przybliżenie liniowe | $f(x)\approx f(a)+f'(a)(x-a)$ dla $x\approx a$ |
| $e^x$, $\sin x$ | $e^x=1+x+\frac{x^2}{2}+\dots$, $\sin x=x-\frac{x^3}{6}+\dots$ |
| Równanie liniowe I rzędu | $y'+ay=b\ \Rightarrow\ y=C e^{-ax}+b/a$ |
| Oscylator (II rząd) | $y''+\omega^2 y=0\ \Rightarrow\ y=A\cos\omega t+B\sin\omega t$ |
| Tłumienie | $y''+2\gamma y'+\omega_0^2y=0$, $\omega_d=\sqrt{\omega_0^2-\gamma^2}$ |
| Szereg Fouriera | $f(x)=\frac{a_0}{2}+\sum_{n\ge1}\big(a_n\cos n x+b_n\sin n x\big)$ |
| Transformata Fouriera | $\tilde f(k)=\frac{1}{\sqrt{2\pi}}\int f(x)e^{-ikx}dx$ |
| Delta Diraca | $\int\delta(x-a)f(x)dx=f(a)$; $\delta(x)=\frac{1}{2\pi}\int e^{ikx}dk$ |
| Całka Gaussa | $\int_{-\infty}^{\infty}e^{-ax^2}dx=\sqrt{\pi/a}$ |
| Gauss z linią | $\int_{-\infty}^{\infty}e^{-ax^2+bx}dx=\sqrt{\pi/a}\;e^{b^2/4a}$ |
| Tw. Parsevala | $\int\lvert f\rvert^2dx=\int\lvert\tilde f\rvert^2dk$ |
| Nieoznaczność Fouriera | $\Delta x\,\Delta k\ge\frac12$ |

**Ważne dla fizyki:** operator pędu w reprezentacji położeniowej
$\hat p=-i\hbar\frac{d}{dx}$; relacja $E=\hbar\omega$, $p=\hbar k$.

## 5. Mechanika kwantowa (rozdział 05)

| Wzór | Zapis |
| --- | --- |
| Równanie Schrödingera | $i\hbar\frac{\partial}{\partial t}\Psi=\hat H\Psi$ |
| Stany stacjonarne | $\hat H\psi=E\psi$, $\Psi(x,t)=\psi(x)e^{-iEt/\hbar}$ |
| Normalizacja | $\int\lvert\psi\rvert^2dx=1$ |
| Prawdopodobieństwo położenia | $dP=\lvert\psi(x)\rvert^2dx$ |
| Wartość oczekiwana | $\langle A\rangle=\int\psi^*\hat A\psi\,dx$ |
| Rozkład na bazy | $\psi=\sum_n c_n\psi_n$, $c_n=\langle\psi_n\vert\psi\rangle$, $P_n=\lvert c_n\rvert^2$ |
| Komutator | $[\hat A,\hat B]=\hat A\hat B-\hat B\hat A$ |
| Zasada nieoznaczoności | $\Delta A\,\Delta B\ge\frac12\lvert\langle[\hat A,\hat B]\rangle\rvert$ |
| $[\hat x,\hat p]$ | $=i\hbar$ (stąd $\Delta x\Delta p\ge\hbar/2$) |
| Tw. Ehrenfesta | $\frac{d}{dt}\langle A\rangle=\frac{1}{i\hbar}\langle[A,\hat H]\rangle+\langle\partial_tA\rangle$ |
| Ewolucja stanu | $\lvert\psi(t)\rangle=e^{-i\hat Ht/\hbar}\lvert\psi(0)\rangle$ |
| Studnia nieskończona | $\psi_n=\sqrt{\frac2L}\sin\frac{n\pi x}{L}$, $E_n=\frac{n^2\pi^2\hbar^2}{2mL^2}$ |
| Oscylator harmoniczny | $E_n=\hbar\omega(n+\tfrac12)$, $\omega=\sqrt{k/m}$ |
| Bariera, tunelowanie | $T\approx e^{-2\kappa a}$, $\kappa=\frac{\sqrt{2m(V_0-E)}}{\hbar}$ |
| Atom wodoru | $E_n=-\frac{13{,}6\,\text{eV}}{n^2}$, $L^2$: $\hbar^2 l(l+1)$ |
| Foton | $E=h\nu=\hbar\omega$, $p=h/\lambda=\hbar k$ |
| Prawo Malusa | $I=I_0\cos^2\theta$; dla fotonu $P=\cos^2\theta$ |
| Spin-1/2 | $S_z=\frac\hbar2\sigma_z$, stany $\lvert+\rangle,\lvert-\rangle$ = kubit |
| Dudnienia | $\lvert\psi(t)\rangle=\frac{1}{\sqrt2}(e^{-iE_1t/\hbar}\lvert1\rangle+e^{-iE_2t/\hbar}\lvert2\rangle)$ → częstość $\Delta E/\hbar$ |

## 6. Pomiar i macierz gęstości (rozdziały 06, 17)

| Wzór | Zapis |
| --- | --- |
| Pomiar rzutowy | $P(m)=\lvert\langle m\vert\psi\rangle\rvert^2$, stan po pomiarze $\lvert m\rangle$ |
| Pomiar obserwabli | $A=\sum_a a\lvert a\rangle\langle a\rvert$, $P(a)=\lvert\langle a\vert\psi\rangle\rvert^2$ |
| $\langle A\rangle$ | $=\sum_a a P(a)=\langle\psi\vert A\vert\psi\rangle$ |
| Pomiar w bazie X | $P(+)=\lvert\langle+\vert\psi\rangle\rvert^2$, $\lvert\pm\rangle=\frac{1}{\sqrt2}(\lvert0\rangle\pm\lvert1\rangle)$ |
| Prawdopodobieństwo częściowe | $P(a)=\mathrm{Tr}(P_a\rho)$, $P_a=\lvert a\rangle\langle a\rvert$ |
| Macierz gęstości | $\rho=\sum_k p_k\lvert\psi_k\rangle\langle\psi_k\rvert$, $\mathrm{Tr}\rho=1$ |
| Stan czysty | $\mathrm{Tr}\rho^2=1$ |
| Współrzędne Blocha | $r_x=2\,\mathrm{Re}\,\rho_{01}$, $r_y=-2\,\mathrm{Im}\,\rho_{01}$, $r_z=\rho_{00}-\rho_{11}$ |
| Ślad częściowy | $(\mathrm{Tr}_B\rho)_{ij}=\sum_k \rho_{ik,jk}$ (dla 2 kubitów) |
| Entropia von Neumanna | $S(\rho)=-\mathrm{Tr}(\rho\log_2\rho)=-\sum_i\lambda_i\log_2\lambda_i$ |
| Splątanie z rozkładu Schmidta | $\log_2$ liczby niezerowych $s_i$ > 1 ⇒ stan splątany |
| Kanał kwantowy (Kraus) | $\mathcal{E}(\rho)=\sum_iK_i\rho K_i^\dagger$, $\sum_iK_i^\dagger K_i=I$ |
| Kanał depolaryzujący | $\mathcal{E}(\rho)=(1-p)\rho+\frac p3(X\rho X+Y\rho Y+Z\rho Z)$ |
| Tłumienie amplitudy | $K_0=\begin{pmatrix}1&0\\0&\sqrt{1-\gamma}\end{pmatrix}$, $K_1=\begin{pmatrix}0&\sqrt\gamma\\0&0\end{pmatrix}$ |
| Tłumienie fazy | $\rho\to\begin{pmatrix}\rho_{00}&(1-\gamma)\rho_{01}\\(1-\gamma)\rho_{10}&\rho_{11}\end{pmatrix}$ |
| Dekoherencja w czasie | $\rho_{01}(t)=\rho_{01}(0)e^{-t/T_2}$ |
| Zasada Landauera | $W\ge k_BT\ln2$ (koszt usunięcia 1 bitu) |

**Przykład dla $|\Phi^+\rangle=\frac{1}{\sqrt2}(|00\rangle+|11\rangle)$:**

$$
\rho=\frac12\begin{pmatrix}1&0&0&1\\0&0&0&0\\0&0&0&0\\1&0&0&1\end{pmatrix}
\ \Rightarrow\ \rho_A=\mathrm{Tr}_B\rho=\begin{pmatrix}\frac12&0\\0&\frac12\end{pmatrix}=\frac I2
\ \Rightarrow\ S(\rho_A)=1\ \text{bit (maksimum splątania).}
$$

## 7. Kwantowa teoria informacji (rozdział 07)

| Wzór | Zapis |
| --- | --- |
| Zakaz klonowania | nie istnieje $U$, które dla **wszystkich** $\lvert\psi\rangle$ spełnia $U(\lvert\psi\rangle\otimes\lvert0\rangle)=\lvert\psi\rangle\otimes\lvert\psi\rangle$ |
| Dowód w skrócie | unitarność zachowuje iloczyn skalarny, a klonowanie wymagałoby $\langle\psi\vert\phi\rangle=(\langle\psi\vert\phi\rangle)^2$ |
| Nierozróżnialność | jeśli $\lvert\langle\psi\vert\phi\rangle\rvert<1$, to jednym pomiarem nie rozróżnisz stanów z pewnością 1 |
| Optymalne rozróżnianie | $p_{\text{sukces}}\le\frac12+\frac12\sqrt{1-\lvert\langle\psi\vert\phi\rangle\rvert^2}$ |
| Ograniczenie Holevo | dostępna informacja klasyczna $\chi\le S(\rho)$ (entropia von Neumanna) |
| Teleportacja | 1 e-bit + 2 bity klasyczne → przeniesienie 1 kubita |
| Supergęste kodowanie | 1 e-bit + 1 przesłany kubit → 2 bity klasyczne |
| Dystans śladowy | $D(\rho,\sigma)=\frac12\mathrm{Tr}\lvert\rho-\sigma\rvert$ |
| Wierność | $F(\rho,\sigma)=\left(\mathrm{Tr}\sqrt{\sqrt\rho\,\sigma\sqrt\rho}\right)^2$; dla czystych $F=\lvert\langle\psi\vert\phi\rangle\rvert^2$ |
| Związek $F$–$D$ | $1-\sqrt{F}\le D\le\sqrt{1-F}$ |

## 8. Obwody i bramki (rozdział 06)

- Kolejność: $\lvert\psi_{\text{końc}}\rangle=U_k\cdots U_2U_1\lvert\psi_0\rangle$ —
  bramka wykonana jako pierwsza stoi **najbliżej** wektora stanu.
- Kolejność kubitów (małoendianowa): bramka na kubicie 0 (dolnym) → $I\otimes G$;
  bramka na kubicie 1 (górnym) → $G\otimes I$; CNOT (kontrola górny, cel dolny) →
  $\lvert0\rangle\langle0\rvert\otimes I+\lvert1\rangle\langle1\rvert\otimes X$.
- CNOT w bazie $\{\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle\}$
  ma postać $\begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{pmatrix}$
  (zamienia $\lvert10\rangle\leftrightarrow\lvert11\rangle$).
- Zbiór uniwersalny: $\{H,T,\text{CNOT}\}$.
- Bramka kontrolowana-$U$: $C_U=\lvert0\rangle\langle0\rvert\otimes I+\lvert1\rangle\langle1\rvert\otimes U$.
- Kluczowe tożsamości:
  - $HZH=X$, $HXH=Z$, $HYH=-Y$, $H^2=I$, $XZX=-Z$, $S=T^2$;
  - $H^{\otimes2}\,\text{CNOT}_{12}\,H^{\otimes2}=\text{CNOT}_{21}$;
  - $\text{SWAP}$ z trzech CNOT-ów: $\text{CNOT}_{12}\text{CNOT}_{21}\text{CNOT}_{12}$;
  - $e^{-i\theta Z/2}=R_Z(\theta)$.
- Stany Bella: $\lvert\Phi^\pm\rangle=\frac{1}{\sqrt2}(\lvert00\rangle\pm\lvert11\rangle)$,
  $\lvert\Psi^\pm\rangle=\frac{1}{\sqrt2}(\lvert01\rangle\pm\lvert10\rangle)$;
  z $\lvert00\rangle$: $H$ na kontroli, potem CNOT.

## 9. Splątanie i twierdzenie Bella (rozdział 09)

| Wzór | Zapis |
| --- | --- |
| Stan iloczynowy | $\lvert\psi\rangle=\lvert a\rangle\otimes\lvert b\rangle$ |
| Kryterium splątania | brak rozkładu iloczynowego ⟺ rząd macierzy współczynników $>1$ ⟺ liczba niezerowych $s_i>1$ |
| Kryterium PPT (2 kubity) | stan separowalny ⟺ $\rho^{T_B}\succeq0$ (Peres–Horodecki) |
| CHSH | $S=\lvert E(a,b)-E(a,b')+E(a',b)+E(a',b')\rvert$ |
| Granica klasyczna | $S\le2$ (modele zmiennych ukrytych) |
| Maksimum kwantowe | $S_{\max}=2\sqrt2\approx2{,}828$ dla kątów $0°,45°,22{,}5°,67{,}5°$ |
| Korelacja dla stanu Bella | polaryzacyjnie $E(a,b)=-\cos\big(2(a-b)\big)$; spinowo (kąty na sferze Blocha) $E(\hat a,\hat b)=-\hat a\cdot\hat b$ |
| Monogamia (Coffman–Kundu–Wootters) | $C_{AB}^2+C_{AC}^2\le C_{A\lvert BC}^2$ |
| Concurrence (2 kubity) | $C=\max\left(0,\lambda_1-\lambda_2-\lambda_3-\lambda_4\right)$ |
| Entropia splątania | $E=-\sum_i s_i^2\log_2 s_i^2$ z rozkładu Schmidta |

## 10. Kryptografia kwantowa (rozdział 10)

- **Szyfr Vernama:** $C=M\oplus K$ z losowym, jednorazowym kluczem tej samej
  długości → doskonała tajność ($H(M\lvert C)=H(M)$).
- **BB84 — cztery stany:** baza $Z$: $\lvert0\rangle$ (bit 0), $\lvert1\rangle$ (bit 1);
  baza $X$: $\lvert+\rangle$ (bit 0), $\lvert-\rangle$ (bit 1). Nadawca losuje bit i
  bazę, odbiorca losuje bazę pomiaru. Publicznie ujawniają **tylko bazy** — bity z
  zgodnych baz tworzą klucz (sifting).
- **QBER** = odsetek błędów w kluczu. Próg bezpieczeństwa dla BB84 ≈ 11%;
  powyżej tego progu klucz odrzucamy.
- **Intercept-resend:** dla jednego podsłuchiwanego bitu szansa błędu $=1/4$,
  więc pełny podsłuch daje $QBER\approx25\%$; przy 10% podsłuchu $QBER\approx2{,}5\%$,
  a wykrycie z próbki $n$ bitów: $P=1-\left(\tfrac34\right)^n$.
- Protokoły pokrewne: **B92** (dwa stany nieortogonalne), **E91** (splątanie + CHSH).
- Etapy po transmisji: sifting → uzgadnianie klucza (reconciliation) → wzmocnienie
  prywatności (privacy amplification).

## 11. Metrologia kwantowa (rozdział 11)

| Wzór | Zapis |
| --- | --- |
| Nierówność Craméra–Rao | $\mathrm{Var}(\hat\theta)\ge\frac{1}{N\,F(\theta)}$ dla $N$ pomiarów |
| Klasyczna informacja Fishera | $F(\theta)=\sum_i\frac{1}{p_i}\left(\frac{\partial p_i}{\partial\theta}\right)^2$ |
| Kwantowa informacja Fishera | $F_Q=\mathrm{Tr}(\rho L^2)$, gdzie $\rho L+L\rho=2\,\partial_\theta\rho$ |
| Granica śrutowa (shot noise) | $\Delta\varphi\ge\frac{1}{\sqrt{N}}$ (klasyczne zasoby, np. $N$ fotonów) |
| Granica Heisenberga | $\Delta\varphi\ge\frac{1}{N}$ (stan GHZ / N00N) |
| Stan N00N | $\lvert\text{N00N}\rangle=\frac{1}{\sqrt2}\left(\lvert N,0\rangle+\lvert0,N\rangle\right)$ |
| Interferometr | $P\propto\cos^2\frac{\Delta\varphi}{2}$, czułość $\propto\sin\frac{\Delta\varphi}{2}$ |
| Ściśnięcie (squeezing) | $\Delta\varphi\approx\frac{1}{\sqrt N\,e^{r}}$ — redukcja szumu o $e^{-r}$ |

## 12. Korekcja i mitygacja błędów (rozdział 13)

- **Kod bit-flip (powtarzalny, [[3,1,3]]):** $\lvert0\rangle_L=\lvert000\rangle$,
  $\lvert1\rangle_L=\lvert111\rangle$. Syndromy z pomiarów $Z_1Z_2$ i $Z_2Z_3$:
  $00$ — brak błędu, $10$ — błąd na kubicie 1, $11$ — na kubicie 2, $01$ — na kubicie 3.
- **Kod phase-flip:** ta sama konstrukcja w bazie $\lvert\pm\rangle$.
- **Kod Shora [[9,1,3]]:** 9 kubitów = 3 bloki phase-flip, każdy z 3 kubitów
  bit-flip; koryguje dowolny błąd jednego kubita.
- **Kod Steane'a [[7,1,3]]:** 7 kubitów, dystans 3, korekcja jednego błędu.
- **Kod powierzchniowy (surface code):** dystans $d$ koryguje $\lfloor(d-1)/2\rfloor$
  błędów; potrzeba $\approx2d^2$ kubitów fizycznych (dane + ancilla).
- **Twierdzenie o progu:** jeśli błąd każdego elementu $p<p_{th}$ (zwykle
  $\sim0{,}1\%$–$1\%$), to błąd logiczny maleje jak $(p/p_{th})^{(d+1)/2}$.
- **Mitygacja:** ZNE (pomiar dla szumu $2\lambda,3\lambda$ i ekstrapolacja do
  $\lambda=0$); kalibracja $P_{\text{zmierz}}=AP_{\text{ideal}}+b$ i odwracanie
  macierzy kalibracyjnej; twirling i odrzucanie wyników.

## 13. Stałe i przydatne liczby

| Stała | Wartość |
| --- | --- |
| $\hbar$ | $1{,}054\,571\,8\times10^{-34}$ J·s |
| $h$ | $6{,}626\,070\,15\times10^{-34}$ J·s |
| $k_B$ | $1{,}380\,649\times10^{-23}$ J/K |
| $e$ | $1{,}602\,176\,634\times10^{-19}$ C |
| $\mu_B$ | $9{,}274\times10^{-24}$ J/T |
| $\varepsilon_0$ | $8{,}854\times10^{-12}$ F/m |
| $\ln 2$ | $0{,}6931$ |
| $2\sqrt2$ | $2{,}828\,427$ |
| $\pi$ | $3{,}141\,593$ |

Dla $T=300$ K: $k_BT\approx25{,}9$ meV $\approx4{,}14\times10^{-21}$ J,
a koszt Landauera $k_BT\ln2\approx2{,}87\times10^{-21}$ J na bit.

## 14. Ostatnia powtórka: 12 rzeczy, które trzeba umieć na pamięć

1. $\langle\psi\vert\psi\rangle=1$ oraz $P(a)=\lvert\langle a\vert\psi\rangle\rvert^2$.
2. Macierze $H,X,Y,Z$ i tożsamość $HZH=X$.
3. Kolejność mnożenia w obwodzie oraz macierz CNOT.
4. Stany Bella i fakt, że $\rho_A=I/2$ oznacza maksymalne splątanie.
5. $\langle E\rangle=\sum_n\lvert c_n\rvert^2E_n$ i rozwiązanie studni potencjału.
6. Prawo Malusa: $I=I_0\cos^2\theta$.
7. CHSH: granica klasyczna $S\le2$, maksimum kwantowe $S=2\sqrt2$.
8. BB84: cztery stany, sifting, QBER jako detektor podsłuchu.
9. Grover: $\approx\frac\pi4\sqrt N$ iteracji; dla $N=4$ sukces pewny.
10. Cramér–Rao: $\Delta\theta\propto1/\sqrt N$ klasycznie, $\propto1/N$ ze stanem GHZ.
11. Syndromy kodu powtarzalnego 3-kubitowego i poprawka.
12. Zakaz klonowania — dowód przez zachowanie iloczynu skalarnego.



