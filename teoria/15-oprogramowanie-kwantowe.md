# 15. Oprogramowanie kwantowe


## 1. Zakres rozdziału

Rozdział obejmuje oprogramowanie kwantowe: pisanie obwodów w SDK (Qiskit, Cirq, PennyLane, Braket,
Q#, QuTiP, ProjectQ), zapis obwodu w QASM 2 i QASM 3, transpilację na bramki natywne i łączność
urządzenia oraz typy symulatorów (statevector, macierz gęstości, sieci tensorowe, z modelem szumu).
Omawia shoty i liczniki, layout, pomiar pośredni i sterowanie klasyczne, mitygację w SDK (ZNE,
twirling, M3, `resilience_level`), algorytmy wariacyjne (VQE, QAOA) oraz budowę własnego
symulatora stanu.

Materiał dotyczy zadań Z-15 (obwód Bella, QASM, transpilacja, symulatory, prawdziwy sprzęt, VQE)
i stanowi narzędzie weryfikacji rachunków z rozdziałów 06–13; teorię algorytmów wariacyjnych
rozwija rozdział 19.

Qiskit i Cirq zmieniają API co kilka wersji (`execute` zniknęło, primitives zastąpiły
`backend.run`); zgodność kodu zależy od wersji biblioteki (`pip show qiskit`) i jej dokumentacji.

## 2. Najważniejsze definicje

- **SDK kwantowe**: biblioteka do budowy i uruchamiania obwodów — **Qiskit** (IBM), **Cirq**
  (Google), **PennyLane** (Xanadu, obwody różniczkowalne), **Braket** (AWS), **Q#** (Microsoft,
  własny język), **QuTiP** (układy otwarte), **ProjectQ** (kompilator, ETH).
- **QASM**: tekstowy format obwodu: **QASM 2** (`qreg`/`creg`), **QASM 3** (typy, wyrażenia,
  sterowanie klasyczne w czasie rzeczywistym).
- **Transpilacja**: przełożenie obwodu logicznego na obwód z **bramek natywnych** i zgodny
  z **łącznością** urządzenia (rozdział 12).
- **Bramka natywna** i **dekompozycja**: np. `RZ`, `SX`, `ECR` (IBM), `CZ`, `√X` (Google), `MS`
  (jony); bramka $H$ to na takim sprzęcie `rz(pi/2) sx rz(pi/2)`.
- **Poziom optymalizacji** (`optimization_level=0..3`): jak agresywnie transpilator skraca obwód.
- **Symulator statevector** (wektor $2^n$), **macierzy gęstości** (macierz $4^n$), **sieci
  tensorowych** (graf, dobry przy małym splątaniu), **z modelem szumu** (kanały błędów).
- **Shot**: jedno powtórzenie pomiaru; z $n$ shotów dostajemy **liczniki** (*counts*) i histogram.
- **Layout (mapowanie logiczne→fizyczne)**: które kubity fizyczne pełnią role logicznych;
  ustala je transpilator.
- **Pomiar pośredni / sterowanie klasyczne**: instrukcje warunkowe (np. „jeśli wynik 1, zastosuj $X$”).
- **Mitygacja w SDK**: ZNE, twirling, M3 (korekcja odczytu); w Qiskit Runtime — `resilience_level`.
- **VQE / QAOA**: algorytmy **wariacyjne**: obwód z parametrami $\vec\theta$ + klasyczny
  optymalizator minimalizujący $\langle H\rangle$.

## 3. Teoria krok po kroku

### 3.1 SDK i ekosystemy

| SDK | Producent | Mocna strona |
| --- | --- | --- |
| **Qiskit** | IBM | cały ekosystem: symulatory, chmura, primitives |
| **Cirq** | Google | elastyczne bramki, symulatory w Pythonie |
| **PennyLane** | Xanadu | różniczkowanie obwodów, uczenie maszynowe (QML) |
| **Amazon Braket** | AWS | dostęp do wielu urządzeń w jednym API |
| **Q#** | Microsoft | własny język + estymator zasobów |
| **QuTiP / ProjectQ** | open source | układy otwarte i kanały / kompilacja i redukcja zasobów |

Wszystkie biblioteki działają na tej samej konwencji: **$n$ kubitów $\to$ bramki $\to$ pomiar
$\to$ rozkład wyników**; różnią się składnią i tym, do czego są przywiązane (PennyLane pod gradienty).

```python
from qiskit import QuantumCircuit                              # Qiskit
qc = QuantumCircuit(2); qc.h(0); qc.cx(0, 1); qc.measure_all()

import cirq                                                     # Cirq
q0, q1 = cirq.LineQubit.range(2)
circuit = cirq.Circuit(cirq.H(q0), cirq.CNOT(q0, q1), cirq.measure(q0, q1, key="m"))

import pennylane as qml                                         # PennyLane
@qml.qnode(qml.device("default.qubit", wires=2))
def bell_probs():
    qml.Hadamard(wires=0); qml.CNOT(wires=[0, 1]); return qml.probs(wires=[0, 1])
```

### 3.2 QASM 2 i QASM 3 — wymiana obwodów między narzędziami

**QASM 2** (OpenQASM 2.0, `qreg`/`creg`) i **QASM 3** (typy, wyrażenia, sterowanie klasyczne):

```
OPENQASM 2.0;                        OPENQASM 3.0;
include "qelib1.inc";                include "stdgates.inc";
qreg q[2];                           qubit[2] q;  bit[2] c;
creg c[2];                           h q[0];
h q[0];                              cx q[0], q[1];
cx q[0],q[1];                        c = measure q;
measure q -> c;
```

W Qiskit 1.x eksport to `qc.qasm()`; w 2.x używa się modułów `qiskit.qasm2`/`qiskit.qasm3`
(np. `qasm3.dumps(qc)`), a import — `QuantumCircuit.from_qasm_str(...)`. Uwaga na **kolejność
kubitów**: `q[0]` jest (w konwencji tego repozytorium i w Qiskitcie) najmłodszym bitem, ale część
podręczników używa odwrotnej konwencji — **zawsze sprawdź ją na obwodzie `x q[0]`**.

### 3.3 Budowa obwodu w kodzie

```python
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

qc = QuantumCircuit(2)
qc.h(0)                     # Hadamard na q0
qc.cx(0, 1)                 # CNOT: kontrola q0, cel q1 -> stan Bella
qc.rz(0.7, 1)               # R_Z(0.7): argument to KĄT (macierz ma theta/2 - konwencja repo)
qc.ry(np.pi/2, 0)
print(qc.draw())            # tekstowy rysunek obwodu

sv = Statevector.from_instruction(qc)          # dokładny stan, bez shotów
print(sv.probabilities_dict(), sv.expectation_value("ZZ"))

qc_meas = qc.copy(); qc_meas.measure_all()
from qiskit.primitives import StatevectorSampler
counts = StatevectorSampler(seed=42).run([qc_meas], shots=1024).result()[0].data.meas.get_counts()
print(counts)               # np. {'00': 505, '11': 519}
```

Trzy rzeczy do zapamiętania: (1) bramki stosuje się w kolejności zapisu, a macierz obwodu jest
iloczynem od prawej; (2) `Statevector.from_instruction` daje dokładny stan, więc na symulatorze
shoty nie są potrzebne; (3) pomiar trzeba dodać jawnie, a wynik jest losowy — dlatego ustawiamy
ziarno (`seed`), żeby praca była powtarzalna.

### 3.4 Bramki natywne, transpilacja i optymalizacja

Twoje `h`, `cx`, `rz` to bramki *logiczne*. Sprzęt wykonuje **bramki natywne** i to tylko
między sąsiadami w swojej topologii. Transpilator robi trzy rzeczy: (1) rozkłada bramki na
natywne, (2) wybiera **layout** (które kubity fizyczne pełnią role logicznych), (3) wstawia
SWAP-y, gdy trzeba przenieść informację (rozdział 12, sekcja 3.9).

```python
from qiskit_aer import AerSimulator
backend = AerSimulator()                       # albo backend z chmury
isa = transpile(qc, backend=backend, optimization_level=3, seed_transpiler=42)
print(isa.count_ops())        # np. {'rz': 4, 'sx': 3, 'cx': 1}
```

- `optimization_level=0` — tylko odwzorowanie na sprzęt; `=3` — agresywne upraszczanie
  (sklejanie obrotów, kasowanie par odwrotnych bramek).
- **Koszt transpilacji** mierzymy liczbą bramek dwukubitowych: to one wnoszą dominujący błąd;
  zawsze porównaj `count_ops()` przed i po transpilacji.
- Gdy sprzęt nie ma bramki $H$, transpilator użyje `rz(pi/2) sx rz(pi/2)`; bramki kontrolowane
  (`crz`, `mcx`) dekomponują się na CNOT-y i obroty, a dla `mcx` koszt rośnie liniowo z liczbą kontroli.

### 3.5 Symulatory

| Symulator | Reprezentacja | Kiedy używać | Granica praktyczna |
| --- | --- | --- | --- |
| statevector | wektor $2^n$ | brak szumu, dokładne amplitudy | $\approx30$ kubitów |
| macierz gęstości | $\rho$, $4^n$ elementów | szum, stany mieszane, kanały | $\approx15$ kubitów |
| sieci tensorowe | graf | mało splątania, obwody 1D | głębokie splątanie = wolno |
| z modelem szumu | wektor/macierz + kanały | testy mitygacji i kalibracji | jak wyżej, wolniej |

```python
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error

noise = NoiseModel()
noise.add_all_qubit_quantum_error(depolarizing_error(0.01, 1), ["h", "rz", "sx"])
noisy = AerSimulator(noise_model=noise)          # symulacja z szumem 1%
dm    = AerSimulator(method="density_matrix")    # macierz gęstości
```

Różnica między symulatorem idealnym a symulatorem szumu jest w praktyce najważniejsza: pierwszy
odpowiada na pytanie „czy obwód jest poprawny?”, drugi — „czy zadziała na takim sprzęcie?”.

### 3.6 Prawdziwy sprzęt: kolejki, shoty, kalibracja

Na prawdziwym urządzeniu nie ma stanu dokładnego — są **liczniki** z $n$ shotów, obarczone
szumem, a obwód trzeba przetranspilować na **bramki natywne i layout** tego konkretnego
urządzenia. Przykład (Qiskit Runtime; nazwy usług i kanałów zmieniają się między wersjami —
sprawdź dokumentację):

```python
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2
from qiskit import transpile

service = QiskitRuntimeService(channel="ibm_quantum_platform")
backend = service.least_busy(operational=True, simulator=False)
print(backend.name, backend.num_qubits)

isa = transpile(qc_meas, backend=backend, optimization_level=3, seed_transpiler=42)
sampler = SamplerV2(mode=backend)
job = sampler.run([isa], shots=4096)
print(job.job_id())                                     # identyfikator do raportu!
counts = job.result()[0].data.meas.get_counts()
```

O co zadbać: **kolejka** (zadanie czeka — wysyłaj z zapasem czasu), **shots** (błąd statystyczny
$\sim1/\sqrt n$, rozdział 03), **kalibracja** (parametry dryfują, więc dwie sesje dają różne
wyniki — rozdział 12) oraz **raportowanie**: nazwa backendu, liczba shotów, identyfikator zadania,
data, poziom optymalizacji i użyta mitygacja (warunek powtarzalności, rozdział 14).

### 3.7 Odczyt wyników, histogramy, statystyka szumu i mitygacja

Liczniki zamieniamy na prawdopodobieństwa, dzieląc przez liczbę shotów, a niepewność szacujemy
jak dla rozkładu dwumianowego (rozdział 03):

$$p_i=\frac{n_i}{n}, \qquad \Delta p_i=\sqrt{\frac{p_i(1-p_i)}{n}} .$$

Dla `{'00': 505, '11': 519}` (n = 1024) mamy $p_{00}=0{,}493\pm0{,}016$ i $p_{11}=0{,}507\pm0{,}016$ —
oba zgodne z idealnym $\tfrac12$ w granicach błędu statystycznego.

- **Wartość oczekiwana z liczników:** $\langle Z_0Z_1\rangle=\frac{n_{00}+n_{11}-n_{01}-n_{10}}{n}$,
  a $\langle Z\rangle=\frac{n_0-n_1}{n}$.
- **Pomiar w innej bazie:** dla $\langle X\rangle$ dodaj $H$ przed pomiarem (bo $HZH=X$), dla
  $\langle Y\rangle$ — $S^\dagger$ i $H$; pomiar w $Z$ nie zmierzy $X$.
- **Porównanie z ideałem:** total variation distance $D=\tfrac12\sum_i\lvert p_i^{\rm exp}-p_i^{\rm ideal}\rvert$;
  dla $n$ shotów oczekujemy $D\sim1/\sqrt n$, więc $D$ wyraźnie większe oznacza szum lub błąd obwodu.
- **Mitygacja w SDK** (rozdział 13): ZNE, twirling, M3. W Qiskit Runtime wybiera się je przez
  `resilience_level` lub osobno w opcjach primitives; `qiskit-experiments` ma gotowe protokoły.

### 3.8 VQE i QAOA — pierwsze algorytmy wariacyjne

**Zasada wariacyjna:** dla dowolnego stanu $\lvert\psi(\vec\theta)\rangle$

$$\langle\psi(\vec\theta)\rvert H\lvert\psi(\vec\theta)\rangle\ \ge\ E_0 ,$$

więc minimalizując energię po parametrach obwodu, zbliżamy się do **energii stanu podstawowego**.
Schemat VQE (*variational quantum eigensolver*): obwód z parametrami (ansatz) $\to$ pomiar
wartości oczekiwanych $\to$ klasyczny optymalizator (COBYLA, SPSA, gradienty) $\to$ nowe parametry.

```python
import numpy as np
from scipy.optimize import minimize
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, SparsePauliOp

H = SparsePauliOp.from_list([("XX", 1.0), ("ZZ", 1.0)])   # H = X0X1 + Z0Z1

def energy(theta):
    qc = QuantumCircuit(2)
    qc.ry(theta[0], 0); qc.ry(theta[1], 1); qc.cx(0, 1)
    qc.ry(theta[2], 0); qc.ry(theta[3], 1)      # ansatz 4-parametrowy
    return float(np.real(Statevector.from_instruction(qc).expectation_value(H)))

res = minimize(energy, x0=np.zeros(4), method="COBYLA")
print(round(res.fun, 6), res.x)      # -2.0 ... prawidłowa energia stanu podstawowego
```

Liczby do zapamiętania: widmo $H=X_0X_1+Z_0Z_1$ to $\{-2,0,0,2\}$, więc $E_0=-2$ (stan
$\frac{1}{\sqrt2}(\lvert01\rangle-\lvert10\rangle)$). Powyższy 4-parametrowy ansatz **osiąga**
$-2{,}0000$; gdybyśmy zostawili tylko `ry,ry,cx` (2 parametry), doszlibyśmy najwyżej do $-1$, bo
taki obwód nigdy nie wytworzy amplitudy na $\lvert10\rangle$ — to najważniejsza lekcja o VQE:
**ansatz musi umieć wyrazić stan podstawowy**.

**QAOA** (alternating operator ansatz) to szczególny przypadek dla problemów optymalizacyjnych
(np. MaxCut): warstwy „kosztu” $e^{-i\gamma H_C}$ i „mieszania” $e^{-i\beta H_B}$ przeplatane
$p$ razy. Więcej teorii, w tym granice jakości przybliżenia: [rozdział 19](19-ponad-program-algorytmy-zaawansowane-i-granice.md).

### 3.9 Własny (minimalny) symulator

Napisz własny symulator, żeby zrozumieć, co robi biblioteka — i bo takie zadania pojawiają się
w finale. Potrzebne są tylko trzy elementy: macierze bramek, `np.kron` do ich złożenia i reguła
Borna. Szkielet (pełna wersja: `kod/simulator.py`, rozdział 06):

```python
import numpy as np
I = np.eye(2); X = np.array([[0, 1], [1, 0]]); H = np.array([[1, 1], [1, -1]])/np.sqrt(2)

def op_on(i, g, n):                      # bramka g na kubicie i (0 = najmłodszy bit)
    mats = [I]*n; mats[n - 1 - i] = g
    M = np.array([[1.0]])
    for m in mats: M = np.kron(M, m)
    return M

def run(circuit, n):                     # circuit = [(bramka, kubit), ...]
    psi = np.zeros(2**n, dtype=complex); psi[0] = 1.0
    for g, i in circuit: psi = op_on(i, g, n) @ psi
    return psi

psi = run([(H, 0), (X, 1)], 2)           # H na q0 i X na q1
print(np.round(np.abs(psi)**2, 3))       # prawdopodobieństwa: [0 0 0.5 0.5]
```

Taki symulator obsłuży 10–20 kubitów, a jego rozszerzenie o szum (macierze Krausa, rozdział 17)
i o statystyczne pomiary to już pełnoprawne narzędzie badawcze.

## 4. Przykłady rozwiązane

### Przykład 15.1 (łatwy): obwód Bella na symulatorze

**Dane:** `qc = H(0); CX(0,1)`, start $\lvert00\rangle$, $n=1024$ shoty.
**Rachunek (ręczny):** $H\lvert0\rangle=\lvert+\rangle$, po CNOT otrzymujemy
$\lvert\Phi^+\rangle=\frac{1}{\sqrt2}(\lvert00\rangle+\lvert11\rangle)$. Zatem
$p_{00}=p_{11}=\tfrac12$, $p_{01}=p_{10}=0$ oraz

$$\langle ZZ\rangle=\tfrac12(+1)+\tfrac12(+1)=1,\qquad \langle XX\rangle=1,\qquad \langle Z\otimes I\rangle=0 .$$

**Symulacja (kod z 3.3):** `sv.probabilities_dict()` daje `{'00': 0.5, '11': 0.5}`,
`sv.expectation_value("ZZ")` daje `1.0`, a liczniki: `{'00': 505, '11': 519}`.
Niepewność statystyczna: $\Delta p=\sqrt{0{,}5\cdot0{,}5/1024}=0{,}0156$, a zmierzona częstość
$505/1024=0{,}493$ zgadza się z $\tfrac12$ w granicach $1\sigma$.

**Odpowiedź:** $p_{00}=p_{11}=\mathbf{0{,}5}$, $\langle ZZ\rangle=\mathbf{1}$, liczniki
$\mathbf{505{:}519}$ zgodne z ideałem w granicach $\pm0{,}016$.
*Interpretacja:* na symulatorze bez szumu wartości oczekiwane są dokładne (bez shotów), a
liczniki różnią się od ideału **wyłącznie** statystycznie — to odniesienie dla każdego
eksperymentu na prawdziwym sprzęcie.

### Przykład 15.2 (trudniejszy): koszt transpilacji

**Dane:** obwód 3-kubitowy z jedną bramką CNOT między $q_0$ i $q_2$; sprzęt o topologii linii
$q_0-q_1-q_2$; wierność bramki dwukubitowej $99{,}7\%$.
**Rachunek:** w linii odległość między $q_0$ i $q_2$ wynosi $2$, więc transpilator wstawia
$2$ SWAP-y, a każdy SWAP to $3$ CNOT:

$$2\cdot3=6\ \text{CNOT}\ \text{zamiast }1 .$$

Wierność „transportu”: $0{,}997^{6}=0{,}982$ — samo **przeniesienie** kubita kosztuje prawie
$2$ punkty procentowe wierności. Gdyby obwód miał $50$ takich bramek ($300$ CNOT), wierność
spadłaby do $0{,}997^{300}=0{,}406$ zamiast $0{,}997^{50}=0{,}861$ przy idealnej łączności.

**Odpowiedź:** transpilacja kosztuje $\mathbf{6}$ CNOT na jedną daleką bramkę (6-krotny wzrost),
przez co wierność obwodu z $50$ takimi bramkami spada z $\mathbf{0{,}861}$ do $\mathbf{0{,}406}$.
*Interpretacja:* „koszt transpilacji” to nie abstrakcja — to bezpośrednia strata wierności;
dlatego obwody pisze się pod topologię sprzętu (rozdział 12, sekcja 3.9).

## 5. Typowe pułapki (błędy początkujących)

1. **Brak pomiaru.** Obwód bez `measure_all()` uruchomiony z shotami „zwraca” stan $0$ — pomiar nie dzieje się sam.
2. **Odwrócona kolejność bitów.** Wynik `01` w Qiskitcie to $q_1=0$, $q_0=1$; sprawdź to na obwodzie `x(0)`, zamiast zgadywać.
3. **Pomiar w złej bazie.** Aby otrzymać $\langle X\rangle$, dodaj $H$ przed pomiarem ($HZH=X$); pomiar w $Z$ nie zmierzy $X$.
4. **Brak ziarna i porównywanie po różnej transpilacji.** `optimization_level` i `seed_transpiler` zmieniają obwód; bez nich wynik nie jest powtarzalny.
5. **Wnioski z symulatora idealnego.** Obwód o głębokości $200$ bramek „działa” bez szumu, a na sprzęcie daje szum — testuj też symulatorem z modelem szumu.
6. **Mylenie shotów z kubitami i pojedynczy shot jako odpowiedź.** `shots=4096` to liczba powtórzeń, a jeden wynik to nie wartość oczekiwana (rozdział 06); podawaj niepewność.

## 6. Zadania (Z-15)

**Z-15.1.** Obwód Bella. (a) Napisz kod Qiskit tworzący $\lvert\Phi^+\rangle$ i podaj rozkład prawdopodobieństw. (b) Policz $\langle ZZ\rangle$, $\langle XX\rangle$, $\langle Z\otimes I\rangle$ ręcznie i porównaj z symulatorem. (c) Ile shotów potrzeba, by wyznaczyć $p_{00}$ z dokładnością $0{,}01$?

**Z-15.2.** QASM. (a) Zapisz obwód Bella w QASM 2 i QASM 3. (b) Wyjaśnij różnicę w zapisie pomiaru. (c) Dlaczego przy wymianie obwodów między SDK trzeba sprawdzić kolejność kubitów — podaj test.

**Z-15.3.** Transpilacja. (a) Podaj liczbę CNOT-ów dla bramki między $q_0$ i $q_4$ na linii $5$-kubitowej. (b) Policz wierność takiej bramki przy $F_{\rm CNOT}=99{,}7\%$. (c) Porównaj `optimization_level=0` i `3`: co zmienia się w `count_ops()` i dlaczego to ma znaczenie dla wierności?

**Z-15.4.** Symulatory. (a) Wymień trzy typy symulatorów i ich granice praktyczne. (b) Dlaczego macierz gęstości obsłuży mniej kubitów niż wektor stanu? (c) Kiedy symulator sieci tensorowych wygrywa, a kiedy przegrywa?

**Z-15.5.** Prawdziwy sprzęt. (a) Opisz kolejność kroków od obwodu do histogramu. (b) Jak raportować wyniki (podaj pięć elementów). (c) Dlaczego ten sam obwód wysłany dwa razy daje inne liczniki?

**Z-15.6. [★]** VQE. (a) Wyjaśnij zasadę wariacyjną i rolę ansatzu. (b) Dla $H=X_0X_1+Z_0Z_1$ podaj $E_0$ i uzasadnij, dlaczego ansatz `ry,ry,cx` nie wystarczy. (c) Co się stanie, gdy ansatz jest za głęboki (barren plateaus)?

## 7. Wskazówki do zadań

- **Z-15.1.** (b) użyj $\lvert\Phi^+\rangle$ i reguły Borna; (c) $\Delta p=\sqrt{p(1-p)/n}\le0{,}01$.
- **Z-15.2.** (a) patrz 3.2; (c) test na `x q[0]`.
- **Z-15.3.** (a) $d$ SWAP-ów po $3$ CNOT-y; (b) $F^n$; (c) sprawdź liczbę bramek dwukubitowych.
- **Z-15.4–15.5.** (a) patrz 3.5 i 3.6; licz pamięć $2^n$ vs $4^n$.
- **Z-15.6.** (b) widmo $H$ z 3.8 i amplituda na $\lvert10\rangle$; (c) gradienty znikają wykładniczo.

## 8. Co dalej

- **Algorytmy zaawansowane i granice** — [rozdział 19](19-ponad-program-algorytmy-zaawansowane-i-granice.md): QAOA, tw. Holevo, zasoby.
- **Korekcja i mitygacja** — [rozdział 13](13-korekcja-i-mitygacja-bledow.md): od ZNE do kodów powierzchniowych.
- **Analiza danych** — [rozdział 16](16-analiza-danych-i-obliczenia-naukowe.md): histogramy, dopasowania, testy.
- Własny symulator do porównań: `python kod/simulator.py`; pełna weryfikacja: `python kod/verify_all.py`.
- Pełne rozwiązania: [rozwiazania-15.md](../zadania/rozwiazania/rozwiazania-15.md); praca domowa: [PD-3](../praca-domowa/praca-domowa-03.md).




