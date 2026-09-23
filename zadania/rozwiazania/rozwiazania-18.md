# Rozwiązania do rozdziału 18

## Z-18.1

(a) Stany $\lvert+\rangle$ i $\lvert0\rangle$ są **czyste** (rząd 1), więc $S=0$ w obu przypadkach.
(b) $\tfrac I2$ ma wartości własne $\tfrac12,\tfrac12$:
$S=-\tfrac12\log_2\tfrac12-\tfrac12\log_2\tfrac12=1$ bit.
(c) $\rho=\mathrm{diag}(0{,}75;0{,}25)$:
$S=-0{,}75\log_20{,}75-0{,}25\log_20{,}25=0{,}3113+0{,}5=0{,}8113$ bita — **mniej** niż w (b),
bo stan jest „bliżej” czystego.

**Odpowiedź:** (a) $\mathbf{0}$ i $\mathbf{0}$; (b) $\mathbf{1}$ **bit**; (c) $\mathbf{0{,}811}$ **bita**.
*Fizycznie:* entropia von Neumanna maleje, gdy stan przybliża się do czystego; maksimum ($\log_2 d$)
osiąga dla stanu maksymalnie mieszanego.

## Z-18.2

(a) Dla $\lvert\psi\rangle=0{,}8\lvert00\rangle+0{,}6\lvert11\rangle$:
$C=2\lvert\alpha\beta\rvert=2\cdot0{,}8\cdot0{,}6=0{,}96$;
$E_{\rm f}=h\big(\tfrac{1+\sqrt{1-0{,}96^2}}2\big)=h(0{,}64)=0{,}9427$.
(b) Każdy stan Bella ma $C=1$ (maksymalne splątanie dwóch kubitów).
(c) Stan iloczynowy $\lvert+\rangle\otimes\lvert0\rangle$: $C=0$.

**Odpowiedź:** (a) $\mathbf{C=0{,}96}$, $\mathbf{E_{\rm f}=0{,}9427}$; (b) $\mathbf{C=1}$;
(c) $\mathbf{C=0}$.
*Fizycznie:* $C$ rośnie od zera (iloczyn) do jedynki (stan Bella) — to „miara liniowa” splątania.

## Z-18.3

(a) Dla stanu Wernera $\rho^{T_B}$ ma widmo $\big(\tfrac{1+p}4\big)^{3},\ \tfrac{1-3p}4$; dla $p=0{,}6$:
$\{0{,}4;\ 0{,}4;\ 0{,}4;\ -0{,}2\}$.
(b) Negatywność $N=\tfrac12\big(\sum\lvert\lambda_i\rvert-1\big)=\tfrac12(0{,}4\cdot3+0{,}2-1)=0{,}2$;
log-negatywność $E_N=\log_2(1+2N)=\log_2 1{,}4=0{,}4854$.
(c) $\lambda_{\Phi^+}=p+\tfrac{1-p}4=0{,}7$, więc $C=\max(0,\ 2\cdot0{,}7-1)=0{,}4>0$ — stan **jest**
splątany (zgodnie z $N>0$).

**Odpowiedź:** (a) $\mathbf{\{0{,}4;0{,}4;0{,}4;-0{,}2\}}$; (b) $\mathbf{N=0{,}2}$,
$\mathbf{E_N=0{,}485}$; (c) $\mathbf{C=0{,}4>0}$ — splątany.
*Fizycznie:* domieszka $\tfrac I4$ „rozcieńcza” splątanie, ale do $p=\tfrac13$ stan pozostaje splątany.

## Z-18.4

(a) $S(\rho_A)=h(\cos^2\theta)$ z $\theta=\pi/8$: $\cos^2\theta=0{,}8536$, więc
$\rho_A=\mathrm{diag}(0{,}8536;0{,}1464)$ i $S=0{,}6009$ bita.
(b) Maksimum dla 2 kubitów to $\theta=\pi/4$ (wtedy $S=1$); tu $S=0{,}60<1$, więc splątanie **nie**
jest maksymalne.
(c) $C=2\lvert\cos\theta\sin\theta\rvert=\sin(2\theta)=\sin(\pi/4)=0{,}7071$; z formuły Woottersa
$E_{\rm f}=h\big(\tfrac{1+\sqrt{1-0{,}5}}2\big)=h(0{,}8536)=0{,}6009=S(\rho_A)$ ✓.

**Odpowiedź:** (a) $\mathbf{\rho_A=\mathrm{diag}(0{,}8536;0{,}1464)}$, $\mathbf{S=0{,}6009}$;
(b) nie (max przy $\theta=\pi/4$); (c) $\mathbf{C=0{,}7071}$, $E_{\rm f}=S(\rho_A)$.
*Fizycznie:* dla stanów czystych entropia formacji równa się entropii splątania — dwie drogi, jedna liczba.

## Z-18.5

(a) Dla pary Bella w kanale tłumienia fazy koherencje mnożone są przez $1-\lambda=e^{-t/T_2}$, a
concurrence zależy tylko od nich, więc $C(t)=e^{-t/T_2}$.
(b) Przy $t=1{,}5\,T_2$: $C=e^{-1{,}5}=0{,}2231$.
(c) $e^{-t/T_2}<0{,}1\Rightarrow t/T_2>\ln10=2{,}303$, czyli po $t\approx2{,}30\,T_2$ splątanie spada
poniżej $C=0{,}1$.

**Odpowiedź:** (a) $\mathbf{C(t)=e^{-t/T_2}}$; (b) $\mathbf{0{,}223}$; (c) $\mathbf{t>2{,}30\,T_2}$.
*Fizycznie:* zanik jest wykładniczy, więc o „dobrej” koherencji decyduje $T_2$, a nie chwilowa
amplituda szumu.

## Z-18.6

(a) Kanał depolaryzujący skaluje wektor Blocha każdego kubita przez $(1-p)$, więc korelacje
$E(a,b)\to(1-p)E(a,b)$, a dla optymalnych kątów $S(p)=2\sqrt2\,(1-p)$.
(b) $S(p)=2\Rightarrow1-p=\tfrac{1}{\sqrt2}\Rightarrow p=1-\tfrac{1}{\sqrt2}=0{,}2929$.
(c) Próg splątania stanu Wernera to $p>\tfrac13=0{,}333$ (bo $\lambda_{\Phi^+}>\tfrac12$), a próg
naruszenia CHSH to $p>0{,}7071$. Próg zepsucia CHSH ($0{,}293$) jest więc **niższy** niż próg utraty
splątania ($0{,}333$) — można mieć splątanie bez naruszenia nierówności Bella.

**Odpowiedź:** (a) $\mathbf{S(p)=2\sqrt2(1-p)}$; (b) $\mathbf{p=0{,}293}$; (c) CHSH psuje się
wcześniej niż samo splątanie.
*Fizycznie:* „mieć splątanie” i „naruszać Bella” to dwie różne własności stanu.

## Z-18.7

(a) Nierówność CKW: $C^2_{AB}+C^2_{AC}\le C^2_{A(BC)}$ (tzw. monogamia splątania).
(b) Dla $\lvert W\rangle=\tfrac{1}{\sqrt3}(\lvert001\rangle+\lvert010\rangle+\lvert100\rangle)$:
$\tau_{AB}=C_{AB}^2=\tfrac49$, $\tau_{AC}=\tfrac49$, a
$\tau_{A(BC)}=C^2_{A(BC)}=2\big(1-\mathrm{Tr}\rho_A^2\big)=4\lambda_1\lambda_2 =4\cdot\tfrac23\cdot\tfrac13=\tfrac89$.
(c) $\tfrac49+\tfrac49=\tfrac89=\tau_{A(BC)}$ — nierówność jest **nasycona** (równość). Oznacza to,
że splątanie $A$ z $BC$ jest w całości „rozdzielone” między pary $AB$ i $AC$; w $\lvert\mathrm{GHZ}\rangle$
byłoby inaczej ($\tau_{AB}=\tau_{AC}=0$, $\tau_{A(BC)}=1$).

**Odpowiedź:** (b) $\mathbf{\tau_{AB}=\tau_{AC}=\tfrac49}$, $\mathbf{\tau_{A(BC)}=\tfrac89}$;
(c) CKW **nasycona** — splątanie „podzielone” między pary.
*Fizycznie:* monogamia to ilościowe ograniczenie na rozkład splątania w układzie wieloczęściowym
(podstawa bezpieczeństwa QKD).

## Z-18.8

(a) $Q_{\min}=k_BT\ln2$: dla $T=300$ K
$Q=1{,}380649\cdot10^{-23}\cdot300\cdot0{,}6931=2{,}871\cdot10^{-21}$ J $=0{,}0179$ eV; dla $T=4$ K
$Q=1{,}380649\cdot10^{-23}\cdot4\cdot0{,}6931=3{,}828\cdot10^{-23}$ J.
(b) $10^9$ bitów w $300$ K: $10^9\cdot2{,}871\cdot10^{-21}=2{,}871\cdot10^{-12}$ J.
(c) Komputery kwantowe działają w kriogenice ($T\approx10$ mK–$4$ K), gdzie $kT\ln2$ jest maleńkie,
ale zasada Landauera obowiązuje **zawsze**: kasowanie bitów, chłodzenie i korekcja błędów odprowadzają
ciepło do otoczenia, więc bilans entropii całego układu (komputer + kriostat) nie maleje.

**Odpowiedź:** (a) $\mathbf{2{,}87\cdot10^{-21}}$ **J** ($300$ K), $\mathbf{3{,}83\cdot10^{-23}}$ **J**
($4$ K); (b) $\mathbf{2{,}87\cdot10^{-12}}$ **J**; (c) zasada obowiązuje, uwzględniając cały układ.
*Fizycznie:* chłodzenie nie „omija” drugiej zasady — przenosi entropię do otoczenia, płacąc pracą.
