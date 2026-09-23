# Słownik pojęć PL–EN

Terminy używane w przewodniku i na Olimpiadzie. Kolumna „PL” to termin polski
(używany w tym repo), „EN” — angielski (przydatny przy czytaniu literatury i
dokumentacji bibliotek).

## Podstawy

| PL | EN | Uwaga |
| --- | --- | --- |
| kubit | qubit | kwantowy odpowiednik bitu |
| stan | state | $\lvert\psi\rangle$ |
| amplituda | amplitude | $c_k$, zespolona |
| faza globalna | global phase | nieobserwowalna |
| faza względna | relative phase | obserwowalna (interferencja) |
| superpozycja | superposition | $\alpha\lvert0\rangle+\beta\lvert1\rangle$ |
| pomiar | measurement | rzutowy (projekcyjny)/POVM |
| wartość oczekiwana | expectation value | $\langle A\rangle$ |
| wariancja | variance | $\mathrm{Var}(A)$ |
| normalizacja | normalization | $\langle\psi\vert\psi\rangle=1$ |
| ortogonalność | orthogonality | $\langle\phi\vert\psi\rangle=0$ |
| iloczyn tensorowy | tensor product | $\otimes$ |
| operator unitarny | unitary operator | $U^\dagger U=I$ |
| operator hermitowski | Hermitian operator | $A^\dagger=A$ (obserwabla) |
| rzut | projector / projection | $\lvert m\rangle\langle m\rvert$ |
| baza obliczeniowa | computational basis | $\{\lvert0\rangle,\lvert1\rangle\}$ |

## Informatyka kwantowa

| PL | EN | Uwaga |
| --- | --- | --- |
| bramka | gate | operacja unitarna |
| obwód kwantowy | quantum circuit | sekwencja bramek |
| brama kontrolowana | controlled gate | CNOT, CZ, $C_U$ |
| zbiór uniwersalny | universal gate set | np. $\{H,T,\text{CNOT}\}$ |
| splątanie | entanglement | nie-lokalny zasób |
| stan Bella | Bell state | 4 stany maks. splątane |
| nierówność Bella | Bell inequality | CHSH to jej postać |
| zmienne ukryte | hidden variables | model lokalny-realistyczny |
| teleportacja kwantowa | quantum teleportation | 1 e-bit + 2 bity klasyczne |
| supergęste kodowanie | superdense coding | 2 bity w 1 kubicie |
| zakaz klonowania | no-cloning theorem | nie da się skopiować |
| dekoherencja | decoherence | utrata koherencji |
| wierność | fidelity | $F(\rho,\sigma)$ |
| dystans śladowy | trace distance | $D(\rho,\sigma)$ |
| macierz gęstości | density matrix | $\rho$ |
| stan mieszany | mixed state | $\mathrm{Tr}\rho^2<1$ |
| ślad częściowy | partial trace | $\mathrm{Tr}_B$ |
| rozkład Schmidta | Schmidt decomposition | miara splątania |
| concurrence | concurrence | 2 kubity |
| negatywność | negativity | miara splątania |
| kanał kwantowy | quantum channel | opis dekoherencji |
| reprezentacja Krausa | Kraus representation | operator sum |
| POVM | POVM | pomiar uogólniony |
| entropia von Neumanna | von Neumann entropy | $S(\rho)$ |
| informacja Fishera | Fisher information | metrologia |
| granica śrutowa | shot-noise limit | $1/\sqrt N$ |
| granica Heisenberga | Heisenberg limit | $1/N$ |
| wyrocznia | oracle | czarna skrzynka w algorytmach |
| przyspieszenie kwantowe | quantum speedup | np. Grover $\sqrt N$ |
| kwantowa przewaga | quantum advantage | empiryczna supremacja |
| odporność na błędy | fault tolerance | próg błędu |

## Kryptografia i protokoły

| PL | EN | Uwaga |
| --- | --- | --- |
| wymiana klucza | key distribution (QKD) | BB84, E91 |
| podsłuch | eavesdropping | Eve |
| współczynnik błędów | QBER | próg ≈ 11% |
| przesiewanie | sifting | uzgadnianie baz |
| uzgadnianie klucza | key reconciliation | korekcja błędów klucza |
| wzmocnienie prywatności | privacy amplification | skracanie klucza |
| szyfr jednorazowy | one-time pad | Vernam |
| kryptografia postkwantowa | post-quantum cryptography (PQC) | matematyka klasyczna |

## Sprzęt i inżynieria

| PL | EN | Uwaga |
| --- | --- | --- |
| kubit nadprzewodzący | superconducting qubit | transmon |
| jony w pułapce | trapped ions | np. $^{171}\text{Yb}^+$ |
| atomy neutralne | neutral atoms | pęsety optyczne |
| kubit topologiczny | topological qubit | anyony |
| czas relaksacji | $T_1$ | zanik populacji |
| czas koherencji fazy | $T_2$ | zanik fazy |
| wierność bramki | gate fidelity | jakość operacji |
| łączność | connectivity | topologia sprzętu |
| transpilacja | transpilation | dopasowanie do sprzętu |
| korekcja błędów | error correction (QEC) | kod powierzchniowy |
| mitygacja błędów | error mitigation | ZNE, twirling |
| syndrom | syndrome | objaw błędu |
| próg korekcji | threshold | $\sim0{,}1\%$–$1\%$ |
| kryteria DiVincenzo | DiVincenzo criteria | warunki budowy komputera |

## Narzędzia

| PL | EN | Uwaga |
| --- | --- | --- |
| symulator stanu | statevector simulator | $2^n$ amplitud |
| symulator macierzy gęstości | density-matrix simulator | obsługuje szum |
| sieć tensorowa | tensor network | efektywne symulacje |
| liczba pomiarów | shots | statystyka wyników |
| kalibracja | calibration | macierz błędów odczytu |
| dekompozycja bramki | gate decomposition | np. $C_U$ z CNOT |
| optymalizacja poziomu | optimization level | w Qiskit |
