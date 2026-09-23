"""Minimalny symulator obwodów kwantowych (NumPy).

Konwencje (zgodne z dokumentacją repo):
  * kolejność kubitów małoendianowa: stan |q_{n-1}...q_1 q_0> ma indeks
    q_0 + 2*q_1 + ... + 2^(n-1)*q_{n-1},
  * wektor stanu to tablica o kształcie (2**n,),
  * bramka jednokubitowa G na kubicie `k` to operator
    I^{(x)2^k} (x) G (x) I^{(x)2^(n-1-k)}.

Uruchomienie:
    python kod/simulator.py
"""

from __future__ import annotations

import sys

import numpy as np

if hasattr(sys.stdout, "reconfigure"):     # Windows: konsola bywa w cp1252
    sys.stdout.reconfigure(encoding="utf-8")

# ---------------------------------------------------------------- bramki 1 kubit
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
H = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
S = np.diag([1, 1j]).astype(complex)
T = np.diag([1, np.exp(1j * np.pi / 4)]).astype(complex)


def R_x(theta: float) -> np.ndarray:
    """Obrót wokół osi X o kąt theta (macierz z theta/2)."""
    c, s = np.cos(theta / 2), np.sin(theta / 2)
    return np.array([[c, -1j * s], [-1j * s, c]], dtype=complex)


def R_y(theta: float) -> np.ndarray:
    """Obrót wokół osi Y o kąt theta (macierz z theta/2)."""
    c, s = np.cos(theta / 2), np.sin(theta / 2)
    return np.array([[c, -s], [s, c]], dtype=complex)


def R_z(theta: float) -> np.ndarray:
    """Obrót wokół osi Z o kąt theta (macierz z theta/2)."""
    return np.diag([np.exp(-1j * theta / 2), np.exp(1j * theta / 2)]).astype(complex)


GATES_1Q = {"I": I2, "X": X, "Y": Y, "Z": Z, "H": H, "S": S, "T": T}


def kron_power(mat: np.ndarray, power: int) -> np.ndarray:
    """Iloczyn tensorowy `power` kopii macierzy (power=0 -> [[1]])."""
    out = np.ones((1, 1), dtype=complex)
    for _ in range(power):
        out = np.kron(out, mat)
    return out


# ---------------------------------------------------------------- stan i bramki
def zero_state(n_qubits: int) -> np.ndarray:
    """Stan |00...0> dla `n_qubits` kubitów."""
    psi = np.zeros(2 ** n_qubits, dtype=complex)
    psi[0] = 1.0
    return psi


def basis_state(n_qubits: int, index: int) -> np.ndarray:
    """Stan bazowy |index> (index = suma q_k * 2^k)."""
    psi = np.zeros(2 ** n_qubits, dtype=complex)
    psi[index] = 1.0
    return psi


def apply_1q(psi: np.ndarray, gate: np.ndarray, qubit: int, n_qubits: int) -> np.ndarray:
    """Zastosuj bramkę `gate` na kubicie `qubit` do stanu `psi`.

    Konwencja małoendianowa: indeks stanu to q_0 + 2*q_1 + ... , więc q_0 jest
    **najmłodszym** bitem i odpowiada **skrajnemu prawemu** czynnikowi w iloczynie
    tensorowym. Dlatego operator na kubicie `k` ma postać

        I^{(x)(n-1-k)} (x) G (x) I^{(x)k}

    (a nie odwrotnie — to najczęstsze źródło pomyłek w kodzie).
    """
    if not 0 <= qubit < n_qubits:
        raise ValueError(f"qubit {qubit} poza zakresem 0..{n_qubits - 1}")
    op = np.kron(
        kron_power(I2, n_qubits - 1 - qubit),
        np.kron(gate, kron_power(I2, qubit)),
    )
    return op @ psi


CNOT = np.array(
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], dtype=complex
)  # kontrola = kubit "starszy" (lewy) w zapisie |qc qt>, cel = "młodszy"


def apply_cnot(psi: np.ndarray, control: int, target: int, n_qubits: int) -> np.ndarray:
    """Bramka CNOT dla 2-kubitowego układu (kolejność małoendianowa).

    Dla dwoch kubitow: kontrola = kubit 1 (starszy), cel = kubit 0.
    Dla innych par podajemy permutacje indeksow przez skladanie SWAP-ow.
    """
    if n_qubits != 2:
        raise NotImplementedError("simulator obsluguje CNOT dla 2 kubitow")
    if (control, target) == (1, 0):
        return CNOT @ psi
    if (control, target) == (0, 1):
        swap = np.array(
            [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]], dtype=complex
        )
        return swap @ (CNOT @ (swap @ psi))
    raise ValueError("control i target musza byc rozne")


def apply_cz(psi: np.ndarray) -> np.ndarray:
    """Bramka CZ na dwoch kubitach (diag(1,1,1,-1))."""
    return np.diag([1, 1, 1, -1]).astype(complex) @ psi


# ---------------------------------------------------------------- pomiar i opisy
def probabilities(psi: np.ndarray) -> np.ndarray:
    """Rozkład prawdopodobieństw w bazie obliczeniowej."""
    return np.abs(psi) ** 2


def measure(psi: np.ndarray, shots: int = 1000, seed: int = 42) -> dict[str, int]:
    """Symulacja `shots` pomiarów w bazie obliczeniowej."""
    rng = np.random.default_rng(seed)
    p = probabilities(psi)
    p = p / p.sum()
    n = int(np.log2(len(psi)))
    idx = rng.choice(len(psi), size=shots, p=p)
    out: dict[str, int] = {}
    for i in idx:
        key = format(int(i), f"0{n}b")
        out[key] = out.get(key, 0) + 1
    return dict(sorted(out.items()))


def partial_trace_B(rho: np.ndarray) -> np.ndarray:
    """Ślad częściowy po drugim kubicie (B = kubit 0, młodszy)."""
    rho = rho.reshape(2, 2, 2, 2)  # (i1, i0, j1, j0)
    return np.einsum("ikjk->ij", rho)


def expectation(psi: np.ndarray, op: np.ndarray) -> complex:
    """Wartość oczekiwana <psi|op|psi>."""
    return complex(np.vdot(psi, op @ psi))


def ket_str(psi: np.ndarray, tol: float = 1e-9) -> str:
    """Czytelny zapis stanu jako kombinacji stanów bazowych."""
    n = int(np.log2(len(psi)))
    parts: list[str] = []
    for i, amp in enumerate(psi):
        if abs(amp) < tol:
            continue
        label = format(i, f"0{n}b")
        if abs(amp.imag) < tol:
            parts.append(f"{amp.real:+.4f}|{label}>")
        else:
            parts.append(f"({amp.real:+.4f}{amp.imag:+.4f}j)|{label}>")
    return " ".join(parts) if parts else "0"


def _test() -> None:
    # H|0> = |+>
    psi = apply_1q(zero_state(1), H, 0, 1)
    assert np.allclose(psi, np.array([1, 1], dtype=complex) / np.sqrt(2))
    # HZH = X
    assert np.allclose(H @ Z @ H, X)
    # X|0> = |1>
    assert np.allclose(apply_1q(zero_state(1), X, 0, 1), np.array([0, 1], dtype=complex))
    # H na GORNYM kubicie (q1) daje |+>|0> = (|00> + |10>)/sqrt(2) -> indeksy 0 i 2
    psi = apply_1q(zero_state(2), H, 1, 2)
    assert np.allclose(psi, (basis_state(2, 0) + basis_state(2, 2)) / np.sqrt(2))
    # H na DOLNYM kubicie (q0) daje |0>|+> = (|00> + |01>)/sqrt(2) -> indeksy 0 i 1
    psi = apply_1q(zero_state(2), H, 0, 2)
    assert np.allclose(psi, (basis_state(2, 0) + basis_state(2, 1)) / np.sqrt(2))
    # CNOT na |10> daje |11>
    psi = apply_cnot(basis_state(2, 2), control=1, target=0, n_qubits=2)
    assert np.allclose(psi, basis_state(2, 3))
    # Bell: H na q1 + CNOT -> (|00>+|11>)/sqrt(2)
    psi = apply_1q(zero_state(2), H, 1, 2)
    psi = apply_cnot(psi, control=1, target=0, n_qubits=2)
    bell = (basis_state(2, 0) + basis_state(2, 3)) / np.sqrt(2)
    assert np.allclose(psi, bell)
    # ślad częściowy stanu Bella daje I/2
    rho = np.outer(bell, bell.conj())
    rho_a = partial_trace_B(rho)
    assert np.allclose(rho_a, np.eye(2) / 2)
    # prawdopodobieństwa sumują się do 1
    assert abs(probabilities(bell).sum() - 1) < 1e-12
    # CNOT nie zmienia |++>
    plus_plus = np.ones(4, dtype=complex) / 2
    assert np.allclose(apply_cnot(plus_plus, 1, 0, 2), plus_plus)
    # test regresyjny zadania P4 (theta = 0.7 rad) w konwencji q1 = górny kubit
    th = 0.7
    psi = apply_1q(zero_state(2), H, 1, 2)
    psi = apply_1q(psi, R_y(th), 0, 2)
    psi = apply_cnot(psi, 1, 0, 2)
    assert np.allclose(probabilities(psi), [0.441211, 0.058789, 0.058789, 0.441211], atol=1e-6)
    zz = np.kron(Z, Z)
    assert abs(expectation(psi, zz).real - np.cos(th)) < 1e-12
    print("[OK] simulator.py: wszystkie testy wewnetrzne przeszly")


def main() -> None:
    print("Symulator obwodow kwantowych (NumPy), konwencja maloendianowa.")
    print("-" * 62)
    psi = apply_1q(zero_state(2), H, 1, 2)
    print("po H na q1:      ", ket_str(psi))
    psi = apply_1q(psi, R_y(0.7), 0, 2)
    print("po R_Y(0.7) q0:  ", ket_str(psi))
    psi = apply_cnot(psi, control=1, target=0, n_qubits=2)
    print("po CNOT:         ", ket_str(psi))
    print("prawdopodobienstwa:", np.round(probabilities(psi), 6))
    print("pomiary (1000 shots, seed=1):", measure(psi, 1000, seed=1))
    print("-" * 62)
    _test()


if __name__ == "__main__":
    main()

